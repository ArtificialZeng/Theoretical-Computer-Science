# Research 3: exact orientation certificates and the unresolved ambient density bound

Job `c049-dualpreserve-research-2396269cbd5d`, assigned pass 3/3,
2026-11-03 UTC. Research records only. No original-scope resolution,
candidate, manuscript, innovation certification, or referee verdict.

## 1. The actual target and the tested sufficient route

The complete immutable algorithmic statement in source.md is unchanged.
Its equivalent critical-graph extremal formulation and paid mixed-fault
reduction remain as in intake/minimal-critical-kernel.md. The missing bound
is global, for arbitrary digraphs and all demand pairs, including deficient
maximum-flow-one/two demands. Nothing below removes this case.

Let B be the undirected multigraph having one edge item for each directed
input edge of a critical graph G. An antiparallel pair contributes TWO
items. Let E*(B) be the minimum of sum_v a(v)^2 over all orientations of
these items, where a(v) is indegree in the freely chosen orientation.
The sufficient ENERGY assertion from pass 2 is

    E*(B) = O(n(p+1) polylog(n+2)).                         [UNPROVED]

It would imply m^2 <= n E*(B) by Cauchy, hence the desired critical-edge
bound and the already paid deterministic construction. It is NOT asserted
equivalent to the original algorithmic question.

## 2. Exact dual certificate (standard convex orientation theory)

The orientation optimization itself is known, not a new contribution.
Borradaile--Iglesias--Migler--Ochoa--Wilfong--Zhang, JGAA 21(4),
687--708 (2017), DOI 10.7155/jgaa.00435, Corollary 2 and Theorem 3,
prove the path-reversal optimization for convex indegree costs. Frank and
Murota, arXiv:1808.07600v3, develop more general square-sum/min-max theory.
The following elementary proof also covers the at-most-two parallel items
here and gives directly checkable integer certificates.

If a directed u-to-v path has a(v)>=a(u)+2, reverse it. Only its endpoint
loads change, and the square-sum falls by 2(a(v)-a(u)-1)>=2. Starting from
any orientation this terminates, with at most m^2/2 reversals, because its
nonnegative integer initial energy is at most m^2. Each path search and
reversal is polynomial. This orientation is an ANALYSIS assignment, with
no obligation to follow the original directed graph.

For the terminal orientation let r(v)=max{a(w): v reaches w}, including
the zero-edge path. No improving path means a(v)<=r(v)<=a(v)+1. Set
z(v)=max(0,2r(v)-1). Along any oriented item u->v, r(u)>=r(v), so
z(u)>=z(v): the assigned head v minimizes z among its two endpoints.
For every vertex,

    a(v)^2 = z(v)a(v) - floor(z(v)^2/4).

Indeed z(v) is 2a(v)-1 or 2a(v)+1, except for the harmless a=r=0 case.
For ANY nonnegative integers x,z, x^2>=zx-floor(z^2/4). Consequently
every orientation and every nonnegative integer vector z satisfy

    sum_v a(v)^2 >= sum_{uv in B} min(z(u),z(v))
                    - sum_v floor(z(v)^2/4).

The constructed orientation/z attain equality. This proves exact global
optimality and the integer dual formula without assuming a generic
min-max theorem or treating a successful program as a proof.

The code implements both this primal/dual certificate and an independent
unit-capacity min-cost flow: each item chooses an endpoint; the kth slot
at a vertex costs 2k-1. Successive shortest residual augmentations use
integer reduced costs. Bellman--Ford checks the final residual graph has
no negative cycle. Small independent orientation enumeration checks both.

## 3. A sharper description of the remaining sufficient inequality

For a nonempty edge set define

    D(B) = max_{nonempty U subset V} |E(B[U])|^2 / |U|.

Set D=0 if there are no edges. All induced edge counts retain multiplicity.
For n>=2 and m>0, the following generic bounds hold:

    D(B) <= E*(B) <= (2 + H_{2n-3}/2) D(B),               (1)

where H_j=sum_{i=1}^j 1/i. These are routine consequences of the dual,
not a new fault-tolerant sparsification theorem.

Lower bound: in any orientation the indegrees restricted to U sum to at
least |E(B[U])|. Cauchy gives |E(B[U])|^2/|U| <= sum_{v in U}a(v)^2.

Upper bound: use the optimal z above and S_k={v:z(v)>=k}. Since B has
at most two edges per unordered vertex pair, a(v)<=2(n-1), so
0<=z(v)<=4n-5. Layer expansion of the dual gives exactly

    E*(B) = sum_{k=1}^{4n-5}
             ( |E(B[S_k])| - floor(k/2)|S_k| ).

The k=1 term is at most m<=2D: take U to be the at-most-2m nonisolated
vertices to obtain D>=m/2. For k>=2 put j=floor(k/2)>=1. With x=|S_k|,

    |E(B[S_k])|-j|S_k| <= sqrt(Dx)-jx <= D/(4j).

Each j appears at most twice, up to j=2n-3. Summing proves (1), including
empty S_k and negative terms. Empty graphs have E*=D=0 separately.

Thus ENERGY, up to an additional logarithm, has the following equivalent
SUFFICIENT kernel, now explicitly exposing the ambient budget:

    For EVERY critical (G,P) and EVERY nonempty U subset V(G),
    |E(G[U])|^2 <= C n(p+1)|U| log(n+2)^c.                [DENSITY: UNPROVED]

Unlike the refuted hereditary degeneracy assertion, its right side keeps
the FULL original n, including private selector vertices. It cannot be
replaced by |U|^2(p+1) without reviving that known obstruction. Taking
U=V shows why DENSITY suffices for the original edge-count bound, but
the converse from the original full-graph bound is NOT established.

The global active-three-cut-to-DENSITY implication remains the precise
unknown step. Neither convex orientation optimization nor the dual pays
the required n(p+1) budget; those calculations only reformulate it.

## 4. Exact finite evidence and limits

energy-test.py checks every orientation of every simple undirected graph
through five vertices (1100 graphs including n=0,1), and checks 100 seeded
instances with possible antiparallel items against independent min-cost
flow. Every computed optimum also has the integer dual equality above.

The fresh critical-graph screen considers all 4164 labelled loop-free
digraphs on n=2,3,4. For each edge it enumerates every outgoing cut of
size at most three and the required internal source/suffix routes. It
then finds a MINIMUM-cardinality demand set whose witnesses cover every
edge by increasing-cardinality exhaustive demand-subset search. This
optimizes the new ENERGY test, rather than replaying the old cut-equivalence
check. Such a minimum cover maximizes E*/[n(p+1)] for each fixed graph;
unreachable/reflexive padding cannot improve this ratio.

The exact maxima of E*/[n(p+1)] for n=2,3,4 are 1/3, 4/3 and 31/12.
The n=4 maximizing example has 11 directed edges, two demands and energy
31; it merely excludes small guessed constants, not any O() bound.
The code/results serialize its edges, demands and minimizing orientation.
No finite test proves ENERGY or DENSITY in unbounded n,p.

An independent deterministic checker directly enumerates all 67 failure
sets of size at most two for all 12 nonreflexive demands of that saved
n=4 graph. It verifies a critical witness for all 11 edges under the
reported two demands, and verifies no single demand forces all 11 edges.
It also recomputes energy by all 2048 orientations and min-cost flow.
Separately it checks (1) with exact fractions on all 1094 nonempty simple
undirected graphs with n=2..5. These are independent implementations in
this same worker context, not a fresh referee or independent-model review.

sharing-test.py examines a different possible falsifier: compressing the
private induced-matching selectors by identifying same-position internal
chain vertices periodically across matchings. It preserves separate source
and target endpoints, all core vertices, and simple input edges. Ternary
progression-free instances have (matching count,matching size) equal to
(19,4),(55,8),(163,16). At each size it tests the unmerged construction
and nine declared left/right/both sharing choices, stopping on the first
failed inherited witness. The three unmerged instances pass all 3124
specified core witnesses. All 27 sharing cases fail an inherited witness.
This is an OBSERVED FAILURE of these specified compression/witness pairs.
It is not a theorem excluding other sharing rules, and failure of one
inherited witness does not exclude another witness for the same edge.
The full ENERGY optima of the first two unmerged graphs are 646 and 4950;
the larger instance's uncomputed optimum is null, not zero.

## 5. Decision and unresolved kernel

No proof or counterexample resolves source.md. The primary literature
recheck retains the previously verified gap; the orientation machinery is
established prior work. No substantive independent innovation or STOC
assessment is claimed. The assigned third accumulated research pass is
the last authorized pass. Preserve these artifacts and PARK unresolved;
do not generate a claim.json, manuscript or PDF.

One specific future test, only if separately authorized after this exhausted
cap: prove or refute DENSITY using demand-active <=3-edge cuts, seeking
an induced set U with |E(G[U])|^2/[n(p+1)|U|] growing faster than every
fixed polylog, or a global charging proof. This retains all auxiliary
vertices in n and does not quietly narrow the full original question.
