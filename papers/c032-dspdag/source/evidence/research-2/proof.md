# Rectangular batching for labelled disjoint paths on a common DAG order

Proposer: c032-dspdag-research-5f16f6951448. This is a research proof packet,
not a manuscript, referee verdict, or venue assessment. The immutable question
is source.md; its existential quantifier is answered by the k=3 corollary below.

## Theorems and computational model

Fix an integer k>=2. On a common N-vertex acyclic order, let each of k path
labels have its own allowed-edge graph and prescribed source and target. Exact
strictly vertex-disjoint detection admits the bound

    O_k(N^k log(N+2) + sum_b (N/b)^k B_k(b)),                 (1)

where b ranges over powers of two from 1 through N/2 after power-of-two padding,
and B_k(b) is any deterministic EXACT Boolean multiplication cost for
(b by b) times (b by b^(k-1)), including reading and writing its arrays.
Private completion vertices and endpoint normalization increase N only by a
constant depending on k. For weighted shortest paths, add O_k(m+n) original
weight additions/comparisons to construct the allowed-edge graphs.

Two unconditional consequences are claimed:

* For every fixed k>=3, deterministic detection costs
  O_k(m+n+n^(k-2+log_2(7))) source-model word operations, using O_k(n^k) words.
  With elementary arithmetic bit costs on the NEW bounded-word operands this
  becomes O_k(n^(k-2+log_2(7)) log^2(n+2)), plus original-weight preprocessing.
* For every fixed k>=3, deterministic detection costs O_k(m+n+n^(k+0.3))
  in the source model. In particular for k=3 it costs O(m+n+n^3.3),
  including elementary bit arithmetic for the new algebraic operands. In
  particular k=3 and delta=7/10 give a full positive answer to AVW Open Problem 3.
  This numerical consequence uses the established rectangular multiplication
  bound of Le Gall--Urrutia, Table 3 and Section 2.2, with an explicit rational
  degeneration to Boolean bounded-word bridge proved in Section 6 below.

There is no width, sparse-instance, unweighted, unique-distance, or
distances-given promise. The n-only source bound uses the ordinary O(n^2)-arc
input convention; an arbitrary parallel-arc encoding retains its O(m) scan.
Original weights have the same addition/comparison model as AVW's baseline.
For arbitrary B-bit integer weights, the actual original-weight preprocessing
bit cost, e.g. O_k((m+n)(B+log(n+2))), must be added. No unbounded input integer
is assumed to fit a word. Only the NEW matrix and indexing operands are shown
to occupy O_k(log(n+2)) bits. Detection, rather than path reporting, is claimed.

## 1. Original shortestness, endpoints, and completion

Topologically relax distances d_i from each original source in the ORIGINAL
weighted DAG. An unreachable designated target causes NO. Retain an edge
(u,v) for label i exactly when d_i(u) is finite and
d_i(v)=d_i(u)+w(u,v). Every original shortest path is retained, and telescoping
proves every retained source--target path has its original shortest length.
This familiar reduction is not a new contribution. It costs O_k(m+n) weight
operations and is performed before any path conflicts are considered.

First take strict vertex disjointness, including terminals. If endpoints of
different labels coincide, reject. A within-label equality s_i=t_i is allowed:
the original path is trivial in a DAG. Append one private vertex z_i for each
label, all after the original vertices, with the sole label-i completion edge
t_i->z_i. Deleting or appending this edge proves equivalence. A path that
passes t_i without completing cannot later return to it in an acyclic graph;
there is consequently no spurious successful path. Every unfinished token is
at an original vertex, earlier than every completed token at its z_i.

For the interpretation permitting only endpoint/endpoint sharing, replace
each terminal vertex v by private copies v_i for exactly the labels having v
as an endpoint. Labels without v as endpoint cannot visit it. Other vertices
remain shared. For label i forbid entry into its source and exit from its
target, apart from completion. Map tight edges to the appropriate copies.
Copies at one original vertex are consecutive in the common order; no original
edge joins vertices at the same original rank. Mapping paths back and forth
proves equivalence: precisely the permitted endpoint sharing is separated,
while every prohibited internal intersection remains a shared collision or
an unavailable visit. The within-pair trivial path uses its single endpoint
copy followed by completion. At most 2k private endpoint copies are required.

If the weaker convention forbids ONLY internal/internal intersections, retain
also one shared internal copy of each terminal v, used by labels for which v
is not an endpoint. Endpoint uses go to their private copies. Exactly two
internal uses collide, whereas endpoint/internal and endpoint/endpoint uses
do not. The same mapping proves equivalence. Thus none of these original
endpoint conventions restricts the claimed exponent. Strict disjointness on
the resulting label-specific graphs is the remaining task.

Pad the common topological order with isolated vertices to a power-of-two N.
The number of vertices is O_k(n); all label edges are forward. Distances are
never recomputed in the transformed or partially occupied graph.

## 2. The frontier graph, proved for every fixed k

A state q=(q_1,...,q_k) has pairwise distinct coordinates. Write rho(q)=min_i q_i.
Initialize F to zero except F(s_1,...,s_k)=1. In a state, only the label i of
the unique least coordinate u=q_i may move, along its allowed edge (u,x).
Retain the transition only when the new tuple is pairwise distinct. Since
x>u and all unchanged coordinates exceed u, rho strictly increases.

Soundness follows by appending each move to that label's path prefix. Every
abandoned vertex is smaller than every current coordinate: this holds initially
and is preserved because the minimum strictly increases. A destination x>u
cannot hit any abandoned vertex, and the validity check prevents hitting a
current coordinate. Hence the prefixes remain vertex disjoint.

For completeness fix any feasible family to the private sinks. Advance the
least token along its fixed path. While any token is unfinished, the least
token is not a completed sink because all unfinished positions precede every
sink. Thus an edge is available, and disjointness makes the move legal. The
number of remaining edges decreases until all private sinks are reached.
Reachability of their ordered tuple is therefore equivalent to feasibility.
For an arbitrary intermediate tuple F denotes THIS state-graph reachability,
not an unsupported assertion about all possible disjoint prefixes.

Let A_i be label i's Boolean adjacency matrix. The exact incoming contributions
to a valid target p are

    F(p[i:=u]) AND A_i(u,p_i), for every i and every u<rho(p).   (2)

Invalid states always have F=0. Equation (2) is a one-edge recurrence, with
one complete predecessor tuple in each term; it never combines witnesses
chosen independently for different paths.

## 3. Chronological recursion and the k output classes

Solve(l,r) recursively finalizes all states whose minimum lies in [l,r]. At
entry all incoming transitions with source minimum <l have already been applied
to these states, and all smaller-minimum states are final. A singleton interval
needs no internal update. Otherwise split into equal L=[l,h], R=[h+1,r] of
size b; call Solve(L), apply precisely the L-to-R minimum transitions, then
call Solve(R). Each transition with minima u<v belongs to the unique recursion
node where u is in the left half and v in the right half. This proves the
entry/finalization invariant inductively. Seeds, even seeds later in the order,
stay present; backward transitions do not exist.

For a cross step put S=[h+1,N-1], T=[r+1,N-1]. Fix moved label i, and order the
other k-1 labels once and for all. A context c is their tuple. For u in L,
set B(c,u)=F(c with coordinate i inserted as u), and C(u,x)=A_i(u,x).
Context coordinates are in S, so the unique source minimum is u. Partition
outputs into exactly k classes:

    0: x in R; c in S^(k-1).
    j (1<=j<=k-1): x in T; c_j in R;
                  c_a in T for a<j, c_a in S for a>j.

If the changed coordinate is in R use class 0. Otherwise it is in T, and the
first context coordinate in R uniquely selects class j. These conditions are
equivalent to target minimum in R. Invalid targets are masked. Contexts with
repeated coordinates have zero B entries. Each Boolean product output has one
fixed context and therefore implements exactly (2), retaining pairing and all
collision constraints. During the cross step only states with minimum in R
are written; every B source has minimum in L and is already final. Reordering
labels, classes, or product blocks within the cross step is consequently safe.

For k=3 the classes reduce to (x in R,c in SxS), (x in T,c in RxS), and
(x in T,c in TxR). In the last two classes x is allowed beyond the current
interval. Disallowing this would omit legitimate transitions.

## 4. Rectangular packing and the global charge

Group contexts in batches of at most b^(k-1), and changed-coordinate targets
in batches of at most b. Zero-pad incomplete batches. Compute

    C^transpose [b by b] * B^transpose [b by b^(k-1)]

over the Boolean semiring. The result is indexed by (target,context); scan,
mask, and OR it into F. Although the operands are transposed, they implement
the same contraction over u in L. Fixed k permits O_k(1) index arithmetic per
entry. Ordinary tuple enumeration and indexing use O_k(log(N+2))-bit integers.

Class 0 has at most N^(k-1) contexts and one target batch, hence at most
(N/b)^(k-1) products. Every other class has at most b N^(k-2) contexts and
at most N/b target batches. Its count is at most (N/b)^(k-1) as well: the
ceiling of a context ratio is at most the integer (N/b)^(k-2). Zero target or
context domains cause no calls. These estimates hold for b=1, final blocks,
the root, and empty tails. Across k moved labels and k classes there are at
most k^2 (N/b)^(k-1) products per node.

Each product packs b^2+b^k input entries, scans b^k outputs and masks/scatters
them in O_k(b^k) operations. This is charged EVERY time, including when an
input is repacked for a different target block. Generating the class context
lists costs O_k(N^(k-1)) per node and is within the same total packing bound
O_k((N/b)^(k-1)b^k)=O_k(N^(k-1)b). Lists may instead be generated in streaming
batches. No whole N^k state-table scan is made at an individual node.

There are N/(2b) nodes of half-width b. Multiplication at that level costs
O_k((N/b)^k B_k(b)); all nonmultiplication data movement costs O_k(N^k).
Initialization costs O_k(N^k). Summing proves (1). If B_k(b)=O(b^tau) for a
fixed tau>k, the geometric sum is O_k(N^tau), and N^k log N is absorbed.
An uncharged Boolean oracle or an arithmetic exponent alone is not used in (1).

Space is the O_k(N^k) Boolean state table, adjacency, current O_k(b^k) packed
arrays and logarithmic scheduler stack, PLUS the primitive workspace. Without
a workspace bound for the supplied primitive no additional space conclusion
is claimed from (1).

## 5. Fully explicit fallback for every fixed k

Split the b^(k-1) columns of a rectangular product into b^(k-2) blocks of b
columns. Each block is an exact integer square product of 0/1 matrices,
followed by positivity thresholding. Strassen's seven-product identities give
O(b^alpha), alpha=log_2(7), arithmetic operations per block. Thus
B_k(b)=O_k(b^(k-2+alpha)), including its b^k entries, since alpha>2.
The exponent exceeds k and is less than k+1. Formula (1) gives the claimed
all-fixed-k bound. A stream of square products and the state table uses
O_k(N^k) words, with no rectangular workspace assumption.

Exactness is integer positivity, not parity. At Strassen depth d input sums
have magnitude at most 2^d. Leaf products have magnitude at most b^2; at most
four signed terms combine per output per return level. All intermediate
magnitudes are O(b^4), hence O(log(N+2)) bits. Straightforward integer
multiplication costs O(log^2(N+2)) bits; additions cost less. Therefore the
displayed bit bound follows without assuming unit-time arbitrary integers.

## 6. Rational border rank supplies the stronger k=3 Boolean primitive

The precise external theorem used here is Le Gall--Urrutia, arXiv:1708.05622v2,
Table 3 (k=2), with exponent <=3.251640. Their Section 2.2 works over a field F,
defines degenerations by polynomial maps over F[lambda], and defines this
exponent as the infimum of beta for which the border rank of <q,q^2,q> is
O(q^beta). Specialize their field to Q. In particular for some sufficiently
large fixed integer q0, the Q border rank r0 of <q0,q0^2,q0> is <q0^3.26.
The strict margin absorbs the asymptotic constant. This is a use of an
established prior multiplication result, not a new laser-method theorem.

Here is the exact-rank conversion, including its field. Fix a Q-polynomial
degeneration of r0 independent scalar multiplications to that fixed matrix
tensor: its polynomial image has leading coefficient lambda^s times the
tensor, and total degree at most D, for some FIXED s,D. Take its t-th tensor
power. The leading coefficient at degree st is <q0^t,q0^(2t),q0^t>, and
total degree is at most Dt. Evaluate at Dt+1 distinct rational points.
Univariate interpolation expresses that coefficient as a Q-linear combination
of these evaluations. Each evaluation has tensor rank at most r0^t, hence
the exact Q-rank is at most (Dt+1)r0^t. For some sufficiently large FIXED t,
this is <(q0^t)^3.27. This is one fixed exact rational tensor identity, not a
sequence of floating-point approximate products. Polynomial interpolation is
possible over Q with no field-size obstruction.

Put q=q0^t. Permuting the last two tensor variable groups turns
<q,q^2,q> into <q,q,q^2>. Indeed the trilinear form
sum_(a,b,c) X_ab Y_bc Z_ca has the same coefficients after permuting groups
and transposing/reindexing the relevant variables. A rank decomposition is
preserved, and reading the third group's coefficients gives an exact bilinear
algorithm for (q by q) times (q by q^2). Let r<q^3.27 be its rank. If useful,
add zero products to make r>q^3, still retaining the strict upper bound.

All coefficients of this ONE finite base algorithm are rational constants.
Let H be the product of their nonzero denominators and choose a fixed integer
C>|H|+2. For a complete N-vertex instance choose by a deterministic sieve a
prime p in (K,2K), where K=max(N,C). Bertrand's theorem guarantees existence.
No denominator vanishes modulo p. The sieve costs O(K log log(K+2)) ordinary
word steps, or a conservative O(K log^2(K+2)) bit steps, within the cubic
budget up to a fixed constant. One prime is reused for the entire instance.
Each coefficient is reduced once; its bit length is a fixed constant.

For any desired half-width b, pad to M=q^a with b<=M<qb. Recursively apply
the fixed base identity over F_p to M by M times M by M^2 matrices. All
identities are rational polynomial identities with invertible denominators,
so reduction modulo p preserves them exactly. With dense linear maps of
constant base dimensions, the recursion obeys

    T(M) <= r T(M/q) + O_q(M^3).

The additive term includes constructing EVERY linear combination and
recombining outputs. Thus T(M)=O_q(M^(log_q r))=O_q(b^3.27).
Padding costs O_q(b^3) and is included. Only O(log(N+2))-bit residues occur;
elementary modular arithmetic, including remainder, costs O(log^2(N+2))
bits per operation. The true product of the ORIGINAL 0/1 factors has each
entry in [0,b], even after zero padding. Since p>N>=b, a residue is zero iff
that nonnegative integer entry is zero. Thresholding 'nonzero' is therefore
an exact Boolean product, with no cancellation error or random choice.

This proves B_3(b)=O(b^3.27 log^2(N+2)) for a globally chosen modulus. Substituting
in the level sum, its N-dependent bit factor is O(N^3.27 log^2(N+2)), including
all packing and prime setup. This is O(N^3.3). The standalone primitive could
equally choose its own prime above max(b,C); a global prime simply avoids
repeated setup. This distinguishes the b-dependent cost in (1) from the
global bit-factor implementation. A depth-first implementation can stream
the constant number r of subproducts with O_q(M^3) live words; that extra
space fact is unnecessary to the original question.

For k>3, partition the b^(k-1) columns into exactly b^(k-3) blocks of b^2
columns and use this same k=3 primitive. This costs
O_k(b^(k+0.27) log^2(N+2)), including all b^k input/output entries. In (1)
the level sum is O_k(N^(k+0.27) log^2(N+2))=O_k(N^(k+0.3)); the additive
N^k log N is smaller. Thus the same constant saving 0.7 holds for every fixed
k>=3, without any additional rectangular exponent theorem. The original
question only needs its k=3 consequence. This general-k corollary is a direct
consequence of the proved primitive bound, not a second contribution.

The constants may be impractically large. A fixed finite rational base is
hardwired once, independent of graph size, so this is a uniform algorithm,
not per-input nonuniform advice. No base coefficient list or fast rectangular
implementation is supplied by the finite verifier. The numerical exponent
depends on the stated established theorem and the exact conversion above.
The fallback in Section 5 independently resolves the original if a referee
finds a problem with this stronger dependency or bridge. Such a problem would
require revising the current stronger claim before acceptance.

## 7. Contribution, falsification, and review obligations

Shortest-path filtering, the least-token recurrence, generic divide and
conquer, Strassen, tensor permutation/interpolation, and rectangular exponent
bounds are prior techniques. In particular Valiant's 1974 report/1975 JCSS
paper already accelerates a chronological closure by Boolean multiplication.
The proposed contribution is the precise output-minimum partition and its
rectangular context grouping, together with the globally charged schedule
for all labelled common-order disjoint paths. It yields a polynomial dense
exponent saving for every fixed k and the stronger k=3 corollary, rather than
an improvement restricted to a graph family. The prescribed shortest-path
question is fully contained in that common-order theorem.

Fresh current primary comparisons and access limits are recorded separately
in literature.md. Bounded negative searches do not certify priority. The
authoritative scientific evidence is this argument and its dependencies;
finite exact comparisons in validation.json are only bug checks. They do
not establish an asymptotic exponent or replace any proof above.

No gap is currently identified by the proposer in these stated theorems.
The rational-field dependency, exact interpolation, fixed-base uniformity,
endpoint equivalences, rectangular data movement, original-model compatibility,
novelty, substantive value, and STOC significance must all be assessed afresh.
No previous acceptance applies to this strengthened packet. No manuscript or
PDF is authorized by this research job.
