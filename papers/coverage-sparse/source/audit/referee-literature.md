# Fresh primary-source comparison

Job: `coverage-sparse-referee-ec417dd22ce0`.
Checked live on 2026-10-31 Asia/Shanghai (2026-10-30 UTC).
This is a bounded contribution screen, not a priority certificate.

## Actual primary statements inspected

1. Arjun Ramachandra, *Dimension Dependent Correlation Gap Bounds under
   Restricted Independence*, arXiv:2609.02659v1, [primary text](https://arxiv.org/html/2609.02659v1).
   Inspected Theorem 2, Remark 7, Sections 4.1.1--4.1.3, and the displayed
   dual in Section 4.2, equations (22)--(24). Theorem 2 concerns all-pairs
   independence and asymptotic e/(e-1) tightness with block count and block
   size both diverging. The Cartesian feature construction and its numerator
   are prior work. Equation (24) has a nonzero cross-block coefficient.
   The submitted statement fixes the block size, permits every cross-block
   moment to vary freely, and proves matching class suprema with a finite
   one-sided error bound. Removing constraints increases the optimized
   denominator, so the all-pairs lower bound does not imply this sparse
   lower bound. I did not re-audit the prior paper's complete proof.

2. Paul Dütting et al., *The Cost of Consistency: Submodular Maximization
   with Constant Recourse*, arXiv:2412.02492v1,
   [primary text](https://arxiv.org/html/2412.02492v1), Section 3.2,
   Coverage Functions. Inspected the independent two-sample hit calculation
   and its comparison with the coupled union probability. It gives the
   familiar 3/4 factor. The submitted k-color resampling bound is an
   elementary multi-group version of that ingredient and must not be sold
   as a new decorrelation principle. The inspected assertion does not bound
   all joint laws obeying only within-clique moment tests, or give their
   sparse graph-class tightness.

3. Rajan Udwani and David Wajc, *Online Submodular Welfare Maximization:
   Computation is not the Bottleneck*, arXiv:2610.16060,
   [primary text](https://arxiv.org/html/2610.16060), Section 3.1,
   Definition 3.1, Lemmas 3.2 and 3.4, Corollaries 3.5--3.6 and their
   correlation-gap discussion. The same normalized Cartesian polynomial
   and alpha_k constant are explicit. The no-collision specialization and
   concavity step are also explicit. In that setting, zero collisions are
   forced by restricting which item marginals may be positive within a
   part. In the submitted witness, every item has positive marginal and
   collisions are possible; their total expectation is controlled by
   tested moments. Thus the cited corollary does not directly apply to
   the submitted feasible laws. The exact collision penalty and sharp
   graph-class conclusion require an additional argument.

## Fresh search coverage

Queries used, in addition to opening the three primary texts:

- `"correlation gap" "colorable"`
- `"coverage" "pairwise independence" "graph"`
- `"correlation gap" "sparse" independence`
- `"pairwise independent correlation gap" graph restricted`
- `"correlation gap" "partial independence"`
- `"correlation gap" "bounded degree"`
- `"coverage functions" "decorrelation" blocks`
- `"correlation gap" "tested" pairs`
- `"correlation gap" "graph" "chromatic"`
- `"pairwise independent" "coverage" "blocks"`
- `"correlation gap" "one-sided"`

Search results were used to locate sources, not as mathematical evidence.
No equivalent full sparse graph-class theorem was identified in this bounded
search or in the inspected primary statements. A search hit using an
"independence graph" for sensors concerned simultaneous operation, rather
than the graph-tested Bernoulli moment model; no mathematical inference was
drawn from that hit. This screen does not establish universal novelty or
recognized open-problem status. No bibliographic access failure was used
to infer a mathematical result.

## Contribution assessment

The upper-bound method, constant and Cartesian family are known ingredients.
The additional result controls all couplings under sparse moment tests,
including cross-block couplings absent from the compared prior formulations,
and identifies the sharp fixed-k graph-class hierarchy. The rational pointwise
certificate makes the one-sided error statement quantitative. Its credible
use is to distinguish the strength of graph-tested second-moment information
from all-pairs independence when optimizing a coverage expectation. This is
a coherent contribution of sufficient mathematical substance to accept the
frozen resolution scope; no conference acceptance or global priority follows.
