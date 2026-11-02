# Current primary-source and adverse-value comparison

Job c031-detlis-research-bf90b0105355; inspected 2026-11-02 UTC. This is a
researcher's bounded comparison, not a fresh referee verdict, priority
certificate, or STOC assessment. The new proof is self-contained and does
not cite supervisor confidence or historical acceptance as evidence.

**Exact 2D baseline.** [Karthik C. S. and Saladi Rahul, arXiv:2404.04795v2](https://arxiv.org/abs/2404.04795v2),
revised 2025-12-01, and [ITCS 2026, article 87](https://doi.org/10.4230/LIPIcs.ITCS.2026.87).
The current primary record and preserved full primary were rechecked. Theorem
1 is randomized uncolored 2D reporting with square-root overhead. Theorem 5
is the deterministic short-LIS primitive; Section 7 asks for deterministic
subquadratic time. Our proposed two-thirds exponent is weaker quantitatively
than the randomized bound but deterministic for the whole reporting model.
The short-chain and endpoint-stitching framework are prior work.

**Strong 1D results must not be overlooked.** [Gawrychowski, Gorbachev and
Kociumaka, Core-Sparse Monge Matrix Multiplication, ESA 2025, Theorem 1.3
and Section 5](https://drops.dagstuhl.de/storage/00lipics/lipics-vol351-esa2025/html/LIPIcs.ESA.2025.74/LIPIcs.ESA.2025.74.html)
were inspected online, including the stated query definition: two indices
specify a subarray. Its deterministic near-linear preprocessing and
output-linear reporting do not, as stated, include an independent value
interval restricting every internal chain point. Likewise [Korogi,
arXiv:2610.20983v1](https://arxiv.org/abs/2610.20983v1), submitted 2026-10-14,
defines weighted index-interval queries (Introduction and Theorem 1.1,
also checked in the preserved primary). An optimum-weight value query is
not an internal value-coordinate restriction. No claim to improve their
1D results is made. A new 2D composability consequence of their methods
remains a legitimate adverse review question.

**Relative sampling is established, with the same generic rate.**
[Har-Peled and Sharir, Relative (p,epsilon)-Approximations in Geometry,
arXiv:0909.0717v2](https://arxiv.org/abs/0909.0717), revised 2010-01-25,
published DCG 2011. The live primary record and the preserved complete
primary PDF/text were used. Printed pp. 7--11: Lemma 2.8 and Corollary 2.10
give composition; Theorem 2.11 gives the inverse-p relative sample scale;
Lemma 2.15 gives a deterministic construction with its dimension-dependent
cost. For dimension two and inverse-polylogarithmic accuracy, the displayed
cost has n p^-2 polylogarithmic form, precisely the polynomial scale of our
net construction. Our ordered canonical family has VC-dimension at most two,
proved in the dossier; this fact and generic relative sampling are not
claimed as new. The important missing interface is an efficiently evaluable
subsystem on selected points: its canonical paths depend on unselected
original points. Lemma 2.15 alone does not supply that path computation or
its charged total cost. Reconstructing generic sampling without resolving
that interface would not be a substantive contribution.

**Merge/reduce is established.** [Bagchi, Chaudhary, Eppstein and Goodrich,
Deterministic Sampling and Range Counting in Geometric Data Streams,
SCG 2004, Section 2](https://courses.cs.duke.edu/spring07/cps296.2/papers/deterministic_sampling_geom_data_streams.pdf).
The preserved full primary's subsystem-oracle definition, Lemma 2.2,
Observations 2.3--2.4 and weighted versions were re-read. Their oracle lists
the restrictions on Y in time O(|Y|^(d+1)); the bound depends only on Y.
Our replacement costs O(|I| |Y| log^2 n+|Y|^2), where I is the ORIGINAL
interval. It is not a subset-only oracle satisfying their hypothesis for
free. Our global ledger uses disjoint original backgrounds at each merge
level. This is an explicit additional algorithmic step, whose routine versus
substantive nature must be assessed by the fresh referee.

**Path hitting and tree aggregation are established tools.** [Tao, Sheng
and Pei, On k-skip shortest paths, SIGMOD 2011](https://www.cse.cuhk.edu.hk/~taoyf/paper/sigmod11-skip.pdf),
Sections 4.1--4.2, Theorem 1 and Lemmas 1--2 were re-read in the preserved
primary. They already connect consistent path families and small covers;
their actual construction uses a random permutation and its runtime
analysis assumes constant degree. We prove our particular ordered-path
consistency directly, without importing unrestricted graph tie assumptions.
[Alon, Chechik and Cohen, ICALP 2019](https://doi.org/10.4230/LIPIcs.ICALP.2019.12),
Section 1.3/Figure 1 and Lemma 6, were also re-read. Their generic greedy
bound takes an explicit family of paths; efficient critical-family
construction is separate. Our algorithm enumerates compressed traces at
local sample merges and sums signed target weights on selected-source
trees. Neither descendant sums nor conditional expectations are new in
isolation. Listing all global endpoint paths would lose our bound.

**Subsequent graph derandomization was checked as a lead.** The current
primary record of [Karthik and Parter, Deterministic Replacement Path
Covering, arXiv:2008.05421v3](https://arxiv.org/abs/2008.05421v3), and the
publisher primary abstract/model of [Bilo et al., Simpler and Improved
Replacement Path Coverings, ICALP 2026](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.35/LIPIcs.ICALP.2026.35.html)
were opened. Their stated object is a family of subgraphs retaining a
shortest path while avoiding a bounded fault set; the 2026 work explicitly
uses conditional expectations. These inspected statements do not directly
provide the implicit canonical longest-chain oracle needed here. Their
full proofs were not audited in this pass, and no claim to supersede those
graph results or prove a lower bound on their applicability is made.

## Proposed substantive contribution and remaining value uncertainty

The new scientific artifact proves a concrete full-model algorithm, not a
new generic approximation theorem: compute full-background source trees
only on disjoint original intervals, retain their selected traces, evaluate
all rounded conditional scores by signed descendant sums, and charge every
word operation. Relative compression reduces the sample to O-tilde(N/t),
forest aggregation gives a k^3 per-merge charge, and localization gives
O-tilde(N k^2) total construction. Balancing with the prior short-LIS routine
yields the proposed deterministic two-thirds exponent and additive output.
This is one strengthened version of the same original research target.

The source-model gap, the background-sensitive oracle, and the complete
charged reporting bound provide a concrete case for substantive review.
The stronger exponent alone is not a novelty or STOC-value argument.
Known ingredients, enormous constants, the remaining randomized exponent
gap, possible equivalent implicit-blocker machinery, and limited breadth
are adverse considerations. The referee must reject if the integration is
known, routine or value-insufficient. No new acceptance or submission-ready
label is asserted; historical reviews cover their actual earlier snapshot.

Searches included the exact paper title with deterministic/derandomization,
range LIS deterministic 2026, canonical paths subsystem oracle, deterministic
path epsilon-net merge, implicit blocker sets, and replacement path covering.
Search results were leads; mathematical comparisons above use identified
primary records/text. No equivalent complete deterministic 2D theorem was
identified in this bounded search. Unsearched terminology and unreviewed
full implications remain; this negative search does not certify priority.
