# Triage evidence and proposed repair route

Job: robust-stopping-triage-ef6eadc61ec7. Date: 2026-10-31 Asia/Shanghai.
Status: researcher-derived triage arguments, without fresh mathematical review.
The full original task remains unresolved; these observations do not qualify
as an accepted standalone contribution.

## Exact separation of the support-level criterion

For the source's model let b=3, R=3/2, p_1=2/5 and p_2=3/5.
This is admissible because the classical optimum is rho_3=27/19<3/2.
Writing g(t)=sum_x p_x C_t(x), direct calculation gives

    g(1)=3, g(2)=14/5, g(t)=8/5 for every t>=3.

Define the idealized support-level feasibility quantity

    h_* = inf {h: some R-robust f has support contained in {t:g(t)<=h}}.

This tests the conceptual criterion, granting an exact feasibility oracle;
it does not depend on Algorithm 3's indexing or numerical implementation.

Every robust law has moment mu=E[T-1]<=3/2. Since, for every positive t,

    g(t) >= 3 - (7/10)(t-1),

its expected cost is at least 3-(7/10)(3/2)=39/20.
The law f_1=1/4, f_3=3/4 attains this bound. Its prefix quantities at
x=1,2 are respectively 1/2 and 1/4, below the required bounds 1/2 and 1;
its moment is 3/2. Thus it is robust for all integer horizons, and its
expected cost 39/20 is globally optimal. The displayed affine minorant is
an exact dual lower-bound certificate for the unbounded policy domain.

For h<14/5, the allowed support is either empty or contained in {3,4,...}.
Every law on the latter set has moment at least 2 and is infeasible.
For h=14/5 the law f_2=f_3=1/2 is feasible: its prefix quantities are 0,1,
and its moment is 3/2. Consequently h_*=14/5.

Every law allowed at this minimum h has f_1=0. For t>=2,

    g(t) >= 4 - (6/5)(t-1),

so every such feasible law has expected cost at least 4-(6/5)(3/2)=11/5.
The law f_2=f_3=1/2 attains that value. Therefore

    V_p(3/2)=39/20 < 11/5
      = min expected cost among minimum-support-level-feasible policies.

The gap is 1/4. The expected-cost optimum necessarily uses day 1, whose
individual cost 3 exceeds the minimum feasible threshold 14/5. Thus even
optimizing perfectly inside the minimum feasible support-level set does
not recover the expected-cost optimum.

This isolates the inference in arXiv:2603.29233v1 Appendix D.2 that minimum
feasible support level gives expected-cost optimality. D's introduction
also uses the weaker wording “decent solution”; the separation concerns
the explicit optimality inference and the Section 5.3 support-level rule.
It does not refute Lemma 5.1, the monotone-objective results, or Appendix
C.4's one-hot theorem. It does not resolve the source's general task.

## Exact computational discovery and coverage

Run `python3 evidence/triage_exact.py` from the project directory. It uses
only Python's standard library and rational Gaussian elimination. It
enumerates vertices by choosing positive support and independent tight
constraints (normalization, b-1 prefix bounds, and the tail moment). With
b inequalities besides normalization a vertex has at most b+1 positive
coordinates. Every support face at a feasible threshold is a face of the
same polytope, so vertex enumeration also finds the support-threshold
optimum and the best expected objective within that support face.

The saved run stopped at its first separation after 62 cases: all 60
two-point forecasts on {1,...,6} with weights 1/5,2/5,3/5,4/5 at b=2,
R=7/5, followed by two cases at b=3,R=3/2. It used M=7, deliberately
padding the actual two-day forecast, and found seven vertices in the
separating case. No larger sweep was performed. A second run with the
minimal valid cutoff M=3 found three vertices and the same exact values.
The analytic certificates above, rather than this finite search alone,
establish the stated separation on the full policy domain.

## Routine reductions: baseline tools, not novelty claims

Let F(x)=sum_{t<=x}f_t and mu(x)=sum_{t<=x}(t-1)f_t. Expanding costs gives

    E C_T(x) = x + mu(x) + (b-x)F(x).

For each fixed T the cost is nondecreasing in x and tends to b+T-1.
Monotone convergence shows that finite robustness implies
mu(infinity)<=K=(R-1)b; conversely that moment bound and the b-1 prefix
inequalities imply robustness for all x. This is precisely the existing
Lemma 5.1, reproduced here to justify unbounded-horizon certificates.

Set M=max(b,N+1). Move every atom at t>M to M. Its forecast cost is
unchanged because both days exceed N, its moment decreases, and all
prefix inequalities x<b are unchanged. Thus an optimizer exists in the
compact finite feasible polytope on {1,...,M}.

A sharper routine reduction uses forecast support D={d:p_d>0}. Some
optimizer has support contained in

    S={1,...,b} union {d+1:d in D and d>=b}.

For t>=b map it to s=max({b} union {d+1<=t:d in D}). On the entire
integer interval from s to t there is no forecast atom at a horizon in
[s,t-1]. Hence g is affine nondecreasing there, and g(s)<=g(t).
This move reduces moment and leaves all x<b constraints unchanged.
Applying it atomwise gives the claim; S has at most b+|D| elements.
For fixed early masses on {1,...,b-1}, the remaining tail has prescribed
total mass and an upper bound on its first moment. Its optimum is given
by the lower convex hull of (t-1,g(t)) for t in S,t>=b and can be chosen
with at most two tail atoms. This is a standard two-constraint linear
optimization fact, not by itself a publishable advance.

## Admission and next test

Advance one bounded research pass. Nearest prior result: Lemma 5.1,
Appendix C.4, and the claimed general water-filling construction. Proposed
delta: a corrected, explicit primal/dual optimizer for arbitrary forecasts
that handles both the prefix inequalities and tail moment, with a proved
running time beyond a generic LP call. The exact separation motivates the
repair; the routine support/hull reductions supply a finite verifier.

One next test: construct the tail-moment Lagrangian oracle for
c_lambda(t)=g(t)+lambda(t-1), lambda>=0, with explicit optimization over
the prefix constraints and probability simplex. Test the proposed
piecewise-geometric prefix rule and its dual inequalities against all
exact vertices for b=2,3,4, N<=6 and two-point probabilities with denominator
5, at R=rho_b,3/2,2 whenever admissible. A mismatch rejects that rule; a
match is only finite evidence and must be followed by a quantified proof
and bit-complexity analysis. Merely stating Lagrangian duality, using a
generic LP, or publishing this small separation does not meet the target.
