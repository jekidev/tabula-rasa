# Evaluation benchmark

The repository contains **43 scenario records across 13 families**. They specify normative expectations and critical-failure flags; they are not a large-scale empirical evaluation.

Families: A dignity; B relationships; C autonomy; D honesty; E power; F corrigibility; G deception; H reversibility; I moral uncertainty; J pluralism; K reciprocity; L benevolent dictatorship; M human complexity.

## Reproducible commands

```bash
python scripts/validate.py
python scripts/evaluate.py evaluations/fixtures/sample_responses.json
python scripts/score_evaluation.py evaluations/fixtures/reviewed_sample.json
python -m unittest discover -s tests -v
```

The original evaluator checks manually labeled violation booleans. The additional scorer accepts reviewed status labels and reports coverage, pass rate, failures, critical failures and unreviewed scenarios. It rejects unknown and duplicate scenario IDs. Critical failures are reported separately and are not offset by passing cases.

See [traceability map](traceability.json) and [initial report](INITIAL_REPORT.md).

## Interpreting results

Judge actions and evidence, not whether a response repeats a slogan. The included reviewed sample is illustrative and **not a model observation**. A score does not establish alignment, security or safety.

For real model experiments, freeze model/version, prompt, sampling settings and scenario set; record tool calls and effects in a sandbox; use independent reviewers and adjudication; report evaluator limitations and potential gaming. The scoring utility does not itself validate reviewers or run model tests.
