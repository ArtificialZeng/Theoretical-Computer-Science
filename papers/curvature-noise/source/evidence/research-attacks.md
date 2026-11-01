# Adversarial checks and candidate limits

Job `curvature-noise-research-5a09759394ef`. These are research checks, not a
fresh review, human peer review, or an acceptance flag.

## Decisive analytic checks

* **Fixed oracle versus adaptive adversary.** The maximum formula defines a
  single table on every subset before the private seed is sampled. No answer
  is modified during a run. The uniform choice of H is only a proof device;
  finite averaging selects one H for the algorithm's entire seed distribution.
* **Adaptive selection bias.** A per-query probability assertion is applied
  only to queries from the H-independent baseline transcript. After the first
  divergence no further query independence is claimed. The disagreement
  event is bounded using that baseline sequence and induction.
* **Promise-only algorithm budget.** The baseline g0 is an allowed noisy
  oracle for F0 of the same exact curvature. Hence its run obeys the same
  query bound and feasible-output promise. The algorithm is not given OPT
  or hidden singleton values as additional information in `problem.md`.
* **Unqueried output.** No assumption that the output was queried is needed.
  On agreement its value is bounded directly using the expected intersection
  with a uniform H; on disagreement every feasible true value is at most k.
* **Large queries.** The same hypergeometric union bound applies through
  s=n. The proof never limits query cardinality to the feasibility budget.
* **Integer thresholds.** The conservative event X>=ceil(cs) contains the
  leakage event even when cs is integral. If ceil(cs)>k its probability is
  zero. No membership-independence approximation is made.
* **Noise and curvature boundaries.** K=0 is valid and has c=1; in fact
  every oracle answer is independent of H, as also checked exactly. The
  proof excludes K=1 and epsilon=0 rather than substituting into a vanishing
  denominator. Tiny positive epsilon and K arbitrarily close to one appear
  in the held-out finite grid, but the corollary requires fixed K<1.
* **Vanishing target.** When rho->0, additive o(1) matching does not imply
  relative sharpness. The candidate explicitly retains that limitation.
* **Polynomial-query quantifiers.** C and d are fixed for each algorithm
  family; they are not optimized afresh at each finite n.

No exact counterexample was found to the finite statement. A known-method
comparison also shows why the specified uniform modular-shift family cannot
prove the smaller fixed-noise product factor: all its k-set true values are
at least (1-K)k. This is only an obstruction to that particular family.

## Reproducible finite checks

Run from the project directory:

    python3 evidence/research_check.py

It prints JSON and does not overwrite evidence. The saved output is
`evidence/research-checks.json`. It verifies the original source hash before
and after. Only Python's standard library is required.

The held-out range n=12,...,18, epsilon in {1/101,2/5,99/100}, and curvature
in {1/101,2/3,99/100} is disjoint from the triage grids. For k=2,...,min(6,n-2)
and r in {1,k-1}, subject to n>k+r, it checks all feasible (s,h) pairs,
global oracle bounds, the leakage implication, and the exact hypergeometric
union bound. Result: 567 tuples, 33,894 feasible points, 7,308 tail checks.

For four n=6,k=2,r=1 instances, the verifier exactly optimizes over every
adaptive deterministic policy through depth Q=2. A fifth n=8,k=3,r=2
instance is optimized through Q=1. Each case enumerates every hidden k-set,
every query subset of all sizes, and every possible k-set output. Queries
with the same response partition are deduplicated without changing available
information. The Bellman value of a posterior set of hidden instances is
the maximum total true payoff over outputs at depth zero; at larger depth
it is the maximum sum of child values over all query-response partitions.
Uniform hidden probabilities permit integer total-payoff recursion. This
also covers randomized policies by averaging deterministic policies.

All 14 depth/case results satisfy the exact bound (8). For example, at
n=6,k=2,r=1,epsilon=3/4,K=1/2, the exact optimal expected ratios for
Q=0,1,2 are 29/70, 15/28, and 55/84. The corresponding bound is
29/70+Q/5. These checks are nonvacuous at both positive query depths.
At K=0,epsilon=2/5 every depth has ratio 13/21 and zero leakage.

These finite enumerations do not establish arbitrary Q, arbitrary parameters,
the exponential relaxation with Euler's constant, or asymptotics. Those
assertions depend on the analytic proof, not on computation. There is no
claim that the tested policies are an independent fresh model review.

## Remaining risks for a referee

The exact finite theorem and asymptotic deduction have no known analytic gap
in this dossier. Their novelty/significance is less certain than their
derivation: the construction and proof pattern are known, and this is a
calibrated bound rather than a new method. A finite primary-source search
cannot exclude differently phrased earlier results. The Gong--Liu--Geng--Fang
full theorem text remains uninspected. No manuscript may be created unless
the real fresh-referee gate accepts this exact contribution and scope.
