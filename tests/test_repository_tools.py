import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
INSTALLER = ROOT / "tools" / "install.py"
from ai_workflow import cli


class RepositoryToolTests(unittest.TestCase):
    def run_cli(self, *args: str):
        return subprocess.run([sys.executable, str(INSTALLER), *args], cwd=ROOT, text=True, capture_output=True)

    def install(self, target: Path, workflow="greenfield", platform="android", profile="safety"):
        cp = self.run_cli(workflow, "--platform", platform, "--profile", profile, "--target", str(target))
        self.assertEqual(cp.returncode, 0, cp.stdout + cp.stderr)

    def test_repository_validator_passes(self):
        cp = subprocess.run([sys.executable, str(ROOT / "tools/validate_repository.py")], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(cp.returncode, 0, cp.stdout + cp.stderr)

    def test_four_workflow_platform_dry_runs(self):
        for workflow in ("greenfield", "brownfield"):
            for platform in ("android", "ios"):
                with self.subTest(workflow=workflow, platform=platform), tempfile.TemporaryDirectory() as td:
                    cp = self.run_cli(workflow, "--platform", platform, "--target", td, "--dry-run")
                    self.assertEqual(cp.returncode, 0, cp.stdout + cp.stderr)
                    self.assertIn("WOULD ADD", cp.stdout)
                    self.assertFalse((Path(td) / ".ai-workflow/manifest.json").exists())

    def test_fresh_install_writes_manifest_and_status_json(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td)
            self.install(target, "greenfield", "ios", "safety")
            manifest = json.loads((target / ".ai-workflow/manifest.json").read_text())
            self.assertEqual(manifest["platforms"], ["ios"])
            self.assertEqual(manifest["profile"], "safety")
            self.assertTrue((target / ".agents/routing/routes.json").is_file())
            self.assertFalse((target / ".templates/design/README.md").exists())
            status = self.run_cli("status", "--target", str(target), "--json")
            self.assertEqual(json.loads(status.stdout)["profile"], "safety")
        with tempfile.TemporaryDirectory() as td:
            target = Path(td)
            cp = self.run_cli("greenfield", "--platform", "android", "--target", str(target))
            self.assertEqual(cp.returncode, 0, cp.stdout + cp.stderr)
            self.assertEqual(json.loads((target / ".ai-workflow/manifest.json").read_text())["profile"], "safety")
        with tempfile.TemporaryDirectory() as td:
            target = Path(td)
            cp = self.run_cli("greenfield", "--platform", "android", "--skills-only", "--target", str(target))
            self.assertEqual(cp.returncode, 0, cp.stdout + cp.stderr)
            self.assertEqual(json.loads((target / ".ai-workflow/manifest.json").read_text())["profile"], "skills")

    def test_update_and_uninstall_preserve_modified_managed_file(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td)
            self.install(target)
            managed = target / "AGENTS.md"
            managed.write_text("recipient edit\n", encoding="utf-8")
            preview = self.run_cli("update", "--target", str(target), "--dry-run")
            self.assertIn("CONFLICT MODIFIED MANAGED FILE", preview.stdout)
            self.assertEqual(self.run_cli("update", "--target", str(target)).returncode, 0)
            self.assertEqual(managed.read_text(encoding="utf-8"), "recipient edit\n")
            self.assertEqual(self.run_cli("uninstall", "--target", str(target)).returncode, 0)
            self.assertEqual(managed.read_text(encoding="utf-8"), "recipient edit\n")
            self.assertTrue((target / ".ai-workflow/manifest.json").is_file())

    def test_dual_platform_composition_and_both_from_clean_state(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td)
            self.install(target, "greenfield", "android")
            cp = self.run_cli("update", "--target", str(target), "--platform", "ios")
            self.assertEqual(cp.returncode, 0, cp.stdout + cp.stderr)
            self.assertTrue((target / ".agents/skills/android").is_dir())
            self.assertTrue((target / ".agents/skills/ios").is_dir())
        with tempfile.TemporaryDirectory() as td:
            target = Path(td)
            self.install(target, "brownfield", "both", "full")
            agents = (target / "AGENTS.md").read_text(encoding="utf-8")
            self.assertIn("Android", agents)
            self.assertIn("iOS", agents)

    def test_all_profile_workflow_platform_installs_and_profile_contents(self):
        matrix = (ROOT / "docs/PROFILE_CONTENT_MATRIX.md").read_text(encoding="utf-8")
        match = re.search(r"<!-- profile-test-authority: (\{.*?\}) -->", matrix)
        self.assertIsNotNone(match, "profile content matrix must expose test authority")
        authority = json.loads(match.group(1))
        for workflow in ("greenfield", "brownfield"):
            for platform in ("android", "ios"):
                for profile in ("skills", "safety", "feature", "full"):
                    with self.subTest(workflow=workflow, platform=platform, profile=profile), tempfile.TemporaryDirectory() as td:
                        target = Path(td)
                        self.install(target, workflow, platform, profile)
                        manifest = json.loads((target / ".ai-workflow/manifest.json").read_text())
                        self.assertEqual(manifest["profile"], profile)
                        self.assertTrue((target / ".agents/routing/routes.json").is_file())
                        self.assertTrue((target / "FIRST_SAFE_CHANGE.md").is_file())
                        expectation = authority[profile]
                        self.assertEqual((target / "AGENTS.md").exists(), expectation["agents"])
                        self.assertEqual((target / ".templates/mobile/mobile/SMALL_FEATURE_RECORD_TEMPLATE.md").exists(), expectation["small_record"])
                        if workflow == "greenfield":
                            self.assertEqual((target / ".templates/architecture/ADR.template.md").exists(), expectation["architecture"])
                        else:
                            self.assertEqual((target / "AI_PLAYBOOK.md").exists(), expectation["brownfield_playbook"])

    def test_profile_transitions_preserve_modified_files_and_compose_platforms(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td)
            self.install(target, "greenfield", "android", "skills")
            self.assertEqual(self.run_cli("update", "--target", str(target), "--profile", "safety").returncode, 0)
            self.assertEqual(self.run_cli("update", "--target", str(target), "--profile", "feature").returncode, 0)
            self.assertTrue((target / ".templates/mobile/mobile/SMALL_FEATURE_RECORD_TEMPLATE.md").exists())
            self.assertEqual(self.run_cli("update", "--target", str(target), "--profile", "full").returncode, 0)
            managed = target / "AGENTS.md"
            managed.write_text("recipient policy edit\n", encoding="utf-8")
            preview = self.run_cli("update", "--target", str(target), "--profile", "feature", "--platform", "ios", "--dry-run")
            self.assertIn("REMOVE .templates/architecture/ADR.template.md", preview.stdout)
            self.assertIn("CONFLICT MODIFIED MANAGED FILE", preview.stdout)
            self.assertEqual(self.run_cli("update", "--target", str(target), "--profile", "feature", "--platform", "ios").returncode, 0)
            manifest = json.loads((target / ".ai-workflow/manifest.json").read_text())
            self.assertEqual(manifest["profile"], "feature")
            self.assertEqual(manifest["platforms"], ["android", "ios"])
            self.assertEqual(managed.read_text(encoding="utf-8"), "recipient policy edit\n")
            self.assertFalse((target / ".templates/architecture/ADR.template.md").exists())
        with tempfile.TemporaryDirectory() as td:
            target = Path(td)
            self.install(target, "brownfield", "ios", "feature")
            self.assertEqual(self.run_cli("update", "--target", str(target), "--profile", "safety").returncode, 0)
            self.assertFalse((target / ".templates/mobile/mobile/SMALL_FEATURE_RECORD_TEMPLATE.md").exists())

    def test_routing_corpus_and_cli_explanation(self):
        cases = json.loads((ROOT / "evals/routing_cases.json").read_text())
        self.assertGreaterEqual(len(cases), 30)
        for case in cases:
            result = cli.route_result(case["workflow"], case["platform"], "safety", case["facts"])
            selected = {item["skill"] for item in result["required_checks"]}
            self.assertTrue(set(case["required"]).issubset(selected), case["id"])
            self.assertFalse(set(case["forbidden"]).intersection(selected), case["id"])
            self.assertEqual(result["recommended_tier"], case["minimum_tier"], case["id"])
            self.assertEqual(result["hard_escalation"]["reason"], case["escalation_reason"], case["id"])
        cp = self.run_cli("route", "--workflow", "greenfield", "--platform", "ios", "--fact", "schema_migration", "--fact", "concurrency")
        self.assertEqual(cp.returncode, 0, cp.stdout + cp.stderr)
        self.assertIn("ios-persistence-migration-readiness", cp.stdout)
        self.assertIn("because detected", cp.stdout)

    def test_collision_force_and_reinstall_never_overwrite(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td)
            existing = target / "AGENTS.md"
            existing.write_text("recipient-owned\n", encoding="utf-8")
            cp = self.run_cli("greenfield", "--platform", "ios", "--target", str(target))
            self.assertNotEqual(cp.returncode, 0)
            self.assertIn("unmanaged recipient", cp.stderr)
            force = self.run_cli("greenfield", "--platform", "ios", "--target", str(target), "--force")
            self.assertIn("deprecated and disabled", force.stderr)
            self.assertEqual(existing.read_text(encoding="utf-8"), "recipient-owned\n")
        with tempfile.TemporaryDirectory() as td:
            target = Path(td)
            self.install(target)
            self.assertIn("use `ai-workflow update`", self.run_cli("greenfield", "--platform", "android", "--target", str(target)).stderr)

    def test_corrupt_manifest_traversal_and_symlink_are_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td)
            self.install(target)
            (target / ".ai-workflow/manifest.json").write_text('{"schema_version":1,"workflow":"greenfield","files":[{"path":"../outside","installed_hash":"x"}]}')
            cp = self.run_cli("status", "--target", str(target))
            self.assertIn("unsafe managed path", cp.stderr)
            with self.assertRaises(cli.InstallerError):
                cli._safe_relative("/absolute")
        with tempfile.TemporaryDirectory() as td, tempfile.TemporaryDirectory() as outside:
            target = Path(td)
            (target / ".agents").symlink_to(outside, target_is_directory=True)
            cp = self.run_cli("greenfield", "--platform", "android", "--target", str(target))
            self.assertIn("symlinked destination", cp.stderr)
            self.assertEqual(list(Path(outside).iterdir()), [])

    def test_failure_injection_and_file_directory_conflict_leave_no_ambiguous_install(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "recipient"
            actions, manifest = cli.plan_install(target, "greenfield", ("android",), False)
            with self.assertRaises(cli.InstallerError):
                cli.commit_plan(target, actions, manifest, fail_after_writes=3)
            self.assertFalse((target / "AGENTS.md").exists())
            self.assertFalse((target / ".ai-workflow/manifest.json").exists())
        with tempfile.TemporaryDirectory() as td:
            target = Path(td)
            (target / "AGENTS.md").mkdir()
            cp = self.run_cli("greenfield", "--platform", "android", "--target", str(target))
            self.assertNotEqual(cp.returncode, 0)
            self.assertTrue((target / "AGENTS.md").is_dir())
            self.assertFalse((target / ".ai-workflow").exists())

    def test_eval_corpus_has_both_packages_and_unique_ids(self):
        cases = json.loads((ROOT / "evals/cases.json").read_text())
        self.assertGreaterEqual(len(cases), 10)
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        self.assertEqual({case["package"] for case in cases}, {"greenfield", "brownfield"})


if __name__ == "__main__":
    unittest.main()
