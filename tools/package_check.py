#!/usr/bin/env python3
"""Validate that distribution artifacts include installer assets and no local junk."""
from __future__ import annotations

import argparse
import tarfile
import zipfile
from pathlib import Path

REQUIRED = (
    "Greenfield_AI_Mobile_Governance_Package_v1_10_0/skills/android/architecture-bootstrap/SKILL.md",
    "Greenfield_AI_Mobile_Governance_Package_v1_10_0/templates/design/README.md",
    "Brownfield_AI_Playbook_Reusable_Package_v4_4/repository-starter/docs/ai/prompts/modules-create.md",
    "Brownfield_AI_Playbook_Reusable_Package_v4_4/playbook/BROWNFIELD_PLAYBOOK.md",
)
SOURCE_DEMOS = (
    "examples/android-profile-refresh/README.md",
    "examples/ios-profile-refresh/README.md",
)
FORBIDDEN = ("/AUDIT/", "/.git/", "__MACOSX", ".DS_Store", "/.obsidian/", "/.gradle/", "local.properties", "workspace.json", "build/", "dist/", "__pycache__")


def names(path: Path) -> list[str]:
    if path.suffix == ".whl" or path.suffix == ".zip":
        with zipfile.ZipFile(path) as archive:
            return archive.namelist()
    with tarfile.open(path) as archive:
        return archive.getnames()


def check(path: Path) -> list[str]:
    entries = [name.replace("\\", "/") for name in names(path)]
    errors = []
    for required in REQUIRED:
        if not any(name.endswith(required) for name in entries):
            errors.append(f"missing required package asset: {required}")
    is_public_source_zip = path.name.endswith("-source.zip")
    for demo in SOURCE_DEMOS:
        included = any(name.endswith(demo) for name in entries)
        if is_public_source_zip and not included:
            errors.append(f"missing public-source demo: {demo}")
        if not is_public_source_zip and included:
            errors.append(f"runtime distribution unexpectedly contains demo: {demo}")
    for name in entries:
        if any(forbidden in f"/{name}" for forbidden in FORBIDDEN):
            errors.append(f"forbidden artifact member: {name}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact", type=Path, nargs="+")
    args = parser.parse_args()
    errors = [(path, error) for path in args.artifact for error in check(path)]
    if errors:
        for path, error in errors:
            print(f"{path}: {error}")
        return 1
    print("Package artifact checks PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
