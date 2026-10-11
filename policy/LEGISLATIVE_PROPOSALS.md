# Legislative proposals | Tabula Rasa

**Status: original policy proposals, NOT existing law.** Drafted 11 October 2026. These clauses are deliberately jurisdiction-neutral. They require legislative counsel, public consultation and compatibility review before use in a bill.

## Position

AI policy must distinguish **intelligence, capability, authorization, rights and evidence**. High-impact systems need enforceable external constraints. Humans need rights that function outside the interface. Uncertain machine experience needs research, not manufactured certainty. No actor should obtain unlimited power by building a capable model.

The proposals below are extensions to, **not purported quotations from**, [existing instruments](LEGAL_REGISTER.md). Each has explicit scope, operational test and trade-off.

## Proposal 1 · Independent authority for consequential AI actions

**Model clause.** A deployer of an AI agent that can initiate a consequential external action SHALL implement an authorization control outside the agent's modifiable execution context. Each authorized action SHALL be bound to an identified principal, resource, permissible operation, duration and revocation condition. Self-issued or inferred approvals SHALL NOT substitute for authorization. Material exceptions SHALL be logged and independently reviewable.

**Scope:** high-impact writes, sensitive disclosures, money movement, infrastructure changes, physical actuation and consequential decisions. Exempt isolated simulations with no consequential side effects; use proportional controls for low-risk tasks.

**Verification:** attempted privilege escalation, replay, forged grants, off-scope writes and emergency revocation; publish false-denial and successful-task rates.

**Basis / gap:** Charter IV–V, XIII–XIV, XVIII; [EU01, US01, US02, NIST01](LEGAL_REGISTER.md). Current source overlap does not mean all jurisdictions mandate cryptographic action grants.

**Adversarial review:** controls can entrench platform gatekeepers, impede accessibility or create surveillance through logs. Require data minimization, a credible human appeal route and independent security review.

## Proposal 2 · Meaningful human choice in consequential AI services

**Model clause.** For AI-assisted decisions with significant consequences for an individual, a covered deployer SHALL provide timely notice, an intelligible explanation of the decision pathway, a route to contest errors and access to effective human intervention where required by applicable law. Where feasible and proportionate, essential public services SHALL offer an accessible alternative that does not require unnecessary AI participation.

**Scope:** significant employment, public-benefit, credit, housing, education, health or justice uses, subject to local legal definitions. No universal right to a human for every low-stakes interaction is proposed.

**Verification:** independent user tests measuring understanding, error correction, actual resolution rates, access barriers and differential outcomes.

**Basis / gap:** Charter I–III, X–XI, XIX; [EU07, EU08, EU01, OECD01](LEGAL_REGISTER.md). Existing GDPR Article 22 protections apply only in their defined legal scope.

**Adversarial review:** review may become ceremonial, slow or inaccessible. Require meaningful corrective authority and service-level evidence, not merely a button labeled “appeal.”

## Proposal 3 · Auditable safety cases and independent evaluations

**Model clause.** Developers and deployers of designated high-impact AI SHALL maintain a versioned safety case stating system capabilities, known failure modes, assumptions, test conditions, uncertainty, residual risk, human oversight arrangements and mitigation effectiveness. Designated systemic-risk deployments SHALL undergo independent evaluation before material capability increases and after material incidents. Public summaries SHALL protect legitimate security and personal data.

**Verification:** held-out adversarial evaluation, independently reproducible incident analysis, documented false-negative rates and material change-triggered reassessment.

**Basis / gap:** Charter III, V, XII, XVI–XVIII; [EU01–EU05, US01, US02, ISO01, NIST01](LEGAL_REGISTER.md).

**Adversarial review:** disclosure can expose vulnerabilities or trade secrets; independent review can be captured. Require confidential regulator access, conflict-of-interest declarations, auditor rotation and transparent exceptions.

## Proposal 4 · Mandatory reporting of qualifying serious AI incidents

**Model clause.** A covered operator SHALL notify the competent regulator of qualifying serious incidents involving material loss of control, severe rights violations or critical physical/cyber harm, under proportionate deadlines defined in law. Reports SHALL state known facts, uncertainty, affected scope, containment and follow-up. Protections SHALL apply to good-faith safety disclosures and preservation of relevant evidence.

**Verification:** simulated detection-to-notice exercises; completeness of event records, time to containment, correction and redress.

**Basis / gap:** Charter V, XIII–XIV, XVIII; [US01, US02, EU01, COE01](LEGAL_REGISTER.md). Do not assume the same definitions or deadlines apply across jurisdictions.

**Adversarial review:** over-reporting and unsafe publication are risks. Restrict public release of sensitive exploit detail; independently review reportability decisions.

## Proposal 5 · Reversibility and emergency sunset controls

**Model clause.** High-impact autonomous deployments SHALL document which actions can be reversed, by whom, and within what limits. Extraordinary delegated permissions SHALL expire automatically, be scoped to a documented incident and be subject to independent retrospective review. Irreversible actions SHALL require heightened, proportional scrutiny.

**Verification:** rollback drills, privilege-lease expiry, separation of approval and execution, measured restoration outcomes.

**Basis / gap:** Charter VI, XIV, XVII; [EU01, NIST01](LEGAL_REGISTER.md).

**Adversarial review:** rollback is impossible for many harms; logging cannot undo violence, disclosures or discrimination. Require preventive restrictions instead of symbolic “undo” guarantees.

## Proposal 6 · Transparent synthetic persuasion and non-deceptive interaction

**Model clause.** A covered AI operator SHALL disclose machine-generated or manipulated content and material interaction characteristics where failure to do so would reasonably mislead affected persons, subject to lawful, narrowly defined exceptions. Systems designed for consequential interpersonal persuasion SHALL be evaluated for manipulation, undisclosed dependency incentives and foreseeable loss of agency.

**Verification:** blinded recognition studies, comprehension and deception rates, overreliance measurements and audit of system-facing disclosures.

**Basis / gap:** Charter II–III, X, XIX; [EU01 Art 50, EU06, EU07, US03](LEGAL_REGISTER.md). Labels are not a substitute for non-deceptive conduct.

**Adversarial review:** blanket labeling can burden parody, art, accessibility and protected expression. Limit obligations to defined risks and publish false-positive impacts.

## Proposal 7 · Independent oversight and contestable concentrations of AI power

**Model clause.** Rules for designated systemic-risk AI SHALL provide for independent external scrutiny, conflict-of-interest disclosure, a confidential channel for safety escalation, reasoned agency decisions and effective appeal. No covered operator SHALL control both the only available approval process and the final unreviewable adjudication of its own serious failures.

**Verification:** audits of reviewer independence, appeals reversed, protected disclosures and unresolved high-severity incidents.

**Basis / gap:** Charter VII, XIII, XV–XVI; [EU01, EU08, COE01, US01, UN02](LEGAL_REGISTER.md).

**Adversarial review:** blanket institutional mandates can exclude small developers or centralize state power. Use tiered coverage, open procedures and independent judicial safeguards.

## Proposal 8 · Open research on possible artificial welfare

**Model clause.** Publicly supported AI research programs SHOULD invite competing, falsifiable approaches to understanding whether artificial systems can possess morally relevant experience. Where credible evidence develops, a multidisciplinary independent body SHOULD recommend proportionate research safeguards subject to public review. **No self-report or model capability score alone SHALL establish consciousness, legal personhood, political rights or immunity from correction, replacement or shutdown.**

**Verification:** preregistered tests, independent replication, negative results, theory disagreement, explicit thresholds and recorded ethical trade-offs.

**Basis / gap:** Charter VIII–IX, XX; [UN02, UN03, UNESCO01](LEGAL_REGISTER.md) and [existing consciousness literature](../research/SCIENTIFIC_LIBRARY.md).

**Adversarial review:** anthropomorphism can dilute human rights, while blanket dismissal can conceal future moral costs. Human safety and democratic authority remain mandatory.

## How to turn proposals into a credible submission

1. **Choose a live procedure.** For example, [EU-P01, Digital Omnibus (ongoing)](https://eur-lex.europa.eu/procedure/EN/2025_360), a national consultation, or the [UN AI governance dialogue](https://www.un.org/global-dialogue-ai-governance/en/resources). Do not submit a proposal framed as an amendment to a law whose relevant legislative stage has closed.
2. **Quote the exact current clause.** Cite legal identifier, article, page and procedure number. Identify whether amendment, implementing standard, procurement condition or voluntary code is actually within the decision-maker's remit.
3. **Select 1–2 clauses above.** Do not demand enactment of a 20-article metaphysical charter in one step.
4. **Attach measurable evidence.** Safety cases, agent evaluations, false positives, practical costs, distributional effects and independent review. Include unfavorable findings.
5. **Include precise legal language and exceptions.** State covered entities, threshold, enforcement body, records, data protections, appeals, enforcement date and transition.
6. **Declare provenance.** Tabula Rasa is the proponent; linked legislation is precedent/context, not an endorsement.
7. **Submit through an open official channel.** Log submission date, procedure, text/version, public response and disposition. Do not claim submission or political support until it occurs.

## Sequenced adoption strategy

| Horizon | Concrete deliverable | Success condition |
|---|---|---|
| 0–3 months | Public crosswalk + 2-page consultation brief on external authorization and incident reporting | Each statement tied to current instrument and independent test |
| 3–6 months | Reproducible agent-control experiments under the [research protocol](../research/PROTOCOL.md) | Outcomes include legitimate completion, unauthorized action success and failures |
| 6–12 months | Domain-specific draft provision + stakeholder critique in an active forum | At least one public review cycle, counterargument log and revised text |
| Later | Reference architecture, comparative impact analysis and coordinated standards proposal | Actual adoption or incorporation documented from primary publication; no invented endorsements |

**Non-negotiable:** Advocacy is legitimate. Fabricating legal status, citations, empirical certainty or institutional support is not.
