# Precise problem and triage reading

Provenance: c032-dspdag-triage-c30f8ac75ef3, 2026-11-02. The immutable source.md is the authority; this document does not replace its quantifiers. Source integrity and all twelve supplied input hashes are checked in evidence/triage-validation.json.

## Statement, definitions and quantifiers

Let G=(V,E,w) be a directed acyclic weighted graph, n=|V|, m=|E|, with positive edge weights and k prescribed ordered terminal pairs (s_i,t_i). A feasible family consists of paths P_i from s_i to t_i, each of weight exactly dist_G(s_i,t_i), with disjointness as in AVW's vertex-disjoint shortest-path problem. Distances refer to the ORIGINAL graph, before deleting any vertex used by another path. An unreachable pair makes the instance infeasible. Terminal pairing cannot be permuted. Detection alone is requested.

The positive target is: there exist an integer k>=3, a real constant delta>0, and a uniform algorithm A for that fixed k, such that for EVERY source-model weighted DAG instance A decides feasibility in O(n^(k+1-delta)) total time. The constants may depend on the fixed k and delta, not on the instance. The source allows algebraic randomized algorithms; a claimed randomized solution must state its error guarantee and account for amplification. No algorithm or delta has been established here.

The alternative negative target is a precise implication from a stated standard hardness hypothesis ruling out the ABOVE existential improvement. In particular, a lower bound only for k=3, or only for sufficiently large k, is insufficient unless an additional reduction actually excludes every remaining fixed k>=3. Variable-k n^{o(k)} lower bounds and sparse-subclass lower bounds do not supply the required n^(k+1) barrier.

## Source convention and representation obligations

AVW v2 introduction (printed p.1) uses 'internally vertex-disjoint'; its abstract and Section 4.1, Lemma 17, enumerate vertex-disjoint paths and treat any shared vertex as an intersection. The working distinct-terminal interpretation therefore forbids all cross-path shared vertices, including use of another path's terminal. Any repeated/shared-terminal extension must explicitly follow the original convention; it is not silently excluded or assumed equivalent. Before certifying a recurrence, record endpoint/finished-path rules and any terminal normalization with its equivalence proof. An edge-disjoint recurrence is not sufficient.

AVW Section 2 (printed pp.7-8) requires positive weights, constructs source-shortest-path DAGs in O(m+n) per source by topological relaxation, and states Word-RAM O(log n) words for characteristic-two field operations. It does not fully specify the encoding/bit length of all positive edge weights. This is an explicit source-model caveat, not permission to impose bounded weights, integrality, uniqueness, or a distances-given promise. A research claim must state exact weight arithmetic, charge preprocessing and comparisons/additions, and explain its compatibility with the source model; arbitrary precision is not free. Thorup's undirected preprocessing is irrelevant to preprocessing a DAG.

For each i, the tight-edge graph retains (u,v) when d_i(v)=d_i(u)+w(u,v), where d_i(v)=dist_G(s_i,v); it is a sub-DAG and encodes the original shortest paths. Computing these k graphs costs O(k(m+n)) source-model operations. Every later transition must use the appropriate graph for its labelled coordinate.

## Nearest results and proposed substantive delta

AVW v2 introduction, printed p.2, attributes the O(m n^(k-1)) baseline to Fortune-Hopcroft-Wyllie 1980, with shortest-path adaptation noted in Berczi-Kobayashi 2017 Proposition 10. AVW Theorem 2 improves ONLY k=2 to linear detection. Section 5 (printed pp.28-31) gives a related ordered-frontier construction for EDGE-disjoint paths, allowing equal coordinates and simultaneous moves; copying it verbatim would change the problem. AVW Open Problem 3, Section 7, printed p.41, explicitly asks the full target above. Its surrounding discussion identifies matrix multiplication and stronger-than-clique reductions as routes, not solutions.

Choudhary-Kumar-Saggi, ITCS 2026 Theorem 1.1, is a two-pair result on more general directed graphs. Chitnis-Thomas-Wirth arXiv:2408.03933v1 Theorem 5/Corollary 6 concern approximation and variable-parameter ETH hardness, not a matching exponent for each fixed k. Planar FPT results do not cover arbitrary DAGs. See evidence/literature-triage.md for current checks and limitations.

A complete dense-instance polynomial exponent saving for even one fixed k>=3 would break the longstanding frontier-state transition bound and settle the exact source question. This is a plausible substantial algorithms payoff, not a present claim of novelty or STOC competitiveness. The proposed delta is an exact, globally charged batching of labelled frontier transitions; merely rewriting the baseline or invoking FMM without controlling dependencies supplies no advance.

## One decisive first research test

For k=3, write the vertex-disjoint ordered-frontier recurrence on the three labelled tight-edge DAGs, including cross-coordinate collisions, other terminals, and completed paths. Formulate a specific batched Boolean/matrix transition with an explicit topological block dependency invariant. Compare its complete transition/reachability table to direct enumeration of feasible shortest-path triples on stated tiny weighted DAG cases, then prove and sum the number and dimensions of all products and preprocessing. A useful result is either a correct O(n^(4-delta)) schedule for all instances, or an explicit violated batching/dependency invariant guiding repair. A finite match is only validation; a failed batching lemma does not refute the original existential question. No optional proof search or finite experiment was run during triage.


## Research pass 1 proposed positive resolution (not independently audited)

Job c032-dspdag-research-2c4a21894757 constructs a minimum-frontier divide-and-conquer schedule with three disjoint output classes per moved coordinate. The proposed all-instance k=3 algorithm costs O(m+n+n^(1+log_2 7)) source-model word operations, or conservatively O(n^3.9) with ordinary bit arithmetic for its O(log n)-bit matrix operands, plus the source's original-weight preprocessing. Thus k=3, delta=1/10 is the proposed answer to the unchanged existential original. Full correctness, terminal normalization, source-model and globally charged cost proofs are in evidence/research-1/proof.md. No width, distinct-distance, unweighted or sparse-instance restriction is imposed. Repeated endpoints are handled explicitly under both strict and usual internally-disjoint conventions. This is a proposer claim awaiting fresh mathematical/novelty/value review, not accepted mathematics or a venue assessment.
