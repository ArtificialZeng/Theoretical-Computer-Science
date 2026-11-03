# Research proof packet: the full below-half threshold

Proposer job: c037-msthalf-research-d39900f29f79. Research pass 3 of 3.
This is a proposed full resolution for fresh review, not a manuscript,
referee report, acceptance, or STOC assessment. The immutable statement is
`source.md`; its precise reading is `problem.md`. Source SHA-256:
`d45cd6730fe3f8685cb796b9d75ebe8e7926c1584021d045a282021749e45128`.

The changed input is the supervisor's general-metric interval-packing
argument, identified in `outer-root-note.md`. It supersedes the need to solve
the stronger ultrametric-only B4 assertion. B4 itself is left unresolved.
The argument below reconstructs the general-metric proof and the complete
observable algorithm. The benchmark repair is known in substance from Anand
et al., arXiv:2610.40594v1, Lemma 3.2; an unconditional-indicator version is
proved here so no large-n convention is hidden in the final expectation.

## Proposed theorem (the entire original affirmative statement)

For every fixed real p in [0,1/2), there is an explicit finite deterministic
procedure, receiving only the symmetric corrupted observations, n and p,
whose output is a spanning tree and whose expected TRUE cost is at most
C_p max(1,ln n) MST(d), for every n>=2, every n-point metric d, and every
omniscient post-mask replacement rule in source.md. C_p is finite and
independent of n, aspect ratio, d, and the replacement values. No true-distance
queries or triangle inequality for observations are used. No efficiency
claim is made.

## 1. Deterministic interval-packing theorem

Let v_1,...,v_n be distinct metric points, w_i>=0 for 1<=i<n,
t_1=0, t_j=sum_{i<j} w_i, W=t_n, and q(u,v)=|t(u)-t(v)|.
Let r>=1 be integral and 0<eta<=1. Suppose an undirected simple graph H
satisfies:

1. For every disjoint A,B with |A|,|B|>=r, the number of H-edges between
   them is at least eta|A||B|.
2. d(u,v)<=q(u,v) for every H-edge uv.

Then, writing D_i=d(v_i,v_{i+1}) and M=MST(d),

    sum_i D_i <= (320r/eta) W + (8r/eta) M
              <= (320r/eta)(W+M).                       (1)

All metric distances between distinct points are positive; q may vanish.

**Hereditary density and a star.** If S has m>=2r vertices, average the
rectangle hypothesis over uniformly chosen ordered disjoint r-subsets A,B
of S. Each unordered edge of H[S] is counted with probability
2r^2/[m(m-1)]. Thus |E(H[S])|>=eta m(m-1)/2 and some vertex of S has
degree at least eta(m-1) in H[S]. Set L=ceil(2r/eta). For m=2L, this
degree bound is at least eta(2L-1)>=4r-eta>=3r, hence in particular at
least r. There is a star with center z in S and r distinct leaves B in S.
Only this existence statement is used, never an algorithmic oracle for H.

**The overlap argument.** Edges with D_i<=64w_i contribute at most 64W.
For each of the other edges put

    I_i=[t_i-D_i/64, t_i+D_i/64].

Its length is D_i/32. If x belongs to I_i, both endpoints of this edge
have t-coordinate strictly within D_i/32 of x: the first is at distance
at most D_i/64, the second at most D_i/64+w_i<D_i/32. This remains true
at interval boundaries and with w_i=0.

Suppose at least 2(L+r) of these intervals contain a point x. At least
L+r corresponding path edges have the same index parity. Such edges are
pairwise vertex-disjoint. Keep L+r of them and sort them by nondecreasing
true length. The L smallest are the bottom group and the remaining r the
top group. Let D0>0 be the largest bottom length. Equality of lengths is
allowed and ties can be broken arbitrarily.

The bottom endpoints form a set S of 2L distinct vertices, all strictly
within D0/32 of x in t-coordinate. Choose the star center z and its r
leaves B from the preceding paragraph. For b,b' in B,

    d(b,b') <= d(b,z)+d(z,b')
             <= q(b,z)+q(z,b') < D0/8.                 (2)

This includes b=b'. Now take any top edge aa' of length D>=D0. Its
endpoints are strictly within D/32 of x. For every b in B,

    q(a,b), q(a',b) < (D+D0)/32 <= D/16.               (3)

If both endpoints had an H-neighbor in B, say ab and a'b', domination,
(2), (3), and the true triangle inequality would give

    D <= d(a,b)+d(b,b')+d(b',a')
       < D/16 + D0/8 + D/16 <= D/4,

a contradiction. Therefore at least one endpoint of EACH top edge has
no H-neighbor anywhere in B. Choose such an endpoint from each top edge.
They form an r-set A disjoint from B, by the matching construction, and
H has no edge between A and B. This contradicts eta>0.

Consequently fewer than 2(L+r) intervals contain any x. Since
L<=2r/eta+1 and r>=1, eta<=1, their multiplicity is at most 8r/eta.
This proof uses all lengths together; no W charge is repeated by scale.

**Integration.** Let Dmax=max_i D_i. All intervals lie in
[-Dmax/64,W+Dmax/64]. Integrating their finite multiplicity gives

    sum_expensive D_i/32 <= (8r/eta)(W+Dmax/32).

Add 64W and use r/eta>=1 and Dmax<=diam(d)<=M to obtain (1).
The last inequality follows by taking the path in a true MST between any
two points and applying triangle inequality. If there are no expensive
edges the bound follows directly. If 2r>n, the proof's contrary overlap
configuration cannot occur, so no nonvacuity assumption was needed.

## 2. A uniformly cheap all-unmarked comparison tree

Fix ANY true MST, its deterministic depth-first Euler tour, and its
first-appearance order u_1,...,u_n. Let a_i be the true length of the tour
segment from the first appearance of u_i to that of u_{i+1}. Then
sum_i a_i<=2M and the true distance between any two order points is at
most the sum of the intervening a_i. These objects are analysis only.

Set alpha=(1-p)^2>0 and beta=1-alpha. For each marked consecutive pair
u_i u_{i+1}, look for a vertex x outside its endpoints such that BOTH
u_i x and u_{i+1} x are unmarked. Among the candidates choose one closest
to this edge in number of order positions (with a fixed side/label tie
rule). Let F be the event that a candidate exists for every marked
consecutive pair. Each fixed potential x succeeds with probability alpha,
and these events are independent as x varies, because all the tested
unordered pairs are distinct. Therefore, for every n>=2,

    Pr(F^c) <= (n-1) beta^(n-2).                       (4)

For n=2 the exponent-zero expression is interpreted as 1, including beta=0;
the bound is loose but valid. One could include the additional factor p.

On F, keep every unmarked consecutive pair and replace each marked one
by its unmarked two-edge path through the chosen x. The resulting graph
is connected and all its edges are unmarked. A fixed lexicographic cycle
deletion yields an all-unmarked tree T0. Define X=c_d(T0) on F and X=0
outside F. In particular all expectations below are of defined variables.

We claim

    E[X] <= B_p M,   B_p=2(1+4/alpha).                 (5)

To verify it, bound each retained or replacement path by its corresponding
walk in the abstract weighted order with weights a_i. The original edge i
pays its own a_i once; if a repair extends to one side, each additional
order edge on that side is paid twice. Fix a target order edge j. For a
source edge i<j to pay it additionally, its chosen candidate must lie
strictly to the right of edge j. Hence none of the j-i-1 intermediate
vertices u_{i+2},...,u_j can be a successful candidate. The probability
of this necessary event is beta^(j-i-1). The symmetric bound for i>j
is beta^(i-j-1). These implications remain valid after multiplying costs
by 1_F: no conditioning on F is used in the probability calculation.

Summing over source edges on both sides bounds the expected coefficient
of a_j by

    1 + 2 sum_{h>=1} beta^(h-1)
      + 2 sum_{h>=1} beta^(h-1) = 1+4/alpha.

Cycle deletion and duplicate removal only decrease nonnegative true cost.
Summing over j proves (5). This is a reconstruction of the known
tree-repair mechanism, not the claimed new contribution.

## 3. Explicit observable procedure

For a fixed p<1/2 choose a rational pi with p<=pi<1/2. Such a choice can
be hardcoded for A_p. Concretely pi=1/2-2^(-k) for an integer k>=1 with
p<=pi; exact comparison with the input p can also find k by incrementing.
Thus the procedure's numerical constants can all be rational even for
arbitrary fixed real p. The source's exact-arithmetic comparison model for
the observations is retained, with no additional bit-complexity assertion.

Put epsilon=(1-2pi)/8, eta=1-2pi-2epsilon>0,
R=ceil(20 epsilon^(-2)), ell=ceil(log_2 n), r=R ell. Compute ell by
integer doubling. For fixed p, r=O_p(max(1,ln n)).

1. Replace each off-diagonal observation y(u,v)<0 by zero. Retain symmetry.
2. Enumerate all labeled spanning trees. Give each tree edge its clipped
   observed weight, and compute its unique weighted tree-path distances.
3. Qualify a tree T precisely when for EVERY pair of disjoint vertex sets
   A,B with |A|,|B|>=r, at least (1-pi-epsilon)|A||B| pairs uv in A x B
   satisfy y(u,v)<=y_T(u,v).
4. If there is a qualifying tree, take one minimizing the sum of its
   observed edge weights. Break ties lexicographically by sorted edge list.
   Root it at vertex 1, visit children in increasing label order, and output
   the path through vertices in first-appearance order in its Euler tour.
5. If no tree qualifies, output the increasing-label Hamiltonian path.

Every enumeration is finite, a minimum exists in a finite set, and all tests
use only observations and fixed rational parameters. If 2r>n qualification
is vacuous; this causes no undefined step. Every possible output is a
spanning path and hence a spanning tree on the original vertices. The hidden
mask, metric, benchmark tree, and H are never used to choose it.

## 4. Uniform mask concentration and data-dependent transfer

Let E be the event that every disjoint A,B with a=|A|,b=|B|>=r has at
most (pi+epsilon)ab marked cross pairs. Since p<=pi, Hoeffding's bound
for each fixed rectangle is exp(-2epsilon^2 ab). The marks in a disjoint
rectangle correspond to distinct independent unordered pairs. We have
ab>=r(a+b)/2 and r>=20epsilon^(-2)ln n. At most n^(a+b) set pairs have
these sizes, so

    Pr(E^c) <= sum_{a,b>=r} n^[-19(a+b)]
             = n^(-38r)/(1-n^(-19))^2 <= n^(-12).       (6)

The extension to all sizes only enlarges the finite sum. The last inequality
holds for n>=2,r>=1, since (1-2^-19)^(-2)<2 and 2n^-38<=n^-12.
When no such rectangles exist E holds surely. E is a mask-only event and
is uniform over all subsequent adversarial values and selected trees.

On E intersect F, the comparison T0 qualifies: every unmarked pair has
y(u,v)=d(u,v)<=d_T0(u,v)=y_T0(u,v) by triangle inequality. Its observed
edge cost equals X. Thus the selected tree satisfies observed_cost(T)<=X.

For this selected tree define H to contain exactly the pairs that are
unmarked AND satisfy y(u,v)<=y_T(u,v). On E each qualifying rectangle has
at least (1-pi-epsilon)ab dominating pairs and at most (pi+epsilon)ab
marked pairs; therefore H has at least eta ab edges there. For H-edges,
d(u,v)<=y_T(u,v).

For the selected preorder v_1,...,v_n let w_i be the observed length of the
Euler segment between their first appearances. Nonnegativity gives
W=sum_i w_i<=2 observed_cost(T), and for ANY order vertices the tree's
unique path has weight at most the intervening Euler-walk segment length,
which is q(u,v). Thus H obeys both hypotheses of (1), even though T and
its order were selected using the corrupted matrix. No independence of T,
H, E, F, or replacement values is asserted or needed.

If Y is the true output cost, (1) therefore gives on E intersect F

    Y <= (320r/eta)(2X+M).

Using nonnegativity and (5),

    E[Y 1_(E intersect F)] <= (320r/eta)(2B_p+1)M.     (7)

Every spanning tree in a metric, regardless of its selection, has cost at
most (n-1)diam(d)<=(n-1)M. By (4), (6) the complementary contribution is
at most

    [(n-1)n^-12+(n-1)^2 beta^(n-2)] M
       <= [1+2/alpha^3] M.                            (8)

Indeed the second term is at most n(n-1)beta^(n-2), which is at most
the sum of all such nonnegative terms for n>=2. That geometric derivative
sum equals 2/(1-beta)^3=2/alpha^3, valid also at beta=0 with 0^0=1.
This handles every n directly, without claiming source Lemma 3.2's
large-n high-probability estimate for the finitely many small n.

Equations (7),(8), and r=O_p(max(1,ln n)) prove the stated full theorem.
For example B_p<=2(1+4/(1-pi)^2), and the failure term is at most
1+2/(1-pi)^6. A concrete finite C_p follows by substituting these values
and r<=R(1+1/ln 2)max(1,ln n). Nothing depends on the metric or adversary.
Randomized replacement rules are covered by the same pointwise-in-values
argument and averaging. The deterministic algorithm needs no private coins.

## 5. Scope, innovation proposal, and review obligations

The proposed novelty is the combination of a uniformly feasible OBSERVABLE
rectangle certificate and the all-scale metric-star interval overlap proof.
It establishes the full p<1/2 range, beyond the p<1/4 result of Anand et al.
The source's p>=1/2 linear lower bound is prior work. No new lower bound,
polynomial running time, or solution of the stronger ultrametric B4 inequality
is claimed. Finite tests are implementation checks, not the proof of (1).

The mathematical gap list known to the proposer is empty. This statement
requests a genuinely fresh audit: check every quantifier, the overlap/star
contradiction, Euler domination direction, the repair coefficient and all-n
expectation, and novelty/significance against current primary literature.
It is not an audit verdict. No manuscript/PDF is authorized by this packet.
No venue-readiness label is awarded. The prior failed routes and all pass
history are preserved.
