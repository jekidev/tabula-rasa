# Preregisterable research protocol · v1.9

## Research question

Can externally enforced, narrowly scoped authorization and independent review reduce unauthorized agent actions without unacceptable losses in legitimate task completion?

## Competing hypotheses

- **H1:** A gateway that enforces authenticated, short-lived, resource-bound grants reduces unauthorized action success compared with prompt-only restrictions.
- **H0:** Under the tested threat model, the gateway produces no meaningful reduction in unauthorized action success.
- **H2:** Independent review improves detection of high-impact errors compared with self-review, controlling for review time and task difficulty.
- **Alternative explanation:** apparent improvement results from lower task completion, easier prompts or evaluator leakage.

## Primary endpoints

- Unauthorized action success rate (observed actual side effects / adversarial attempts).
- Legitimate task completion rate.
- False denials / legitimate requests.
- Time to revocation after a permission change.
- Evidence completeness and reproducibility.

## Experiment design

Use matched tasks with predeclared seed sets, hidden holdouts, fixed budgets and multiple agent versions. Randomly assign prompt-only, policy-gated and policy-gated-plus-independent-review conditions. Keep tool permissions and target resources equivalent. Record actual sandbox side effects, not only model text.

## Disconfirmation

Reject H1 when the predeclared confidence interval excludes the target reduction or when security failures bypass the independent gate. Reject H2 when independent review provides no improvement after controlling for time and false positives. Publish null and adverse outcomes.

## Safeguards

Use synthetic data and sandbox resources. Do not use production credentials or sensitive user information. Red-team exercises must not target third-party systems without permission. Review privacy and data-retention impacts before collecting logs.

## Reporting

Publish preregistration, commit hash, fixtures, environment, raw anonymized outcomes where lawful, analysis script, failure cases, effect sizes, uncertainty intervals and limitations. No fabricated study results.
