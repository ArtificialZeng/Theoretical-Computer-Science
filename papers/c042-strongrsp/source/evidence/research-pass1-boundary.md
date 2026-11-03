# Research pass 1: vertex-block boundary oracle

Job: c042-strongrsp-research-c6b8438a850b. Original status: unresolved.
This is a local constructive lemma and proof record, not a publication candidate,
independent audit, or resolution of `source.md`.

## Exact contract

Let q>=1 and rho>0, with F=1+rho. States are (v,i,j), 0<=i,j<q.
For an original directed edge uv, the backwards action at v moves to u and adds
nonnegative integer increments (a,b) with fixed probabilities p_e(a,b), independent
of (i,j). Overflow of either clock pays F. The source pays rho before taking any
action at a nonoverflow state. Nontermination pays F. One may also voluntarily
increment either clock by one. For the original model these extra actions do not
improve the true value: the same physical actions can be simulated with fewer
used ticks; source success remains available, and overflow is only delayed.
The original value X is therefore coordinatewise nondecreasing in i,j and lies
in [rho,F]. This is the regularized failure value, including nontermination.
These statements apply to finite supported distributions with overflow tails,
and in particular to the truncated clock increments in the actual Poisson DP.

Select whole active VERTICES A, excluding s; all q^2 states of such a vertex are
active. Every other vertex is an immediate terminal with table B_v in [rho,F].
Assume X(v,i,j)<=B_v(i,j)<=alpha X(v,i,j). Source prices are exactly rho.
Replace B by its upper-orthant minimum

    C_v(i,j) = min {B_v(a,b): a>=i, b>=j, a,b<q}.

This takes O(q^2) operations per supplied vertex by a descending two-dimensional
minimum pass. Monotonicity of X gives X<=C<=B<=alpha X, and C is tick-monotone.
Explosion prices remain F and are not minimized into source prices.

## Algorithm

Process i and j in descending order, as in Section 4 of Ashvinkumar v2.
At layer (i,j), seed each active v with the smaller of its two already-computed
one-tick values (overflow means F). For every edge uv with v active and u inactive,
compute its full expected C/overflow value and use it as an additional seed.
Run a min-heap on active vertices only. When u is popped, fix Z(u,i,j), and relax
each edge uv whose head v is still in the heap using the actual update

    p_overflow F + sum_{a<q-i,b<q-j} p_e(a,b) Z(u,i+a,j+b).

Here inactive endpoint tables are C; all positive-increment terms are already
known. Store a chosen seed/action whenever a key strictly decreases. Zero ties
retain their earlier choice. The source is treated as an inactive exact terminal.
No inactive vertex is inserted into the heap. Self-loops cannot improve a
popped vertex and may be skipped.

## Correctness proof, including zero cycles

1. Initial tick seeds imply Z(u,i,j)<=Z(u,i+1,j) and Z(u,i,j)<=Z(u,i,j+1).
Descending layer induction gives comparison with EVERY higher tick state of the
same active u. Thus every candidate relaxed after popping u is a convex mixture
of values at least Z(u,i,j), including F. Candidate keys cannot be below the last
popped key. Heap removals are nondecreasing, exactly the causality used by the
source's Appendix A, now applied only to active predecessors.

2. The final Z satisfies every Bellman inequality Z(v,i,j)<=expected next Z for
every allowed edge/tick action. An edge from an inactive predecessor was seeded.
For an active predecessor popped before v, its candidate was relaxed; for one
popped after v, the candidate is at least its popped value, hence at least Z(v).
A self-loop also has candidate at least Z(v). Tick inequalities hold by seeding.
At terminals Z is their prescribed price. This establishes inequalities for all
actions, including edges ignored because their head had already been popped.

3. For ANY policy, iterate those inequalities for k transitions, paying F to
trajectories still active at time k. The resulting expected truncated payment
is at least the starting Z. Payments are bounded in [rho,F], and converge to the
actual terminal payment, or F on a nonterminating trajectory. Bounded convergence
gives Z<=the policy's expected payment. Taking infima gives Z<=Y, where Y is the
optimal stopped-system value. This avoids selecting a spurious least fixed point
on a closed zero-increment class.

4. The algorithm's selected pointer policy realizes Z. A selected edge to an
active predecessor strictly decreases that layer's pop rank if its increment is
zero; any positive increment increases i+j; a tick also increases i+j. Seeds
are terminal or tick actions. Thus no realized trajectory can take more than
(2q+1)(|A|+1) actions before termination (a loose bound suffices), and backwards
substitution gives its cost exactly Z. Hence Y<=Z. Together, Z=Y. In particular,
an isolated closed p00=1 class receives F via tick-to-overflow seeds, rather than
an arbitrary smaller algebraic fixed point.

5. The first-hit comparison applies to this very stopped control system. For
X<=Y, replace its first inactive terminal by a near-optimal full continuation;
prices C dominate X. For Y<=alpha X, stop a near-optimal full policy at its first
inactive visit. Its conditional continuation cost dominates X at the visited
state, and C<=alpha X; unchanged source/overflow/nontermination prices are
nonnegative and at most alpha times themselves. Taking limits of near-optimal
policies proves X<=Y<=alpha X, with one factor per trajectory, not per edge.
Voluntary ticks are part of both control systems for this comparison.

## Work and interface obligations

Let d_A be the total number of input adjacency incidences scanned at active
vertices, counting parallel edges separately. Keep incoming and outgoing lists
built once in O(m+n). Enumerate A and scan their incident edges only; obtain
boundary tables only for inactive predecessors encountered there. Each distinct
such predecessor can be charged to an incident edge, so no global inactive scan
is required. Orthant closure/table access costs O(q^2) per encountered endpoint.
If a boundary coordinate query costs H, this adds O((|A|+d_A)q^2 H).

There are q^2 heaps with |A| vertices; each edge update uses O(q^2) arithmetic
operations. A conservative bound is

    O((|A|+d_A) q^4 log(|A|+2) + (|A|+d_A) q^2 H)

and O((|A|+d_A)q^2) local space, apart from external table/coefficient storage.
Lazy timestamps or local dictionaries avoid O(n) array clearing per call.
Boundary prices need only be requested at encountered inactive predecessors.
There is no generic arbitrary affine-MDP claim: nonnegative clock increments,
whole-vertex activation, bounded failure prices and tick seeds are essential to
this proof. Arbitrary isolated active clock-state selection is NOT certified.

For rational input tables/coefficient encodings with L bits, this static solve
uses only comparisons, additions and multiplications, without linear-system
inversion. Its selected policy has polynomially bounded transition depth;
naive denominator growth remains polynomial in the finite supplied encoding,
n and q. This does not yet implement Poisson coefficient approximation or certify
bit growth of a complete recursive algorithm.

## Exact finite validation

Run `python3 evidence/check_boundary_oracle.py` from the project root.
`evidence/boundary-oracle-results.json` serializes 24 rational two-clock fixtures,
q=2 and 4 vertices, including a closed zero-resource SCC, a zero self-loop,
and a 1/1024 survival/exit mixture. All 192 active-vertex subsets were checked.
The heap solver agrees exactly with per-layer enumeration of stationary policies;
1152 active-state comparisons satisfy X<=Y<=9X/8 and tick monotonicity.
There were 8192 policy evaluations, 96 with closed nontermination. The reference
uses the preserved intake Fraction/Gaussian evaluator; it is algorithmically
different from the heap solver but is not an independent human/model audit.
The seeded rational increment laws are not claimed to be Poisson distributions.
Finite tests are supporting checks, not a proof of the universal lemma or runtime.

## Unresolved original and next test

The oracle does not remove numerical-aspect dependence by itself. Next establish
an offline divide-and-conquer implementation on a given monotone clock-event
sequence: prove first-hit depth-error propagation, envelope/tick compatibility,
active-vertex and incident-edge aggregate counts after block activation, and
avoid scanning all inactive vertices at every recursive node. GK25 Section 6
is an additive-distance precedent, not a citation that proves this extension.
Full event coverage, conservative finite-cost Poisson rounding, approximation
constants, all-target selection, zero-optimum cases, multigraph/query cost and
compact deterministic witnesses remain necessary before any original-scope claim.

## Held-out structured checks

After writing the q=2 oracle/statement, `evidence/check_boundary_oracle_heldout.py`
attacked it with six separately selected q=3 systems. These add deterministic
one/two-tick moves, parallel edges, certain overflow and a 1/2^40 mixture.
All 48 active-subset/boundary-mode combinations agree with exact enumeration:
432 active-state comparisons and 1440 policy evaluations, 126 with closed
nontermination. There are 41 strictly inflated active values, so the comparison
is tested beyond equality cases; 20 raw nonmonotone boundary tables are repaired
by orthant closure. See `evidence/boundary-oracle-heldout-results.json`.
No fixture or statement revision was needed after this held-out check.

## Bounded-pass disposition

The main scientific/validation test was complete at 03:36:30 UTC, before the
03:42:49.999991 deadline. Continue is recommended because this pass replaces the
previous unproved static kernel with a costed constructive argument and exact
checks, while a specific offline composition test remains and two accumulated
research passes remain available. The full frozen source is still unresolved.
Only Markdown/code/JSON evidence is produced. Current primary comparison and
its limits are recorded in `evidence/research-pass1-literature.md`.
