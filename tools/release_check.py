#!/usr/bin/env python3
"""Run the maintainers' reproducible local release gate."""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*command: str) -> None:
    completed = subprocess.run(command, cwd=ROOT)
    if completed.returncode:
        raise SystemExit(completed.returncode)


def main() -> int:
    run(sys.executable, "tools/validate_repository.py")
    run(sys.executable, "tools/version_check.py")
    run(sys.executable, "-m", "unittest", "discover", "-s", "tests")
    with tempfile.TemporaryDirectory(prefix="ai-workflow-release-") as td:
        output = Path(td)
        run(sys.executable, "setup.py", "sdist", "--dist-dir", str(output))
        run(sys.executable, "setup.py", "bdist_wheel", "--dist-dir", str(output))
        artifacts = sorted(output.glob("*.whl")) + sorted(output.glob("*.tar.gz"))
        run(sys.executable, "tools/package_check.py", *(str(path) for path in artifacts))
        run(sys.executable, "tools/build_release.py", "--output-dir", str(output))
        run(sys.executable, "tools/package_check.py", str(next(output.glob("*-source.zip"))))
    print("Release verification PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
