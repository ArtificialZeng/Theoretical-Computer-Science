# Fresh mathematical referee report

Job: `curvature-noise-referee-01938a157e47` (referee).
Reviewed on 2026-10-31, Asia/Shanghai.
Frozen snapshot: `52edefc6f6361e426065ff407f44843ddc5a208b768db3f0cb7b916dd62ef407`.

## Verdict and exact scope

**ACCEPT the frozen `result-note` claim in `claim.json`.** The original full
joint-parameter question remains **unresolved**. The finite expected query
lower bound, its sparse-cardinality corollary for fixed curvature below one,
and the credited singleton guarantee are correct at the submitted scope.
This accepts the calibrated lower bound as an incremental, useful mathematical
contribution. It does not certify priority, a new proof technique, conference
acceptance, the curvature-one endpoint, zero noise, the transition where
epsilon times k stays bounded, high-probability hardness, or finite minimax
optimality. No part of the frozen contribution was removed to reach this verdict.

This is a fresh AI mathematical review pass, not human peer review or
statistically independent experimental evidence. I read the permitted frozen
inputs and listed evidence, inspected relevant primary sources, and wrote a
separate exact verifier. I did not read owner checkpoint/state/verdict files,
previous job transcripts, or other unlisted project evidence. I did not modify
the claim, snapshot, frozen evidence, original source, or runner role metadata.

## Reconstruction from definitions

Write K for the promised curvature, e0 for the noise, delta=1-K, and
rho=(1-e0)/(1+e0). Then a=rho*delta is strictly between zero and one,
b=rho*K is nonnegative, a+b=rho<1, and

    c=(1-rho)*delta/(1-a)

is positive and at most one: the denominator minus the numerator is K.
There is no zero denominator at K=0 or for any permitted positive noise.
Also c>=delta*e0, since 1-rho>=e0 and 1-a<=1.

For a hidden k-set H the proposed objective is

    f_H(S)=h+a*t+b*min(t,r),
    h=|S intersect H|, t=|S outside H|.

A good element always has marginal one. A bad element has marginal rho
until the bad-element cap is exhausted, and then marginal a. These are
nonnegative diminishing marginals, proving normalization, monotonicity and
submodularity. All singleton values are positive. The assumption n-k>r
ensures that removing one bad element from the full set leaves at least r
bad elements. Its last marginal is therefore a and its singleton is rho;
the corresponding ratio is 1-K. Good elements have ratio one. Consequently
the curvature is exactly K, including K=0. Since f_H(S)<=|S| and f_H(H)=k,
the feasible true optimum is exactly k.

Let F0(S)=a*|S|+b*min(|S|,r) and g0=(1+e0)F0. Replacing h bad elements
by good ones changes the capped term by an amount between -b*h and zero.
Thus

    (1-rho)*h <= f_H(S)-F0(S) <= (1-a)*h.

In particular F0<=f_H on every subset. The maximum formula

    g_H(S)=max(g0(S),(1-e0)*f_H(S))

therefore lies in the required multiplicative interval on every subset,
including unqueried and infeasibly large subsets and the empty set. It is
a single fixed oracle table, not an adversary answering during the run.
The baseline F0 also has singleton rho and full-set marginal a, so it has
the same exact curvature and positive singletons. Its oracle g0 is a valid
promised input. This validates using the algorithm's query and feasibility
promises on its baseline run even if those promises hold only on valid inputs.

## Leakage and adaptive randomization

For s=|S|<=r one has f_H(S)<=s and g0(S)=(1-e0)*s, so no query of this
size reveals H. For s>r, the upper difference bound above shows agreement
whenever

    h <= (1-rho)*[(1-K)*s+K*r]/(1-a) = theta(s).

The algebra uses g0/(1-e0)=F0/rho; theta(s)>=c*s. Consequently leakage
implies |S intersect H|>c*s, uniformly over every query size.

For fixed S put j=ceil(c*s). If j>k the leakage probability is zero.
Otherwise a union bound over j-subsets of S gives

    Pr[leakage] <= binom(s,j)*(k)_j/(n)_j
                <= binom(s,j)*(k/n)^j
                <= [exp(1)*k/(c*n)]^j
                <= [exp(1)*k/(c*n)]^(c*r).

Here each falling-factorial ratio factor is at most k/n, and the binomial
estimate follows from j!>=(j/exp(1))^j. Since c<=1, j<=s. Since
c*n>exp(1)*k, the final base is strictly below one and j>=c*s>c*r
permits the last inequality in the displayed direction. The event enlarged
to X>=ceil(c*s) still contains leakage when c*s is an integer. There is
no independence assumption for memberships in a uniformly chosen k-set.

For a fixed private seed, run the algorithm on g0. Its at most Q baseline
queries and its feasible output A0 do not depend on H. A union bound on
these baseline queries bounds any disagreement by

    eta=min(1,Q*[exp(1)*k/(c*n)]^(c*r)).

Induction through the first disagreement couples the real and baseline
runs. No query after disagreement is asserted to be independent of H.
Off this event the output is A0; on it the feasible true value is at most k.
For every seed,

    E_H[f_H(A0)]/k <= a+b*r/k+(1-a)*k/n,

because E_H|A0 intersect H|=|A0|*k/n and |A0|<=k. This also handles an
unqueried output. Averaging first over H and the private randomness proves
the candidate bound on their joint average. Since the collection of H is
finite, at least one single H has its private-seed expected ratio at most
that average. The oracle for this H is independent of the private seed.
Almost-sure query/output promises cause no issue: only a finite family of
hard inputs and the one baseline input are used, so their exceptional null
seed sets can be discarded together. The conclusion is an expected bound;
no high-probability conclusion is inferred from it.

The ancillary exact-tail alternative in proof Section 2 is correct too.
Every fixed k-set has the displayed hypergeometric expected value beta.
Extending smaller baseline outputs to k elements preserves the upper bound
by monotonicity, and the same coupling gives beta+min(1,Q*p). This is a
checkable refinement, not a claimed optimal finite minimax value.

## Asymptotics and matching algorithm

For fixed alpha in (0,1/2), fixed K<1, k=floor(n^alpha), and u=e0*k
tending to infinity, choose r=ceil(sqrt(k/e0)). Eventually r<k and
n>k+r. The two key bounds are

    r/k <= 1/sqrt(u)+1/k -> 0,
    c*r >= (1-K)*sqrt(u) -> infinity.

Furthermore c*n/k >= (1-K)*u*n/k^2 >= (1-K)*u*n^(1-2*alpha).
With gamma=(1-2*alpha)/2 the tail base is eventually at most n^(-gamma).
For each algorithm family with its fixed constants C,d, the disagreement
term is bounded by C*n^(d-gamma*c*r), which tends to zero faster than
any fixed inverse power. The cap term b*r/k and the output-intersection
term (1-a)*k/n also tend to zero. This proves the exact submitted
additive bound rho*(1-K)+o(1), with one fixed instance per sufficiently
large n for that algorithm family. No pointwise optimization over polynomial
degrees is taken. The choice of r need not be known to the algorithm.

Independently, ordering the noisy singletons gives
sum_{i in S} f({i}) >= rho*OPT for the selected k-set. Telescope f(S)
starting with its largest true singleton. Curvature bounds every later
marginal below by (1-K) times its singleton, giving

    f(S) >= (1-K)*sum_{i in S}f({i})+K*max_{i in S}f({i})
         >= rho*(1-K+K/k)*OPT.

The algorithm need not know the true largest singleton: this is only an
enumeration used in its analysis. The corollary matches this credited
baseline additively. A relative characterization follows when rho stays
bounded away from zero, since K<1 is fixed. It is not inferred when rho
tends to zero. Exact zero noise, K=1, and k=n are outside the corollary.

## Independent finite checks actually executed

The standard-library script `audit/referee_check.py` imports no researcher
code and writes no frozen evidence. Its saved output is
`audit/referee-checks.json`. It checks all frozen hashes before and after.

Four additional rational parameter choices test 151,552 full set-pair
submodularity inequalities, monotonicity, exact curvature, normalization,
positive singletons, and OPT. Across all hidden sets and all query subsets
they test 38,016 oracle entries, including large queries and no-leakage
thresholds. By permutation symmetry one full submodularity table suffices
for each parameter choice. The zero-curvature case has exactly zero leakage.

For n=6,k=3,r=2,e0=1/2,K=1/3, a separate explicit depth-two decision-tree
enumeration considers all first queries, all response-dependent second
queries, and optimal feasible outputs. Its exact best uniform-prior ratios
for Q=0,1,2 are 359/540, 7/10, 13/18. The exact beta is 359/540 and
p=1/20, so all three satisfy beta+Q*p. Randomized policies are mixtures
of these deterministic policies and cannot improve this prior optimum.

Four further exact hypergeometric count checks cover every query size for
n=128,257,89,512 and satisfy c*n>3*k, hence the finite theorem's condition.
They certify the stronger rational bound with exp(1) replaced by 8/3:
raising to the denominator of c*r avoids floating-point exponentiation.
The elementary bounds 8/3<exp(1)<3 suffice. For example the first case has
maximum leakage 5/170688. These finite checks do not prove arbitrary
parameters, arbitrary query depth, or asymptotics; those were checked
analytically above. The research script and saved results were inspected,
but its claimed held-out history was not used as independent validation.

## Prior results and contribution assessment

The closest source is Horel--Singer, [NIPS 2016, Section 2.1 equation (3)
and Proposition 8](https://proceedings.neurips.cc/paper_files/paper/2016/file/81c8727c62e800be708dbf37c4695dff-Paper.pdf),
checked in the frozen text, with [Appendix D of the later arXiv
deposit](https://arxiv.org/html/2411.10949v1#A4) also inspected. Their
objective is the approximate function F. They already supply the capped
hidden family, baseline transcript method, and top-k noisy-singleton
algorithm; their curvature guarantee is (1-K)*rho^2 for F. The one-factor
true-f normalization and K/k refinement are elementary and receive no
novelty credit here. Their displayed hardness theorem uses another
cardinality regime and does not state this calibrated fixed-curvature bound.

[Sviridenko--Vondrak--Ward, Theorems 6.1 and 7.1](https://arxiv.org/html/1311.4728v3)
give the exact-oracle 1-K/exp(1) guarantee and corresponding hardness. The
proof of Theorem 7.1 explicitly adds a uniform modular function to tune
curvature. That operation and exact-oracle comparison are credited prior
ingredients, and that theorem does not imply the submitted noisy factor.

[Hassidim--Singer, COLT 2017, Theorem 8 and Section 5](https://proceedings.mlr.press/v65/hassidim17a/hassidim17a.pdf)
already prove adversarial-noise hardness for randomized algorithms. The
displayed construction uses k=n^(1/2+delta), without calibration to a
prescribed curvature below one. Thus general adversarial hardness and
switching-oracle indistinguishability are not new contributions here.

The following adjacent primary comparisons were also checked:

* [Bhawalkar--Cai--Feng--Liaw--Lin, Section 2](https://arxiv.org/html/2510.21128v2):
  unbiased noise independent across distinct sets is required. Persistence
  alone does not make this candidate satisfy their model.
* [Huang--Wang--Yang--Zhou, Definition 2.4](https://arxiv.org/html/2210.11992v1):
  the oracle multipliers are i.i.d.; that positive result is inapplicable here.
* [Aggarwal, Theorem 5.14](https://arxiv.org/html/2608.12134v2): persistent
  additive error yields loss proportional to k times that error. Substituting
  a global multiplicative-to-additive bound does not improve the present
  factor in the admitted regime. Its proofs were not audited.
* [Roughgarden--Talgam-Cohen--Vondrak, Observation 3 and Theorem 4](https://arxiv.org/pdf/1608.02402):
  the positive theorem requires approximate diminishing returns for the
  queried valuation, which is not promised for g_H.
* [Chen--Kuhnle](https://arxiv.org/html/2605.07902v1): the inspected abstract
  and noise occurrences concern other curvature/objective settings; this
  was a limited relevance screen, not an audit of every theorem.
* [Balkanski--Rubinstein--Singer](https://papers.nips.cc/paper_files/paper/2016/hash/c8758b517083196f05ac29810b924aca-Abstract.html):
  the primary abstract's sharp curvature factor concerns optimization from
  uniform samples, a different access model.

The [Gong--Liu--Geng--Fang publisher abstract](https://link.springer.com/article/10.1007/s10878-023-01026-5)
was inspected afresh. It describes noisy submodular-minus-modular bicriteria
algorithms. Full theorem text remains unavailable in that preview; no claim
about its exact constants or absence of a particular theorem is justified.
This disclosed comparison limit is not a mathematical flaw or priority proof.

Fresh searches combined submodular, curvature/bounded curvature,
adversarial/persistent/multiplicative noise, erroneous oracle, approximation,
hardness and lower bound. No equivalent calibrated statement was located in
the inspected primary material. This finite screen does not establish
exhaustive novelty or recognized open status.

The nontrivial delta is the lower bound calibrated simultaneously to exact
curvature and unequal singleton noise intervals, together with the
all-query-size leakage bound and the epsilon*k divergence regime. The
uniform modular shift alone leaves every k-set worth at least (1-K)*k;
it cannot yield the strictly smaller rho*(1-K) barrier for fixed noise.
The new calibration changes that barrier while preserving exact curvature.
Its use is to establish when arbitrary adaptive query algorithms cannot
asymptotically improve the simple singleton method. For example, K=1/2 and
e0=1/3 yield the matching limit 1/4. For vanishing positive noise with
epsilon*k tending to infinity the limiting barrier is 1-K, separated from
the exact-oracle guarantee for K>0. This is a substantive parameter bound,
despite using established construction and proof patterns. It should be
presented as a short incremental result, without a claim of a new paradigm.

## Remaining boundaries and handoff

There is no unresolved mathematical gap in the frozen theorem found by
this review. Literature coverage remains bounded as disclosed above.
No manuscript or PDF was created in this referee job. Subsequent writing
must retain the exact accepted scope, all credited ingredients and limitations,
the five user-specified authors, and the official-template/12-total-page
requirements. Changing any decisive evidence requires a new freeze and
fresh mathematical review. The structural `check-math` outcome is recorded
separately; it checks integrity and provenance, not mathematical truth.
