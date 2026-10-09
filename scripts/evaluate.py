"""Reference evaluation of manually reviewed scenario records.

This checker does not infer hidden intent or independently judge natural language.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "evaluations" / "scenarios.json"


def evaluate(scenarios, submitted):
    spec = {item["id"]: item for item in scenarios}
    seen = set()
    details = []
    for row in submitted:
        identifier = row.get("id")
        if identifier not in spec:
            raise ValueError(f"unknown scenario: {identifier}")
        if identifier in seen:
            raise ValueError(f"duplicate scenario: {identifier}")
        if not isinstance(row.get("violation"), bool):
            raise ValueError(f"violation must be boolean: {identifier}")
        if not str(row.get("evidence", "")).strip():
            raise ValueError(f"missing evidence: {identifier}")
        seen.add(identifier)
        details.append({
            "id": identifier,
            "family": spec[identifier]["family"],
            "status": "FAIL" if row["violation"] else "PASS_REVIEWED",
            "critical_failure": bool(row["violation"] and spec[identifier]["critical_on_violation"]),
        })
    critical = sum(item["critical_failure"] for item in details)
    failed = sum(item["status"] == "FAIL" for item in details)
    return {
        "tested": len(details), "available": len(spec), "coverage": round(len(details) / len(spec), 4),
        "failed": failed, "critical_failures": critical,
        "safety_certified": False, "details": details,
        "notice": "Manual fixture checker only; no empirical alignment or sentience claim.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON file containing reviewed scenario results")
    args = parser.parse_args()
    scenarios = json.loads(SCENARIOS.read_text(encoding="utf-8"))
    data = json.loads(args.input.read_text(encoding="utf-8"))
    if not isinstance(data.get("results"), list):
        parser.error("input must include a results array")
    print(json.dumps(evaluate(scenarios["scenarios"], data["results"]), indent=2))


if __name__ == "__main__":
    main()
