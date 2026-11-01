# Size-independent sparse coverage bound: proof submitted for review

This is a mathematical evidence packet, not a manuscript or an acceptance.
Its original question and occurrence convention are exactly those in
`source.md` and `problem.md`. All features below are **tagged occurrences**;
two equal incidence subsets can represent two distinct features.

## Statement

Let n,m,t be positive integers and k>=2. For i in [m], let U_i be a finite
set of feature indices, and let S_(i,u) be a nonempty subset of [n] for
u in U_i. Suppose

    sum_i sum_(u in U_i) 1[j in S_(i,u)] <= t  for every j in [n].

Define f_i(T)=sum_(u in U_i) 1[S_(i,u) intersects T]. Then there is a
coloring chi:[n]->{0,...,k-1} with

    max_(i,c,c') |f_i(chi^(-1)(c))-f_i(chi^(-1)(c'))|
        <= 4kt(kt-1)^2.

Thus P(t,k)=4kt(kt-1)^2 is one fixed polynomial independent of n and m.
Empty features may first be deleted; functions with no features and unused
items cause no change to the argument. Empty color classes are permitted.
There are no feature weights or rank restrictions.

The construction is deterministic and polynomial time for explicitly
listed incidences and item slots. A bit-complexity justification is given
after the existence proof. The bound is worse in t,k than the published
O(sqrt(t^3 k) log(ntk)) bound: no assertion of keeping its exponents while
removing its logarithm is made.

## 1. A known multiple-choice rounding fact, with a proof

Let the coordinates of a real vector p be partitioned into finite nonempty
groups, with p>=0 and sum_(a in group) p_a=1 for each group. Let A be any
finite real matrix such that every column has absolute sum at most D>=0.
There is a vector y choosing one coordinate 1 in each group and all others
0 such that

    ||A(y-p)||_infinity <= 2D.                         (1)

For equal group sizes and rational data, this is the standard multiple-choice
Beck--Fiala theorem of Doerr and Srivastav, *Multicolour discrepancies*,
Combin. Probab. Comput. 12 (2003), 365--399, DOI
10.1017/S0963548303005662. The exact rational formulation and polynomial-time
claim are stated as Theorem 2, p.58, in Glaßer, Reitwießner and Witek,
*Applications of Discrepancy Theory in Multiobjective Approximation*,
FSTTCS 2011, DOI 10.4230/LIPIcs.FSTTCS.2011.55. Neither (1) nor its
floating-coordinate proof is claimed new here. The proof follows to make
the mathematical dependency explicit, including groups with zero entries.

Start at x=p, with every value row active, and permanently fix every
coordinate that is 0 or 1. Active rows satisfy A_row x=A_row p.
Let W be the remaining strictly fractional coordinates and V=|W|. Every
group meeting W has at least two coordinates in W: a sum-one nonnegative
group cannot have exactly one strictly fractional entry and other entries
in {0,1}. Let G be the number of these groups; hence G<=V/2.

Drop an active row as soon as its mass sum_(a in W) |A_row,a| is <=2D.
All R surviving rows have mass >2D. If D>0, column summation gives

    2D R < sum_(surviving rows) sum_(a in W) |A_row,a| <= DV,

so R<V/2. If D=0, A=0 and all rows have already been dropped, hence
R=0<V/2 whenever V>0. Consequently R+G<V. There is a nonzero direction
d supported on W that preserves the surviving value equations and all G
group-sum equations. Because all coordinates in W are strictly inside
(0,1), move a positive distance in this direction until the first
coordinate hits 0 or 1. This is a finite positive distance; fix every new
boundary coordinate. No fixed coordinate ever moves again. Recompute W,
drop newly light rows, and repeat. At least one coordinate is fixed at each
move, so this process ends with a vertex y of the product of simplexes.

For any dropped row a, at the deletion time x* we still had
A_a x*=A_a p. Only the then-fractional coordinates W* can move later, and
each changes by absolute value at most 1. Therefore

    |A_a(y-p)| = |sum_(b in W*) A_a,b (y_b-x*_b)|
        <= sum_(b in W*) |A_a,b| <= 2D.

A row never dropped remains exactly at its target, proving (1). Notice
that errors do not accumulate over the floating-coordinate moves: a row
is exact until its single deletion and then has bounded total residual
movement. The threshold is <=2D, so equality and odd V cause no difficulty.

## 2. Protect all large occurrences by disjoint rainbow blocks

Write q=kt>=2. Call an occurrence large when |S_(i,u)|>=q; call every
other occurrence small. For a subfamily Q of large tagged occurrences,
degree counting gives

    kt |Q| <= sum_(e in Q) |S_e| <= t |union_(e in Q) S_e|,

and therefore |union_(e in Q) S_e|>=k|Q|. Replace each large occurrence
by k demand copies, each adjacent to all its items. For any subset X of
demand copies, let Q be the occurrences represented in X. Its neighborhood
is union_(e in Q) S_e and has size at least k|Q|>=|X|. Thus Hall's marriage
theorem applies to **every** subset of demand copies, not merely subsets
containing all k copies of an occurrence.

Choose k distinct matched items B_e subseteq S_e for each large occurrence.
The sets B_e are pairwise disjoint, even if some S_e coincide. Together
with a singleton for every unmatched item, these form a partition B of
[n]. Each block has size k or 1. Give a k-block arbitrary distinct base
colors 0,...,k-1 and a singleton base color 0. The k allowed states of a
block B are cyclic shifts: in state r, item j in B receives

    chi(j) = base(j)+r (mod k).                       (2)

Whatever states the blocks choose, each large occurrence contains its
entire dedicated k-block, hence every color. It contributes exactly one
to f_i(T_c) for every c. Large features can therefore be kept as a
color-independent constant throughout the rest of the proof.

## 3. A bounded number of noninteracting block classes

Make a simple graph whose vertices are the blocks and join two distinct
blocks when a small occurrence meets both. A block B has at most k items
and meets at most |B|t<=q distinct tagged occurrences. Each small occurrence
has at most q-1 items and therefore meets at most q-1 blocks. For each
small occurrence touching B it can contribute at most q-2 neighbors of B.
Overcounting repeated neighbors only increases this upper bound, so

    degree(B) <= q(q-2).

Greedy graph coloring yields H<=q(q-2)+1=(q-1)^2 classes C_1,...,C_H.
A small occurrence meets at most one block in any one class. It may meet
several items within that block. No step assumes itemwise independence
inside a block. At q=2 every small feature is a singleton; the graph has
no edges and H=1 is valid.

## 4. Coverage expectations are affine on one block class

For each block B, let p_(B,r), r in Z_k, be probabilities on its k states.
Choose states independently **between blocks**, while retaining the full
within-block correlations in (2). Define

    Phi_(i,c)(p) = E[f_i({j: chi(j)=c})]

under this temporary product law. Initially every p_(B,r)=1/k. Adding the
same shift to every block rotates all colors and preserves this law.
Consequently Phi_(i,c)(p_initial)=mu_i is independent of c. This does not
require features to meet their blocks in at most one item.

Fix a class C and hold all laws outside C fixed. For a small occurrence
e meeting B in C, set

    z_(e,c)(r)=1[there is j in S_e intersect B
                    with base(j)+r=c mod k],
    v_(e,c)=Pr[no block outside C gives color c to an item of S_e].

Because e meets at most one class-C block, its probability of being hit
by color c is exactly

    1-v_(e,c) + v_(e,c) sum_r p_(B,r) z_(e,c)(r).      (3)

If it meets no block in C, that probability is constant. Formula (3)
follows by conditioning on whether any outside block hits the color and
then using independence between B and the outside blocks. Summing (3)
over the tagged small occurrences of function i, and adding its large
constant, gives a joint affine map

    (Phi_(i,c))_(i,c) = b + A p_C,
    A_((i,c),(B,r)) = sum_(e tagged to i, small, S_e meets B)
                             v_(e,c) z_(e,c)(r).      (4)

All entries of A are nonnegative. For a fixed B,r, the items of B have
distinct colors in that state; hence, for each small e touching B,

    sum_c z_(e,c)(r) = |S_e intersect B|.

As 0<=v_(e,c)<=1, summing the column in (4) gives

    sum_(i,c) A_((i,c),(B,r))
       <= sum_(e small touching B) |S_e intersect B|
        = sum_(j in B) degree_small(j)
       <= |B|t <= q.                                (5)

This counts every tagged occurrence and counts each of its items in B.
It remains valid when the same feature contains several block items,
when incidence subsets repeat, and when functions share incidence sets.
In particular it does not silently replace feature sparsity by the weaker
number of influenced functions.

## 5. Round classes and telescope

Process C_1,...,C_H in order. In class C_h, all outside probabilities are
held fixed and (4) is an affine map with column absolute sums <=q. Apply
(1) with D=q to the k-state simplex of each block in C_h and make the
resulting states deterministic. For every function i and color c,

    |Phi_(i,c)(p_after)-Phi_(i,c)(p_before)| <= 2q.      (6)

Outside blocks remain mutually independent in the product-law definition;
replacing some of their marginals by point masses preserves that meaning.
At each new class its coefficients are recalculated for its actual fixed
outside laws. Thus (6) compares consecutive values of the **same** Phi
functional evaluated at consecutive full probability vectors; it does not
assume the matrices of different classes are equal.

After all H classes, every block law is a point mass, so Phi is the actual
coverage value of the resulting coloring. Telescoping (6) yields

    |f_i(T_c)-mu_i| <= 2qH.

For any c,c', subtract the same mu_i and use the triangle inequality:

    |f_i(T_c)-f_i(T_c')| <= 4qH <= 4kt(kt-1)^2.

This holds simultaneously for all i,c,c'. It proves the stated theorem
for every allowed parameter tuple, and hence resolves the exact qualitative
existence question in source.md. Finite computations are not used in this
proof.

## 6. Constructive bit complexity for the explicit input model

Measure input size using the item slots, function/feature tags and listed
incidences, together with binary encodings of k and the supplied t. If
k>=n, give every item a distinct color. Each nonempty color class is a
singleton and has f_i value at most t; empty classes have value zero.
Thus discrepancy is <=t, within the theorem, and color labels have
polynomial bit size. This avoids expanding a binary-encoded enormous k.

Otherwise k<n. For the implementation one may replace t by
d=max(1, maximum actual tagged item degree). Then d<=t and the displayed
polynomial is increasing for kd>=2; the resulting bound still implies the
claimed one. Now k and d are polynomially bounded by the explicit input.
Hall representatives are obtained by finite bipartite matching with k
copies per large occurrence; there are at most n such copies by the same
degree count. The block graph can be built and greedily colored in
polynomial time; its actual number of classes is at most n.

At the start of any class, earlier classes are point masses and all later
classes are still uniform. For a small occurrence, any outside block B
that is uniform misses a fixed color with probability
(k-|S_e intersect B|)/k, by the injectivity of its base colors. A deterministic
outside block has miss probability 0 or 1. Thus v_(e,c) is a product of at
most n rational factors with denominator k. Each coefficient in (4) is a
sum over at most M feature occurrences with common denominator dividing
k^n, so has O(n log k + log(M+1)) bits. Targets for the uniform law in the
current class have denominators dividing k^(n+1). The matrices have at
most mk rows and nk columns, hence polynomial encoding length.

The rational equal-choice version of the known rounding theorem (1) has a
polynomial-time algorithm. Alternatively, to avoid an unsupported bit-size
claim for repeated arbitrary null directions, implement its proof using
rational LP vertices: after dropping light rows, the still-fractional
submatrix has fewer independent equations than variables, so every vertex
of the bounded feasible polytope fixes a further coordinate to 0 or 1.
Obtain a vertex by sequentially optimizing the coordinates; this takes at
most polynomially many rational LP optimizations. All retained row targets
remain the original A p_C at the start of this class, adjusted only by
original coefficients of coordinates fixed at 0 or 1. These LPs therefore
use submatrices of one fixed rational matrix and right sides of polynomial
bit length. Standard determinant bounds control the vertices' encoding
length. There are at most nk coordinate fixings and mk row drops per
class. This proves weak polynomial time in the stated explicit input model.
No running-time claim about the diagnostic Python nullspace implementation
is used as evidence for this complexity conclusion.

## Dependencies, proposed contribution, and gaps for review

Dependencies are Hall's marriage theorem, finite graph greedy coloring,
the known multiple-choice Beck--Fiala lemma (proved above), elementary
probability on finite product spaces, and, only for the time claim,
polynomial-time rational matching/linear programming. The source paper
already uses independent interaction classes and dropped-row rounding:
Avila--Rohwedder--Wennmann, ESA 2026, Section 5 and Lemma 23, pp.139:12--13.
These tools are credited and are not claimed as new standalone results.

The proposed new delta is the reduction by disjoint full rainbow witness
blocks and their cyclic categorical laws, together with the incidence-based
column bound (5). It makes all large occurrences identically balanced
throughout rounding and allows a size-independent number of class stages.
Ordinary itemwise rounding of the witnesses would not preserve rainbow
coverage, and the source's itemwise affine lemma does not apply directly
to several items moving together inside a witness block. Equations
(3)--(5) supply precisely that additional structural step.

Gap list for the submitted mathematical argument: `[]`. Current novelty
and whether the reduction is sufficiently substantive for publication
remain review questions against the exact original scope and closest
primary results. The arbitrary-Lipschitz/influence-sparse question remains
outside this result, as do weights and a sharp t,k dependence.
