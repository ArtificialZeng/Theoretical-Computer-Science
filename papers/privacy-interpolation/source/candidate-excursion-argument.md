# New unaccepted subsidiary target: mandatory probability excursions

The previous value/reachability target was correctly parked as known
Laplace--Blackwell theory. Do NOT reopen to relabel that theorem, sorted ROC,
or generic polymatroid decomposition. The following is a NEW proposed
shape-constrained target, with a full budget/excursion frontier, not merely the
old single affine obstruction. Preserve source.md and original_status=unresolved
if only these subsidiary claims qualify. Novelty and standalone value still
require independent research and a fresh referee.

Let Lip(r)=ess sup_t max_i |d log r_i(t)/dt| on the unit interval, as in
the original question. The unrestricted optimum Lambda is known in abstract
form. Define Lambda_mon by also requiring every coordinate monotone in its
endpoint direction (equal endpoints force that coordinate constant).

## A. Exact three-output budget versus excursion frontier

Take E>1 and 0<a<=1/(2E). Put c=1-a(1+E)>0 and

    p=(c,a,aE), q=(c,aE,a), eta=log E,
    B_eta=2 log((E+1)/2).

For L>=eta, minimize max_t r_0(t) over ALL positive normalized AC paths
from p to q with Lip(r)<=L, with no coordinate-monotonicity restriction.
Proposed exact answer:

    P_min(L)=max{c, 1-2a exp(L/2)}.                  (A1)

For L<eta there is no feasible path. For eta<=L<=B_eta, write
B=exp(L/2) and x=B-sqrt(B^2-E), so 1<=x<=sqrt(E),
t0=log(x)/L in[0,1/2]. Put H=1-2aB. On the first half define:

  0<=t<=t0:
    r_2=a exp(Lt), r_3=aE exp(-Lt), r_0=1-r_2-r_3;
  t0<=t<=1/2:
    r_2=a exp(Lt), r_3=2aB-a exp(Lt), r_0=H.

On the second half reflect time and swap coordinates2,3; r_0 is reflected.
Indices here label the reservoir as0 and the two changing coordinates as2,3
only for consistency with the formulas; choose clean1,2,3 labels in the paper.
At the join x+E/x=2B gives continuity. At the midpoint both changing
coordinates equal aB. Endpoints are p,q and every coordinate is positive.

Scaled derivatives on the first piece are a exp(Lt), -aE exp(-Lt), and
a(E exp(-Lt)-exp(Lt)). Its reservoir speed bound is equivalent to
2aE exp(-Lt)<=1, valid by2aE<=1. On the flat piece the only nontrivial
speed bound is a exp(Lt)<=2aB-a exp(Lt), valid up to t=1/2.
Reflection preserves all bounds. Thus this is a genuine path with budget L,
and maximum reservoir mass H. At L=B_eta, t0=0 and H=c. For L>B_eta reuse
that constant-reservoir path, whose actual budget is B_eta<=L.

The lower bound is elementary but global: at t=1/2, the forward endpoint
bound gives r_2<=a exp(L/2), and the backward endpoint bound on coordinate3
gives r_3<=a exp(L/2). Normalization forces r_0>=1-2a exp(L/2); endpoints
also force the peak>=c. This proves(A1) for ALL paths, not just a chosen
parametric family. The endpoint coordinate ratio forces L>=eta.

At L=eta, the two changing log-probabilities attain their endpoint change
at the maximum allowed speed, so their trajectories are forced a.e.:
r_2=a E^t and r_3=a E^(1-t). Normalization fixes the third coordinate.
Hence the fastest parameterized path is UNIQUE and its reservoir peak is
1-2a sqrt(E)>c. The unavoidable excursion is a(sqrt(E)-1)^2. With
a=1/(2E), this approaches1/2 as E->infinity. Do not claim this is a
universal maximum excursion over all endpoint pairs.

## B. Sharp dimension threshold for coordinate-monotone interpolation

For arbitrary positive endpoints with d_DP(p,q)=eta>0 and E=exp(eta),
the affine path has density

    D(t)=max_i |q_i-p_i|/((1-t)p_i+t q_i)
       <=max{(E-1)/(1+(E-1)t),
               (1-E^(-1))/(1-(1-E^(-1))t)}.

The two envelopes switch at t=1/2. Their integral is B_eta. Arc-length
reparameterization of the affine curve is coordinate-monotone with budget
at most B_eta. Since Lambda>=eta,

    Lambda_mon/Lambda <= B_eta/eta.                 (B1)

For the endpoints in(A), unrestricted Lambda=eta by the explicit fastest
path. Coordinate-monotonicity forces the reservoir constant c. The remaining
two coordinates have fixed total a(E+1), with normalized endpoints
(1/(E+1), E/(E+1)) swapped. The classical binary speed bound integrates
to2log((E+1)/2)=B_eta and is attained by its monotone binary geodesic.
Thus(B1) is an equality for EVERY eta>0 in dimension3. Split c into any
number of positive fixed-proportion coordinates for the same equality in
every dimension n>=3. In dimension2, the binary optimal path is already
coordinate-monotone, so the ratio is always1. The sharp n>=3 worst ratio
tends to2 as eta->infinity. Attribute the binary distance and any previously
known affine calculation; the new claim is the shape restriction/excursion
frontier, not the old unrestricted Laplace reachability theorem.

## C. General exact lower certificates for excursions

Given positive p,q, budget L, Z=exp(L)>=1, every feasible path satisfies

    r_i(t)<=min{p_i exp(Lt),q_i exp(L(1-t))}.

For any designated output j, its maximum probability is therefore at least

    C_j=1-min_{1<=z<=Z} sum_{i!=j} min(p_i*z,Z*q_i/z). (C1)

This includes its two endpoint masses if Z>=max_i{p_i/q_i,q_i/p_i}; otherwise
the endpoints themselves already certify infeasibility at budget L.
Do NOT claim(C1) sufficient or sharp for arbitrary endpoints. It is exact
for the family(A), so it gives a sharp computable lower-certificate method.

For rational p,q,Z the certificate can be computed exactly in O(n log n)
rational operations/comparisons plus one square root. Sort breakpoints
v_i=Z*q_i/p_i (squared z-coordinates), all in[1,Z^2]. On each interval the
sum is A*z+B/z, where A is the sum of p_i still on their forward branch and
B=Z times the sum of q_i on their backward branch. Maintain these sums in
one sweep. On a closed squared interval[v_left,v_right], candidates for the
SQUARED minimum are

    (A*v+B)^2/v at either endpoint v;
    4*A*B if A,B>0 and B/A lies in the squared interval.

Thus the result is1-sqrt(R) for a rational minimum R. No transcendental
optimization or sampled-time guarantee is needed. Group tied breakpoints.
One common ratio sort also gives all n designated-coordinate certificates
in O(n^2) arithmetic time using shared prefix sums; prove this if retained.

## Novelty/value and next tests

Search mandatory excursions, shape-preserving or coordinate-monotone DP
interpolation, controlled probability paths, and closest normalization/
transform-linear papers. A current broad primary-source search found no
equivalent statement, but that is not priority evidence. The previous single
obstruction was explicitly judged insufficient. Assess whether(A)'s complete
all-budget frontier, (B)'s sharp shape penalty and(C)'s exact certificate
constitute a substantive NEW result; park again if they merely rephrase a
known theorem or are too slight for an honest standalone result-note.

Independent tests: rationalize the switching point by choosing rational
1<=x<=sqrt(E) and B=(x+E/x)/2, so Z=B^2 is rational. Verify joins,
normalization, derivative-bound endpoint identities, and(C1)'s equality
exactly. Separately compare the sweep with exhaustive branch enumeration
for small rational endpoint vectors. Analytic proofs support continuous
times/all parameters. No manuscript before a new accepted frozen claim.
