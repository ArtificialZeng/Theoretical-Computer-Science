# Bounded primary-literature triage

Job `curvature-noise-triage-903fc47916c5`; inspected 2026-10-31 Asia/Shanghai.
Disposition: **status-uncertain; admit a bounded research test**, not acceptance.
No equivalent sharp joint curvature/persistent-noise lower bound was found in
the passages below. This bounded search does not establish novelty or open status.

## Inspected primary statements

1. Thibaut Horel and Yaron Singer, *Maximization of Approximately Submodular
   Functions*, NIPS 2016. [Official proceedings record](https://proceedings.neurips.cc/paper_files/paper/2016/hash/81c8727c62e800be708dbf37c4695dff-Abstract.html),
   [official PDF](https://proceedings.neurips.cc/paper_files/paper/2016/file/81c8727c62e800be708dbf37c4695dff-Paper.pdf).
   Inspected local `literature/horel-singer-nips2016.pdf`; text extraction in
   `evidence/horel-singer-nips2016.txt`. Printed p.2 defines approximation against
   noisy F, and separately explains transfer to underlying f. Printed pp.4--6,
   Section 2.1, equation (3), Lemma 2, Theorem 3: a hidden-set sum of a modular
   function and capped rank, made indistinguishable on a baseline transcript;
   the theorem's parameter choice has large k and does not state the proposed
   fixed-curvature sparse-k result. Printed p.8, Section 3.2 Proposition 8:
   (1-curvature)*rho^2 for noisy F. **These ingredients and algorithm are prior
   work.** [Later deposit](https://arxiv.org/abs/2411.10949) is submitted in 2024;
   [v1 full text](https://arxiv.org/html/2411.10949v1), Appendix D, Lemma 12 and
   proof of Proposition 8 explicitly select top noisy singletons. The direct
   true-f factor is (1-curvature)*rho, not a new theorem. Its refinement by a
   largest-singleton term is also elementary; proposed novelty cannot rest on it.

2. Maxim Sviridenko, Jan Vondrak, Justin Ward,
   [*Optimal approximation for submodular and supermodular optimization with bounded curvature*, arXiv:1311.4728v3](https://arxiv.org/html/1311.4728v3).
   Inspected Section 6.1 Theorem 6.1: exact-value-oracle algorithm achieves
   1-c/e-O(delta), with high probability, under a matroid. Section 7 Theorem
   7.1 states a corresponding polynomial-value-query obstruction beyond
   1-c/e by any fixed additive constant, even for cardinality constraints.
   This supplies the noiseless comparison, with its accuracy slack retained.
   It does not by itself prove a noisy bound by substituting parameters.

3. Avinatan Hassidim and Yaron Singer,
   [*Submodular Optimization under Noise*, COLT 2017](https://proceedings.mlr.press/v65/hassidim17a/hassidim17a.pdf).
   Inspected Theorem 8 and start of Section 5 (printed p.17), and Section 4.3
   (printed p.13). They already prove a randomized-query lower bound for
   adversarial multiplicative error; general adversarial-noise hardness is not
   a new contribution here. No curvature occurrence was found by text search.
   Also inspected the displayed hidden-set functions and switch oracle in
   Section 5, printed pp.17--18: their stated choice has k=n^(1/2+delta).
   Normalization into the proposed exact-curvature family remains a research
   obligation; the inspected statement itself does not give that calibration.

4. [*A Unified Approach to Submodular Maximization Under Noise*, arXiv:2510.21128](https://arxiv.org/html/2510.21128).
   Inspected cached `literature/stochastic-noise.html`, Section 2, “Noisy value
   oracle”: noise is persistent, unbiased, independent across different sets,
   and subject to a sub-exponential distribution condition. These hypotheses
   differ from the arbitrary fixed adversarial error map of this problem.
   Persistence alone does not make the results interchangeable.

5. Vaneet Aggarwal,
   [*Adversarial Resilience of Poisson-Process Submodular Maximization over Matroids, and Full-Bandit Learning*, arXiv:2608.12134v2](https://arxiv.org/html/2608.12134v2).
   Inspected Section 3.1 controlled-oracle definition and Section 5.6,
   Theorem 5.14: additive uniform error radius xi, factors approaching 1/e or
   1-1/e with an additive loss 8*k*xi, for objectives valued in [0,1]. This
   is an actual persistent adversarial oracle theorem, not merely stochastic.
   Substitution of multiplicative error gives a generally nonconstant loss
   proportional to k*epsilon after scaling; it does not certify or refute the
   proposed barrier in epsilon*k tending to infinity. Its proof dependencies
   were not audited in this triage.

## Search coverage and unresolved leads

Queries included `submodular persistent adversarial multiplicative noise bounded
curvature lower bound approximation`, `"submodular" "curvature" "approximately"
"lower bound" noise`, and `"persistent" "curvature" "submodular" oracle lower
bound`. Search snippets and secondary AI summaries were used only as discovery
leads, never as theorem evidence. A possible adjacent paper is Gong--Liu--Geng--Fang,
*Algorithms for maximizing monotone submodular function minus modular function
under noise*, DOI 10.1007/s10878-023-01026-5. Inspected its
[primary publisher abstract](https://link.springer.com/article/10.1007/s10878-023-01026-5):
it concerns submodular-minus-modular objectives under multiplicative noise and
three deterministic bicriteria algorithms. The page exposes subscription preview
content, not the theorem text. Its exact primary theorem still needs inspection,
especially whether extra modular information or bicriteria feasibility changes
the model. No conclusion about equivalence is justified yet. This access
limitation does not block the mathematical test.

The proof of Sviridenko--Vondrak--Ward Theorem 7.1 was also inspected: adding a
uniform modular term to tune curvature is explicitly a known lower-bound
technique. A new proof must explain why the calibrated noise loss and parameter
regime give substantive content beyond this generic transformation.

Local `selection.md` was compared: this is its persistent-noise lead, distinct
from the coverage result and the stochastic-noise entry. No historical registry
is present inside this project; no global deduplication is claimed. The seed
already credits the capped-rank origin. The proposed delta is its sharp
calibration and epsilon*k asymptotics, not a new lower-bound paradigm.

No PDF, claim acceptance, or release certification was produced. Follow-up must
establish analytic correctness and finish the equivalence checks before claiming
a nontrivial new result.
