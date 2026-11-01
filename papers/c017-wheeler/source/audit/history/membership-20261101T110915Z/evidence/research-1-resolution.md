# Research pass 1: recursive convex blocks and a membership algorithm

Job: c017-wheeler-research-8ca2b0cef7a6. Research evidence; proposed full
resolution, subject to fresh correctness, novelty and significance review.
The original source.md is unchanged. No manuscript/PDF or acceptance is claimed.

## Statement

Membership in the exact current-v3 class specified in source.md and problem.md
is decidable for every finite accessible trimmed deterministic subsequential
transducer, including partial transitions, empty transition outputs, arbitrary
ordered finite alphabets, and terminal outputs (which the property ignores).
The procedure below also proves necessity of the first-test single-pump
certificate, and gives a total computable template bound. It does not use the
source's quotient or function-characterization theorems.

## 1. Ordered blocks and cancellation

First decide whether the nonempty regular reaching languages I_p are pairwise
separated in colex. Reverse their finite automata and test both possible strict
lex orders by the regular-language comparison procedure in section 2. If neither
state direction works for a pair, reject. Otherwise sort the states by this
strict total order. Every I_p is convex in D = union_q I_q.

For each q the following is an ORDERED DISJOINT decomposition of I_q:

    {epsilon}, if q=s; then all I_p a with delta(p,a)=q,
    sorted first by a and then by the state order of p.

Each indicated set is convex relative to I_q. For equal final letters this
follows from separation of the predecessor reaching languages; for unequal
letters it follows from colex. The empty word, when present, is first.
Every nonempty word belongs to exactly one block by determinism. On a block
I_p a, f_q(u a)=f_p(u) omega(p,a). More generally, whenever delta(p,z)=q,
I_p z is a convex subset of I_q, by iterating the one-letter assertion, and
f_q(u z)=f_p(u) omega(p,z).

Appending the SAME fixed word to two inputs preserves and reflects their
colex order, including strictness. The identical assertion holds for outputs,
even when that fixed word is empty. Thus every restriction to I_p z is an
order-isomorphic copy of f_p as regards all pairwise output comparisons.

## 2. Effective comparisons of independent regular ranges

Let O_p={f_p(u):u in I_p}. This is an effectively constructible regular
language: use the input graph as an NFA whose edges carry output words, start
at s, and accept at p; split word edges and retain epsilon edges. Forgetting
input labels loses correlations that are NOT needed here: comparisons below
always involve independently chosen words from distinct ordered blocks.
The range of block I_p z is O_p omega(p,z). A singleton input block has a
singleton output range.

For two epsilon-NFAs X,Y decide existence of x<lex y, x>lex y, or x=y as
follows. Compute epsilon closures and ordinary symbol transitions. Synchronize
on equal symbols until (i) one side can accept and the other has a nonempty
accepted continuation, or (ii) two unequal symbols can be read in the requested
order with accepting continuations on both sides. Reachability in this finite
product graph decides existence. Equality uses simultaneous acceptance after
a shared word. Reverse the NFAs to compare in colex. In particular universal
weak order X<=Y is the absence of an existential x>y. No intersection of
arbitrary rational relations is used. Empty ranges are harmless; the actual
blocks here have nonempty ranges by accessibility.

## 3. Global monotonicity of every state is decidable

For e in {+,-}, form local seed set S_e. A state q belongs to S_e exactly when
some earlier/later pair of its immediate blocks in section 1 has output ranges
violating weak order in direction e. Test all such pairs by section 2. Let
B_e be the set of states reachable in the INPUT GRAPH from S_e, including the
seeds themselves. Then

    f_q is globally nondecreasing iff q not in B_+;
    f_q is globally nonincreasing iff q not in B_-.

Proof: a local violating pair propagates along every path by common right
concatenation. Conversely, take any strict violating pair at q. If its two
words lie in different immediate blocks, q is a seed. Otherwise both are
nonempty and lie in one I_p a; delete their common final letter. The shorter
pair is still violating at p. Repeating terminates because word lengths
strictly decrease, eventually at a seed. The deleted letters form a path from
that seed to q. This proves both directions and avoids an unsupported
fixed-point choice. Write M(q) for the disjunction of the two global flags.

A function between total orders is globally monotone iff it has no strict
peak/valley triple. For completeness, if both a rising pair and a falling pair
exist, sort their at most four distinct arguments and remove consecutive
repetitions in the VALUE sequence. Its successive signs contain both signs,
so two consecutive opposite signs give a strict peak or valley. Therefore
failure of M(q) has an effectively enumerable finite strict-turn witness.
The same observation applies to any explicitly given restriction below.

A strict-turn interval cannot lie in one weakly monotone convex piece. If
there are infinitely many strictly separated such intervals, every interval
requires a distinct partition boundary: in an ordered k-piece partition each
boundary can split at most one of these intervals. Consequently an infinite
separated family rules out every finite partition, for increasing or decreasing
interval direction. This is the only packing implication used below.

## 4. Branching strongly connected components

Consider SCCs of the ordinary labeled input graph, counting distinct labeled
edges. A cyclic SCC that is not a directed simple cycle has a vertex r with
two internal outgoing edges. Their labels differ by determinism. Return paths
inside the SCC complete them to nonempty loop words u,v at r with distinct
first letters. Hence uv != vu. The infinite words rev(u)^omega and
rev(v)^omega differ: equality would imply rev(u)rev(v)=rev(v)rev(u), by the
period-shift argument, contradicting uv != vu. Effectively choose k such that
A=u^k and B=v^k are suffix-incomparable: compare their reversed finite powers
until their first mismatch occurs before both words end. This search terminates.

If any state q in this SCC fails M, append a path from q to r to obtain a
strict-turn triple alpha_1<alpha_2<alpha_3 at r. For n>=0 set

    U_i(n)=alpha_i A B^n.

All words reach r, and all strict output turn signs persist by common suffix
cancellation. The suffix cylinders of A B^n are pairwise disjoint and ordered
in a fixed direction: after the common reversed B^n, rev(A) and rev(B) have
the same fixed first mismatch. This proves the exact interval-separation
condition of first-test.md, in one of its two directions. Thus f_r cannot
have a finite convex monotone partition.

Conversely, if every state in this SCC satisfies M, every state there already
has a one-piece partition. Since monotonicity propagates backwards along
input paths, it is enough to test a representative, but testing all is valid.

## 5. Simple-cycle SCCs: the two annular sides

Let C be an SCC which is a directed simple cycle (a single self-loop counts).
Choose a state q in C and let c be the nonempty word read in one full traversal
from q back to q; let b=omega(q,c). By recursively taking the unique internal
predecessor block for |c| steps in section 1, obtain an effective finite ordered
list of blocks and the decomposition

    I_q = L  disjoint-union  I_q c  disjoint-union  R,    L<I_q c<R.

Each block in L,R is either a singleton word arising from the initial state,
or I_p z for p OUTSIDE C and an explicit path z of length at most |C| entering
C and ending at q. This is a finite construction: at each step retain the
internal child, append the accumulated suffix to all other children, and put
those children on its left or right in their known order. There are no other
internal children because the SCC is a simple cycle. L and R are each convex
in I_q and may be empty. Their images under appending c are similarly ordered.

Write L_n=L c^n and R_n=R c^n. Iterating the decomposition gives

    I_q = (union_{n>=0} L_n) disjoint-union (union_{n>=0} R_n).

There is no leftover finite word, because a word in every I_q c^n would have
length at least n|c| for all n. The L_n are ordered increasingly by n, the
R_n decreasingly; every L_n precedes every R_m. Each L_n,R_n is convex.
The two unions are convex relative to I_q.

**Exact test:** f_q is piecewise monotone iff BOTH restrictions

    f_q on L union Lc,       f_q on Rc union R

are each globally weakly monotone, with independently chosen directions.
The empty restriction passes in either direction.

Necessity: if one restriction is not globally monotone, it has a strict turn
v_1<v_2<v_3. Append c^(2n) to this triple. Its members occupy levels 2n and/or
2n+1 on just that side, so the intervals for successive n are strictly
separated (increasing on L, decreasing on R). Output turn signs persist by
appending b^(2n). This is a first-test certificate with x_i=v_i, y_i=c^2,
z_i=epsilon. It contradicts a finite convex monotone partition.

Sufficiency: if L union Lc is monotone in direction e, appending c^n shows
that L_n union L_(n+1) is monotone in the SAME direction for every n.
Transitivity, inserting an arbitrary point in each intervening nonempty level,
shows monotonicity on the whole left union. If L is empty there is nothing to
check. Apply the same argument on the right in its reversed level order,
using the direction of Rc union R. The two unions therefore give at most two
nonempty convex monotone pieces for I_q. No regularity of partition endpoints
is presumed; these two particular pieces are explicitly regular unions.

The exact test is effective without deciding any new correlated output relation.
Expand each restriction into its finite ordered list of singleton blocks and
blocks I_p z (the second copy appends c to z). A direction e works precisely
when every non-singleton block's predecessor p has global flag e from section 3
and every pair of earlier/later blocks has ranges in weak order e from section 2.
If a block fails its global flag, this restriction really is nonmonotone in
that direction by the order-isomorphic-copy lemma. Hence the test is exact.
All states r in C inherit piecewise monotonicity from q by appending a path
r->q and restricting q's finite partition. Alternatively run the test for each r.

## 6. Complete terminating algorithm

1. Decide total input order; reject if it fails.
2. Construct output-range NFAs and the two global monotonicity flags for all states.
3. Compute SCCs. For every cyclic non-simple SCC require M at all its states.
   For every simple-cycle SCC run the two-side test at a representative.
   Reject if any requirement fails; otherwise accept.

All rejection witnesses above prove failure of the ORIGINAL property. If every
cyclic component passes, its states have finite partitions by sections 4 and 5.
The remaining SCCs are loop-free singleton vertices. In a topological order,
the immediate-block decomposition and the already finite predecessor partitions
give a finite convex monotone partition at each such vertex. A singleton epsilon
block contributes at most one piece. Thus acceptance proves the original property
at EVERY state. Each algorithmic step uses finite graph constructions and
finite-automaton reachability and terminates. Trimming, alphabet degeneracies,
partial transitions and erasure are respected. Terminal outputs are unused.

## 7. First-test necessity and a computable template bound

For every input-ordered machine rejected by step 3, sections 4/5 give an exact
single-pump disjoint-turn certificate of first-test.md, with a COMMON loop
pump for the three words. The needed base strict turn can be found by enumerating
finite words in the specified state or regular two-level restriction: the
preceding rejection proof guarantees termination. Its output and input orders
are evaluated exactly. The branching construction's finite k search terminates
by the proved mismatch. Thus run the membership decision first, return B(T)=0
on acceptance, and on rejection compute this certificate and let B(T) be the
maximum length of its nine template words. On input-order failure return 0.
Return 0 also on malformed descriptions or those outside the promised trimmed
input model, which are decidable syntactic/graph conditions. This defines a
TOTAL computable B on descriptions, without a circular appeal to
certificate necessity: the independent SCC algorithm terminated before the
witness search, whose existence was proved constructively. No useful numerical
or optimal bound on B is claimed. The earlier fixed-certificate Presburger
verifier supplies a separate universal-n verification method if desired.

## Current proof status and adverse checks

This is a proposed complete argument, not a fresh referee verdict. The auxiliary
pair-component and fixed-verifier arguments were checked; the former is valid
but is not needed here. Independent unbounded prefix-output ranges are handled
only as independent REGULAR ranges of distinct blocks, never as unrestricted
rational-relation intersections. The nested-turn positive control passes because
each annular side is monotone even though turns straddle the persistent central
cut. The obsolete 'some cyclic turn' shortcut is explicitly not used.

The finite constructions and adversarial controls have now been executed;
sections 8/9 and research-1-adversarial.md record their exact scope. Primary-source
comparison is in research-1-literature.md. No mathematical gap is currently
identified by the researcher. The full-scope positive resolution is proposed as
a candidate for the actual fresh referee, who must independently assess proof,
novelty and significance. No acceptance or publication artifact is authorized here.

## 8. A conservative polynomial upper bound

Let S>=2 be the total explicit encoding size, enlarged if needed to count all
states, transitions, input/output alphabet symbols and every output character.
Let n<=S, m<=S, and M<=S be respectively the state count, transition count and
maximum edge-output length. Output-range NFAs have O(S) states and edges.
There are at most m+1 immediate blocks in total over all states. In one chosen
representative per simple-cycle component the annular lists contain each external
incoming edge to that component once, plus at most one initial singleton. Thus
the total number of annular blocks over these representatives is at most m+1.
Their doubled lists have O(S) blocks. Each appended path uses at most two
traversals of a simple cycle, so has input length <=2n and output length <=2nM.
All range NFAs actually compared have O(S^2) states and edges. There are O(S^2)
range comparisons for seeds and annular tests combined, plus O(n^2) comparisons
of O(n)-state reversed input-language automata to determine input order.

Here is one explicit deliberately loose implementation bound. For NFAs with
at most K states/edges, epsilon closure and elimination take O(|Gamma| K^4)
operations by enumerating closures, edges and targets. The comparison product
has K^2 vertices; enumerate equal-symbol target pairs and unequal-symbol live
transitions in O((|Gamma|+1)^2 K^4) operations. Its accepting/positive-continuation
predicates are finite reverse reachability. With K=O(S^2), |Gamma|<=S, each
comparison takes O(S^10) elementary operations, and O(S^2) comparisons take
O(S^12). Finite graph bookkeeping is smaller. If symbol identifiers are arbitrary
bit strings, their comparison costs at most S bit operations, giving the equally
safe bound O(S^13) BIT operations under this direct encoding and implementation.
No optimality is asserted. No universal Presburger solver is needed in this
algorithm. The witness-enumeration construction of B(T) is separate; this bound
is for the membership decision, not for enumerating pump witnesses.

## 9. Executed controls

`evidence/check_membership.py` implements regular-language sign comparison,
seed propagation, SCC classification, annular expansion and the exact decision.
`evidence/membership-check.json` records the executed finite tests. All 544
accessible input-ordered binary partial transducers through two states, with
all defined-edge output choices in {epsilon,0,1}, were checked; 600 seeded
3/4/5-state input-ordered machines with variable-length/erasing outputs were
also checked. All states were made final, which supplies valid trimmed inputs
without changing the tested property. Independently sorted finite word outputs
and an interval-partition DP checked the global-flag implications and all
accepted finite piece-count bounds (word lengths 7 and 8, respectively).
Eight named controls include identity, all erasing, ordered variable length,
complement, length coding, mixed erasure, unary and the nested-turn positive
control. No test failure occurred. These finite observations do not prove the
infinite theorem, nonmembership, certificate necessity, or novelty; those claims
rest on the mathematical argument above and still require fresh review.
