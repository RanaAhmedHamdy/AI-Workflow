#!/usr/bin/env python3
"""Deterministic repository checks for AI-Workflow."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from ai_workflow.assets import BROWN_PACKAGE, GREEN_PACKAGE

GREEN = ROOT / GREEN_PACKAGE
BROWN = ROOT / BROWN_PACKAGE


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"').strip("'")
        data[key.strip()] = value
    return data


def validate_skills(errors: list[str]) -> None:
    roots = [GREEN / "skills" / "android", GREEN / "skills" / "ios", BROWN / "skills"]
    for base in roots:
        if not base.exists():
            fail(errors, f"missing skill root: {base.relative_to(ROOT)}")
            continue
        for skill in sorted(base.rglob("SKILL.md")):
            fm = parse_frontmatter(skill)
            rel = skill.relative_to(ROOT)
            if not fm.get("name"):
                fail(errors, f"{rel}: missing frontmatter name")
            elif fm["name"] != skill.parent.name:
                fail(errors, f"{rel}: name '{fm['name']}' != directory '{skill.parent.name}'")
            if not fm.get("description"):
                fail(errors, f"{rel}: missing frontmatter description")
            lines = skill.read_text(encoding="utf-8").splitlines()
            if len(lines) > 500:
                fail(errors, f"{rel}: {len(lines)} lines exceeds 500-line skill guidance")


def validate_platform_leaks(errors: list[str]) -> None:
    apple = re.compile(r"\bplist\b|Info\.plist|SwiftUI|UIKit|Xcode|StoreKit|Keychain|BGTaskScheduler", re.I)
    android = re.compile(r"\bRoom\b|DataStore|WorkManager|Jetpack Compose|AndroidManifest|\bR8\b|\bAPK\b|\bAAB\b", re.I)
    for p in (GREEN / "skills" / "android").rglob("*.md"):
        m = apple.search(p.read_text(encoding="utf-8"))
        if m:
            fail(errors, f"{p.relative_to(ROOT)}: probable iOS copy/paste token '{m.group(0)}'")
    for p in (GREEN / "skills" / "ios").rglob("*.md"):
        m = android.search(p.read_text(encoding="utf-8"))
        if m:
            fail(errors, f"{p.relative_to(ROOT)}: probable Android copy/paste token '{m.group(0)}'")


def validate_ios_routing(errors: list[str]) -> None:
    base = GREEN / "skills" / "ios"
    for name in ["README.md", "INSTALL.md", "AI_CONTEXT.skill-routing.template.md"]:
        text = (base / name).read_text(encoding="utf-8")
        if ".agents/skills/shared/" in text or "skills/shared" in text:
            fail(errors, f"{(base/name).relative_to(ROOT)}: stale shared skill path")
    routing = (base / "AI_CONTEXT.skill-routing.template.md").read_text(encoding="utf-8")
    paths = re.findall(r"`\.agents/skills/ios/([^`]+)`", routing)
    for sub in paths:
        candidate = base / sub
        if not candidate.exists():
            fail(errors, f"iOS routing target does not exist: {candidate.relative_to(ROOT)}")


def validate_metadata(errors: list[str]) -> None:
    for p in ROOT.rglob("*"):
        if ".git" in p.parts:
            continue
        if p.name == ".DS_Store" or p.name.startswith("._") or "__MACOSX" in p.parts:
            fail(errors, f"forbidden archive/macOS metadata: {p.relative_to(ROOT)}")




def validate_package_wiring(errors: list[str]) -> None:
    if not GREEN.is_dir():
        fail(errors, f"missing bundled Greenfield package: {GREEN_PACKAGE}")
    if not BROWN.is_dir():
        fail(errors, f"missing bundled Brownfield package: {BROWN_PACKAGE}")

    for rel in ["README.md", "src/ai_workflow/cli.py", "setup.py"]:
        text = (ROOT / rel).read_text(encoding="utf-8")
        refs = set(re.findall(r"Greenfield_AI_Mobile_Governance_Package_v[0-9_]+", text))
        stale = refs - {GREEN_PACKAGE}
        for ref in sorted(stale):
            fail(errors, f"{rel}: stale Greenfield package reference {ref}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if GREEN_PACKAGE not in readme:
        fail(errors, f"README.md: missing current Greenfield package link {GREEN_PACKAGE}")

    cli = (ROOT / "src/ai_workflow/cli.py").read_text(encoding="utf-8")
    if 'target / ".templates" / "design"' not in cli:
        fail(errors, "Greenfield installer does not install templates/design")

def validate_public_files(errors: list[str]) -> None:
    for name in ["README.md", "LICENSE", "NOTICE", "CITATION.cff", "CONTRIBUTING.md", ".gitignore"]:
        if not (ROOT / name).exists():
            fail(errors, f"missing repository-level public file: {name}")


def validate_evals(errors: list[str]) -> None:
    path = ROOT / "evals" / "cases.json"
    try:
        cases = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(errors, f"eval corpus cannot be parsed: {exc}")
        return
    if len(cases) < 10:
        fail(errors, f"eval corpus has only {len(cases)} cases; expected at least 10")
    ids = [c.get("id") for c in cases]
    if len(ids) != len(set(ids)):
        fail(errors, "eval corpus contains duplicate ids")
    for c in cases:
        cid = c.get("id", "<missing>")
        for key in ["package", "platform", "prompt", "required_any", "forbidden", "expected_behavior"]:
            if key not in c or not c[key]:
                fail(errors, f"eval case {cid}: missing {key}")


def main() -> int:
    errors: list[str] = []
    validate_public_files(errors)
    validate_package_wiring(errors)
    validate_metadata(errors)
    validate_skills(errors)
    validate_platform_leaks(errors)
    validate_ios_routing(errors)
    validate_evals(errors)
    if errors:
        print("Repository validation FAILED:\n")
        for e in errors:
            print(f"- {e}")
        return 1
    print("Repository validation PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
