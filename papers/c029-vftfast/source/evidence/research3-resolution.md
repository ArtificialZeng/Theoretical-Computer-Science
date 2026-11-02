# Full-scope algorithm proposed for fresh review

Job: c029-vftfast-research-9df2f29ab673. Research pass 3 of 3.
This is a mathematical evidence packet, not a manuscript, acceptance, or
STOC assessment. All claims below are proposed for independent review.

## 1. Statement and dependencies

For every fixed rational delta in (0,1), there is a deterministic algorithm,
polynomial in the explicit input length with exponent depending only on
delta, that on every undirected unweighted simple n-vertex graph G and
integers f>=0,k>=1 returns a subgraph H satisfying, simultaneously for all
F subset V(G), |F|<=f, and surviving u,v with finite G-F distance,

    dist_(H-F)(u,v) <= C_delta sqrt(k) dist_(G-F)(u,v) + C_delta k,
    |E(H)| <= C_delta (f+1)^(1+delta) n^(1+1/k) log(n+2)^b_delta.

This is exactly the immutable source.md target under problem.md, including
uniformity in f,k and simultaneous vertex faults. The algorithm has no
fault-query oracle and uses no randomness.

Dependencies, with their precise roles:

* Parter--Popova--Tzalik (PPT), arXiv:2610.33934v1, Sections 4 and 5,
  especially Claim 4.3, Lemma 4.12, Proposition 4.14, Proposition 5.6,
  Observation 5.8, Lemmas 5.9 and 5.14, Theorem 5.15. These supply the
  insertion-witness counting argument; its application to our sequence is
  proved in Section 4 below. Their Theorem 1.4 alone is an existential size
  dependency, not a polynomial-time algorithm for this target.
* Dinitz--Robelle (DR), arXiv:2002.10889v2, Theorems 2, 5, 8 and 9:
  deterministic multiplicative (2t-1) VFT spanners of size
  O(t f^(1-1/t) n^(1+1/t)) and time
  O(m t f^(2-1/t) n^(1+1/t)), for f>=1. Only the unweighted case is used.
* Exterior-algebra representative families are established machinery:
  Fomin--Lokshtanov--Panolan--Saurabh, arXiv:1304.4626v4 / JACM 63(4),
  article 29 (2016), DOI 10.1145/2886094. Section 2 supplies an elementary
  self-contained specialization, so no unverified complexity bound from
  that paper is required.

The novel proposed contribution is the complete parameter-regime compiler:
the f-dependent path representatives become polynomial precisely where a
known multiplicative construction cannot already pay for the desired size.
Neither the exterior algebra, DR's gap cut, PPT's packing analysis, nor the
pendant reduction is claimed as invented here.

## 2. Exact fault-representative path computation

Let J be an N-vertex graph, d<N, f>=0, and T=min(N,f+d+1). Choose a prime
p>=N with p<2N (N>=2) by deterministic trial division; this takes polynomial
time in N. Assign distinct elements alpha_v in F_p to vertices, and use the
T-by-N matrix whose v-th column is
(1,alpha_v,...,alpha_v^(T-1)). Any at most T distinct columns are independent
by the Vandermonde determinant on their first rows.

For a vertex support A of size h<=T, use the exterior vector w(A), with
coordinates the h-row minors of these columns ordered by vertex label.
For any family of h-sets keep actual members corresponding to a linear
basis of these vectors. This preserves avoidance of every Y of size<=T-h:
if A avoids Y, then w(A) wedge w(Y) is nonzero. Express w(A) as a linear
combination of the kept vectors. At least one kept vector has nonzero wedge
with w(Y), so its support avoids Y. If a support intersects Y its wedge is
zero; if it avoids Y the at-most-T distinct columns are independent. This
proves both assertions used in this argument, over the finite field exactly.

For each start x, initialize the family at x to path (x), and other endpoint
families empty. At stage i=0,...,d-1, append one neighbor to each stored
simple i-edge path, rejecting repetitions, and reduce the candidate family
separately at each new endpoint using the basis rule. Store actual paths.
Inductively the resulting family at endpoint v represents all simple i-edge
x-v paths against Y of size<=T-(i+1). Indeed, for a full candidate extension
Q followed by v and a forbidden Y disjoint from that extension, apply the
previous invariant to Y union {v}. A kept parent path avoids this set, can
be extended to v, and still avoids Y. The subsequent basis reduction
preserves this fact. The initial invariant is immediate. No path count,
enumeration of all paths, or probabilistic identity test is involved.

At i=d this represents avoidance of every fault set F of size<=f that is
disjoint from some full d-edge path. If T=f+d+1, this is the displayed rank
budget. If T=N, such an F has size<=N-d-1=T-(d+1), even when f is larger.
Do this for all starts and keep the family for each unordered pair x<y.
Undirectedness permits choosing this orientation without losing a witness.

Let L=max_(1<=h<=d+1) binomial(T,h). Each endpoint has at most L stored
paths. Each stage has at most 2|E(J)| L<=N^2 L candidate extensions per
start. Computing every minor by elimination, followed by a basis reduction,
uses a fixed polynomial in N,d,L,log N field/bit operations. For example
O(N^3(d+1)^4 L^3) field operations, plus polynomial overhead, suffices for
all starts: each candidate uses O(L(d+1)^3+L^2) field operations. Field
operations have polynomial bit complexity in log N. The important bound is

    L <= (f+d+1)^(d+1),
    total time N^O(1) (f+d+1)^O(d+1),

where these O constants are absolute. If d>=N the families are empty and
there is no simple length-d path. The final algorithm below only calls
nontrivial instances with d<N. The test implementation uses prime 101
because its largest N is 18; the general algorithm chooses p as just stated.

## 3. Constructing a d-to-r spanner from the families

Fix r>=d. For every stored path P, with endpoints x,y and protected set
S=V(P), run the following test on the current H, initially empty.
Set C=empty. For j=0,...,f, find a shortest x-y path Q in H-C using BFS.
If none has length<=r, return C and insert every edge of P into H.
Otherwise let B=V(Q) minus S. If B is empty, reject P. If j=f, reject P.
In all other cases replace C by C union B and repeat.

Every returned C avoids P and has size<=(r-1)f: the terminals belong to S,
so a Q of length<=r contributes at most r-1 unprotected vertices per round.
It has dist_(H-C)(x,y)>r by the final BFS. Every insertion adds a new edge,
since otherwise protected P would already give distance d<=r in H-C.

A rejection certifies absence of any cut F of size<=f avoiding S with
dist_(H-F)(x,y)>r. In the B-empty case Q survives every such F. In the
other rejection case we have f+1 earlier/last nonempty sets B, pairwise
disjoint since later Q avoids all previous B. Every admissible F making
distance>r must hit each B, impossible with at most f vertices. This is the
protected version of DR's elementary gap-cut argument.

Scan each family once in any fixed computable order. For final correctness,
fix |F|<=f and an x-y path of length d in J-F. Section 2 provides a stored
P avoiding F. If inserted, P survives. If rejected, the preceding certificate
gave distance<=r in the then-current H-F; adding edges preserves it.
Thus the final H has distance<=r for every such pair and F. In particular it
is an f-VFT d-to-r spanner (indeed it handles all length-d path witnesses,
whether or not geodesic). This proves the simultaneous guarantee without
enumerating faults in the construction.

The time is at most the Section 2 bound plus O(N^2 L (f+1)(N+|E(J)|)).
Every inserted P_i has an explicit fault witness C_i disjoint from P_i,
|C_i|<=(r-1)f, and distance>r in the preceding union of inserted paths.
No claim that our H is a subgraph of a full greedy run is needed or made.

## 4. Packing transfer: what is actually required from PPT

Fix 0<eta<=1/4, k>=4, d=floor(sqrt k), and r=ceil(12k/eta).
For ANY finite sequence of simple d-edge paths P_i and faults C_i with

    H_1=empty, H_i=union_(j<i)P_j,
    C_i disjoint from V(P_i), |C_i|<=q,
    dist_(H_i-C_i)(ends(P_i))>r,

their union has Otilde_eta(q^(1+eta) N^(1+1/k)) edges, provided q>=1 and
k=O(log(N+2)). Log factors have bounded exponents depending only on eta.
Here and below Otilde does not hide a factor growing exponentially in k.

Here is the reduction of PPT's counting proof to precisely these hypotheses.
Write a=sqrt k, t=ceil a, R=ceil(a/eta), s=2R-1. Then s<=r/d. Claim 4.3
still gives an s-critical edge on every P_i: otherwise the d detours in
H_i-C_i concatenate into a route of length<=ds<=r. Apply their analytical
Algorithm 2 to this sequence with fault parameter q and
D=ceil(12 C' s^3 q^(1+eta) N^(1/k)), where C' is their fixed absolute
constant large enough for Lemma 5.14. This system is for analysis only;
the construction never computes its potentially numerous paths.

Lemma 4.12's induction uses the existing path system in H_i, one critical
edge, its compatible fault witness of size<=q, the prepend/filter update,
and the numerical D>=4s^2q. Its path-exchange Lemma 4.16 is stated for an
arbitrary graph and critical pair. Its proof and each of the I1--I7 induction
steps (printed pp.31--34) do not refer to an omitted path, a rejected test,
geodesicity, completeness of a scan, or order of endpoint pairs. In
particular a critical edge is absent from H_i, so first-neighbor insertions
used in I2/I4 and progress are distinct as in that proof. Thus the identical
induction applies to this sequence. Theorem 4.5 gives

    |local insertions| = O(N D s)
                       = O_eta(s^4 q^(1+eta) N^(1+1/k)).

Proposition 4.14 and its Appendix A proof use just that analytical system:
freeze the first full R-path family at each vertex, sample a set of centers,
and apply Lemma A.1 and a union bound over vertices. The center choice is
existential in the edge-count proof; it is not a randomized algorithmic
step. The same families lie in H_i by I1 and monotonicity. For every remaining
insertion P_i it provides two length-R center families, each C'sq-spread,
and the two prefix/suffix distance bounds in H_i-C_i.

To track uniform factors explicitly, the center probability in Lemma A.1 is

    p=min{11 (10C'sq/D)^R log(100*2^(R+2)*D^R*N), 1}.

With the chosen lower bound on D, put
M=log(100*2^(R+2)*D^R*N). Then 10C'sq/D <= (5/(6s^2)) q^(-eta)N^(-1/k).
The proof of Proposition 4.14 therefore supplies centers satisfying

    |S| <= 22 M q^(-eta R) N^(1-R/k).

This also holds when p=1: then 11(10C'sq/D)^R M>=1, and the same upper
bound on the ratio shows that its right side is at least N. In the
nontrivial case q<N, log D=O_eta(log(N+2)), R=O_eta(sqrt k), so M is
polylogarithmic in N under k=O(log(N+2)). The factor (5/(6s^2))^R was
dropped only because it is at most 1. Thus no positive constant to the
power sqrt k is being hidden as a polylogarithm here.

Observation 5.8 uses the same witness-distance contradiction and triangle
inequality. Since our r>=12k/eta, all its strict lower and upper bounds
remain true. Lemma 5.9 consequently produces exactly the same evolving
virtual multigraph: every virtual edge has a path in H_(i+1), avoids C_i,
and has prior virtual distance>2t-1 under C_i. Lemma 5.14 converts the
two spread families into the robust sunflower with kernel the middle
subpath of P_i; the kernel size is at most w=d+1. Its hypotheses use only
the spread bounds, |C_i|<=q, and C_i disjoint from P_i. They hold here.
Theorem 5.15 is expressly a theorem for arbitrary iterative robust CLFT
inputs, and bounds these remaining rounds by

    O(w q^w |S|^(1+1/t)).

The q exponent is w-eta R(1+1/t)<=1 because eta R>=a>=d.
The N exponent (1-R/k)(1+1/t)<=1 because R/k>=1/(t+1).
Since 1+1/t<=3/2, the factor (22M)^(1+1/t) is polylogarithmic.
Thus the remaining rounds are Otilde_eta(w q N). Combining the two classes
and multiplying by d edges per inserted path proves the asserted bound.

For q>=N the bound is immediate from |E(H)|<=N^2<=q N; the preceding
analysis is unnecessary. Empty center sets cause no issue: the global
families are nonempty, so then there are no global rounds. For f=0 use
q=1 in this counting statement, since every insertion witness is empty.
For f>=1 use q=(r-1)f. We have therefore proved that Section 3's output has

    |E(H)| <= Otilde_eta((1+(r-1)f)^(1+eta) N^(1+1/k)).

This proof records the exact extension to a partial path scan. The long park
and robust-sunflower theorems themselves are credited dependencies from PPT,
not new theorems purportedly checked by the finite experiment.

## 5. All scales, including surviving faults

For ell=0,...,d-1 attach a private ell-edge pendant chain to each vertex of
the BASE graph G. Let J_ell be this graph; N_ell=(ell+1)n<=dn. On J_ell run
Section 3 with the SAME d,r,f and retain only its edges with both endpoints
in V(G). Take the union H of these d projected subgraphs.

Fix an original fault set F subset V(G), |F|<=f. If u,v in G-F have distance
b=d-ell>=1, let v' be the pendant tip at v (v'=v for ell=0). In J_ell-F,
dist(u,v')=b+ell=d; surviving pendant chains do not create shortcuts.
The d-to-r guarantee gives an H'_ell-F route to v' of length<=r. A shortest
such route is simple and must enter the private chain at v and traverse
all ell edges. Its preceding segment lies in the base graph, as excursions
into other pendant chains cannot occur in a simple route. Hence the
projected spanner gives distance<=r-ell for every such surviving pair.
No fault set containing new pendant vertices was substituted for F; the
augmented guarantee includes F itself.

Segment a shortest G-F path into length-d subpaths and a final b<d remainder.
Every subpath is geodesic in G-F. The ell=0 projection supplies length<=r
for each full segment; the ell=d-b projection supplies length<=r-(d-b)
for a nonempty remainder. Therefore

    dist_(H-F)(u,v) <= (r/d) dist_(G-F)(u,v)+r.

By Section 4, its edge count is at most

    d * Otilde_eta((1+(r-1)f)^(1+eta) (dn)^(1+1/k)).

This is PPT Appendix B's pendant reduction with all vertex-fault
quantifiers supplied explicitly. It preserves subgraph edges: pendant
edges are removed, no emulator or weighted edges are introduced.

## 6. Uniform polynomial construction and final parameter switch

Handle n<=2 by returning G. For n>=3 replace f by min(f,n-2), which leaves
the requirement for distinct surviving pairs unchanged. Larger given fault
sets with surviving distinct endpoints already have size<=n-2. Cap k at

    K=ceil(log_2(n+2)), computable using integer bit lengths.

If the given k>K, using K costs at most a factor 2 in n^(1+1/k), since
n^(1/K)<=2 and n^(1+1/k)>=n. Its stretch and additive bounds only improve.
This choice of logarithm instead of the possible natural-log cap in
problem.md is an algorithmic boundary choice, not a change to the target.
In the rest of this section k denotes the capped integer.

Set eta=min(delta/2,1/4). For k<=3 use DR with multiplicative parameter k
and fault input max(1,f). It is valid for the requested f and has
O(k max(1,f)^(1-1/k) n^(1+1/k)) edges. Its stretch 2k-1<=3 sqrt k in this
bounded range. Its deterministic time is polynomial, uniformly.

For k>=4 put d=floor(sqrt k), r=ceil(12k/eta). If f>=1 and

    f^(eta*d) >= n,

use DR with multiplicative parameter d and fault input f. Its edge count is

    O(d f^(1-1/d) n^(1+1/d))
      <= O(d f^(1+eta-1/d) n)
      <= O(d (f+1)^(1+delta) n^(1+1/k)).

Its multiplicative stretch is 2d-1<=2 sqrt k, and its time bound above is
uniform polynomial since d<=sqrt K, f<=n, m<=n^2. The switch can be tested
exactly: if eta=a/b in lowest terms, compare integers f^(a*d) and n^b.

Otherwise use Section 5. Now f=0 or log f < log n/(eta*d). Since
f+d+1<=(f+1)(d+1),

    (d+1) log(f+d+1)
      <= (d+1) log(f+1)+(d+1) log(d+1)
      <= O_eta(log(n+2)).

For f>=1, use log(f+1)<=log 2+log f, (d+1)/d<=2, and
(d+1)log(d+1)<=2d^2<=2K. For f=0 the first term vanishes. These elementary
bounds prove that the representative construction, with its ABSOLUTE
exponents from Section 2, is polynomial in n with exponent depending only
on eta. There are d<=sqrt K augmented graphs, each N<=dn<=n^2; use the
BASE n for the switch. BFS tests have f<=n and do not introduce another
exponent depending on d. There is no exponential fault enumeration in the
algorithm; that enumeration occurs only in the finite verification script.

Its size bound from Section 5 is

    Otilde_eta((f+1)^(1+eta) n^(1+1/k)),

because r=O_eta(k), d<=sqrt K, and every additional displayed factor in
d,k is polylogarithmic in n. This is at most the requested delta bound.
Its stretch r/d=O_eta(sqrt k) and additive r=O_eta(k), since k>=4 gives
d>=sqrt k/2. The f=0 case is included by q=1 in the packing analysis;
returning a dense graph merely because f=0 is never used.

Reading the binary encodings of very large input k,f and capping them costs
polynomial input time. The construction is deterministic on every input;
thus no success probability, expected-time cap, or simultaneous-event
argument is left to establish. Constants depend only on the fixed delta.
For any real delta in (0,1), choosing a smaller fixed rational delta'
implies the same existence statement by monotonicity in f+1.

## 7. Validation, limitations, and proposed contribution

The new exact test research3_full_checks.py constructs the representative
families, applies the protected cut scan, builds all pendant scales and
projects their union, and checks every fault set of size<=f in each finite
instance. It also implements DR's modified multiplicative greedy and checks
its stretch. Coverage: all labeled graphs on n=2,3,4; 10 fixed masks each
on n=5,6; d=1..min(3,n-1), f=0..min(2,n-2), and distinct radii among
d,d+1,2d+1,48d^2. The last radius matches eta=1/4,k=d^2; the smaller radii
are deliberately stronger tests of implementation correctness, not of
Section 4's sparsity theorem. Largest augmented N=18.

All 3,160 mixed constructions passed; there were 6,248 d-to-r runs,
23,909 independently checked insertion witnesses, 809,892 exact checks of
rejection certificates, 560,240 exact d-to-r distance comparisons, and
57,856 final mixed-distance comparisons. The DR tests gave 1,848 runs and
33,763 comparisons. There were no failures. These are finite code checks,
not proofs of asymptotic sparsity or novelty. No unbounded exhaustive graph
search is claimed. The general field choice and runtime are proved above.

The prior conditional separator barrier and failed fault-oblivious list
route remain correct diagnostics at their stated scope; they do not refute
this algorithm. Its separator cost depends on f to a power proportional
to d, and so never supplies the forbidden arbitrary-f F(d)poly(n,f) oracle.
The large-f branch is essential to making that cost uniformly polynomial.

Current bounded primary-source checks are recorded in research3-sources.md.
The proposed delta over the nearest results is a uniform deterministic
polynomial construction at PPT's almost-linear fault overhead and
O(sqrt k),O(k) stretch, where PPT explicitly leaves a running-time
improvement open. It adds neither a better size nor better stretch theorem.
The substantive mechanism is the complementary use of a standard but
f-dependent exact representative DP and an existing multiplicative spanner;
neither constituent alone has the full target's uniform size/time/stretch.
Whether this combination has sufficient independent novelty and theoretical
significance under the user's standard must be decided by a fresh critical
review. No numerical acceptance probability or venue-level verdict is made.

Known mathematical gaps in this proposed proof: none identified by this
research pass. This is not a correctness certificate; the fresh referee's
decisive task is to attack Section 4's transfer, the uniform factors in its
center bound, and the complete parameter switch against the cited primary
results. No manuscript/PDF is authorized by this proposal.
