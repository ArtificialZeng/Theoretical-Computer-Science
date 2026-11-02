# Research pass 1: separator obligations and a method-class obstruction

Job: `c029-vftfast-research-6281f7685c7a`. Original status: unresolved.
This is research evidence, not a manuscript, novelty claim, or acceptance.
The immutable question in source.md is unchanged. No full algorithm is proved.

## 1. Protected fixed-path gap cut (proved; routine adaptation of DR2020)

Let H be an undirected unweighted graph, x,y distinct vertices, S a protected
vertex set containing x,y, r>=1, and f>=0. The following procedure either
returns a cut C disjoint from S with |C|<=(r-1)f and dist_(H-C)(x,y)>r,
or correctly certifies that no such protected cut has size <=f.

Start C empty. For j=0,...,f, find a shortest x-y path Q in H-C. If none has
length <=r, return C. Put B=V(Q) minus S. If B is empty, certify absence:
this Q survives every allowed cut. If j=f, certify absence. Otherwise add B
to C and continue. The f+1 nonempty sets B encountered in the last case are
pairwise disjoint: every later Q avoids the previously deleted B's. Every
cut avoiding S and hitting all these Q's must hit every B, requiring at least
f+1 vertices. The successful branch deletes at most r-1 vertices per round,
because both terminals are protected. Time is O((f+1)(|E(H)|+|V(H)|)), including
the possible early exit, with explicit BFS and vertex masks. If r=1 the same
proof handles a terminal edge by the B-empty branch.

Taking S=V(P) proves that path protection does not invalidate the usual
length-bounded-cut gap guarantee. It does not choose P. This is an elementary
adaptation of Dinitz--Robelle, Theorem 4 / Algorithm 2, not an innovative result.

## 2. What a joint separator would buy (conditional positive reduction)

Work with 0<delta<1/2 without loss: for a larger frozen exponent use a smaller
fixed source parameter and monotonicity in f. Set d=floor(sqrt(k)) and
r=ceil(12k/delta), for k>=4. Suppose a deterministic
polynomial-time separator, for any H subset G, either returns a simple
length-d path P in G and C disjoint from V(P), |C|<=q=ceil(c*r*f), with
dist_(H-C)(endpoints(P))>r, or certifies there is no original-budget violation
F with |F|<=f, dist_(G-F)(x,y)=d, and dist_(H-F)(x,y)>r.
Here c is an absolute constant >=1. This completeness requirement is weaker
than the earlier all-length-d-path separator: only shortest-path violations
must be detected. It remains sufficient for the full original problem.

Repeatedly insert a returned P and stop on a valid certificate. Every
insertion contains a previously absent edge: otherwise its protected P was
already present in H-C and had distance <=d<=r. Thus there are at most |E(G)|
insertions and one final separator call. At termination the certificate is
exactly the f-VFT d->r guarantee. There is no enumeration or free oracle in
this conditional algorithm; separator cost is the unresolved part.

Size transfer uses the witness-sequence form of the source analysis, not an
assertion that this output is a subgraph of a different greedy run. Its inputs
are H_i=union_(j<i)P_j, |C_i|<=q, C_i disjoint from V(P_i), and
dist_(H_i-C_i)(endpoints(P_i))>r. Source Claim 4.3, Algorithm 2 / Lemma 4.12,
Proposition 4.14, Proposition 5.6, Observations 5.8 and Lemmas 5.9/5.14, and
Theorem 5.15 use these insertion conditions and earlier/later indices; none
requires a skipped path to have passed a test or endpoints to be scanned in a
particular order. Therefore the same arguments apply to a finite adaptive
witness sequence with the common budget q. This is an application of that
source analysis, not an independent certification of its long base proof.
Theorem 5.4's bound consequently has q substituted for f. Inflating q to O(r*f)
costs O_delta(k^(1+delta)) in the fault factor, a polylogarithm after capping k.
For q beyond the number of available faulty vertices, use the smaller effective
budget; monotonicity still gives the displayed upper bound. For f=0 this
conditional reduction is unnecessary; use a qualifying nonfaulty construction.

All Appendix B scales can be obtained without assuming the same bound for
every shorter d directly. For ell=0,...,d-1, attach to EACH base vertex a
private length-ell pendant path. The enlarged graph has N=(ell+1)n vertices.
Construct its f-VFT d->r spanner by the hypothesized separator. Retain only
base edges. Given a base fault set F and base vertices u,v at distance d-ell
in G-F, F deletes no pendant vertices, u,v survive, and the tip v' satisfies
dist_(G'-F)(u,v')=d. A surviving H'-F route of length <=r to v' must enter its
unique pendant at v; its base part has length <=r-ell. This proves the required
base f-VFT (d-ell)->(r-ell) guarantee. The union of the d base spanners,
by segmenting each shortest G-F path into d-edge pieces and its remainder,
has dist_(H-F)(u,v)<=(r/d)dist_(G-F)(u,v)+r. Its edge count is at most
d times the d->r bound on dn vertices: the extra factors in d,k are polylog(n).
Graphs and run counts stay polynomial. This reduction covers all fault sets
simultaneously; pendant-fault configurations are not being substituted for
base faults. Boundary k<4 and the logarithmic k cap are handled as in problem.md.

Thus polynomial-time shortest-violation separation plus the cited source
analysis WOULD imply the immutable target. Neither this assumption nor its
negation has been proved here.

## 3. Fault-oblivious exact-length path lists can be enormous

**Proved obstruction for a specified method class, not original hardness.**
Fix p>=1, f>=1, d=p+1 and r>=max(d,2). Let U have p+f vertices. Let G be the
complete graph on U union {x,y}, except for the edge xy. Consider any list R
of simple length-d x-y paths selected from G BEFORE seeing H. Suppose the list
has the following property for every H subset G: whenever a length-d path P
and an f-vertex fault set F avoiding P satisfy dist_(H-F)(x,y)>r, some Q in R
admits a cut C avoiding Q with dist_(H-C)(x,y)>r. Allow C arbitrarily large.
Then R contains paths with all binomial(p+f,p) possible internal vertex sets.

Proof: for each p-set A subset U, let F_A=U minus A and let H_A consist
exactly of the edges xz,zy for z in F_A. Any ordering of A gives a simple
length-d path P_A in G-F_A, and H_A-F_A disconnects x,y. If Q has internal
set T different from A, some z belongs to T minus A. The two-edge H_A path
x-z-y is entirely protected by Q, so it survives EVERY C disjoint from Q.
It has length 2<=r. Consequently the only eligible paths in R have internal
set exactly A. This holds for every A and proves the lower bound.

This is stronger than just observing the usual binomial bound for uniform
matroid representatives: even unlimited witness inflation cannot repair an
omitted support in this fault-oblivious list model. Different orderings of the
same support do not help. It does not prohibit H-dependent path choices,
implicit algebraic methods that never materialize such a list, or an algorithm
that handles this graph directly. No computational hardness assumption is used.
The basic complement argument is elementary and no independent novelty is claimed.

For a formal uniform-time scaling, pad with isolated vertices to n=ceil(exp(d^2))
and take f=floor(n^a) for fixed 0<a<1, with k=d^2<=ceil(ln(n+2)). Since
binomial(f+p,p)>=(f/p)^p, the list has n^(a*p-o(p)) members and is not bounded
by any fixed polynomial in n. Padding has no effect on the fixed-endpoint
statement. This family may be easy for the original construction (including
sparsity shortcuts); it proves no lower bound for the original graph problem.

**Crucial limitation / changed next test.** For p>=2,
dist_(G-F_A)(x,y)=2<d. Thus the large-list witness is NOT a shortest-distance-d
violation. The lower bound therefore does not exclude a shortest-violation
separator as in Section 2. A further necessary property is useful: every
shortest path in G-F is an induced path of G, because a chord between its
nonconsecutive vertices would survive F and shorten the path. Inducedness is
only necessary: longer alternative shortcuts through unprotected vertices
can still prevent a path from being shortest. Ordinary simple-path color
coding therefore does not establish this restricted separator either.
This is a specific remaining positive route, rather than an excuse to treat
the failed list method as a negative answer.

## 4. Verification and actual research status

`research1_checks.py` checks the protected gap procedure against exact subset
enumeration on every labeled H with at most five vertices, all terminal pairs,
all protected sets containing them, radii 1..4, and budgets 0..2. It separately
checks the displayed lower-bound family for p,f in 1..4. Its JSON records exact
coverage and failure counts. These finite checks supplement the proofs and
do not certify an infinite algorithm or the source's packing theorem.

The unresolved kernel is polynomial-time SHORTEST-VIOLATION separation as
specified in Section 2. One next test: construct or diagnose that separator
using H-dependent length-bounded-cut packings, with completeness only for
dist_(G-F)(x,y)=d, output budget O(r*f), and actual path protection. A sufficient
time bound is 2^O(r+d*log(d+2))*poly(n,f,r), with fixed polynomial exponents,
which becomes polynomial under k<=ceil(ln(n+2)); an f^d or n^d bound fails.
The decisive output is an explicit separator and proof, or a shortest-path
witness defeating its stated rule. The nongeodesic example above cannot
decide this new kernel. Original status remains unresolved.
