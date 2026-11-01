# Precise problem and triage scope

The verbatim question remains in `source.md`; its immutable SHA-256 is
`9488f12633da72d763b0ad127ff791f002ff7451ea26826a68d35a832f0bad15`.
This is a generated research question, not a verified recognized open problem.
The supplied `candidate-argument.md` is an unaccepted seed.

## Objects, quantifiers, and conventions

For each integer n >= 1 let Y = {1,...,n} and
Delta_n^o = {x in R^n : x_i > 0 for all i, sum_i x_i = 1}.
All logarithms are natural. For all p,q in Delta_n^o put

    d_DP(p,q) = max_i |log(q_i/p_i)|.

An admissible path r is a coordinatewise absolutely continuous map
[0,1] -> Delta_n^o with r(0)=p and r(1)=q. Define

    C(r) = ess sup_t max_i |r_i'(t)/r_i(t)|,
    Lambda(p,q) = inf {C(r): r admissible}.

The cost may be infinite for an individual admissible path. Since a continuous
strictly positive path on the compact parameter interval has each coordinate
bounded away from zero, log r_i is absolutely continuous. Thus C(r) <= L is
equivalent to both-direction metric privacy

    exp(-L|s-t|) <= r_i(s)/r_i(t) <= exp(L|s-t|)

for every i and s,t in [0,1]. An affine path is always admissible with finite
cost, so the infimum is finite. At p=q it equals zero. For n=1 every pair is
identical and no positive-distance ratio is defined.

Determine Lambda for every n and every positive pair, whether an optimal path
attains it, and how to construct or compute one. For n >= 2 and eta > 0 define

    W_n(eta) = sup {Lambda(p,q)/eta : p,q in Delta_n^o,
                                      d_DP(p,q) = eta}.

Determine W_n(eta) and its supremum over eta, including attainment and limiting
cases. No zero coordinates, infinite alphabets, approximate DP, arbitrary
multi-anchor extensions, or multidimensional input geometry are implicitly
included. A path on an interval is a continuous-domain extension of its two
endpoint distributions; endpoint privacy tests alone do not establish a
particular extension's cost.

## Required comparisons

For the same fixed time parameter compare the affine path
r_i(t)=(1-t)p_i+t q_i and normalized geometric path
r_i(t)=p_i^(1-t)q_i^t / sum_j p_j^(1-t)q_j^t.
Distinguish fixed-parameter cost from reparameterized path length.
The transform-linear family uses a specified monotone scalar transform f and
parameter alpha: f^-1((1-alpha(t))f(p_i)+alpha(t)f(q_i)), followed by
normalization when needed. Continuity/monotonicity alone does not imply finite
Lipschitz cost; any assertion needs its regularity and parameterization stated.
Compare only the actual hypotheses of arXiv:2609.14125 and arXiv:2601.09946,
which explicitly account for normalization, rather than alleging that they
certify unmodified endpoint budgets in general.

## Nearest inspected statements and proposed delta

BCSZ, *Private Algorithms Can Always Be Extended*, arXiv:1810.12518v2,
Section 2, Proposition 2.1, gives factor-two privacy extension on arbitrary metric input spaces.
Qiu, arXiv:2601.09946v1, Section 5.2, Definitions 5--6 and Proposition 3,
gives normalized log-convex interpolation with factor-two budget accounting.
Liu--Qiu, arXiv:2609.14125v1, Theorem 5 and Appendix E, uses calibrated
pre-normalization budgets, including epsilon/2. These are related upper bounds,
not yet verified equivalents of the exact finite-distance optimum asked here.

Thompson distance on the full positive cone equals d_DP; restricting its
endpoint formula to the simplex does not by itself make the simplex a geodesic
subspace. Hilbert simplex geometry instead uses the range of log coordinate
ratios (up to a convention-dependent factor), not their maximum absolute value.
Further overlap with Laplace trade-off functions, continuous group privacy,
Blackwell comparison, and canonical noise must be screened before novelty claims.
This triage inspected Dong--Roth--Su, arXiv:1905.02383v3, Theorem 2.10,
Proposition 2.15, and Lemma A.6: together they give the seed's abstract
reachable-set criterion by known testing theory. See `evidence/triage-analysis.md`.
The proposed new value must therefore come from a useful explicit finite
construction/algorithm and sharp comparisons, rather than the scalar flow or
abstract reachability criterion alone. Neither significance nor novelty of
that remaining delta has been established.

Proposed delta to investigate: the seed's exact reachable-set characterization
q(A) <= h_T(p(A)) for every subset A, where h_T solves a'=min(a,1-a), its
reduction to likelihood-ratio prefixes, and a sharp finite-eta overhead. A
verification route is scalar comparison for necessity, a complete greedy
base-polytope argument for sufficiency, and a supporting-line argument for
prefix reduction. The quantified theorem and novelty remain unaccepted.

Triage may admit a research test; it cannot certify a manuscript. The exact
five-author list, official ACM template, <=12 total pages, and genuine fresh
referee/release gates in `requirements.md` govern any later accepted artifact.

## Research pass 2: separate mandatory-excursion subsidiary scope

The explicit reopening instructions in requirements.md replace the old
computational-decomposition reopening target with a shape-constrained target.
The old unrestricted Laplace/Blackwell reachability result remains known and
parked; no O(n^2) improvement for constructing general optimal paths is claimed.
The original source and its full required transform-family comparison remain
unresolved. The exact pre-pass-2 interpretation is preserved in
`evidence/research-pass1-problem.md`.

For a path use C(r) exactly as above. Define Lambda_mon by additionally
requiring each coordinate monotone in its endpoint direction, equal endpoints
forcing a constant. Define Lambda_box by requiring every coordinate to remain
in its closed endpoint range. Both are infima over positive normalized AC
paths, using the same fixed unit interval and essential-supremum log speed.

For swapped triplets p=(c,a,b), q=(c,b,a), 0<a<b, a+b<1, c=1-a-b,
define the peak frontier P(L)=inf_{C(r)<=L} max_t r_0(t), with infeasible
budgets treated separately. The new claim is P(L)=max{c,1-2a exp(L/2)} for
all feasible L. The minimum feasible budget is log(b/a) when b<=1/2 and
log(1/[4a(1-b)]) when b>1/2. The proof in
`evidence/research-excursion-proof.md` supplies a matching path, including the
previously unseeded b>1/2 regime, and uniqueness at this minimum budget.

A second sharp claim compares Lambda_mon and Lambda_box with Lambda over all
positive endpoint pairs at fixed d_DP=eta>0. Both worst ratios equal
2log((exp(eta)+1)/2)/eta for n>=3, attained in every such dimension; for n=2
they equal 1. This is the price of a path-shape restriction, distinct from the
known unrestricted worst ratio relative to the endpoint metric.

A third supporting claim gives only necessary excursion certificates for
arbitrary endpoints and budget: C_j=1-min_{1<=z<=Z} sum_{i!=j}
min(p_i z,Zq_i/z), Z=exp(L). Rational certificates admit a sorted exact
O(n log n) arithmetic evaluation per coordinate and O(n^2+n log n) for all
coordinates. They are sharp for the swapped family; no general sufficiency
or feasibility algorithm is asserted.

Primary comparisons and value limits are in
`literature/research-excursion-screen.md`. Standard binary flow and endpoint
Lipschitz envelopes are credited ingredients. Normalization may cause scalar
transform-linear rules to leave coordinate endpoint ranges, so no theorem
about all normalized transform-linear families is inferred. A result-note
candidate requires a fresh mathematical/value referee before any manuscript.
