"""Ownership and authoring-helper separation, exercised on isolated repositories."""
import json
from pathlib import Path
import subprocess
import sys
import unittest

from test_workshop import Fixture, REPO
from common import Problem, read_catalog
from validate import validate


class ClassificationTests(Fixture):
    def test_missing_maintenance_is_rejected(self):
        path = self.root / "catalog.yaml"
        text = path.read_text()
        text = "\n".join(line for line in text.splitlines()
                         if not line.strip().startswith("maintenance:")) + "\n"
        path.write_text(text)
        with self.assertRaises(Problem):
            read_catalog(self.root)

    def test_helper_cannot_be_registered_as_installable_output(self):
        path = self.root / "catalog.yaml"
        text = path.read_text()
        if "role: maintained-skill" in text:
            text = text.replace("role: maintained-skill", "role: authoring-helper")
        else:
            text += "    role: authoring-helper\n"
        path.write_text(text)
        with self.assertRaises(Problem):
            read_catalog(self.root)

    def test_created_here_is_distinct_from_imported(self):
        entry = read_catalog(self.root)["sample"]
        self.assertEqual("created-in-repository", entry["origin"])
        self.assertEqual("first-party", entry["maintenance"])

    def test_import_requires_existing_provenance_record(self):
        path = self.root / "catalog.yaml"
        text = path.read_text()
        if "origin: created-in-repository" in text:
            text = text.replace("origin: created-in-repository", "origin: imported-existing")
        else:
            text += "    origin: imported-existing\n"
        path.write_text(text)
        with self.assertRaises(Problem):
            read_catalog(self.root)

    def test_helper_source_fingerprint_is_validated(self):
        (self.root / "authoring-tools.yaml").write_text(
            "schema_version: 1\ntools:\n"
            "  - id: external:helper\n    role: authoring-helper\n    required: false\n"
            "    purpose: Help with authoring.\n    when_to_use: When authoring.\n"
            "    source:\n      distribution: external-package\n"
            "      version: '1.0'\n      entrypoint_sha256: invalid\n"
        )
        with self.assertRaises(Problem):
            validate(self.root)

    def test_machine_path_is_not_a_portable_helper_record(self):
        (self.root / "authoring-tools.yaml").write_text(
            "schema_version: 1\ntools:\n"
            "  - id: external:helper\n    role: authoring-helper\n    required: false\n"
            "    path: /machine/private/helper\n"
            "    purpose: Help.\n    when_to_use: When needed.\n"
            "    source:\n      distribution: external-package\n"
            "      version: '1.0'\n      entrypoint_sha256: " + "'a'".replace("a", "a"*64) + "\n"
        )
        with self.assertRaises(Problem):
            validate(self.root)

    def test_optional_helpers_need_no_local_resolution_in_ci(self):
        (self.root / "authoring-tools.yaml").write_text(
            "schema_version: 1\ntools:\n"
            "  - id: external:helper\n    role: authoring-helper\n    required: false\n"
            "    purpose: Help.\n    when_to_use: When needed.\n"
            "    source:\n      distribution: external-package\n"
            "      version: '1.0'\n      entrypoint_sha256: '" + "a"*64 + "'\n"
        )
        self.assertEqual(1, validate(self.root)["authoring_tools"])

    def test_helper_identifier_is_not_an_installable_skill(self):
        tool = REPO / "tools/install.py"
        result = subprocess.run(
            [sys.executable, str(tool), "install", "--skill", "skill-creator",
             "--target-root", str(self.target_root), "--state-root", str(self.state),
             "--apply"], capture_output=True, text=True,
        )
        self.assertNotEqual(0, result.returncode)
        self.assertFalse(self.target_root.exists())
        self.assertFalse(self.state.exists())


if __name__ == "__main__":
    unittest.main(failfast=True)
