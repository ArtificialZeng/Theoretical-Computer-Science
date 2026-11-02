# Verification report

Mode: Search verification, with frozen primary full texts and accepted-scope comparison.
Job: c034-grouptri-release-98d1e823492f. Search date: 2026-11-02 UTC.
Manuscript digest: a40f8840ae0d14f65c4af83e804cb282ac08f663f3e89dfedb04cd0efadea7ba. PDF digest: e9b3d5055ad93f76865143de8acab7b3c4dc6c1f3cd1fe3b20482eb99d68cfa4.

The advisory $citation-check-skill was explicitly invoked and read. Pass 1 is the fixed 33-claim list in audit/release-claims.md; pass 2 below uses those IDs without re-extraction. The explicit bounded worker assignment authorized completion without another confirmation pause. Definitions and methodology descriptions are excluded under the skill rules. Mathematical rows are release-scope checks against the actual accepted frozen proof and report, not new mathematical certification.

| Metric | Count |
|---|---:|
| Extracted claims checked | 33 |
| Supported at the stated verification scope | 32 |
| Bibliographic record checked with limited optional DOI-registration refresh | 1 |
| Contradicted attributions / numerical discrepancies found | 0 |
| Undefined citation keys | 0 |

Overall: accept_with_citation_limitations. The limitation concerns optional DOI registry completion, not paper existence or claim support. No Excel or authoritative user BibTeX list was designated; literature/user_bibliography_check.md was inspected.

## Pass 2: claim-to-source checks

| IDs | Status and exact support |
|---|---|
| C01 | Scope aligned: full all-M theorem and every-c quantifier match claim.json, source.md and audit/math.md; main proof Sections 2--6 retained. |
| C02 | Exact: formula agrees with the accepted recurrence; for M=4 the rational saving is 1/144000000. |
| C03 | Verified paraphrase: Maj26 Theorem 21.3 and Corollary 21.7(a), source pp.100,102; deterministic elementary-group bound. |
| C04 | Verified paraphrase: Maj26 Remark 21.8, pp.103--104; carries and invariance under re-gauging. |
| C05 | Verified paraphrase: Maj26 Propositions 21.9 and 21.10, pp.104--105; hypotheses retained. |
| C06 | Verified paraphrase: Maj26 Open Problem 21.12 at the end of Section 21.2 asks precisely bounded exponent, polynomial order and saving depending only on exponent. |
| C07 | Verified paraphrase: CVX23 Theorem 5.1 and complete proof, pp.18--19; initial cubic sorting is distinct from later updates. |
| C08 | Verified interpretation: CVX23 high-frequency edge predicates imply the potential equations; the manuscript reconstructs them rather than attributing a named group-lifting theorem. |
| C09 | Verified paraphrase: SWX26 introduction and Section 2.3, pp.1--5, discuss detection/all-edge/listing reductions and their quantitative limits. No tight generic equivalence is attributed. |
| C10 | Scope aligned with accepted extension theorem and explicit masks; dense or residue-diverse inputs impose no new promise. |
| C11 | Scope aligned; d<=c log_2 n follows from every factor being >=2. Precise coordinate wording replaces the prior vague phrase. |
| C12 | Scope aligned with frozen embedding proof; cyclic injection and polynomial-order accounting unchanged. |
| C13 | Verified exact formula and hypotheses: Maj26 Theorem 21.3, p.100. Constants may depend on fixed order exponent; saving does not. |
| C14 | Verified: Maj26 Corollary 9.1(b), Section 16, Corollary 21.7; exact arithmetic 0.077/14=0.0055>0.001. |
| C15 | Scope aligned: source restriction for fixed p excludes finitely many sizes, explicitly handled by enumeration. |
| C16 | Scope aligned: three independent edge-kind markers, plus-sum signs and O(b^2(D+3)) construction agree with frozen proof. |
| C17 | Scope aligned: Lemma 3.1 retains cap, distinctness, completeness and full cost; no witness-output strengthening of main theorem. |
| C18 | Scope aligned: detector cutoff and fresh masks are explicit; large dimension is charged against each queried side. |
| C19 | Scope aligned: incidence deletion, pivot assignment and frequency scans retain all stated charges. |
| C20 | Scope aligned: Lemma 4.1 and the exact predicates retain the disjoint cover and edgewise potential identities. |
| C21 | Scope aligned: algebraic cancellation and pZ_M to Z_q division retained, including p dividing q. |
| C22 | Scope aligned: complete kernel instance, independent markers, polynomial group-order bound and graph materialization are explicit. |
| C23 | Scope aligned: smaller recursive exponent, fixed-M rational parameters, small cases and termination are explicit. |
| C24 | Scope aligned: all five ledger rows and the epsilon_0 delta_q/144 recurrence match accepted evidence; no new free preprocessing. |
| C25 | Exact recorded finite coverage: audit/independent-checks.json and identical packaged recorded-checks.json list 512 cases, sides 0--3. |
| C26 | Exact recorded finite coverage: same records and local-lift code give 676333 cases, composite M<=36, proper prime divisors. |
| C27 | Exact recorded finite coverage: 3548440 marker cases, q=2--36. |
| C28 | Exact recorded finite coverage: 360 graphs, sides 1--6, dimensions 1--3, 6850 constructed kernel instances. |
| C29 | Exact recorded finite coverage: 2047 rational ledger cases, M=2--2048. |
| C30 | Verified description of supplied finite checks: brute-force detectors; exact coverage is separated from the asymptotic proof and performance. |
| C31 | Metadata verified from Maj26 versioned/current arXiv records; author/title/2026/v1/12 October/advertised DOI agree. Optional registry completion remains uncertified; see limitation below. |
| C32 | Metadata verified from CVX23 versioned/current arXiv records: all three authors, title, 2023/v1/25 March and advertised arXiv DOI agree. |
| C33 | Metadata verified from SWX26 versioned/current arXiv records: all three authors, title, 2026/v1/19 August and advertised arXiv DOI agree. |

## Primary sources and bounded novelty comparison

- [Maj26 versioned record](https://arxiv.org/abs/2610.17420v1), and [current record](https://arxiv.org/abs/2610.17420). Full frozen text: intake/primary/2610.17420v1-pdf.txt and its PDF. Nearest results: Theorem 21.3, Corollary 21.7, Remark 21.8, Propositions 21.9--21.10 and Open Problem 21.12; matrix instantiation: Corollary 9.1(b), Section 16.
- [CVX23 versioned primary](https://arxiv.org/abs/2303.14572v1). Full frozen text: intake/primary/2303.14572-primary.txt and PDF, Theorem 5.1, pp.18--19. Its known decomposition is attributed; the candidate claims the charged non-split extension, not this prior structure alone.
- [SWX26 versioned primary](https://arxiv.org/abs/2608.19092v1). Full frozen text: intake/primary/2608.19092v1.txt and PDF, introduction and Section 2.3. The reference is relevant context rather than an unproved tight listing oracle.

All applicable academic search templates were executed for all three citations: author/year/title prefix, full title with arXiv/Semantic Scholar filters, author/year/venue, DOI, and arXiv ID. The current-primary bounded-exponent search and raw results are preserved in audit/release-web-searches.json. Only primary records/text support the judgments. The current records display v1 only; no equivalent full extension was located in this bounded check. This is not an exhaustive priority certificate and does not upgrade audit/stoc-assessment.json.

## Limitation and dependency scope

The versioned Maj26 arXiv page displayed a pending-registration annotation beside its advertised DOI; the current unversioned page lists that DOI without the annotation. The record, full text and nearby claims are accessible. Optional DOI registry completion was not independently certified within this audit; preserve the existing DOI and versioned arXiv link. This narrow metadata refresh limit is recorded in unverified_citations, without claiming the paper is missing or rejecting its supported prose.

All nine publication.json inputs were read or byte-checked: TeX, actual BibTeX database, generated bibliography, unmodified official class/style, build instructions, Makefile, verifier and finite-coverage record. The compiler recorder has only main.tex, acmart.cls and generated main.bbl as local typesetting inputs; generated main.bbl is byte-identical to the listed source main.bbl. BibTeX additionally uses the listed references.bib and ACM-Reference-Format.bst. All other TeX dependencies are system packages. There are no figures or unlisted TeX imports. The ZIP includes exactly those nine files. All three cited keys resolve to the three rendered references on page 8; no irrelevant reference was added.

Manuscript Sections 2--6 match the accepted proof. Editorial changes add no new mathematical assertion. Fixed-M scope and dependence on the cited elementary backend are explicit. The exact author and substantial body/end AI disclosures were checked in source, extracted PDF and rendered pages. Current [official CFP](https://acm-stoc.org/stoc2027/stoc2027-cfp.html) was inspected for identified authors, letter/single-column/11pt/one-inch margins and the two material-AI disclosures. The user cap of twelve total pages is met. No external submission was performed.
