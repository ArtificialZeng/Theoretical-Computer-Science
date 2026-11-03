# Precise original problem and triage scope

The immutable statement is source.md; its recorded SHA-256 is in evidence/triage-entry.json. This document interprets that statement without replacing or narrowing it.

## Quantifiers and input model

For every fixed real p in [0,1), there must exist an explicit classical randomized algorithm A_p and constants a_p,C_p>0 satisfying all the following. For every integer n>=2, let X={1,...,n} and let d:X×X→[0,infinity) be a finite genuine metric: symmetric, zero precisely on the diagonal, positive off diagonal, and satisfying the triangle inequality. Define MST(d) as the minimum sum of d-lengths of a spanning tree on X.

Independently for each unordered distinct pair, draw a marked indicator of probability p. An omniscient adversary sees d, the entire mask, and A_p, and supplies a symmetric matrix D with diagonal zero: unmarked pairs have D_uv=d(u,v), and marked pairs have arbitrary finite 0<=D_uv<=d(u,v). It acts before seeing A_p's private bits. Its choices may depend jointly on the entire mask; independence of the resulting observed entries is not assumed. A_p receives only D, with no queries to true distances or hidden mask labels. D need not be a metric.

For every such adversary, the algorithm must always output a spanning tree T on X and satisfy

    E_mask,private[sum_{uv in T} d(u,v)] <= C_p * max(1,log_2 n)^4 * MST(d).

On every observed input and every execution of the private bits, the total number of exact arithmetic/comparison operations and private bit operations must be at most

    n^(a_p * max(1,log_2 n)).

This is an arithmetic/comparison guarantee, independent of true and observed aspect ratios. It is not unit-bit arithmetic on arbitrary reals. Rational bit-complexity would require a separate precision-dependent bound. The algorithm may hardwire a rational q with 0<q<=1-p; constants may depend on q, never on n or aspect ratio. A bounded-bit sampling implementation and literal valid cases for p=0 and small n are part of the target. In particular p=0 admits an ordinary MST on D, and n=2 always has the single edge as its unique tree. Neither boundary case solves the remaining range.

A negative resolution must refute this entire algorithm-existence assertion, possibly under a precisely stated supported standard hypothesis. Failure of the supplied hierarchy or of a subsidiary lemma is insufficient.

## Nearest verified prior and proposed delta

Anand, Gupta, Jayaram, Lee and Vakilian, *Approximating Minimum Spanning Trees in Metrics under Semi-Random Corruptions*, arXiv:2610.40594v1, Theorems 1.2 and 1.3: an unrestricted-time logarithmic approximation for all fixed p<1, and a quasipolynomial logarithm-to-the-fourth approximation for p<=0.1. Its Section 6 already supplies hierarchical carving, admissibility/future-seed tests and leader extraction (Theorem 6.2; Definitions 6.4–6.6; Algorithms 2–3). Theorem 1.3's footnote says some arguments need sufficiently small p. The live record inspected 2026-11-03 still lists v1 only. See evidence/triage-literature.json for positions and search limits.

Source status: NEW-QUESTION, an author-independent computational refinement; this is not an attributed open conjecture. No equivalent full-range computational theorem was identified in the bounded current search. That is not a priority or open-status certificate.

Proposed delta: retain the quasipolynomial worst-execution bound and O_p(log^4 n) expectation throughout every fixed p<1. The supplied route replaces fixed low-noise thresholds with uniform uncorrupted-rectangle concentration and high quantiles, including overlapping future seeds. The inherited hierarchy and extraction are prior, not new contributions.

## Research admission and limits

Advance to a bounded first RESEARCH pass; no claim is proved or disproved at triage. Full computational/noise range has plausible algorithmic value, but substantive novelty, technical depth and STOC significance are unestablished. Merely changing thresholds or constants would fail the publication gate.

The decisive first test is an end-to-end adversarial reconstruction of the first-absorption/all-future-seed invariant: explicitly define all seed birth scales, old-object mergers and overlapping/identical comparisons; establish nonaccumulating outliers and separate seed-center/leftover counts; then close weighted hierarchy charging, every-execution runtime, observable aspect normalization, unconditional bad-mask expectation and finite-bit leader selection. A failure must identify the exact broken implication and whether repair remains possible. Small fixtures cannot substitute for this test.

This original permits only decreases for p<1. The previously exhausted arbitrary-corruption p<1/2 project is distinct and remains unresolved. Local comparison uses the supplied intake screening; the full external historical registry was not inspected. No research pass is consumed by this triage job, and no historical counter is reset. No manuscript/PDF or publication label is authorized by this decision.
