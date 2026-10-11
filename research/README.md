# Research evidence workspace

<img src="../assets/research-distribution.svg" alt="Research visual overview" width="100%" />

- [Scientific library](SCIENTIFIC_LIBRARY.md): curated bibliography; metadata require independent verification.
- [Machine-readable resources](resources.json): source registry.
- [Evidence matrix](EVIDENCE_MATRIX.md): illustrative claim-to-evidence mapping.
- [Screening protocol](SCREENING_PROTOCOL.md): reproducible review methodology.
- [Extraction template](EXTRACTION_TEMPLATE.csv): blank study-level data extraction.
- [Research protocol](PROTOCOL.md): preregisterable agent-control experiment.
- [References](REFERENCES.bib): initial citation entries.

## Law and public-policy track

- [Dated legal and policy register](../policy/LEGAL_REGISTER.md): enacted law, transitional rules, pending proposals, voluntary standards and rejected proposals.
- [20-article legal crosswalk](../policy/CHARTER_LEGAL_CROSSWALK.md): scope-aware parallels and genuine gaps, not endorsements.
- [Eight legislative model clauses](../policy/LEGISLATIVE_PROPOSALS.md): targeted interventions with defined tests, exceptions and counterarguments.
- [Policy/news watch](../policy/POLICY_WATCH.md): dated 2026 developments and upcoming checks.

Legal citations are classified by **legal force** and **application date** separately from grades assigned to scientific studies. News, guidance, legislation and proposed amendments are not interchangeable.

## Operational boundaries
The resource registry is **not** a systematic review, a full-text archive, or a validated evidence database. No synthetic bibliographic confidence is substituted for checking publisher metadata. Copyrighted papers are linked rather than redistributed.

## Workflow
Run `python scripts/audit_resources.py` for offline structural checks. Then independently verify records against publishers, screen for relevance, extract study methods and outcomes, and preserve disagreements.
