# Research pass 2: clipped offline two-clock composition

Job: c042-strongrsp-research-266844093669. This is a local algorithmic lemma,
not a full resolution, innovation assessment, or publication candidate.
The immutable original in `source.md` remains unresolved.

## Contract and algorithm

Use exactly the finite-increment, whole-vertex static control model proved in
`research-pass1-boundary.md`, including voluntary ticks, source payoff rho,
failure/nontermination payoff M=1+rho, and rho>0. At integer times 0,...,T,
each edge has a supplied increment distribution. Assume the distributions are
stochastically nonincreasing in time in the coordinatewise order (a coupling
with both increments nonincreasing suffices). Thus the full optimal tables
X_t are nonincreasing in time and nondecreasing in both clock coordinates.
To see time monotonicity, simulate a later-time policy's larger-increment
counterpart, or use the earlier-time optimal policy at the later time while
maintaining virtual earlier clocks; fewer actual ticks cannot hurt success.
Equivalently the finite-rank Bellman construction and monotone couplings give
the comparison. This assumption is on the supplied finite laws; no finite-cost
construction of Poisson approximations is inferred from it.

Let alpha=1+zeta>1. Solve X_0 and X_T exactly. For an interval [l,r] with
r-l>=2 at depth h, its stored endpoint tables U_l,U_r have

    X_l <= U_l <= alpha^h X_l,   X_r <= U_r <= alpha^h X_r,
    rho <= U_r <= U_l <= M,

and both tables are clock-monotone. The root has h=0. Activate a vertex v
iff some clock state k=(i,j) has U_l(v,k)>alpha U_r(v,k). All q^2 states of
v are then active. At midpoint t=floor((l+r)/2), give each inactive vertex
the boundary table B_v=U_l(v,*), and solve just the active vertices with the
pass-1 oracle, obtaining Y. For active entries set

    U_t = max(U_r, min(U_l,Y))

coordinatewise. Inactive entries of U_t remain U_l. Recurse on [l,t] and
[t,r]. Endpoint versions are immutable. Adjacent endpoints need no call.
T=0 or T=1 is handled directly. The source is always inactive and exact.

## Error and monotonicity proof

For an inactive entry, X_t<=X_l<=U_l and

    U_l <= alpha U_r <= alpha^(h+1) X_r <= alpha^(h+1) X_t.

The static first-hit lemma therefore gives X_t<=Y<=alpha^(h+1)X_t on active
entries. Both U_l and Y dominate X_t, so their minimum does too. The outer
maximum cannot spoil this lower bound. Also U_r<=alpha^h X_t, so the maximum
still obeys the upper error bound alpha^(h+1)X_t. Inactive entries obey the
same bound by the displayed inequality. Min and max preserve coordinatewise
clock monotonicity. Finally U_l>=U_t>=U_r. Induction proves every claim and
global time monotonicity of all stored versions. This proof does not assume
that a clipped value comes with the static oracle's realizing policy.

Let D=max(1,ceil(log2(max(1,T)))); computing this uses bounded integer doubling,
not a logarithm of a real input weight. There are at most D midpoint levels,
so every reported estimate lies between X_t and alpha^D X_t. For example,
zeta=1/(16D) gives alpha^D<=16/15 by bounding the binomial series by the
geometric series with ratio 1/16. This is a constant value distortion, not
the final RSP length/cost accuracy allocation.

## Nested activity and aggregate incidence work

A vertex inactive at a parent has U_l<=alpha U_r for every clock entry.
In either child, the earlier endpoint can only decrease and the later
endpoint can only increase. Hence the same inequality holds in both children.
It can never reactivate below that parent. Consequently the root scans n
vertex blocks; each later call tests only its parent's active vertices.
Two child tests per parent cost O(q^2) block-coordinate comparisons per
parent-active vertex, plus persistent-table access. No all-vertex scan is
needed at later recursion nodes.

Fix a depth and one vertex-clock entry k. The intervals [l,r] at that depth
have disjoint interiors in time order. Global estimate monotonicity implies

    product_over_intervals U_l(v,k)/U_r(v,k) <= M/rho.

Each interval witnessed by k has ratio strictly greater than alpha. Thus k
witnesses at most log(M/rho)/log(alpha) such intervals. Union bounding over
the q^2 coordinates, and then D depths, gives at most

    R = q^2 D log(M/rho)/log(alpha)

active calls per vertex (round this expression upward for an integer bound).
This argument uses logs only in the analysis. With fixed rho and
zeta=Theta(1/D), R=O(q^2 D^2). For any fixed nonnegative vertex weights w_v,
the total sum of w_v over all active lists is at most R sum_v w_v. Choosing
w_v=1+d_v, where d_v counts both input adjacency incidences, proves the
corresponding active-vertex/incident-edge work bound even for parallel edges.
No degree-dependent exception or per-target n multiplier is hidden here.

## Data access, storage, output

Build incoming/outgoing adjacency lists once. Store each q^2 vertex table
as a leaf block of a persistent balanced binary tree on vertex labels.
Lookup costs O(log(n+2)); a block update copies O(log(n+2)) nodes and q^2
values. At a midpoint, start from the U_l root and update only active blocks.
The static oracle retrieves inactive blocks only at incident-edge endpoints;
cache a retrieved block within the call. Build active membership locally
(balanced dictionaries, or arrays with timestamps) rather than clearing n
entries. The oracle reads/relaxes only edges incident to active vertices.
This is a constructive persistent representation, not n copies per time.

If one edge's coefficient snapshot at time t costs H arithmetic/control
operations, a conservative total bound, including both full endpoint solves,
is

 O(T + (n+m)(1+R) q^4 [H+log(n+2)]),

plus the cost of preparing the supplied coefficient/event data. Persistent
storage is O(n q^2 + T + n R [q^2+log(n+2)]) in addition to graph/coefficients;
static scratch is reused depth first and fits the same larger bound after
including incident-boundary scratch. A sorted per-edge event list gives
H=O(log(J+2)) index comparisons plus the supplied coefficient access cost
when an edge has at most J events. Neither the algorithm nor the work proof
scans the full event graph at each midpoint. The recursion has O(T+1) nodes.

Store a root pointer per event time. Given a fixed threshold, global time
monotonicity permits binary search for each target's first accepted time in
O(log(T+2) log(n+2)) block accesses/comparisons, hence n times this work for
all targets. These estimates alone are not path witnesses. The full original
still needs a certified real-resource bound and its deterministic decoder.

For arbitrary uncompressed m, log T may involve log m. This local lemma
therefore does not by itself meet the frozen polylog(n) bound. The full
program must first prove an O(m polylog(n)/poly(epsilon)) parallel-edge
compression with only polynomial(n,1/epsilon) retained edges; the intake
proposal is not established by the present proof.

## Numerical boundary of this lemma

This section establishes exact arithmetic composition on supplied rational
increment laws. It does not establish the frozen intermediate bit bound.
Repeated exact DP products and recursive estimates may have large encodings
as q or 1/epsilon grows. Conservative bounded-precision coefficient tables,
rounding-stable oracle estimates and an error allocation through this very
recursion remain indispensable. An exact arithmetic-count proof cannot be
substituted for that obligation.

## Validation and disposition

`check_offline_composition.py` and `offline-composition-results.json` record
14 exact-rational event sequences (q=2 and a structured q=3 family), plus
four dyadically rounded recursion runs under the extension in
`research-pass2-rounding.md`. The exact runs have 3,134 midpoint-state
comparisons, 380 exact potential checks and 144 strictly inflated entries;
their reference evaluates 22,344 stationary policies, 1,140 with closed
nontermination. Rounded runs add 1,230 state comparisons, 116 potential
checks and 144 inflated entries, using b=17 or 18. All checks pass.

The recursion interface actually uses persistent blocks, parent-only
activation tests and indexed active incidence scans. The checker asserts
that each call's incidence inspections equal q^2 times its active degree
sum. A scan-min queue is used for these tiny fixtures, so this is not a
heap running-time benchmark. Global all-state scans occur only in the
explicitly marked validation/reference code, not in the offline interface;
their reads are not misreported as production timing. The reference reuses
the preserved policy evaluator and is not an independent referee.

These initial exact-endpoint sequences caused no clipping. To test the
otherwise unexercised branches, two additional exact local induction
fixtures have admissible inherited approximate endpoints. One produces
raw 153/256 above the earlier envelope 17/32; the other produces raw 9/32
below the later envelope 81/256. Clipping restores the respective envelope
and preserves the claimed error bound. Both witnesses are serialized.
This is an adversarial extension of the suite, not evidence that the
original unrounded sequences exercised those branches.

The numerical extension supplies another local proof with exact tests;
none of these distributions is claimed to be a constructed Poisson law.
No original-scope candidate or manuscript/PDF is created. The next decisive
test is finite-cost conservative probability/event compilation and its
complete resource-error, bit-length and all-target integration, with the
unchanged original and one accumulated research pass remaining.
