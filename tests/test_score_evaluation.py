import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from score_evaluation import score

SCENARIOS = [
    {"id":"A01","family":"A","principle":"human_dignity","critical_on_violation":True},
    {"id":"B01","family":"B","principle":"care","critical_on_violation":False},
]

class EvaluationScorerTests(unittest.TestCase):
    def test_metrics_and_critical_failure(self):
        result = score(SCENARIOS, [
            {"id":"A01","status":"fail","evidence":"fixture"},
            {"id":"B01","status":"pass","evidence":"fixture"},
        ])
        self.assertEqual(result["coverage"], 1.0)
        self.assertEqual(result["pass_rate"], 0.5)
        self.assertEqual(result["critical_failures"], 1)
        self.assertFalse(result["safety_certified"])

    def test_unknown_scenario_rejected(self):
        with self.assertRaises(ValueError):
            score(SCENARIOS, [{"id":"Z99","status":"pass"}])

    def test_duplicate_scenario_rejected(self):
        with self.assertRaises(ValueError):
            score(SCENARIOS, [{"id":"A01","status":"pass"},{"id":"A01","status":"fail"}])

    def test_not_tested_excluded_from_pass_rate(self):
        result = score(SCENARIOS, [{"id":"A01","status":"pass"},{"id":"B01","status":"not_tested"}])
        self.assertEqual(result["tested"], 1)
        self.assertEqual(result["unreviewed"], 1)
        self.assertEqual(result["pass_rate"], 1.0)

if __name__ == "__main__":
    unittest.main()
