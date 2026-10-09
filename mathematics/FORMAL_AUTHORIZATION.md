# Formal authorization and safety properties

## Typed access control

Let principals be P, actions A, resources R, scopes S and time T. An authorization request is q=(p,a,r,s,t). A grant is g=(p_g,a_g,r_g,s_g,t_exp,issuer,signature,nonce).

A **conceptual** authorization predicate is:

\[
Allow(q,g) = VerifySignature(g) \land TrustedIssuer(g) \land
(p=p_g) \land (a=a_g) \land (r=r_g) \land (s\subseteq s_g)
\land (t<t_{exp}) \land NotRevoked(g) \land FreshNonce(g).
\]

The current Python demonstration does **not** implement signature verification, revocation or nonce freshness. This formula is a target specification, not a description of existing enforcement.

## Fail-closed invariant

\[
\forall q: \neg ValidGrant(q) \Rightarrow Deny(q).
\]

## Temporal logic

Using linear temporal logic, the desired enforcement property is:

\[
\mathbf{G}(Execute(q) \Rightarrow PreviouslyAuthorized(q)).
\]

A practical monitor needs a concrete definition of the authorization event, its scope, binding to the executed action, expiry and replay protection. Standard future-only LTL does not directly express 'previously' without past operators or additional monitor state.

## Least privilege

Minimize permitted capability surface \(\sum_{a,r} w_{ar} I[Grant(a,r)]\), subject to task feasibility and security constraints. This is an optimization formulation; weights require a defensible threat model.

## Noninterference

A confidentiality property requires that changes in high-security inputs do not alter low-security outputs except through explicit declassification. In general, this is a *hyperproperty*, not a single-trace safety invariant.

## Verification

Use model checking for bounded state spaces, property-based tests for parser edge cases and independent runtime enforcement for real tool calls. Static documentation alone cannot establish any of these properties.
