# Full-scope stronger deterministic reporting theorem: proof dossier

Research job c031-detlis-research-bf90b0105355, pass 2, 2026-11-02 UTC.
This is mathematical evidence submitted for fresh review, not a manuscript,
an acceptance, or a venue assessment. The unchanged original is source.md;
problem.md gives its precise interpretation. Earlier files are preserved.

**Proposed theorem.** There is a uniform deterministic algorithm which, for
every n>=1 real sequence and every m>=0 index/value rectangles, reports a
longest strictly increasing subsequence in each rectangle in

    O((n+m) n^(2/3) log^30(n+m+2)) + O(K)

comparison and word operations, with K the total output length. The exponent
30 is a conservative fixed constant. Original-value comparisons have unit
cost; word width is Theta(log(n+m+2)). Larger constant-factor bit lengths are
implemented using a constant number of words and charged polylogarithmic
arithmetic. No real-arithmetic or probability oracle is assumed. All ties,
overlaps, sparse/dense inputs, empty answers and optimum lengths are covered.
Thus epsilon=1/3 resolves the immutable existence assertion in its full scope.

The proposed delta over the earlier scientific proof is a relative-frequency
compression with certified fixed-point conditional expectations, represented
by compressed canonical source trees. This improves the sample and charged
compression bounds together. The generic sampling principles are prior art.

## 1. Canonical chain family and exact local backgrounds

Let p_i=(i,a_i). Put i<j in the dominance order exactly when i<j and a_i<a_j.
For comparable endpoints u,v, let P(u,v) be a longest chain from u to v,
with ties resolved by lexicographically smallest index sequence. Include
P(u,u) and the empty chain. Write F for this global family.

If x,y lie on P(u,v), its x-to-y subchain is P(x,y). Indeed, replacement by
a longer subchain increases the entire length; replacement by an equally
long lexicographically smaller subchain improves its tie order. Both
replacements remain feasible because inserted points lie strictly between
the bounding endpoints in each coordinate. Thus either contradicts the
choice of P(u,v). This proves consistency, rather than assuming arbitrary
independent tie choices have it.

Let S be a multiset of s selected original points, possibly with dummy
occurrences belonging to no path. Every nonempty trace F intersect S is
the trace of P(x,y) where x,y are its first and last distinct selected
vertices. This follows from consistency; repeated occurrences of a vertex
are either all included or all excluded. Consequently at most d^2 nonempty
traces suffice, where d<=s is the number of distinct real selected vertices.
Duplicate descriptors are harmless. Empty traces can be omitted because
every subsequent draw also has zero membership in them.

For completeness this ordered path system has VC-dimension at most two:
if three index-ordered points x,y,z all lie on one canonical path, then
P(x,z) contains y, and consistency forces every canonical path containing
x,z to contain y. Thus {x,z} and {x,y,z} cannot both be traces. If no path
contains the triple it also cannot be shattered. This is a standard path-
system observation; the proof does not infer an efficient oracle from it.

Suppose all selected real points lie in an ORIGINAL contiguous index interval
I. A path between any two of them lies wholly in I. The feasible paths and
lexicographic tie order computed using all original points of I are therefore
exactly the global ones. The local source computations below use this full
background. They do not recompute paths on S alone. The distinction matters:
for values (0,3,1,2,4), P(1,5)=(1,3,4,5) has trace {1,5} on {1,2,5}; the
selected-only canonical 1-to-5 path is instead (1,2,5).

For every rectangle with a nonempty optimum, take the endpoints u,v of one
optimum. P(u,v) lies in their coordinate bounding rectangle and hence in
the query, and is at least as long as that optimum. It is therefore itself
optimal. Hitting every long member of F suffices for every long query.

## 2. Computing the actual compressed source trees

For one selected source u, sweep original indices in I from u to its right.
Coordinate-compress the ORIGINAL real values, giving equal values equal
ranks. A Fenwick maximum structure queries ranks strictly below the current
rank. Initialize only u as reachable. The key of a predecessor is its
maximum source-path length followed by lexicographically smallest source
path. Append the current vertex to the attaining predecessor and update
the Fenwick structure. Induction proves this computes exactly P(u,v) for
every reachable v: all feasible predecessor choices are considered, and
appending a common endpoint preserves the order of equal-length paths.

These predecessor pointers form a rooted tree whose root-to-v path is
P(u,v). Binary lifting is built on insertion, since a parent has smaller
original index. For equal-depth distinct paths, find the LCA and compare
the original indices of the children immediately below it. Those children
are the first unequal entries of the two paths. An O(log(n+2)) LCA/lifting
comparison therefore implements the tie rule without path-length scans,
hashes, or huge lexicographic integers. Fenwick operations take O(log n)
comparisons. Sorting, initialization, lifting and all sweeps cost
O(|I| log^2(n+2)) per source. Storage is interval-sized, not global-n-sized.
Unreachable points and padded dummies are not inserted.

Mark selected distinct vertices. In increasing original index order store
at every reachable original vertex its nearest selected ancestor, including
itself when selected. This is one O(|I|) pass. For each selected reachable
v, its parent in the compressed selected tree is the nearest selected
ancestor of its original parent (or absent for the root u). This connects
each selected vertex to its closest selected predecessor on P(u,v), so
root-to-v paths in the compressed tree are EXACTLY the selected traces.
The compressed tree contains at most d vertices. Keep one such tree for
each selected source. Retain one descriptor (u,v) for every reachable pair,
including u=v. There are M<=d^2<=4k^2 descriptors when s=2k.

Assign each selected distinct vertex x its occurrence multiplicity w_x in S.
A forward traversal computes a_(u,v), the input occurrence count on the
compressed root-to-v path, by adding w_v to its parent's count. Euler
entry/exit labels give constant-time membership: x lies on this path iff
x is reachable in this source tree and is an ancestor of v. A dummy is
never a member. Constructing all these trees, counts and labels costs

    O(|I|s log^2(n+2) + s^2)

operations and O(|I|log(n+2)+s^2) working words when original source trees
are discarded one at a time. Selected-point rank arrays have size |I|;
the d-by-d compressed arrays have size O(s^2). No explicit O(s)-bit vector
per trace is required. Dummies-only S is recognized immediately.

## 3. Relative compression and a finite-word derandomization

Take s=2k input occurrences and the M nonempty trace descriptors. Let p in
(0,1] and eta in (0,1]. For a trace with a occurrences put u=a/(2k).
Call k independent uniform occurrence draws bad for this trace when

    |observed frequency - u| > eta(p+u).                (1)

Here u is always the INPUT representative frequency. It is not the unknown
original interval frequency. For x>0 the Bernoulli Bernstein bound gives

    Pr[|observed frequency-u|>x]
       <= 2 exp(-k x^2/(2u+2x/3)).                      (2)

A short derivation: for centered Bernoulli X with mean u,
log E exp(lambda(X-u)) <= u(exp(lambda)-1-lambda)
<= u lambda^2/(2(1-lambda/3)) for 0<=lambda<3. Markov's inequality with
lambda=x/(u+x/3) proves the upper bound. The lower bound follows from
exp(-lambda)-1+lambda<=lambda^2/2, giving the stronger denominator 2u;
for x>u that tail is empty. The means u=0,1 are deterministic and may be
handled directly. With x=eta(p+u), the denominator in (2) is at most
(8/3)(p+u). Thus the probability is at most

    2 exp(-k eta^2 p/3).

In particular the initial expected number of bad traces is at most
2M exp(-k eta^2 p/3). Parameters below make this <=1/8 analytically;
the implementation never evaluates this exponential.

For each a in [0,2k], remaining draws h, and current count c with c+h<=k,
let q[a,h,c] be the exact conditional bad probability. Its h=0 value is
the 0/1 indicator in (1), and conditioning gives

    q[a,h,c] = (a q[a,h-1,c+1]+(2k-a) q[a,h-1,c])/(2k).

Choose a power of two D>=64 M k^2 and compute the INTEGER table

    U[a,0,c] = D * bad_indicator(a,c),
    U[a,h,c] = ceil((a U[a,h-1,c+1]+(2k-a) U[a,h-1,c])/(2k)).

An induction, using convex averaging and less than one unit of upward
rounding at each recurrence, proves

    q[a,h,c] <= U[a,h,c]/D <= q[a,h,c]+h/D.              (3)

At a prefix with h draws left, keep its count c_F for each trace. The
integer score of candidate occurrence x is

    V_x = sum_F U[a_F,h-1,c_F+1_F(x)].                  (4)

Choose a minimum-score occurrence, ties by original occurrence position,
and update the counts. If Q is the true current sum of conditional bad
probabilities, the mean of the true next sums over the 2k occurrences is
exactly Q, counting multiplicities. Equation (3) bounds the mean next
upper scores divided by D by Q+M(h-1)/D. The minimum is at most that mean;
the true chosen next sum is at most its upper score. Hence each draw
increases true potential by at most M(h-1)/D, even though exact monotonicity
is not asserted. Over all k draws the total increase is at most

    M k(k-1)/(2D) <= 1/128.

Starting at <=1/8, the terminal potential is <1. At termination it is the
integer number of bad traces, hence zero. This proves the deterministic
compression for every S under the stated analytic initial bound. M=0 is
handled by returning k dummy occurrences, without using D or a table.

## 4. Aggregating EVERY score, including signed differences

Directly evaluating (4) for every occurrence would be unnecessarily costly.
Put b_F=U[a_F,h-1,c_F], delta_F=U[a_F,h-1,c_F+1]-b_F and B=sum_F b_F.
Then V_x=B+sum_(F containing x) delta_F. For each source tree initialize
an accumulator at each selected vertex. For every trace (u,v), add its
delta at target v. Traverse vertices from leaves to root, adding each
accumulator to its compressed parent. The resulting accumulator at x is
the sum of deltas over descendant targets, precisely the root-to-target
traces containing x. Add these accumulators at x over all source trees.
The score of a real candidate is B plus its accumulated sum; the score
of a dummy is B. Repeated occurrences have the same score but retain
their multiplicity in the averaging proof and in the output multiset.

This computes exactly (4) for every occurrence, not an approximation to
its value. Negative deltas require signed addition only. All descriptors,
all tree traversals, all candidates and all count updates using Euler
ancestry take O(M+d^2+s)=O(k^2) operations per draw. With k draws their
cost is O(k^3). The table contains O(k^3) entries, including ALL a values,
and has the same operation bound before the polylogarithmic arithmetic
factor. There is no exact-binomial table in the production choices.

When k<N, M<4N^2, D can be chosen below max(2,128 M k^2), so log D=O(log N).
Equation (3) gives 0<=U<=D+k. Recurrence products have O(log N) bits up
to fixed factors; all signed sums have magnitude O(M(D+k)). They therefore
use a constant number of Theta(log(n+m+2))-bit words. Ceil division by
2k is a shift when k is a power of two; ordinary polylogarithmic arithmetic
would also suffice. All table initialization, entries, candidate arrays,
signed sums, counters, comparisons and updates are charged. The complete
per-node bound is

    O(|I| k log^2(n+2) + k^3 polylog(n+2)).             (5)

The tree setup is additional to compression, as displayed; it is not
silently absorbed by a k-only bound at a large original interval.

## 5. Equal-original-size merge/reduce and the stronger parameters

For n>=2 set N to the next power of two >=n, pad with N-n dummies, and put

    t = least integer with t^3>=n^2,
    L = ceil(log2(N+2)), H=L+1,
    p = t/N, eta=1/(16H),
    k = next power of two >= 512 p^(-1) eta^(-2) L.     (6)

These are exact integer/rational operations. Compute t by binary search
with cube comparisons; no real root instruction is used. We have
t=Theta(n^(2/3)) and k=O(n^(1/3) log^3(n+2)), including when k>=N.
All parameter calculations use O(log n) bits up to fixed factors.
For these parameters the base bad indicator is the integer comparison
16 H N |2c-a| > 2k t + aN, so its construction also has that bit bound.

If k>=N, take all real points and skip compression; the charged fallback
is considered below. Otherwise k divides N. Partition the original padded
index order into k-blocks, initially represented exactly by their occurrences.
At a merge, join the representatives of adjacent equal-size ORIGINAL
intervals, producing 2k occurrences, and compress using their complete
original parent interval I. Both retained children have k representatives
but the same original size; this equality is essential to averaging.

At every node M<=4k^2<4N^2 and k eta^2 p>=512L. Since 2^L>=N+2 and
exp(L)>2^L, the bound 8N^2 exp(-(512/3)L) is <1/8 for N>=2. Thus the
initial potential condition of Section 3 holds uniformly at every merge,
independently of its input representatives and their multiplicities.

Fix ANY F in the global canonical family. Let phi denote its fraction
among all original padded positions of a node, and r its representative
frequency. After j compression levels the simultaneous invariant is

    |r-phi| <= E_j (phi+p), E_j=(1+eta)^j-1.            (7)

The bottom is exact. At a merge the two original intervals have equal
length and their samples equal cardinality, so both original and input
sample frequencies average the corresponding children. If u is the joined
sample frequency, |u-phi|<=E_j(phi+p). The trace oracle covers the trace
of this global F, or it is empty and preserved exactly. Compression adds
at most eta(p+u). Since p+u<=(1+E_j)(p+phi), the resulting error is at most
[E_j+eta(1+E_j)](p+phi)=E_(j+1)(p+phi). This proves (7) for EVERY F.

There are at most H levels. Expanding the binomial and bounding each
coefficient by H^i gives (1+1/(16H))^H < sum_(i>=0)(1/16)^i=16/15.
Hence E_H<1/15. At the root every F of length >=t has phi>=p and
r>=phi-(phi+p)/15>=13phi/15>0. Only now discard dummies and deduplicate.
The resulting R has at most k real points and hits every long canonical
chain, therefore a canonical optimum in every long rectangle.

At each level original parent intervals are disjoint. Thus the first term
in (5) sums to O(Nk log^2 n) per level, and to O(Nk log^3 n) in total.
The number of merge nodes is N/k-1<N/k. The k^3 table/aggregation costs
sum to O(Nk^2 polylog n). There is no global-n scan per small merge.
Total net construction time is therefore

    O(Nk log^3(n+2)+Nk^2 polylog(n+2))
       = O(n^(5/3) polylog(n+2)).                     (8)

Explicitly, a factor log^2 for constant-word arithmetic more than suffices,
so (8) is bounded by O(n^(5/3) log^8(n+2)). Working memory is bounded by
these time charges. Uniform asymptotics do not assert practical constants.

## 6. Short-LIS answers: exact below t and feasible at every length

The following reconstructs the source's deterministic truncated routine;
its basic method is prior work. Build a balanced binary tree of original
index intervals. At each split I_L,I_R store, for every start v in I_L and
1<=alpha<=t, A(v,alpha), the minimum last value of an alpha-chain starting
at v within I_L; infeasible states are +infinity. Similarly, for every
endpoint v in I_R and 1<=beta<=t, store B(v,beta), the maximum first value
of a beta-chain ending at v within I_R; infeasible states are -infinity.
Length-one states equal a_v. The recurrences for larger lengths are

    A(v,alpha)=min_(w>v,a_w>a_v in I_L) A(w,alpha-1),
    B(v,beta)=max_(w<v,a_w<a_v in I_R) B(w,beta-1).

They are valid by separating the first or last element; attaining states
store linked witnesses. For each length a strict-rank Fenwick sweep over
previous-length states costs O(|I| log n). Sum across splits and levels
to get O(nt log^2 n) work and O(nt log n) witness states. Cap lengths at
the child size where smaller than t.

For each split and length, put feasible A records in a static orthogonal
range-min structure on coordinates (v,a_v,A(v,alpha)), weighted by their
third coordinate and storing a witness. B records use an analogous range-
max structure. Nested balanced range trees suffice: canonical box
decomposition uses O(log^3 n) pieces, each storing an extremal value/pointer.
Recursive sorting and duplication use O(q log^3 n) preprocessing for q
records, a conservative bound. All splits/lengths cost O(nt log^4 n).

Normalize a query to index interval [l,r] and value interval [a,b] by
comparisons/binary searches. Empty and single-index cases are direct.
For l<r use the lowest index-tree node containing both endpoints; its
split s satisfies l<=s<r. Query, for each positive length at most t,

    L_alpha = min A(v,alpha): l<=v<=s, a<=a_v<=b, A(v,alpha)<=b;
    R_beta  = max B(v,beta): s<v<=r, a<=a_v<=b, B(v,beta)>=a.

Both are feasible chains in the query: every interior value lies between
their endpoint values, and index monotonicity keeps them in the queried
side. Conversely every feasible left alpha-chain has peak >=A of its
start, and the minimizing witness satisfies all boundaries. Thus L_alpha
is exactly its minimum possible peak; the analogous maximum-base fact
holds for R_beta. Inclusive boundaries are used for query membership,
while joining two positive chains requires the STRICT test L_alpha<R_beta.
The left operation is a minimum even if a contrary display is read in the
source. No infeasible state is treated as an actual chain.

Include zero-length empty states and one-sided feasible chains. L_alpha
is nondecreasing in alpha (drop the last point of a longer chain), and
R_beta nonincreasing in beta (drop the first point). Infeasible states
form suffixes. For each alpha<=t binary search the maximum compatible
beta<=t, also allowing alpha=0, and retain the largest alpha+beta.
All candidates are feasible. If the optimum is at most t, its two side
lengths are included and their extremal endpoints preserve compatibility;
thus the retained chain is exactly optimal. Otherwise the returned chain
may be shorter but is still feasible. Store only its two handles. This
routine has total overhead O((n+m)t log^6(n+m+2)); final handles expand
by linked-pointer steps in time proportional to their length.

## 7. Stitching and final-winner-only reporting

For every r in R, compute longest strict chains from r to all northeast
endpoints and from all southwest endpoints to r using strict-rank sweeps,
keeping length and parent pointers. Reverse index order/comparison for
the latter, without arithmetic on original values. O(n log^2 n) work per
r suffices; any attaining tie rule works for these reporting trees.
Put the endpoints and their lengths in static 2D orthogonal range-max
structures. A query containing r obtains its maximum forward and backward
lengths. Both corresponding paths lie in the query by endpoint-box
containment; they have no common vertex except r, by strict index order.
Their concatenation has length forward+backward-1 and is feasible.

For an optimum of length >=t, R hits a canonical optimum at some r. Each
maximized half is at least the corresponding optimum half, so their
feasible concatenation is optimal. For lengths <=t the short routine is
optimal. Take the largest feasible value over all stitching candidates
and the short handle, including empty queries and threshold equality.
The overhead is O((n+m)|R| log^3(n+m+2)). Store only constant-size candidate
handles and lengths; do not expand losing candidates.

Finally expand one winner per query. A stitching handle follows its two
parent trees, reverses one list using an output-sized buffer and suppresses
one repeated r. A short handle follows its linked states. Thus all final
expansion costs O(K) with no polylogarithmic or sample-size multiplier.

## 8. Full uniform cost, fallback and scope

For k<N, combine (8) and Sections 6--7:

    O((n+m)t log^6(n+m+2)
      + Nk log^3(n+2) + Nk^2 log^2(n+2)
      + (n+m)k log^3(n+m+2)) + O(K).

Substituting (6) bounds this by the stated log^30 theorem. The n^(5/3)
net cost is absorbed by (n+m)n^(2/3). All representations and addresses
are polynomial in n,m, so constant-factor larger pointer widths cost a
constant number of words; all explicit arithmetic charges above apply.

If k>=N, use every real point as R and skip ALL net tables. All-point
stitching costs O((n+m)n log^3(n+m+2)), at most O((n+m)k log^3(n+m+2)).
The same k=O(n^(1/3)log^3(n+2)) upper bound follows from its formula in
this regime too, and therefore this fits the theorem. The conservative
constants may cause fallback for a huge finite range, but no uncharged
asymptotic threshold is assumed. n=1 costs O(m+1+K); m=0 can return
immediately. The original requires n>=1; if n=0 is additionally allowed,
return m empty answers in O(m) under the usual max(1,n) convention.

Values are only compared and stored, never assumed to be small integers.
Equal values have equal ranks and cannot follow one another in any strict
chain. Query normalization handles any specified open/closed endpoint
convention without changing membership. All queries may overlap arbitrarily;
the simultaneous hit property is independent of their number. The proof
settles reporting rather than length alone and includes all optimum lengths.

**Proposer gap list: no mathematical gap identified in this reconstruction.**
The finite check file exercises only stated finite instances and manual
compression parameters, not the enormous uniform-parameter construction.
The universal theorem rests on the arguments above. Novelty/value must be
reviewed separately against the primary sources and their oracle assumptions.
Neither the older acceptance nor this dossier certifies the stronger claim.
No new manuscript, audit verdict, acceptance record, or STOC label is made.
