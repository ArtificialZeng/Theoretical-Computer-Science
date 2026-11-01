# Proposed resolution: exact matching-advice frontiers at degree two

Research job: advice-matching-research-eee7dbe89d57. This is a proof submitted
for fresh scrutiny, not a referee report or an acceptance. The model is exactly
problem.md: simple unweighted bipartite graphs, integral irrevocable matches,
fixed graph/order/advice independent of private coins, and an injective partial
matching table which may contain absent edges. No additional graph information
is supplied by the advice. All optima below are cardinality optima.

## Statements

Let D be the class with maximum degree at most two on both sides, allowing
isolates and arbitrary interleaving of components. Let C be its 2-regular
subclass (disjoint simple even cycles, including 4-cycles). For each requested
consistency c in [0,1], the largest achievable robustness is

    D: r_D(c) = min(3/4, 3/2-c),
    C: r_C(c) = min(7/8, 7/4-c).

The D formula answers the original source's full frontier question under its
explicit frozen oblivious-adversary reading. The C formula is a related sharp
regime, proved in the same argument rather than split into another project.
Both guarantees are strict multiplicative guarantees, with no additive error,
for every finite n, arrival order, and table. Correctness on good advice is
required for EVERY maximum matching, including partial maximum matchings.

Known ingredients must be credited: the D upper gadget and c+r<=3/2 are
already in Choo et al. and Jin--Ma; the advice-free C optimum 7/8 is already
proved by Fàbrega--Muñoz (2018), Proposition 2 and Theorem 2. The randomized
priority rule below also coincides on C with an established semi-OCS rule
identified explicitly by Feng et al. (2025), Algorithm 2 and the paragraph
after it. No novelty is claimed for those baselines, the gadget without
advice, deterministic high-degree priority, or random mixing. See
literature/research-comparison.md for the exact proposed delta and limitations.

## Online rules

Maintain the number h(u) of incident edges revealed at each offline vertex.
When v arrives, increment h at all its neighbors. A neighbor is fresh when
h(u)=1 and exhausted when h(u)=2. An exhausted vertex has no later incident
edges, by the realized offline degree promise. Availability means not already
matched. Both rules always match if an available neighbor exists.

E: Prefer an available exhausted neighbor. If none exists, take the sole
available neighbor, or choose uniformly between the two available fresh
neighbors with an independent fair coin. Break ties between exhausted
neighbors by a fixed label order.

T: Give the same priority to an available exhausted neighbor. Otherwise take
a(v), if it is a present available neighbor, and use fixed label order as
fallback. T uses no randomness. Only a(v), not a graph encoding, is consulted.

Both rules require only already revealed edges and the offline degree bound.
They do not know the component decomposition or future arrival order.

## Lemma 1: the root-boundary invariant

Fix one final nontrivial component and its induced online order. Classify an
arrival by its actual degree and the number of its neighbors seen previously:

- A pair root is a degree-two arrival with two fresh neighbors; let a count it.
- An extension is a degree-two arrival with one old and one fresh neighbor;
  let b count it.
- A merge is a degree-two arrival with two old neighbors; let z count it.
- An initial online leaf is a degree-one arrival with a fresh neighbor;
  let s count it.
- A terminal online leaf has an old neighbor; let t count it.

These classifications depend on the fixed graph and order, never on coins or
matching choices. At a root both neighbors are free, and exactly one becomes
occupied. Give its two offline endpoints complementary occupancy bits. Under
E they are opposite fair bits from that root's independent coin. An initial
leaf creates one occupied endpoint with deterministic bit 1.

An offline vertex seen once is an endpoint of the revealed subgraph and may
still have one future neighbor. Its occupancy is its boundary bit. At an
extension, the new offline endpoint has the SAME occupancy as the old one had
before this arrival: if the old endpoint is free, priority matches it and
leaves the new endpoint free; if it is occupied, the new endpoint is matched.
In either case the extension succeeds. This identity is deterministic and
holds for E and T. No new randomness is used.

At a merge, both old neighbors become exhausted. It fails exactly when their
two bits are 1, and then consumes these two boundaries. If it succeeds, its
choice between free exhausted neighbors cannot affect any later boundary.
An online terminal leaf fails exactly when its one consumed boundary bit is 1.
Thus every surviving boundary is precisely one of the original root bits
(or a deterministic bit 1), transported without alteration. No bit is copied
or reused at two distinct future consumption events.

For a path, contract each extension. The graph linking the a pair roots and
s initial leaves via merges is a path: roots have two ports, initial leaves
one, and remaining ports are consumed by terminal online leaves or are final
offline endpoints. This is also immediate from the final component being a
path; a merge between boundaries already in the same revealed component would
close a cycle and cannot occur. For a cycle the analogous port graph is a
cycle of roots, possibly a single root with its two ports joined.

The two bits consumed by an edge between DISTINCT root objects therefore
come from distinct independent coins under E, even if the corresponding
revealed paths were previously joined to other roots. Their unconditional
joint probability of both being 1 is 1/4. A root-to-initial-leaf edge has
failure probability 1/2. These statements are unconditional identities on
the fixed input; conditioning on observed success histories is unnecessary
and generally would destroy the claimed independence.

## Lemma 2: exact component expectations

A path has m online vertices, q offline vertices, and ell in {0,1,2} ONLINE
endpoints. Then q=m+1-ell, s+t=ell, and

    q=2a+b+s,     z=a+s-1.

The first identity counts first appearances of offline vertices. The second
follows from m=a+b+z+s+t and the path's vertex counts, or from connecting
a+s initial revealed components into one by z merges.

If a>=1, no merge connects two initial-leaf objects: those each have just
one port, and their joining would already form a whole final path with no
room for a root. Each of the s leaf objects consequently has one root
neighbor in the contracted path. The remaining z-s=a-1 merge edges join
distinct roots. Also, every terminal leaf is fed by a root bit: a path segment
starting at an initial leaf cannot reach a terminal leaf without passing a
root, since that segment would itself be a completed component. Summing
failure indicators using Lemma 1 gives

    E[|E(path)|] = m - (a-1)/4 - s/2 - t/2
                 = m - (a-1)/4 - ell/2.            (P)

If a=0, all surviving boundaries are occupied. There are z=s-1 failed merges
and t failed terminal leaves, so there are s-1+t=ell-1 failures. A nontrivial
path without roots has ell>=1 (its first online arrival must be a leaf).
Its output is m-ell+1=min(m,q), its exact optimum. This covers a single edge
and the two-online-leaf path. Isolated online/offline vertices contribute 0.

For a cycle, s=t=0, q=m=2a+b and z=a. If a=1, extensions preserve the two
opposite root bits and the closing merge cannot fail; the output is m.
If a>=2, every merge edge of the root port cycle joins DISTINCT roots,
including the last closing edge. With a=2 there are two parallel port edges,
but each uses a different pair of root ports, and linearity of expectation
still applies. Hence

    E[|E(cycle)|] = m                 if a=1,
                 = m-a/4             if a>=2.      (C)

These formulas depend on arrival order only through a and the path endpoint
type. They use the degree promise on BOTH sides.

## Corollary: E's guarantees

On paths with ell=0, OPT=m, m>=2a and the deficit (a-1)/4 is at most m/8.
On paths with ell=2 and a>=1, OPT=m-1 and the deficit relative to OPT is
(a-1)/4; since m-1=2a+b+s-1>=2a-1>=2(a-1), this is at most OPT/8.
Paths with a=0 are optimal. Thus these two unbalanced types attain 7/8.

On a balanced path (ell=1), OPT=m and the deficit is (a+1)/4. If a>=1,
m=2a+b+s>=a+1, giving ratio at least 3/4. The smallest Z path, with m=2,
a=1, attains exactly 3/4. Formula (C) and m>=2a give 7/8 on every cycle.
Linearity over final components, regardless of their arrival interleaving,
therefore proves E>=3 OPT/4 on D and E>=7 OPT/8 on C. E ignores advice,
so these ratios are simultaneously consistency and robustness guarantees.

## Lemma 3: T is optimal for every maximum advice table

Let A be any maximum matching of the realized graph, and M the matching
produced by T. Suppose |M|<|A|. The symmetric difference A triangle M then
contains an M-augmenting path. Label its edges as

    v0--u0--v1--u1-- ... --vk--uk,

where vi--ui belongs to A and vi+1--ui belongs to M. Vertex v0 and offline
endpoint uk are unmatched by M. Let tau(v) be the arrival time.

Because T always matches when possible, u0 had to be occupied when v0
arrived; hence tau(v1)<tau(v0). Suppose tau(vi)<tau(vi-1). When vi chose
ui-1, that offline vertex had not appeared previously: its only two possible
neighbors are vi and the later vi-1, by maximum offline degree two. Thus T
chose a FRESH vertex at this step. A valid free advised neighbor ui would
have been preferred to ui-1: any available exhausted neighbor would instead
have been chosen, so none existed; among fresh neighbors T takes its own
valid available advice. Since T did not take ui, that vertex was already
occupied by vi+1, which must have arrived even earlier. Consequently

    tau(v0)>tau(v1)> ... >tau(vk).

At the last step vk, its advised neighbor uk is free even at termination,
so was available when vk arrived. The same argument forces T to take uk,
contradiction. The length-one augmenting path (k=0) is excluded directly by
T's always-matching rule. Thus |M|=|A|=OPT.

This argument allows A to leave vertices unmatched, allows arbitrary offline
labels, and does not require A to be a perfect matching. It uses only the
legitimate advised pairs. No stronger information is silently inferred.

## Lemma 4: robustness of T

For every advice table, including tables with absent edges, T is greedy and
its final matching is maximal: an edge with two finally free endpoints would
have had its offline endpoint free when its online endpoint arrived. Each
edge of a maximum matching touches a matched endpoint of M, and each edge
of M can account for at most two optimum edges. Therefore |T|>=OPT/2 on D.

On a cycle, the invariant of Lemma 1 is deterministic. Every pair root,
regardless of its advised choice, creates exactly ONE occupied port and one
free port. Extensions preserve these port bits. Each failed merge consumes
two occupied ports; no root port is reused. Therefore the number of failures
is at most floor(a/2), under arbitrary advice and arbitrary deterministic
correlations between the root choices. There are no online leaves and no
other failures. It follows that

    |T(cycle)| >= m-floor(a/2) >= m-a/2 >= 3m/4,

because m=2a+b>=2a. Summing cycles proves robustness 3/4 on C. Together with
Lemma 3, T attains (consistency,robustness)=(1,1/2) on D and (1,3/4) on C.
The latter guarantee is degree-aware, and remains valid when advice is wrong
on every edge where T consults it.

## Achievability of the two frontiers

Write beta=3/4 on D and beta=7/8 on C. Rules E and T attain respectively
(beta,beta) and (1,2beta-1). For c<=beta use E. For c>=beta, select T once
before the input with probability p=(c-beta)/(1-beta), and otherwise use E.
For each fixed input and table, linearity of expectation gives consistency
(1-p)beta+p=c and robustness (1-p)beta+p(2beta-1)=2beta-c. This mixture is
standard and is not asserted to be a new technique. Guarantees for all
smaller r follow immediately.

## Matching upper bounds: fixed indistinguishable inputs

For D use U={0,1}, V={x,y}, order x,y, with x adjacent to both offline
vertices. The two completions have N(y)={0} and N(y)={1}. They are both
three-edge paths with OPT=2. Conditional on the common first action, the
sum of the two best possible final matching sizes is at most 3 (and 2 on
abstention). This bound holds with an arbitrary common table. Using empty
advice in both worlds gives 4r<=3. Using the same table A(x)=0,A(y)=1,
which is optimal in the second completion, gives 2c+2r<=3. These are the
known Choo/Jin--Ma bounds, verified directly in evidence/known-obstruction.md.

For C take U={0,1,2,3}, V={x1,x2,y1,y2}, in that order. In both worlds,
N(x1)={0,1}, N(x2)={2,3}. Complete with

    G0: N(y1)={0,2}, N(y2)={1,3};
    G1: N(y1)={0,3}, N(y2)={1,2}.

Both are simple 8-cycles and OPT=4. Fix any pair of common initial actions.
If both x vertices matched, exactly two offline vertices remain free, one
in each initial pair. In one completion those two free vertices lie in a
single y-neighborhood, allowing only one further match; in the other they
lie in different y-neighborhoods, allowing two. The sum of the final optimum
continuation upper bounds is thus 7. With one initial match the sum is at
most 6, and with no initial match it is at most 4. These statements cover
abstention and all correlations in the first two choices.

An algorithm sees the same history in both worlds before y1. Couple its
private random tape across worlds; the conditional sum bound holds for every
tape, hence also after expectation. Empty advice gives 8r<=7. With the fixed
table A(x1)=0,A(x2)=2,A(y1)=3,A(y2)=1, advice is perfect in G1, and remains
an injective matching table in G0 although its last two pairs are absent.
The same sum inequality gives 4c+4r<=7. This is a fixed oblivious pair of
inputs, not an adversary reacting to realized random choices. The advice-free
7/8 gadget is known; the common-table use gives the required advice tradeoff.

Thus both achievable formulas meet their upper bounds for every c in [0,1].

## Dependencies, scope, and gap list for the referee

Logical dependencies: component classification of degree-two graphs; elementary
matching symmetric difference and maximal-matching bound; counting/linearity;
the self-contained root invariant above. No numerical computation or external
theorem is needed for logical correctness. Literature is needed to assess
novelty/value and attribution, especially because the cycle baseline, its
algorithm, and its root-orientation analysis have substantial prior overlap.

Known mathematical gaps in the proposed proof: none identified by this worker.
This is a request for fresh review, not a certification that no gaps exist.
Scope not claimed: adaptive-adversary achievability, weighted/fractional
matching, online-degree-only G(n,2), random-arrival guarantees, or hidden graph
advice. The proof settles the exact interpretation frozen in problem.md.

Reproducible supporting checks: python3 evidence/check_frontiers.py --max-online 8.
The independently implemented forward distribution verifies all four component
types and every order through eight online vertices, all their maximum advice
matchings, all cycle root orientations, all 265 labelled degree-bounded n=3
graphs with every order and every one of 34 partial injective advice tables,
and every initial-action case in the two upper gadgets. Finite evidence is
supplementary; completeness here is for these finite domains only.
