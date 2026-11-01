# Focused primary-source comparison, research pass 1

Job: `coverage-sparse-research-6239617d8b3f`.
Inspected live on 2026-10-31 Asia/Shanghai (2026-10-30 UTC).
This supplements `triage-literature.md`; it is not a priority certificate.

## Nearest results and the exact proposed difference

1. Arjun Ramachandra, *Dimension Dependent Correlation Gap Bounds under
   Restricted Independence*, arXiv:2609.02659v1.
   [Primary text](https://arxiv.org/html/2609.02659v1), Theorem 2,
   Sections 4.1.1--4.1.3, equations (13)--(15), (24).
   Reinspected the theorem and Cartesian family. The theorem imposes all
   pairs and takes both block size and block count to infinity. Its reduced
   dual includes a cross-block coefficient; the displayed choice in (24)
   makes that coefficient nonzero. The current witness is the same family
   with equal-size blocks and normalized weights. Our proposed difference
   is fixed block size `k`, no cross-block tests, a rational finite certificate,
   exact graph-class suprema, and one-sided error stability. The all-pairs
   theorem alone does not imply the sparse lower bound: deleting constraints
   increases the denominator, in the direction that weakens a ratio lower
   bound. This is a logical comparison, not an audit of that paper's proof.

2. Paul Dütting et al., *The Cost of Consistency: Submodular Maximization with
   Constant Recourse*, arXiv:2412.02492v1.
   [Primary text](https://arxiv.org/html/2412.02492v1), Section 3.2,
   Coverage Functions, and the surrounding two-sample question.
   Reinspected the two-group coverage calculation: independent hit probability
   is `beta+theta-beta*theta`, compared with a coupled hit probability at most
   `min{1,beta+theta}`, yielding `3/4`. The `k`-group calculation in our upper
   bound is an elementary extension of this prior ingredient and must not
   carry a standalone novelty claim. The inspected assertion concerns
   decorrelation of two sampled set families; it does not give the sparse
   graph-class tightness or finite within-clique moment certificate.

3. Rajan Udwani and David Wajc, *Online Submodular Welfare Maximization: Computation is not the Bottleneck*,
   arXiv:2610.16060.
   [Primary text](https://arxiv.org/html/2610.16060), Section 3.1,
   Definition 3.1, Lemma 3.4, Corollaries 3.5--3.6.
   Reinspected the same Cartesian coverage polynomial and the special
   no-collision formula. These are known ingredients. The paper optimizes
   online allocation with hidden partition information; the inspected results
   do not optimize distributions under graph-tested pair moments. Literal
   searches for `pairwise` and `color` found no matches in this HTML, a search
   aid only. It further limits novelty to the exact sparse graph theorem.

## Search record and limitations

The current arXiv abstract records for all three papers were also opened;
each lists only version 1 as of this check. The versioned texts inspected
therefore match the latest records returned by arXiv.

Fresh live queries included:

- `"correlation gap" "colorable"`
- `"coverage" "correlation gap" "block" independence graph`
- `"Dimension Dependent Correlation Gap Bounds under Restricted Independence"`
- `"correlation gap" "partial independence" coverage`
- `"correlation gap" "chromatic number"`
- `"coverage" "decorrelation" "blocks"`
- `"correlation gap" "bounded degree" graph`

No equivalent full graph-class theorem was identified in these searches or
the inspected primary statements. This is a bounded negative search, not
proof of novelty or of a previously recognized open problem. A differently
phrased block-decorrelation theorem could subsume the upper bound; that alone
would not dispose of the lower-bound contribution. No historical cross-project
registry is available in this project. The fresh referee should test whether
the combined sparse tightness and error certificate are already known or too
minor to support a contribution. No venue-fit claim follows from the proof.
