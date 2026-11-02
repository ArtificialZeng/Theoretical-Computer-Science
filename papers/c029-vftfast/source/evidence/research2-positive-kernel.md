# Pass 2: a parameter split reopens the positive construction route

Job c029-vftfast-research-36ff17e1eeb1. This is proof-program evidence,
not a manuscript or a claim of full original resolution. Original remains
unresolved pending the final end-to-end source-transfer and novelty check.

## A. Constructive representative-path lemma

Let d>=1, f>=0, and T=min(n,f+d+1). For every ordered terminal pair x,y,
one can compute a list of simple length-d x-y paths such that whenever an
x-y length-d path avoids F, |F|<=f, some listed path avoids F. There is a
deterministic algorithm with time

    n^O(1) (f+d+1)^O(d+1) 2^O(d),

where all O exponents are absolute. This is not FPT in d independent of f;
it is consistent with the supplied CLIQUE barrier.

Here is a self-contained linear-algebra implementation. Work over a prime
field of size at least n (a prime between n and 2n suffices for n>=2), with
an explicit T by n Vandermonde matrix on distinct field elements. Every
set of at most T columns is independent. For a p-set A, let w(A) be the
vector of all p by p minors on its columns, in a fixed column order; it has
binomial(T,p) coordinates. For a family of p-set supports, retain any column
basis of their w-vectors, keeping one actual path per basis vector.

This reduction preserves disjointness against every Y of size<=T-p:
if A avoids Y, w(A) wedge w(Y) is nonzero. Expressing w(A) in the retained
basis shows at least one retained B also has nonzero wedge with w(Y), hence
B avoids Y. This uses only linearity of exterior product and independence
of distinct Vandermonde columns. No matroid-representative black box is needed.

For each fixed start x, initialize the path (x). At stage i (paths of i
edges, p=i+1 vertices) and each endpoint v, retain a basis for that endpoint.
For stage i+1, append v along every graph edge from a retained path ending
at u, excluding repetitions, then reduce each new endpoint family to a basis.
The invariant is disjointness representation against every Y with
|Y|<=T-(i+1). To extend a full path ending at v, apply the previous invariant
to Y union {v}; the added vertex costs exactly one unit of the available
rank. Reduce again. This proves the invariant by induction, and at i=d it
covers every actual fault set (if T=n and f+d+1>n, any F disjoint from a
length-d path has size<=n-d-1=T-(d+1)). Store predecessors to recover paths.
If d>=n no simple length-d paths exist; this case is immediate.

All stages have p<=d+1. The coordinate count is at most
max_(p<=d+1) binomial(f+d+1,p) <= (f+d+1)^(d+1).
Candidate counts per stage are at most n^2 times this dimension. Exact
Gaussian elimination and minor determinants give a fixed polynomial in this
dimension, n,d,log n. Rank T and its explicit matrix also have polynomial
size in the explicit graph input after capping f at n-2. This justifies the
claimed form including bit complexity. A basis over a finite field is exact.

Apply the protected fixed-path gap cut of research1-separator.md to every
listed path, for every terminal pair. If an original-budget violation
F exists, the list contains a path avoiding F for its endpoints. The protected
cut routine cannot reject that path and returns a compatible witness cut of
size at most (r-1)f. Conversely every returned path/cut is explicitly valid.
Thus this gives an arbitrary-H joint separator in time
n^O(1)(f+d+1)^O(d+1)2^O(d), complete even for ALL simple length-d paths.
It does not give the F(d)poly(n,f) separator ruled out conditionally.

## B. The large-f / small-f switch

Fix the ORIGINAL delta, and set eta=min(delta/2,1/4). Cap k at
K=ceil(ln(n+2)), and use d=floor(sqrt(k)) for k>=4. Handle bounded k by
known polynomial multiplicative constructions with constants depending only
on the bounded range. For f>=1 split at

    f >= n^(1/(eta*d)).

In the LARGE-f branch, the known polynomial-time (2d-1,0) VFT spanner
has size poly(d)*f^(1-1/d)*n^(1+1/d). The switch ensures
n^(1/d)<=f^eta, so its size is at most
poly(d)*f^(1+eta-1/d)*n <= polylog(n)*f^(1+delta)*n^(1+1/k).
Its stretch is O(sqrt(k)); additive zero is sufficient. The deterministic
optimal-size polynomial construction in BDR2021 is the precise dependency;
its explicit uniform k factors/time must be verified in the final pass.

In the SMALL-f branch, log f < log n/(eta*d). Consequently
(f+d+1)^O(d+1) is n^O_eta(1): use f+d+1 <= (f+1)(d+1),
(d+1)/d<=2, and d log(d+1)=O(log(n+2)) under the k cap.
The representative-path separator is therefore genuinely uniform polynomial
in this regime. Repeatedly insert its returned path until its certificate;
each insertion adds a new edge, so at most m insertions occur.

Use r=ceil(12k/eta), q=(r-1)f. The source witness-sequence packing theorem
with common fault budget q would then give
polylog(n)*q^(1+eta)*n^(1+1/k), which meets the ORIGINAL f^(1+delta)
size dependence. The source analysis / order-insensitive witness transfer is
the same cited dependency identified in research1-separator.md. This pass
has not independently re-audited that long proof. For all shorter scales,
apply the pendant-path reductions in that record. Crucially use the BASE n
for the small-f split; the enlarged N<=dn only improves the complexity upper
bound and costs polylogarithmic factors in size. Inflate only the construction
witness budget q, never the original fault guarantee f.

For f=0, use the known nonfaulty mixed-stretch construction. For n<=2 and
k=1 use G where its size qualifies. For k>K apply the construction at K;
n^(1+1/K)<=e*n and its stretch/additive terms are smaller than those required
at k. Integer threshold comparison can avoid real arithmetic: eta is fixed
rational a/b, so compare f^(a*d) with n^b exactly. No randomized sampling is
needed in the representative algorithm. All log powers may depend on delta,
never on f or k. No original quantifier is changed.

## C. Actual status and single decisive next test

The new part of the research program is the combination of the f-dependent
representative separator with the large-f multiplicative branch. The earlier
pass treated f^d as a globally fatal cost; it is not fatal after this switch.
This observation is positive algorithmic evidence, not original hardness.

Before asserting full resolution, the FINAL remaining research pass must
assemble and adversarially check the deterministic end-to-end theorem:
(1) verify the uniform polynomial parameter dependence of BDR2021's
multiplicative constructor (or use DR2020 with its polynomial stretch factor);
(2) verify source Theorem 5.4 for arbitrary adaptive insertion histories with
budget q, including all scales and source size factors; (3) implement/check
the representative DP with finite-field bases and test the complete spanner
on bounded exact graph/fault domains; (4) recheck current primary literature
for the combined parameter-switch algorithm. A flaw in one of these named
steps blocks the original claim. No candidate/acceptance/PDF is created now.

## D. Closing checks and simplifications

Before scientific close, the local DR2020 v2 Theorem 2 and Theorem 9 were
read explicitly: size O(d*f^(1-1/d)*n^(1+1/d)) and deterministic worst-case
time O(m*d*f^(2-1/d)*n^(1+1/d)). These have uniform polynomial dependence
under d<=sqrt(log(n+2)); use this dependency in the large-f branch rather
than requiring the sharper BDR2021 algorithm. Its extra d size factor is
polylogarithmic. This closes the large-f runtime uncertainty in item (1).

The finite-field DP implementation research2_representative_checks.py passed
106,424 exact fault-disjointness comparisons for 4,024 DP configurations on
110 graphs. All labeled graphs on 2..4 vertices were covered, together with
18 fixed graph masks each on 5 and 6 vertices, all starts/endpoints,
d=1..min(n-1,4), and f=0..n-d-1. These tests verify the finite implementation,
not source packing transfer or the complete spanner guarantee.

One may alternatively scan each fixed representative list just once, applying
the protected gap routine as the spanner grows. Rejection certifies no protected
budget-f cut at that time, and this absence is preserved by adding edges.
Insertion includes the whole listed path. Thus the final original-f guarantee
follows from representation and monotonicity without repeated separation.
Every inserted path still has a q-budget witness for the source size analysis.
This does not close the pending source-analysis verification by itself.
