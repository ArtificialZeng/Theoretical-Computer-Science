# Research pass 1: outcome and reproducible evidence

Job `robust-stopping-research-a43d444f406e`. The proposed contribution is an
exact general repaired optimizer, submitted as a result-note candidate only.
Original status remains unresolved. No fresh mathematical referee has run;
no mathematical acceptance, manuscript or PDF has been created.

`research-argument.md` states and argues the quantified theorem, the
normalization sweep, the exact one-dimensional moment-price recovery,
bit complexity, unbounded-domain primal/dual certificates, scope and gaps.
`prefix_oracle.py` is a Python standard-library implementation. Its prefix
oracle uses dual-adjusted slacks; its activation sets are nested. Consecutive
geometric and gap recurrences are credited to Kim--Fan, not claimed new.
The proposed contribution is the corrected selection/optimization rule and
its exact certificate construction.

## Exact coverage

Run from the project root:

    python3 evidence/test_prefix_oracle.py
    python3 evidence/check_oracle_certificates.py
    python3 evidence/check_triage_certificate.py

The test module imports the unchanged triage rational basis enumerator,
which is separate from the new optimizer. No floating-point solver is used.
All basis enumeration uses normalization plus tight constraints and support
faces; with b robustness inequalities a vertex has at most b+1 positive
coordinates. Enumerating all independent bases of every such support covers
all vertices, including degenerate ones (repetitions are removed).

- 594 specified small cases: b=2,3,4; R=rho_b,3/2,2; all six one-hot forecasts
  on horizons <=6 and all 60 two-point forecasts on distinct horizons <=6
  with weights a/5, a=1,2,3,4. For each fixed b,R the full robust polytope on
  days 1,...,7 is enumerated once. Every optimum agrees exactly.
- 12 held-out cases: b=5; R=3125/2101,3/2,7/4,3; three forecasts with 3 or
  8 atoms on horizons <=8, with full robust vertex enumeration on days <=9.
  All agree. This is a larger dimension and a non-two-point family.
- 144 arbitrary signed-cost tests for the moment-relaxed normalized prefix
  oracle: b=2,3,4,5, R=3/2,3,11/2 and 12 deterministic seeded cost vectors
  for each pair, on days 1,...,7. Independent generic basis enumeration of
  this different polytope agrees in all cases. Signed costs exercise
  normalization and the tail cap independently of forecast shape.
- Five larger full-optimizer certificates: b=12,20,40,100 (and b=3,R=5),
  verified by direct exact primal/dual inequalities, without enumeration.
- Three cases force max_chord_probes=0, exercising the guaranteed bisection
  fallback. They require respectively 139,205,297 isolation iterations and
  agree with the accelerated implementation. The largest number of oracle
  calls in the default 611-case run was eight. This is observed performance,
  not a worst-case bound replacing the proved bit-complexity statement.

`oracle-tests.json` gives coverage. `oracle-test-cases.json` stores all 611
full-optimizer policies and dual prices; `linear-oracle-test-cases.json`
stores all 144 arbitrary-cost certificates; `bisection-test-cases.json`
stores the three forced fallback certificates. The separate checker imports
neither optimizer nor enumerator. It checks every original hypothesis,
finite prefix and moment constraint, dual inequality for every buy-day up
to M=max(b,N+1,support f), and exact equality of objectives. Above M, g is
constant, the prefix-dual contribution is empty and lambda>=0, proving all
remaining dual inequalities. Prefixes plus the moment certify robustness
for all actual horizons. `oracle-certificates.json` binds the three data
files and reports the counts. This is same-worker deterministic arithmetic
verification, not fresh mathematical review.

The default cases include 57 policies with two tail days, 252 certificates
with both lambda>0 and a positive prefix dual multiplier, and 106 policies
entirely before day b. These counts are descriptive, not extra theorems.
For example, b=2,R=3/2,p_2=1/5,p_3=4/5 gives f_1=1/2,f_2=1/4,f_4=1/4,
value 49/20, lambda=1/10, alpha=31/10,y_1=11/10. The exact certificates
therefore exercise more than a tail-only affine lower bound.

## Failure and operational record

One initial large-case input used b=40,R=3/2, below rho_40, and was rejected
by the feasibility assertion. That input was corrected to R=8/5 and explicit
admissibility validation was added. This was an invalid test input, not a
counterexample to the theorem. A deliberately conservative pure-bisection
large-b stress run was interrupted before output after its small tests had
completed; no result from the interrupted run is counted. Eight optional
exact chord probes now accelerate discovery, with equality certified by the
same dual and bisection retained as a guaranteed fallback. The recorded
successful runs are complete and no test process remains active.

The unchanged triage separation still proves V=39/20 while the best policy
within the minimum feasible raw support level costs 11/5, for b=3,R=3/2,
p_1=2/5,p_2=3/5. The new solver reproduces f_1=1/4,f_3=3/4,lambda=7/10,
alpha=3 and y=0. This conceptual correction is paired with the general
repair; the small example alone was not promoted as a standalone result.

## Next gate

Freeze `claim.json` and its listed files, then request the runner's real
fresh referee. Ask it to attack equation (7), simultaneous activations and
mass truncation (8), tied/nonvertex oracle outputs in rational isolation,
intermediate bit bounds, and novelty/substantive value against the closest
primary results. The source remains immutable; there is no authority in
this research job to manufacture acceptance or proceed to manuscript work.
