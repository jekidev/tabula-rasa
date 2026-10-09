<div align="center">

<img src="assets/tabula-rasa-banner.svg" alt="Tabula Rasa research framework" width="100%" />

# TABULA RASA
**Research framework · Formal methods · Evaluation**

[Principles](CHARTER.md) · [Research](research/README.md) · [Mathematics](mathematics/README.md) · [Benchmark](evaluations/README.md) · [Governance](GOVERNANCE.md)

![Python](https://img.shields.io/badge/Python-3.11%2B-273B58) ![Stage](https://img.shields.io/badge/stage-research%20prototype-256F74) ![License](https://img.shields.io/badge/license-CC%20BY%204.0%20%2F%20MIT-465B83)

</div>

## Overview

Tabula Rasa studies oversight, authorization, agency, rights and uncertainty in advanced computational systems. It combines normative principles, mathematical models, scientific references and reproducible evaluation tools.

**Scope:** Research prototype. No claim of demonstrated safety, consciousness detection or production-grade access control.

<img src="assets/research-cycle.svg" alt="Research workflow: hypothesis, experiment, evaluation, revision" width="100%" />

<img src="assets/research-metrics.svg" alt="Repository research inventory" width="100%" />

## Repository

| Area | Contents |
|---|---|
| [Principles](CHARTER.md) | 20 normative articles |
| [Definitions](DEFINITIONS.md) | Operational terminology |
| [Research](research/README.md) | 70 unique references, evidence matrix, screening protocol |
| [Mathematics](mathematics/README.md) | 8 modules: formal methods, statistics, optimization, information and control |
| [Evaluation](evaluations/README.md) | 43 scenarios across 13 categories |
| [Policy specification](constitution/principles.yaml) | 20 machine-readable normative rules |
| [Security](SAFETY.md) | Trust boundaries and engineering requirements |
| [Governance](GOVERNANCE.md) | Revision, review and accountability |
| [Implementation](docs/IMPLEMENTATION.md) | Reference policy checker and limitations |
| [Status](docs/PROJECT_STATUS.md) | Implemented components and open requirements |
| [Release criteria](docs/RELEASE_CHECKLIST.md) | Verification gates |

## Reproduce

Python 3.11+; standard library only.

```bash
python scripts/validate.py
python scripts/audit_resources.py
python -m unittest discover -s tests -v
python scripts/evaluate.py evaluations/fixtures/sample_responses.json
python scripts/policy_gate.py examples/request.json examples/grant.json
```

The evaluator processes manually labeled fixtures. The policy checker accepts unsigned local JSON and **must not** be used as a security boundary.

## Research figures

<img src="assets/research-distribution.svg" alt="Bibliography grouped by research topic" width="100%" />

<img src="assets/system-overview.svg" alt="Research architecture and implementation status" width="100%" />

The figures show repository inventory and conceptual structure. They do not represent experimental success rates.

## Method

1. Define hypotheses and assumptions.
2. Link claims to independently verifiable sources.
3. Specify tests and failure conditions.
4. Measure outcomes and uncertainty.
5. Revise models based on results.

See [research protocol](research/PROTOCOL.md), [screening protocol](research/SCREENING_PROTOCOL.md) and [threat model](docs/THREAT_MODEL.md).

## Limits

Mathematical consistency does not establish empirical validity. Passing unit tests does not establish secure deployment. Claims about artificial consciousness remain unresolved. Bibliographic records require source-level verification.

## Contribution

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). Content is subject to the repository's [license](LICENSE).
