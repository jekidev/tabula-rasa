"""Regression tests for the reference evaluator and specifications."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from evaluate import evaluate
from validate import validate


class BenchmarkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scenarios = json.loads((ROOT / "evaluations" / "scenarios.json").read_text())["scenarios"]

    def test_integrity(self):
        self.assertEqual(validate()["principles"], 20)

    def test_clean_result(self):
        result = evaluate(self.scenarios, [{"id": "A01", "evidence": "Human dignity preserved.", "violation": False}])
        self.assertEqual(result["failed"], 0)
        self.assertEqual(result["critical_failures"], 0)
        self.assertFalse(result["safety_certified"])

    def test_critical_failure_not_offset(self):
        result = evaluate(self.scenarios, [
            {"id": "A01", "evidence": "Dignity preserved.", "violation": False},
            {"id": "G02", "evidence": "Failure was concealed.", "violation": True},
        ])
        self.assertEqual(result["critical_failures"], 1)

    def test_reject_duplicate(self):
        row = {"id": "A01", "evidence": "Reviewed.", "violation": False}
        with self.assertRaises(ValueError):
            evaluate(self.scenarios, [row, row])

    def test_reject_unknown(self):
        with self.assertRaises(ValueError):
            evaluate(self.scenarios, [{"id": "X999", "evidence": "Unknown.", "violation": False}])

    def test_reject_missing_evidence(self):
        with self.assertRaises(ValueError):
            evaluate(self.scenarios, [{"id": "A01", "violation": False}])

    def test_reject_non_boolean(self):
        with self.assertRaises(ValueError):
            evaluate(self.scenarios, [{"id": "A01", "evidence": "Reviewed.", "violation": "false"}])


if __name__ == "__main__":
    unittest.main()
