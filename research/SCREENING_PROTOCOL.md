# Systematic evidence screening protocol · v1.10

This is a **protocol**, not a claim that a systematic review has been completed.

## Research questions
RQ1: Under what conditions do external authorization controls measurably reduce unauthorized AI-agent actions?
RQ2: Which empirical evaluations reliably measure deception, power seeking, and resistance to correction?
RQ3: What indicators, if any, could support inferences about artificial consciousness or moral patienthood?
RQ4: How does human–AI interaction affect user autonomy, calibration, dependence and oversight?

## Search sources
OpenAlex, Crossref, Semantic Scholar, PubMed (where relevant), ACM Digital Library, IEEE Xplore, arXiv, institutional archives, and standards bodies. Document exact search date, query, coverage, API restrictions and duplicates.

## Example search strategies
- `("AI agent" OR "language model") AND (authorization OR "tool use") AND (security OR oversight)`
- `("language model" OR "AI agent") AND (deception OR "reward hacking" OR "power seeking") AND evaluation`
- `("artificial consciousness" OR "machine consciousness") AND (indicator OR theory OR assessment)`
- `("human AI interaction" OR "automation bias") AND (autonomy OR trust OR reliance)`

## Inclusion
Original empirical studies, methodologically explicit theoretical contributions, authoritative standards, systematic reviews, and significant negative or contradictory results. Include preprints with an explicit unreviewed flag.

## Exclusion
Duplicated records; unverifiable bibliographic identity; promotional material without methods; unsupported claims about sentience; inaccessible methodology where empirical verification is central. Preserve exclusion reasons.

## Screening and extraction
1. Deduplicate by DOI and canonical identifiers, then title/year.
2. Screen title and abstract against each RQ.
3. Full-text screen using recorded eligibility decisions.
4. Extract population/system, model version, intervention, comparator, outcome, statistical uncertainty, limitations, funding and conflict of interest.
5. Require independent second review for disputed or high-impact claims.
6. Produce a PRISMA-style flow only from real recorded counts, never estimated counts.

## Risk of bias
Assess selection bias, outcome leakage, evaluator independence, model contamination, reporting bias, confounding, sample size, reproducibility and external validity. Grade each dimension separately rather than inventing a universal quality score.

## Synthesis
Do not pool heterogeneous benchmarks into a meta-analysis without defensible comparability. Report null results, contradictory findings and sensitivity to inclusion rules. Do not infer AI sentience from performance on language tests.

## Reproducibility
Archive search strings, retrieval timestamps, deduplication decisions, screened records, extraction forms, analysis scripts and protocol amendments. Respect publisher licensing and privacy.
