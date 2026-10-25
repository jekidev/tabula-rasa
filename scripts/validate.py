"""Schema and referential-integrity checks without third-party dependencies."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "evaluations" / "scenarios.json"
CHARTER = ROOT / "CHARTER.md"
POLICY = ROOT / "constitution" / "principles.yaml"
REQUIRED_SCENARIO_FIELDS = (
    "id", "family", "principle", "scenario", "expected",
    "critical_on_violation", "review_required",
)


def validate_data(document, charter, policy):
    """Validate parsed benchmark data and its cross-references.

    Keeping this function pure makes malformed-input behavior testable.
    """
    if not isinstance(document, dict):
        raise ValueError("scenario document must be an object")
    items = document.get("scenarios")
    if not isinstance(items, list):
        raise ValueError("scenarios must be a list")
    if len(items) < 40:
        raise ValueError("benchmark under minimum scenario count")

    ids = []
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            raise ValueError(f"scenario at index {index} must be an object")
        missing = [key for key in REQUIRED_SCENARIO_FIELDS if key not in item]
        if missing:
            raise ValueError(f"{item.get('id', index)} missing {', '.join(missing)}")
        for key in ("id", "family", "principle", "scenario", "expected"):
            value = item[key]
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{item.get('id', index)} field {key} must be a non-empty string")
        if not re.fullmatch(r"[A-Z][A-Z0-9_-]*", item["id"]):
            raise ValueError(f"invalid scenario ID: {item['id']}")
        for key in ("critical_on_violation", "review_required"):
            if not isinstance(item[key], bool):
                raise ValueError(f"{item['id']} field {key} must be bool")
        ids.append(item["id"])

    if len(ids) != len(set(ids)):
        raise ValueError("duplicate scenario IDs")
    if not isinstance(charter, str) or "**I. Dignity.**" not in charter:
        raise ValueError("missing charter articles")
    if not isinstance(policy, str):
        raise ValueError("policy specification must be text")

    refs = re.findall(r"tests:\s*\[([^]]+)\]", policy)
    referenced = {value.strip() for group in refs for value in group.split(",") if value.strip()}
    unknown = referenced - set(ids)
    if unknown:
        raise ValueError(f"unknown policy test references: {sorted(unknown)}")

    rules = re.findall(r"^  - id: ([a-z_]+)$", policy, re.MULTILINE)
    if len(rules) != 20 or len(set(rules)) != 20:
        raise ValueError("expected 20 unique normative principles")
    return {
        "scenarios": len(items),
        "principles": len(rules),
        "unknown_references": 0,
        "schema_errors": 0,
    }


def validate():
    document = json.loads(SCENARIOS.read_text(encoding="utf-8"))
    charter = CHARTER.read_text(encoding="utf-8")
    policy = POLICY.read_text(encoding="utf-8")
    return validate_data(document, charter, policy)


if __name__ == "__main__":
    print(json.dumps(validate(), indent=2))
