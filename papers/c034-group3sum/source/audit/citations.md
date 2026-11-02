# Verification Report

Mode: Search, with frozen-proof scope comparison for the manuscript's own mathematics.
Document: manuscript/main.tex and the final eight-page PDF.
Job: c034-group3sum-release-5f0540aba52c. Search date: 2026-11-02 UTC.
Method: $citation-check-skill explicitly applied as an advisory two-pass audit.
Pass 1 is the fixed extraction audit/citation-extraction.md; pass 2 below uses
only those IDs. The user's explicit autonomous bounded release request overrides
the advisory confirmation pause. No user Excel/BibTeX authority was designated;
literature/user_bibliography_check.md was inspected.

| Metric | Count |
|---|---:|
| Extracted claims | 22 |
| Verified against the stated source/proof/evidence scope | 22 |
| Numerical error / misleading / hallucination / unverified | 0 |

Overall: accept. This release audit checks scope, attribution and artifacts; it
does not replace the accepted mathematical referee or certify universal priority.

## Fixed-claim verification

| IDs | Evidence and location | Finding |
|---|---|---|
| C01-C02 | Frozen research/divisor-profile-proof.md, statement and Sections 2-8; accepted audit/math.md, items 1-10 | Main theorem and mechanism match the accepted all-M scope, explicit saving, per-input success and worst-case caps. |
| C03-C04 | Maj26, PDF pp.76,82-83; Theorem 19.17, Corollary 19.25, Open Problem 19.26 | Deterministic p^2 prior and general target correctly distinguished. |
| C05 | Maj26, PDF pp.68-70, Lemmas 19.6-19.7; AVW26, Section 4.1 | Support/probe and matrix infrastructure directly attributed. |
| C06 | Frozen proof Sections 2-5 and accepted innovation review; Maj26 Section 19.7 | Simultaneous profiles and extremal divisor certificate supply the stated difference; no priority superlative added. |
| C07 | Maj26, PDF pp.84-86; Lemmas 20.3(d),20.4(a), Remark 20.6 | The finite quotient and coordinate translation, including the anticipated consequence, are prior. |
| C08 | CIMY26, abstract and Sections 2.1-2.2, Theorem 2.3 | Subset-convolution integer context is supported; no torsion implication is attributed. |
| C09-C15 | Frozen proof Sections 1-6; accepted math review items 1-7 | Normalization, profiles, hash, order probabilities, probes and support scans are reproduced without strengthening. |
| C16 | AVW26, Corollary 26, Section 4.1, live HTML and frozen exact statement | Integer-entry hypotheses, dimensions, all three exponents and selected-entry interface match exactly. |
| C17 | Frozen proof Sections 7-8; accepted math review items 8-10 | All costs, query budget, cap failures and fixed-witness probability match acceptance. |
| C18-C19 | Maj26 Lemmas 20.3(d),20.4(a), Remark 20.6 and accepted audit/math.md prior-results discussion | Routine consequence of the accepted full theorem; finite quotient and preimage recovery explicit; no full dichotomy asserted. |
| C20-C21 | audit/referee-verifier-results.json and audit/referee-verifier.py | 778,1382,4622,144,45932,13244 match exactly; mixed moduli, fragmentation and nonsurjective images are present. Tests explicitly do not prove asymptotics. |
| C22 | Three live arXiv version records below; references.bib, main.bbl and rendered PDF pp.7-8 | Names, titles, 2026 dates and v1 identifiers match; all three citation labels resolve. |

## Primary sources and search coverage

- [AVW26 record](https://arxiv.org/abs/2610.06783v1), 5 October 2026, Josh Alman and Virginia Vassilevska Williams; [original text](https://arxiv.org/html/2610.06783v1), Corollary 26. Its integer selected-entry primitive matches Lemma 7.
- [Maj26 record](https://arxiv.org/abs/2610.17420v1), 12 October 2026, Ruhollah Majdoddin; [original text](https://arxiv.org/html/2610.17420v1), cited Sections 19-20, plus frozen primary PDF/text. The live unversioned record still displayed v1 only.
- [CIMY26 record](https://arxiv.org/abs/2610.42012v1), 30 October 2026, Timothy M. Chan, Reina Itakura, Zhiyuan Ma and Yuancheng Yu; [original text](https://arxiv.org/html/2610.42012v1), abstract and Sections 2.1-2.2. Integer subset convolution supports the contextual sentence.

Applicable search templates were run for each entry: first-author/year/first
three title words; title with arXiv/Semantic Scholar domains; author/year/arXiv
(the cited preprint venue); arxiv:identifier. No DOI is supplied in references.bib,
so no DOI-query template applies. The long Maj26 title query used its distinctive
opening and lossless-reductions phrase. Additional current-scope searches:
`"bounded exponent" "3SUM" abelian 2026` and
`"3SUM" "divisor" "coset" bounded exponent`. Search leads were not substituted
for original source text. No equivalent all-M result was found in this bounded
screen; unindexed/unpublished work is outside coverage. No inaccessible metadata
endpoint or primary-text limitation remains for the actual citations.

## Dependency and output scope

Every publication.json source_files entry was inspected: main.tex is the only
authored TeX input; references.bib is the only database; main.bbl is its actual
compiled bibliography; acmart.cls and alpha.bst are the local styles; build.sh
and README describe reproduction. No figure/import or additional custom style
is used. The isolated clean build recorder lists only main.tex, acmart.cls,
generated main.aux/main.out and the declared main.bbl outside system TeX files.
BibTeX's log names the declared references.bib and alpha.bst. Thus the explicit
list is complete. PDF citations and bibliography were also read in extracted
text and rendered pages. No undefined key, question-mark label, unsupported
novelty claim or material attribution discrepancy was found. Three relevant
citations retained; no irrelevant count-filling citation inserted.

The mathematical/innovation/STOC reports are preserved; classification remains
working_paper. No external submission or public posting is implied.
