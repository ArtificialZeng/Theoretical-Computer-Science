# Verification Report

**Mode:** Search plus primary-document comparison.
**Document:** manuscript/main.tex and the final seven-page PDF.
**Overall status:** PASS within release scope.

Job: c029-vftfast-release-bdd37c945f4e. Checked 2026-11-02 UTC.

Mathematical snapshot: b1495a4cbeb794181b64a2bc9a00b637d90f0a7a7fdf654844a24036b4029e66.
Manuscript snapshot: 8013342c36141de01d96e75509498833a97008d1df48c6153524aefa6caa4daa.
PDF SHA-256: 8f61902bb7427aec09254cd8ac7566c87a76748f4dc9eb4d9bbed9828af7a7a8.

The advisory $citation-check-skill was explicitly invoked. Pass 1 is the fixed 25-claim extraction in audit/citation-extraction.md; pass 2 below follows that list without re-extraction. The user authorized completion of this bounded release audit. Mathematical entries mean agreement with the accepted frozen statement and inspected supporting derivation, not a substitute new mathematical referee verdict.

Metric | Count
--- | ---
Claims extracted | 25
Verified for stated release scope | 25
Numerical errors | 0
Unverified claims | 0
Contradicted or misleading attributions | 0

ID | Status | Source and exact scope
--- | --- | ---
C01 | Verified — paraphrase | PPT26 frozen primary, printed pp.4–5, Theorem 1.4 and following runtime paragraph; live arXiv v1 record refreshed.
C02 | Verified — accepted-scope match | source.md, problem.md, claim.json, evidence/research3-resolution.md, accepted audit/math.md; same full graph/fault/parameter quantifiers, no strengthening.
C03 | Verified — exact bounds/paraphrase | DR20 v2 printed p.2 Theorem 2, pp.5–6 Algorithm 2/Theorem 4 and p.9 Theorem 9. Protected-path adaptation is proved locally, not attributed verbatim.
C04 | Verified — paraphrase | BDR21 v3 Theorems 1.1–1.3, deterministic development Section 5; refreshed arXiv abstract and SIAM proceedings primary record.
C05 | Verified — paraphrase | FLPS16 v4 Section 2.5, Section 3 Theorem 3/minor-vector proof, Sections 5.1 and 5.5; journal title/DOI/63(4)/article 29/60 pages confirmed from author-hosted journal PDF pp.1–2.
C06 | Verified — paraphrase | KP23 v3 Theorem 28 and immediately following vertex variant (I5v)/(I6v), plus Section 7. Live HTML title/authors/version/date agree.
C07 | Verified — paraphrase | BCCCS26 v1 abstract and Section 1: edge-fault model and improved covering/query results. No claim of a vertex-fault spanner theorem is attached.
C08 | Verified — paraphrase | BCCS26 v1 abstract and Section 1: edge-fault model and near-optimal covering results. Metadata agrees with live v1 record.
C09 | Verified — accepted-scope match | FLPS Theorem 3 and manuscript proof; frozen resolution representative lemma and accepted referee reconstruction.
C10 | Verified — accepted-scope match | Frozen resolution representative DP and accepted referee reconstruction; cap and avoidance budgets unchanged.
C11 | Verified — accepted-scope match | Frozen protected scan argument, DR20 cut-test antecedent and accepted referee; no arbitrary-H separator claim.
C12 | Verified — paraphrase | PPT26 Claim 4.3; each accepted insertion supplies compatible endpoints and ds<=r.
C13 | Verified — paraphrase/application | PPT26 Algorithm 2, Lemma 4.12/I1–I7, Theorem 4.5 and Lemma 4.16 (printed pp.24–31); application to the partial sequence is explicitly this paper’s verified transfer, not an asserted prior theorem.
C14 | Verified — paraphrase/application | PPT26 Proposition 4.14 and Appendix A Lemma A.1 (printed pp.26–27 and 53–55); manuscript retains uncapped sampling constants and compatible history hypotheses.
C15 | Verified — accepted-scope match | Frozen resolution center-count/rounding derivation; exact parameter evidence; no exponential-in-sqrt(k) factor silently discarded.
C16 | Verified — paraphrase/application | PPT26 Observation 5.8 and Lemma 5.9; longer radius inequalities stated in manuscript and frozen proof.
C17 | Verified — parameter substitution | PPT26 Lemma 5.14 and Theorem 5.15: its exponent 1+1/ceil(stretch/2) becomes 1+1/t when virtual stretch is 2t-1. The source result is credited.
C18 | Verified — accepted-scope match | Frozen witness-transfer proof and accepted referee reconstruction; no containment in a different greedy run asserted.
C19 | Verified — paraphrase/application | PPT26 Appendix B Claims B.1/B.2 and Corollary B.3 (printed pp.56–57); this manuscript spells out identical original faults in augmented graphs.
C20 | Verified — accepted-scope match | Frozen pendant projection and geodesic segmentation; displayed size/stretch match accepted theorem.
C21 | Verified — accepted-scope match | Frozen caps/regime-switch proof; exact integer comparison and f=0/small-k branches retained.
C22 | Verified — exact | evidence/research3-full-checks.json: all counts, parameter ranges, labeled versus ten-mask coverage and maximum augmented N=18 agree exactly.
C23 | Verified — exact | evidence/research3-parameter-checks.json: 20465 cases = 4093 k values times five eta values; zero failures.
C24 | Verified — exact | audit/referee-checks.json: 84 graphs, zero failures, separately implemented checks. No claim of human review or formal verification.
C25 | Verified — accepted-scope match | Runtime proof has exponent dependent on eta=min(delta/2,1/4); no optimized or practical runtime claim.

## Bibliography and access

All seven cited entries exist and support the nearby conservative claims. Author lists, titles, cited years and version dates match the primary records. The BDR bibliography deliberately describes the 2020 v3 preprint and separately notes SODA 2021; KP23 describes its 2023 v3, avoiding confusion with its 2021 extended abstract. The FLPS journal and preprint titles differ and both are accurately identified. All citations are relevant; none was inserted to satisfy a quota. literature/user_bibliography_check.md explicitly records that no user Excel bibliography was designated. No workbook basis was invented.

Live primary sources consulted:

- https://arxiv.org/abs/2610.33934v1 ; frozen intake/primary/VFTAlphaBeta.pdf/.txt.
- https://arxiv.org/abs/2002.10889 ; frozen intake/primary/GreedyVFT2020v2.pdf/.txt; author’s publication record https://www.cs.jhu.edu/~mdinitz/pub.html.
- https://arxiv.org/abs/2007.08401v3 ; https://epubs.siam.org/doi/10.1137/1.9781611976465.174 ; frozen intake/primary/OptimalVFT2021v3.pdf/.txt.
- https://arxiv.org/html/1304.4626v4 ; https://arxiv.org/abs/1304.4626v4 ; https://fedorvf.github.io/articles/2016/2016b.pdf (journal pp.1–2 confirm metadata).
- https://arxiv.org/html/2008.05421v3 .
- https://arxiv.org/html/2604.27966v1 .
- https://arxiv.org/html/2608.07124v1 ; https://arxiv.org/abs/2608.07124v1 .

All applicable academic query templates were run: first author/year/title prefix, full title with arXiv/Semantic Scholar restriction, author/year/venue (arXiv for versioned preprints), each supplied arXiv identifier and the FLPS DOI. Secondary hits were leads only. A direct FLPS DOI refresh returned 403, DR’s v2 abs refresh returned a cache miss, and BCCCS’s v1 abs page returned a cache miss. Alternative primary full texts supply the actual claims and metadata; these endpoint failures leave no reference unverified and do not imply nonexistence. No unsupported priority or first-result assertion appears. The novelty check remains a bounded current comparison with the accepted primary comparisons, not an exhaustive priority guarantee. The actual working_paper assessment is retained.

## Complete dependency scope

Reviewed every publication.json source input: main.tex, references.bib, the unchanged official acmart.cls and ACM-Reference-Format.bst, build.sh, and generated final bbl. The preamble has no additional local imported TeX, graphic or custom package. Recorder output from the isolated build identifies the local class and generated aux/out/bbl; aux/out are build products, not authored dependencies. System TeX packages are installed dependencies. BibTeX consumes the listed bib and bst. All seven cite keys are defined exactly once and occur in the bbl; every reference is present and readable on rendered page 7. No undefined citation or cross-reference appears in the final log or extracted/rendered text. No charts, empirical figures or numerical data visualizations occur.

The editorial changes remove redundant caveats, positively state the accepted construction-time result, and give factual substantial AI disclosure in the body and endmatter. No theorem, bound, parameter, proof or finite-check count changed. The mathematical snapshot’s 17 file hashes still match.
