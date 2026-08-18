\
#!/usr/bin/env python3
"""Keyword smoke-checker for saved agent responses to evals/cases.json."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--responses-dir", type=Path, required=True)
    ap.add_argument("--require-all", action="store_true")
    args = ap.parse_args()

    cases = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
    failures = 0
    checked = 0
    missing = 0

    for case in cases:
        path = args.responses_dir / f"{case['id']}.txt"
        if not path.exists():
            missing += 1
            if args.require_all:
                print(f"MISS {case['id']}: {path}")
                failures += 1
            continue
        checked += 1
        text = path.read_text(encoding="utf-8").lower()
        problems: list[str] = []
        for group in case["required_any"]:
            if not any(term.lower() in text for term in group):
                problems.append("missing one of: " + ", ".join(group))
        for term in case["forbidden"]:
            if term.lower() in text:
                problems.append("contains forbidden phrase: " + term)
        if problems:
            failures += 1
            print(f"FAIL {case['id']}")
            for p in problems:
                print(f"  - {p}")
        else:
            print(f"PASS {case['id']}")

    print(f"\nchecked={checked} missing={missing} failures={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
