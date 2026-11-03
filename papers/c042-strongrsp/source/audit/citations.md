# Release citation and scope audit

Job: c042-strongrsp-release-8a7cb8c2de68. Search date: 2026-11-03 UTC.
Verdict: accept. Method: explicitly invoked $citation-check-skill, used its
two-pass extraction and relevant claim-to-source checks as advisory, then
inspected primary texts and the final PDF. The user's autonomous bounded-job
instruction overrides the skill's extraction-confirmation pause. No Excel or
authoritative user bibliography was designated; none was invented.

## Verification report

The fixed extraction is evidence/release/citation-extraction.json and its readable
Markdown companion. Twelve external attribution/bibliographic items are verified;
one grouped mathematical item is checked for consistency with accepted scope,
and one computational-method item is checked against frozen evidence. No citation
contradiction, undefined key, or unresolved metadata/text-access limitation remains.
This release audit is not a new mathematical referee verdict.

| IDs | Primary evidence and exact location | Finding |
|---|---|---|
| C01, C04, M02 | [Ashvinkumar, Bernstein and Karczmarz, v1](https://arxiv.org/html/2410.17179v1), Section 9 and Lemma C.1; frozen PDF, printed pp.42,46 | Verified. A target-specific bottleneck confines the optimum to a ratio-n interval. The source distinguishes that reduction from its all-target aspect dependence. Repeating a target-specific run n times does not supply the manuscript's aggregate bound. The 2024 arXiv version and SODA 2025 note are distinguished correctly. |
| C02, C03, M01 | [Ashvinkumar, current record](https://arxiv.org/abs/2610.18337); [v2 text](https://arxiv.org/html/2610.18337v2), Theorem 1 and paragraph after Theorem 2, printed p.3 | Verified. The deterministic bicriteria bound is Otilde(m log(nW)/epsilon^9). The stated all-target strong-polynomiality question and single-target distinction match. Current history identifies v2, 29 October 2026. |
| C05 | Same v2 primary text, Sections 4 and 6, particularly the DP update, potential and Lemma 6.2 | Verified attribution of clock DP and conditional-expectation witness potential. The manuscript gives credit rather than claiming these as new. |
| C06, M03 | [Gorkiewicz and Karczmarz, v1 record](https://arxiv.org/abs/2502.10348v1); [Section 6](https://arxiv.org/html/2502.10348v1), Algorithm 4 and Lemmas 6.1--6.3 (Algorithm 4 on PDF p.18) | Verified. The active-set recursion and multiplicative accounting concern ordinary additive SSSP with weights in {0} union [1,W]. The manuscript does not invoke it as a stochastic-boundary theorem. Authors, title, year, version and arXiv DOI agree. |
| C07, M04 | [Dagstuhl record and official BibTeX](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.117); [official text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.117/LIPIcs.ICALP.2025.117.html), Theorem 1 and Sections 2--4 | Verified. This is an offline ordinary-SSSP precedent, with the displayed theorem using m log(nW) log^3(n) loglog(n)/epsilon. All five authors, title, ICALP 2025, LIPIcs 334, pages 117:1--117:20 and DOI match. |
| C08 | The preceding two ordinary-SSSP primary statements and their algorithms | Supported comparison: their boundary operations are additive distance relaxations, not the stopped stochastic first-hit contract proved here. |
| C09 | source.md, claim.json, accepted audit/math.md and audit/innovation.json; manuscript Theorem 1 and Sections 2--7 | Scope consistent: all inputs, parallel/zero edges, zero optima, relaxed feasibility semantics, total near-linear preprocessing/space, finite arithmetic and bounded-space deterministic queries are retained. The exponents 20,100 and intermediate ledger match the accepted account. No new broader theorem or strengthened guarantee was introduced. |
| C10 | Frozen boundary/rounded/compiler/integration result files, bounded-exponential-results.json and actual audit/referee-checks.json | The manuscript accurately describes small diagnostic tests and distinguishes Decimal checks from a certified universal proof. No test has been upgraded into proof evidence. |

All applicable academic search templates were run, including DOI and supplied
arXiv-ID queries, with requests/results saved in evidence/release/search-1.json
through search-5.json. An initial versioned A26 abstract-page cache miss was
resolved by its current primary record and accessible v2 full text. No equivalent
full resolution was identified in this bounded refresh; this is not an exhaustive
priority certificate. Existing mathematical innovation acceptance and the actual
working_paper venue assessment are preserved, without promotion.

## Complete dependency and rendered-reference scope

Reviewed every file in publication.json: manuscript/main.tex, references.bib,
main.bbl, acmart.cls, ACM-Reference-Format.bst, build.sh and README.md. The compiler
recorder and BibTeX inputs identify no undeclared authored/imported source,
custom style, figure or bibliography. System TeX files are installed packages;
main.aux/main.out are generated compiler intermediates. There are no figures.
The two local official ACM files are byte-identical to the designated distribution.

The four actual cite keys A26, ABK24, GK25, MMNNS25 all resolve to distinct BibTeX
and rendered bibliography entries. The final compiler log and PDF text contain
no unresolved citations or cross-references. Page 2 uses full surnames and numeric
hyperlinked citations; page 9 prints all authors and DOI links clearly. Numeric
labels are permitted by the CFP's recommendation, which prefers alphanumeric
labels without requiring them. No unnecessary reference was inserted.

Publication-only edits and earlier bytes are preserved under evidence/release/.
The accepted mathematical snapshot and all prior verdicts remain unchanged.

