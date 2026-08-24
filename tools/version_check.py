#!/usr/bin/env python3
"""Check that the release identity is internally consistent."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from ai_workflow import __version__


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tag", help="also require a matching v<version> tag")
    args = parser.parse_args()

    manifest = json.loads((ROOT / "release-manifest.json").read_text(encoding="utf-8"))
    expected = str(__version__)
    fields = {
        "project_version": manifest.get("project_version"),
        "python_distribution_version": manifest.get("python_distribution_version"),
        "cli_version": manifest.get("cli_version"),
    }
    errors = [f"{name}={value!r}, expected {expected!r}" for name, value in fields.items() if value != expected]
    if args.tag:
        match = re.fullmatch(r"v(.+)", args.tag)
        if not match or match.group(1) != expected:
            errors.append(f"tag={args.tag!r}, expected 'v{expected}'")
    if errors:
        print("Release identity check FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Release identity check PASSED: {expected}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
