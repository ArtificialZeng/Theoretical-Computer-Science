# Bounded-bit conservative clock compiler

Job c042-strongrsp-research-a3a11d57c4b5. Mathematical proof record, for review;
not independent acceptance, a manuscript or a venue assessment. The original
is exactly source.md. This record supplies the probability construction missing
from the two earlier passes. No exponential is evaluated by the compiler.

## Uniform construction and error proof

Let q>=2 be an integer, U=4q, 0<mu<=U dyadic, h=2^-b, and H=2U+b+2.
Find k0=floor(mu) by bounded binary comparisons on integers 0,...,U. Define
the analytic relative Poisson weights r(k)=Pr[Pois(mu)=k]/Pr[Pois(mu)=k0].
They satisfy r(k0)=1, r(k-1)=r(k)k/mu below the mode, and
r(k+1)=r(k)mu/(k+1) above it. Every multiplier moving away from k0 is <=1,
so all r(k)<=1. Compute w(k0)=1 by these recurrences through 0,...,H,
rounding DOWN to h after every operation. Then

    0 <= r(k)-w(k) <= Hh.

Indeed each recurrence adds at most h to the preceding error. For k>=2U
every upward multiplier is <=1/2. Consequently the tail after H is <=h
(in fact <=h/4). With S=sum_{k>=0}r(k)>=1, set

    Sminus=sum_{k=0}^H w(k), E=((H+1)^2+1)h, Splus=Sminus+E.

Then Sminus<=S<=Splus. For j<q put

    L_j=floor_h( sum_{k<=j}w(k) / Splus ), tau=2E+h.

The numerator deficit is <=(H+1)Hh, and replacing S by Splus contributes
at most E because S>=1. Final rounding contributes at most h. Therefore

    0 <= F_mu(j)-L_j <= tau,  0<=L_0<=...<=L_(q-1)<=1.       (1)

For mu=0 use the exact CDF identically one. On an increasing list of means,
replace L_j(mu_a) by min_{d<=a} L_j(mu_d). This preserves coordinatewise
CDF monotonicity and (1): every earlier true CDF is >=F_mu_a, whereas the
current candidate is present in the minimum. The result is decreasing in
mean. CDF differences give a nonnegative dyadic probability vector on
0,...,q with total mass exactly one; q means overflow. This law dominates
the true truncated Poisson law. Its total variation distance from it is
<=q*tau: write d_j=F_mu(j)-L_j and telescope the PMF differences, including
the last overflow difference. Two independent clocks have row variation
<=2q*tau by coupling the two coordinates.

In particular, for 0<z<1,

    sum_{k<q} p_proxy(k) z^k <= exp((z-1)mu).                 (2)

Use the decreasing function z^k for k<q and zero for k>=q. The missing
overflow contribution is essential; applying the untruncated PGF directly
to the law capped at q would have the wrong justification.

## Finite arithmetic and precision

Let r=1+ceil(log2(n+2))+ceil(log2(q+2)) and choose b=64r. Integer logarithms
here mean charged bounded doubling, never a logarithm of an input weight.
Since n,q<=2^r, H+1<=75*2^r<=2^(r+7). Thus

    tau <= 2^(2r+16-b) <= 1/[2^20 N q], N=(2q+1)(n+1).

For the last inequality use Nq<=2^(3r+3) and 59r>=39. All these precision
choices are independent of resource magnitudes and input precision.

Rounding on [0,1] is a binary search for a bounded integer index in
[0,2^b], with b+O(1) comparisons. A temporary recurrence numerator or
denominator has O(b+bits(mu)+log(H+2)) bits. Summing H+1 dyadics adds only
O(log(H+2)) bits. Normalization involves one ratio of such bounded integers,
then immediately rounds it; the long unrounded relative weights are never
stored by the algorithm. Per mean the work is O((H+q)(b+log(H+2))) plus
bounded mode search. Probability storage is O(q) per mean. Reference weights
in the checker are validation objects, not the production encoding bound.

## Upward mean grid and events

Let eta=epsilon/1000, q the first power of two >=2^20 eta^-2, and delta a
dyadic in (eta/(200n),eta/(100n)]. Choose h_mu dyadic <=eta*delta/100.
Start at delta; repeatedly append ceil_h_mu((1+eta/4)mu), except clip the
last point to U. Clip BEFORE invoking bounded rounding when the unrounded
next point exceeds U. All nonfinal ratios are in [1+eta/4,1+eta/2]; the
final ratio is no larger than 1+eta/2. There are

    J=O(eta^-1 log(nq/eta))

points. Zero stays zero, a positive raw mean below delta rounds to delta,
and all others round to the smallest grid point above them; above U they
are blocked (certain failure). For unblocked values,

    raw <= rounded <= (1+eta/2)raw+delta.                    (3)

Each grid value and every rounded intermediate has O(log(nq/eta)) bits.
Grid construction uses bounded-index comparisons and charged rounding.

For length ell>0 and rate factor q/((1+4eta)L), the changes occur exactly at
L=q*ell/((1+4eta)mu_j); the AT-threshold state uses mu_j. The mean is
constant between successive events, decreasing with increasing L. A zero
length has no events. Equal events are merged, with all simultaneous changes
applied. Thus the compiled two-clock laws meet the stochastic monotonicity
contract of research-pass2-offline.md. Per-edge sorted event indices support
snapshots in O(log(J+2)) operations, without rescanning the event set.

For a simple positive-length optimum Lstar in a retained graph, its largest
edge a lies in [Lstar/n,Lstar]. The raw mean for this edge at Lstar is
strictly inside [delta,U]. Choose the largest grid point <= that mean. Its
event L satisfies Lstar<=L<=(1+eta/2)Lstar. This supplies an event with the
right direction even when replacing parallel edges has greatly shortened
the original optimum; using original OPT/n for a representative edge would
be invalid.

For a fixed path of <=n edges, ideal independent Poisson clocks at the
rounded means can be coupled to these compiled laws with mismatch probability
<=2nq*tau<=2^-19. No assertion about all-policy absorption is required for
this completeness calculation. Alternatively the finite-rank optimal-policy
comparison from the intake note gives a value error <=2Nq*tau, since its
combinatorial rank is retained when the increment law changes.

## Exact checks and observed implementation correction

check_compiled_poisson.py is a new checker using actual binary-comparison
rounding in the compiler. compiled-poisson-results.json records 43 positive
tables plus four exact zero tables, 333 certified CDF coordinates, 274036
bounded rounding comparisons, 2360 mean-rounding checks and eight event
coverage witnesses including aspect scales 2^-200 and 2^200. The reference
uses exact finite relative weights and a rational geometric tail enclosure.
This is finite supporting evidence for the proof, not exhaustive validation.

The first checker run failed its bounded-rounding domain assertion when
the geometric update exceeded U+1. This was an implementation guard error,
not a Poisson counterexample. The final grid now clips raw>=U before rounding;
the complete test then passed. No original theorem follows from a diagnostic
failure, and no pass counter was reset.
