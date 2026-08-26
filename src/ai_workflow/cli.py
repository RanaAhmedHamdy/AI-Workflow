#!/usr/bin/env python3
"""Safely install and maintain AI-Workflow scaffolding in a recipient repository."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

from . import __version__
from .assets import BROWN_PACKAGE, GREEN_PACKAGE

MANIFEST_DIR = ".ai-workflow"
MANIFEST_NAME = "manifest.json"
MANIFEST_SCHEMA_VERSION = 1
PROFILES = ("skills", "safety", "feature", "full")


def _asset_root() -> Path:
    """Locate bundled assets in a checkout or an installed environment."""
    source_root = Path(__file__).resolve().parents[2]
    if (source_root / GREEN_PACKAGE).is_dir() and (source_root / BROWN_PACKAGE).is_dir():
        return source_root
    installed_root = Path(sys.prefix) / "share" / "ai-workflow"
    if (installed_root / GREEN_PACKAGE).is_dir() and (installed_root / BROWN_PACKAGE).is_dir():
        return installed_root
    raise RuntimeError("AI-Workflow package assets were not found; reinstall a complete distribution.")


ROOT = _asset_root()
GREEN_ROOT = ROOT / GREEN_PACKAGE
BROWN_ROOT = ROOT / BROWN_PACKAGE
ROUTING_PATH = ROOT / "routing" / "routes.json"


@dataclass(frozen=True)
class FileSpec:
    path: str
    source_id: str
    content: bytes
    platforms: tuple[str, ...]
    symlink_target: str | None = None

    @property
    def digest(self) -> str:
        value = self.content if self.symlink_target is None else f"symlink:{self.symlink_target}".encode("utf-8")
        return hashlib.sha256(value).hexdigest()


@dataclass(frozen=True)
class Action:
    kind: str
    path: str
    spec: FileSpec | None = None
    reason: str = ""


class InstallerError(RuntimeError):
    pass


def _hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _safe_relative(value: str) -> PurePosixPath:
    candidate = PurePosixPath(value)
    if not value or candidate.is_absolute() or any(part in {"", ".", ".."} for part in candidate.parts):
        raise InstallerError(f"unsafe managed path in manifest or package: {value!r}")
    return candidate


def _target_path(target: Path, relative: str, allow_leaf_symlink: bool = False) -> Path:
    relative_path = _safe_relative(relative)
    destination = target.joinpath(*relative_path.parts)
    current = target
    for index, part in enumerate(relative_path.parts):
        current = current / part
        if current.is_symlink() and not (allow_leaf_symlink and index == len(relative_path.parts) - 1):
            raise InstallerError(f"refusing symlinked destination path: {current}")
    return destination


def _path_exists(path: Path) -> bool:
    """Return true for regular paths and broken symlinks."""
    return path.exists() or path.is_symlink()


def _managed_path_matches(path: Path, entry: dict) -> bool:
    """Check ownership without following an unexpected symlink."""
    if entry.get("kind", "file") == "symlink":
        return path.is_symlink() and os.readlink(path) == entry.get("target") and entry.get("installed_hash") == hashlib.sha256(f"symlink:{entry.get('target')}".encode("utf-8")).hexdigest()
    return path.is_file() and not path.is_symlink() and _hash_file(path) == entry.get("installed_hash")


def _normalise_platforms(values: Iterable[str]) -> tuple[str, ...]:
    platforms = {item for value in values for item in (("android", "ios") if value == "both" else (value,))}
    if not platforms or platforms.difference({"android", "ios"}):
        raise InstallerError("one or both supported platforms are required")
    return tuple(sorted(platforms))


def _source_id(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace(os.sep, "/")


def _tree_specs(destination: str, source: Path, platforms: tuple[str, ...]) -> list[FileSpec]:
    if not source.is_dir():
        raise InstallerError(f"required package asset is missing: {source}")
    return [FileSpec(f"{destination}/{item.relative_to(source).as_posix()}", _source_id(item), item.read_bytes(), platforms) for item in sorted(source.rglob("*")) if item.is_file()]


def _file_spec(destination: str, source: Path, platforms: tuple[str, ...]) -> FileSpec:
    if not source.is_file():
        raise InstallerError(f"required package asset is missing: {source}")
    return FileSpec(destination, _source_id(source), source.read_bytes(), platforms)


def _text_spec(destination: str, content: str, source_id: str, platforms: tuple[str, ...]) -> FileSpec:
    return FileSpec(destination, source_id, content.encode("utf-8"), platforms)


def _canonical_profile(value: str | bool | None) -> str:
    if value is True or value == "skills-only":
        return "skills"
    if value is False or value is None:
        return "full"
    if value not in PROFILES:
        raise InstallerError(f"unknown profile: {value!r}")
    return value


def routing_model() -> dict[str, Any]:
    try:
        model = json.loads(ROUTING_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise InstallerError(f"cannot read bundled routing model: {exc}") from exc
    if not isinstance(model, dict) or model.get("schema_version") != 1:
        raise InstallerError("bundled routing model is unsupported")
    return model


def profile_context(workflow: str, platforms: tuple[str, ...], profile: str, specs: Iterable[FileSpec] = ()) -> str:
    display = "both" if len(platforms) == 2 else platforms[0]
    profile_info = routing_model()["profiles"][profile]
    feature_path = "Use the compact `SMALL_FEATURE_RECORD.md` only in the feature/full profiles; otherwise provide a bounded change note in the receiving repository." if profile in {"feature", "full"} else "Do not create feature-governance artifacts unless the repository explicitly opts into the feature/full profile."
    full_path = "Full profile also enables Architecture Spine, ADR, Design Authority, readiness, acceptance, and release-governance routing." if profile == "full" else "Escalate to the full profile before creating or changing Architecture Spine/ADR authority."
    installed = {spec.path: spec for spec in specs}
    installed.update({"AGENTS.md": FileSpec("AGENTS.md", "generated:agents", b"", platforms), "CLAUDE.md": FileSpec("CLAUDE.md", "generated:claude", b"", platforms), "AI_CONTEXT.md": FileSpec("AI_CONTEXT.md", "generated:context", b"", platforms), "FIRST_SAFE_CHANGE.md": FileSpec("FIRST_SAFE_CHANGE.md", "generated:first-safe-change", b"", platforms), ".agents/routing/routes.json": FileSpec(".agents/routing/routes.json", "bundled:routing", b"", platforms)})
    skill_paths = sorted(path for path in installed if path.startswith(".agents/skills/") and path.endswith("/SKILL.md"))
    claude_skill_paths = sorted(path for path in installed if path.startswith(".claude/skills/"))
    prompt_paths = sorted(path for path in installed if "/prompts/" in path)
    template_paths = sorted(path for path in installed if path.startswith(".templates/"))
    policy_paths = sorted(path for path in installed if path.startswith(".agents/policies/"))
    grouped = set(skill_paths + claude_skill_paths + prompt_paths + template_paths + policy_paths)
    other_paths = sorted(path for path in installed if path not in grouped and path not in {"AGENTS.md", "CLAUDE.md", "AI_CONTEXT.md", "FIRST_SAFE_CHANGE.md", ".agents/routing/routes.json"})

    def paths(lines: Iterable[str]) -> str:
        return "\n".join(f"- `{path}`" + (f" → `{installed[path].symlink_target}`" if installed[path].symlink_target else "") for path in lines) or "- None installed by this profile."

    return f"""# AI-Workflow task router

Installed workflow: **{workflow}**
Platforms: **{display}**
Adoption profile: **{profile}** — {profile_info['summary']}

## Use this router

1. Interpret the developer request; state observable facts, not skill names (for example: `persistence`, `schema_migration`, `concurrency`, `lifecycle`, `privacy`, `localization`, `accessibility`, or `unknown_behavior`).
2. Apply `.agents/routing/routes.json` deterministically. Do not pretend the table understands natural language.
3. State selected skills and one short reason for each, any unselected relevant concern, the recommended tier, hard escalation, and unresolved facts.
4. Ask or stop only if an unresolved fact changes safety or authority. Skills are procedures, never implementation or release authorization.

Example: “This changes a persisted profile schema and Flow-owned state, so I apply persistence/migration, coroutine, protected-boundary where applicable, and runtime-evidence checks. STANDARD/COMPLEX escalation is required because migration/data-loss risk is present.”

{feature_path}

{full_path}

## Canonical entry points

- `AGENTS.md` is the single canonical repository instruction file for this installation.
- `CLAUDE.md` is a Claude Code adapter that imports `AGENTS.md` and this context index.
- `FIRST_SAFE_CHANGE.md` is the shortest recommended first-use path.
- `.agents/routing/routes.json` is the deterministic fact-to-procedure registry.

## Installed skills

Read the relevant `SKILL.md` only after routing the observable task facts. The `.claude/skills/` entries are symlinks to the same canonical skill directories, so Claude Code and Agent Skills-compatible tools share one source of truth.

### Canonical skill files

{paths(skill_paths)}

### Claude-compatible aliases

{paths(claude_skill_paths)}

## Installed policies

{paths(policy_paths)}

## Installed prompts

Prompts are optional Brownfield playbook aids; they are not automatically loaded as instructions.

{paths(prompt_paths)}

## Installed templates

Templates are artifact shapes, not project facts or implementation authorization.

{paths(template_paths)}

## Other installed references

{paths(other_paths)}
"""


def first_safe_change(workflow: str, profile: str) -> str:
    steps = ("inspect source → characterize unknown behavior if necessary → classify risk → route applicable specialist checks → bounded implementation → evidence/review" if workflow == "brownfield" else "identify authority → classify risk → choose SMALL/STANDARD/COMPLEX → route specialist checks → bounded implementation → evidence")
    artifact = "For a confirmed SMALL feature, copy `.templates/mobile/mobile/SMALL_FEATURE_RECORD_TEMPLATE.md` to the feature folder." if profile in {"feature", "full"} else "Keep a concise recipient-owned change note; do not manufacture a full feature lifecycle."
    return f"""# First safe change

Start with the change, not a catalogue of skills:

`{steps}`

Read `AI_CONTEXT.md`, name the observable facts, then use `.agents/routing/routes.json` (or `ai-workflow route`) to get the procedures and explanation. A hard escalation is not permission to skip work: promote the change to STANDARD/COMPLEX or opt into a deeper profile.

{artifact}

Implementation authorization, evidence, acceptance, and release authorization remain distinct decisions even when they appear in one SMALL record.
"""


def lightweight_policy(workflow: str, profile: str) -> str:
    return f"""# AI-Workflow {profile.title()} policy

Use `AI_CONTEXT.md` and `.agents/routing/routes.json` before choosing specialist procedures. State facts, selected checks, reasons, tier recommendation, hard escalation, and unresolved safety-relevant facts. {"For brownfield work, inspect source and characterize uncertain behaviour before changing it." if workflow == "brownfield" else "Do not invent product, design, or architecture authority."}

Protected boundaries, implementation authorization, evidence, acceptance, and release authorization remain separate. Do not claim runtime evidence from source inspection or previews.
"""


def claude_instructions(workflow: str, platforms: tuple[str, ...], profile: str) -> str:
    display = "both" if len(platforms) == 2 else platforms[0]
    return f"""# Claude Code project instructions

This repository uses AI-Workflow ({workflow}, {display}, {profile} profile).

Read the canonical repository policy and context index:

@AGENTS.md
@AI_CONTEXT.md

`AGENTS.md` is the single source of truth. Do not create a second policy file or infer project facts from this adapter. Use `.claude/skills/` for Claude Code skill discovery; those entries point to the canonical `.agents/skills/` directories. Route the task's observable facts before loading a specialist skill, and preserve all authorization, evidence, and protected-boundary rules from `AGENTS.md`.
"""


def compose_brownfield_agents(platforms: tuple[str, ...]) -> str:
    common = (BROWN_ROOT / "templates/AGENTS.common.md").read_text(encoding="utf-8").rstrip()
    common = common.replace("# AGENTS.md - Common Mobile Repository Policy", "# AGENTS.md — Brownfield Mobile Repository Policy")
    overlays = []
    for platform in platforms:
        name = "AGENTS.brownfield.ios.v1.4.md" if platform == "ios" else "AGENTS.brownfield.android.md"
        lines = (BROWN_ROOT / "templates" / name).read_text(encoding="utf-8").rstrip().splitlines()
        if lines and lines[0].startswith("# "):
            lines[0] = "## " + lines[0][2:]
        lines = [line.replace("Use with `AGENTS.common.md`. ", "The common Brownfield policy above applies. ").replace("> Version 1.4. Use with `AGENTS.common.md`. ", "> Version 1.4. The common Brownfield policy above applies. ") for line in lines]
        overlays.append("\n".join(lines))
    return common + "\n\n---\n\n## Platform-specific policy\n\n" + "\n\n---\n\n".join(overlays) + "\n"


def _deduplicate(specs: Iterable[FileSpec]) -> list[FileSpec]:
    result: dict[str, FileSpec] = {}
    for spec in specs:
        _safe_relative(spec.path)
        old = result.get(spec.path)
        if old is not None and (old.content != spec.content or old.symlink_target != spec.symlink_target):
            raise InstallerError(f"package composition produces conflicting content for {spec.path}")
        result[spec.path] = spec
    return [result[path] for path in sorted(result)]


def _routing_specs(workflow: str, platforms: tuple[str, ...], profile: str, specs: Iterable[FileSpec] = ()) -> list[FileSpec]:
    return [
        _file_spec(".agents/routing/routes.json", ROUTING_PATH, platforms),
        _text_spec("AI_CONTEXT.md", profile_context(workflow, platforms, profile, specs), f"generated:{workflow}:{profile}:context", platforms),
        _text_spec("FIRST_SAFE_CHANGE.md", first_safe_change(workflow, profile), f"generated:{workflow}:{profile}:first-safe-change", platforms),
    ]


def _symlink_spec(destination: str, target: str, source_id: str, platforms: tuple[str, ...]) -> FileSpec:
    return FileSpec(destination, source_id, b"", platforms, symlink_target=target)


def _claude_skill_specs(specs: Iterable[FileSpec], platforms: tuple[str, ...]) -> list[FileSpec]:
    links: list[FileSpec] = []
    for spec in specs:
        if not spec.path.startswith(".agents/skills/") or not spec.path.endswith("/SKILL.md"):
            continue
        parts = spec.path.split("/")
        if len(parts) == 4:
            alias = parts[2]
        elif len(parts) == 5 and parts[2] in {"android", "ios"}:
            alias = parts[3] if parts[3].startswith(f"{parts[2]}-") else f"{parts[2]}-{parts[3]}"
        else:
            continue
        target = os.path.relpath(spec.path.rsplit("/", 1)[0], ".claude/skills").replace(os.sep, "/")
        links.append(_symlink_spec(f".claude/skills/{alias}", target, f"symlink:{spec.path}", platforms))
    return links


def _integration_specs(specs: list[FileSpec], workflow: str, platforms: tuple[str, ...], profile: str) -> list[FileSpec]:
    specs.append(_file_spec("AGENTS.md", GREEN_ROOT / "templates/mobile-agent-policy-modular/AGENTS.md", platforms) if workflow == "greenfield" and profile == "full" else _text_spec("AGENTS.md", compose_brownfield_agents(platforms) if workflow == "brownfield" and profile == "full" else lightweight_policy(workflow, profile), f"generated:{workflow}:{profile}:agents", platforms))
    specs.append(_text_spec("CLAUDE.md", claude_instructions(workflow, platforms, profile), f"generated:{workflow}:{profile}:claude", platforms))
    specs.extend(_claude_skill_specs(specs, platforms))
    specs.extend(_routing_specs(workflow, platforms, profile, specs))
    return specs


def _feature_template_specs(platforms: tuple[str, ...]) -> list[FileSpec]:
    mobile = GREEN_ROOT / "templates/mobile"
    specs = [_file_spec(".templates/governance/FEATURE_COMPLEXITY_TIER_POLICY.md", GREEN_ROOT / "templates/governance/FEATURE_COMPLEXITY_TIER_POLICY.md", platforms)]
    specs.append(_file_spec(".templates/mobile/README.md", mobile / "README.md", platforms))
    specs.extend(_tree_specs(".templates/mobile/mobile", mobile / "mobile", platforms))
    specs.extend(spec for platform in platforms for spec in _tree_specs(f".templates/mobile/{platform}", mobile / platform, (platform,)))
    return specs


def greenfield_specs(platforms: tuple[str, ...], profile: str | bool) -> list[FileSpec]:
    profile = _canonical_profile(profile)
    specs = [spec for platform in platforms for spec in _tree_specs(f".agents/skills/{platform}", GREEN_ROOT / "skills" / platform, (platform,))]
    policies = GREEN_ROOT / "templates/mobile-agent-policy-modular"
    if profile != "skills":
        for name in (["FEATURE_DELIVERY_INVARIANTS.md", "GOVERNANCE_LIFECYCLE.md", "IMPLEMENTATION_POLICY.md", "EVIDENCE_AND_COMPLETION.md", "PROTECTED_BOUNDARIES.md"] if profile == "full" else ["IMPLEMENTATION_POLICY.md", "EVIDENCE_AND_COMPLETION.md", "PROTECTED_BOUNDARIES.md"]):
            specs.append(_file_spec(f".agents/policies/{name}", policies / ".agents/policies" / name, platforms))
        specs.extend(spec for platform in platforms for spec in _tree_specs(f".agents/policies/{platform}", policies / ".agents/policies" / platform, (platform,)))
    if profile in {"feature", "full"}:
        specs.extend(_feature_template_specs(platforms))
    if profile == "full":
        specs.extend(_tree_specs(".templates/governance", GREEN_ROOT / "templates/governance", platforms))
        specs.extend(_tree_specs(".templates/design", GREEN_ROOT / "templates/design", platforms))
        architecture = GREEN_ROOT / "templates/architecture"
        for name in ["README.md", "ADR.template.md", "cross-feature-architecture-coverage.template.md", "IMPLEMENTATION_READINESS_GATE.template.md"]:
            specs.append(_file_spec(f".templates/architecture/{name}", architecture / name, platforms))
        for platform in platforms:
            specs.append(_file_spec(f".templates/architecture/ARCHITECTURE_SPINE.{platform}.template.md", architecture / f"ARCHITECTURE_SPINE.{platform}.template.md", (platform,)))
        specs.append(_file_spec("docs/decisions/DECISION_REGISTER.md", GREEN_ROOT / "templates/governance/DECISION_REGISTER.template.md", platforms))
    return _deduplicate(_integration_specs(specs, "greenfield", platforms, profile))


def brownfield_specs(platforms: tuple[str, ...], profile: str | bool) -> list[FileSpec]:
    profile = _canonical_profile(profile)
    names = [item.name for item in sorted((BROWN_ROOT / "skills").iterdir()) if item.is_dir() and (item / "SKILL.md").is_file()]
    names = [name for name in names if name != "adaptive-compose" or "android" in platforms]
    specs = [spec for name in names for spec in _tree_specs(f".agents/skills/{name}", BROWN_ROOT / "skills" / name, ("android",) if name == "adaptive-compose" else platforms)]
    # Brownfield's source-first procedures are complemented by the same namespaced
    # platform safety skills as Greenfield; this keeps routing references installable.
    specs.extend(spec for platform in platforms for spec in _tree_specs(f".agents/skills/{platform}", GREEN_ROOT / "skills" / platform, (platform,)))
    if profile in {"feature", "full"}:
        specs.extend(_feature_template_specs(platforms))
    if profile == "full":
        specs.extend(spec for spec in _tree_specs(".templates/brownfield", BROWN_ROOT / "templates", platforms) if not Path(spec.path).name.startswith("AGENTS."))
        specs.append(_file_spec("checklists/cross-feature-architecture-coverage.template.md", BROWN_ROOT / "checklists/cross-feature-architecture-coverage.template.md", platforms))
        specs.extend(_tree_specs("docs/ai", BROWN_ROOT / "repository-starter/docs/ai", platforms))
        specs.append(_file_spec("docs/ai/README.md", BROWN_ROOT / "repository-starter/README.md", platforms))
        specs.append(_file_spec("AI_PLAYBOOK.md", BROWN_ROOT / "playbook/BROWNFIELD_PLAYBOOK.md", platforms))
    return _deduplicate(_integration_specs(specs, "brownfield", platforms, profile))


def build_specs(workflow: str, platforms: tuple[str, ...], profile: str | bool) -> list[FileSpec]:
    return greenfield_specs(platforms, profile) if workflow == "greenfield" else brownfield_specs(platforms, profile)


def manifest_path(target: Path) -> Path:
    return target / MANIFEST_DIR / MANIFEST_NAME


def load_manifest(target: Path) -> dict | None:
    path = manifest_path(target)
    if not path.exists():
        return None
    if path.is_symlink():
        raise InstallerError(f"refusing symlinked installer manifest: {path}")
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise InstallerError(f"invalid installer manifest: {exc}") from exc
    if not isinstance(manifest, dict) or manifest.get("schema_version") != MANIFEST_SCHEMA_VERSION or manifest.get("workflow") not in {"greenfield", "brownfield"} or not isinstance(manifest.get("files"), list):
        raise InstallerError("unsupported or malformed installer manifest")
    _canonical_profile(manifest.get("profile"))
    for entry in [*manifest["files"], *manifest.get("preserved_removed", [])]:
        if not isinstance(entry, dict) or not isinstance(entry.get("path"), str) or not isinstance(entry.get("installed_hash"), str):
            raise InstallerError("manifest contains an invalid managed-file entry")
        _safe_relative(entry["path"])
        kind = entry.get("kind", "file")
        if kind not in {"file", "symlink"}:
            raise InstallerError("manifest contains an unsupported managed-file kind")
        if kind == "symlink":
            target = entry.get("target")
            if not isinstance(target, str) or not target or PurePosixPath(target).is_absolute() or "\\" in target or "\x00" in target:
                raise InstallerError("manifest contains an unsafe symlink target")
            cursor = list(PurePosixPath(entry["path"]).parent.parts)
            for part in PurePosixPath(target).parts:
                if part in {"", "."}:
                    continue
                if part == "..":
                    if not cursor:
                        raise InstallerError("manifest symlink target escapes target")
                    cursor.pop()
                else:
                    cursor.append(part)
    return manifest


def manifest_entry(spec: FileSpec) -> dict:
    entry = {"path": spec.path, "source_id": spec.source_id, "installed_hash": spec.digest, "platforms": list(spec.platforms)}
    if spec.symlink_target is not None:
        entry.update({"kind": "symlink", "target": spec.symlink_target})
    return entry


def make_manifest(workflow: str, platforms: tuple[str, ...], profile: str | bool, entries: Iterable[dict], preserved: Iterable[dict], created_directories: Iterable[str] = ()) -> dict:
    return {"schema_version": MANIFEST_SCHEMA_VERSION, "package_version": __version__, "workflow": workflow, "platforms": list(platforms), "profile": _canonical_profile(profile), "files": sorted(entries, key=lambda item: item["path"]), "preserved_removed": sorted(preserved, key=lambda item: item["path"]), "created_directories": sorted(set(created_directories))}


def _assert_target(target: Path, create_allowed: bool = True) -> None:
    if target.exists() and target.is_symlink():
        raise InstallerError(f"refusing a symlinked target: {target}")
    if target.exists() and not target.is_dir():
        raise InstallerError(f"target is not a directory: {target}")
    if not target.exists() and not create_allowed:
        raise InstallerError(f"target does not exist: {target}")


def _check_destinations(target: Path, paths: Iterable[str], allow_leaf_symlink: bool = False) -> None:
    for path in paths:
        _target_path(target, path, allow_leaf_symlink=allow_leaf_symlink)


def plan_install(target: Path, workflow: str, platforms: tuple[str, ...], profile: str | bool) -> tuple[list[Action], dict]:
    _assert_target(target)
    if load_manifest(target) is not None:
        raise InstallerError("an AI-Workflow installation already exists; use `ai-workflow update` instead of reinstalling")
    profile = _canonical_profile(profile)
    specs = build_specs(workflow, platforms, profile)
    _check_destinations(target, [spec.path for spec in specs])
    conflicts = [spec.path for spec in specs if _target_path(target, spec.path).exists()]
    if manifest_path(target).exists():
        conflicts.append(f"{MANIFEST_DIR}/{MANIFEST_NAME}")
    if conflicts:
        shown = "\n".join(f"  - {path}" for path in conflicts[:20])
        raise InstallerError("installation would overwrite unmanaged recipient paths; no files were changed:\n" + shown)
    return [Action("add", spec.path, spec, "new package file") for spec in specs], make_manifest(workflow, platforms, profile, (manifest_entry(spec) for spec in specs), ())


def plan_update(target: Path, requested_platforms: tuple[str, ...] | None = None, requested_profile: str | None = None) -> tuple[list[Action], dict, list[str]]:
    _assert_target(target, False)
    old = load_manifest(target)
    if old is None:
        raise InstallerError("no AI-Workflow installation manifest found in target")
    platforms = _normalise_platforms([*_normalise_platforms(old["platforms"]), *(requested_platforms or ())])
    profile = _canonical_profile(requested_profile or old.get("profile"))
    desired = {spec.path: spec for spec in build_specs(old["workflow"], platforms, profile)}
    previous = {entry["path"]: entry for entry in old["files"]}
    preserved = {entry["path"]: entry for entry in old.get("preserved_removed", [])}
    _check_destinations(target, [*desired, *previous, *preserved], allow_leaf_symlink=True)
    actions: list[Action] = []
    notes: list[str] = []
    next_entries: dict[str, dict] = {}
    for path, entry in previous.items():
        destination = _target_path(target, path, allow_leaf_symlink=True)
        spec = desired.pop(path, None)
        if spec is None:
            if not _path_exists(destination):
                notes.append(f"MISSING (previous package file): {path}")
            elif _managed_path_matches(destination, entry):
                actions.append(Action("remove", path, reason="removed by newer package"))
            else:
                notes.append(f"PRESERVE MODIFIED (removed upstream): {path}")
                preserved[path] = entry
        elif not _path_exists(destination):
            notes.append(f"MISSING MANAGED FILE (preserved): {path}")
            next_entries[path] = entry
        elif not _managed_path_matches(destination, entry):
            notes.append(f"CONFLICT MODIFIED MANAGED FILE (preserved): {path}")
            next_entries[path] = entry
        elif spec.digest == entry["installed_hash"]:
            notes.append(f"UNCHANGED: {path}")
            next_entries[path] = manifest_entry(spec)
        else:
            actions.append(Action("replace", path, spec, "safe update of unchanged managed file"))
            next_entries[path] = manifest_entry(spec)
    for path, spec in desired.items():
        if _path_exists(_target_path(target, path, allow_leaf_symlink=True)):
            notes.append(f"UNMANAGED COLLISION (preserved): {path}")
        else:
            actions.append(Action("add", path, spec, "new package file"))
            next_entries[path] = manifest_entry(spec)
    for path, entry in list(preserved.items()):
        destination = _target_path(target, path, allow_leaf_symlink=True)
        if not _path_exists(destination) or _managed_path_matches(destination, entry):
            preserved.pop(path, None)
        else:
            notes.append(f"PRESERVED REMOVED FILE: {path}")
    manifest = make_manifest(old["workflow"], platforms, profile, next_entries.values(), preserved.values(), old.get("created_directories", []))
    return actions, manifest, notes


def plan_uninstall(target: Path) -> tuple[list[Action], dict | None, list[str]]:
    _assert_target(target, False)
    old = load_manifest(target)
    if old is None:
        raise InstallerError("no AI-Workflow installation manifest found in target")
    entries = [*old["files"], *old.get("preserved_removed", [])]
    _check_destinations(target, [entry["path"] for entry in entries], allow_leaf_symlink=True)
    actions: list[Action] = []
    residual: list[dict] = []
    notes: list[str] = []
    for entry in entries:
        destination = _target_path(target, entry["path"], allow_leaf_symlink=True)
        if not _path_exists(destination):
            notes.append(f"ALREADY MISSING: {entry['path']}")
        elif _managed_path_matches(destination, entry):
            actions.append(Action("remove", entry["path"], reason="unmodified package-owned file"))
        else:
            residual.append(entry)
            notes.append(f"PRESERVE MODIFIED FILE: {entry['path']}")
    manifest = None if not residual else make_manifest(old["workflow"], _normalise_platforms(old["platforms"]), old.get("profile"), (), residual, old.get("created_directories", []))
    return actions, manifest, notes


def _manifest_bytes(manifest: dict) -> bytes:
    return (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode("utf-8")


def _copy_entry(source: Path, destination: Path) -> None:
    """Copy a regular file or preserve a symlink itself."""
    if source.is_symlink():
        destination.symlink_to(os.readlink(source), target_is_directory=source.is_dir())
    else:
        shutil.copy2(source, destination)


def commit_plan(target: Path, actions: list[Action], manifest: dict | None, fail_after_writes: int | None = None) -> list[str]:
    """Stage writes and roll back every changed file if commit fails.

    ``fail_after_writes`` exists solely for failure-injection tests.
    """
    stage = Path(tempfile.mkdtemp(prefix="ai-workflow-stage-", dir=target.parent))
    backups = stage / "backups"
    staged: dict[str, Path] = {}
    changed: list[tuple[Path, Path | None]] = []
    created: list[str] = []
    target_existed = target.exists()
    try:
        for action in actions:
            if action.kind in {"add", "replace"} and action.spec is not None and action.spec.symlink_target is None:
                assert action.spec is not None
                path = stage / "files" / action.path
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(action.spec.content)
                if _hash_file(path) != action.spec.digest:
                    raise InstallerError(f"staging verification failed for {action.path}")
                staged[action.path] = path
        manifest_stage = stage / "manifest.json"
        if manifest is not None:
            manifest_stage.write_bytes(_manifest_bytes(manifest))
            json.loads(manifest_stage.read_text(encoding="utf-8"))
        if not target.exists():
            target.mkdir(parents=True)
            created.append(".")
        writes = 0
        for action in actions:
            destination = _target_path(target, action.path, allow_leaf_symlink=True)
            if _path_exists(destination) and destination.is_dir() and not destination.is_symlink():
                raise InstallerError(f"file-versus-directory conflict at {destination}")
            backup = None
            if _path_exists(destination):
                backup = backups / action.path
                backup.parent.mkdir(parents=True, exist_ok=True)
                _copy_entry(destination, backup)
            else:
                missing: list[Path] = []
                parent = destination.parent
                while parent != target and not parent.exists():
                    missing.append(parent)
                    parent = parent.parent
                for directory in reversed(missing):
                    directory.mkdir()
                    created.append(str(directory.relative_to(target)).replace(os.sep, "/"))
            changed.append((destination, backup))
            if action.kind == "remove":
                destination.unlink()
            elif action.spec is not None and action.spec.symlink_target is not None:
                if _path_exists(destination):
                    destination.unlink()
                destination.symlink_to(action.spec.symlink_target, target_is_directory=True)
            else:
                shutil.copy2(staged[action.path], destination)
            writes += 1
            if fail_after_writes is not None and writes >= fail_after_writes:
                raise OSError("injected installer write failure")
        destination_manifest = manifest_path(target)
        if manifest is not None:
            if not destination_manifest.parent.exists():
                destination_manifest.parent.mkdir()
                created.append(MANIFEST_DIR)
            backup = None
            if destination_manifest.exists():
                backup = backups / "manifest.json"
                backup.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(destination_manifest, backup)
            changed.append((destination_manifest, backup))
            shutil.copy2(manifest_stage, destination_manifest)
        elif destination_manifest.exists():
            backup = backups / "manifest.json"
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(destination_manifest, backup)
            changed.append((destination_manifest, backup))
            destination_manifest.unlink()
        return created
    except Exception as exc:
        failures = []
        for destination, backup in reversed(changed):
            try:
                if backup is None:
                    if _path_exists(destination):
                        destination.unlink()
                else:
                    if _path_exists(destination):
                        destination.unlink()
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    _copy_entry(backup, destination)
            except OSError as rollback_error:
                failures.append(str(rollback_error))
        for directory in sorted((target / item for item in created if item != "."), key=lambda path: len(path.parts), reverse=True):
            try:
                directory.rmdir()
            except OSError:
                pass
        if not target_existed:
            try:
                target.rmdir()
            except OSError:
                pass
        detail = "" if not failures else "; rollback errors: " + "; ".join(failures)
        raise InstallerError(f"installation commit failed; changed files were rolled back: {exc}{detail}") from exc
    finally:
        shutil.rmtree(stage, ignore_errors=True)


def _print_plan(title: str, actions: list[Action], notes: Iterable[str], dry_run: bool) -> None:
    print(title)
    for action in actions:
        verb = {"add": "ADD", "replace": "UPDATE", "remove": "REMOVE"}[action.kind]
        print(f"{'WOULD ' if dry_run else ''}{verb} {action.path}" + (f" ({action.reason})" if action.reason else ""))
    for note in notes:
        print(note)


def _finalise_created_directories(target: Path, manifest: dict, created: list[str]) -> None:
    if created:
        manifest["created_directories"] = sorted(set(manifest.get("created_directories", []) + created))
        manifest_path(target).write_bytes(_manifest_bytes(manifest))


def command_install(args: argparse.Namespace, parser: argparse.ArgumentParser) -> int:
    if args.force:
        parser.error("--force is deprecated and disabled. Use `ai-workflow update --dry-run` to review safe changes.")
    target = args.target.absolute()
    try:
        platforms = _normalise_platforms(args.platform)
        if args.skills_only and args.profile != "safety":
            parser.error("--skills-only is a compatibility alias for --profile skills and cannot be combined with another profile")
        profile = "skills" if args.skills_only else args.profile
        actions, manifest = plan_install(target, args.command, platforms, profile)
        _print_plan(f"AI-Workflow {args.command} install: profile={profile}, platforms={','.join(platforms)}, target={target}", actions, (), args.dry_run)
        if not args.dry_run:
            _finalise_created_directories(target, manifest, commit_plan(target, actions, manifest))
            suffix = " --skills-only is deprecated; use --profile skills." if args.skills_only else ""
            print(f"Installed {len(manifest['files'])} package-owned files. Run `ai-workflow status --target {target}` to inspect ownership.{suffix}")
    except InstallerError as exc:
        parser.error(str(exc))
    return 0


def command_update(args: argparse.Namespace, parser: argparse.ArgumentParser) -> int:
    target = args.target.absolute()
    try:
        requested = _normalise_platforms(args.platform) if args.platform else None
        actions, manifest, notes = plan_update(target, requested, args.profile)
        _print_plan(f"AI-Workflow update: profile={manifest['profile']}, target={target}", actions, notes, args.dry_run)
        if not args.dry_run:
            _finalise_created_directories(target, manifest, commit_plan(target, actions, manifest))
            print("Update complete. Preserved conflicts remain recorded in the manifest.")
    except InstallerError as exc:
        parser.error(str(exc))
    return 0


def command_uninstall(args: argparse.Namespace, parser: argparse.ArgumentParser) -> int:
    target = args.target.absolute()
    try:
        actions, manifest, notes = plan_uninstall(target)
        _print_plan(f"AI-Workflow uninstall: target={target}", actions, notes, args.dry_run)
        if not args.dry_run:
            created = commit_plan(target, actions, manifest)
            if manifest is not None:
                _finalise_created_directories(target, manifest, created)
                print("Uninstall preserved modified recipient files; the manifest remains for residual-state tracking.")
            else:
                try:
                    (target / MANIFEST_DIR).rmdir()
                except OSError:
                    pass
                print("Uninstall complete; only unmodified package-owned files were removed.")
    except InstallerError as exc:
        parser.error(str(exc))
    return 0


def command_status(args: argparse.Namespace, parser: argparse.ArgumentParser) -> int:
    target = args.target.absolute()
    try:
        _assert_target(target, False)
        manifest = load_manifest(target)
        if manifest is None:
            result = {"installed": False, "target": str(target), "reason": "manifest not found"}
        else:
            modified, missing = [], []
            for entry in [*manifest["files"], *manifest.get("preserved_removed", [])]:
                destination = _target_path(target, entry["path"], allow_leaf_symlink=True)
                (missing if not _path_exists(destination) else modified if not _managed_path_matches(destination, entry) else []).append(entry["path"])
            result = {"installed": True, "target": str(target), "workflow": manifest["workflow"], "profile": _canonical_profile(manifest.get("profile")), "platforms": manifest["platforms"], "package_version": manifest["package_version"], "manifest_schema_version": manifest["schema_version"], "tracked_file_count": len(manifest["files"]), "modified_managed_files": modified, "missing_managed_files": missing, "preserved_removed_files": [entry["path"] for entry in manifest.get("preserved_removed", [])], "update_eligible": not modified and not missing}
        if args.json:
            print(json.dumps(result, indent=2, sort_keys=True))
        elif not result["installed"]:
            print(f"AI-Workflow: not installed in {target} ({result['reason']}).")
        else:
            print(f"AI-Workflow: installed ({result['workflow']}; profile={result['profile']}; platforms={','.join(result['platforms'])}; version={result['package_version']})")
            print(f"Manifest schema: {result['manifest_schema_version']}; tracked files: {result['tracked_file_count']}")
            print(f"Modified managed files: {len(result['modified_managed_files'])}; missing managed files: {len(result['missing_managed_files'])}")
            print(f"Update eligibility: {'yes' if result['update_eligible'] else 'review conflicts first'}")
    except InstallerError as exc:
        parser.error(str(exc))
    return 0


def route_result(workflow: str, platform: str, profile: str, facts: Iterable[str]) -> dict[str, Any]:
    model = routing_model()
    facts_set = set(facts)
    known = set(model["facts"]) | {item for values in model["hard_escalation"].values() for item in values}
    unknown = sorted(facts_set - known)
    if unknown:
        raise InstallerError("unknown routing fact(s): " + ", ".join(unknown))
    selected: list[dict[str, str]] = []
    seen: set[str] = set()
    for route in model["routes"]:
        if route.get("workflow") and route["workflow"] != workflow:
            continue
        triggered = sorted(facts_set.intersection(route["facts_any"]))
        if not triggered:
            continue
        for skill in route["skills"].get(platform, []):
            if skill not in seen:
                seen.add(skill)
                selected.append({"skill": skill, "because": "detected " + ", ".join(triggered)})
    complex_hits = sorted(facts_set.intersection(model["hard_escalation"]["complex"]))
    standard_hits = sorted(facts_set.intersection(model["hard_escalation"]["standard"]))
    tier = "COMPLEX" if complex_hits else "STANDARD" if standard_hits else "SMALL"
    reason = ", ".join(complex_hits or standard_hits) or "no deterministic hard-escalation trigger detected"
    return {"workflow": workflow, "platform": platform, "profile": profile, "detected_facts": sorted(facts_set), "required_checks": selected, "optional_checks": (["documentation-impact-assessment"] if "documentation" not in facts_set else []), "recommended_tier": tier, "hard_escalation": {"required": bool(complex_hits or standard_hits), "reason": reason}, "unresolved_facts": []}


def command_profiles(args: argparse.Namespace, parser: argparse.ArgumentParser) -> int:
    model = routing_model()
    for name in PROFILES:
        item = model["profiles"][name]
        recommended = " (recommended default)" if item["recommended"] else ""
        print(f"{name}{recommended}: {item['summary']} Process weight: {item['process_weight']}.")
    return 0


def command_route(args: argparse.Namespace, parser: argparse.ArgumentParser) -> int:
    try:
        result = route_result(args.workflow, args.platform, args.profile, args.fact or [])
        if args.json:
            print(json.dumps(result, indent=2, sort_keys=True))
        else:
            print(f"Task classification: {result['workflow']} / {result['platform']} / {result['profile']}")
            print("Detected concerns: " + (", ".join(result["detected_facts"]) or "none supplied"))
            print(f"Recommended tier: {result['recommended_tier']}")
            print("Required checks:")
            for item in result["required_checks"]:
                print(f"- {item['skill']}: because {item['because']}")
            if not result["required_checks"]:
                print("- none; verify the facts before treating the change as low risk")
            print(f"Escalation: {'required' if result['hard_escalation']['required'] else 'not triggered'} — {result['hard_escalation']['reason']}")
    except InstallerError as exc:
        parser.error(str(exc))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subcommands = parser.add_subparsers(dest="command", required=True)
    for command in ("greenfield", "brownfield"):
        child = subcommands.add_parser(command, help=f"install {command} scaffolding")
        child.add_argument("--platform", action="append", choices=["android", "ios", "both"], required=True, help="target platform; repeat to compose platforms")
        child.add_argument("--target", type=Path, default=Path.cwd(), help="receiving repository root")
        child.add_argument("--profile", choices=PROFILES, default="safety", help="adoption profile (default: safety)")
        child.add_argument("--skills-only", action="store_true", help="deprecated compatibility alias for --profile skills")
        child.add_argument("--dry-run", action="store_true", help="preview without modifying the target")
        child.add_argument("--force", action="store_true", help="deprecated and disabled for recipient safety")
        child.set_defaults(handler=command_install)
    update = subcommands.add_parser("update", help="safely update an existing installation")
    update.add_argument("--target", type=Path, default=Path.cwd())
    update.add_argument("--platform", action="append", choices=["android", "ios", "both"], help="append platform content during update")
    update.add_argument("--profile", choices=PROFILES, help="explicitly transition to an adoption profile")
    update.add_argument("--dry-run", action="store_true")
    update.set_defaults(handler=command_update)
    uninstall = subcommands.add_parser("uninstall", help="remove only unmodified package-owned files")
    uninstall.add_argument("--target", type=Path, default=Path.cwd())
    uninstall.add_argument("--dry-run", action="store_true")
    uninstall.set_defaults(handler=command_uninstall)
    status = subcommands.add_parser("status", help="inspect installation ownership and local changes")
    status.add_argument("--target", type=Path, default=Path.cwd())
    status.add_argument("--json", action="store_true")
    status.set_defaults(handler=command_status)
    profiles = subcommands.add_parser("profiles", help="explain adoption profiles")
    profiles.set_defaults(handler=command_profiles)
    route = subcommands.add_parser("route", help="deterministically route already-identified change facts")
    route.add_argument("--workflow", choices=["greenfield", "brownfield"], required=True)
    route.add_argument("--platform", choices=["android", "ios"], required=True)
    route.add_argument("--profile", choices=PROFILES, default="safety")
    route.add_argument("--fact", action="append", help="observable change fact; repeat for each fact")
    route.add_argument("--json", action="store_true")
    route.set_defaults(handler=command_route)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.handler(args, parser)


if __name__ == "__main__":
    raise SystemExit(main())
