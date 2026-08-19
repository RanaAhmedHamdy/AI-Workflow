#!/usr/bin/env python3
"""Bootstrap AI-Workflow assets into another repository.

Greenfield installs the reusable governance/policy/template scaffold and the
selected native platform skill pack. It seeds AI_CONTEXT.md and the decision
register from templates, but intentionally does not fabricate architecture,
feature, readiness, evidence, or release artifacts that require project facts
or owner decisions.

Brownfield installs the reusable repository-starter workflow, a composed
platform-aware AGENTS.md, the reusable checklist/template material, and the
applicable reusable skills. Project-specific manifests/checkpoints remain for
the receiving repository to create from evidence.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

GREEN_PACKAGE = "Greenfield_AI_Mobile_Governance_Package_v1_9_1"
BROWN_PACKAGE = "Brownfield_AI_Playbook_Reusable_Package_v4_4"


def _asset_root() -> Path:
    """Locate bundled assets in a source checkout or an installed tool environment."""
    source_root = Path(__file__).resolve().parents[2]
    if (source_root / GREEN_PACKAGE).is_dir() and (source_root / BROWN_PACKAGE).is_dir():
        return source_root

    installed_root = Path(sys.prefix) / "share" / "ai-workflow"
    if (installed_root / GREEN_PACKAGE).is_dir() and (installed_root / BROWN_PACKAGE).is_dir():
        return installed_root

    raise RuntimeError(
        "AI-Workflow package assets were not found. Reinstall the tool from the repository "
        "or run tools/install.py from a complete AI-Workflow checkout."
    )


ROOT = _asset_root()
GREEN_ROOT = ROOT / GREEN_PACKAGE
BROWN_ROOT = ROOT / BROWN_PACKAGE


@dataclass(frozen=True)
class Operation:
    dst: Path
    src: Path | None = None
    content: str | None = None
    label: str | None = None

    def describe_source(self) -> str:
        if self.label:
            return self.label
        if self.src is not None:
            try:
                return str(self.src.relative_to(ROOT))
            except ValueError:
                return str(self.src)
        return "generated content"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def greenfield_context(platform: str) -> str:
    src = GREEN_ROOT / "templates" / "governance" / "AI_CONTEXT.template.md"
    text = read_text(src)
    display = "iOS" if platform == "ios" else "Android"
    policy = (
        ".agents/policies/ios/IOS_ENGINEERING_POLICY.md"
        if platform == "ios"
        else ".agents/policies/android/ANDROID_ENGINEERING_POLICY.md"
    )
    text = text.replace("- Platform: [Android / iOS / both]", f"- Platform: {display}")
    text = text.replace("| Platform policy | [fill in] | |", f"| Platform policy | `{policy}` | |")
    return text


def compose_brownfield_agents(platform: str) -> str:
    common = read_text(BROWN_ROOT / "templates" / "AGENTS.common.md").rstrip()
    overlay_name = (
        "AGENTS.brownfield.ios.v1.4.md" if platform == "ios" else "AGENTS.brownfield.android.md"
    )
    overlay = read_text(BROWN_ROOT / "templates" / overlay_name).rstrip()
    lines = overlay.splitlines()
    if lines and lines[0].startswith("# "):
        lines[0] = "## " + lines[0][2:]
    overlay = "\n".join(lines)
    return (
        common
        + "\n\n---\n\n"
        + "# Platform overlay\n\n"
        + "The following platform-specific policy is installed with the common brownfield policy and is active authority for applicable work.\n\n"
        + overlay
        + "\n"
    )


def greenfield_operations(target: Path, platform: str, skills_only: bool) -> list[Operation]:
    ops: list[Operation] = []
    skills_src = GREEN_ROOT / "skills" / platform
    ops.append(Operation(target / ".agents" / "skills" / platform, src=skills_src))
    if skills_only:
        return ops

    policy_src = GREEN_ROOT / "templates" / "mobile-agent-policy-modular"
    ops.append(Operation(target / "AGENTS.md", src=policy_src / "AGENTS.md"))

    policies = policy_src / ".agents" / "policies"
    for name in [
        "FEATURE_DELIVERY_INVARIANTS.md",
        "GOVERNANCE_LIFECYCLE.md",
        "IMPLEMENTATION_POLICY.md",
        "EVIDENCE_AND_COMPLETION.md",
        "PROTECTED_BOUNDARIES.md",
    ]:
        ops.append(Operation(target / ".agents" / "policies" / name, src=policies / name))
    ops.append(Operation(target / ".agents" / "policies" / platform, src=policies / platform))

    governance = GREEN_ROOT / "templates" / "governance"
    ops.append(Operation(target / ".templates" / "governance", src=governance))

    architecture = GREEN_ROOT / "templates" / "architecture"
    for name in [
        "README.md",
        "ADR.template.md",
        f"ARCHITECTURE_SPINE.{platform}.template.md",
        "cross-feature-architecture-coverage.template.md",
        "IMPLEMENTATION_READINESS_GATE.template.md",
    ]:
        ops.append(Operation(target / ".templates" / "architecture" / name, src=architecture / name))

    mobile = GREEN_ROOT / "templates" / "mobile"
    ops.append(Operation(target / ".templates" / "mobile" / "README.md", src=mobile / "README.md"))
    ops.append(Operation(target / ".templates" / "mobile" / "mobile", src=mobile / "mobile"))
    ops.append(Operation(target / ".templates" / "mobile" / platform, src=mobile / platform))

    ops.append(
        Operation(
            target / "AI_CONTEXT.md",
            content=greenfield_context(platform),
            label="generated from templates/governance/AI_CONTEXT.template.md",
        )
    )
    ops.append(
        Operation(
            target / "docs" / "decisions" / "DECISION_REGISTER.md",
            src=governance / "DECISION_REGISTER.template.md",
        )
    )
    return ops


def brownfield_skill_names(platform: str) -> list[str]:
    names = [
        p.name
        for p in sorted((BROWN_ROOT / "skills").iterdir())
        if p.is_dir() and (p / "SKILL.md").exists()
    ]
    if platform == "ios":
        names = [name for name in names if name != "adaptive-compose"]
    return names


def brownfield_operations(target: Path, platform: str, skills_only: bool) -> list[Operation]:
    ops: list[Operation] = []
    for name in brownfield_skill_names(platform):
        ops.append(Operation(target / ".agents" / "skills" / name, src=BROWN_ROOT / "skills" / name))
    if skills_only:
        return ops

    ops.append(
        Operation(
            target / "AGENTS.md",
            content=compose_brownfield_agents(platform),
            label=f"generated from AGENTS.common.md + brownfield {platform} overlay",
        )
    )
    ops.append(Operation(target / ".templates" / "brownfield", src=BROWN_ROOT / "templates"))
    ops.append(
        Operation(
            target / "checklists" / "cross-feature-architecture-coverage.template.md",
            src=BROWN_ROOT / "checklists" / "cross-feature-architecture-coverage.template.md",
        )
    )

    starter = BROWN_ROOT / "repository-starter"
    ops.append(Operation(target / "docs" / "ai", src=starter / "docs" / "ai"))
    ops.append(Operation(target / "docs" / "ai" / "README.md", src=starter / "README.md"))
    ops.append(Operation(target / "AI_PLAYBOOK.md", src=BROWN_ROOT / "playbook" / "BROWNFIELD_PLAYBOOK.md"))
    return ops


def validate_plan(ops: list[Operation], force: bool) -> None:
    conflicts = [op.dst for op in ops if op.dst.exists()]
    if conflicts and not force:
        listed = "\n".join(f"  - {p}" for p in conflicts[:20])
        extra = "" if len(conflicts) <= 20 else f"\n  ... and {len(conflicts) - 20} more"
        raise FileExistsError(
            "bootstrap would overwrite existing paths; rerun with --force only if replacement is intentional:\n"
            + listed
            + extra
        )


def apply_operation(op: Operation, dry_run: bool) -> None:
    action = "WOULD INSTALL" if dry_run else "INSTALL"
    print(f"{action} {op.describe_source()} -> {op.dst}")
    if dry_run:
        return

    if op.dst.exists():
        if op.dst.is_dir():
            shutil.rmtree(op.dst)
        else:
            op.dst.unlink()
    op.dst.parent.mkdir(parents=True, exist_ok=True)

    if op.src is not None:
        if op.src.is_dir():
            shutil.copytree(op.src, op.dst)
        else:
            shutil.copy2(op.src, op.dst)
    else:
        assert op.content is not None
        op.dst.write_text(op.content, encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("package", choices=["greenfield", "brownfield"])
    ap.add_argument("--platform", choices=["android", "ios"], required=True, help="target native platform")
    ap.add_argument("--target", type=Path, default=Path.cwd(), help="receiving repository root")
    ap.add_argument(
        "--skills-only",
        action="store_true",
        help="install only reusable skills; skip governance/templates/starter scaffold",
    )
    ap.add_argument("--force", action="store_true", help="replace existing destination paths")
    ap.add_argument("--dry-run", action="store_true", help="preview the complete install plan")
    return ap


def main(argv: list[str] | None = None) -> int:
    ap = build_parser()
    args = ap.parse_args(argv)
    target = args.target.resolve()

    if args.package == "greenfield":
        ops = greenfield_operations(target, args.platform, args.skills_only)
    else:
        ops = brownfield_operations(target, args.platform, args.skills_only)

    try:
        validate_plan(ops, args.force)
    except FileExistsError as exc:
        ap.error(str(exc))

    mode = "skills-only" if args.skills_only else "full bootstrap"
    print(f"AI-Workflow {args.package} {mode}: platform={args.platform}, target={target}")
    for op in ops:
        apply_operation(op, args.dry_run)

    if not args.skills_only:
        if args.package == "greenfield":
            print("\nBootstrap complete. Project-specific architecture/feature/readiness artifacts were NOT fabricated.")
            print("Next: replace placeholders, confirm product authority, then follow the Greenfield bootstrap lifecycle.")
        else:
            print("\nStarter installed. Brownfield project-specific manifests/checkpoints were NOT created from example state.")
            print("Next: adapt docs/ai examples from repository evidence and create the project-specific AI_CONTEXT.md/router.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
