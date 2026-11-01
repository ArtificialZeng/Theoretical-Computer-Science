# Focused primary-source comparison for the expanded revision

Job: coverage-sparse-research-357cde21e920. Checked 2026-10-31 Asia/Shanghai.
This is a bounded literature screen, not a priority or conference-fit certificate.
Dates and retrieval details belong in this dossier, not in the future paper.

## Required foundational and nearest citations

1. **Agrawal, Ding, Saberi and Ye (2012), Price of Correlations in Stochastic
Optimization**, Operations Research 60(1), 150--162,
[DOI 10.1287/opre.1110.1011](https://doi.org/10.1287/opre.1110.1011).
The author-hosted source PDF and its extracted text were inspected: Theorem 2
and the submodular specialization in Section 3 give the classical mutual-
independence correlation-gap context. The future paper should cite this
foundation when introducing the moment-information question. Its denominator
is the independent expectation, rather than a graph-constrained maximum.
Local primary input: revision/literature/adsy2012.pdf; publisher-deposited
metadata: revision/literature/Agrawal2012-crossref.json.

2. **Calinescu, Chekuri, Pál and Vondrák (2011), Maximizing a Monotone
Submodular Function Subject to a Matroid Constraint**, SIAM Journal on
Computing 40(6), 1740--1766,
[DOI 10.1137/080733991](https://doi.org/10.1137/080733991).
The source PDF was inspected at its introduction, Theorem 1.1 and discussion
of multilinear extension, continuous greedy and pipage rounding. It supplies
the submodular-optimization foundation; its matroid feasibility constraints
are distinct from graph-tested moment constraints. No claim here improves
its matroid approximation theorem.
Local primary input: revision/literature/ccpv2011.pdf; publisher-deposited
metadata: revision/literature/Calinescu2011-crossref.json.

3. **Ramachandra and Natarajan (2025), Pairwise independent correlation gap**,
Operations Research Letters 60, article 107255,
[DOI 10.1016/j.orl.2025.107255](https://doi.org/10.1016/j.orl.2025.107255).
Read the [original arXiv v3](https://arxiv.org/html/2209.08563v3), Section 1.1,
Definition 2 and Theorem 5. The displayed n=3 constant 27/19 in Section 1.1
belongs to f^+/F, where F is the MUTUALLY independent multilinear extension.
Theorem 5 gives the sharp n=3 PAIRWISE-optimized bound f^+/f++<=4/3.
These are different denominators. Our k is a graph-color bound, whereas n=mk
counts variables; the numerical expression alpha_k does not identify the
models. The reviewer response must make this correction respectfully.
Local text: revision/literature/rn2025.html; publisher-deposited metadata:
revision/literature/RamachandraNatarajan2025-crossref.json. The cached
rn2025-endpoint-response.html is an HTML response, not a source PDF.
Its failed earlier retrieval is not evidence that the reference or PDF does
not exist. The arXiv primary text suffices for these checked statements.

4. **Ramachandra and Natarajan (2026), Counterexample to a conjecture on the
pairwise independent correlation gap using AI**, arXiv:2606.19663v1.
Read [Section 2 and the following remarks](https://arxiv.org/html/2606.19663v1).
The five-element weighted-coverage example has numerator 4 and a certified
pairwise denominator at most 479/160, giving a ratio at least 640/479>4/3.
This disproves the proposed universal pairwise 4/3 bound. It does not dispute
the earlier n=3 theorem or our bipartite tested-graph result. Cite the original
counterexample, without treating an automated index as proof of its content.
Local primary text: revision/literature/rn2026-counterexample.html.

5. **Ramachandra (2026), Dimension Dependent Correlation Gap Bounds under
Restricted Independence**, arXiv:2609.02659v1.
Reinspected [Theorem 2 and Sections 4.1--4.2](https://arxiv.org/html/2609.02659v1).
They already give the Cartesian coverage family and asymptotic e/(e-1)
pairwise lower bound as both block size and block count grow; the paper
also states the t-wise consequence. Those are prior results. The revised
R7 gives an explicit finite sandwich and rate from a within-block-only
certificate. The proposed core delta remains fixed-k graph-class sharpness,
which survives deletion of all cross-block tests. Deleting constraints
increases the optimized denominator, so the all-pairs lower-bound theorem
alone does not prove this sparse tightness assertion.
Local primary text: literature/ramachandra2026.html. This bounded pass did
not independently reproduce that source's separate n=4 computational proof;
our proofs do not depend on it.

6. **Dütting, Fusco, Lattanzi, Norouzi-Fard, Svensson and Zadimoghaddam
(2025), The Cost of Consistency: Submodular Maximization with Constant
Recourse**, STOC 2025, 1406--1417,
[DOI 10.1145/3717823.3718131](https://doi.org/10.1145/3717823.3718131).
Reinspected [Section 3.2, Coverage Functions](https://arxiv.org/html/2412.02492v1):
the two-group hit-probability calculation gives the 3/4 resampling factor.
R1 extends this per-feature argument to k groups. Attribute the ingredient;
the new claim is not invention of resampling or alpha_k. The official
publisher-deposited Crossref record now directly confirms the proceedings
pages 1406--1417. The former metadata limitation is resolved.
Local inputs: literature/cost-consistency2025.html and
revision/literature/Dutting2025-crossref.json.

7. **Udwani and Wajc (2026), Online Submodular Welfare Maximization:
Computation is not the Bottleneck**, arXiv:2610.16060v1.
The [primary arXiv record](https://arxiv.org/abs/2610.16060) exists, identifies
both authors and lists “In FOCS 2026.” The [original full text](https://arxiv.org/html/2610.16060v1),
Definition 3.1 and Lemma 3.4, uses the same probability-coverage polynomial;
its online-allocation bounds also involve alpha_k. Cite the accessible
preprint accurately without fabricating proceedings metadata or treating
indexing delay as nonexistence. Its stated model is online welfare, rather
than optimization under prescribed graph-tested pair moments.
Local primary record: revision/literature/uw2026-record.html.

## Additional lead and search limits

A primary-source search also located Ramachandra and Natarajan,
[Tight Probability Bounds with Pairwise Independence](https://arxiv.org/abs/2006.00516),
with a [SIAM publisher record](https://epubs.siam.org/doi/abs/10.1137/21M1408294).
Its inspected abstract concerns the union probability of one family of
pairwise independent events and a 4/3 union-bound ratio. The full family of
its graph-related subsidiary bounds was not re-audited in this pass. A
single-feature probability bound does not automatically optimize a sum of
features with one common feasible law. This lead limits the completeness
of any negative novelty assertion; it is not a mathematical dependency.

Live queries screened combinations of “correlation gap” with “chromatic,”
“colorable,” “sparse pairwise,” “graph-tested,” “moment errors,”
“heterogeneous pairwise,” and “coverage matching 3/4.” The nearest inspected
primary statements above did not exhibit the complete fixed-k sparse
class theorem or the added exact matching/error formulas. This establishes
only that no equivalent was identified in these sources and queries on
this date. It does not prove priority or exhaustive novelty. Secondary
aggregators returned by the searches were not used to support technical
claims. The refined theorem remains modest in relation to its known
construction and elementary upper-bound ingredient; a fresh referee should
assess both its correctness and contribution size.

No user Excel bibliography was consulted or created. No missing source
metadata is being used to block the mathematically justified local revision.
