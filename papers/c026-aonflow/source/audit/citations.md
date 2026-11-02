# Verification Report

Mode: Search plus complete frozen primary documents.
Document: manuscript/main.tex, its complete publication dependencies, and the final seven-page PDF.
Job: c026-aonflow-release-7db9e6fea069. Search date: 2026-11-02 UTC.
Method: explicitly invoked $citation-check-skill as an advisory two-pass audit; fixed extraction is audit/release-7db9e6fea069-extraction.md. The user requested a bounded autonomous release, so verification proceeded without an interactive confirmation stop. No source or metadata veto was applied.

## Summary

All 15 extracted claim groups were reviewed in order. No numerical discrepancy, contradicted attribution, unsupported strengthening, or undefined citation was found in the final manuscript. Four substantive bibliography records are relevant. Two optional live publisher refreshes remain unavailable; complete primary material supports all cited mathematical statements. Verdict: accept_with_citation_limitations. These are access limitations, not findings that any paper is nonexistent. No Excel workbook or authoritative user bibliography was designated; literature/user_bibliography_check.md was read, and no workbook or irrelevant citation was invented.

## Fixed claim-to-source mapping

| Claim | Evidence checked | Finding |
|---|---|---|
| C01 | CKS05 Theorem 3.2, author PDF page 7 | O(log^2 k) general-graph AON baseline; verified. |
| C02 | BJS26 Section 5 / Conjecture 5.1, printed p.13; current official ICALP HTML | Original near-logarithmic target, exact congestion one and throughput/concurrent-flow obstacle; verified. |
| C03 | CKS05 Lemma 1.1, author PDF pp.3–4 | Uniformization and duplication are explicitly prior work; verified. |
| C04 | Anand26 v1 Theorems 1.4 and 5.1, Section 5 preamble and Appendix C, live arXiv text | Improved decomposition context verified. Weight-at-least-one versus arbitrary-nonnegative/n-sensitive guarantee distinguished; no AON theorem attributed. |
| C05 | BJS26 Theorem 3.1, frozen primary p.3 and current publisher HTML | Nonnegative integral weights, total-weight overhead and G[U] induced-component expansion; verified. Harmless bounded small arguments and fixed enlarged constants preserve the source guarantee. |
| C06 | CKS05 Theorem 3.1 and footnote, PDF p.7 | Uniform alpha-edge-flow-linked matching rounding and correction requirement; verified. |
| C07 | CKS13 Theorem 3.8 and Section 3.4, pp.1478–1483 | Nice-instance hypotheses identified explicitly; manuscript does not invoke it as an arbitrary-component black box. |
| C08 | CKS13 Lemmas 3.3–3.4, pp.1476–1477 | Grouping and common-distribution conclusion verified. Leaf ownership/residual coverage are explained as the accepted transfer, rather than quoted verbatim as a new prior theorem. |
| C09 | CKS13 Lemmas 3.9 and 3.11–3.14, pp.1478–1483 | Centers, separating bridges, tagging, five-color selection and transit pairing match. Shared-node convention occurs at end of Section 3.4. |
| C10 | CKS13 Lemma 3.10, p.1479 | Simple-path bridge-load integrality and exact congestion one; verified. |
| C11 | Frozen claim, accepted audit/math.md and manuscript Theorem 1 | Same complete original input class, unit capacities, distinct admissions, polynomial bits and >=3/4 guarantee. Release prose does not strengthen accepted scope. |
| C12 | Accepted proof and explicit equations (1)–(10), sampler paragraph and terminal-parameter calculation | Constants and arithmetic agree: epsilon=1/(4T), phi=epsilon/(8 Gamma(2K)), cut <=epsilon K/4, >=3K/4 unhit, yield >=3 c0 F/(256 Gamma(2K)), probability >61/64 and 2K=O(k^2). Local finite diagnostics were reproduced from the source ZIP, with their limits retained. |
| C13 | Accepted math report's corrected CKS reconstruction, corresponding primary lemmas and manuscript Section 5 | Common-distribution half-capacity premise, uniform leaf ownership and residual convention supplied. No nonuniform theorem or new clustering result asserted. |
| C14 | Publisher BJS record; live CKS05 author PDF and institutional publication record; CKS13 published title page; live Anand arXiv v1 record | Authors/titles/dates/pages/versions/DOIs agree. Optional CKS publisher refreshes unavailable as disclosed below. |
| C15 | Frozen contribution, accepted innovation report, CKS/BJS/Anand primary comparisons | Protected-copy admission interface is stated as the new contribution. Imported algorithms retain attribution; no exhaustive priority claim or venue promotion. |

## Source and dependency scope

The sorted sources_checked list is exactly publication.json source_files. Read all authored content, bibliography, generated .bbl, Makefile and build instructions; checked local acmart and bibliography style against the unmodified official input copies. The recorder .fls lists main.tex, acmart.cls and the .bbl as the only local substantive compilation inputs; .aux and .out are generated cross-reference files. BibTeX additionally reads the listed references.bib and ACM-Reference-Format.bst. No imported figure, hidden local style or authored input is omitted. System TeX packages are installed dependencies. All four citation keys appear in the regenerated bibliography, and citations/cross-references are resolved both in the final log and rendered PDF. The manuscript has no chart/data-table claim requiring a separate visual-data source audit.

## Access limitations and conservative prior comparison

CKS05's ACM publisher endpoint returned HTTP 403; its full author PDF was accessible and its DOI/pages are corroborated in the author's institutional record. The latter has an unrelated event-index field; the author PDF, rather than that field, establishes STOC 2005. CKS13's live author PDF timed out and its DOI endpoint returned HTTP 403; the complete frozen published PDF/text contains the DOI and every cited passage. These external refresh limits do not undermine the available text support. They are retained in unverified_citations solely to disclose incomplete live publisher refresh. No user-designated-workbook authority is asserted.

The current official BJS and Anand records were rechecked. No equivalent full AON result was located in the inspected primary comparisons. This bounded statement is not an exhaustive priority finding. The accepted working_paper assessment and its depth/breadth uncertainties remain unchanged.

## Sources consulted

* [BJS official publisher record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.22), official linked HTML, and intake/primary/2602.15015-expanders.pdf/.txt.
* [CKS05 author PDF](https://chekuri.cs.illinois.edu/papers/well-linked.pdf), complete frozen PDF/text, and [author institutional metadata](https://experts.illinois.edu/en/publications/multicommodity-flow-well-linked-terminals-and-routing-problems/).
* CKS13 complete frozen published PDF/text; DOI printed on title page. Live [author PDF](https://chekuri.cs.illinois.edu/papers/anflow-sicomp.pdf) and [publisher DOI](https://doi.org/10.1137/100796820) refresh unavailable.
* [Anand arXiv v1 record](https://arxiv.org/abs/2610.17237v1) and [primary HTML](https://arxiv.org/html/2610.17237v1).
* [Official STOC 2027 CFP](https://acm-stoc.org/stoc2027/stoc2027-cfp.html): identified human author, separate title page, letter paper, 11pt single-column body, one-inch margins and substantive AI disclosure. User's stricter 12-total-page cap is met by seven pages. Format compliance does not establish venue readiness.

Exact query templates, passage locations, available sources and limits are recorded in evidence/release-7db9e6fea069-primary-checks.json.
