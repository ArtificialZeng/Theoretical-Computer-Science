# Fresh mathematical referee report

Verdict: **accept**, as one `result-note`; original status: **unresolved**.
Job: `robust-stopping-referee-e4128dd151f7`.
Snapshot: `16612a3cefda20c6efcd422319de1c7c33a069858cbf520c875c4612c7ef6b36`.
Review completed 2026-11-01 Asia/Shanghai.

This decision covers the entire exact statement in frozen `claim.json`:
the general optimizer with `max_chord_probes=0`, its support, certificates,
arithmetic/bit bounds, the uniform frontier with uniqueness and sharp support,
and both small objective separations. No failed portion has been dropped.
This is a fresh model-context mathematical review, not human peer review,
certification of priority, or a judgment of suitability for STOC.

## Inputs and integrity

I read the source, precise interpretation, claim, snapshot, requirements,
required revision instructions/seed, central frozen arguments, implementation,
and relevant primary passages. I did not consult checkpoint, scheduling
state, owner verdicts, earlier job transcripts, or earlier audit contents.
Existing math reports were preserved under `audit/before-e4128dd151f7-*`
without inspecting their contents. All 39 frozen-file hashes and the
canonical digest independently matched before and after the computation.
The immutable source SHA-256 is
`9721525d4da99587f7ef8b0f276225877c55b07af8d97e03a873448bbe839b32`.
No frozen input, manuscript, source statement, or role metadata was changed.

The required newer published-software handoff was read as an instruction;
its additional unfrozen execution files are outside this decision. This
acceptance makes no claim about actual author-software output.

## General optimizer: reconstructed decisive steps

Set a=b-1, r=R-1, K=rb and g(t)=E_p C_t(D). For fixed t, C_t(x)
increases to b+t-1. Monotone convergence therefore yields E(T-1)<=K
from robustness without assuming a finite moment. Expanding the early
costs gives exactly

    A_x f = sum_{t<=x}(a+t-x)f_t <= rx,  1<=x<b.

Conversely these rows and the moment bound imply every original
robustness constraint: early horizons use the rows and later ones use
C_t(x)<=b+t-1. The geometric law in the proof directly verifies
nonemptiness even at R=rho_b. Infinite original policy support presents
no extra compactness assumption.

For t>=b, move its mass to the last s<=t in
{b} union {d+1:p_d>0,d>=b}. No forecast atom lies in [s,t-1], so
g(t)-g(s)=(t-s)Pr[D>=t]>=0. The move reduces moment and leaves early
rows unchanged. Applying this atomwise proves the finite compact reduction
to S. The same dominance holds for g(t)+lambda(t-1), lambda>=0;
it extends finite dual checks to every omitted buy-day. Zero forecast
probabilities and arbitrarily large encoded horizon values are covered.

For the unnormalized prefix polytope, each feasible preceding prefix
leaves exactly [0,U_i] as the next-coordinate interval. The preceding
row bounds its numerator below by r+sum_{j<i}f_j>0, and all future
coordinates may be zero because subsequent old left sides decrease.
Backward elimination therefore minimizes an affine function exactly:
select zero for nonnegative coefficient, U_i for negative coefficient,
and substitute into earlier costs. Induction gives equality of value
functions for every feasible preceding prefix. The supplement supplies
the needed proof rather than merely assuming a greedy principle.

For coefficients c_i-alpha this gives the nonnegative triangular
recurrence y_i and value -r sum i y_i. Positive y_i select tight rows;
positive reduced costs select zero mass. These relations prove exact
primal-dual equality directly.

For normalization, on active set B the derivatives h_i solve the stated
triangular equations. If k is the next active index after i, subtracting
the equation at k gives inactive-slack speed
(k-i)sum_{j>=k}h_j>0; beyond the last active index it is 1. The same
backward induction gives h_i>0 on B. Thus positive dual coordinates
never deactivate, inactive slacks decrease strictly with alpha, and at
most b-1 activation events occur, with simultaneous activations allowed.

The canonical prefix mass is r(product(1+gap/a)-1). Inserting a day
strictly increases it: splitting gap u+v introduces positive extra term
uv/a^2; appending a day adds a factor greater than one. At an activation
the old and new schedules both minimize the prefix objective because
new multipliers are zero there. If their masses straddle 1, the displayed
convex combination restores exactly mass 1, stays feasible, and attains
the dual value. If the cheapest tail cap is reached first, residual
mass at that tail does so. Mass exactly one, ties, negative costs and
an empty active set require no generic-position assumption. Suffix sums
make each event O(b), yielding O(b^2+|S|) operations per oracle call.

For moment pricing, q(lambda)=min_Q(J+lambda mu) is a finite lower
envelope. Adding the optimality inequalities at two prices proves that
minimizing moments are nonincreasing. Each vertex of Q has at most b
positive coordinates. A basis uses normalization and independent prefix
rows, has integer entries bounded by b, and determinant bounded by
D=b!b^b. Its coordinates have common denominator q_R|det|; objectives
and moments have denominators <=H and values in [0,L]. Intersections
of distinct vertex lines with different moments therefore have reduced
numerator and denominator bounded by Z=2LH^4. Distinct intersection
prices are at least 1/Z^2 apart.

At Z+1 every minimizing vertex has minimum feasible moment, which is
<=K by nonemptiness. Bisection maintains a left policy with moment >K
and a right policy with moment <=K. Once its width is below 1/Z^2,
the bracket contains exactly one relevant breakpoint: no breakpoint
would force the same optimizing moment throughout, and two distinct
ones are excluded by separation. Both endpoint policies optimize at
that price by continuity, even for nonvertex tied outputs. Their line
intersection and moment interpolation give the exact price and moment-K
law. Recomputing the oracle dual certifies equality after subtracting
lambda K. Endpoint breakpoints and a right moment already equal to K
are included. This proves the code's pure-bisection path.

Each oracle law uses at most one day >=b. The final mixture uses at
most two such days and at most b+1 total. Its nonnegative prices obey

    g(t)+lambda(t-1)+sum_{x>=t,x<b}(a+t-x)y_x >= alpha

on all positive integer buy-days by dominance. Taking expectations
gives the claimed global lower bound, attained by the constructed law.
There is no signed infinite-sum gap: g is bounded, the prefix term is
finitely supported, and finite moment was established from robustness.

## Intermediate bits and operation counts

For any fixed active set of size k, write y_i=u_i alpha+v_i directly
in the original current costs. Their denominators divide a^k and Q a^k,
respectively, where Q is a common cost denominator. Absolute growth is
at most exponential in b, hence polynomial in bit length. Each activation
root is a ratio of these affine coefficients, with
O(log Q+log M+b log b) bits. Recomputing this system from original
costs avoids iterating denominator bounds from previous roots. Suffix
sums share the same denominators.

Canonical schedules have common denominator dividing q_R a^a;
normalization interpolation has polynomial bit length. Bisection takes
O(log Z) steps and its dyadic prices have O(log Z) bits. Adjusted
costs and final line intersections/interpolation therefore retain
polynomial bit length in numerical b and input binary length. This
adequately covers intermediate values as well as output. The claim
correctly distinguishes oracle calls from total rational operations,
allows polynomial preprocessing for g, and asserts neither strong
polynomiality nor polynomial time in log b. Generic finite LP already
gives polynomial bit time; no asymptotic speedup follows here.

## Uniform frontier, uniqueness, and sharp support

Direct summation gives g(t)=m+d_t for 1<=t<=b and m thereafter.
The A_j,C_j,M_j geometric identities follow by one-step recurrence.
C_j strictly increases, so the breakpoints are strictly ordered and
have the claimed classical lower endpoint. On segment j, endpoint
checks give 0<=f_j<=r z_j. Earlier prefix rows are tight, the jth
row is feasible, and later zero-extension rows gain slack. The residual
tail is nonnegative at r_j because M_j<=b, strictly for j<b, and
then throughout by affinity. The formula makes mu=rb. Adjacent endpoint
policies agree.

For lambda_j=(b+j-2)/(2b)>0, alpha=m+lambda_j b and y_i=0 for i>=j,
the equality equations give y_i>0 for every i<j. Their base value is
a y_{j-1}=(b-j+2)/(2b), and successive increments use the positive
quantity (b+j-2i)/(2b). Reduced costs vanish exactly on
{1,...,j,b+1}. At j<t<=b they are
(b+1-t)(t-j)/(2b)>0; at t>b+1 they are
lambda_j(t-b-1)>0. This proves a dual inequality on the infinite domain.

The dual gap decomposes into nonnegative reduced-cost, prefix-slack and
moment-slack terms. Equality forces precisely that allowed support,
tight first j-1 rows and tight moment. Those equations and normalization
uniquely determine the displayed law, including r=r_b and r=1 and
both formulas at every shared endpoint. For r>1, T=b+1 attains the
unconstrained minimum m; uniqueness is not claimed.

Substitution gives the stated affine pieces. Their slopes obey
s_1=-(b-1)/2 and s_{j+1}-s_j=-(b+C_j)/(2b)<0. Since increasing r
encounters decreasing j, slopes increase strictly to the final zero
plateau. Every segment has positive length, proving exactly b decreasing
pieces and the plateau. On the open bottom segment all b+1 masses
are positive, and uniqueness proves their necessity, including both
days b and b+1.

Consecutive terms and cumulative sums give the shared table in O(b)
rational operations. Common power denominators, the factor 2b and
the query R give O(b log b+len(R)) bits per rational. Dense listing
of b whole policy vectors is correctly excluded from that operation
bound. I found no exception at b=2 or at any type of endpoint.

## Exact objective separations

For b=3,R=3/2,p=(2/5,3/5), costs are 3,14/5,8/5,8/5,... .
The inequality g(t)+(7/10)(t-1)>=3 is tight at 1 and 3; the law
f_1=1/4,f_3=3/4 attains the lower bound 39/20. Below raw support
level 14/5 only days >=3 are allowed, whose moment is at least
2>3/2. At that level row 2 gives f_2<=1/2 while moment and support
give mu>=2-f_2. Thus f_2=1/2 and all residual mass is at day 3,
giving unique feasible law there and cost 11/5. This refutes exactly
the expected-cost/support-level identification. The frozen literal
Algorithm 3 trace distinguishes its moment updates and tail scan from
that ideal prescription; 11/5 is not certified as actual software output.

For p=(1/2,1/2), cost coefficients are (3,5/2,3/2,...) and
expected-ratio coefficients (9/4,3/2,1,...). Their global dual
inequalities have (alpha,lambda)=(3,3/4) and (2,1/2), respectively,
and equality sets {1,3} and {2,3}. They prove the claimed unique
optima 15/8 and 5/4, with cross-objective values 21/16 and 2.
Both laws satisfy every prefix constraint. Dividing cost by the fixed
positive expected offline optimum instead preserves its optimizer.

## Independent computations actually performed

I wrote `audit/referee-e4128dd151f7.py` in this pass. It imports the
implementations but none of the candidate's verifiers/search routines.
It uses direct original-cost, prefix, moment and dual checks, plus
its own rational Gaussian elimination and generic vertex enumeration.
All of the following passed:

- 611 saved general-optimizer, 3 saved forced-bisection and 144 saved
  signed-oracle certificates;
- 84 new signed/tied/zero-cost oracle instances compared with every
  vertex of the corresponding small normalized prefix polytope;
- 40 new pure-bisection cases, including classical-minimum robustness,
  zero forecast entries, huge sparse horizons and very large R;
- 1,119 uniform direct-certificate instances for b=2,...,22,37,61,
  with both endpoint formulas, sevenths within segments, plateau,
  positive dual signs, reduced-cost zero sets and sharp support;
- 63 new exact vertex comparisons in total, including small uniform
  uniqueness tests, plus exact checks of both separating examples.

Inputs, counts and binding are saved in
`audit/referee-e4128dd151f7-checks.json`. These finite checks support
implementation behavior; the quantified conclusions rest on the proofs.

## Primary comparison and substantive contribution

The nearest source is [Kim--Fan v1](https://arxiv.org/html/2603.29233v1),
Section 5, C.4 and D.2--D.7. The robustness reduction and geometric/gap
recurrences are prior. At y=b, C.1(ii) gives the same capped law for
r<=1-1/b: the candidate moment equation is Phi(P)=b(1-r), which
dominates Phi(Pcheap) on exactly that range. Above it the uniform law
is another one-hot-b optimum. This overlap is correctly credited.
D.2 makes the inference refuted by the separating example. The current
[PMLR publication](https://proceedings.mlr.press/v306/kim26l.html)
was confirmed; the accepted criticism remains version-specific.

I inspected relevant primary statements of
[Li--Christianson--Li](https://arxiv.org/html/2510.14887v1),
[Diakonikolas et al.](https://proceedings.mlr.press/v139/diakonikolas21a/diakonikolas21a.pdf),
[Cui--Dinitz](https://arxiv.org/html/2602.21104v1), and
[Hartline--Johnsen--Shah](https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/html/LIPIcs.ITCS.2026.75/LIPIcs.ITCS.2026.75.html).
Passages and limits are in `audit/referee-e4128dd151f7-sources.md`.
DKT does have per-instance robustness; its guarantee, not an absence
of pointwise robustness, distinguishes it here. Finite LP methods,
geometric policies, support reductions, mixing and ordinary duality
are prior ingredients.

The combined result passes as a useful, nontrivial technical note:
the normalization sweep and exact price recovery supply a constructive
certifying repair for arbitrary forecasts, and the uniform strict-dual
analysis supplies the complete objective frontier, uniqueness and a
sharp support lower family. This is more than an implementation failure
or an LP restatement. The uniform family alone would merit a much
narrower novelty assessment because of its exact one-hot overlap.
No generic-LP speedup, new canonical distribution, priority guarantee
or venue-level significance is established. The bounded primary search
found no exact duplicate of the combined construction; historical
moment/DRO duplicate clearance is not exhaustive.

## Gaps and scope limits

No unresolved mathematical gap was found in this exact frozen combined
claim. The broader arbitrary-forecast complete-frontier task remains
unresolved. Additional published-software reproduction claims or a
criticism of another source version are not accepted by this snapshot;
introducing them substantively requires a new freeze and fresh review.
No manuscript was written or released in this job. Writing and final
citation/build/visual audits remain separate phases under the user
author/template/page requirements.

The required structural `check-math` result is saved separately as
`audit/referee-e4128dd151f7-gate.json`. It checks evidence binding
and actual role provenance, not mathematical truth.
