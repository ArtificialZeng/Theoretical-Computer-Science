# Research 4: complete selector-witness tests and a sparse two-port certificate

Job `c049-dualpreserve-research-960416a85f25`, authorized cumulative pass 4/4.
Research evidence only, not a manuscript, candidate or fresh referee report.
The immutable original in source.md remains unresolved. No novelty or venue
competitiveness is certified for the subsidiary facts below.

## Scope and the unresolved positive program

The full uniform polynomial-time original-edge mixed-two-fault construction
is unchanged. The standard greedy deletion and vertex-splitting equivalence
is in intake/minimal-critical-kernel.md. A sufficient, still UNPROVED bound is

    |E(G[U])|^2 <= C n(p+1)|U| log(n+2)^c

for every two-edge-fault edge-critical (G,P) and every nonempty U, retaining
the full ambient n. The orientation-pair formulation would suffice if the
pairs of items assigned to a common vertex admitted a bounded-multiplicity
charge to (demand, ambient vertex). Neither this charge nor DENSITY is proved.
The known three-connected-demand cover does not handle all witnesses of
connectivity one or two. No argument here fills that remaining general gap.

The proof/disproof split in this pass was: seek a globally paid cut charge,
while testing whether shared induced-matching selectors could contradict its
ambient density budget. Prior periodic-sharing experiments checked only
inherited witnesses. Their failure did not exclude alternative witnesses.
This pass completes that finite alternative-witness test and proves why a
fully shared family has a sparse certificate instead of a density obstruction.

## Exact all-fault classification on ten specified DAGs

The graph generator is the preserved build() in
research-2396269cbd5d-sharing-test.py, with no concatenation/hub edges.
For k=1,2 it has t=2*3^k+1 matchings and D=2^k edges per matching.
The new test uses five declared sharing choices at each k: no sharing,
fully shared left only, fully shared right only, fully shared both sides,
and both sides shared into floor(t/2) periodic groups. Demands are the t
diagonal source-target pairs. Every ambient vertex remains counted.

For EACH graph, all 1+m+binom(m,2) original edge-fault sets are enumerated.
For a fixed source and fault set in a DAG, the edges present on every route
to a vertex v are computed by intersecting, over reachable incoming arcs
u->v, the mandatory-edge set for u with that arc added. Induction in a
topological order proves this recurrence; unreachable vertices contribute
no predecessor. The source has an empty mandatory set. Thus an edge belongs
to a terminal's resulting set exactly when it is critical for that demand
under that fault set. Exhausting all faults/demands classifies every core
edge, including absence of ANY alternate witness in the declared finite graph.
No graph-isomorphism or demand symmetry reduction is used.

All ten cases completed: 242923 fault sets, 4519717 demand queries, and
1234 distinct reported critical-edge witnesses. Every saved witness was
independently checked by ordinary BFS in G-F and G-F-e. No timeout occurred.

| k | sharing | n | m | critical core / total core |
|---|---|---:|---:|---:|
| 1 | none | 42 | 56 | 14/14 |
| 1 | full left only | 36 | 56 | 14/14 |
| 1 | full right only | 36 | 56 | 14/14 |
| 1 | full both | 30 | 56 | 14/14 |
| 1 | both, 3 groups | 34 | 56 | 14/14 |
| 2 | none | 190 | 342 | 76/76 |
| 2 | full left only | 136 | 306 | 19/76 |
| 2 | full right only | 136 | 306 | 19/76 |
| 2 | full both | 82 | 270 | 0/76 |
| 2 | both, 9 groups | 130 | 302 | 42/76 |

In particular, the k=1 cases show concretely why a failed inherited witness
cannot establish noncriticality. The k=2 full-both result motivates the
following infinite family argument. The table alone establishes no
asymptotic bound, impossibility theorem, or original-scope disproof.

## A complete sparse certificate for the fully shared family

Here is a precise family theorem, not the original problem. All guarantees
in this section concern at most two EDGE faults. No general mixed-fault
or arbitrary-graph conclusion is inferred from this family theorem.

Let B=(U,W,E_B) be a simple D-regular bipartite graph with |U|=|W|=t,
D>=2 and t>=3. Partition its edges into t induced matchings M_i of size D,
ordered as (u_i,j,w_i,j), j=0,...,D-1. Assume that for each fixed position
j the lists (u_i,j)_i and (w_i,j)_i are permutations of U and W. The cyclic
progression-free bases used in the tests satisfy these assumptions: with
odd modulus t, a matching indexed by i contains

    u_i,j=(i-a_j)/2,  w_i,j=(i+a_j)/2  (mod t).

Division by 2 is invertible, so each fixed position is a permutation.
Progression-freeness makes each matching induced, as proved in the preserved
research-2 evidence and checked in the imported generator.

Orient the core U->W. Each private left selector is a directed chain with
attachments at its positions to u_i,j, and each private right chain receives
attachments from w_i,j. Identify ALL left positions j>=1 across matchings,
keeping the sources s_i at position 0 distinct; call the common positions
A_j. Identify ALL right positions j<=D-2, keeping the targets t_i at
position D-1 distinct; call the common positions B_j. Sources and targets,
core vertices and left/right common positions are mutually distinct.
There are n=4t+2(D-1) vertices. The graph has
m=3tD+2t+2D-4 edges after duplicate arcs are removed.

Write a=A_1 and b=B_(D-2). Every source has exactly the two outgoing arcs

    alpha_i=s_i->a,    gamma_i=s_i->u_i,0,

and every target exactly the two incoming arcs

    beta_j=b->t_j,     eta_j=w_j,D-1->t_j.

Also a has an arc to every U vertex, and every W vertex has an arc to b.
These arcs exist because of the fixed-position permutation assumption.
No arc goes from a right selector back to the core or to a left selector.

For ANY demand set P subset {s_i} x {t_j}, define

    R={u_i,0->w_j,D-1 in E_B : (s_i,t_j) in P}.

The two endpoint maps are bijections, so |R|<=p=|P|. Then there is an
input-edge two-edge-fault preserver H with

    |E(H)| <= 8t+p.

**Construction.** A regular bipartite graph is a union of D disjoint perfect
matchings. For completeness, for X subset U, regularity gives
D|X|<=D|N(X)|; Hall supplies a perfect matching. Removing it leaves a
(D-1)-regular graph, so induction gives the decomposition. Retain any two
of these matchings, all of R, all 4t source/target incident arcs displayed
above, the t arcs a->U and the t arcs W->b. Their total is at most 8t+p.
All other common selector vertices can remain isolated in H.

**Correctness.** Fix (s_i,t_j) and F of at most two original edge faults.
There are four cases for alpha_i and beta_j.

1. Both survive. A retained perfect matching gives t edge-disjoint a-to-b
   paths of length three, one through each of its core edges. Since t>=3,
   at least one avoids F. Concatenate alpha_i and beta_j.
2. Alpha_i fails and beta_j survives. If gamma_i also fails, G-F cannot
   leave its source. Otherwise, the two retained core edges out of u_i,0,
   followed by the arcs from their distinct W endpoints to b, give two
   edge-disjoint u_i,0-to-b paths. Only one further fault is available.
   One route survives, and gamma_i and beta_j complete it.
3. Beta_j fails and alpha_i survives. Symmetrically, if eta_j fails there
   is no route in G-F. Otherwise the two retained core edges into
   w_j,D-1 and their distinct a-to-U attachment arcs give two edge-disjoint
   a-to-w_j,D-1 paths. One survives the remaining fault.
4. Both fail. These consume the two faults. Any surviving source-target
   route in G must use gamma_i, exactly one core edge, and eta_j. Entering
   a right common selector cannot reach the target through the failed
   beta_j or return to the core. Thus reachability is equivalent to the
   existence of u_i,0->w_j,D-1 in B. If that edge exists it belongs to R
   and is retained in H; otherwise G-F is unreachable.

These cases prove the full edge-fault guarantee for P. Being a subgraph,
H cannot introduce reachability. The construction is deterministic polynomial
time by ordinary bipartite matching. This is a standard matching/root-cover
argument for this special graph family, with no substantive novelty claim.

## Exact critical-core classification when D>=3

In the same fully shared family, for D>=3 and arbitrary P as above, a core
edge is critical if and only if it belongs to R. Consequently the number
of originally critical core edges is at most p.

If e=u_i,0->w_j,D-1 belongs to R, fail alpha_i and beta_j. The case-4
argument gives a unique surviving path gamma_i,e,eta_j, so e is critical.
Conversely, if e is not in R, choose two perfect matchings from the D-factor
decomposition that avoid the matching containing e. The preceding complete
preserver H then omits e. Any purported criticality witness for e would
contradict preservation by this subgraph, so none exists.

For diagonal demands, R is empty: the first and last edges of an induced
matching have distinct endpoints and no cross core edge. Thus the fully
shared diagonal family has no critical core edges whenever D>=3. The
D=2 cases fall outside this classification and may retain all core edges,
exactly as in the finite table. Adding reachable cross demands restores
the corresponding core edges individually, costing one such demand per edge.
This rules out this particular fully shared construction as the hoped-for
cheap dense critical core. It does not rule out partial sharing, different
selectors, alternative dense cores, or the general DENSITY conjecture.

## Separate certificate validation

The certificate code constructs two perfect matchings by augmenting paths.
A separate C++ implementation propagates Boolean target-reachability masks
in reverse topological order in both G-F and H-F. It does not use the
mandatory-edge recurrence above. Every original fault set of size <=2 is
tested, including faults on omitted edges. Targets fit its explicitly
checked 64-bit domain (t=7 or 19); this is an exact bitset, not a hash.

Four certificate cases passed: k=1,2, each with the diagonal demands alone
and with the additional cross demands corresponding to every core edge.
Retained sizes were respectively 56,56,152,190; the original sizes were
56,56,270,270. Coverage: 76366 fault-set instances and 4215520 demand
comparisons. Every comparison agrees. An initial successful implementation
kept two unnecessary common-chain arcs in the k=2 certificates (sizes
154 and 192); the final predicate restricts root attachments to core vertices
and the same complete comparisons were rerun. This refinement does not
change the theorem, classification, or earlier all-fault results.

The two implementations are independent deterministic checks within this
same worker context, not a fresh referee/model or external peer review.
Their finite success supports the code and family proof; it proves no
unbounded general-graph claim by extrapolation.

## Literature, remaining gap and decision

Current primary pages for CCC2110.11613, thesis2605.20897 and HSW2510.02562
were rechecked. They still list v1; the thesis retains the old preserver
bound and HSW's object is SCC preservation. No equivalent full resolution
was identified in this bounded current search. See literature.md and web.json;
this is not an exhaustive priority or open-status certificate.

The new evidence eliminates a specific compression falsifier and supplies
a complete positive certificate for that family. It neither pays the global
orientation-pair charge nor proves or refutes the ambient DENSITY bound.
Arbitrary crossing active cuts, whose internal prefix/suffix routes run
outside a chosen dense core, remain the exact unresolved kernel.

Decision: PARK, candidate_kind=none, original_status=unresolved. The fourth
and final authorized research pass is used; there is no fifth pass under
this authorization. All earlier routes, counters, usage and verdicts remain.
No claim.json, manuscript/PDF, innovation acceptance or STOC label is created.

One possible future test, only under separate authorization: prove a global
charging theorem assigning optimized-orientation item pairs to (demand,
ambient vertex) with polylogarithmic multiplicity for the residual edges
having only connectivity-one/two witnesses, or produce a critical family
violating that budget. The family proof above only handles one common
left port and one common right port; general crossing cut interfaces have
not been reduced to that form. No such reduction is assumed.
