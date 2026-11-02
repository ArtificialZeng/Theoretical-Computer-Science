# Current primary comparison and proposed substantive delta

Research job c025-incdec-research-76b5f4e5209a, refreshed 2026-11-01 UTC.
This is the proposer's bounded literature screen, not a fresh referee verdict
or a proof of priority.

## Direct original-scope source

Disser, Klimm, Lutz and Strubberg, *Incremental–decremental maximization*,
Acta Informatica 63, article 31 (2026), DOI 10.1007/s00236-026-00546-x.
Publisher: https://link.springer.com/article/10.1007/s00236-026-00546-x
Preprint: https://arxiv.org/abs/2508.14516 (current record displays v1,
20 August 2025). The preserved journal PDF/text are source inputs, not outputs.

The publisher page and local primary text were rechecked at Section 1's model
and infimum-over-algorithms definition, Section 1.1/Corollary 2/Table 1,
Proposition 11, Section 3's algorithm description, Proposition 17, and
Appendix B Proposition 19/Corollary 20. The source's full-pair upper bound is
1+e/(e-1), while its structural lower bound is 2. Its deterministic algorithm
compares marginal h utility of extending the constructed prefix against
marginal g utility of extending the unconstructed suffix. Its exact worst-case
ratio is 1+e/(e-1), including an instance with modular g. Its equal-total
2 result does not cover arbitrary unequal totals.

The proposed algorithm instead compares *actual objective differences*
F(P+e)-F(P), chooses one direction from endpoint totals, and continues through
negative gains. It has no interleaved right deletions in its forward orientation.
Thus the theorem is not claimed to be a new analysis of the source algorithm,
and its source-algorithm lower examples are not contradicted. The proof does
not assume that a generic nonmonotone submodular function admits such a ratio;
it explicitly uses the h/g decomposition for a bounded union loss and endpoint
upper bound. The source's Proposition 18 on arbitrary nonmonotone incremental
objectives is therefore not contradicted either.

The proposed substantive advance is a uniform sharp upper bound of 2 on the
ENTIRE original pair class, with polynomial oracle access, matching the existing
structural lower bound. The one-budget cancellation and endpoint choice are the
new proposed mechanism, not a new lower bound. The proof uses elementary
submodularity, but the claimed payoff is full sharp resolution of the source
gap rather than an elementary restricted corollary. No previously verified
result in this bounded screen directly supplies that complete chain theorem.
Whether this simple observation has been published elsewhere, whether its value
meets the user's substantive-innovation bar, and whether it has STOC importance
or depth must be assessed independently by the fresh referee. No confidence
score or readiness label is assigned here.

## Adjacent current primary sources

Bienkowski, Blikstad, Byrka, Costa, Disser and Lutz, *Incremental Submodular
Maximization: Better Than Greedy*, ESA 2026, 134:1-23,
DOI 10.4230/LIPIcs.ESA.2026.134.
https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2026.134
The official record was reopened. The preserved primary introduction explains
that its 1.373 monotone-incremental guarantee sacrifices computational efficiency.
It handles the single monotone objective case (g=0), not the arbitrary pair.
No efficient 1.373 bound or original-pair resolution is inferred from it.

Chen and Kuhnle, *Curvature Beyond Positivity: Greedy Guarantees for Arbitrary
Submodular Functions*, arXiv:2605.07902v1, 8 May 2026.
https://arxiv.org/abs/2605.07902
The current primary abstract was inspected. It gives curvature-dependent greedy
with pruning and multilinear guarantees for general submodular optimization.
That abstract does not state the present all-cardinality single-permutation
ratio-2 theorem. Its full 44-page text was not checked during this bounded job;
this is an explicit residual literature limitation, not an asserted separation
from every theorem in that paper.

Feldman and Ward, *Submodular Maximization over a Matroid k-Intersection:
Multiplicative Improvement over Greedy*, ICALP 2026, 89,
DOI 10.4230/LIPIcs.ICALP.2026.89.
https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.89/LIPIcs.ICALP.2026.89.html
The primary abstract/introduction concern optimizing a set under a given
matroid intersection and extensions to nonmonotone functions. They do not state
a single chain simultaneous across all cardinalities of the present h/g pair
model. No claim about all of its technical theorems is made here.

## Search coverage and limits

Queries included the exact original title; incremental/decremental with
submodular, deterministic, competitive ratio, actual or net marginal greedy;
2-competitive with incremental–decremental; and nonmonotone submodular greedy
with initial value/all-cardinality terms. Only primary sources above were used
for mathematical comparisons. No full equivalent resolution was identified
in these checked sources on this date. The search is bounded and cannot certify
priority. In particular a generic theorem expressed through additive
nonmonotonicity rather than this application could contain an antecedent;
this is a specific useful novelty check for fresh review.
