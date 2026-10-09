import json
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from audit_resources import audit

class ResourceAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "research" / "resources.json").read_text())

    def test_registry_has_records(self):
        self.assertGreaterEqual(audit(self.data)["records"], 50)

    def test_duplicate_identifiers_are_reported(self):
        row = self.data["resources"][0]
        report = audit({"resources": [row, row]})
        self.assertTrue(any("duplicate" in x for x in report["issues"]))

    def test_invalid_urls_are_reported(self):
        row = {**self.data["resources"][0], "url": "http://example.com"}
        report = audit({"resources": [row]})
        self.assertTrue(any("HTTPS" in x for x in report["issues"]))

if __name__ == "__main__":
    unittest.main()
