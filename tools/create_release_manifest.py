#!/usr/bin/env python3
"""Create a machine-readable manifest for one validated artifact directory."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from ai_workflow import __version__


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    artifacts = []
    for path in sorted(args.artifact_dir.iterdir()):
        if not path.is_file() or path.name in {args.output.name, "SHA256SUMS"} or path.name.endswith(".sha256"):
            continue
        if path.suffix not in {".whl", ".zip", ".gz"}:
            continue
        kind = "wheel" if path.suffix == ".whl" else "source ZIP" if path.name.endswith("-source.zip") else "sdist"
        artifacts.append({"filename": path.name, "sha256": sha256(path), "type": kind})
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    payload = {
        "project": "AI-Workflow",
        "project_version": __version__,
        "git_commit": commit,
        "built_at_utc": datetime.now(timezone.utc).isoformat(),
        "artifacts": artifacts,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
