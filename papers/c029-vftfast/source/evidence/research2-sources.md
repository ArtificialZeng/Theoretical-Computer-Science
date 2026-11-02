# Research pass 2: primary-source comparison

Checked 2026-11-02 UTC for job c029-vftfast-research-36ff17e1eeb1.

The live [arXiv source record](https://arxiv.org/abs/2610.33934) still lists
only v1 (24 October 2026). The [v1 introduction](https://arxiv.org/html/2610.33934v1)
still explicitly leaves the running-time improvement open. The manifest-
verified local text was used for Section 2.3, Algorithm 1, Claim 4.3,
Algorithm 2, Proposition 4.14, Proposition 5.6, Theorem 5.4 and Appendix B.
The final source-transfer obligation is identified in the positive-kernel
record and has not been converted into an unsupported full-resolution claim.

[Dinitz--Robelle](https://arxiv.org/abs/2002.10889), v2, Theorem 2 and its
unweighted size/runtime analysis provide a polynomial multiplicative spanner
with size O(t*f^(1-1/t)*n^(1+1/t)); this slightly nonoptimal polynomial t
factor is harmless here. It is a possible simpler dependency than the optimal
[Bodwin--Dinitz--Robelle](https://arxiv.org/abs/2007.08401), v3 constructor.
The unweighted DR2020 algorithm and its stated parameter dependence should
be used to remove any uncertainty about uniformity in the final pass.

[Fomin--Lokshtanov--Panolan--Saurabh](https://arxiv.org/html/1304.4626v4),
Theorem 1 / Section 3 and Section 2.5, supply the standard exterior-algebra
representative-set and Vandermonde uniform-matroid foundations. The proof
and DP here specialize established machinery; they are not claimed as a
new representative-set theorem. The new research direction is the parameter
switch combining f-dependent path compression with large-f multiplicative
spanners. Current bounded title/arXiv-number/polynomial-time searches did
not find that complete combined construction. This is not a novelty verdict
or an exhaustive priority claim; final checking is still required.

The method-hardness record states the direct conditional implication to
parameterized CLIQUE, and does not need an asserted unconditional lower
bound. The primary [Downey--Fellows W[1] paper](https://www.sciencedirect.com/science/article/pii/0304397594000973)
was located for context only; the new history lemma is proved directly.
No external contact or submission occurred. No bibliography workbook exists.
