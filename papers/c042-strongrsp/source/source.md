# Frozen original: strongly polynomial near-linear single-source restricted shortest paths

Primary: Vikrant Ashvinkumar, A Deterministic Near-Linear Time Approximation Algorithm for Restricted Shortest Paths in Directed Graphs, arXiv:2610.18337v2,29October2026, Theorem1 and the paragraph immediately after Theorem2, printedp3. https://arxiv.org/abs/2610.18337v2

Original excerpt (short):

> While it remains open to give a strongly polynomial near-linear time algorithm (in fact, sub-mn time)

This paragraph concerns the SINGLE-SOURCE, ALL-TARGETS bicriteria RSP problem. The same paragraph says that the SINGLE-TARGET strongly polynomial near-linear variant already follows by standard techniques. ABK25 arXiv2410.17179v1, OpenProblems printedp42 and LemmaC.1 printedp46, records the same all-targets aspect-ratio issue and explains the single-target threshold reduction.

## Exact full assertion

There exist universal constants K,a,b>0 and an explicit uniform deterministic classical algorithm A with the following property. For EVERY finite directed adjacency-list graph with n>=2 labeled vertices, m edges, arbitrary finite NONNEGATIVE real edge lengths ell(e) and costs c(e), a source s, a budget C>0 and a rational accuracy0<epsilon<=1/2, A preprocesses in at most

    K (m+n) log(n+2)^a epsilon^(-b)

TOTAL elementary operations and space bounded by the same order. For every target t for which a path of cost<=C exists, the resulting all-target representation deterministically yields an s-to-t path P_t with

    c(P_t)<=(1+epsilon)C,
    ell(P_t)<=(1+epsilon)OPT_C(t),

where OPT_C(t) is the minimum true length among s-to-t paths of true cost<=C. The representation includes one finite length bound per represented target and compact witness data. A queried witness can be recovered in polynomial time in n,log(n+2),1/epsilon plus its output size, independent of both weight aspect ratios/precision; all recovered paths must satisfy the actual reported bounds. It is permissible to cycle-erase a nonnegative walk.

A target with no true C-feasible path may be reported unavailable, or may have a returned actual path satisfying the RELAXED cost bound; this does NOT assert exact budget feasibility. Reporting unavailable for any true C-feasible target is forbidden. Unreachable targets have no fabricated path. Zero lengths/costs, OPT=0, disconnected graphs, equal weights, all densities and arbitrary aspects are included. C=0 can be handled separately by deleting positive-cost edges and solving ordinary SSSP; it is not the research barrier.

The operation model is a real-arithmetic comparison RAM with basic exact +,-,*,/ on real input quantities and charged ordinary graph/control/index operations. There is no free logarithm/floor of an arbitrary input weight, digit extraction, exact exponential/Poisson oracle, unbounded advice, random choice, or free exponential policy synthesis. Any probability evaluation/rounding must have an explicit finite-cost implementation; rational intermediate encodings must have polynomial bit length in the input encoding and n,m,log(1/epsilon). The count is arithmetic operations, NOT a promise to read arbitrarily long rational encodings in constant bit time. Control indices have O(log(n+m+1/epsilon)) bits up to a fixed factor.

The displayed bound is independent of ALL numerical magnitudes, ratios and input precision; a log W factor, m^(1+o(1)) overhead beyond polylogs, a per-target n factor, a sub-mn-only improvement, an adaptive DP lemma or a special graph family does not prove this frozen assertion. The full original is the near-linear all-targets algorithm, not the weaker sub-mn question also mentioned by the source.

## Closest verified prior and scope boundary

Ashvinkumar26 Theorem1 gives deterministic bicriteria time Otilde(m log(nW)/epsilon^9), W the positive-length aspect ratio. Theorem2 states a fixed-k extension; neither statement removes W for ALL targets. ABK25 LemmaC.1 removes W for ONE target by locating a cost-feasible bottleneck edge and searching a length interval of ratio n. Running that reduction separately for n targets is insufficient. GK25 Theorem3 gives a known OFFLINE approximate ordinary-SSSP data structure for polynomially bounded weights, not an offline stochastic/Poisson DP theorem. Liu25/STOC26's online incremental theorem is m^(1+o(1))logW and likewise does not resolve the target.

Current exact/equivalent searches and current v2 record support open status; no complete equivalent was identified in the inspected sources. This is not a priority certificate. The target is mathematically distinct from exhausted c041 (ordinary unconstrained nonnegative SSSP with a fine logarithmic bound), and no old attempt budget is reset.

A proof must supply the ENTIRE correct all-input algorithm, its total operation count, compact witnesses and numerical/control implementation. Failure of a proposed offline-DP/quantization/MDP lemma is only a route diagnostic. Conditional hardness without an original hypothesis does not unconditionally disprove this algorithm-existence assertion. Routine/known/insufficiently valuable full consequences still fail the innovation gate.
