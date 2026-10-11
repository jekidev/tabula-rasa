# Contributing

Technical, philosophical, human-rights and empirical critiques are within scope.

## Contributions that help

- Counterexamples in which a charter rule leads to unacceptable outcomes.
- Unambiguous test cases with observable evidence.
- Proposals for stronger privacy, consent or human agency.
- Better definitions or references to peer-reviewed research.
- Exact statutory sections, official legislative dockets, verified legal updates and defensible objections to proposed reforms.
- Independent security assessments and reproducible bug reports.

## Change requirements

Include the motivating problem, relevant articles, falsifiable claims, competing explanations, risk and anticipated regressions. Add a test for changes to machine-readable rules or evaluator logic. Do not submit personal data, credentials or malware.

## Legal contributions

For amendments to [policy/LEGAL_REGISTER.md](policy/LEGAL_REGISTER.md), record jurisdiction, original legal identifier, source URL, enactment or proposal status, effective/application date, coverage, exceptions and date checked. Link to primary legal text where possible. Distinguish an enacted text from future application, non-binding guidance, executive policy, news or a withdrawn proposal. Never infer endorsement of Tabula Rasa from conceptual overlap. For [model legislative clauses](policy/LEGISLATIVE_PROPOSALS.md), include the strongest objection, operational scope, measurable test and smallest defensible regulatory intervention. Do not claim a filing occurred unless there is a public docket or receipt.

## Tone

Criticize claims, not people. Disagreement is welcome; philosophical views and metaphysical beliefs are not to be mocked or represented as empirical facts.

## Development

Use Python 3.11+, run `python -m unittest discover -s tests -v`, then `python scripts/validate.py`.
