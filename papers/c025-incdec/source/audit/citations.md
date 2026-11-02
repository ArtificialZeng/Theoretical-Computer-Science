# Verification Report

**Mode:** Search, with original primary text and accepted-scope cross-check.
**Document:** manuscript/main.tex and the final six-page PDF.

Job: c025-incdec-release-4b3b2544efe9. Audit date: 2026-11-02 UTC.

Mathematical snapshot: 2b34def4196da89c592b17665c39fbf7b0b04e44c40aeac720bf40cd52fb35b4.
Manuscript snapshot: d4717112b7a2b8ec108123ef8efb3e63f3f6ed5f1f6caf1810a2969f35593c6a.
PDF SHA-256: 407ec869e3c74ed3fea9001fc3e1afb187d4b3175fabfd78c52d40408afeb186.

## Summary

| Metric | Count |
|---|---:|
| Fixed claims extracted | 25 |
| Verified in final text | 25 |
| Wording issues repaired | 1 |
| Unverified or contradicted citations | 0 |
| Undefined citation keys | 0 |

**Overall status: PASS after the disclosed repair.** This is an actual internal release audit, not external peer review or a new mathematical certificate. $citation-check-skill was explicitly invoked and read, and used as advisory guidance. Extraction was completed and saved before verification. The user's bounded one-job release instruction authorized proceeding without a separate confirmation pause. All 25 fixed claims are mapped below; no claims were added during verification.

## Claim-to-source findings

| Claims | Primary location / evidence | Finding |
|---|---|---|
| C01 | DKLS26, Section 1.1, Corollary 2, Proposition 11, Section 5; journal PDF pp.3,14–15,20–21 | Full-pair upper 1+e/(e-1), lower 2 and stated gap are accurate. |
| C02 | DKLS26 Proposition 17, p.20 | Equal endpoint totals are a genuine extra hypothesis of that earlier factor-2 result. |
| C03 | DKLS26 algorithm p.8; Proposition 19 and Corollary 20, pp.21–22 | Separate summand marginals and the tight old-algorithm constant, including modular g, are supported. |
| C04 | BBBCDL26 Theorems 1.1–1.2, p.134:3 | Upper is reported approximately 1.373; lower is 1.25. Original introduction expressly requires optimum-set access and sacrifices efficiency. Repaired manuscript to say approximately before 1.373, preserving every mathematical claim of the accepted candidate. |
| C05 | CK26 v1, Section 2, Definition 2, Theorem 1, Remark 1 | Fixed at-most-k comparator, trajectory curvature and deletion of previously chosen elements are explicit. Comparison is limited to the stated pruning theorem. |
| C06 | Frozen literature.md and fresh bounded release queries | The historical dated bounded-search statement matches its record. Current searches located no full equivalent; no universal priority is certified. |
| C07–C10 | claim.json, problem.md, accepted math.md, manuscript Theorem 1.1 and Sections 2–4 | Final theorem retains every original quantifier, arbitrary unequal totals, exact-value unit-cost model, and both structural/polynomial constants. No unsupported strengthening. |
| C11 | Section 2 candidate count | Sum of n-i+1 is n(n+1)/2; two summand evaluations per candidate and two endpoints give the stated bound with cached current value. |
| C12–C16 | Accepted universal argument versus manuscript Section 3 | Union budget, global bound, diminishing gains, both sign cases, reversal, zero/endpoint and tie cases are all explicitly retained. Finite checks are not used as proof. |
| C17–C18 | Manuscript baseline argument; DKLS26 Eq.(5), pp.8–9 | Nonnegative baseline transfer and two additional baseline queries are supported; negative baselines remain excluded. |
| C19–C21 | DKLS26 Proposition 11 at curvature 1, pp.14–15; manuscript Section 4 | Coverage family is correctly attributed and reproduced; finite ratio 2-2/n and limiting impossibility are correct, without claiming a new lower bound. |
| C22 | DKLS26 Proposition 18, p.21 | Larger nonmonotone incremental class has unbounded deterministic ratio; manuscript asserts no transfer of its own guarantee there. |
| C23 | Current Springer publisher record and preserved journal title page | All four authors, title, year 2026, volume 63, article 31 and DOI agree. |
| C24 | Current official Dagstuhl record and PDF title page | All six authors, title, ESA 2026, LIPIcs 388, 134:1–134:23 and DOI agree. |
| C25 | Current arXiv abstract/version and full HTML | Both authors, title, May 8 2026 v1 and arXiv-issued DOI agree. Only the specifically cited v1 theorem is compared. |

Definitions and procedural AI acknowledgments were not extracted as external factual claims. No statistical charts, tables or plotted data occur. The approximately 2.582 shorthand is visibly marked approximate and agrees with the displayed exact expression.

## Sources and bounded search

- [DKLS26 journal primary record](https://link.springer.com/article/10.1007/s00236-026-00546-x), plus preserved intake/primary/incremental-decremental-2026.pdf and .txt.
- [BBBCDL26 official primary record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.134), plus preserved intake/primary/ESA2026-134-incremental.pdf and .txt.
- [CK26 versioned primary record](https://arxiv.org/abs/2605.07902v1) and [full primary text](https://arxiv.org/html/2605.07902v1), especially Section 2, Definition 2 and Theorem 1.
- [Current official STOC CFP](https://acm-stoc.org/stoc2027/stoc2027-cfp.html), submission format and substantive-AI-disclosure sections. Its nonanonymous single-column submission format is distinct from the later sigconf proceedings format. The title page, 11pt source option, USLetter geometry and one-inch margins conform; six total pages satisfy the user's stricter cap. No actual submission is authorized.

All applicable author/year/title, title restricted to arXiv/Semantic Scholar, author/year/venue, DOI and supplied arXiv-ID search templates were run, followed by bounded exact-model/2-competitive/endpoint-greedy searches. Only primary records and original text support the comparisons. Search date is 2026-11-02 UTC. Lack of an equivalent in these checked sources is not proof of priority; CK26 is compared only at its stated theorem, without endorsing all of that preprint.

## Bibliography and dependency scope

literature/user_bibliography_check.md was inspected before generating the rebuilt PDF. No Excel or authoritative user BibTeX database was designated, and no workbook basis or quota was invented. The three relevant citations suffice for the comparisons actually made. All three cited keys occur in references.bib and the generated main.bbl; none is undefined or unused. Every reference on rendered page 6 and in extracted PDF text matches the records. No unresolved reference markers appear.

Every sorted publication.json source_file was inspected: README/build.py for build and scope; official acmart.cls/acmart.dtx for provenance and class selection; unchanged standard alphaurl.bst for bibliography handling; main.tex, references.bib and main.bbl for all prose and citations. The compiler recorder's only non-system inputs are main.tex, acmart.cls, main.bbl and generated main.aux/main.out. BibTeX additionally reads the listed references.bib/alphaurl.bst. No imported authored files or figures are missing. README and dtx are conservative extra declared inputs. System TeX packages remain system dependencies.

The accepted mathematical review and innovation assessment are unchanged; the separate venue assessment remains working_paper, with no readiness upgrade. Prior manuscript/PDF bytes and the prior manuscript snapshot were saved under evidence/release/pre-edit before the single publication-only wording repair.
