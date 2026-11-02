# Research proof packet: arena-independent memory for pure reachability SPEs

Proposer job: `c022-spe-memory-research-5979be48ad66` (research pass 1).
This is a proposed resolution for fresh mathematical review, not acceptance,
a manuscript, or an assertion of external peer review.

## Exact theorem and original scope

Let n >= 1. Let (V,E) be any set-sized directed arena without dead ends,
with an initial vertex v0 and an ownership map o:V->{1,...,n}. No finiteness,
countability or branching bound is assumed. Player i's payoff is 1 iff the
play ever visits T_i, for arbitrary subsets T_i of V. Strategies are pure,
and payoffs in a subgame include targets visited in its preceding history.

**Proposed theorem.** If sigma is any pure SPE from v0 with payoff set p0,
there is a pure SPE tau from v0 with exactly the same payoff set p0 such
that every player's strategy is encoded by a vertex-update machine with
at most n*3^n states. All players can share the same memory update and
initial state. Thus F(n)=n*3^n answers the immutable source.md question
positively, for every required subset S, including the empty subset.

The theorem preserves an exact payoff, which is stronger than preserving
only required winners. It assumes an SPE exists; it makes no additional
claim of unconditional SPE existence on arbitrary infinite arenas.

## Notation and finite payoff labels

Write N={1,...,n}, t(v)={i:v in T_i}, and W(h)=the union of t(u) over all
vertices of a nonempty legal history h from v0. W(h) includes its last
vertex. Write x(h)=(last(h),W(h)). Let X={x(h):h is a legal history from v0}.
For x=(v,W) in X and w in Succ(v), its augmented successor is

    y=(w,W union t(w)).

It belongs to X. An augmented edge always refers to an actual arena edge.
For each legal history h, let p_sigma(h) be the set of players whose
target is visited in the whole history h followed by the sigma-continuation
from h (with the boundary vertex written only once). Define

    P(x)={p_sigma(h): h is legal from v0 and x(h)=x}.

Since the assumed sigma is defined at every legal history, P(x) is nonempty.
It is a finite subset of 2^N, even when X and the set of histories are
infinite. Every p in P(v,W) contains W. No algorithm for computing P is
assumed, and no occurrence h is stored in memory.

## Lemma 1: local credibility of labels

For every x=(v,W) in X, every p in P(x), every successor y=(w,W union t(w)),
and i=o(v), there exists q in P(y) with q_i <= p_i. Here q_i denotes the
indicator of membership in q.

**Proof.** Choose a history h ending at v that witnesses p in P(x).
After the legal history hw the original profile has some full payoff
q=p_sigma(hw), which belongs to P(y). If w is the move prescribed by
sigma at h, then q=p. Otherwise the strategy that moves once from v to w
and then follows sigma has payoff q_i in the subgame after h. Since sigma
is an SPE, this one-shot change cannot improve p_i, so q_i <= p_i.
This uses subgame perfection at h, including when h is inconsistent with
sigma. The argument works independently for every successor. QED.

## Lemma 2: a uniform progress selector for each label

For p subset N let X_p={x in X:p in P(x)}. Every x in X_p has an infinite
path entirely in X_p whose accumulating visited set eventually equals p.

**Proof.** Choose h realizing p at x and follow the original sigma from h.
Each extended history along that continuation still has full payoff p,
so all its augmented states belong to X_p. There are finitely many players.
Every member of p not already in W(h) reaches its target at some finite
time. The maximum of these finitely many times is finite; if the set is
empty the maximum is taken as zero. At that time the visited set equals p.
No target outside p is encountered, by the definition of full payoff. QED.

Let C_p={(v,W) in X_p:W=p}. Define d_p(x) to be the minimum number of edges
of a finite path within X_p from x to C_p. Lemma 2 says that d_p(x) is a
finite natural number for every x in X_p. This minimum is over a nonempty
set of natural numbers, and needs no finite-branching or compactness
assumption. No uniform bound on d_p is asserted or required.

For every x=(v,W) in X_p fix an actual successor vertex f_p(x) such that
its augmented successor y belongs to X_p and

    d_p(y)=d_p(x)-1, if d_p(x)>0.

Such a successor exists by a shortest path to C_p. If d_p(x)=0, choose any
successor whose augmented state belongs to X_p; Lemma 2 supplies one.
When d_p(x)=0, W=p and every successor in X_p still has visited set p,
because its visited set both contains W and is contained in its label p.
Thus it still has rank zero.

As usual for arbitrary set-sized arenas, choices of successors may use
set-theoretic choice. They are fixed vertex-dependent next-move tables,
which the source memory model explicitly permits. Following f_p at each
augmented state realizes exactly the full payoff p from every x in X_p:
the natural-number rank decreases to zero in finitely many steps, after
which no new target outside p can be visited. Neither d_p nor its value
is stored in a player's memory.

## Explicit vertex-update machines

Use the common memory set

    M={(A,p,j): A subset p subset N, j in N},

which has n*3^n states: for each player the possibilities are outside p,
in p but outside A, or in A. Here A records the targets visited strictly
BEFORE the current vertex, p is an incoming promise, and j records the
owner of the previous processed vertex, whether or not a deviation occurred.
There is no last-vertex register and no stored expected successor. All players
apply the same update to observed vertices, so their simulated memory stays
synchronized on every legal history, including deviating histories.

Fix a total order on 2^N. For any reachable augmented state x and j in N,
let b_j(x) be the first label q in P(x) minimizing q_j. Given m=(A,p,j)
and a vertex v, form

    B=A union t(v),    x=(v,B),
    R(m,v)=p,          if p in P(x),
    R(m,v)=b_j(x),     otherwise.

These definitions are used when x belongs to X. Set r=R(m,v). Define

    up(m,v)      =(B,r,o(v)),
    next_i(m,v)  =f_r(x),              for v owned by i,
    m0           =(empty,p0,1).

Both up and next_i use the SAME incoming m and current vertex v. In
particular next_i is evaluated before up has processed v: at a history
h v the strategy is exactly next_i(up*(m0,h),v), as in source.md.
The update sees no successor. R belongs to P(x), so B subset r and the
updated state belongs to M. If x is outside X, define up arbitrarily in M
and next_i to be any legal successor; these cases are unreachable after
legal histories from the initialized machine. This makes both functions
total on their prescribed domains.

## Lemma 3: correctness at every legal history

After processing a legal prefix h (possibly empty), the A component of
the memory is exactly the union of target bits along h. At the current
vertex v, the augmented state x=(v,A union t(v)) is therefore in X, and
the normalized promise r=R(m,v) belongs to P(x).

**Proof.** Initially A is empty. If the assertion holds before v, the
formula for up stores exactly A union t(v); normalization is defined at
x in X and outputs a member of P(x). Induction applies along EVERY legal
successor, with no assumption that anyone follows tau. QED.

Suppose the current normalized promise is r. If the prescribed move
f_r(x) is taken, its successor y belongs to X_r, so r belongs to P(y).
At y the incoming promise is r, and normalization retains r regardless
of the stored owner. Repeating this reasoning shows that following the
profile after any legal history keeps the promise r and follows the
selector f_r. Lemma 2 therefore shows that its full payoff, including
that history, is exactly r. This proves credibility of every constructed
continuation, not only of the outcome from v0.

## Lemma 4: arbitrary unilateral deviations cannot improve

Fix ANY legal history H from v0 and a player i. Let r be its normalized
promise. If i belongs to r, the prescribed full payoff is already 1 and
cannot improve. Suppose i does not belong to r, so the prescribed payoff
is 0. Consider any unilateral deviating strategy of i, with no memory,
length or finiteness restriction.

Along the resulting continuation, maintain that the current normalized
promise excludes i. If the current vertex belongs to another player,
that player takes the prescribed move; Lemma 3 retains the current
promise at the next state. If the current vertex belongs to i, let the
arbitrarily selected successor have augmented state y. The update at the
current vertex stored (B,r,i). If r is in P(y), the next normalization
retains r and still excludes i. If r is not in P(y), the next promise is
b_i(y). Lemma 1, applied to the current x and r, supplies a label q in
P(y) with q_i<=r_i=0. Thus b_i(y) also excludes i.

Induction proves the invariant at every finite position of the deviation.
Every normalized promise contains all target bits already visited
(Lemma 3 and the definition of P). Hence T_i has not been visited at any
finite position. The deviation has payoff 0 and cannot improve.
This covers infinitely many deviations as well as finite or one-shot
ones, without a limiting or branching argument. QED.

## Conclusion, dependencies and gap list

Lemma 4 establishes that tau is a Nash equilibrium after every legal
history H, which is exactly SPE. Initially p0 belongs to
P(v0,t(v0)), witnessed by the initial history v0, so normalization keeps
p0. Lemma 3 gives initial payoff exactly p0. The memory bound is n*3^n
and is independent of all arena, edge, target and branching cardinalities.
For any required set S contained in p0, this same equilibrium satisfies S.
This proves the proposed theorem and the full implication in source.md.

Dependencies are the definitions of pure SPE and vertex-update memory,
finiteness of the number of players, elementary finite target-witness
reasoning, the well-ordering of natural numbers, and ordinary set-theoretic
choice of legal selectors. The argument does not invoke a finite-arena
existence theorem, an NE punishment theorem, automata determinization,
randomization, or an edge-to-vertex memory conversion.

Researcher's known mathematical gap list: **empty**. This is the scope
proposed for an independent fresh referee, which must still test correctness,
current novelty and substantive value. No mathematical acceptance is claimed.

No optimality of n*3^n, algorithm for infinite tables, arbitrary omega-regular
extension, quantitative reachability extension, or unconditional infinite-arena
SPE existence is asserted. These are not needed for the immutable question.
