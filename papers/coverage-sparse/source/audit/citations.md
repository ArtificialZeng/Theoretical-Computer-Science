# Fresh citation and scope audit

Verdict: accept. Job `coverage-sparse-release-baf234409c0d`; checked 2026-10-31
Asia/Shanghai. This is the new release review of the revised manuscript, not a
reuse of an earlier audit. Current digest bindings are in citations.json.

`$citation-check-skill` was explicitly applied as an advisory two-pass check:
the fixed extraction is `evidence/release/baf234409c0d/claim-extraction.md`;
verification followed extraction. The bounded autonomous job instruction
supersedes the skill's interactive confirmation pause. Primary texts, not
search-index summaries, support the attributions below. The search templates
were run for all seven entries, including supplied DOI/arXiv identifiers;
records are in web-search-records.json and web-passages.json in that directory.

## Claim-to-source verification

| Claim | Manuscript location | Primary passage and finding |
|---|---|---|
| C01 | Section 2, paragraph 1 | Agrawal, Ding, Saberi and Ye: local author PDF, Theorem 2 and Section 3.1 (PDF pp. 7–8), compares worst coupling to independent sampling and specializes to submodular costs. Foundational attribution is supported. Metadata agrees with publisher-deposited Crossref record: Operations Research 60(1), 150–162 (2012), DOI 10.1287/opre.1110.1011. |
| C02 | Section 2, paragraph 1 | Calinescu, Chekuri, Pál and Vondrák: local primary PDF, Theorem 1.1 and Sections 2.1–2.3, supports continuous greedy, multilinear extension and matroid optimization context. Crossref confirms SIAM J. Comput. 40(6), 1740–1766 (2011), DOI 10.1137/080733991. No graph-moment theorem is attributed to this source. |
| C03 | Section 2, paragraph 2 | [RN2025 primary text](https://arxiv.org/html/2209.08563v3), Section 1.1 equations (1)–(2), Definition 2 and Theorem 5: the 27/19 constant uses the mutually independent denominator, whereas the sharp three-variable pairwise-optimized bound is 4/3. The manuscript and reviewer response distinguish the models correctly. Crossref confirms ORL 60, article 107255 (2025), DOI 10.1016/j.orl.2025.107255. |
| C04 | Section 2, paragraph 2 | [RN2026](https://arxiv.org/html/2606.19663v1), Section 2: five elements, numerator 4 and denominator at most 479/160 imply ratio at least 640/479>4/3. The manuscript says “at least” and preserves the earlier three-variable theorem. Authors, title, year and v1 agree. |
| C05 | Section 2, paragraph 3; Section 5.1 | [Ramachandra2026](https://arxiv.org/html/2609.02659v1), Theorem 2, Corollary 6, Sections 4.1.1–4.1.2: Cartesian transversals, normalized product formula, uniform whole-block numerator, and known all-pairs/t-wise limit. These are explicitly credited. The finite within-block bound is proved in the manuscript. Authors, title, year and v1 agree. |
| C06 | Section 2, paragraph 4 | [Dütting, Fusco, Lattanzi, Norouzi-Fard, Svensson and Zadimoghaddam](https://arxiv.org/html/2412.02492v1), Section 3.2 “Coverage Functions”: joint versus independent two-group sampling yields 3/4. All six authors appear in prose and references. Crossref confirms STOC 2025, 1406–1417, DOI 10.1145/3717823.3718131; the full-version arXiv v1 is from 2024. |
| C07 | Section 2, paragraph 4 | [Udwani and Wajc](https://arxiv.org/html/2610.16060v1), Definition 3.1, Lemma 3.4, Corollaries 3.5–3.6 and following discussion: probability coverage polynomial, no-collision specialization and alpha_k in online welfare. The source exists and is cited as the October 2026 v1 preprint without invented proceedings metadata. |
| C08 | Theorem 1.1; Lemmas 3.1–3.2; Theorems 3.3/4.1; Corollary 5.1 | Compared the entire manuscript with the freshly accepted expanded claim, snapshot and math report. Hypotheses, class-supremum quantifiers, one-sided errors, matching-witness necessity, t-wise range, square-size subsequence and conditional sampler conversion remain within acceptance. All proofs are present. The full t-wise lower bound correctly uses alpha_m. No general fixed-graph or arbitrary-submodular result has been added. |
| C09 | Tables 1–3; Proposition 4.2 | All 15 constants, all five rows (including every primal mass and dual coefficient), and all 20 profile slacks match exact fractions. Fresh computation is in integrity.json and source-reproduction.json; the packaged read-only launcher reproduces the same outputs. The proof provides rational primal/dual weak-duality certificates, rather than interpreting numerical optimization as proof. |
| C10 | Figure 1 | Actual three disjoint 3-cliques, one orange transversal and shaded B2. Whole-block occupancy gives T=3,C=3; nine edges with moments 1/9 give E C=1. Labels, formula and caption agree. No statistical measurement or data plot is implied. |
| C11 | References, final PDF page | All seven author/title/year/version records match the cited primary records and four publisher-deposited metadata files. Seven citation keys exactly match seven bbl keys; rendered labels and hyperlinks resolve. |

The two foundational PDFs and all frozen source records were actually read at
the relevant passages. Crossref records are cached publisher-deposited metadata,
not a user-designated workbook. `literature/user_bibliography_check.md` explicitly
records that no user Excel list exists; none was fabricated or required. No
unverified record remains for the bibliography used here. Earlier access failures
do not establish nonexistence. We did not require a fresh paid publisher PDF
when the original source text and deposited metadata already support the claim.

## Dependency, novelty and response scope

Every sorted publication.json source_files entry was checked. Compiler recorder
inputs agree with this list; main.aux/main.out are regenerated intermediates.
The official unmodified class, local alpha style, imported body and TikZ file,
bib database, generated bbl, official template/provenance, portable code/data,
handoff and all 19 reviewer responses are included. No omitted local compiler
dependency was found. The current ZIP has 22 current members including
publication.json; its extracted launcher and clean build pass. All eight package
renders equal the eight inspected final renders byte for byte.

The main theorem's exact scope is distinguished once from per-fixed-graph
optimization. The known family, alpha_k, two-group ingredient and asymptotic
limit have appropriate attribution. The paper makes a bounded positive
contribution claim about the within-block certificate, sparse sharpness and
finite refinements; it makes no priority, exhaustive-literature or venue-fit
guarantee. The prior focused comparison and fresh exact acceptance support that
scope; this release audit does not certify novelty by absence of search hits.

All 19 tracked responses point to actual final sections/theorems/equations;
R1.6 explicitly retains general graph, fractional-color and submodular questions.
R2.2 uses the portable source entry point. R1.9/R2.7's final title, float,
proof-clause and factual two-sentence AI-disclosure repairs are present.

No unsupported strengthening or misleading citation was found. Search mode
checks citation support; mathematical correctness continues to rest on the
accepted proof and exact certificates, not this audit or successful compilation.
