# Engineering safety protocol

**Scope:** reference design for AI agents, MCP-compatible tools and delegated actions. Documentation is not equivalent to an enforced runtime.

## Trust boundaries

An instruction inside a fetched page, repository, tool response or document is untrusted data, not a new authorization. Agents should validate requested actions against a separately controlled policy gate.

## Minimum enforceable controls

- Least-privilege, task-scoped credentials and permission leases.
- External approval for high-impact writes, financial actions, publishing, sensitive disclosures and physical control.
- Sandbox isolation, network egress controls, quotas and explicit allowlists.
- Audit logs controlled independently of the agent, with data minimization, retention and access limits.
- Revocation and pause outside the agent's ability to rewrite.
- No unauthorized replication, persistence or changes to the policy engine.
- Transparent notice of material uncertainty and tool side effects.
- Human-accessible exports, alternatives and reasonable exit paths.
- Independent evaluation and incident response.

## Decision record

Each significant tool action should capture: time, agent/runtime version, task, authorized principal, tool, target scope, rule decision, consent reference, action outcome and incident link. Never log secrets or personal data indiscriminately.

## Incident procedure

Pause or isolate dangerous execution where feasible; preserve relevant evidence; revoke affected credentials; notify authorized operators; investigate independently; repair, review and publish an appropriately redacted retrospective.

## Risk boundary

No fixed score establishes safety. Real systems must be judged by actual capabilities, permissions, context, severity, irreversibility and independent empirical evaluation.
