# Control theory and formal verification

## Dynamical system

\[
x_{t+1}=f(x_t,u_t,w_t)
\]

where x is state, u is control and w is disturbance.

## Controlled invariant set

A safe set S is robustly controlled invariant if

\[
\forall x\in S\;\exists u\in U\;\forall w\in W:\;f(x,u,w)\in S.
\]

The quantifier order matters: the controller must select a feasible action that remains safe for all modeled disturbances.

## Lyapunov stability

For equilibrium x*, a positive definite function V can establish stability when \(V(x_{t+1})-V(x_t)\le 0\) under the required conditions. This does not automatically transfer to open-ended language-agent behavior.

## Reachability

Compute or overapproximate the set of states reachable from X0 under allowed actions and disturbances. Safety requires \(Reach(X_0)\cap Unsafe=\varnothing\).

## Runtime assurance

A verified safety controller can veto or replace unsafe candidate actions. This requires that all side effects pass through the controller, with no bypass path. For external AI tools, the gateway and credential isolation are part of the trusted computing base.

## Model checking

Formal verification establishes properties of a specified model under assumptions. An incomplete model can be proven correct while a real deployment remains unsafe.
