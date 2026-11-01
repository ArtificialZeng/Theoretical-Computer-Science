# Exact mandatory excursions and the cost of preserving endpoint ranges

Research-pass-2 argument, proposed for a fresh referee; no acceptance is claimed.
The original question and its status are unchanged. The unrestricted general
reachability theorem, binary distance, and cone geometry are not claimed new.
The intended contribution is the sharp shape-constrained comparison and the
complete budget/peak frontier below. The latter extends the supplied seed to
**every** positive swapped triplet, including a swapped probability above 1/2.

## Definitions and elementary binary ingredient

Use exactly the positive finite simplex and absolutely continuous paths in
problem.md. Put C(r)=ess sup max_i |r_i'/r_i|, and let Lambda be the unrestricted
infimum. Lambda_mon also requires each coordinate to be monotone in its
endpoint direction, with equal endpoints forcing a constant coordinate.
Lambda_box instead requires min(p_i,q_i)<=r_i(t)<=max(p_i,q_i) for all i,t.
The affine curve makes both restricted classes nonempty.

If C(r)<=L, positivity and absolute continuity imply

    r_i(t)<=min(p_i exp(Lt), q_i exp(L(1-t))).                 (1)

Normalization also implies |r_i'|<=L min(r_i,1-r_i): sum the absolute
derivative bounds over all the other coordinates. Define the increasing map

    Phi(x)=log(2x)                 for 0<x<=1/2,
           -log(2(1-x))           for 1/2<=x<1.

Then |(Phi(r_i))'|<=L almost everywhere. For a binary distribution (x,1-x),
this proves its intrinsic distance is |Phi(q_1)-Phi(p_1)|; the monotone
Phi-linear path attains it. This scalar fact is standard, included to make
the new claims self-contained. No Laplace/Blackwell sufficiency is needed
anywhere in the proofs below.

## Theorem 1: all positive swapped triplets, all budgets

Let 0<a<b, a+b<1, c=1-a-b, and set

    p=(c,a,b), q=(c,b,a), eta=log(b/a),
    T*= log(b/a)                  if b<=1/2,
        log(1/[4a(1-b)])          if b>1/2,
    T0=2 log((a+b)/(2a)).

There is a path with C(r)<=L if and only if L>=T*. For every such L, the
minimum (attained) reservoir peak is

    min_{C(r)<=L} max_t r_0(t) = max{c,1-2a exp(L/2)}.       (2)

The infimum Lambda equals T*. The path with C(r)<=T* on the fixed unit
interval is unique. Its reservoir peak is 1-2sqrt(ab) if b<=1/2, and
1-sqrt(a/(1-b)) if b>1/2; in both cases it strictly exceeds c.

### Lower bounds

Coordinate 1 goes from a to b, so the binary ingredient gives L>=T*.
Equation (1) at t=1/2 gives r_1,r_2<=a exp(L/2). Thus normalization and
the endpoints give both terms on the right of (2).

For reference, T*<T0. Indeed T*=integral_a^b dx/min(x,1-x), whereas
T0=integral_a^b dx/min(x,a+b-x). The former denominator is at least the
latter, and strictly larger on the nonempty interval ((a+b)/2,b).
The latter integral equals the displayed T0 by reflection about (a+b)/2.

### Construction for T*<=L<=T0

Set B=exp(L/2), H=1-2aB. Then H>=c>0 and aB<1/2. On the first half use
physical time s=Lt, u=exp(s), 1<=u<=B. Define the fastest scalar binary
decrease from b, denoted g(u):

    if b<=1/2:  g(u)=b/u;
    if b>1/2:   kappa=1/[2(1-b)], K=1/[4(1-b)],
                g(u)=1-(1-b)u       for 1<=u<=kappa,
                     K/u           for u>=kappa.

Write h(u)=1-au-g(u). Set

    r_1=au, r_0=min{H,h(u)}, r_2=max{g(u),2aB-au}.           (3)

For b<=1/2 let K=b and u*=sqrt(K/a). For b>1/2 use the K above;
then u*=sqrt(K/a)>kappa. In either case L>=T* says B>=u*.
The function h increases from c to its unique maximum at u* and then
decreases. In the initial phase b>1/2 it is cu; in the later phase it is
1-au-K/u. Moreover h(B)>=1-2aB=H because K<=aB^2.
Consequently h>=c throughout [1,B], and {u:h(u)>=H}=[u0,B] for a first
crossing u0 (u0=1 when H=c). Formula (3) therefore consists of an initial
uncapped path followed by a constant-reservoir segment. Its coordinates are
strictly positive and sum to one; at B they are (H,aB,aB).

Check speed in s, whose budget is 1. In the initial binary phase,

    (r_0,r_1,r_2)=(cu,au,1-(1-b)u),

the first two derivatives equal their coordinates, and |r_2'|=1-r_2<=r_2
because r_2>=1/2. In a later uncapped phase, r_1'=r_1, r_2'=-r_2,
r_0'=r_2-r_1. Here r_1<=aB<1/2 and r_2<=1/2, so

    r_0+r_0'=1-2r_1>=0, r_0-r_0'=1-2r_2>=0.

In the capped phase, r_0'=0 and r_2'=-r_1. Since r_2=2aB-au>=au=r_1,
all speed bounds again hold. The formulas agree at both possible joins;
there are finitely many smooth pieces, hence absolute continuity.
On the second half reflect time and swap coordinates 1 and 2. The midpoint
is fixed by this operation. This gives the required endpoints and a
positive normalized path with C(r)<=L and peak exactly H.

At L=T0, H=c, so (3) is the constant-reservoir binary geodesic throughout.
For L>T0 reuse that unit-interval path, whose budget is T0<=L. Its peak c
attains the lower bound. This completes existence and (2) for all budgets.

### Uniqueness at the minimum budget

At L=T*, Phi(r_1(1))-Phi(r_1(0))=T* while |(Phi(r_1))'|<=T*.
The nonnegative deficit has integral zero; hence (Phi(r_1))'=T* almost
everywhere. Thus r_1(t)=Phi^{-1}(Phi(a)+T*t). Similarly
r_2(t)=Phi^{-1}(Phi(b)-T*t). Normalization forces r_0. The attaining
construction just proved shows this forced path is admissible. In particular,
the claim is uniqueness within the normalized simplex at this budget;
it is not an ambient-cone uniqueness assertion.
Its midpoint has r_1=r_2=a exp(T*/2), and (2) yields the stated peak.
Since T*<T0, this peak is strictly greater than c.

### Supplied family as a corollary

For E>1 and 0<a<=1/(2E), take b=aE. Then b<=1/2 and T*=eta=log E;
(2) is exactly A1. At the minimum budget the excess peak is
a(sqrt(E)-1)^2. Taking a=1/(2E) makes that excess approach 1/2 as E grows.
This is a limit within this family, not a universal extremum claim.

## Theorem 2: sharp price of monotonicity and endpoint-range preservation

For each eta>0 put E=exp(eta), B_eta=2log((E+1)/2). For n>=3,

    sup_{d_DP(p,q)=eta} Lambda_mon(p,q)/Lambda(p,q)
      = sup_{d_DP(p,q)=eta} Lambda_box(p,q)/Lambda(p,q)
      = B_eta/eta.                                           (4)

Each supremum is attained by positive endpoints in every n>=3. For n=2
both ratios are always 1. The right side of (4) tends to 2 as eta tends to
infinity; this concerns a shape restriction, not the known unrestricted
endpoint-distance overhead.

### Upper bound

For the affine path l_i(t)=p_i+t(q_i-p_i), its continuous positive speed
when p!=q is D(t)=max_i |q_i-p_i|/l_i(t). If rho=q_i/p_i>=1 then its term
is (rho-1)/(1+t(rho-1)), increasing in rho, hence at most
f(t)=(E-1)/(1+t(E-1)). If rho<=1, put k=1-rho<=1-E^{-1}; its term
k/(1-tk) increases with k, hence at most g(t)=(1-E^{-1})/(1-t(1-E^{-1})).
The envelopes cross at 1/2; f is larger on the first half. Therefore

    length(l)=integral_0^1 D(t)dt
       <= integral_0^(1/2) f(t)dt + integral_(1/2)^1 g(t)dt
       =2log((E+1)/2)=B_eta.

Let s(t)=integral_0^t D/length(l). Its positive derivative is continuous
and bounded away from zero, so its inverse is continuously differentiable.
Reparameterization by s gives cost exactly length(l), remains coordinate
monotone and inside the endpoint box. Since Lambda>=eta, both ratios in
(4) are at most B_eta/eta. The inequality Lambda_box<=Lambda_mon is also
immediate from inclusion of path classes.

### Attainment and dimension threshold

Choose any 0<a<=1/(2E), b=aE, c=1-a-b. Theorem 1 gives Lambda=eta.
Either restricted class forces the equal-endpoint reservoir to be constant c.
Thus the other two coordinates have total m=a+b; dividing by m preserves
their log derivatives. Their binary endpoints are (1/(E+1),E/(E+1))
and its swap. The binary ingredient gives restricted optimum B_eta, attained
by the monotone binary geodesic. For n>3 split c into n-2 positive masses:
an unrestricted construction splits r_0 in those fixed proportions, preserving
log speeds; each restricted path fixes every such coordinate. Equality remains.
For n=2 the binary optimal path is monotone and within endpoint ranges, proving
ratio 1. There are no positive-distance pairs when n=1.

## Theorem 3: exact general endpoint-envelope excursion certificates

Let n>=2, p,q be positive probabilities and Z=exp(L)>=
max_i{p_i/q_i,q_i/p_i}. For a designated coordinate j define

    S_j(z)=sum_{i!=j} min(p_i z,Z q_i/z),  1<=z<=Z,
    C_j=1-min_{1<=z<=Z} S_j(z).                            (5)

Every path with budget <=L has max_t r_j(t)>=C_j>=max(p_j,q_j).
If Z fails the endpoint condition, the endpoints certify infeasibility.
Equation (5) is a necessary certificate, not an asserted sufficient cap test
or a decision procedure for general path feasibility.

For rational p,q,Z one certificate is computable using O(n log n) rational
arithmetic operations and comparisons, followed by one square root. All n
certificates require O(n^2+n log n) such operations and at most n square
roots, reusing a common likelihood-ratio sort. These are arithmetic, not
bit-complexity bounds. The certificate equals the true minimum peak for the
whole swapped-triplet family of Theorem 1 at every feasible budget.

### Proof and sweep

Equation (1) and normalization give r_j(t)>=1-S_j(exp(Lt)); taking a
maximum proves the certificate. At z=1 every min selects p_i, and at z=Z
every min selects q_i, proving the endpoint inclusion.

Set v=z^2. Coordinate i changes branch at v_i=Zq_i/p_i, which belongs to
[1,Z^2]. Sort the ratios q_i/p_i and group ties. Between adjacent event
values S_j(z)=A z+B/z for nonnegative rational A,B; initially A=1-p_j,
B=0. At an event transfer each i!=j from A to B by A-=p_i, B+=Zq_i.
Tied events are transferred as a group. For a closed v-interval [l,h],
the minimum squared value is the minimum of

    (A l+B)^2/l, (A h+B)^2/h,
    4AB if A,B>0 and l<=B/A<=h.

Indeed differentiation in z gives its only interior critical point z^2=B/A;
if A or B is zero the function is monotone. Squaring preserves minimizers
because S_j>=0. Taking the rational minimum R over all intervals therefore
gives C_j=1-sqrt(R). This proves exactness of the evaluation algorithm.
There are O(n) grouped intervals, and O(1) updates per event. For all j
reuse the sorted order, allowing the harmless breakpoint of j itself and
skipping its transfer; each scan still has O(n) work, giving the bound.

For p=(c,a,b), q=(c,b,a), the two changing-coordinate events are Z a/b
and Z b/a. Z>=exp(T*)>=b/a places both inside [1,Z^2]. The first cell
has S=a(1+b/a)z, the middle S=az+Za/z, and the last S=Z(a+b)/z.
The middle stationary point z=sqrt(Z) lies in its cell because Z>=b/a.
Thus min S=min{a+b,2a sqrt(Z)} and C_0 is exactly (2). Attainment is supplied
by Theorem 1, not by the endpoint-envelope argument alone.

## Dependencies, failure routes and scope limits

Dependencies: elementary AC chain rule, the scalar comparison / Phi integral,
affine arc-length reparameterization, and a sorted rational sweep. Prior
Laplace/Blackwell reachability and generic polymatroid decomposition are
background and are not needed to establish these theorems.

The original transform-family comparison is not settled in full. Scalar
transform-linear interpolation before normalization stays between endpoint
values; normalizing it may leave those ranges. Consequently Theorem 2 does
not automatically apply to normalized geometric or arbitrary normalized
transform-linear schemes. The inspected 2026 papers account for normalization;
these theorems do not refute their stated guarantees. No O(n^2) improvement
for decomposing general optimal paths has been established in this pass.

Known analytic gap list for the exact stated theorems: empty as assessed by
this researcher. Fresh mathematical and novelty/value review remains required.
The certificate algorithm is a straightforward envelope evaluation and is
supporting machinery, not a claimed new general optimization technique.
Finite checks and independently written consumers are described in their JSON
artifacts; they are not independent model-context refereeing.
