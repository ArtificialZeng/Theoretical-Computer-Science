# Primary-source comparison for the proposed complete algorithm

Job c029-vftfast-research-9df2f29ab673; checked 2026-11-02 UTC.

1. [Parter--Popova--Tzalik, New Fault-Tolerant (alpha,beta)-Spanners](https://arxiv.org/abs/2610.33934).
   The live record lists v1, submitted 24 October 2026, and no later version.
   The live [v1 text](https://arxiv.org/html/2610.33934v1), Introduction,
   retains the running-time challenge. The manifest-verified local PDF/text
   contains all packing dependencies used in Section 4 of the proof record.
   This source supplies the size/stretch baseline; the proposal improves
   construction time. Its polynomial Baswana--Sen alternative has a different
   fault exponent.

2. [Dinitz--Robelle, Efficient and Simple Algorithms for Fault Tolerant Spanners](https://arxiv.org/abs/2002.10889),
   v2 (24 May 2020), Theorems 2, 5, 8, 9, local printed pp.3,7--9.
   These give the deterministic multiplicative constructor with the explicit
   polynomial parameter dependence used in the large-fault and bounded-k
   regimes. The proposal does not improve their multiplicative theorem.
   Their gap-cut test is the prior for the protected-path test proved here.

3. [Fomin--Lokshtanov--Panolan--Saurabh, Efficient Computation of Representative Sets with Applications in Parameterized and Exact Algorithms](https://arxiv.org/abs/1304.4626),
   v4 (22 February 2016); published as *Efficient Computation of Representative
   Families with Applications in Parameterized and Exact Algorithms*, JACM
   63(4), article 29 (2016), [DOI 10.1145/2886094](https://doi.org/10.1145/2886094).
   The live [v4 text](https://arxiv.org/html/1304.4626v4), Sections 2.5 and 3,
   supplies the standard Vandermonde/exterior basis comparison. The DP here
   is proved directly; no new general representative-family theorem is claimed.

4. [Bodwin--Dinitz--Robelle, Optimal Vertex Fault-Tolerant Spanners in Polynomial Time](https://arxiv.org/abs/2007.08401),
   v3, is the sharper multiplicative comparison preserved in intake. Its
   algorithm is unnecessary: DR's extra polynomial factor in stretch fits
   the frozen polylogarithmic size slack.

Bounded searches in this pass included the source title and arXiv number
with polynomial/running-time terms, and fault-tolerant spanners combined with
representative families/sets, including arxiv.org-restricted searches. They
returned the source and standard constituent literature; no equivalent full
parameter-switch construction was identified. Nonprimary search results were
not used as mathematical dependencies. This is a bounded comparison, not an
exhaustive priority certificate.

The proposed delta is a uniform deterministic polynomial construction at the
full PPT tradeoff. Representatives alone have an f-dependent exponent and
DR alone has the wrong stretch/size combination in the small-fault regime.
Their complementary regimes are the proposed new step. The proof also checks
PPT's counting argument for the actual incomplete representative-path scan;
it does not claim containment in a full greedy output.

A fresh review must decide correctness, novelty, theoretical significance
and the separate STOC criteria. Whether this compiler is sufficiently
nonroutine and consequential is not established merely by open-problem
wording or finite tests. No acceptance or readiness label is asserted.
