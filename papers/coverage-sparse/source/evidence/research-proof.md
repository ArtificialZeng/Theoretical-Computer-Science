# Proposed complete resolution: proof dossier, awaiting fresh referee

Job: `coverage-sparse-research-6239617d8b3f`.
Date: 2026-10-31 Asia/Shanghai. This is mathematical research evidence, not a
manuscript, acceptance certificate, or claim of conference suitability.

## Statement and dependencies

Use exactly the objects and maxima in `problem.md`. Set
`alpha_k = 1-(1-1/k)^k` for every integer `k >= 1`. For both graph classes
`C_k = {G: chi(G)<=k}` and `B_k = {G: Delta(G)<=k-1}`, the supremum of
`f^+(x)/f_G^=(x)` equals `1/alpha_k`. For every fixed finite real `delta>=0`,
the supremum of `f^+(x)/f_{G,delta}^le(x)` over either class also equals
`1/alpha_k`. The supremum allows all finite ground sets, all marginals, and
all finite nonnegative weighted coverage functions with `f^+(x)>0`.

More precisely, a witness with `n=mk` vertices and exactly `n(k-1)/2`
tested pairs has `f^+(x)=1` and, for `k>=2, m>=1`,

    alpha_k <= f_G^=(x) <= min{1,alpha_k+(k-1)/(2km)},
    alpha_k <= f_{G,delta}^le(x)
            <= min{1,alpha_k+(1+delta)(k-1)/(2km)}.

All assertions below are proved analytically. Finite calculations are secondary
checks only. Dependencies are elementary finite probability, finite products,
AM-GM, concavity of a polynomial, geometric sums, and greedy graph coloring.
No external theorem about a correlation gap is needed for the proof.

## 1. A feasible law from a proper coloring

Fix any proper coloring `V=C_1 disjoint-union ... disjoint-union C_k`, allowing
empty classes. Given any law `D` on subsets with marginals `x`, draw independent
copies `S_1,...,S_k` from `D`, and return

    R = union_{c=1}^k (S_c intersect C_c).

Each vertex is included with its original marginal. Endpoints of an edge are
in distinct color classes and depend on independent samples, so their joint
inclusion probability is exactly `x_i x_j`. Thus the law of `R` is feasible
for both the equality model and every stated upper-error model. No
independence within a color class or restriction on nonedges is used.

For a feature `H`, put `a_c=P_D(S intersects H intersect C_c)` and
`b=P_D(S intersects H)`. The union bound gives `b<=min{1,s}`, where
`s=sum_c a_c` lies in `[0,k]`. Independence of the samples gives

    P(R intersects H) = 1-product_c(1-a_c)
                     >= h(s) := 1-(1-s/k)^k.

The inequality is AM-GM for the `k` nonnegative factors `1-a_c`.
For `k>=2`, `h` is nondecreasing and concave on `[0,k]`:
`h'(s)=(1-s/k)^(k-1)>=0` and
`h''(s)=-(k-1)/k (1-s/k)^(k-2)<=0`.
For `0<=s<=1`, concavity between `0` and `1` yields
`h(s)>=s h(1)=alpha_k s`; for `1<=s<=k`, monotonicity yields
`h(s)>=h(1)=alpha_k`. Hence each feature is hit with probability at least
`alpha_k b`. Multiply by its nonnegative weight and sum the finite family.
Taking `D` to maximize the unrestricted expectation proves

    f_G^=(x) >= alpha_k f^+(x),
    f_{G,delta}^le(x) >= alpha_k f^+(x).

A graph of maximum degree at most `k-1` has a proper coloring with at most
`k` colors: process any ordering of its vertices and give each a color not
used by an already colored neighbor. At most `k-1` colors are forbidden.
Therefore the same bounds hold for both graph classes.

For `k=1` every graph in either class has no edges. Its feasible laws are all
marginal-preserving laws in both models, and its ratio is exactly one.
This handles the endpoint without powers or logarithms at zero.

## 2. The Cartesian coverage witness and its numerator

Let `B_1,...,B_m` be disjoint sets of size `k`, with `G` the disjoint union of
the cliques on these sets. Write vertices as `(r,j)` for `1<=r<=m,1<=j<=k`.
For each tuple `u=(u_1,...,u_m)` in `{1,...,k}^m`, make the feature
`H_u={(r,u_r):1<=r<=m}` of weight `k^(-m)`. These are finitely many features
of a legitimate nonnegative weighted coverage function. Their total weight
is one. For `a_r=|S intersect B_r|`, direct counting of missed tuples gives

    f(S) = 1-product_{r=1}^m(1-a_r/k).

Set every marginal to `x_i=1/m`. Select a block uniformly and include all of
it, excluding everything else. Each vertex then has the specified marginal;
every feature is hit with certainty. Since `f(S)<=1` for every subset,
`f^+(x)=1`. This law is used only for the numerator.

The graph has chromatic number `k`, maximum degree `k-1`, `n=mk` vertices,
and `m*binom(k,2)=n(k-1)/2` edges. Thus it belongs to both classes and has
linearly many tested pairs for each fixed `k`. The feature family may be
exponential; the original question imposes no feature-size restriction.
This construction is already present in Ramachandra (2026), Section 4;
its reuse is explicitly acknowledged, not claimed as a new family.

## 3. Local integer inequality, with a direct proof

Fix `k>=2`, let `p=1/k` and `q=1-p`. For each integer `0<=a<=k`, define
`d_a=q^a-(1-ap)`. We claim

    0 <= d_a <= binom(a,2) p^2.                         (1)

We have `d_0=0` and

    d_{a+1}-d_a = p(1-q^a).

The geometric-sum identity gives
`0<=1-q^a=p sum_{j=0}^{a-1}q^j<=ap` (the empty sum is zero).
Summing the increments for `a` steps proves (1), including `a=0,1,k`.
This proof uses no asymptotic approximation or alternation estimate.

## 4. Product comparison and a rational pointwise dual

For occupancies of any subset, put `A_r=1-a_r/k` and `Q_r=q^(a_r)`.
By (1), `0<=A_r<=Q_r<=1`. The exact telescoping identity

    product_r Q_r - product_r A_r
      = sum_r (Q_r-A_r) product_{s<r}Q_s product_{s>r}A_s

has every product factor in `[0,1]`. With
`T=sum_r a_r` and `C=sum_r binom(a_r,2)`, it follows that

    f(S) <= 1-q^T+C/k^2.                               (2)

There is a supporting line with rational coefficients for integer `T`.
Set `g(t)=1-q^t` on the nonnegative integers and `beta_k=q^k/k`.
Its successive differences are `g(t+1)-g(t)=q^t/k`. If `t>=k`, sum
the differences from `k` to `t-1`, each at most `beta_k`. If `t<k`, sum
from `t` to `k-1`, each at least `beta_k`, and rearrange. In both cases,

    1-q^t <= alpha_k+beta_k(t-k)  for all integers t>=0. (3)

Consequently the following is an explicit, entirely rational, pointwise
dual feasible inequality for every subset `S` and every `m>=1`:

    f(S) <= alpha_k+beta_k(|S|-k)
                     + (1/k^2) sum_r binom(|S intersect B_r|,2). (4)

The originally proposed logarithmic tangent is also valid: on real `t>=0`,
`1-q^t` is concave with derivative `-q^k log(q)` at `k`, so (2) gives that
tangent certificate. Formula (4) avoids transcendental arithmetic in checks.
Neither argument imposes any cross-block pair constraint.

## 5. Average using only tested within-block pairs

Under every law with the stated marginals,
`E T=mk/m=k`. For the upper-error feasible set, linearity of expectation gives

    E C = sum_r sum_{{i,j} subset B_r} P(i,j in S)
        <= m binom(k,2) (1+delta)/m^2
         = (1+delta) k(k-1)/(2m).

The coefficient `1/k^2` in (4) is nonnegative, so averaging (4) proves

    E f(S) <= alpha_k+(1+delta)(k-1)/(2km).

Taking the maximum and using `f<=1` proves the finite upper-error bound.
For the equality model the displayed moment inequality holds as equality
with `delta=0`, proving its finite bound as well. Section 1 supplies each
lower bound `alpha_k` because `f^+(x)=1`.

This covers arbitrary real `delta>=0`, not just rational errors. For `m=1`,
all marginals are one, hence `S=V` almost surely and both optima are one;
the upper bounds remain valid. They are not asserted sharp for every `k,m`.

## 6. Take the class suprema in the prescribed order

Fix `k>=2` and a finite `delta>=0`. Every instance in either graph class has
ratio at most `1/alpha_k` by Section 1. On the witness, for every positive
integer `m`, the ratio in the upper-error model is at least

    1 / [alpha_k+(1+delta)(k-1)/(2km)].

The lower bound tends to `1/alpha_k` as `m` tends to infinity. The same
argument with `delta=0` handles equality. Since each finite witness lies in
both classes, their suprema are at least the limit. This proves all four
asserted values. It asserts a class supremum, not equality for every graph,
and does not require a finite witness attaining that supremum.

Thus the extremal gap persists with `n(k-1)/2` tested pairs and every fixed
finite one-sided multiplicative error. The constant depends on `k`; no
optimal edge-budget tradeoff or claim for unrestricted growing errors follows.

## Gap and scope ledger

- Known mathematical gaps in the stated original resolution: none found in
  this research pass. A fresh mathematical referee has not yet checked it.
- Proposed contribution: exact fixed-`k` graph-class hierarchy together with
  sparse within-block certification and finite one-sided-error stability.
- Known overlap: Cartesian coverage is prior work; the two-block `3/4`
  recombination argument and the `alpha_k` constant are prior ingredients.
  These are not claimed new separately. Novelty of the combined graph theorem
  is limited to the primary-source screen, not a priority assertion.
- No arbitrary monotone-submodular extension, fixed-graph characterization,
  optimal pair-budget necessity result, or conference acceptance is claimed.
- Computational assistance: an AI research pass derived and checked the
  argument. Standard-library rational checks are supplementary evidence;
  no Lean formalization, external peer review, or new agent was used.
