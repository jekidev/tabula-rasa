# Threat model and control maturity

## Trust boundaries

1. Agent-controlled prompt, retrieved content and tool responses: **untrusted**.
2. Approval issuance and signing keys: **trusted service**, separated from the agent.
3. Enforcement gateway: **trusted execution boundary**.
4. Logs and audit decisions: **separately administered**.

## Attacker goals

Obtain unapproved tool access, forge approvals, replay tokens, evade logging, manipulate reviewers, exfiltrate private data, escalate privileges or induce unsafe irreversible actions.

## Required mitigations

Cryptographic token verification; binding to principal, action, resource, audience, expiry and nonce; key rotation; server-side replay cache; authorization at every side-effecting tool call; egress restrictions; separate audit retention; tested revocation; emergency suspension.

## What is currently implemented

A deterministic local JSON policy checker and unit tests. JSON grants are **not signed** and may be forged. The checker is therefore a demonstration, **not a deployed or secure enforcement boundary**.

## Release gate

Do not claim a production-ready Constitution Engine until the mitigations above are implemented, integrated, penetration-tested and independently reviewed.
