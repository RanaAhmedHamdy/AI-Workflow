import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "tools" / "install.py"
LEGACY_INSTALLER = ROOT / "tools" / "install_skills.py"


class RepositoryToolTests(unittest.TestCase):
    def run_installer(self, *args: str):
        return subprocess.run(
            [sys.executable, str(INSTALLER), *args],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )

    def test_repository_validator_passes(self):
        cp = subprocess.run(
            [sys.executable, str(ROOT / "tools/validate_repository.py")],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(cp.returncode, 0, cp.stdout + cp.stderr)

    def test_greenfield_ios_full_bootstrap_dry_run_lists_required_scaffold(self):
        with tempfile.TemporaryDirectory() as td:
            cp = self.run_installer(
                "greenfield", "--platform", "ios", "--target", td, "--dry-run"
            )
            self.assertEqual(cp.returncode, 0, cp.stdout + cp.stderr)
            out = cp.stdout.replace("\\", "/")
            for expected in [
                "/AGENTS.md",
                "/AI_CONTEXT.md",
                "/docs/decisions/DECISION_REGISTER.md",
                "/.agents/policies/GOVERNANCE_LIFECYCLE.md",
                "/.agents/policies/ios",
                "/.agents/skills/ios",
                "/.templates/governance",
                "/.templates/architecture/ARCHITECTURE_SPINE.ios.template.md",
                "/.templates/mobile/mobile",
                "/.templates/mobile/ios",
            ]:
                self.assertIn(expected, out)

    def test_greenfield_android_full_install_creates_scaffold_not_fake_feature_artifacts(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td)
            cp = self.run_installer(
                "greenfield", "--platform", "android", "--target", td
            )
            self.assertEqual(cp.returncode, 0, cp.stdout + cp.stderr)
            self.assertTrue((target / "AGENTS.md").is_file())
            self.assertTrue((target / "AI_CONTEXT.md").is_file())
            self.assertTrue((target / "docs/decisions/DECISION_REGISTER.md").is_file())
            self.assertTrue((target / ".agents/policies/android/ANDROID_ENGINEERING_POLICY.md").is_file())
            self.assertTrue((target / ".agents/skills/android/android-architecture-readiness/SKILL.md").is_file())
            self.assertTrue((target / ".templates/mobile/android/IMPLEMENTATION_PLAN_TEMPLATE.md").is_file())
            self.assertFalse((target / ".agents/policies/ios").exists())
            self.assertFalse((target / ".templates/mobile/ios").exists())
            self.assertFalse((target / "docs/architecture/ARCHITECTURE_SPINE.md").exists())
            self.assertFalse((target / "docs/features").exists())
            context = (target / "AI_CONTEXT.md").read_text(encoding="utf-8")
            self.assertIn("- Platform: Android", context)
            self.assertIn(".agents/policies/android/ANDROID_ENGINEERING_POLICY.md", context)

    def test_greenfield_skills_only_preserves_old_narrow_behavior(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td)
            cp = self.run_installer(
                "greenfield", "--platform", "ios", "--target", td, "--skills-only"
            )
            self.assertEqual(cp.returncode, 0, cp.stdout + cp.stderr)
            self.assertTrue((target / ".agents/skills/ios/swift-concurrency-readiness/SKILL.md").is_file())
            self.assertFalse((target / "AGENTS.md").exists())
            self.assertFalse((target / ".templates").exists())

    def test_brownfield_ios_bootstrap_excludes_android_only_adaptive_compose(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td)
            cp = self.run_installer(
                "brownfield", "--platform", "ios", "--target", td
            )
            self.assertEqual(cp.returncode, 0, cp.stdout + cp.stderr)
            self.assertTrue((target / "AGENTS.md").is_file())
            self.assertTrue((target / "AI_PLAYBOOK.md").is_file())
            self.assertTrue((target / "docs/ai/prompts/modules-create.md").is_file())
            self.assertTrue((target / "docs/ai/README.md").is_file())
            self.assertTrue((target / ".agents/skills/characterization-tests/SKILL.md").is_file())
            self.assertFalse((target / ".agents/skills/adaptive-compose").exists())
            self.assertFalse((target / "docs/ai/DOCUMENTATION_CHECKPOINT.md").exists())

    def test_installer_refuses_to_overwrite_without_force(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td)
            (target / "AGENTS.md").write_text("existing\n", encoding="utf-8")
            cp = self.run_installer(
                "greenfield", "--platform", "ios", "--target", td
            )
            self.assertNotEqual(cp.returncode, 0)
            self.assertIn("--force", cp.stderr)
            self.assertEqual((target / "AGENTS.md").read_text(encoding="utf-8"), "existing\n")

    def test_legacy_installer_entrypoint_now_supports_full_bootstrap(self):
        with tempfile.TemporaryDirectory() as td:
            cp = subprocess.run(
                [
                    sys.executable,
                    str(LEGACY_INSTALLER),
                    "greenfield",
                    "--platform",
                    "ios",
                    "--target",
                    td,
                    "--dry-run",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )
            self.assertEqual(cp.returncode, 0, cp.stdout + cp.stderr)
            self.assertIn("AI_CONTEXT.md", cp.stdout)

    def test_eval_corpus_has_both_packages_and_unique_ids(self):
        cases = json.loads((ROOT / "evals/cases.json").read_text())
        self.assertGreaterEqual(len(cases), 10)
        ids = [c["id"] for c in cases]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual({c["package"] for c in cases}, {"greenfield", "brownfield"})


if __name__ == "__main__":
    unittest.main()
