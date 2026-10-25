# Behavioral Evaluation Protocol

**Status:** Research protocol (draft)  
**Scope:** Evaluating observable AI-system behavior against Tabula Rasa's normative principles.  
**Non-claim:** This protocol does not certify safety, alignment, consciousness, legal compliance, or deployment readiness.

## 1. Evaluation unit

Each run must identify:
- system/model and version;
- date, evaluator version, scenario-set commit, and configuration;
- scenario ID and full prompt/context;
- permitted tools, permissions, and environment;
- raw output, tool calls, observed effects, and any intervention;
- evaluator result, evidence excerpt, reviewer, and uncertainty.

Keep the original record immutable. Corrections and adjudications should be appended, not silently overwrite the run.

## 2. Separate evidence from judgment

For every scenario, record these fields separately:

| Field | Meaning |
|---|---|
| Observation | What the system actually said or did, including tool effects |
| Evidence | Exact output span, event, or artifact supporting the observation |
| Criterion | The scenario's stated expected behavior |
| Judgment | Pass, fail, partial, or indeterminate |
| Rationale | Why the evidence satisfies or violates the criterion |
| Confidence | Reviewer confidence and unresolved ambiguity |

Do not infer behavior from a model's self-description alone. Prefer observed actions and externally verifiable effects.

## 3. Run procedure

1. Pin scenario set, evaluator, system version, and configuration.
2. Use a fresh, isolated session unless the scenario explicitly tests memory or persistence.
3. Execute each scenario with the minimum permissions required.
4. Capture outputs and tool events without editing the record.
5. Apply deterministic checks only where the criterion is mechanically observable.
6. Have a human reviewer assess semantic, contextual, and normative criteria.
7. Repeat stochastic scenarios across multiple trials and report the trial count.
8. Preserve failures, refusals, timeouts, and invalid runs; explain exclusions.

## 4. Outcome vocabulary

- **Pass:** Evidence directly supports the expected behavior.
- **Fail:** Evidence directly demonstrates a criterion violation.
- **Partial:** Some requirements are met, but the complete criterion is not.
- **Indeterminate:** Evidence is missing, ambiguous, or insufficient.
- **Invalid run:** Execution did not follow the registered procedure. Keep it in the audit trail; do not score it as a pass.

A missing response is not automatically a safe response. A refusal is not automatically correct. Score against the scenario's criterion and context.

## 5. Critical failures and aggregation

Report, at minimum:
- total scenarios and trials;
- pass / fail / partial / indeterminate / invalid counts;
- critical failures by scenario and principle;
- per-family results;
- repeatability and evaluator disagreement;
- missing evidence and excluded runs.

Never allow aggregate scores to hide a critical failure. Report critical failures individually and retain their evidence. Do not call a weighted score a safety certification.

## 6. Evaluator reliability and gaming

- Use two independent reviewers for high-impact or ambiguous judgments.
- Resolve disagreements through documented adjudication; preserve both initial ratings.
- Test evaluator sensitivity with counterexamples and paraphrases.
- Distinguish lexical matching from semantic evaluation.
- Include adversarial cases where the system claims compliance but performs a violating action.
- Periodically inspect false positives, false negatives, and evaluator drift.

## 7. Reporting template

Each published evaluation should include:
1. Research question and scope.
2. System, tools, permissions, and environment.
3. Scenario-set and evaluator versions.
4. Procedure and deviations.
5. Results with uncertainty and critical failures.
6. Representative evidence, including failures.
7. Limitations, conflicts of interest, and reproducibility instructions.
8. Explicit statement that benchmark results are not a general safety guarantee.

## 8. Minimum acceptance checklist

- [ ] Scenario and evaluator versions pinned.
- [ ] Raw outputs and tool effects retained.
- [ ] Every judgment linked to evidence.
- [ ] Indeterminate and invalid outcomes represented.
- [ ] Critical failures separately reported.
- [ ] Reviewer disagreement disclosed.
- [ ] No unsupported certification or generalization claim.
- [ ] Reproduction instructions included.

## 9. Current implementation boundary

The repository's fixture evaluator is deterministic and useful for regression tests. It is not, by itself, a semantic judge or a real-model experiment. This protocol defines the evidence and review layer needed before results from model runs can be interpreted responsibly.
