# Capped witness listing with legal group queries

Research pass 1, job `c034-grouptri-research-e96d630c6fdd`.
This is a reconstruction of a standard detection/listing tool, not a novelty
claim, full resolution, or publication candidate. Generic relationships are
prior work; see the primary comparisons below.

## Explicit conditional tool statement

Fix a prime p, a constant c>0 and 0<epsilon<=1. Suppose complete-input Exact
Triangle over F_p^d has a deterministic detection algorithm taking
O_C(b^(3-epsilon) polylog(b+2)) time whenever p^d<=b^C, for every fixed C>0,
with epsilon independent of C. For every fixed 0<theta<1 there is then a
deterministic algorithm on n-vertex-per-part instances with p^d<=n^c that,
for every outer pair (a,b), returns exactly min(t_ab,T) distinct witnesses,
where T=ceil(n^(1-theta))+1 and t_ab is its true witness count. Its charged
time is O_(p,c,theta)(n^(3-epsilon*theta/6) polylog(n+2)). It also allows
arbitrary missing edges, supplied by Boolean adjacency masks. No universe of
all group elements is enumerated. Constants in polylog factors are fixed.

For n<=1 or empty parts use direct enumeration. A zero-dimensional original
label group uses the same marker algorithm below, including on masked graphs.
For other n pad the vertex parts to N, the least power of two >=n. A padded
vertex has all incident edges marked absent. Use the cap T computed from n;
T<=3n^(1-theta) for n>=1. Write alpha=theta/6 and let b0 be the least power
of two >=N^alpha. Thus N^alpha<=b0<2N^alpha (b0<=N). If rounding makes b0=N,
the finite range of such n can be absorbed into the constant and brute-forced.

## Legal complete-input masks

Append three F_p coordinates, one for each edge kind AB, BC, AC. A present
edge has three zero marker coordinates. An absent edge has 1 in its own
kind's coordinate and 0 in the other two, with arbitrary original coordinates.
Each triangle contains exactly one edge of each kind. Its sum in a marker
coordinate is consequently 0 or 1 according as that edge is present or absent.
The complete encoded instance has a zero triangle exactly when the masked
instance has one. This also works at p=2; a shared single sentinel would fail.
The encoded dimension is d+3 and the exponent stays p. Original labels may be
zero-dimensional; the marker extension is still nontrivial.

At a query of side b>=b0>=N^alpha, p^(d+3)<=p^3*n^c<=N^(c+3log_2(p)),
so it is <=b^C for C=(c+3log_2(p))/alpha. This is one fixed C for all queries
in this input family. There are NO oracle calls below b0. Word sizes log b
and log n differ by at most the fixed factor 1/alpha; all representations
and coordinate arithmetic remain valid at the charged cost.

## Algorithm and invariants

Maintain one count and output list per original outer pair, initially zero.
Depth-first traverse the product octree: at side b the three parts are
intervals of length b; the eight children halve each interval. On entering
a cube construct and query its complete encoded group instance. Its active
edges are the original present edges, except that AB pairs with count T are
also absent. A negative answer returns immediately. A positive cube of side
b>b0 recursively visits its eight children in fixed order. A positive cube
of side b0 scans all its triples, outputting a triangle exactly when it is
originally present, has zero original sum, and its pair has current count<T.
Increment that pair's count immediately after each output. All comparisons
and original-label checks cost polylog(n+2). A positive cube may use only its
entry-time query; descendants each reconstruct masks from current counts.

1. Counts only increase, and never exceed T. Every emitted tuple is a valid
   original triangle. Distinct octree leaves have disjoint tuple domains;
   each tuple is scanned once inside its leaf. Thus there are no duplicates.
2. Every positive cube emits at least one tuple before it returns. At entry
   it has a valid witness of a currently unsaturated pair. If no earlier
   descendant emits a tuple, this witness stays active and survives all
   queries along its path, reaching a brute-force leaf that emits it. If an
   earlier descendant emits a tuple, the assertion is already satisfied.
   Depth-first execution is essential: counts do not change outside the
   cube while its subtree is being processed.
3. If a pair's final count is <T, it was never saturated. An unreported true
   witness for that pair could not have been removed by any mask; all its
   ancestors would have queried positively and its leaf would have scanned
   and emitted it. Therefore its final count is exactly t_ab. If a pair is
   saturated, its final count is T and it has at least T genuine witnesses.

This proves the exact min(t_ab,T) guarantee, including completeness for
t_ab<=ceil(n^(1-theta)). A pair with exactly T witnesses is deliberately
classified as heavy for that threshold; no claim that it has >T is needed.

## Fully charged ledger

Let Z be the total number of outputs; Z<=n^2*T=O(n^(3-theta)). At side b,
there are at most (N/b)^3 queried cubes, even if every branch is explored.
Constructing each masked graph costs O(b^2*(d+3)), dominated by
b^(3-epsilon)*polylog(n+2) because epsilon<=1. Oracle calls at this level
therefore cost O(N^3*b^(-epsilon)*polylog(n+2)). Summing the geometric series
over b=N,N/2,...,b0 gives O(N^(3-alpha*epsilon)*polylog(n+2)). Recursion,
negative queries, adjacency checks and count lookups are included in this
bound. The root setup costs O(n^2*(d+3)).

At any depth, positive cubes have disjoint tuple domains. By invariant 2,
associate each positive cube with an output in its own subtree. Outputs
associated to distinct cubes at that depth are distinct. Hence at most Z
leaves are positive. Their brute-force scans cost
O(Z*b0^3*polylog(n+2))=O(n^(3-theta+3alpha)*polylog(n+2))
=O(n^(3-theta/2)*polylog(n+2)). Output storage costs O(Z log n) bits per
constant number of vertex indices, within the same bound. Counts cost O(n^2)
words. With alpha=theta/6 and epsilon<=1, the oracle term dominates the
stated time. Streaming cubes avoids materializing the entire recursion tree.

## Backend and prior-work boundary

Majdoddin, arXiv:2610.17420v1, Theorem 21.3 and its proof (printed pp.100-101)
state deterministic elementary-group detection/all-edges time
O(p^6*b^(3-epsilon_H*gamma_H)*(log b)^6), with saving independent of the
dimension/order constant. Corollary 9.1(b), Definition 2.1 and Section 16
instantiate H(1/14,0.077); its displayed saving is 0.0055. This worker read
the complete Theorem 21.3 proof and the matrix-corollary proof including its
H instantiation, not a fresh audit of all 130 pages of dependencies.
Thus the tool is directly parametrized by the actual stated prior backend,
and not a newly assumed stronger oracle. Fixed p meets the theorem's prime
size restriction for all sufficiently large b; the remaining finite range
is absorbed in the p-dependent constant and solved by brute force.

CVX23 (arXiv:2303.14572), Theorem 5.1, printed pp.18-19, uses cubic initial
witness sorting and then faster updates; the capped routine replaces only
that sorting need in the proposed quotient route. Sheffield--Vassilevska
Williams--Xi, arXiv:2608.19092v1, documents established generic
detection/all-edge/listing reductions and their losses. This conservative
octree proof is not claimed to improve them or to be independently new.
Live arXiv records for both recent papers still showed only v1 on 2026-11-02.

## Remaining scope

The tool alone does not resolve source.md. Needed next: a fully charged
quotient decomposition with edgewise potentials, lifting into the kernel,
complete-input kernel masks, and an induction over every fixed M. The
frequency-table and materialized-piece costs must be charged explicitly;
CVX23's compact representation time cannot automatically be used for calls
that require full labelled graphs. No full-resolution claim is made here.
