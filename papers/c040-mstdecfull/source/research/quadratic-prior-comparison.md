# Primary comparison for the strongest same-original claim

Proposer: c040-mstdecfull-research-e695ca56645f, accumulated research pass 2.
This is a research comparison, not a fresh mathematical or STOC review.

The immutable original asks for all fixed p<1, zero true queries, expected
O_p(log^4 n) approximation, and aspect-independent quasipolynomial operations
on every execution. The complete proposed algorithm in
research/quadratic-resolution-proof.md satisfies these quantifiers with the
stronger expected O_q(log^2 n) bound and no private randomness. It uses the
same algorithm as the earlier cubic packet; its retained accounting is sharper.

The current primary is Anand, Gupta, Jayaram, Lee and Vakilian,
*Approximating Minimum Spanning Trees in Metrics under Semi-Random Corruptions*,
[arXiv:2610.40594v1](https://arxiv.org/html/2610.40594v1). The live
[record](https://arxiv.org/abs/2610.40594) inspected during this job lists v1
only, submitted 29 October 2026. Theorem 1.2 gives an unrestricted-time
O_p(log n) approximation for every fixed p<1. Theorem 1.3 gives a
quasipolynomial expected O(log^4 n) algorithm for p<=0.1, with a footnote
that some arguments require sufficiently small p. These are prior results.

Section 6 supplies hierarchical carving, admissibility against all future
seeds, the nonaccumulation architecture, aspect normalization and the
promotion/intersection argument. Theorem 6.2 charges random physical leaders
with an O(log n log Delta') overhead relative to hierarchy cost. This proposal
instead charges a deterministic DFS leaf path, using final degree two and
one right exit per child interval. The actual-outlier inequality is

    cost(P)<=2 beta H+12 beta Omega,
    Omega=sum_(i,C) 2^i |C minus core_i(C)|.

Separate generated-cluster and leftover-singleton counts give both
H,Omega<=14R(L+1)MST, whereas substituting the uniform r-outlier budget
before summing gives only the earlier cubic estimate. The high-noise
uniform rectangle bootstrap and high quantiles extend the construction to
all fixed p<1. Distinct seeds actually born are globally disjoint; checking
all overlapping future seeds is definitional completeness and is not claimed
as an essential separate novelty. The quadratic estimate refines the same
DFS insight, not a second independent contribution or a second paper.

Relative to the primary baseline, the proposed complete theorem improves
the entire computational corruption range, the logarithmic exponent and
the need for private randomness. It does not attain the inefficient
logarithmic benchmark, establish polynomial runtime, or resolve arbitrary
increase/decrease corruptions. The meaningful value case concerns the whole
algorithm and reusable extraction lemma. The short accounting refinement
alone would not justify a separate contribution; a fresh referee must still
reject the whole claim if it is routine, known or insignificant.

Fletcher and Hershkowitz, *Spanning Tree Embeddings Are Not Much Harder than
Hierarchical Partitions*, SODA 2026, 5344-5373,
[DOI 10.1137/1.9781611978971.193](https://epubs.siam.org/doi/10.1137/1.9781611978971.193),
is adjacent primary work. Its official abstract concerns graph-spanning
distance embeddings from hierarchies with Omega(log n) growth per level.
This proposal bounds total metric-closure path cost at dyadic levels with
hidden, nonnested outlier cores. The statements differ; the inaccessible
full adjacent proof has not been checked for an equivalent auxiliary lemma.
The access gap is explicit and does not certify priority.

Bateni, Dharangutte, Jayaram and Wang, *Metric Clustering and MST with Strong
and Weak Distance Oracles*, [COLT 2024 primary](https://proceedings.mlr.press/v247/bateni24a.html),
Theorems 4-6, distinguishes metric-preserving observations from unrestricted
observations. Its square-root-logarithmic theorem assumes observed metricity;
it does not give the full nonmetric upper bound here. The exact local primary
text and intake/oracle-primary-model-comparison.md preserve this distinction.

Theorem 7.2 of Anand et al. is a reduction to quietly planted colorability,
not a consequence of the Planted Clique hypothesis or a general computational
lower bound proved by low-degree evidence. Its written construction uses
within-class zero distances. No genuine-metric hardness transfer is claimed
or used by this upper theorem.

Current bounded searches found no equivalent complete all-p quadratic-log
theorem. This is no proof of priority or comprehensive absence. No new venue
judgment is made: the actual old cubic review remains working_paper and does
not cover this new claim. A fresh critical assessment must address technical
depth, importance and breadth before any label could change.
