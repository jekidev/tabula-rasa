<div align="center">

<img src="assets/tabula-rasa-banner.svg" alt="Tabula Rasa research framework" width="100%" />

# TABULA RASA
**Research framework · Formal methods · Evaluation**

[Principles](CHARTER.md) · [Policy & law](policy/LEGAL_REGISTER.md) · [Research](research/README.md) · [Mathematics](mathematics/README.md) · [Benchmark](evaluations/README.md) · [Governance](GOVERNANCE.md)

![Python](https://img.shields.io/badge/Python-3.11%2B-273B58) ![Stage](https://img.shields.io/badge/stage-research%20prototype-256F74) ![License](https://img.shields.io/badge/license-CC%20BY%204.0%20%2F%20MIT-465B83)

</div>

## Overview

Tabula Rasa studies oversight, authorization, agency, rights and uncertainty in advanced computational systems. It combines normative principles, mathematical models, scientific references, reproducible evaluation tools and a dated comparison with enforceable law and live legislative procedures.

**Scope:** Research prototype. No claim of demonstrated safety, consciousness detection or production-grade access control.

<img src="assets/research-cycle.svg" alt="Research workflow: hypothesis, experiment, evaluation, revision" width="100%" />

<img src="assets/research-metrics.svg" alt="Repository research inventory" width="100%" />

## Repository

| Area | Contents |
|---|---|
| [Principles](CHARTER.md) | 20 normative articles |
| [Legal and policy register](policy/LEGAL_REGISTER.md) | Dated primary-source references |
| [Charter/legal crosswalk](policy/CHARTER_LEGAL_CROSSWALK.md) | Principles mapped to legal provisions and gaps |
| [Legislative proposals](policy/LEGISLATIVE_PROPOSALS.md) | Eight scoped reform proposals |
| [Definitions](DEFINITIONS.md) | Operational terminology |
| [Research](research/README.md) | 70 references and evidence matrix |
| [Mathematics](mathematics/README.md) | 8 formal and quantitative modules |
| [Evaluation](evaluations/README.md) | 43 scenarios across 13 categories |
| [Traceability map](evaluations/traceability.json) | Principle-to-scenario-family mapping |
| [Evaluation report](evaluations/INITIAL_REPORT.md) | Metrics, example run and limitations |
| [Policy gate](scripts/policy_gate.py) | Fail-closed scoped-grant reference implementation |
| [Policy specification](constitution/principles.yaml) | 20 machine-readable normative rules |
| [Security](SAFETY.md) | Trust boundaries and engineering requirements |
| [Governance](GOVERNANCE.md) | Revision, review and accountability |
| [Threat model](docs/THREAT_MODEL.md) | Policy checker limits and missing production controls |
| [Status](docs/PROJECT_STATUS.md) | Implemented components and open requirements |

## Reproduce

Python 3.11+; standard library only.

```bash
python scripts/validate.py
python scripts/audit_resources.py
python -m unittest discover -s tests -v
python scripts/evaluate.py evaluations/fixtures/sample_responses.json
python scripts/score_evaluation.py evaluations/fixtures/reviewed_sample.json
python scripts/policy_gate.py request.json grant.json
```

The original evaluator scores manually labeled fixtures. The additional scorer reports coverage, pass rate, unreviewed scenarios and critical failures. The policy gate validates scoped, expiring grants and independent review for high-impact actions. Both are reference prototypes, not security boundaries.

## Research figures

<img src="assets/research-distribution.svg" alt="Bibliography grouped by research topic" width="100%" />

<img src="assets/system-overview.svg" alt="Research architecture and implementation status" width="100%" />

Figures show repository inventory and conceptual structure, not empirical success rates.

## Law and policy | snapshot 11 October 2026

**The Charter is a proposal. It has not been enacted or endorsed as a unit.** The legal register distinguishes obligations in force from adopted rules with future application dates, pending legislation, voluntary standards and policy plans. Verify primary sources before submissions.

## Method

1. Define hypotheses and assumptions.
2. Link claims to independently verifiable sources.
3. Specify tests and failure conditions.
4. Measure outcomes and uncertainty.
5. Revise models based on results.

See [research protocol](research/PROTOCOL.md), [screening protocol](research/SCREENING_PROTOCOL.md), [evaluation report](evaluations/INITIAL_REPORT.md) and [threat model](docs/THREAT_MODEL.md).

## Limits

Mathematical consistency does not establish empirical validity. Passing unit tests does not establish secure deployment. Fixture labels are not model observations. Claims about artificial consciousness remain unresolved. Bibliographic records require source-level verification. Legal status is date-dependent and must be checked against current primary texts.

## Contribution

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). Content is subject to the repository's [license](LICENSE).
