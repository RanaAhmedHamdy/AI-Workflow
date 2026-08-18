\
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RepositoryToolTests(unittest.TestCase):
    def test_repository_validator_passes(self):
        cp = subprocess.run([sys.executable, str(ROOT / "tools/validate_repository.py")], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(cp.returncode, 0, cp.stdout + cp.stderr)

    def test_greenfield_ios_installer_dry_run_is_platform_scoped(self):
        with tempfile.TemporaryDirectory() as td:
            cp = subprocess.run([
                sys.executable, str(ROOT / "tools/install_skills.py"), "greenfield",
                "--platform", "ios", "--target", td, "--dry-run"
            ], cwd=ROOT, text=True, capture_output=True)
            self.assertEqual(cp.returncode, 0, cp.stdout + cp.stderr)
            self.assertIn(".agents/skills/ios", cp.stdout.replace("\\", "/"))

    def test_eval_corpus_has_both_packages_and_unique_ids(self):
        cases = json.loads((ROOT / "evals/cases.json").read_text())
        self.assertGreaterEqual(len(cases), 10)
        ids = [c["id"] for c in cases]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual({c["package"] for c in cases}, {"greenfield", "brownfield"})


if __name__ == "__main__":
    unittest.main()
