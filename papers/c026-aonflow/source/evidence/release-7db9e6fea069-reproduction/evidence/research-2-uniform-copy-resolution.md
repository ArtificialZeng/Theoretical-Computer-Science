# Full-target proof proposal: uniform copies and protected admission

Job: c026-aonflow-research-02dec8252283. Research pass 2. This is a proof
dossier for fresh review, not an acceptance record or a manuscript. The immutable
original is source.md; its full interpretation is problem.md. No graph-class,
congestion, admission, or parameter restriction is imposed below.

## Statement

There is one randomized polynomial-time algorithm for the original undirected,
unit-edge-capacity all-or-nothing flow problem which always outputs a feasible
subset of distinct original pairs with congestion at most 1, and, with probability
at least 3/4, outputs at least

    OPT / [C log(k+2) exp(C sqrt(log log(k+4)))]

pairs, for an absolute constant C. It uses a polynomial number of random bits
and rational operations on numbers of polynomial bit length. Repetition and
retaining the largest verified feasible answer amplifies its success probability.
Thus its approximation ratio is log^(1+o(1)) k for the full immutable target.

The proposed new step is a reduction from fixed, integral-terminal flow-expander
decomposition to original unit admission. It retains a fixed feasible family of
uniform path copies, and keeps a unit bottleneck for each original endpoint
occurrence, preventing duplicate-copy admission. This avoids repeatedly changing
the maximum-throughput weights. The decomposition and the exact-congestion
rounding are prior results, not new theorems claimed here.

## Precisely used published results

1. Bansal--Jambulapati--Saranurak, arXiv:2602.15015v2, Theorem 3.1,
   printed p.4, also official ICALP 2026 article 22, Theorem 3.1: for integral
   A>=0, compute C with |C|<=phi |A| Gamma(|A|) and with A restricted to
   every component of G-C phi-flow-expanding in its induced graph. Here
   Gamma(t)=O(log(t+2) exp(O(sqrt(log log(t+4))))) can be taken nondecreasing.
   Flow expansion means routability of EVERY A-respecting demand at congestion
   1/phi. Zero-weight vertices are permitted. This is the theorem as stated,
   including its polynomial-time guarantee; its internal proof is not re-proved.
2. Chekuri--Khanna--Shepherd, STOC 2005, *Multicommodity flow, well-linked
   terminals, and routing problems*, Theorem 3.1, printed p.5: for 0<alpha<=1,
   if the product demand alpha/|X| on unordered terminal pairs is routable
   at congestion 1, any matching M on X has a polynomial-time congestion-1
   unit routing for at least c0 alpha |M| selected pairs, for an absolute c0>0.
   This is the edge-capacitated theorem; no integral-path conclusion is used.
   Its footnote requires strengthened clustering. The corrected support is
   CKS, *The All-or-Nothing Multicommodity Flow Problem*, SIAM J. Comput.
   42(4) (2013), 1467--1493, DOI 10.1137/100796820, Section 3.4,
   Lemmas 3.9--3.14. The transfer of that proof is checked below; journal
   Theorem 3.8's formal nice-instance premise is not silently discarded.

CKS2005 Lemma 1.1 motivates uniformization, but the construction, independence,
probability, bounded sampling and admission bookkeeping needed here are supplied
explicitly rather than inferred from its proof sketch.

## 1. Endpoint normalization and the small-parameter branch

Admit coincident-endpoint pairs immediately with zero edge use and remove them.
Let k now denote the remaining number (using the original k in the final bound
only weakens the guarantee). Give every endpoint occurrence a separate new leaf
joined to its original vertex by a unit-capacity edge. Move that occurrence's
terminal to the leaf. Call these the OLD terminal leaves and their OLD edges.
Even indexed duplicate pairs now form a matching on distinct leaves.

This preserves the optimum exactly: extend every original unit flow along its
two occurrence edges, each used by only that original commodity; conversely,
project any normalized feasible flow after deleting its two pendant segments.
Cycle removal permits simple paths, so projection does not increase edge loads.

Let N>=16 be an integer at least the explicit input encoding length and the
numbers of vertices, edges and pairs AFTER this normalization. N can be chosen
within a constant factor of the original encoding length. Set b=ceil(log2 N).
If k<=b, enumerate all 2^k<=2N subsets and use a compact rational multicommodity
flow LP to test whether each subset's unit demands are feasible. Return an
optimum subset. This is polynomial in the explicit input length, with an
exponent independent of k. No assumption relating n and k is made.

Otherwise k>b. Solve the fractional admission LP on the normalized instance:
maximize F=sum x_i subject to 0<=x_i<=1 and feasible splittable flows of value x_i.
It has a polynomial-size rational edge formulation. If there is no connected
pair, return the empty set. Otherwise F>=1, since any one connected pair is
feasible. Also F<=k. Fix a polynomial-size rational simple-path decomposition
of the optimum flow, cancelling cycles first. The LP optimum upper-bounds OPT.

## 2. Uniform path copies, in strict polynomial time

Put T=64 ceil(log2(2N)) and epsilon=1/(4T). For each pair i, split its fixed
path flow into d_i=ceil(T x_i) pieces of total mass at most 1/T each (no pieces
when x_i=0). A piece may contain fractions of several original paths. This is
done by processing the path list sequentially, ending a piece at mass 1/T.
Consequently the total number of positive path fragments is at most the original
number of paths plus the number D=sum d_i of pieces, and

    D <= TF+k <= k(T+1).

For each piece independently, select ONE path fragment P with probability
T times its mass; select nothing with the remaining probability. Let K be the
number of selections and Z_e the number of selected paths using old edge e
(including all normalized occurrence edges). Under this ideal rational
sampling law,

    E[K]=TF,                  E[Z_e]<=T.

The indicators contributing to each Z_e are independent across pieces. Standard
Chernoff bounds for independent Bernoulli variables give

    Pr[K<TF/2] <= exp(-TF/8) <= exp(-T/8),
    Pr[Z_e>4T] <= (e^3/4^4)^T < (1/8)^T.

The second inequality follows by exponential Markov with parameter log 4 and
mean at most T; bounding the larger event Z_e>=4T is sufficient. There are at
most N old edges. Since N>=16 and T>=320, the sum of these failure bounds is
less than 1/32. For example exp(-T/8)<(8/9)^T, (8/9)^320<1/64, and
N 8^-T<1/64. These conservative rational bounds are checked in the code.

To avoid an unbounded-time rational rejection sampler, let Q be the sum, over
all pieces, of their numbers of outcomes, counting a null outcome. Set
B=ceil(log2(64Q)). For each piece use B unbiased bits, interpreted as U in
{0,...,2^B-1}, and locate U/2^B in its rational cumulative-probability intervals.
Each interval's probability differs from the ideal by at most 2^-B; hence the
total variation distance of the joint law from the independent ideal law is
at most Q 2^-B<=1/64 (the sum-of-marginal-TV bound). Sampling and interval
comparisons take strict polynomial time and polynomially many random bits.
Thus the good event

    K>=TF/2 and Z_e<=4T for EVERY old edge e

has probability greater than 3/4 under the implemented sampler. Check it
explicitly using exact arithmetic. If it fails, output an arbitrary connected
original pair. This branch is feasible; no approximation claim is made for it.

On the good event, attach a fresh source and sink copy leaf for each selected
piece beyond the OLD leaves of its original pair. Route epsilon on its selected
old path, extended through the two new edges. The new edges each carry epsilon;
every old edge carries epsilon Z_e<=1. These K path-copy flows are jointly
feasible. Importantly, the OLD occurrence edges have not been removed, replaced
by large capacities or bypassed. Every copy of original pair i has to cross
the SAME old source occurrence edge of i.

## 3. One decomposition with fixed integral endpoint weights

In the resulting graph G*, give every one of the 2K new copy terminals weight
1 and every other vertex weight 0. This integral weighting A has total 2K.
Use a computable nondecreasing integer upper bound Gamma on the overhead in
BJS Theorem 3.1, with its absolute constants fixed once and for all. For
example, put d(t)=ceil(log2(t+4)), h(t)=ceil(sqrt(ceil(log2(d(t)+2)))),
and take Gamma(t)=C0 d(t) 2^(C1 h(t)), for sufficiently large fixed positive
integers C0,C1. Integer bit lengths and integer square roots compute these
quantities exactly, without comparing transcendental numbers.
This choice has polynomial bit complexity and log^(1+o(1)) growth.

Set phi=epsilon/[8 Gamma(2K)] and apply that theorem ONCE. Its cut set satisfies

    |C| <= phi (2K) Gamma(2K) = epsilon K/4.

Call a selected copy pair hit if its fixed prepared path uses at least one edge
of C. The union bound, with the FEASIBLE prepared epsilon path flows, gives

    epsilon * (#hit copy pairs)
      <= sum_{e in C} (prepared flow load on e) <= |C|.

At least 3K/4 copy pairs are unhit. Each has both endpoints in one remaining
component and has its entire prepared path there. Multiple cut edges hitting
the same path only overcount its loss. Do not charge a whole original pair's
fractional mass merely because some of its paths were hit.

For a component H, let M_H be these unhit copy pairs and X_H their endpoints.
Every A restricted to H is phi-flow-expanding. The endpoint indicator of X_H
is pointwise at most A. In particular the product demand

    D_H({u,v}) = phi/|X_H|,        u,v distinct in X_H,

has marginal at most phi at every endpoint. Dividing this demand by phi gives
an A-respecting demand, which routes at congestion 1/phi; scaling back proves
that D_H routes at congestion 1 in H. It is computable by a rational compact LP.
This argument uses all-demand expansion, and does not assert monotonicity of a
normalized product formula after its denominator changes. Components with
M_H empty are ignored.

Apply the uniform CKS congestion-1 matching rounding theorem with alpha=phi
and matching M_H. Its promise holds exactly as just shown, and phi<=1. It
returns at least c0 phi |M_H| unit copy demands without violating capacities.
Component routings have disjoint edges. Over all components they select at least

    c0 phi (3K/4) = 3 c0 K/[128 T Gamma(2K)]
                      >= 3 c0 F/[256 Gamma(2K)]

copy demands. All these inequalities are real lower bounds on the integer
number selected; a nonempty connected component can always route one pair
when the asymptotic bound is below a constant.

## 4. Protected admission and the parameter k

In the FULL augmented graph, the old source occurrence edge for original pair i
is a bridge separating all its new source-copy terminals from every new
sink-copy terminal of that pair. In a feasible unit routing of any two copies
of i, the cut consisting of this one old edge would have load at least 2.
That contradicts congestion 1. Thus the combined component output contains
at most ONE selected copy of each original pair. This is a cut argument for
splittable unit demands, not an assumption of integral paths. It also applies
to parallel indexed original pairs, which have distinct old occurrence edges
and are legitimately distinct demands.

Project away copy and occurrence segments. The output is therefore a feasible
subset of distinct ORIGINAL indexed pairs, with the SAME cardinality and loads
at most 1 on every original edge. Extra same-vertex pairs admitted initially
have zero load and can be added; the approximation bound is preserved because
Gamma is at least a fixed positive constant.

Since k>ceil(log2 N), T<=64(k+2). Hence

    2K <= 2D <= 2k(T+1) = O(k^2),

and Gamma(2K)<=C log(k+2) exp(C sqrt(log log(k+4))). The small-k branch was
already polynomial and exact. This is ONE uniform polynomial-time algorithm
for every input; it does not hide a parameter-dependent running-time exponent
or replace log k by log n. All graph augmentations have polynomial size.
All invoked flow LPs, path decompositions, output checks and projections are
polynomial in bit complexity. Finite random sampling already has a fixed
polynomial bit bound. The chosen overhead constants are constants of the cited
decomposition algorithm, not input-dependent advice.

## 5. Corrected CKS dependency reconstruction

This checks why the conference theorem's exact congestion assertion is supported
by the corrected journal argument. It is NOT a new nonuniform rounding result.
Let X be the matching endpoints, q=|X|, and suppose the unordered product demand
alpha/q is feasibly routed. Set rho(v)=alpha/4 for v in X and 0 otherwise,
and let mu be uniform on X. For each ordered pair u,v in X, route
alpha/(4q) from u to v using the product flow, in the appropriate direction.
For u=v keep the same amount in place. Thus each terminal simultaneously sends
rho(u) units to the SAME distribution mu. On each unordered product commodity,
the two directions together use one half its routed amount. The aggregate
common-distribution flow therefore has load at most 1/2 on EVERY edge.

This supplies exactly the common-distribution conclusion of CKS2013 Lemma 3.4
needed in Section 3.4, with their rho=1/(2 alpha(G,T)) replaced by alpha/4.
The sole use of the nice-instance/Raecke-tree premise in the Section 3.4
rounding is to obtain that conclusion. The other steps use the graph, terminal
matching, uniform rho and connected grouping, as follows (printed pp.1478--1483):

* Lemma 3.9 is a weighted tree-center argument: one cluster can receive one
  unit within rho while its edges carry at most 1/2. Lemma 3.12 gives the
  separating cluster bridge for a noncenter, by a single-source min-cut.
* Lemma 3.3 groups uniform rho into connected edge-disjoint clusters with
  disjoint OWNED receiving sets S_j of mass in [1,2), leaving total owned
  mass less than 1. Discard pairs incident to uncovered terminals. The number
  discarded is at most 1/rho, whereas total pairs have rho-weight q rho/2.
  When q rho is below a fixed constant, route one arbitrary pair instead.
  Otherwise the remaining pairs are a constant fraction, and greedy cluster
  selection retains Omega(q rho) pairs since a selected pair blocks at most
  two clusters, each containing fewer than 2/rho owned terminals.
* In the proof of Lemma 3.11, tagging the first external contact of a
  noncenter merges it with an auxiliary cluster. Lemma 3.13 proves that it
  can then spread one unit using half capacity except on BRIDGES OF THE
  WHOLE INPUT GRAPH, on which it uses at most 1. The min-cut proof requires
  two distinct cluster centers and total receiving weight at least 1 in
  each participating cluster. Both hold here, with the same uniform rho.
* After identifying a selected pair's clusters, the tagging digraph has
  out-degree at most 2 on pair nodes. Its special-node subgraph is
  4-degenerate, so a 5-coloring retains a constant fraction independent of
  tags from other clusters. Mated pairs and direct mate tags give disjoint
  local unit routes, or the remaining case has only unselected transit
  clusters. Lemma 3.14 pairs tagging contacts through each transit tree by
  edge-disjoint paths; at most one contact is unmatched for each odd degree
  >=3. Hence at least a third of pairs have neither endpoint isolated.
  A further degree-at-most-2 conflict selection retains at least a third
  of those pairs. The resulting amalgamations are edge-disjoint and give
  the Lemma 3.11 pseudocenters and disjoint receiving supports. These steps
  involve only topology and the uniform mass-counting bound, not a tree
  embedding or demand feasibility on a Raecke tree.
* Shared cluster vertices are explicitly treated in the final paragraph
  on printed p.1483: tagging can be through a shared vertex instead of an
  external edge. Receiving mass belongs to its original owned S_j only,
  as ensured in Lemma 3.3; a transit path uses its vertex at no edge cost.
  The copied terminals themselves are degree-one and cannot be shared
  connectors. Replacing shared tags by the corresponding zero-edge contact
  is exactly the source's stated correction, not an added vertex capacity.

At this point either a constant fraction of selected pairs is mated (route
them within their edge-disjoint connected amalgamations), or retain the
unmated class. Each endpoint of an unmated pair spreads one unit to its owned
support within rho, at load at most 1/2 on nonbridges and 1 on bridges. Supports
are disjoint. Scale each terminal's above common-distribution flow by its
received mass divided by rho(v). The combined second-stage load is at most
1/2 per edge. Each endpoint reaches mu; couple its distribution with its
mate's at mu, concatenate and remove cycles. Loads before cycle removal are
at most 1 on nonbridges and 3/2 on bridges.

Lemma 3.10 now gives EXACT congestion 1: for simple paths, a unit commodity
uses any bridge either with its whole unit (if endpoints are separated) or
not at all. Its total load on a bridge is an integer and is <2, hence <=1.
All other edge loads can only decrease. No constant-congestion substitution
has occurred. All center tests are rational single-source max-flow, and all
tagging, coloring, pairing and cycle cancellation are polynomial operations.

This reconstructs the general uniform matching-rounding contract stated in
CKS2005 Theorem 3.1 using the corrected journal clustering, without assuming
that our input is a nice Raecke instance. We rely on the published corrected
shared-vertex argument as prior work. We do not claim to have proved the
nonuniform NR from research pass 1: the uniform-copy construction eliminates
that unproved premise from the original-target proof.

## 6. Adversarial checks, novelty scope and review obligations

The supplied exact script checks the copy-splitting identities, categorical
sampling marginals, fixed-path cut charging, bounded dyadic probability error,
the rational error-budget inequalities and the old-bridge multiplicity cut on
explicit finite domains. It is not an implementation or exhaustive verification
of BJS or CKS, and does not certify this infinite algorithmic theorem. Those
theorems are explicit dependencies. The general arguments are above.

The key failure cases were checked in the argument: tiny rational x_i do not
create denominator-many copies; shared original endpoints get different old
occurrence bridges; duplicate input pairs keep separate indices; original k
can be much smaller than n (the exact branch applies); disconnected inputs
allow F=0; discarded paths lose pairs of copies, not integral original credit;
surviving demand normalization uses all-demand expansion; rounding is exactly
congestion 1; and distinct-copy counting is converted to distinct-original
counting only AFTER the bottleneck cut proof.

Current primary-source comparisons are recorded separately in
research-2-literature.md. No full equivalent was located in that bounded search.
The proposed substantive advance is the full original-target improvement from
the O(log^2 k) guarantee explicitly recorded by BJS2026 to log^(1+o(1)) k,
through a protected-copy reduction that removes both the changing-throughput
interface and n dependence without weakening congestion. This is a SHORT
composition of strong prior tools. A fresh referee must critically decide
whether the reduction is sufficiently nonroutine and whether its significance
is competitive; neither is inferred from correctness or the open-problem label.

Proposer's mathematical gap list: empty relative to the two precisely stated
published dependencies above. The shared-vertex clustering is a cited corrected
prior result, not a new unverified nonuniform extension. No independent fresh
review, acceptance, venue-quality certification, manuscript or PDF is produced
in this job. A proposed resolution can still be rejected on correctness,
novelty, significance or interpretation grounds.
