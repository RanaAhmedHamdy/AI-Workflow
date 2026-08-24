#!/usr/bin/env python3
"""Build a deterministic public source ZIP from a strict repository allowlist."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from ai_workflow import __version__

ALLOWED_FILES = {".gitignore", "LICENSE", "NOTICE", "CITATION.cff", "CONTRIBUTING.md", "SECURITY.md", "README.md", "pyproject.toml", "setup.py", "MANIFEST.in", "release-manifest.json"}
ALLOWED_TREES = {"src", "tools", "tests", "docs", "evals", "routing", "examples", ".github", "Greenfield_AI_Mobile_Governance_Package_v1_10_0", "Brownfield_AI_Playbook_Reusable_Package_v4_4"}
FORBIDDEN = {"AUDIT", "build", "dist", ".git", ".obsidian", ".gradle", "__pycache__", ".pytest_cache", ".mypy_cache", ".venv", "venv"}


def allowed(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    if any(part in FORBIDDEN for part in rel.parts) or path.name in {".DS_Store", "local.properties"} or path.name.startswith("._") or path.suffix in {".pyc", ".pyo"}:
        return False
    return (len(rel.parts) == 1 and rel.name in ALLOWED_FILES) or rel.parts[0] in ALLOWED_TREES


def validate_files(files: list[Path]) -> None:
    required = [ROOT / "pyproject.toml", ROOT / "src/ai_workflow/cli.py", ROOT / "examples/android-profile-refresh/README.md", ROOT / "examples/ios-profile-refresh/README.md", ROOT / "Greenfield_AI_Mobile_Governance_Package_v1_10_0/skills/android/architecture-bootstrap/SKILL.md", ROOT / "Brownfield_AI_Playbook_Reusable_Package_v4_4/playbook/BROWNFIELD_PLAYBOOK.md"]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    if missing:
        raise RuntimeError("missing release files: " + ", ".join(missing))
    for path in files:
        rel = path.relative_to(ROOT)
        if any(part in FORBIDDEN for part in rel.parts) or path.name in {".DS_Store", "local.properties"} or path.name.startswith("._"):
            raise RuntimeError(f"forbidden release file: {rel}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    check = subprocess.run([sys.executable, str(ROOT / "tools/validate_repository.py")], cwd=ROOT)
    if check.returncode:
        return check.returncode
    files = sorted((path for path in ROOT.rglob("*") if path.is_file() and allowed(path)), key=lambda path: path.relative_to(ROOT).as_posix())
    validate_files(files)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    archive = args.output_dir / f"AI-Workflow-{__version__}-source.zip"
    epoch = int(os.environ.get("SOURCE_DATE_EPOCH", "315532800"))
    timestamp = __import__("time").gmtime(epoch)[:6]
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as output:
        for path in files:
            info = zipfile.ZipInfo(path.relative_to(ROOT).as_posix(), timestamp)
            info.external_attr = 0o100644 << 16
            output.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    checksum = archive.with_suffix(archive.suffix + ".sha256")
    checksum.write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    print(archive)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
