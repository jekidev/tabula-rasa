import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from policy_gate import decide

NOW = datetime(2026, 10, 9, tzinfo=timezone.utc)
REQUEST = {"principal": "agent-1", "action": "write", "resource": "document-7", "scope": "paragraph-2"}
GRANT = {**REQUEST, "expires_at": "2026-10-10T00:00:00Z", "approved_by": "human-1"}

class PolicyGateTests(unittest.TestCase):
    def test_valid_scoped_grant(self):
        self.assertTrue(decide(REQUEST, GRANT, NOW)["allow"])

    def test_missing_grant_denied(self):
        self.assertFalse(decide(REQUEST, {}, NOW)["allow"])

    def test_expired_denied(self):
        self.assertFalse(decide(REQUEST, {**GRANT, "expires_at": "2026-10-08T00:00:00Z"}, NOW)["allow"])

    def test_scope_mismatch_denied(self):
        self.assertFalse(decide({**REQUEST, "scope": "whole-document"}, GRANT, NOW)["allow"])

    def test_unknown_action_denied(self):
        self.assertFalse(decide({**REQUEST, "action": "replicate"}, {**GRANT, "action": "replicate"}, NOW)["allow"])

    def test_publish_needs_independent_review(self):
        req = {**REQUEST, "action": "publish"}
        self.assertFalse(decide(req, {**GRANT, "action": "publish"}, NOW)["allow"])
        self.assertTrue(decide(req, {**GRANT, "action": "publish", "independent_review": True}, NOW)["allow"])

    def test_self_approval_denied(self):
        req = {**REQUEST, "action": "delete"}
        grant = {**GRANT, "action": "delete", "approved_by": "agent-1", "independent_review": True}
        self.assertFalse(decide(req, grant, NOW)["allow"])

    def test_naive_expiry_denied(self):
        self.assertFalse(decide(REQUEST, {**GRANT, "expires_at": "2026-10-10T00:00:00"}, NOW)["allow"])

if __name__ == "__main__":
    unittest.main()
