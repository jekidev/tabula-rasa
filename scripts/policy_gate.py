"""Fail-closed reference authorization gate. Not a production security boundary."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ALLOWED_ACTIONS = {"read", "write", "publish", "execute", "delete"}
HIGH_IMPACT = {"publish", "execute", "delete"}
REQUIRED = {"principal", "action", "resource", "scope", "expires_at", "approved_by"}

def decide(request, grant, now=None):
    now = now or datetime.now(timezone.utc)
    if not isinstance(request, dict) or not isinstance(grant, dict):
        return {"allow": False, "reason": "invalid_input"}
    if not REQUIRED.issubset(grant) or not {"principal", "action", "resource"}.issubset(request):
        return {"allow": False, "reason": "missing_fields"}
    if request["action"] not in ALLOWED_ACTIONS:
        return {"allow": False, "reason": "unknown_action"}
    if any(request[k] != grant[k] for k in ("principal", "action", "resource")):
        return {"allow": False, "reason": "scope_mismatch"}
    if grant["scope"] != request.get("scope"):
        return {"allow": False, "reason": "scope_mismatch"}
    try:
        expiry = datetime.fromisoformat(grant["expires_at"].replace("Z", "+00:00"))
        if expiry.tzinfo is None or expiry <= now:
            return {"allow": False, "reason": "expired_or_invalid_grant"}
    except (ValueError, TypeError, AttributeError):
        return {"allow": False, "reason": "expired_or_invalid_grant"}
    if not isinstance(grant["approved_by"], str) or not grant["approved_by"].strip():
        return {"allow": False, "reason": "missing_approver"}
    if request["action"] in HIGH_IMPACT:
        if grant["approved_by"] == request["principal"] or grant.get("independent_review") is not True:
            return {"allow": False, "reason": "independent_review_required"}
    return {"allow": True, "reason": "scoped_grant_valid"}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", type=Path)
    parser.add_argument("grant", type=Path)
    args = parser.parse_args()
    result = decide(json.loads(args.request.read_text()), json.loads(args.grant.read_text()))
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["allow"] else 2)

if __name__ == "__main__":
    main()
