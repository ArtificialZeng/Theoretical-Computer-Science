# Full-range decrease-only MST: proposed quadratic-log resolution

Research proof dossier, job c040-mstdecfull-research-e695ca56645f, accumulated pass 2 of 3.
This is a proposed proof for fresh critical review, not a referee report or
manuscript. The unchanged original is source.md. All logarithms in algorithmic
parameters below are implemented by integer doubling. No true queries occur.

## 1. Statement and parameters

For every rational 0<q<=1 there is an explicit deterministic algorithm using
only the observed matrix D. If each unordered pair is independently marked
with probability p<=1-q and marked observations may be decreased arbitrarily,
the algorithm always returns a spanning path and has

    E_mask[cost_d(P)] <= C_q max(1,log_2 n)^2 MST(d).

Every execution uses at most n^(a_q max(1,log_2 n)) exact arithmetic/comparison
and bit operations, independently of the aspect ratio. One may take
C_q=10^15 q^-5 and a sufficiently large implementation constant a_q
as detailed in Section 9.
In particular this proves the weaker fourth-power bound in source.md for
every fixed p<1, by hardwiring any rational 0<q<=1-p. Randomness of the
algorithm is unnecessary; its private-bit cost is zero. These constants
are deliberately loose, and the operation model is that of source.md,
not unit-bit arithmetic on arbitrary real numbers.

Set h=log_2 n, ell=ceil(h), r=ceil(80 q^-2 ell),
R=ceil(128r/q), tau=1-q/8, A=32 and beta=256.
Thus r<=81q^-2 ell, R<=11000q^-3 ell and r/R<=q/128.
For n=2 output its unique edge. If R>n, output the label-order path.
The latter has true cost at most (n-1)MST(d)<R MST(d), already within the
claimed bound. In all subsequent cases R<=n. An optional separate A_0
for p=0 can simply compute an exact MST of D; the displayed algorithm
also meets the claimed approximation when p=0.

## 2. A uniform mask event, independent of adversarial choices

Let E be the event that every two disjoint subsets U,V with |U|,|V|>=r
have at least (q/2)|U||V| unmarked cross pairs. For fixed sizes a,b, the
cross indicators are independent with unmarked probability 1-p>=q.
Hoeffding's inequality gives failure probability at most exp(-q^2 ab/2).
Since ab>=r(a+b)/2, and there are at most n^(a+b) choices,

    Pr[E fails] <= sum_(a,b>=r)^n exp((a+b)ln n-q^2 r(a+b)/4)
                 <= sum_(a,b>=1) n^(-27(a+b)) < n^-20.

Here q^2 r/4>=20 ell>=20 ln(n)/ln(2), so the exponent coefficient is
strictly larger than 27; the final geometric bound holds for n>=2.
If the relevant disjoint sets do not exist, E is vacuous. E is a property
only of the original mask, and holds simultaneously for all metrics and
all observations compatible with that mask. We never condition on an
adaptive seed or assert independence of observations.

An observed seed at scale s is any R-set S with D_uv<=s for all distinct
u,v in S. On E, such a seed admits a hidden center z_S in S and a set
G_S={x in S:d(x,z_S)<=2s} of size at least R-r. Indeed split S into
halves of sizes floor(R/2),ceil(R/2), both at least r. Some z in the
first half has at least qR/4>=32r unmarked neighbors U in the other
half. Each such neighbor is within true distance s of z. If r points
F of S were at distance >2s from z, then U and F would be disjoint,
and every U--F true distance would exceed s. All their observed
distances are <=s, so every cross pair would be marked, contradicting E.
Choose a center once when a seed is first used and retain it thereafter.
The algorithm does not know or use the center. In later comparisons its
radius bound may be taken either at its birth scale or at a larger scale.

## 3. Quantiles and complete overlap handling

For a finite list of M numbers its tau-quantile is order statistic
k=ceil(tau M). Define Q(x,S) on the R entries D_xs, including diagonal
zero when x belongs to S. Define Z(S,S') on the R^2 ordered entries
D_ss', including repeated unordered pairs and diagonals if the sets
overlap. These definitions apply also to S=S'. Do not replace the
latter quantile by a special artificial zero value.

Suppose seeds S,S' have hidden centers and core-radius bounds 2s,2s'.
The following assertions hold simultaneously on E:

    Q(x,S) <= d(x,z_S)+2s;                                      (1)
    |Z(S,S')-d(z_S,z_S')| <= 2s+2s'.                           (2)

For (1), at least R-r>tau R entries have the stated upper bound,
using D<=d. For the upper half of (2), at least (R-r)^2 entries are
core--core entries with the stated upper bound. Their fraction is
at least (1-r/R)^2>tau. For the lower half put
l=d(z_S,z_S')-2s-2s'. If l<=0 it follows from nonnegativity. If l>0,
the two cores are disjoint, even if the original seeds overlap. E
gives at least (q/2)(R-r)^2>(q/8)R^2=(1-tau)R^2 unmarked
core--core entries, each at least l. Because the cores are disjoint
these entries correspond to distinct unordered pairs; independence
is used only in proving E. If more than (1-tau)M entries are >=l,
fewer than tau M entries are <l, so the ceil(tau M)-th entry is >=l.
This also proves the needed integer-rounding statement. In particular
overlapping and identical seeds require no unproved extension of a
disjoint-seed comparison.

We also need the following set, rather than pointwise, soundness:

    fewer than r points x in X have both Q(x,S)<=B
    and d(x,z_S)>B+2s, for any real B>=0.                       (3)

If there were r such points F, they would be disjoint from G_S.
Each x has at least ceil(tau R) observed-small entries and hence at
most R-ceil(tau R)<=qR/8 observed-large entries. Every unmarked edge
from x to G_S must be observed-large. Thus F--G_S has at most
|F|qR/8 unmarked pairs. E requires at least (q/2)|F||G_S|, which
is strictly greater since |G_S|>=R-r>R/4. This is a contradiction.

## 4. Explicit observable algorithm

Let U=max_(u<v) D_uv. If U=0 return the label-order path. Otherwise
put lambda=2U/n^2, D*_uv=max(1,D_uv/lambda) off the diagonal,
D*_uu=0, and L=ceil(log_2 n^2). The algorithm constructs L+1 nested
partitions, with C_0 singletons and C_L={X}. All scales and quantiles
in the rest of the construction refer to D* and t_i=2^i.

For every scale i and every observed seed S at t_i define the observable
predicate F_i(S,x): for every j in {i,...,L} and EVERY R-set S' that
is an observed clique at t_j, require

    Q(x,S') <= A t_i + Z(S,S') + 4 t_j.                       (4)

There is no restriction on intersection between S,S', or on x belonging
to them. A fresh seed S is admissible at i exactly when it is an observed
clique at t_i and F_i(S,x) holds for every x in S.

At each i=1,...,L-1 the active objects initially are all clusters from
C_(i-1). Each nonsingleton object carries its representative R-set seed;
every singleton object is its point. Active objects are pairwise disjoint
as subsets of X. Output clusters from this scale are held separately and
are never reinserted into the active list at the same scale.

While there is an active old-seed object, choose the lexicographically
first representative S. If there is none, choose the lexicographically
first admissible R-set of active singleton points, if one exists;
otherwise stop. With the chosen S make one output cluster by taking:

* its own active old object, if it has one;
* all other active old objects with representative S0 satisfying
  Z(S,S0)<=A t_i;
* every active singleton x with Q(x,S)<=A t_i and F_i(S,x).

Take the union of the full underlying objects, remove exactly these objects
from the active list, and give the output cluster representative S. Fresh
seed members are included because their Q(x,S)<=t_i and admissibility
ensures F_i(S,x). Each iteration removes at least one active object.
At termination carry remaining singletons and the separately held output
clusters into C_i. This is a nested partition, and every nonsingleton
cluster contains its R-set representative, which remains a clique at
all larger scales. Force C_L={X} with hidden core X. Finally order
children of every cluster by their least point label, list singleton
leaves in depth-first order in the CLUSTER tree, and connect consecutive
leaves. This is a deterministic spanning path on every input.

For use in the analysis, on E a point satisfying
d(x,z_S)<=(A-2)t at current scale t always passes both carving tests
relative to S. First (1) gives Q(x,S)<=At. For any future S' at t',
(1), the triangle inequality and the lower half of (2) give

    Q(x,S') <= d(x,z_S)+d(z_S,z_S')+2t'
             <= (A-2)t+Z(S,S')+2t+4t'
             = At+Z(S,S')+4t'.                              (5)

The radius 2t is a valid upper bound for the carried seed's core even
if it was born earlier. In particular every true-diameter-at-most-t
R-set is admissible: its hidden center belongs to that set, so each
of its points is within true distance t<=(A-2)t of the center.

## 5. The global first-absorption invariant

Fix a nonsingleton cluster C created at scale t and represented by S_f.
Every point x in C has a first level t_0<=t at which it ceased to be
a singleton. Let S_0 be the representative selected for that first
cluster, which may itself have been an old seed. By the singleton
carving test, or by fresh-seed admissibility when x was a fresh member,
x satisfied F at t_0 relative to S_0.

Follow the representative along the ancestor chain from this cluster
to C. At each later level s there is at most one representative change,
because outputs do not reenter that scale's active list. If a different
old representative is absorbed, the merge rule and (2) give center
distance at most (A+4)s. If its representative is retained the center
distance is zero. Therefore the total center displacement is at most

    d(z_S0,z_Sf) <= (A+4) sum_(dyadic s<=t) s <= 2(A+4)t.       (6)

The final R-set S_f, even if overlapping or identical to S_0, was among
the future tests at scale t in F_(t0)(S_0,x): it is a clique at t in
the FULL universe, independently of whether it had then been selected.
By (4), the upper half of (2), and (6),

    Q(x,S_f) <= A t_0+Z(S_0,S_f)+4t
              <= A t+2(A+4)t+2t_0+2t+4t
              <= (3A+16)t = 112t.                           (7)

The birth scales of S_0,S_f are at most t_0,t respectively; their fixed
birth centers justify exactly the radius bounds used here. Apply (3)
with B=112t. Fewer than r points of the ENTIRE set {x:Q(x,S_f)<=112t}
are farther than 114t from z_Sf. Consequently removing fewer than r
points from C leaves a hidden core of diameter at most 228t<256t.
Its size is at least R-r>r. This controls the entire merged cluster,
not one incoming object at a time. Every singleton has empty core and
one outlier. Non-root nonsingletons have fewer than r outliers. No
outlier count is added across merges. The forced root has core X.

## 6. Weighted number of clusters

Write W=MST of the current true metric. Distinct representatives chosen
at one level t have centers at distance >(A-4)t=28t. Indeed suppose
an earlier selected S and a later selected S' had closer centers.
If S' was an active old object, (2) would imply Z(S,S')<=At, so it
would have been removed. If S' was fresh, every point in its hidden
seed core was within 2t+28t=(A-2)t of z_S. By (5) it would have
passed both singleton tests and been removed when S was selected,
contradicting its later availability. These cases exhaust all choices.

In any metric, k points at pairwise distance >delta satisfy
k<=1+2W/delta: shortcut a doubled true MST into a cyclic tour of
these points; for k>=2 its k consecutive distances are >delta and
their sum is <=2W. This argument uses centers only for analysis.
Hence the number K_i of seed-generated clusters is at most
1+2W/(28t)<=1+W/t.

No true-diameter-t set contains R leftover singletons, since that
R-set would be admissible by (5) and the algorithm could not stop.
Greedily choose uncovered leftover points and cover them by true
radius-t/2 balls. Their centers are >t/2 apart, so there are at most
1+4W/t balls. Each ball has true diameter <=t and therefore at most
R-1 leftovers. If there are no leftovers use zero balls. It follows
that

    |C_i| <= R+4R W/t_i.                                    (8)

Assume for now that the normalized true metric has minimum distance
at least 1 and diameter Delta* in [n^2/2,n^2]. Then W>=n-1 and
t_L<2n^2<=4Delta*<=4W. For

    H=sum_(i=0)^L t_i |C_i|,

the bottom contributes n<=2W, the top t_L, and (8) gives

    H <= n+(R+1)t_L+4R(L-1)W <= 14R(L+1)W.                 (9)

Only the number of levels, rather than the numerical aspect ratio,
appears in (9).

### Actual outlier mass, without multiplying by the worst cluster budget

Keep the two categories in the preceding packing argument separate. At an
intermediate level i, K_i is the number of seed-generated nonsingleton
clusters and N_i the number of leftover singleton clusters. These exhaust
C_i, including unchanged old nonsingletons, which are selected or absorbed
and emitted by the same carving loop. Section 5 gives fewer than r outliers
for each generated cluster, and exactly one for each singleton. Thus, with
O_i=sum_(C in C_i) |C minus core(C)|,

    O_i <= r K_i+N_i
        <= r+(R-1) + [r+4(R-1)]W/t_i
        <= 2R+5R W/t_i,                                    (9a)

since r<=R. The bottom has O_0=n; the forced root has O_L=0. Define

    Omega=sum_(i=0)^L t_i O_i.

Under the same normalized scale assumptions as (9),

    Omega <= n+2R sum_(i=1)^(L-1) t_i+5R(L-1)W
          <= [2+8R+5R(L-1)]W
          <= 14R(L+1)W.                                   (9b)

Here sum_(i=1)^(L-1) t_i<t_L<=4W, n<=2W and R>=1.
The sum is zero if there are no intermediate levels. In particular both
H and Omega have the same O(R(L+1)W) bound; replacing each singleton's
one outlier by r would unnecessarily introduce another logarithm.

## 7. Outlier-sensitive deterministic extraction lemma, with proof

Let C_0,...,C_L be any nested partitions with singleton bottom and
one-cluster top, scales 2^i, in any metric. Suppose the root core X has
diameter <=beta 2^L, each non-root nonempty core has size >b and
diameter <=beta 2^i with at most b outliers, and each empty-core
cluster has at most B points, where B>=b>=1. Cores need not be nested
or computable. Treat each level-cluster pair as a distinct node even
when the underlying set repeats at consecutive levels. Put

    H=sum_(i=0)^L 2^i |C_i|,
    o_i(C)=|C minus core_i(C)|,
    Omega=sum_(i=0)^L 2^i sum_(C in C_i) o_i(C).

Any depth-first ordering of the cluster-tree singleton leaves gives a
spanning path P satisfying the actual-outlier bound

    cost(P) <= 2 beta H+12 beta Omega.                      (10)

Proof. Orient each path edge from earlier leaf u to later leaf v. Let
j>=1 be the level of their least common cluster. Promote each endpoint
x from level j to the first containing cluster A_x whose core contains
x, at level k_x. The root core is X, so these levels exist. Let
k=max(k_u,k_v) and D=C_k(u)=C_k(v). Its core is nonempty because the
endpoint attaining k belongs to it. The cores of A_x and D intersect.
If A_x=D or D is the root this is immediate; otherwise A_x is a
non-root cluster with |core(A_x)|>b, while D omits at most b points
and A_x is contained in D. Thus choose w_x in their core intersection.
The triangle inequality and the three core diameter bounds imply

    d(u,v) <= d(u,w_u)+d(w_u,w_v)+d(w_v,v)
           <= beta 2^k_u+beta 2^k+beta 2^k_v
           <= 3 beta 2^k.

If k=j, both endpoints lie in the core of their common level-j
cluster, so d(u,v)<=beta 2^j. Charge this edge to the level-(j-1)
child containing u. Every cluster is a contiguous interval in a
compatible DFS leaf order. The charged edge leaves that interval
to the right; there is at most one such edge. Consequently all these
immediate edges have total cost at most 2 beta H.

If k>j, choose a later-promoted endpoint x (break ties by using u)
and charge C_(k-1)(x). Since k-1>=j, minimality of k_x implies x
is an outlier of that cluster. The edge costs at most
6 beta 2^(k-1). Each outlier point has degree at most two in the
FINAL path, so a level-cluster pair C can receive at most 2o_i(C)
late charges. Summing gives total late-edge cost at most 12 beta
Omega. These two disjoint edge classes prove (10).

In particular Omega<=B H recovers the earlier uniform-budget bound
beta(2+12B)H. The retained charge is valid for arbitrary changing
cores, repeated sets and empty-core clusters; no assumption of core
membership persisting up the hierarchy was used. The path is the leaf
order of the cluster tree, not the first-appearance order of a physical
leader tree. The algorithm requires no access to hidden cores.

For the constructed hierarchy take b=B=r and beta=256. Every singleton
has empty core and size 1; every other non-root core satisfies the
hypotheses by Section 5, and the root bound follows from Delta*<=t_L.
Combining (9), (9b) and (10), on the two stated good events,

    cost_(d*)(P) <= 196 beta R(L+1) MST(d*)
                 = 50176 R(L+1) MST(d*).                  (11)

This holds for every hierarchy and every compatible adversarial
observation satisfying the stated core and scale assumptions.

## 8. Normalization, unconditional expectation and boundaries

Let Delta be the original true diameter and W=MST(d). For a diametral
pair a,b and every other x, choose one of ax,bx of length >=Delta/2.
Together with ab these are n-1 distinct unordered pairs. If U<Delta/2,
every one must be marked. Therefore the scale event G={U>=Delta/2}
satisfies Pr[G fails]<=p^(n-1), uniformly over adversaries. No union
over adversarial choices is needed: one unmarked chosen pair suffices.

For U>0 define off-diagonal d*_uv=max(1,d_uv/lambda), with diagonal
zero. This is a genuine metric: for three distinct points, if the
left side is 1 it is at most the sum of two entries each >=1;
otherwise use the original triangle inequality and monotonicity.
Repeated-vertex triangle inequalities are identities. D*<=d*, and
unmarked entries remain equal after applying the same transform.
Thus the mask event E applies to the transformed instance without
any independence assumption about lambda or D*.

On G, since U<=Delta and lambda=2U/n^2,

    n^2/2 <= Delta*=max(1,Delta/lambda) <= n^2.

All conditions used in (9) and (11) follow. Also

    MST(d*) <= W/lambda+(n-1),
    lambda(n-1) <= 2Delta/n <= 2W/n,
    d_uv <= lambda d*_uv.

So on E intersect G, the original cost is at most
100352 R(L+1) W. On every other mask, including U=0, the output
is still a spanning path, of cost at most (n-1)Delta< nW.
The expected contribution from those masks is at most

    n(n^-20+p^(n-1))W <= (1+1/q)W.

For the final inequality, n p^(n-1)<=sum_(k=0)^(n-1) p^k
<=1/(1-p)<=1/q; p=0,n>=2 also satisfies it literally.
No conditioned distribution of the mask is used. Since L<=2ell,
L+1<=3ell and ell<=2h for n>=2, the good-event term is at most

    100352*11000*3*4 q^-3 h^2 W
    = 13246464000 q^-3 h^2 W.

Adding (1+1/q)W is bounded by 10^15 q^-5 h^2 W, because
0<q<=1 and h>=1. Thus the announced conservative C_q proves the
quadratic rather than cubic logarithm.
The n=2 and R>n branches were verified separately in Section 1.

## 9. Every-execution implementation bound

All integer parameters are obtained with rational arithmetic and loops
over doubling integers; no logarithm oracle or real rounding oracle is
required. Put N=binom(n,R)<=n^R. Enumerate all R-subsets of labels.
For each, check clique status at all L scales. Precompute all Q(x,S)
and all Z(S,S') by sorting lists of lengths R and R^2 and selecting
ceil(tau R), ceil(tau R^2). These ranks are exact rational/integer
computations depending only on q and R. Even quadratic sorting takes
O(R^4) comparisons for each seed pair. Compute all F_i(S,x) by
scanning all j>=i and all clique sets S' at t_j. This is at most
O(L^2 n N^2) table comparisons after the quantiles are available.
It includes ALL overlaps and identical seeds explicitly.

At a level at most n carving iterations occur. Each fresh-seed search
can scan all N R-sets and their point memberships; active objects and
underlying point unions can be represented by label lists or bit vectors.
All copying, tie-breaking, constructing cluster parents, leaf traversal
and writing n-1 edges cost only an additional polynomial factor in n,L.
Since R<=n in this branch and L<=2ell<=2n, the entire implementation
has at most c L^2 n^(2R+6) elementary operations for an absolute
implementation constant c. This is bounded by n^(a_q h) for a constant
a_q depending only on q and the fixed implementation, after also
charging the integer-control overhead below. Indeed
R<=11000q^-3 ell<=22000q^-3 h. Integer control variables have
O(R log n+log L) bits, plus a q-dependent constant. Charging their
elementary bit operations adds only polynomial factors in R,log n.
In particular the fixed routines have a bound c_q n^(2R+k) for
constants c_q,k; choose an integer
a_q>=44000q^-3+k+ceil(log_2(max(1,c_q)))+1. Then n>=2,h>=1
give c_q n^(2R+k)<=n^(a_q h). Both c_q and k are obtained from the
fixed subset enumeration, quadratic sorting, table loops and elementary
integer routines; neither depends on distances, their precision, the
mask, or n. This supplies the required worst-execution constant rather
than a runtime statement restricted to good masks.
The arithmetic values involving D are charged in the required exact
arithmetic/comparison model. No unit-cost rational-bit strengthening
is claimed; input precision must be charged separately in such a model.
There are no private random bits, rejection loops, or aspect-dependent
scale loops. On bad masks the same fixed loops terminate and the forced
root and leaf traversal still give a valid spanning path.

## 10. Dependencies, value and unresolved review questions

The hierarchy, future-seed admissibility idea, normalization and
promotion/intersection charging framework are inherited from Anand,
Gupta, Jayaram, Lee and Vakilian, arXiv:2610.40594v1, Section 6,
especially Theorem 6.2 and Algorithms 1--3. They are not claimed new.
The proposed changes are an all-p high-quantile version with uniform
rectangle control and all overlapping future seeds, together with
deterministic bounded-degree DFS leaf extraction. The latter avoids
the level-summed expected degree of physical random leaders and
removes its log(aspect) factor. Retaining actual outlier counts in that
same charging proof, and separating generated clusters from singleton
leftovers in the weighted sum, removes a second avoidable factor and
gives the quadratic logarithm throughout the full noise interval.
This is one coherent algorithmic contribution, not a separate paper
or an independently established second innovation. Distinct seeds actually
born in the algorithm are globally disjoint: a fresh seed uses singleton
points that cease permanently to be singleton. Defining comparisons for
all overlaps is useful completeness, not the essential new contribution.

No mathematical gap is currently identified in this complete proposed
argument. The candidate still requires a fresh audit of all sections,
current novelty and substantive value. In particular, bounded literature
search is not a priority certificate, and the simplicity of the new
extraction lemma raises a real risk that it is known or value-insufficient.
The old cubic packet and its actual accepted working_paper assessment
are preserved without changes in history/cubic-pass1-20261103T004138Z/.
That review does not cover this strengthened statement. This researcher
supplies no new acceptance, venue judgment or manuscript. The strongest
exact claim requires a new actual freeze and fresh review; working_paper
remains the inherited conservative label, without a venue upgrade.

Theorem 7.2 of the primary is a reduction to quietly planted colorability,
with partial low-degree evidence. It is not a proved consequence of the
Planted Clique hypothesis or a universal polynomial-time impossibility.
Its displayed construction has within-class zero distances; this dossier
does not assert a transfer of that hardness statement to genuine metrics.
The upper proof here does not rely on any hardness result. The adjacent
Fletcher--Hershkowitz SODA 2026 full proof remains inaccessible through
the inspected ordinary routes; its abstract alone cannot exclude an
equivalent auxiliary lemma. All priority and significance language must
retain these limits.
