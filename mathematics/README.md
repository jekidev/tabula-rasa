# Mathematical foundations of Tabula Rasa

A reproducible collection of formal tools for analyzing AI oversight, authorization, evaluation, epistemic uncertainty and governance. The equations are **models and research instruments**, not proof that a deployed AI system is safe or conscious.

## Modules

1. [Formal authorization](FORMAL_AUTHORIZATION.md): typed requests, deny-by-default predicates, noninterference, temporal constraints.
2. [Decision theory](DECISION_THEORY.md): expected utility, risk-sensitive objectives, robust optimization, constrained MDPs, corrigibility.
3. [Information theory](INFORMATION_THEORY.md): entropy, mutual information, divergence, calibration and evidence.
4. [Statistics and experiments](STATISTICS.md): power, confidence intervals, multiple comparisons, effect sizes, sequential testing.
5. [Game theory and governance](GAME_THEORY.md): incentives, principal-agent problems, mechanism design and voting.
6. [Control and verification](CONTROL_THEORY.md): invariant sets, reachability, Lyapunov stability, model checking.
7. [Uncertainty about consciousness](MORAL_UNCERTAINTY.md): Bayesian uncertainty, moral uncertainty, value of information and epistemic limits.
8. [Executable examples](../scripts/math_models.py) with [regression tests](../tests/test_math_models.py).

## Reproducibility principles

- State assumptions and units for every formula.
- Distinguish mathematical implication from empirical applicability.
- Do not infer causality from correlations or benchmark scores.
- Do not claim a numerical moral-status probability without a justified model and observations.
- Validate numerical calculations against independently specified examples.
