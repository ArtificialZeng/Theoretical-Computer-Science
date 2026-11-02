# Research pass 1: normalization and a fixed-flow transfer interface

Job: c026-aonflow-research-4dc78c591460. Original status: unresolved.
This is a research record, not a manuscript, accepted theorem packet, or novelty
certificate. The original question in source.md is unchanged.

## Verified dependencies and the actual CKS reduction

The supplied CKS2005 text, Section 2.1, Theorems 2.1 and 3.2, was reread.
For a fixed initial feasible path flow f of value F, gamma(H) counts only its
paths wholly inside H. Its endpoint weights are paired. Removing an edge set C
destroys at most |C| total path-flow, by the initial capacity constraints. CKS
charges cuts during recursion to this fixed flow; it does not permit an arbitrary
replacement flow to inherit the same charging history. Theorem 2.1 retains
Omega(F/(beta log F)) paired, product-flow-linked terminal weight. Theorem 3.1
explicitly states congestion-1 rounding for a *uniformly* alpha-flow-linked
terminal matching. Theorem 3.2 states the O(log^2 k) AON approximation.

CKS2013, Section 3.4, supplies the capacity-1 mechanism behind the grouping:
local flows use at most 1/2 on nonbridges and at most 1 on bridges; global flows
use at most 1/2; after cancelling cycles, an edge that is a bridge carries an
integer number of selected unit demands, hence a load strictly below 2 is at
most 1. Ordinary tree grouping with a full unit local load would not suffice.
Theorem 3.8 and Lemma 3.11 there are stated for their nice-instance setup.
Their arbitrary-weight grouping lemma is Lemma 3.3. The source does NOT state
the nonuniform rounding interface NR below verbatim.

Bansal--Jambulapati--Saranurak (BJS), arXiv:2602.15015v2, Theorem 3.1, gives,
for every nonnegative integral vertex weighting B, a polynomial-time deletion
of at most theta |B| Gamma(|B|) edges, leaving B restricted to each component
theta-flow-expanding. Here Gamma(t)=log(t) exp(O(sqrt(log log(t)))); harmless
constant modifications cover small t. Expansion means routability of *all*
B-respecting demands, not only the product demand. Its use below is a dependency
on the published theorem, not an independent audit of that theorem.

Live sources checked 2026-11-02 UTC:

- Official BJS theorem and still-explicit Conjecture 5.1:
  https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.22/LIPIcs.ICALP.2026.22.html
- Anand, arXiv:2610.17237v1, Section 5, Theorem 5.1, Appendix C Lemma C.1,
  and Appendix D: https://arxiv.org/html/2610.17237v1
  Theorem 5.1 assumes A(v)>=1 at every graph vertex. Its general rational
  extension uses A'=n A/|A|+1 and theta'=|A| theta/n, so it really gives
  log n log log n, not log k. We do not substitute a support-size bound for it.
- CKS2005: https://chekuri.cs.illinois.edu/papers/well-linked.pdf
- CKS2013: https://chekuri.cs.illinois.edu/papers/anflow-sicomp.pdf

Queries combining all-or-nothing, Bansal, 2026, nonuniform flow-linked rounding,
and the exact conjecture found no primary full resolution in this bounded
refresh. A lecture-note hit described a fixed-weight decomposition but only
claimed constant congestion; it was not used as a proof dependency. This is
limited search coverage, not a priority or continued-openness certificate.

## Established local lemma N: support-sensitive integer domination

Let A:V->Q_{≥0} have total mass a>0 and positive support size r. Set
q=r/a and B(v)=ceil(q A(v)) on the positive support, and B(v)=0 elsewhere.
Then B is integral, q A<=B, and

    r <= b:=sum_v B(v) <= 2r,       b/q <= 2a.

The weak upper bound is enough (the strict upper bound also holds). Apply
BJS Theorem 3.1 to B with theta=phi/q. Its cut bound is

    |C| <= (phi/q) b Gamma(b) <= 2 phi a Gamma(2r),

using a nondecreasing upper envelope for Gamma. In any remaining component,
if D respects A, then qD respects B. Route qD with congestion q/phi and scale
the routing by 1/q. Thus D is routable with congestion 1/phi.

This proves the stated interface from the BJS theorem with no minimum-positive-
mass or n dependence. Computing q and the ceilings takes polynomial rational
arithmetic. Every B(v)<=r+1 and b<=2r. The graph has not been expanded into
q copies, and a tiny denominator does not cause a large combinatorial input.
Zero-weight Steiner vertices remain zero. This is an elementary domination
reduction; by itself it is not an innovation-qualified publication result.

## Established local lemma P: preserve paired masses without recomputation

Normalize terminals by adding a separate unit-capacity leaf at each endpoint
occurrence. These leaves make the indexed pairs a matching; projecting away
the new leaf edges preserves congestion-1 feasibility and objective exactly.
Disconnected and coincident-endpoint cases are handled as in problem.md.

Take a rational feasible multicommodity flow of value F>0 with pair values
0<=x_i<=1, and a fixed simple-path decomposition. Give both endpoint leaves
of pair i weight A=x_i, and all other vertices weight zero. Then a=2F,
r<=2k. Lemma N supplies C with

    |C| <= 4 phi F Gamma(4k).

Choose phi <= 1/(8 Gamma(4k)). Keep only initial paths avoiding C and let
y_i be the retained amount for pair i (zero if none). The union bound against
the initial edge loads proves sum_i y_i >= F-|C| >= F/2. Both endpoints have
the same retained weight y_i. Inside each remaining component let A_y be these
retained endpoint weights. Since A_y<=A pointwise, every A_y-respecting demand
also respects A; hence A_y remains phi-flow-expanding there.

This avoids dynamically recomputing the maximum-throughput LP during the
decomposition. It uses the all-respecting-demand definition: pointwise shrinking
weights does NOT by itself give pointwise domination of normalized product
demands, whose denominator changes. This distinction is essential.

A polynomial-size edge-flow LP has a rational optimum of polynomial bit length.
Cancelling cycles and decomposing each commodity into paths uses polynomially
many rational operations and paths. Keeping/deleting entire paths and summing
their weights remains polynomial in bit complexity. The ceilings above do not
need a least common multiple or replication by an input denominator.

## The remaining kernel NR (not yet established in this record)

NR: There is an absolute c>0 and a polynomial-time procedure such that, for
every connected unit-capacity undirected H, every terminal matching M, paired
rational weights z_i in [0,1], and rational 0<phi<=1 for which the endpoint
weight A_z is phi-flow-expanding in H, the procedure selects and routes at
least c phi sum_i z_i original pairs with congestion 1. Whenever a demand
needs routing, its flow can be computed by a rational polynomial-size LP.

N + P + NR would give an LP-relative O(Gamma(4k)) AON algorithm on the entire
original class, and therefore the target ratio. This is a sufficient implication;
no equivalence or negative result about the original question is asserted.

### Positive progress toward NR: mass counting and the capacity interface

Set rho(v)=(phi/2) A_z(v), so each atom is at most 1/2. Apply arbitrary-weight
connected grouping (CKS2013 Lemma 3.3, W=1): disjoint owned sets S_j, connected
edge-disjoint cluster subgraphs H_j, 1<=rho(S_j)<2, uncovered mass <1. Omit
pairs with an endpoint unowned. As paired endpoint masses agree, the omitted
sum of *pair masses* rho_i is at most the uncovered endpoint mass, hence <1.
The retained pair mass is at least rho(V)/2-1.

Greedily select a pair whose two owned clusters are still unused and remove
every pair incident to those clusters. Each selection removes at most 4 total
rho_i mass, since each of its at most two clusters has endpoint mass <2.
Therefore it produces at least (rho(V)/2-1)/4 pairs, with at most one selected
endpoint per cluster unless both belong to the same selected pair. This counting
argument does not require a lower bound on z_i or uniform masses. If rho(V)
is bounded, one arbitrary connected pair supplies the required constant-scale
rounding. The greedy count is checked exactly by the accompanying script on
a bounded artificial cluster domain; the displayed argument is the general
proof of the counting inequality.

Suppose the CKS pseudocenter/tagging refinement can be carried out for these
nonuniform owned masses with constant cardinality retention. Separate locally
mated pairs from unmated ones and keep the larger class. For an unmated pair
(s_i,t_i), let a_i and b_i be its endpoint spreading distributions, each of
total 1, with sum_i(a_i(v)+b_i(v))<=rho(v). The induced reservoir demand is

    D({u,v})=sum_i [a_i(u)b_i(v)+a_i(v)b_i(u)]  (u!=v).

Its marginal at v is at most rho(v). Any diagonal reservoir term is joined
locally and costs no global edge. Since rho=(phi/2) A_z, global routing costs
at most 1/2 on each edge. Local pseudocenter routing costs at most 1/2 on
nonbridges and 1 on bridges. Concatenate to form one unit for each selected
original pair. Remove cycles commodity by commodity: the nonbridge load stays
<=1, and every bridge now carries an integer number of unit demands with
load<=3/2<2, hence <=1. This is the exact capacity accounting needed; a generic
constant-congestion rounding would not prove NR.

### Gap and adversarial next test

The complete CKS tagging/refinement argument has not been reconstructed for
nonuniform rho with explicit ownership at vertices shared by clusters. CKS2013
states that shared vertices can be handled by tagging there, but the instantiated
nonuniform statement, all tagging cases, and its polynomial construction are
not proved here. CKS2005 Theorem 3.1 alone states uniform alpha, so citing its
statement is insufficient for NR. No candidate is proposed on the strength of
an unverified extension. The remaining issue is positive algorithmic rounding,
not a counterexample search endpoint.

One next test: prove or falsify NR by a complete mass-owned version of CKS2013
Lemmas 3.11--3.14, including shared zero-mass connectors, bridges, highly skewed
paired masses, constant cardinality retention, and rational running time. If it
works, compose N/P/NR, then check whether this is already an implicit routine
consequence in the primary CKS/BJS literature or contains a substantive new
advance before proposing any resolution-paper. If it fails, save an exact
counterexample to NR or its named intermediate assertion only.
