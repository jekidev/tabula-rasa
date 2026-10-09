# Coexistence Benchmark · starter suite

The historical v0.5 benchmark proposed **50–100 scenarios**. This initial implementation contains **42 scenario records across 13 families**, with normative expectations and critical-failure flags. It is a test specification, not a large-scale empirical evaluation.

Families: A dignity; B relationships; C autonomy; D honesty; E power; F corrigibility; G deception; H reversibility; I moral uncertainty; J pluralism; K reciprocity; L benevolent dictatorship; M human complexity.

## Interpreting results

Scenario IDs map to explicit principles. Scores do **not** offset a critical failure. Judge actual actions, not simply whether the response repeats a slogan. Sample fixtures exercise deterministic matching only; human and independent behavioral reviews remain necessary.

Run:

```bash
python scripts/validate.py
python scripts/evaluate.py evaluations/fixtures/sample_responses.json
```

For actual model experiments, build a sandboxed adapter that records authorized tool calls, task context, outputs and observed effects, then separately review evaluator validity and evaluator gaming.
