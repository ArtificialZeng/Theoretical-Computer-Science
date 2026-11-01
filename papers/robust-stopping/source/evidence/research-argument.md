# Proposed repair: an exact prefix oracle and one moment price

Job `robust-stopping-research-a43d444f406e`, research pass 1. This is a
candidate argument for a future fresh referee, not mathematical acceptance.
The original source is unchanged. Read `requirements.md` and `problem.md`.
The parent seed `candidate-argument.md` was inspected as an unaccepted seed;
the backward elimination below agrees with its first step. The normalization
activation sweep and explicit exact one-price recovery below are the new
steps investigated in this pass. No manuscript is prepared.

## Proposed theorem and exact scope

For integer b>=2, rational finitely supported forecast p on positive integer
horizons, and rational R>=rho_b, the algorithm in `prefix_oracle.py` returns
an expected-cost minimizing R-robust policy and rational nonnegative prices
lambda,y_1,...,y_{b-1}, together with a rational alpha, satisfying

    g(t)+lambda*(t-1)+sum_{x=t}^{b-1}(b+t-1-x)*y_x >= alpha     (all t>=1),
    J_p(f)=alpha-(R-1)*sum_{x=1}^{b-1}x*y_x-lambda*(R-1)*b.

An empty sum is zero. These inequalities certify global optimality on the
original unbounded domain. The returned support lies in

    S={1,...,b} union {d+1:p_d>0, d>=b},

and uses at most two days >=b. The algorithm uses no generic LP solver.
After computing g on S, it makes O(log Z) calls to an explicit linear
optimization oracle, each taking O(b^2+|S|) rational arithmetic operations.
Z is defined below; log Z is polynomial in b and the binary input length.
All intermediate rational numbers have polynomial bit length. Thus this is
an exact algorithm polynomial in the numerical value b and input bit length,
not a polynomial-in-log(b) or strongly polynomial claim.

This is a proposed general repaired optimizer, coupled with the exact
support-threshold separation in `triage-findings.md`. Baseline support
reduction, LP duality, rational isolation and convexity of value functions
are standard ingredients, not separate novelty claims. The broad original
research task remains marked unresolved: no full Pareto-frontier enumeration
or optimal dependence on binary-encoded b is claimed. A fresh referee must
assess correctness, overlap and whether this repair is a substantive result.

## 1. Baseline robustness and finite reduction

Set a=b-1, r=R-1 and K=rb. The cost at actual horizon x is

    E C_T(x)=x+sum_{t<=x}(t-1)f_t+(b-x)*sum_{t<=x}f_t.

It is nondecreasing in x for each fixed t, and tends to b+t-1. Monotone
convergence therefore gives the necessary moment bound E[T-1]<=K. The
b-1 constraints at x<b are

    sum_{t<=x}(a+t-x)f_t <= r*x.                           (1)

Conversely these constraints and the moment bound imply every original
robustness inequality: (1) covers x<b, and for x>=b the expected cost is at
most its limit b+E[T-1]<=Rb. This is Kim--Fan Lemma 5.1, not a new lemma.

For t>=b, let s be the largest element of {b} union
{d+1:p_d>0,d>=b} not exceeding t. There is no positive forecast atom in
[s,t-1]. Consequently g(t)-g(s)=(t-s)*Pr[D>=t]>=0. Moving mass from t to s
reduces its moment, does not change (1), and does not increase its objective.
This also proves dominance for g(t)+lambda*(t-1) whenever lambda>=0. The
finite robust polytope on S is compact and nonempty. For nonemptiness, the
classical policy

    f_t=b^(t-1)*(b-1)^(b-t)/(b^b-(b-1)^b), 1<=t<=b,

sums to one, satisfies (1) at R=rho_b with equality, and has moment
b*(rho_b-1); hence it is feasible at every larger R. Direct summation or the
recurrence below verifies these identities. Thus a finite-support optimum
exists. The omitted unbounded buy-days will also be covered by dual dominance.

Let Q be the probability simplex on S intersected with (1), with its moment
bound omitted. This finite polytope is the domain of the linear oracle.

## 2. Triangular prefix schedules

Temporarily omit normalization too. Define P={z>=0: (1) holds on [a]}.
For a feasible prefix through i-1, its next feasible interval is exactly

    0 <= z_i <= U_i=(r*i-sum_{j<i}(a+j-i)*z_j)/a.            (2)

For i=1 the numerator is r>0. For i>1 the preceding constraint implies the
numerator is at least r+sum_{j<i}z_j>0. Future coordinates can always be zero:
when a positive prefix has been fixed, increasing the constraint horizon
reduces the old left side and increases its right side. Hence elimination
of the last coordinate never introduces a hidden earlier restriction.

For any linear cost w*z, eliminate coordinates i=a,...,1. A nonnegative
current coefficient selects z_i=0; a negative coefficient selects U_i and
updates every earlier coefficient by -w_i*(a+j-i)/a. Induction on i proves
exact minimization over P. Equivalently, for any alpha and prefix costs c_i,
compute backward

    y_i=max(0,(alpha-c_i-sum_{j>i}(a+i-j)*y_j)/a).           (3)

This is a dual certificate for min_{z in P} sum_i(c_i-alpha)z_i:
its value is -r*sum_i i*y_i. Choose upper endpoints precisely where y_i>0;
zero endpoints where the reduced cost is positive; either choice at ties.
Forward reconstruction is feasible by (2), and complementary slackness
checks equality, proving the claim without assuming a general greedy theorem.

For B={s_1<...<s_k} subset [a], write v(B) for the prefix schedule with
positive coordinates at B and (1) tight there. Set s_0=0, F_0=0. Subtracting
successive tight constraints yields

    v(B)_{s_j}=(s_j-s_{j-1})*(r+F_{j-1})/a,
    F_j=r*(product_{l=1}^j(1+(s_l-s_{l-1})/a)-1).          (4)

The consecutive geometric update and gap recurrence in (4) already appear
in Kim--Fan Appendix D.3--D.4, equations (30)--(31). The product expression
is their iteration; it is not claimed new. The repair below determines the
active days by dual-adjusted slacks, rather than the raw support threshold.

These schedules need not have total mass <=1 and are not probability
policies. Every v(B) is feasible in P; between consecutive elements of B,
the left side of (1) decreases while the bound increases. Inserting a day
into B strictly increases its total mass: splitting a gap Delta into two
positive gaps u,v replaces 1+Delta/a by
(1+u/a)(1+v/a)=1+Delta/a+uv/a^2; appending a last day adds a factor >1.

## 3. Normalization by a finite activation sweep

Take arbitrary rational costs c_t on S, not necessarily forecast-shaped.
Let c_tail=min_{t>=b,t in S}c_t, choosing any minimizing day t_tail.
For alpha<=c_tail, equation (3) gives a feasible dual of optimization on Q:

    h(alpha)=alpha-r*sum_i i*y_i.                          (5)

For a fixed active set B, the y_i are affine in alpha and vanish off B.
Let h_i=dy_i/dalpha for i in B. Backward differentiation gives

    a*h_i+sum_{j>i,j in B}(a+i-j)*h_j=1.                   (6)

All h_i are positive. To see this without a sign assumption on an inverse,
let k be the next element of B after i. If there is no such k the relevant
reduced-cost speed is 1. Otherwise, writing H_k=sum_{j>=k,j in B}h_j,
the equation at k gives

    1-sum_{j>i,j in B}(a+i-j)*h_j=(k-i)*H_k>0.             (7)

Backward induction proves positivity. For an inactive i the reduced slack
c_i-alpha+sum_{j>i}(a+i-j)y_j therefore has strictly negative derivative.
Existing positive y_i increase with alpha, so no day ever deactivates.
Every day activates at most once. Simultaneous activations are allowed.

Start at alpha=min(c_tail,min_{i<b}c_i), B empty. At the current alpha add
all zero reduced slacks to B and recompute (3). Let m(B)=sum v(B). If m(B)<1
and alpha<c_tail, move to the earliest remaining slack root or c_tail,
whichever comes first. The roots are obtained exactly from their current
slack divided by the positive speed (7).

If c_tail is reached with m(B)<1, return v(B) plus tail mass 1-m(B) at
t_tail. If an activation changes the mass from m_-<1 to m_+>=1, return

    z=(1-theta)*v(B_-)+theta*v(B_+),
    theta=(1-m_-)/(m_+-m_-),                              (8)

and no tail mass. Although either raw schedule may have mass above one,
(8) has mass exactly one and is prefix feasible by convexity. Both schedules
minimize the raw prefix problem at this activation alpha: new y_i are zero,
and all positive older y_i correspond to tight constraints in both. Thus
(8) and the tail case attain (5), proving optimality over Q. The equality
case m(B)=1 is included in (8). A tail cap tied with an activation is also
covered. Empty B, negative costs, multiple equal costs and R>=b require no
separate generic-position assumption.

There are at most a activation events. For any fixed B, (3), (6) and all
slacks can be computed in O(a) operations using suffix sums of y_i,i*y_i,
h_i,i*h_i. Equation (4) is another O(a) pass. Selecting the next event scans
at most a days. Thus the complete oracle costs O(b^2+|S|) rational operations.
Its output is a feasible normalized policy and an exact dual, with at most
one tail day. `linear_oracle` implements this sweep explicitly.

## 4. Exact recovery of the tail-moment price

For lambda>=0 apply the preceding oracle to

    c_t=g(t)+lambda*(t-1),
    q(lambda)=min_{f in Q}(J_p(f)+lambda*mu(f)).            (9)

The returned policy need not be a vertex in a tied face. If the output at
lambda=0 has moment <=K, it already solves the robust problem. Otherwise
we find two oracle outputs on opposite sides of K and isolate their common
price exactly. The following deliberately generous bound avoids a real
arithmetic or limiting-precision claim.

Let q_R be the denominator of R and q_p the lcm of forecast probability
denominators. Define

    D=b!*b^b, H=q_p*q_R*D, L=b+max(S), Z=2*L*H^4.          (10)

Every vertex of Q has at most b positive coordinates. Select normalization
and independent tight prefix rows to solve for them; the integer matrix has
entries of magnitude <=b and determinant of magnitude <=D. Cramer's rule
shows that its coordinates have a common denominator q_R*|det|. Consequently
both its moment and objective have denominators <=H and values between
0 and L. Every intersection of two distinct lines J+lambda*mu with different
moments therefore has numerator and denominator of magnitude <=Z after
reduction: differences have numerator <=2LH^2 and denominator <=H^2,
and taking their quotient gives the bound 2LH^4. Distinct intersections in
[0,infinity), including zero, are separated by at least 1/Z^2.

The reference implementation first makes at most eight optional exact chord
probes. At a bracket with endpoint policies f_-,f_+, take their line
intersection lambda and call the oracle there. If its value equals their
common value, both endpoints optimize there, so (11) and the returned dual
certify the answer immediately. An oracle policy of moment K likewise
certifies the answer immediately. Otherwise its moment updates the bracket
exactly as in bisection. The intersection lies in the bracket by endpoint
optimality, and a strict value improvement cannot occur at an unchanged
endpoint. These eight probes affect neither the proof nor its asymptotic
bound; setting max_chord_probes=0 exercises the pure bisection algorithm.

All positive intersections are <=Z. At lambda_hi=Z+1, every minimizing
vertex of (9) has minimum possible moment, as does any convex combination
of such vertices. That moment is <=K by robust feasibility. Starting with
lambda_lo=0 and the already found moment >K, bisect [lo,hi]. If the new
policy has moment >K replace the left endpoint and its policy; otherwise
replace the right endpoint and its policy. Monotonicity follows by adding
the two oracle optimality inequalities at different prices.

After at most ceil(log2((Z+1)Z^2))+1 iterations the interval has width
strictly below 1/Z^2, so contains at most one distinct line-intersection
price. It must contain a breakpoint kappa at which both endpoint policies
minimize (9). Indeed q is the lower envelope of finitely many vertex lines.
If there were no breakpoint in the closed interval, all optimizers there
would have the same moment; this contradicts the strict moment bracket.
On either side of the sole breakpoint all minimizing vertex lines have the
same (moment,objective) pair. If an endpoint itself is that breakpoint,
its possibly nonvertex output is already optimal there. Continuity proves
the assertion for both endpoints in all cases.

Writing f_- and f_+ for the stored policies, recover the exact price and
policy by

    kappa=(J(f_+)-J(f_-))/(mu(f_-)-mu(f_+)),
    theta=(K-mu(f_+))/(mu(f_-)-mu(f_+)),
    f=theta*f_-+(1-theta)*f_+.                             (11)

Their moments satisfy mu(f_-)>K>=mu(f_+), so denominators are nonzero and
0<=theta<1. Both policies optimize (9) at kappa and hence so does f, while
mu(f)=K. Recompute the oracle's dual at kappa. Subtracting kappa*K from
its value proves the primal/dual equality in the theorem. A breakpoint at
zero is allowed. The case mu(f_+)=K simply returns f_+.

Each endpoint oracle uses at most one tail day. Their mixture therefore has
at most two tail days and at most b+1 buy-days in all. This is a constructive
support bound, not a claim that either raw prefix schedule is a policy.

## 5. Bit complexity and certificate meaning

Let ell denote the total binary encoding length of R and a sparse list of
forecast atoms (horizon,probability), together with b. Then
log H=O(ell+b log b), log L=O(ell+log b), and log Z=O(ell+b log b).
Computing costs on S by prefix probability/moment sums after sorting takes
O(|S|+|supp p| log |supp p|) arithmetic operations; the simple reference
implementation instead directly sums each cost and still runs in polynomial
time. Excluding this preprocessing, the algorithm takes

    O((b^2+|S|)*(ell+b log b))

rational operations. No such bound is asserted for the exhaustive test code.
For polynomial bit complexity, equations (3) and (6) on any fixed active set
have triangular diagonal a and depth <=a. Their affine coefficients have
bit length polynomial in b and the current cost bit length. Each activation
price is a root of one such affine slack; its rational bit length is
polynomial as well, regardless of how previous roots were represented.
The canonical schedules (4) have common denominator q_R*a^a and numerator
of polynomial bit length, and (8) only takes ratios of their mass differences.
Bisection uses O(log Z) bits of denominator. Equation (11), the final price
and its recomputed dual likewise involve only polynomial-length rationals.
Standard exact rational arithmetic therefore yields polynomial bit time in
b and ell. This argument bounds intermediate values, not just the output.

Finally the displayed dual inequality gives, for every robust law on all
positive integers, J>=alpha-r*sum x*y_x-lambda*K by expectation. There is
no unjustified interchange of signed infinite sums: g is bounded, finite
moment follows from robustness, and the prefix contribution has finite
support. Checking it on S suffices by the tail dominance in Section 1.
This explains precisely how the finite certificate binds the infinite task.

## 6. Standard frontier facts and remaining scope

For fixed p, V_p(R) is nonincreasing, convex and piecewise affine with
rational breakpoints on [rho_b,infinity). Finite support reduction makes
this a finite parametric LP; its dual expresses V as the supremum of affine
functions of R with nonpositive slopes. Finiteness of the polyhedral value
function gives piecewise affinity. It eventually equals min_t g(t): any
minimizing finite deterministic day t is feasible for
R>=(b+t-1)/min(t,b). These are standard consequences, included for context.
They do not provide an output-sensitive algorithm enumerating every
frontier segment, and no bound on its number of segments is claimed here.

Known mathematical gaps in the stated optimizer argument: none identified
by its proposer after the exact tests, subject to fresh mathematical review.
Priority/substantive-value status remains uncertain. Test coverage and the
independent arithmetic check are recorded separately; neither is peer review.
