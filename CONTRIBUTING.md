# Contributing to Tabula Rasa

We welcome technical, philosophical, human-rights and empirical critiques.

## Contributions that help

- Counterexamples in which a charter rule leads to unacceptable outcomes.
- Unambiguous test cases with observable evidence.
- Proposals for stronger privacy, consent or human agency.
- Better definitions or references to peer-reviewed research.
- Independent security assessments and reproducible bug reports.

## Change requirements

Include the motivating problem, relevant articles, falsifiable claims, competing explanations, risk and anticipated regressions. Add a test for changes to machine-readable rules or evaluator logic. Do not submit personal data, credentials or malware.

## Tone

Criticize claims, not people. Disagreement is welcome; philosophical views and metaphysical beliefs are not to be mocked or represented as empirical facts.

## Development

Use Python 3.11+, run `python -m unittest discover -s tests -v`, then `python scripts/validate.py`.
