# Persistent-noise curvature bound: analytic proof for review

Proposer: `curvature-noise-research-5a09759394ef`. Research evidence, not a
fresh mathematical acceptance. The full question in `source.md` remains
unresolved. All statements use the true objective and the oracle model frozen
in `problem.md`.

## 1. Finite theorem

Let integers n,k,r satisfy n>k+r and 1<=r<k. Let 0<=K<1 and
0<e0<1, and define

    rho=(1-e0)/(1+e0), a=rho*(1-K), b=rho*K,
    c=(1-rho)*(1-K)/(1-a).

If cn>exp(1)k, then for every possibly randomized algorithm making at most Q
adaptive value queries on every promised input, and always returning a set of
size at most k, there is a single valid pair (f_H,g_H), fixed independently
of the algorithm's private randomness, with exact curvature K and OPT=k, such
that

    E f_H(A)/k <= a + br/k + (1-a)k/n
                   + min(1,Q [exp(1)k/(cn)]^(cr)).                (1)

Queries of every cardinality are allowed. No running-time or numerical
precision assumption is used. A worst-case query bound holding almost surely
over the private seed suffices, with null seeds discarded.

### Family and global promises

Choose H uniformly from the k-subsets of V=[n]. For h=|S intersect H|,
t=|S outside H| and s=h+t, put

    f_H(S)=h+a t+b min(t,r),
    F0(S)=a s+b min(s,r),
    g0(S)=(1+e0) F0(S),
    g_H(S)=max(g0(S),(1-e0)f_H(S)).                           (2)

These formulas define each oracle on ALL subsets before any run. A good
element has marginal 1. A bad element has marginal a+b=rho while fewer than
r bad elements are present, and a thereafter. The marginals are nonnegative
and decrease under inclusion. Hence f_H is normalized, monotone and
submodular, with positive singletons 1 and rho. Because n-k>r, a bad
element's full-set marginal is a. Good elements have full-set/singleton ratio
1 and bad ones a/rho=1-K. Thus curvature is exactly K, including K=0.
Moreover f_H(S)<=h+(a+b)t<=s and f_H(H)=k, proving OPT=k.

We have 0<c<=1: positivity follows from rho<1 and K<1; subtracting the
numerator defining c from its denominator gives K>=0. Also

    c >= (1-K)e0,                                            (3)

because 1-rho=2e0/(1+e0)>=e0 and 1-a<=1.

The cap decreases by at most h on replacing s by s-h. Consequently

    f_H(S)-F0(S)
      = (1-a)h + b[min(s-h,r)-min(s,r)]
      is between (1-a-b)h=(1-rho)h and (1-a)h.               (4)

In particular F0<=f_H, so g0<=(1+e0)f_H. Each argument of the maximum
in (2) is at most (1+e0)f_H, and one is exactly (1-e0)f_H. This proves
both noise inequalities globally, even on unqueried sets. Persistence is
immediate from (2).

The baseline is itself a promised input: F0 has singleton rho and full-set
marginal a (as n-1>=r), hence exact curvature K; g0 is its allowed upper
endpoint oracle. This matters when the query and output promises apply only
to valid inputs.

### Leakage for every query size

If s<=r, then f_H(S)=rho s+(1-rho)h<=s and
g0(S)=(1-e0)s, so g_H(S)=g0(S) for every H.

If s>r, (4) implies that g_H(S)=g0(S) whenever

    h <= theta(s)
       = (1-rho)[(1-K)s+Kr]/(1-a) >= cs.                    (5)

Indeed this inequality says (1-e0)[F0+(1-a)h]<=(1+e0)F0.
Thus leakage implies X=|S intersect H|>theta(s)>=cs.

For fixed S of size s>r, let j=ceil(cs). Then 1<=j<=s. If j>k the
leakage probability is zero. Otherwise, a union bound over the j-subsets
of S gives

    P[X>=j] <= binom(s,j) (k)_j/(n)_j
              <= binom(s,j)(k/n)^j
              <= [exp(1) s k/(j n)]^j
              <= [exp(1) k/(cn)]^j
              <= [exp(1) k/(cn)]^(cr).                      (6)

Here (k)_j/(n)_j is the probability that any specified j elements lie in
H; each factor (k-i)/(n-i)<=k/n. The standard binomial estimate follows,
for example, from j! >= (j/exp(1))^j. The last step uses cn>exp(1)k and
j>=cs>cr. No independence among element-membership indicators is assumed.
The enlargement to X>=ceil(cs) is valid also when cs is integral.

### Adaptive randomized coupling

Fix a private seed omega and run the algorithm against g0. Denote its
queries S_1(omega),...,S_m(omega), m<=Q, and output A0(omega). These sets
are independent of H. Let B be the event that some such baseline query
has g_H(S_i)!=g0(S_i). Applying (6) to these fixed queries and taking a
union bound gives

    P_H[B | omega] <= min(1,Q [exp(1)k/(cn)]^(cr)).           (7)

If B does not occur, induction on query number shows that the actual run
against g_H has the same queries, answers, stopping time and output A0.
This argument does not require a query chosen after divergence to be
independent of H. Since every feasible set has f_H value at most k,

    f_H(A^{g_H}_omega) <= f_H(A0(omega)) + k 1_B.

For every seed, E_H |A0 intersect H|=|A0|k/n<=k^2/n. The alternate
expression f_H(A0)=a|A0|+(1-a)|A0 intersect H|+
b min(|A0 outside H|,r) therefore gives

    E_H f_H(A0)/k <= a+(1-a)k/n+br/k.

Averaging over omega and using (7) proves (1) on average over the finite
set of possible H. At least one fixed H has its private-seed expectation
at most this average. The same H is used for all seeds. This completes
the finite proof.

## 2. Exact finite alternative for verification

The same coupling gives a sharper rationally checkable bound without the
condition cn>exp(1)k. Define

    p = max_{0<=s<=n} P_H[g_H(S_s)!=g0(S_s)],

where S_s is any fixed s-set. It is evaluated exactly by summing
binom(s,h)binom(n-s,k-h)/binom(n,k) over h for which the two formulas
in (2) differ. Also define X~Hypergeometric(n,k,k) and

    beta = a+(1-a)k/n+(b/k) E[min(k-X,r)].

Then some fixed H satisfies

    E f_H(A)/k <= beta+min(1,Qp).                            (8)

To justify beta for a baseline output of size <k, extend that output
arbitrarily to a k-set and use monotonicity for each H. Symmetry gives
the displayed expectation for every fixed k-set. Formula (6) shows that
p is at most the exponential bound when its condition holds, and beta
is at most the first three terms of (1). Thus (8) also implies (1).
This is an ancillary sharpening used for exact checks, not an asserted
finite minimax characterization.

## 3. Sparse-cardinality asymptotic corollary

Fix 0<alpha<1/2 and 0<=K<1. Let k=floor(n^alpha), 0<e_n<1 and
u_n=e_n k -> infinity. Set rho_n=(1-e_n)/(1+e_n) and choose

    r=ceil(sqrt(k/e_n)).

Then r/k<=1/sqrt(u_n)+1/k ->0, so eventually 1<=r<k and n>k+r.
Writing delta=1-K>0, (3) yields

    cr >= delta sqrt(u_n) -> infinity,
    cn/k >= delta u_n n/k^2 >= delta u_n n^(1-2alpha).

Put gamma=(1-2alpha)/2>0. Eventually exp(1)k/(cn)<=n^(-gamma).
For every fixed algorithm-family bound Q(n)<=C n^d, the failure term
in (1) is at most C n^(d-gamma cr)=n^(-omega(1)). The other remainders
satisfy

    br/k <= K[1/sqrt(u_n)+1/k] ->0,
    (1-a)k/n <= k/n ->0.

Consequently each such algorithm family has a sequence of fixed valid
instances with exact curvature K and

    E f_n(A_n)/OPT_n <= rho_n(1-K)+o(1).                     (9)

The quantifier is per algorithm family, not a pointwise supremum over
unbounded polynomial degrees at each n.

## 4. Matching standard algorithm (credited baseline)

Query all singletons and take the k largest g({i}), obtaining S. For an
optimal k-set O (extended by monotonicity when necessary), the ordering gives

    (1+e0) sum_{i in S} f({i}) >= sum_{i in S}g({i})
       >= sum_{i in O}g({i}) >= (1-e0)sum_{i in O}f({i})
       >= (1-e0) f(O).

Start a telescoping enumeration of S with its largest true singleton.
Every subsequent marginal is at least (1-K) times its singleton by
submodularity and the definition of curvature. Therefore

    f(S) >= (1-K)sum_{i in S}f({i})+K max_{i in S}f({i})
         >= (1-K+K/k)sum_{i in S}f({i})
         >= rho(1-K+K/k) OPT.                              (10)

This is a routine true-objective analysis/refinement of the Horel--Singer
singleton algorithm, not the proposed novelty. Together (9) and (10)
give an additive asymptotic characterization in the stated regime. If
rho_n stays bounded away from zero and K<1 is fixed, it is also a relative
1+o(1) characterization of that positive factor. If rho_n->0, only the
additive assertion is made. In particular, if e_n->0 while e_n k->infinity,
the sharp limiting factor is 1-K. For K>0 this differs from the known
noiseless factor 1-K/exp(1), up to the accuracy slack in that prior theorem.

## 5. Scope, dependencies, and unresolved questions

Dependencies are the value-oracle model, elementary submodularity via
diminishing marginals, a hypergeometric union bound, finite averaging, and the
credited singleton method. No unproved analytic step is known in (1)--(10)
at this research stage; fresh review is still required.

Not asserted: all-parameter optimality; exact finite minimax factors;
the K=1 endpoint; e0=0; a transition theorem for bounded e0*k;
high-probability hardness; relative sharpness when rho_n->0; or novelty of
the hidden capped-rank family, modular curvature tuning, or transcript method.
The closest-source comparison and limitations are in
`evidence/research-literature.md`. Exact computations are ancillary finite
falsification tests, not proofs of the quantified theorem.
