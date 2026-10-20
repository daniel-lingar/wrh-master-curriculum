"""Guard the withdrawal boundary when the public catalog is rebuilt."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

BUILDER = Path(__file__).with_name("build_session_catalog.py")


class CatalogWithdrawalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "scripts").mkdir()
        shutil.copyfile(BUILDER, self.root / "scripts" / BUILDER.name)
        (self.root / "Part-I").mkdir()
        (self.root / "Part-I" / "Session_01_Example.md").write_text(
            "# Session 1: WITHDRAWN_SOURCE_DO_NOT_PUBLISH\nPrivate source body.\n",
            encoding="utf-8",
        )
        self.output = self.root / "assets" / "data" / "sessions.json"

    def run_builder(self):
        subprocess.run(
            [sys.executable, str(self.root / "scripts" / BUILDER.name)],
            check=True, capture_output=True, text=True,
        )
        raw = self.output.read_text(encoding="utf-8")
        result = json.loads(raw)
        self.assertEqual(result["count"], 0)
        self.assertEqual(result["sessions"], [])
        self.assertEqual(result["status"], "withdrawn_pending_independent_review")
        self.assertNotIn("WITHDRAWN_SOURCE_DO_NOT_PUBLISH", raw)
        self.assertNotIn("Private source body", raw)
        return raw

    def test_clean_build_keeps_source_withdrawn_and_is_idempotent(self):
        self.assertEqual(self.run_builder(), self.run_builder())

    def test_rebuild_removes_previously_populated_catalog(self):
        self.output.parent.mkdir(parents=True)
        self.output.write_text(
            '{"count":1,"sessions":[{"html":"old delivery content"}]}',
            encoding="utf-8",
        )
        self.assertNotIn("old delivery content", self.run_builder())


if __name__ == "__main__":
    unittest.main()
