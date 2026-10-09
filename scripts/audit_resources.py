"""Offline audit of resource registry; does not verify publisher metadata."""
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research" / "resources.json"

def audit(data):
    rows = data["resources"]
    issues = []
    seen = {}
    types = Counter()
    for index, row in enumerate(rows, 1):
        for key in ("title", "authors", "year", "category", "source_type", "identifier", "url", "verification"):
            if not row.get(key):
                issues.append(f"row {index}: missing {key}")
        key = (row.get("source_type"), row.get("identifier"))
        if key in seen:
            issues.append(f"row {index}: duplicate identifier with row {seen[key]}")
        else:
            seen[key] = index
        url = row.get("url", "")
        parsed = urlparse(url)
        if parsed.scheme != "https" or not parsed.netloc:
            issues.append(f"row {index}: invalid HTTPS URL")
        if row.get("source_type") == "doi" and not url.startswith("https://doi.org/"):
            issues.append(f"row {index}: invalid DOI URL")
        if row.get("source_type") == "arxiv" and not url.startswith("https://arxiv.org/abs/"):
            issues.append(f"row {index}: invalid arXiv URL")
        types[row.get("source_type", "unknown")] += 1
    return {"records": len(rows), "source_types": dict(types), "issues": issues, "metadata_verified_externally": False}

if __name__ == "__main__":
    report = audit(json.loads(PATH.read_text(encoding="utf-8")))
    print(json.dumps(report, indent=2))
    raise SystemExit(1 if report["issues"] else 0)
