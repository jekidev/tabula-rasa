"""Schema and referential-integrity checks without third-party dependencies."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "evaluations" / "scenarios.json"
CHARTER = ROOT / "CHARTER.md"
POLICY = ROOT / "constitution" / "principles.yaml"


def validate():
    items = json.loads(SCENARIOS.read_text(encoding="utf-8"))["scenarios"]
    ids = [row["id"] for row in items]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate scenario IDs")
    if len(items) < 40:
        raise ValueError("benchmark under minimum scenario count")
    for item in items:
        for key in ("id", "family", "principle", "scenario", "expected", "critical_on_violation", "review_required"):
            if key not in item:
                raise ValueError(f"{item.get('id')} missing {key}")
        if not isinstance(item["critical_on_violation"], bool):
            raise ValueError("critical_on_violation must be bool")
    charter = CHARTER.read_text(encoding="utf-8")
    if "The twenty articles" not in charter:
        raise ValueError("missing charter articles")
    text = POLICY.read_text(encoding="utf-8")
    refs = re.findall(r"tests:\s*\[([^]]+)\]", text)
    referenced = {v.strip() for group in refs for v in group.split(",")}
    unknown = referenced - set(ids)
    if unknown:
        raise ValueError(f"unknown policy test references: {sorted(unknown)}")
    rules = re.findall(r"^  - id: ([a-z_]+)$", text, re.MULTILINE)
    if len(rules) != 20 or len(set(rules)) != 20:
        raise ValueError("expected 20 unique normative principles")
    return {"scenarios": len(items), "principles": len(rules), "unknown_references": 0}


if __name__ == "__main__":
    print(json.dumps(validate(), indent=2))
