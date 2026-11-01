# Verification Report

Mode: Search plus frozen-proof support audit. Method: explicitly invoked $citation-check-skill, advisory under the user's release instructions. Extraction and support verification were separate passes; the fixed input is evidence/release/claims-extracted.md. The user's explicit complete bounded-audit authorization supersedes an interactive extraction-confirmation pause. Checked 2026-11-01 UTC / 2026-11-02 Asia/Shanghai.

Job: c021-ccrapumping-release-92d7dacdae19.

Evidence snapshot: fb196911906a12d3f006a58d590694062481bf6aa44e05c6691883c3e220d3cf.
Manuscript snapshot: 99eb0bd7c1fdc78cfa6c6d2b1e58391d7bde1db59600709934d6a48a747cdfff.
PDF SHA-256: a9c5a9244838f61a7c8fcd01a8ef0902229b629de8e3ba55d917e0c639c5f27b.

Summary: 32 substantive claim groups reviewed; no contradicted attribution, numerical mismatch, undefined citation, unsupported strengthening or useful unresolved citation-access limitation remains. Original mathematical assertions are supported by the accepted frozen argument and the same proof in the manuscript; this is a scope/support audit, not a new mathematical referee verdict or external verification of new theorems. Definitions and methodology descriptions are excluded by the advisory extraction rules.

## Primary citation records and exact support

- **MPS26**: Filip Mazowiecki, Antoni Puch, Daniel Smertnig; STACS 2026, LIPIcs 364, 67:1-67:21, DOI 10.4230/LIPIcs.STACS.2026.67. [Publisher record and official PDF](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2026.67) verified the metadata. Definition 11 and Theorem 15 are on printed p.67:8; Section 3.2 and Example 26 on p.67:13 state the insufficiency conjecture and exact witness. Actual official page images evidence/official-p08.png and official-p13.png were inspected, including the algebraic-closure overbar. The article does not prove this witness's nonrecognizability; the manuscript correctly supplies that new conclusion rather than attributing it to the source.
- **MPSfull**: Same authors and title, [arXiv:2502.07356v2](https://arxiv.org/abs/2502.07356v2), revised 12 January 2026; record supplies DOI 10.48550/arXiv.2502.07356. Lemma 50/Appendix B.1, pp.26-27, gives squarefree linearization; Appendix B.4, p.28, gives the polynomial pumping calculation. Section 2 and Appendix A use eventual exponential-polynomial representation. The final exposition states that convention; the witness's displayed polynomial holds at every n>=0. No inference from the source's typographically problematic half-integer-set shorthand is needed: the manuscript directly generates the polynomial over Z[1/2].
- **MR19**: Filip Mazowiecki and Cristian Riveros, JCSS 100 (2019), pp.1-29, DOI 10.1016/j.jcss.2018.07.002, verified in the [author-hosted journal PDF](https://criveros.ing.uc.cl/papers/jcss19.pdf), first page. Propositions 1-2 concern normal/reset structure; Proposition 3, p.9, assumes a non-zero semiring. Theorem 1, pp.12-14, is the natural-semiring Fibonacci separation; Theorem 2, pp.14-18, concerns max-plus reversal. The manuscript preserves these hypotheses and does not claim they establish rational-field separation.
- **PS24**: Antoni Puch and Daniel Smertnig, [arXiv:2410.03444v2](https://arxiv.org/abs/2410.03444v2), revised 29 October 2024, DOI 10.48550/arXiv.2410.03444 confirmed by the primary record. Actual body Theorem 3.4/Corollary 3.5, p.16, and Proposition 9.4, pp.49-50, concern invertible semigroup/weighted representations and block-triangular monomial covers. A three-dimensional upper-unitriangular action already has one-dimensional monomial diagonal blocks while its letters may fail to commute; hence those criteria alone do not supply the copyless commutation obstruction. This is an explicit comparison, not an attribution of the new proof.

## Fixed claim-by-claim support, in order

| Claim | Status and support |
|---|---|
| C01 | Verified paraphrase: MPS26 Theorem 15, Section 3.2, Example 26. |
| C02 | In-scope original theorem: claim.json; frozen resolution-proof; manuscript Theorem 1 and Sections 6-7. Full finite control, polynomial copyless updates, arbitrary finite registers and rational constants retained. |
| C03 | In-scope original theorem: accepted one-state unipotent obstruction; manuscript Theorem 2 and Sections 3-5. |
| C04 | Frozen proof support: retraction, polynomial projection and simultaneous transfer, Sections 3-4; no physical inverse assumed. |
| C05 | Frozen proof support: return-word construction, Section 7. |
| C06 | Verified paraphrase: MPSfull Lemma 50, Appendix B.1. |
| C07 | Verified paraphrase: MPSfull Appendix B.4. |
| C08 | Verified paraphrase: MR19 Propositions 1-3, Theorems 1-2; semiring qualifications preserved. |
| C09 | Verified paraphrase plus explicit comparison: PS24 Theorem 3.4, Corollary 3.5, Proposition 9.4; UT3 has monomial diagonal blocks. |
| C10 | Frozen proof/direct substitution support: disjoint copyless supports give multiaffinity and composition, Section 2. |
| C11 | Direct construction: missing transitions go to a constant-zero output sink; no new model restriction. |
| C12 | Verified source convention: MPS26 Definition 11, Section 2 and MPSfull Appendix A; final EPS wording clarified. |
| C13 | Known baseline and self-contained proof: MPSfull Lemma 50; manuscript Section 2. |
| C14 | Frozen proof support: explicit residual map with kernel N and invariant W,N, Section 2. |
| C15 | Frozen proof support: rational specialization and disjoint-support surjectivity, Lemma 3. |
| C16 | Frozen proof support: minimum attained in {0,...,r}, active-output count for ee, Section 3. |
| C17 | Frozen proof support: retraction and polynomial Chinese remainder projection, Lemma 4. |
| C18 | Frozen proof support: (I-Ebar)M_e=0 and invertible M_e, Section 3. |
| C19 | Frozen proof support: substitution identity and minimal eae active count, Section 4. |
| C20 | Frozen proof support: explicit common quotient isomorphism, Section 4. |
| C21 | Frozen proof support: Lemma 5, including zero-dimensional register image. |
| C22 | Frozen proof support: k! power, affine coordinate splitting, Lemma 5. |
| C23 | Frozen proof support: rational-spectrum polynomial Jordan factors and invariant subquotients, Lemma 5. |
| C24 | Exact identity: truncated binomial substitution modulo X^d, Equation 7. |
| C25 | Exact matrix/concatenation identities checked against formula, Equations 8-9. |
| C26 | Exact symbolic summation and n->n+1 shift, Equation 10; empty words included. |
| C27 | Exact generator/coefficient check: -1 and 1/2 generate the needed subring; only base 1, Section 6. |
| C28 | Frozen proof/direct finite-graph argument: shortest SCC return paths and density inequalities, Equation 11. |
| C29 | Frozen proof support: actual return-block updates at q after p, Section 7; composition retains copylessness. |
| C30 | Exact 3x3 multiplication and three independent row/column spans, Equation 12 and Section 7. |
| C31 | Frozen proof support: canonical simultaneous similarity and noncommuting transpose contradiction, Section 7. |
| C32 | Verified scope: proof uses polynomial projection, no group-image assertion, no register bound; finite checks expressly diagnostic. |

## Search scope, dependencies, and final references

The applicable author/year/title, exact-title/arXiv, venue, DOI and arXiv-ID search templates were run for all four records; searches with broad surnames returned irrelevant leads, which were discarded. Primary publisher, versioned arXiv and journal-PDF records supplied the conclusions above. Follow-up searches used copyless + sum of the positions, copyless + uniform pumping + positions, and copyless + unipotent + commute. No equivalent separation was identified among returned primary leads on this date. This bounded screen does not prove priority; the manuscript makes no exhaustive-first or priority assertion. The accepted innovation report supplies the independent local substantive-value assessment, not external peer review.

literature/user_bibliography_check.md was inspected. No Excel or authoritative user bibliography was designated, and no quota or invented workbook was used. All four entries are directly pertinent. All four rendered bibliography entries and in-text keys [1]-[4] were checked on the final PDF. The complete sorted publication.json input set, local recorder inputs, BibTeX database/style, vendored official class and auxiliary generated bibliography were reviewed. evidence/release/dependency-check.json has no unlisted nonauxiliary local TeX input. No authored external import or figure exists. Noncompiled README/class-source/build documentation entries are intentional package inputs. Every listed input is bound by the current manuscript snapshot.

Verdict: accept. No citation limitations remain to disclose. The manuscript introduces no mathematics beyond the accepted frozen claim. Release edits are only the source-convention clarification and shorter factual AI methodology paragraph, recorded in evidence/release/editorial.diff.
