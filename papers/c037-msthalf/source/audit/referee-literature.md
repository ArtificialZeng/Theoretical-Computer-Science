# Fresh primary-literature comparison

Referee job: `c037-msthalf-referee-9071a36d85a3`.
Checked 2 November 2026 UTC against frozen snapshot
`d0a2fbd366a632f17366053e75f1a37a1254cc80a92e14c60a7d14734548277b`.
This is an internal bounded search, not an exhaustive priority certification.

1. Anand, Gupta, Jayaram, Lee and Vakilian, *Approximating Minimum Spanning
   Trees in Metrics under Semi-Random Corruptions*, arXiv:2610.40594v1
   (29 October 2026). The current [primary record](https://arxiv.org/abs/2610.40594)
   displays only v1 and the comment SODA 2027. I inspected its
   [full text](https://arxiv.org/html/2610.40594v1) and the frozen local text,
   particularly Definitions 2.1–2.3, Lemma 3.2, Lemmas 4.4 and 5.6,
   Theorems 1.4/5.3 and 1.5. The upper-bound model matches the original
   question, including an adversary that sees the whole mask, observations
   without triangle inequality, no true-distance queries, and expected true
   tree cost. Its general-corruption upper bound assumes p<1/4. Its
   decrease-only result assumes a restriction unavailable here. Its
   repair tree and preorder constructions are antecedents, explicitly credited
   by the candidate. The proof of Lemma 5.6 requires bad-pair density below
   one half to force a common-neighbor charging contradiction. It does not
   establish the positive-density rectangle-to-metric transfer proved here.
   The stated half-threshold lower bound supplies the comparison boundary;
   the candidate supplies no new lower bound. The source's displayed
   construction has zero intracluster distances; its asymptotic linear
   obstruction also holds for strict metrics by using a small positive
   intracluster value, as explained in `audit/math.md`.

2. Bateni, Dharangutte, Jayaram and Wang, *Metric Clustering and MST with
   Strong and Weak Distance Oracles*, COLT 2024, PMLR 247:498–550.
   I checked the [official record](https://proceedings.mlr.press/v247/bateni24a.html)
   and [official paper](https://proceedings.mlr.press/v247/bateni24a/bateni24a.pdf),
   including Theorem 4 and Appendix F.2.2/Theorem 32. Theorem 4 assumes the
   weak observations themselves form a metric and gives a no-strong-query
   O(sqrt(log n)) approximation. That hypothesis fails for the arbitrary
   observations in this project. Theorem 32 gives a logarithmic obstruction
   at corruption probability 1/3. It does not close the upper-bound threshold
   gap. I do not infer an identical logarithmic lower bound for every p,
   particularly p=0.

Fresh searches used the exact title, identifier with “improved”,
“minimum spanning tree semi-random corruptions half threshold rectangle
interval packing”, “semi-random corruptions MST 1/2”, “corrupted minimum
spanning trees threshold”, “rectangle metric dominating spanning trees
corruption”, “corrupted metric rectangle”, and general-corruption MST with
2026/2027. Only primary sources above support the technical conclusions.
Search noise, mirrors and aggregators were not treated as verification.
No equivalent full p<1/2 general-corruption upper bound or equivalent
rectangle transfer theorem was identified in these searches. Unindexed,
unpublished, or differently phrased work remains a limitation of the search.

The specific substantive delta is a certificate feasible under arbitrary
post-mask changes and a deterministic all-metric interval-packing argument
requiring only positive density in every sufficiently large disjoint
rectangle. Together they settle the whole remaining interval below one half.
The extension is not supplied by substituting a different parameter into
the prior common-neighbor proof. Algorithmic efficiency and consequences
for other objectives remain unproved and are not accepted claims.
