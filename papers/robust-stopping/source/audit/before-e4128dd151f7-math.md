# Fresh mathematical referee report

Job: `robust-stopping-referee-1afb6017baeb` (referee).
Snapshot: `ddab1f97b4e3cfd90e3a03d39b4a5be6796cd12df3f12088626365322167231a`.
Review date: 2026-10-31, Asia/Shanghai.

**Verdict: accept the exact frozen result-note candidate.** The general
optimizer, support guarantee, all-domain primal/dual certificate, stated
arithmetic and bit complexity, and the specified support-level separation
pass this review. The original task remains **unresolved** as declared.
Acceptance is a fresh AI mathematical review, not human peer review, a
priority guarantee, publication acceptance, or a final artifact release.

## Scope and integrity

I read `requirements.md`, `source.md`, `problem.md`, `claim.json`, the frozen
snapshot and its listed evidence, including the unaccepted parent seed. I
did not read checkpoint/state files, earlier referee decisions, owner
transcripts, or owner progress summaries. Assertions of correctness in the
candidate dossier were not treated as evidence. The release contract was
read to implement this job's required audit schema.

All 22 frozen file hashes and the canonical snapshot digest were independently
recomputed and matched before testing and again afterwards. In particular,
the immutable source hash remains
`9721525d4da99587f7ef8b0f276225877c55b07af8d97e03a873448bbe839b32`.
No frozen evidence, statement, or implementation was changed. Fresh files
are confined to `audit/`. Requirements were reread before finalizing this
report. No manuscript/PDF, external submission, account action, additional
agent, model process, or background worker was created.

The accepted domain is every integer b>=2, every finite rational forecast
probability distribution on positive integer horizons, and every finite
rational R>=rho_b. Robustness is required at **every** actual integer
horizon. The accepted algorithm is the frozen `evidence/prefix_oracle.py`,
including its optional, bounded eight chord probes and guaranteed bisection
fallback. It returns an optimizer and exact certificate, with support in
S=[b] union {d+1:p_d>0,d>=b}, at most two support days >=b, and the stated
O(log Z) calls to an O(b^2+|S|) arithmetic oracle after forecast-cost
preprocessing. Polynomial bit time is in numerical b and binary input
length. No polynomial-in-log(b), strongly polynomial, full frontier
enumeration, or full resolution of `source.md` is accepted or implied.

## Reconstructed decisive argument

Write a=b-1, r=R-1>0, K=rb, and g(t)=E_p C_t(D). Expanding the cost gives

    E_f C_T(x) = x + sum_{t<=x}(a+t-x) f_t.

For each t the cost is nondecreasing in x, with limit b+t-1. Monotone
convergence proves that robustness implies E[T-1]<=K, without assuming
integrability in advance. Conversely that moment bound controls every
x>=b, and the b-1 displayed prefix inequalities control x<b. Thus the
reduction is exact on the unbounded actual-horizon domain.

For t>=b, round t down to the preceding member s of S. No positive forecast
atom lies in [s,t-1], so

    g(t)-g(s) = (t-s) Pr[D>=t] >= 0.

The move reduces moment and preserves every early prefix constraint. It
also dominates for g(t)+lambda(t-1) whenever lambda>=0. Thus finite-support
primal optimization and tail dual checking both extend to the original
infinite domain. The classical probabilities
b^(t-1)a^(b-t)/(b^b-a^b), 1<=t<=b, sum to one and saturate the classical
prefix and moment bounds. They establish nonemptiness for every admissible
R, including equality at rho_b; compactness now applies on S.

Temporarily remove both normalization and moment. Given a feasible prefix,
the exact feasible interval for coordinate i is

    0 <= z_i <= (ri-sum_{j<i}(a+j-i)z_j)/a.

For i>1 the numerator is at least r+sum_{j<i}z_j, using the preceding
constraint. It is strictly positive; future zero coordinates remain
feasible. Backward elimination therefore has no hidden extension condition.
Eliminating a coordinate chooses its zero or upper endpoint according to
the current reduced cost. This yields the recursion

    y_i=max(0,(alpha-c_i-sum_{j>i}(a+i-j)y_j)/a).

These are nonnegative dual prices for the raw prefix problem. Its minimum
value is -r sum_i i y_i. A canonical schedule v(B), with upper endpoints
exactly at B, attains this value when every positive y_i belongs to B and
every positive reduced slack is outside B. This is a direct elimination
argument; it does not assume the desired normalized optimizer.

The substantive normalization step is valid. For fixed B, differentiate the
triangular equations in alpha, writing h_i=dy_i/dalpha on B. If k is the
next active day after i, their equations imply

    1-sum_{j>i,j in B}(a+i-j)h_j
        = (k-i) sum_{j>=k,j in B}h_j > 0.

If there is no such k the left side is 1. Backward induction proves
h_i>0 on B and strictly negative slack derivative at every inactive day.
Existing prices cannot deactivate. Therefore the activation sweep has at
most b-1 events. Adding simultaneous zero-slack days leaves the current
y values unchanged, so simultaneous activation introduces no inconsistency.

The canonical schedule's total mass is
r(product_j(1+(s_j-s_{j-1})/a)-1). Inserting a day strictly increases it:
splitting a gap u+v introduces the positive extra factor uv/a^2; appending
also increases the product. At the first event where mass crosses 1, the
old and new raw schedules both minimize at the **same** alpha. Their
convex combination of mass exactly 1 is feasible and attains

    alpha-r sum_i i y_i.

The schedules individually may have mass above 1; the argument correctly
does not treat them as probability policies. If the tail cap min_{t>=b}c_t
is reached before a crossing, adding the missing mass on a minimizing tail
day gives the same primal/dual equality. Equality of mass to 1, empty
active sets, negative costs, cap/event ties and R>=b all satisfy this
argument. Reading `linear_oracle` confirmed that it implements precisely
these alternatives, including the interpolation at a crossing.

For the moment constraint set c_t=g(t)+lambda(t-1) and let Q be the
normalized prefix polytope on S. Its value q(lambda) is the lower envelope
of its finitely many vertex lines J+lambda mu. If the returned lambda=0
policy already has mu<=K, its zero moment price certifies the robust
optimum directly. Otherwise a bracket with left moment >K and right moment
<=K is necessary; monotonicity of minimizing moments follows by adding two
optimality inequalities. This holds for arbitrary tied-face outputs, not
only vertices.

I checked the explicit rational-isolation bound rather than assuming an
approximate price is sufficient. A vertex of Q has <=b positive entries.
One can select normalization and independent tight prefix rows on its
support. Their integer determinant has magnitude at most D=b! b^b; the
right-hand sides have common denominator q_R. Hence its coordinates have
common denominator dividing q_R times that determinant. Vertex moments
and objectives have denominators <=H=q_p q_R D and lie in [0,L], with
L=b+max S. Differences of these rationals have denominators <=H^2 and
numerators <=2LH^2. Any intersection of distinct-slope vertex lines
therefore has numerator and denominator <=Z=2LH^4. Distinct intersection
prices, including zero, are separated by >=1/Z^2, and all positive ones
are <=Z.

Consequently at price Z+1 every optimizing vertex has minimum possible
moment. Robust feasibility implies that moment is <=K. Bisecting the
bracket to width <1/Z^2 uses O(log Z) calls. A strict moment bracket must
contain an intersection; there is at most one distinct intersection in
the final closed bracket. On each adjacent open interval, optimizing
vertex lines have the same slope and intercept. Thus **both stored
endpoint policies**, including nonvertices or policies returned exactly
at a tie, optimize at the common price kappa. Their line intersection
recovers kappa exactly. The specified mixture has moment K and minimizes
q(kappa). The moment denominator is nonzero because mu_left>K>=mu_right.
Recomputing the prefix dual at kappa and subtracting kappa K proves the
claimed equality. If the crossing is at zero or mu_right=K, the same
formulas remain valid.

Each relaxed-oracle policy has at most one tail day; a mixture of two such
policies has at most two. The eight optional chord probes preserve the
bracket: their intersection lies between endpoint prices by endpoint
optimality; equal oracle and endpoint values certify that both endpoints
minimize there. A probe of moment K is independently sufficient. Strict
improvement cannot occur at an unchanged endpoint. The fallback still has
the proved call bound.

For any feasible law, taking expectations of the displayed global dual
inequality gives

    J >= alpha-r sum_{x=1}^{b-1} x y_x-lambda K.

The prefix sum is finite, g is bounded for the given forecast, and finite
moment was already proved. There is no signed infinite-series exchange or
unjustified limiting step. The returned equality is a sufficient global
certificate, independently of the algorithm that found it.

## Complexity and implementation scope

For fixed B the suffix sums of y_i, i y_i, h_i and i h_i compute the dual
state and all slack speeds in O(b) arithmetic operations. Scanning roots
and constructing v(B) each cost O(b). There are <=b-1 activations, and the
tail minimum costs O(|S|), establishing O(b^2+|S|) per oracle. Forming the
adjusted cost dictionary also fits this bound.

The bit claim survives exact tie handling and interpolation. On each B,
the affine coefficients in alpha solve a triangular system with diagonal
a and depth <=a. With rational input costs they have polynomial bit
length. Each activation price is a root of one such affine function of
the original costs; it is not an uncontrolled recursive expression in all
previous roots. Raw schedules have a common denominator q_R a^a, and
mass interpolation uses ratios of polynomial-length quantities.
The fixed eight chord probes preserve polynomial bit length. Subsequent
dyadic bisection adds O(log Z) denominator bits, and exact final line
intersection and dual reconstruction use polynomial-length rationals.
Since log Z=O(input length+b log b), the asserted rational-operation and
bit-time bounds follow. The deliberately conservative bound is valid;
observed small call counts do not replace it. Direct cost preprocessing in
the reference program is polynomial, as the claim permits.

## Independent exact checks

`audit/referee_verify.py` is a newly written verifier. Its saved-certificate
checks import neither the candidate optimizer nor the earlier enumerator.
They evaluate the original costs, probabilities, all early horizons, the
limiting moment, support restrictions, nonnegative prices, dual inequalities
at every necessary interval endpoint, and exact primal/dual equality.
For t>=b, the dual expression is nondecreasing between forecast jumps;
checking each left endpoint proves all omitted integer buy-days.

The completed run, recorded in `audit/referee-checks.json`, checked:

- All 611 saved full-optimizer certificates, all three saved forced-bisection
  certificates, and all 144 saved arbitrary-cost certificates: 758 total.
- 3,240 new exhaustive signed-cost vectors with repeated costs, b=2,...,5,
  including simultaneous activations and tail-cap ties.
- 246 new inputs chosen so a prescribed raw prefix schedule has mass
  exactly 1, b=2,...,9.
- 360 new seeded forecast inputs, b=2,...,17, covering R=rho_b, just above
  rho_b, R=2, R=b and R=11/2; sparse forecasts, very large positive horizons,
  and zero-probability atoms were included.
- Three new calls with chord probes disabled: two exercised 65 and 139
  bisection iterations; the third correctly terminated already at price
  zero. Each agreed exactly with the default algorithm.

All checks passed using `fractions.Fraction`. The new tests certify their
specific outputs by duality; the preceding analytic reconstruction, rather
than test coverage or replay of a search, establishes the quantified claim.
The original test driver was not run because it overwrites frozen evidence.

For b=3,R=3/2,p_1=2/5,p_2=3/5, direct evaluation yields
g(1)=3, g(2)=14/5, g(t)=8/5 for t>=3. The affine bound
g(t)>=3-(7/10)(t-1) proves J>=39/20, attained by (f_1,f_3)=(1/4,3/4).
Below level 14/5, every allowed day is >=3 and moment is at least 2>K=3/2.
At level 14/5, (f_2,f_3)=(1/2,1/2) is feasible. For all t>=2 the bound
g(t)>=4-(6/5)(t-1) proves the restricted optimum 11/5, attained by that
policy. Prefix feasibility was also checked directly. This proves the
claimed conceptual separation on the unbounded domain, rather than just
an implementation failure.

## Primary-source comparison and contribution

The nearest source is [Kim--Fan, arXiv:2603.29233v1](https://arxiv.org/html/2603.29233v1).
I inspected the cached primary HTML and reopened the current primary text,
especially Section 5, Appendix C.4 Theorem C.1 and Appendix D.2--D.8.
Lemma 5.1 gives the robustness reduction; C.1 already solves arbitrary
one-hot forecasts. D.3--D.4 contain the geometric and gap recurrences.
D.2 explicitly identifies the minimum feasible raw support level with
the expected objective optimum. The separation above targets precisely
that inference. The accepted delta is a certified general replacement:
backward dual elimination, nested normalization activation for arbitrary
linear costs, and exact moment-price/primal recovery with bit bounds.
Standard recurrences and LP principles must retain their existing credit.

[Li--Christianson--Li, arXiv:2510.14887v1](https://arxiv.org/html/2510.14887)
was checked at Section 5.2, Appendix D.1--D.3 and E.1. Its support reduction,
equalizing distributions, primal/dual methods and point-prediction frontier
constructions are close prior art. They do not supply the general arbitrary
forecast optimizer reviewed here; their asymptotic strong-optimality
qualifier must not be omitted when cited.

[Cui--Dinitz, arXiv:2602.21104v1](https://arxiv.org/html/2602.21104v1),
Section 2.1 and its stated guarantees, use additive loss against the policy
knowing the true distribution under unknown Wasserstein error. This is a
different benchmark from an externally fixed hard pointwise cap.

[Hartline--Johnsen--Shah, ITCS 2026](https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/html/LIPIcs.ITCS.2026.75/LIPIcs.ITCS.2026.75.html),
Definitions 1--2 and Section 2.1, use a Bayesian-policy benchmark and a known
finite sequence length with online good/bad weather observations. General
zero-sum optimization methods are prior tools, not the new contribution.

[Yoshinaga--Kawase, arXiv:2601.06813v1](https://arxiv.org/html/2601.06813),
Section 4.1, optimizes distributionally robust expected ratios under nested
prediction intervals using LPs. Its forecast set and metric differ from
this fixed arbitrary expected-cost objective with prescribed robustness.

[Diakonikolas et al., ICML 2021](https://proceedings.mlr.press/v139/diakonikolas21a/diakonikolas21a.pdf),
Section 2.1, Corollary 2.8 and Theorem 2.9, provides distributional learning
and strategy combination results; generic mixing is established prior art.
[Kang--Park--Fan, AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/40991/44952),
Algorithm 1 and its surrounding model, uses a posterior rental-cost rule
on a known bounded horizon, without the prescribed cap R as an input.
Neither inspected statement is the complete optimizer accepted here.

Fresh web searches included arbitrary-distribution hard-robust randomized
ski-rental optimization, prefix linear optimization, and triangular/nested
parametric LPs. Search results were used to locate primary statements, not
as proof of absence. I found no equivalent complete construction in these
inspected sources. The remaining literature screen is bounded: unrelated
sections and every historical general optimization result were not audited.
There is no exhaustive priority or historical duplicate certificate.

This is a substantive result note because the universal forecast input is
not a toy restriction, the nested activation proof supplies an explicit
solver beyond an LP restatement, and its global certificate repairs a
concrete expected-cost error while retaining all prefix and tail constraints.
It has a credible use as an exact forecast-policy constructor and verifier.
The small separating example, support reduction, standard duality and
frontier convexity would not independently qualify as separate papers.
They belong with the optimizer in one coherent note. Acceptance does not
rest on the user's requested paper count or assumed venue suitability.

## Remaining limits and handoff

No mathematical gap was found within the exact frozen theorem. No scope
was weakened or repaired in this pass. The original broader task, complete
frontier enumeration and improved dependence on binary b remain outside the
accepted result. Literature priority remains subject to the stated bounded
screen. The audit permits the runner to proceed to the separate writing
phase only after the structural `check-math` gate passes. The exact five
authors, official unmodified ACM template and <=12 total pages remain
requirements for that future phase; none is certified by this math audit.

The structural gate result is saved separately in
`audit/referee-gate-check.json`. That gate checks hashes and real runner
role provenance; it does not certify this report's mathematics.
