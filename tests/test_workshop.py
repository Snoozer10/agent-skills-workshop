"""Isolated acceptance tests; no global skill roots or live agents."""
import io
from contextlib import redirect_stdout
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from common import Problem, manifest
import install as deployment
from validate import validate

REPO = Path(__file__).resolve().parents[1]


class Fixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="skill-workshop-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "repo"
        self.source = self.root / "skills" / "sample"
        self.source.mkdir(parents=True)
        (self.source / "SKILL.md").write_text(
            "---\nname: sample\ndescription: Handle a bounded sample task.\n---\n# Sample\n",
            encoding="utf-8",
        )
        (self.source / "binary.dat").write_bytes(b"\x00\r\n\xff\n")
        (self.root / "catalog.yaml").write_text(
            "schema_version: 1\nskills:\n"
            "  - name: sample\n    path: skills/sample\n    role: maintained-skill\n    maintenance: first-party\n    origin: created-in-repository\n    version: unversioned\n"
            "    categories: [test]\n    hosts: [codex]\n"
            "    activation: as-imported\n    qualification: unverified\n"
            "    limitations: [not runtime tested]\n", encoding="utf-8",
        )
        (self.root / "authoring-tools.yaml").write_text("schema_version: 1\ntools: []\n", encoding="utf-8")
        for doc in ("README.md", "AGENTS.md", "CONTRIBUTING.md"):
            (self.root / doc).write_text("# Fixture\n", encoding="utf-8")
        self.target_root = self.base / "discovery"
        self.target = self.target_root / "sample"
        self.state = self.base / "state"

    def put(self, **kwargs):
        return deployment.install(self.root, "sample", self.target_root, self.state, **kwargs)

    def initial(self):
        return self.put(apply=True)

    def upgraded(self):
        first = self.initial()
        old = manifest(self.target)
        (self.source / "binary.dat").write_bytes(b"new\x00bytes\n")
        second = self.put(apply=True, previous_receipt=first["receipt"])
        return old, second


class InstallationTests(Fixture):
    def test_default_runtime_receipts_preserve_legacy_local_evidence(self):
        legacy = self.root / ".local" / "legacy-receipt.txt"
        legacy.parent.mkdir()
        legacy.write_bytes(b"historical evidence\r\n")
        output = io.StringIO()
        argv = ["install.py", "install", "--skill", "sample",
                "--target-root", str(self.target_root), "--apply"]
        with patch.object(deployment, "ROOT", self.root), patch.object(sys, "argv", argv):
            with redirect_stdout(output):
                self.assertEqual(0, deployment.main())
        receipt = Path(json.loads(output.getvalue())["receipt"])
        self.assertTrue(receipt.is_relative_to(self.root / ".runtime" / "installs"))
        self.assertEqual(b"historical evidence\r\n", legacy.read_bytes())
        deployment.restore(receipt, apply=True)
        self.assertEqual(b"historical evidence\r\n", legacy.read_bytes())

    def test_public_cli_preview_install_and_restore(self):
        tool = REPO / "tools" / "install.py"
        args = [sys.executable, str(tool), "install", "--skill", "campaign-orchestrator",
                "--target-root", str(self.target_root), "--state-root", str(self.state)]
        baseline = manifest(self.base)
        preview = subprocess.run(args, text=True, capture_output=True)
        self.assertEqual(0, preview.returncode, preview.stderr)
        self.assertEqual(baseline, manifest(self.base))
        applied = subprocess.run(args + ["--apply"], text=True, capture_output=True)
        self.assertEqual(0, applied.returncode, applied.stderr)
        receipt = json.loads(applied.stdout)["receipt"]
        package = self.target_root / "campaign-orchestrator"
        self.assertEqual(manifest(REPO / "skills" / "campaign-orchestrator"), manifest(package))
        restored = subprocess.run([sys.executable, str(tool), "restore", "--receipt",
                                   receipt, "--apply"], text=True, capture_output=True)
        self.assertEqual(0, restored.returncode, restored.stderr)
        self.assertFalse(package.exists())

    def test_preview_creates_nothing(self):
        before = manifest(self.base)
        plan = self.put()
        self.assertFalse(plan["apply"])
        self.assertEqual(before, manifest(self.base))
        self.assertFalse(self.target_root.exists())
        self.assertFalse(self.state.exists())

    def test_install_preserves_bytes_and_restore_removes_first_install(self):
        expected = manifest(self.source)
        result = self.initial()
        self.assertEqual(expected, manifest(self.target))
        before = manifest(self.base)
        deployment.restore(result["receipt"])
        self.assertEqual(before, manifest(self.base))
        deployment.restore(result["receipt"], apply=True)
        self.assertIsNone(manifest(self.target))
        self.assertEqual(expected, manifest(Path(result["receipt"]).parent / "removed"))
        deployment.restore(result["receipt"], apply=True)
        self.assertIsNone(manifest(self.target))

    def test_update_and_restore_exact_prior_bytes(self):
        old, result = self.upgraded()
        self.assertNotEqual(old, manifest(self.target))
        deployment.restore(result["receipt"], apply=True)
        self.assertEqual(old, manifest(self.target))

    def test_unmanaged_target_requires_exact_adoption(self):
        shutil.copytree(self.source, self.target)
        with self.assertRaises(Problem):
            self.put(apply=True)
        self.assertFalse(self.state.exists())
        result = self.put(apply=True, adopt=True)
        self.assertEqual(manifest(self.source), manifest(self.target))
        self.assertTrue(Path(result["receipt"]).exists())

    def test_adoption_cannot_overwrite_different_bytes(self):
        shutil.copytree(self.source, self.target)
        (self.target / "binary.dat").write_bytes(b"private local edit")
        with self.assertRaises(Problem):
            self.put(apply=True, adopt=True)
        self.assertEqual(b"private local edit", (self.target / "binary.dat").read_bytes())

    def test_update_rejects_intervening_edits(self):
        first = self.initial()
        (self.target / "binary.dat").write_bytes(b"local")
        with self.assertRaises(Problem):
            self.put(apply=True, previous_receipt=first["receipt"])
        self.assertEqual(b"local", (self.target / "binary.dat").read_bytes())

    def test_restore_rejects_intervening_edits(self):
        result = self.initial()
        (self.target / "binary.dat").write_bytes(b"local")
        with self.assertRaises(Problem):
            deployment.restore(result["receipt"], apply=True)
        self.assertEqual(b"local", (self.target / "binary.dat").read_bytes())

    def test_restore_rejects_changed_backup(self):
        _, result = self.upgraded()
        backup = Path(result["receipt"]).parent / "previous"
        (backup / "binary.dat").write_bytes(b"corrupt")
        current = manifest(self.target)
        with self.assertRaises(Problem):
            deployment.restore(result["receipt"], apply=True)
        self.assertEqual(current, manifest(self.target))

    def test_interrupted_install_recovers_original(self):
        first = self.initial()
        old = manifest(self.target)
        (self.source / "binary.dat").write_bytes(b"new")
        real_replace = os.replace

        def fail_candidate(src, dst):
            if Path(src).name == "candidate":
                raise OSError("isolated interruption")
            return real_replace(src, dst)

        with patch.object(deployment.os, "replace", side_effect=fail_candidate):
            with self.assertRaises(OSError):
                self.put(apply=True, previous_receipt=first["receipt"])
        self.assertIsNone(manifest(self.target))
        receipts = [p for p in self.state.glob("*/receipt.json")
                    if (p.parent / "previous").exists()]
        self.assertEqual(1, len(receipts))
        deployment.restore(receipts[0], apply=True)
        self.assertEqual(old, manifest(self.target))

    def test_interrupted_restore_can_resume(self):
        old, result = self.upgraded()
        real_replace = os.replace

        def fail_previous(src, dst):
            if Path(src).name == "previous":
                raise OSError("isolated restoration interruption")
            return real_replace(src, dst)

        with patch.object(deployment.os, "replace", side_effect=fail_previous):
            with self.assertRaises(OSError):
                deployment.restore(result["receipt"], apply=True)
        self.assertIsNone(manifest(self.target))
        deployment.restore(result["receipt"], apply=True)
        self.assertEqual(old, manifest(self.target))

    def test_writer_lock_prevents_second_install(self):
        self.state.mkdir()
        with deployment.writer_lock(self.state, self.target):
            with self.assertRaises(Problem):
                self.put(apply=True)
        self.assertIsNone(manifest(self.target))

    def test_state_cannot_be_under_discovery_root(self):
        with self.assertRaises(Problem):
            deployment.install(self.root, "sample", self.target_root,
                               self.target_root / "state", apply=True)
        self.assertFalse(self.target_root.exists())

    def test_source_cannot_be_a_destination(self):
        with self.assertRaises(Problem):
            deployment.install(self.root, "sample", self.root / "skills",
                               self.state, apply=True)

    def test_receipt_for_another_target_is_refused(self):
        first = self.initial()
        second_root = self.base / "other"
        shutil.copytree(self.source, second_root / "sample")
        with self.assertRaises(Problem):
            deployment.install(self.root, "sample", second_root, self.state,
                               apply=True, previous_receipt=first["receipt"])

    def test_source_copy_failure_leaves_existing_target_intact(self):
        first = self.initial()
        old = manifest(self.target)
        with patch.object(deployment.shutil, "copytree", side_effect=OSError("copy failed")):
            with self.assertRaises(OSError):
                self.put(apply=True, previous_receipt=first["receipt"])
        self.assertEqual(old, manifest(self.target))


class ValidationTests(Fixture):
    def skill_text(self, text):
        (self.source / "SKILL.md").write_text(text, encoding="utf-8")

    def test_valid_fixture(self):
        self.assertEqual(1, validate(self.root)["skills"])

    def test_duplicate_yaml_keys_rejected(self):
        self.skill_text("---\nname: sample\nname: other\ndescription: task\n---\n")
        with self.assertRaises(Problem):
            validate(self.root)

    def test_name_mismatch_rejected(self):
        self.skill_text("---\nname: different\ndescription: task\n---\n")
        with self.assertRaises(Problem):
            validate(self.root)

    def test_missing_link_rejected(self):
        self.skill_text("---\nname: sample\ndescription: task\n---\n[Read](missing.md)\n")
        with self.assertRaises(Problem):
            validate(self.root)

    def test_skill_link_escape_rejected(self):
        self.skill_text("---\nname: sample\ndescription: task\n---\n[Read](../../README.md)\n")
        with self.assertRaises(Problem):
            validate(self.root)

    def test_wrong_case_link_rejected(self):
        (self.source / "Reference.md").write_text("# Reference\n", encoding="utf-8")
        self.skill_text("---\nname: sample\ndescription: task\n---\n[Read](reference.md)\n")
        with self.assertRaises(Problem):
            validate(self.root)

    def test_version_mismatch_rejected(self):
        self.skill_text("---\nname: sample\ndescription: task\nmetadata:\n  version: '1.0.0'\n---\n")
        with self.assertRaises(Problem):
            validate(self.root)

    def test_uncataloged_skill_rejected(self):
        (self.root / "skills" / "unregistered").mkdir()
        with self.assertRaises(Problem):
            validate(self.root)

    def test_claude_invocation_drift_rejected(self):
        path = self.root / "catalog.yaml"
        path.write_text(path.read_text().replace("as-imported", "explicit-only-intent"))
        self.skill_text("---\nname: sample\ndescription: task\ndisable-model-invocation: false\n---\n")
        with self.assertRaises(Problem):
            validate(self.root)

    def test_codex_invocation_drift_rejected(self):
        path = self.root / "catalog.yaml"
        path.write_text(path.read_text().replace("as-imported", "explicit-only-intent"))
        self.skill_text("---\nname: sample\ndescription: task\ndisable-model-invocation: true\n---\n")
        agents = self.source / "agents"
        agents.mkdir()
        (agents / "openai.yaml").write_text("policy:\n  allow_implicit_invocation: true\n")
        with self.assertRaises(Problem):
            validate(self.root)

    def test_manifest_rejects_symlink_when_supported(self):
        link = self.source / "linked"
        try:
            link.symlink_to(self.root / "README.md")
        except OSError as exc:
            self.skipTest(f"symlink creation unavailable: {exc}")
        with self.assertRaises(Problem):
            manifest(self.source)


class ImportTests(unittest.TestCase):
    def test_historical_import_receipt_is_well_formed(self):
        # Historical evidence remains valid after future source revisions.
        receipt = json.loads((REPO / "docs/imports/2026-10-28.json").read_text())
        names = set()
        for package in receipt["imports"]:
            self.assertNotIn(package["skill"], names)
            names.add(package["skill"])
            paths = set()
            for item in package["files"]:
                self.assertNotIn(item["path"], paths)
                paths.add(item["path"])
                self.assertRegex(item["sha256"], r"^[a-f0-9]{64}$")
                self.assertGreaterEqual(item["bytes"], 0)
                self.assertFalse(Path(item["path"]).is_absolute())
                self.assertNotIn("..", Path(item["path"]).parts)
            self.assertIn("SKILL.md", paths)
        self.assertEqual({"campaign-orchestrator", "antigravity-multiagent"}, names)


if __name__ == "__main__":
    unittest.main(failfast=True)
