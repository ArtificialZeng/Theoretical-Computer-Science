# Frozen interpretation and triage scope

Provenance: `robust-stopping-triage-ef6eadc61ec7`, triage, 2026-10-31
(Asia/Shanghai). The original question is the complete, unchanged `source.md`,
SHA-256 `9721525d4da99587f7ef8b0f276225877c55b07af8d97e03a873448bbe839b32`.
This file interprets that question; it does not replace it.

## Exact model

Input: an integer b >= 2; an integer N >= 1; rational probabilities
p_1,...,p_N >= 0 with sum 1; and a finite rational R >=
rho_b = b^b/(b^b-(b-1)^b). Zero-probability entries are allowed. A policy is
a probability mass function f on the positive integers, with sum f_t=1,
drawn independently of the actual integer horizon x. Buying takes place at
the start of day T, if the season survives to that day. Its cost is x for
T>x and b+T-1 for T<=x. No mass at infinity is allowed by the source;
finite hard robustness would exclude such mass in any event.

For every integer x >= 1, require

    sum_t f_t C_t(x) <= R min(x,b).

For each such input, characterize an optimizer of

    V_p(R) = inf_f sum_{x=1}^N p_x sum_t f_t C_t(x).

The universal robustness quantifier is over the unbounded actual horizon,
not merely x<=N. All expectations over f are internal randomization against
a fixed obliviously chosen horizon. Advice p describes the objective and
does not restrict the adversary. The ratio of expectations
V_p(R)/sum_x p_x min(x,b) has the same optimizers, because its denominator
is fixed and positive. The different objective
sum_x p_x E_f[C_T(x)]/min(x,b) generally does not.

The source is a research task rather than a single asserted theorem: seek a
structural and algorithmic characterization for every rational input, an
exact robustness/objective tradeoff, and a precise assessment and useful
repair of the water-level argument in arXiv:2603.29233. A subsidiary
counterexample does not resolve this complete task. Any running-time claim
must distinguish dependence on numerical b,N from their binary encoding,
and specify exact rational output versus approximation.

## Closest prior statements and admission target

Kim--Fan, arXiv:2603.29233v1, Section 5, has exactly this cost function,
objective and hard robustness constraint. Lemma 5.1 reduces robustness to
the b-1 prefix inequalities and one moment bound. Theorems 5.2--5.3 treat
special objective shapes. Appendix C.4 Theorem C.1 solves all one-hot
forecasts. Section 5.3 and Appendix D propose general water filling; D.2
identifies support-threshold feasibility with expected-cost optimality.
These are substantive prior claims to audit, not absent baselines.

The proposed delta is a general, certified optimization rule that correctly
accounts for the prefix constraints and tail moment, beyond an LP
restatement. A small failure of Algorithm 3 or a one-hot formula alone
does not qualify. First distinguish expected cost from minimization of the
maximum deterministic-threshold cost appearing in the policy's support.
Then test a dual-adjusted greedy/hull construction on exact small cases.

Cui--Dinitz, arXiv:2602.21104v1, Section 2, instead compares additive loss
against the best policy knowing the true distribution, with unknown
Wasserstein error; its principal guarantee does not settle this exact
constrained optimization. Hartline--Johnsen--Shah, ITCS 2026, Sections 2--4,
uses finite weather sequences and prior-independent performance against a
Bayesian policy; its algorithmic framework must be credited, but the
specific theorem is not the same model.

Additional close overlap: arXiv:2510.14887, Section 5 and Appendices D--E,
already gives prediction-specific randomized Pareto constructions and
one-hot support reduction. arXiv:2601.06813 Section 4 optimizes a weighted
worst-case interval metric by LP, which differs from an arbitrary forecast
expected-cost objective. Neither source justifies calling this question
recognized open. Literature status: `status-uncertain`; contribution and
novelty remain to be established.

## Boundaries

This is an independent lead, not a subdivision of the coverage result.
`selection.md` is the available local historical topic screen; there is no
full historical registry in this project. No candidate-argument.md exists
at intake. No mathematical acceptance, manuscript or PDF is authorized by
triage. Later phases must reread requirements.md and use the real fresh
referee and release gates, the exact five authors, official template, and
12-total-page limit.
