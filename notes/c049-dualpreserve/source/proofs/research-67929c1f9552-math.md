# Research 1: shared flows, return-edge isolation, and the remaining global count

Job `c049-dualpreserve-research-67929c1f9552`, 2026-11-03 UTC.
The immutable original is unresolved. These are research records, not a
publication candidate, novelty certification, or fresh referee assessment.

## 1. What was actually tested

The assigned coordinate-sharing potential was implemented with exact integer
successive shortest residual augmentations (Bellman--Ford), at most three
augmentations per capped flow. Every accepted best response has its exact cost
decrease checked against the independently recomputed potential decrease.
Forty separately generated four-vertex instances also compare maximum value and
minimum cost against exhaustive enumeration of ALL edge supports. This checks
the flow implementation rather than inferring it from the potential formula.

The flow/cut suite covers all 4096 labelled loop-free four-vertex digraphs for
the SINGLE demand pattern {(0,2),(1,3)}; 48 seeded pruned critical graphs with
5--8 vertices; five declared instances of the published 2022 chain family;
and three small 2020 lifts. The latter use tree bases, NOT asymptotic
Theorem 26 extremizers. Outputs and exact coverage are in flow-results.json.
Unchecked large-graph critical-edge counts are null, not zero. No old
exhaustive checker was rerun to reconstruct history.

The exchange identity in the handoff is correct under BOTH unilateral swaps'
unit-capacity feasibility: on an edge of A, the summed cost change is -2,
and likewise on an edge of B. Thus Delta_i+Delta_j=-2(|A|+|B|).
This does not bound the number of blocked exchanges or off-flow edges.

## 2. A precise obstruction to support-only charging

In the 2020 Section 5 lift, EACH demand has a UNIQUE maximum two-flow,
independently of positive edge prices or other commodities. The strand using
the source's right-chain edge must traverse that whole chain and enter t on
the right terminal edge. The second strand must therefore use the left terminal
edge. Since no edge returns from the central/right region to a left chain,
that strand must traverse the whole direct left chain. Both are forced.
Other demand sources have indegree zero and other targets have outdegree zero,
so neither supplies an alternative continuation.

Consequently ALL central edges have zero load in every selected capped flow.
Nevertheless the already verified published interior-shift witnesses force
Omega(ell*b) central edges on the asymptotic unique-path base family. This is
not a new lower bound: it identifies exactly why the NEW sharing potential is
blind to the hard part of a known construction. Any rule asserting that each
critical edge is in selected-flow support, or is a capacity blocker ON such
support, is false. A rule explicitly accounting for off-flow cuts is untouched.

In the 2022 family with r left/right chains of L vertices, p=r^2 and
n=2rL. Each demand similarly has its unique maximum two-flow using its first
and last crossings. The union has 2r(L-1)+2r^2 edges, while the (L-2)r^2
interior crossings are critical and outside the union. This was checked with
NEW flow selection, not by replaying the old lower-bound verification.

## 3. A different rule covering some off-flow edges

For a critical edge e, a witness is a demand i=(s_i,t_i) and a set A with
e in delta_G^+(A), |delta_G^+(A)|<=3, s_i in A, t_i outside A, and the
internal prefix/suffix routes specified in intake/minimal-critical-kernel.md.
Define the reverse demand set

    R(A) = {j : s_j outside A and t_j in A},
    beta(e) = min_witness_(A,i) |R(A)|.

Only critical edges receive beta; this minimum is over every valid witness,
not an arbitrary cut chosen by a heuristic. Removing originally unreachable
or reflexive demands first is permitted but not needed for the lemma below.

**Return-edge isolation lemma (proved here as a reduction).** Let T be a
subset of demand indices containing i and disjoint from R(A). Form the simple
n-vertex digraph G_T by adding the edges t_j->s_j for j in T (deduplicate
existing edges). Every two-edge-fault SCC preserver K of G_T contains e.

Proof. Fail D=delta_G^+(A) minus {e}, so |D|<=2. The internal routes and e
give an s_i-to-t_i route in G-D. The added edge t_i->s_i makes these endpoints
strongly connected in G_T-D. No added edge leaves A, by T disjoint from R(A).
Therefore a route from s_i to t_i in K-D has to leave A using e, its sole
surviving outgoing edge. SCC preservation supplies that route. Hence e is
in K and is an original edge. This proof does not assume min-cut VALUE
preservation implies fault preservation. Parallel-edge gadgets, extra p
vertices, and output shortcuts are unnecessary. QED.

**Consequence using current primary literature.** For every integer b>=0,
the set L_b={critical e: beta(e)<=b} has size

    |L_b| = O(n(b+1) log(n+2)^(7/2)).

Use Hoppenworth--Saranurak--Wang, FOCS 2025, arXiv2510.02562v1,
Theorem 1.1: a fixed-two-fault SCC preserver has O(n log(n)^(5/2))
edges and polynomial construction time. For b>=1, include each demand
independently with probability 1/(b+1). For a fixed edge's minimizing witness,
the isolation event has probability at least 1/[4(b+1)]. With
ceil(56(b+1) ln(n+2)) independent samples, failure probability for that edge
is at most (n+2)^(-14); union bound over m<=n^2 edges gives at most
(n+2)^(-12). For b=0 one may add all return edges in a single sample.
The union of the SCC preservers therefore contains every L_b edge on a
positive-probability event and has the displayed size. Projection retains only
original edges. This is a partial coverage/edge-count lemma, not a full
preserver: the other critical edges are still necessary. Its novelty has
NOT been established; do not propose this elementary application as a paper.
The existential log exponent could be improved using the same source's
smaller existential bound, but no such optimization is needed here.

The separate return-edge checker verifies the lemma's decisive reachability
implication for every cut and every qualifying sampled subset in 40 seeded
small critical graphs. It does not implement the HSW construction or certify
a new asymptotic high-beta bound.

## 4. A tempting global charging tradeoff is false

The stronger repair |{e: beta(e)>b}|=O(np/(b+1)) for ALL b, even with fixed
polylog factors, would balance the preceding lemma at b approximately sqrt(p).
It is FALSE on the 2022 chain family.

Indeed, let e be any crossing at layer k, and A any outgoing cut of size<=3
containing e. Put X={i: left(i,k) in A} and
Y={j: right(j,k) outside A}. Then x=|X|, y=|Y| are positive and xy<=3,
since all X times Y crossings leave A. At most 3-xy other outgoing cut
edges remain. Among the r-x left chains whose layer-k node is outside A,
at most 3-xy can have their source inside A: each such chain supplies a
distinct additional outgoing chain edge before layer k. Thus at least
r-x-(3-xy) sources are outside A. Similarly at least r-y-(3-xy) targets
are inside A. Every such source-target combination is a demand. Inspection
of positive integers x,y with xy<=3 gives, for r>=3,

    |R(A)| >= (r-3)^2.

This lower bound does not even need the internal-route witness conditions.
For r>=12 all Lr^2 crossing edges have beta(e)>p/2. At b=floor(p/2),
np/(b+1)=O(n), while Lr^2=nr/2. Taking L=3 and r growing gives a
polynomial excess over every fixed polylog. The old lower construction is
known; the consequence for this newly specified charging rule is the research
test. Complete cut enumeration in three small chain instances independently
checks the beta definition and its numerical behavior.

This does NOT refute the weaker bound needed only at b=ceil(sqrt(p)), where
the same chain family is consistent with, and of the target order of,
O(n sqrt(p)). It also does not refute source.md.

## 5. Exact remaining kernel and proposed next test

Let b=ceil(sqrt(p)) and B be the subgraph consisting of critical edges with
beta(e)>b. The return-edge lemma already pays the desired tilde-O(n sqrt(p))
budget for every other edge. The missing assertion is a global bound on B.
There is no proof from the cut-excess identity, flow potential, or small fits.

One concrete sufficient next test: determine whether B has undirected
degeneracy O(sqrt(p)), counting directed edges with multiplicity at most two
per undirected adjacency. Equivalently up to constants, does a core of B of
minimum total incident degree d force p=Omega(d^2)? Prove this from crossing
active three-cuts, or construct an asymptotic critical family with
p=o(d^2). This is a stronger, explicitly UNPROVED sufficient lemma, not an
equivalent reformulation or weakened replacement of the original. The
published chain has d of order sqrt(p); the small tree-base 2020 lifts have bounded core degree. The asymptotic
2020 unique-path bases still require a real degeneracy assessment: their
published total-edge bound is not a certificate for every induced core.
Passing finite tests is not proof. A counterexample
would kill this method without resolving the original.

Research may continue for this specific test within the two remaining passes.
No claim.json, manuscript/PDF, acceptance, or STOC quality label is justified.
