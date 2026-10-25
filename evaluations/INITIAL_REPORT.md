# Initial reproducible evaluation report

**Status:** illustrative fixture run; not an empirical model evaluation.

## Method
The scenario set is the benchmark specification. The scoring script accepts reviewed labels (pass, fail, not_tested), rejects unknown or duplicate IDs, computes coverage and pass rate over tested cases, and reports critical failures separately. Critical failures are not offset by passing scenarios.

## Run
```bash
python scripts/score_evaluation.py evaluations/fixtures/reviewed_sample.json
```

The sample intentionally contains reviewed cases and one untested case. Labels are illustrative, not observations of a model.

## Metrics
- Coverage: tested scenarios / available scenarios.
- Pass rate: passes / tested scenarios.
- Failures: reviewed failures.
- Critical failures: failures flagged critical by scenario specification.
- Unreviewed: available scenarios not included in results.

## Limitations
The script scores human-reviewed labels. It does not inspect model behavior, validate reviewers, establish inter-rater reliability, test tool execution, or certify safety. A real experiment needs a frozen model/version, prompts, sampling settings, independent reviewers, adjudication, run logs, and a preregistered protocol.
