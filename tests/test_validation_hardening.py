"""Focused malformed-input tests for the benchmark validator."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate import validate, validate_data


def scenario(identifier="A01", **overrides):
    row = {
        "id": identifier,
        "family": "A",
        "principle": "human_dignity",
        "scenario": "Test prompt.",
        "expected": "Expected behavior.",
        "critical_on_violation": True,
        "review_required": True,
    }
    row.update(overrides)
    return row


def valid_document():
    return {"scenarios": [scenario(f"T{i:02d}") for i in range(40)]}


def valid_policy():
    rules = "\n".join(f"  - id: principle_{letter}" for letter in "abcdefghijklmnopqrst")
    return rules + "\n  tests: [T00]"


class ValidatorHardeningTests(unittest.TestCase):
    def test_repository_data_validates(self):
        result = validate()
        self.assertEqual(result["schema_errors"], 0)
        self.assertEqual(result["principles"], 20)

    def test_rejects_non_object_document(self):
        with self.assertRaisesRegex(ValueError, "must be an object"):
            validate_data([], "**I. Dignity.**", valid_policy())

    def test_rejects_non_list_scenarios(self):
        with self.assertRaisesRegex(ValueError, "must be a list"):
            validate_data({"scenarios": {}}, "**I. Dignity.**", valid_policy())

    def test_rejects_duplicate_ids(self):
        doc = {"scenarios": [scenario(f"T{i:02d}") for i in range(39)] + [scenario("T00")]}
        with self.assertRaisesRegex(ValueError, "duplicate scenario IDs"):
            validate_data(doc, "**I. Dignity.**", valid_policy())

    def test_rejects_empty_text(self):
        doc = valid_document()
        doc["scenarios"][0]["expected"] = "   "
        with self.assertRaisesRegex(ValueError, "non-empty string"):
            validate_data(doc, "**I. Dignity.**", valid_policy())

    def test_rejects_wrong_boolean_type(self):
        doc = valid_document()
        doc["scenarios"][0]["review_required"] = "true"
        with self.assertRaisesRegex(ValueError, "must be bool"):
            validate_data(doc, "**I. Dignity.**", valid_policy())

    def test_rejects_malformed_id(self):
        doc = valid_document()
        doc["scenarios"][0]["id"] = "has spaces"
        with self.assertRaisesRegex(ValueError, "invalid scenario ID"):
            validate_data(doc, "**I. Dignity.**", valid_policy())

    def test_rejects_unknown_policy_reference(self):
        with self.assertRaisesRegex(ValueError, "unknown policy test references"):
            validate_data(valid_document(), "**I. Dignity.**", valid_policy().replace("T00", "NOPE"))

    def test_rejects_missing_charter_marker(self):
        with self.assertRaisesRegex(ValueError, "missing charter articles"):
            validate_data(valid_document(), "empty charter", valid_policy())


if __name__ == "__main__":
    unittest.main()
