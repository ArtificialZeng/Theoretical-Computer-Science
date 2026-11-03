# Full-scope constructive claim submitted for critical review

Job c042-strongrsp-research-a3a11d57c4b5. This is a research proof dossier,
not a manuscript, mathematical acceptance, independent audit or STOC assessment.
The claimed theorem is the ENTIRE assertion in immutable source.md, with its
precise reading in problem.md. The proposed resolution is positive. This proof
uses the static and rounded offline lemmas in research-pass1-boundary.md,
research-pass2-offline.md and research-pass2-rounding.md, at their actual stated
contracts, and the compiler proved in research-pass3-compiler.md. Their exact
tests support those arguments; they are not substitutes for them.

## 1. Parameters, arbitrary parallel edges and zero optima

Fix eta=epsilon/1000, gamma=8eta, rho=1/32, C'=(1+2eta)C. Let q be the first
power of two >=2^20 eta^-2, U=4q, N=(2q+1)(n+1). Every integer logarithm or
dyadic precision index below is computed by bounded doubling/comparisons.

First remove edges of cost>C. Build normalized cost buckets: zero; a tiny
bucket (0,delta_c] with delta_c dyadic in (eta/(2n),eta/n]; and a geometric
dyadic grid from delta_c through 1. Generate this grid exactly as the mean
grid in the compiler, with multiplication factor 1+eta/4 and rounding mesh
<=eta*delta_c/100, clipping the final point to 1. All bucket ratios are at
most 1+eta/2, and their number Jc is O(eta^-1 log(n/eta)). An edge's bucket
is located by binary comparisons of c(e)/C with these bounded grid points.

In each (tail,head,bucket) retain a minimum-length actual original edge,
breaking ties by input order. Maintain a deterministic balanced map, whose
number of keys is <=n^2(Jc+1), without enumerating empty keys. Thus processing
the arbitrary original m records takes O(m[log(n+2)+log(Jc+2)]) comparisons
and arithmetic operations, never m log m. Store actual original IDs and
resource records for retained edges. Let M<=min(m,n^2(Jc+1)) be their count.

Every original retained-cost edge e has representative e' with

    ell(e')<=ell(e), c(e')<=(1+eta)c(e)+eta*C/n.

This follows separately for the zero, tiny, and geometric buckets. Replacing
all edges on a simple original C-feasible path gives the same vertex sequence,
no larger length, and cost <=C'. No simplicity assumption on the input graph
has been made. Nonnegative cycles can be removed, so original optima have
simple representatives. Replacing edges does not change endpoints.

Run ordinary nonnegative COST SSSP on retained ZERO-LENGTH edges. For every
vertex reached with cost<=C' store its zero-length path via an SSSP tree and
report bound zero. In particular every target with original OPT=0 is covered.
Zero-cost cycles pose no difficulty for a deterministic SSSP tree; ties retain
existing parents, and only settled-to-unsettled improvements are adopted.
The source has the empty path. Targets covered here require no clock query.

## 2. Finite event sequence, probability compiler, preprocessing

Use the compiler's dyadic mean grid from delta in (eta/(200n),eta/(100n)]
to U. Its size J is O(eta^-1 log(nq/eta)). Fix cost raw mean
q*c(e)/((1+4eta)C'). A zero resource stays exactly zero; every unblocked
positive mean is rounded UP to this grid. A raw mean above U gives certain
failure. Compile ALL mean laws by the bounded-bit conservative construction
and prefix-min CDF closure in research-pass3-compiler.md, with its b=64r.
The two clocks are independent, including their separate overflow symbols.
The probabilities are dyadic, nonnegative and normalized.

For each retained positive-length edge create the J real event values

    L=q*ell(e)/((1+4eta)mu_j).

Sort this COMPRESSED list and merge equal values, retaining per-edge event
lists with their global merged indices. At an event use the new, smaller
mean, including equality. Below the first own event an edge is blocked;
after the last it uses delta. Its law is indexed by predecessor search in
its own list in O(log(J+2)) operations. Zero lengths always use zero mean.
Cost means are fixed. There are E<=MJ events. There is no global geometric
weight exponent and no scan of an aspect-ratio interval. The bit length of
each event is bounded by that of its input edge and polynomial parameter
encodings. If E=0, all edges have zero length (or M=0); every original
feasible target was covered in Section 1, and all others may be unavailable.

Otherwise index the event snapshots by 0,...,E-1. Increasing indices give
stochastically nonincreasing increments, jointly in the two coordinates.
Use the actual whole-vertex, regularized-failure control model of pass 1:
source payoff rho, overflow/nontermination payoff 1+rho, voluntary ticks,
and backwards original-edge actions. Its exact value X is rho plus optimal
failure probability. This definition includes zero edges and closed classes.

Let D=max(1,ceil(log2(max(1,E-1)))); zeta=1/[16(2D+1)]. Choose a dyadic h0
such that

    h0<=min(zeta*rho/N, 1/[2^20 N]).

Apply EXACTLY the rounded, clipped persistent offline algorithm from pass 2.
In particular solve both endpoints rounded, replace the earlier endpoint by
its coordinatewise maximum with the later one, activate whole vertices,
use earlier-endpoint tables on inactive vertices, and clip midpoint labels
between the inherited endpoints. Do not attach a realizing policy to a
clipped label. Boundary values remain grid-aligned and clock-monotone.

The pass-2 proof gives, for every stored state and snapshot,

    X <= U <= (1+zeta)^(2D+1) X <= (16/15) X.              (4)

Estimates are globally nonincreasing in time, and clock-monotone. Its proof
uses the finite pointer rank N to bound upward-rounding residual by Nh0;
it does NOT require uniform absorption of arbitrary policies or contracting
zero-zero SCCs. Each vertex is active at O(q^2 D^2) calls; the same bound
charges every incident edge, including parallel edges. Only a parent's
active vertices are tested in its children. Persistent vertex blocks avoid
copying the whole graph or all-state table at each time.

For each not-yet-covered target find its first snapshot with
U(t,0,0)-rho<=1/16 by binary search in persistent versions. If none, report
unavailable. Otherwise store its L_t and length bound B_t=(1+8eta)L_t.
The following two sections prove this decision and its output semantics.

## 3. Completeness with all event and approximation directions fixed

Let a target be original C-feasible and not covered by zero-length SSSP.
In the retained graph with budget C', let Lstar be its optimal length.
It exists, is positive, is attained by a simple path, and is <=original
OPT_C(t). A largest edge on this path has length a in [Lstar/n,Lstar].
Its raw mean at Lstar lies in [q/((1+4eta)n),q/(1+4eta)], strictly inside
[delta,U]. The compiler's edge-local coverage proof gives an event

    Lstar <= L <= (1+eta/2)Lstar <= (1+eta)OPT_C(t).        (5)

This argument uses Lstar, rather than an invalid lower bound on the length
of a representative of an original optimal path.

At this event every edge of that optimal retained path is unblocked for
both clocks. By the upward-mean inequality, the total mean on each clock is

    <=(1+eta/2)q/(1+4eta)+n*delta <=q(1-2eta).

Indeed eta<=1/2000, (1+eta/2)/(1+4eta)<=1-3eta, and
n*delta<=eta/100<=q*eta. The sum of independent ideal Poisson increments
on a fixed path is Poisson with its total mean. If that mean is <=q(1-d),
the exponential-moment bound with exponent -log(1-d) gives tail at q at
most exp(-q[-log(1-d)-d])<=exp(-qd^2/2). Here d>=2eta and the chosen q
makes the union of the two tails <1/512. This is an analytic proof; no
exponential is required by the implementation.

The two compiled clocks on <=n path edges can be coupled to these ideal
increments with mismatch probability <=2nq*tau<=2^-19. Hence the compiled
control system can follow this fixed path with failure

    f <= 1/512+2^-19.

By (4), U-rho <=(16/15)(rho+f)-rho<1/16. Therefore some accepted event
exists. The FIRST accepted event has L_t<=L from (5). Reporting unavailable
for a true original feasible target is impossible. Originally infeasible
targets may also be accepted; the next section supplies actual relaxed-budget
paths for every accepted target and prohibits fabricated unreachable paths.

## 4. Explicit bounded-bit, bounded-space deterministic query

At one accepted L_t, run ONE whole-graph rounded static oracle on the retained
graph, at the same h0, and retain its chosen pointers. This is QUERY work,
never n separate preprocessing runs. If Y=X_t is the exact full static value,
its returned labels Z obey Y<=Z<=Y+Nh0. At (t,0,0),

    V=Z-rho <=1/16+2^-20,

since the accepted clipped preprocessing label is an upper bound on Y.
Terminal V is 0 at source and 1 at overflow. The chosen pointer action at
every state satisfies E[V_next]<=V_current (upward rounding gives this
direction). Every pointer trajectory has <=N decisions: a zero increment
decreases its layer's pop rank; a positive increment or wait increases the
clock sum; there are fewer than 2q nonterminal unit advances. This also
handles original zero-zero cycles without SCC contraction.

Put z=(1+4eta)/(1+8eta), d=1-z, and start two dyadic variables H_l=H_c=1/8.
Choose their mesh h=2^-b_d with b_d>=32+4 ceil(log2(q+2)) and
h<=1/[2^20 N]. At a selected edge whose rounded means are mu_l,mu_c,
an outcome (k,l) surviving both clocks proposes the analytic updates

    H_l'=H_l exp(k log z+d mu_l), H_c'=H_c exp(l log z+d mu_c).

Define Phi=V+H_l+H_c and give overflow outcomes potential 1, omitting H.
The conservative PGF inequality (2) in research-pass3-compiler.md proves
E[Phi_next]<=Phi_current. Independence allows the extra survival restriction
from the other clock to be dropped for an upper bound. A voluntary tick
multiplies its H by z and has V_next=V_current at a chosen tick seed.
Thus a nonoverflow outcome of a chosen edge has true proposed score at
most current Phi whenever Phi<1.

Compute upper approximations to the two proposed H's as specified below,
each with excess <=2h after upward rounding. Choose the surviving increment
pair minimizing the computed upper score; reject a pair with a component
certified >2. At least one candidate has score <=Phi+4h, so it is not
rejected while Phi+4h<3/4. Tick updates are computed exactly then rounded
up, with drift <=h. Induction gives

    Phi <= 1/16+2^-20+1/4+4Nh <3/4.                        (6)

Only candidates with score<3/4 are ever selected. Overflow is impossible,
and the finite pointer rank reaches source within N decisions. Store the
backward actual-edge walk, reverse it, and cycle-erase using a vertex stack.
Waits produce no physical edges. Output IDs are those of actual retained
original edges. Output workspace is O(nq+n+M), within the allowed bound.

Upward rounding preserves throughout

    H_l >= (1/8) z^(used length ticks) exp(d sum traversed mu_l),

including tick actions; similarly for cost. If physical length exceeds
(1+8eta)L_t, the raw-rate lower bound on each rounded mean implies
sum mu_l>q/z. Since used ticks<q, this would give

    H_l > (1/8) exp(q[log z+d/z]-log z)>1.

To justify the last strict bound, expand log(1-d)+d/(1-d): the linear terms
cancel and each remaining coefficient is (r-1)/r>=1/2. Thus the bracket
is >=d^2/2; d=gamma/[2(1+gamma)]>=gamma/3. Our q satisfies
q gamma^2/18>log 8 (for instance log 8<3), with ample margin.
This contradicts (6). The cost argument is identical with C' in place of L_t.
Therefore the actual path has length<=B_t and cost<=(1+8eta)C'. Combining
with (5),

    B_t <=(1+8eta)(1+eta)OPT_C(t)<=(1+epsilon)OPT_C(t),
    cost <=(1+8eta)(1+2eta)C<=(1+epsilon)C.

Cycle erasure cannot increase either nonnegative resource. The zero-length
branch has already supplied its exact bound. An accepted unreachable target
would have yielded an actual path by the finite pointer/potential argument,
so none can be fabricated.

## 5. Numerical subroutine used by the query (no exact exp/log oracle)

Here b=b_d>=32, a=ceil(log2(q+2)), J0=16(b+a+1). Since d<=1/4, compute
the EXACT rational finite sum L0=-sum_{r=1}^{J0}d^r/r. The logarithm tail
is <=2*4^(-J0-1). For k<q let x0=k L0+d mu. The true x=k log z+d mu obeys

    0<=x0-x<=2^-32b.

The sum's length and its rational bit lengths are polynomial in b,a and
the encoding of eta; no exponent of order 1/eta is formed.

Set T=b+2. If x0>=T+1, then H>=2^-b implies H exp(x)>2; this component
may be rejected, not assigned a fictitious upper enclosure. If x0<=-T-1,
return h as the new H: since H<=1 and e>2, H exp(x)<=exp(-b-3)<h.
Otherwise |x0|<b+3. Choose a power of two R with 8(T+2)<=R<16(T+2).
Set B=100(b+a+1), h'=2^-B, and y'=floor_h'(x0/R), so |y'|<1/7.
Evaluate the degree K=16b exponential Taylor polynomial by Horner:

    A=1; for r=K,...,1: A=floor_h'(1+y'*A/r).

Every Horner value is between 0 and 2. The rounding error is at most
h'/(1-1/7)<2h'. Replacing x0/R by y' adds <2h'. The Taylor tail is
<=2*7^(-K-1)<=2^(-32b-1). Thus

    |A-exp(x0/R)| <=4h'+2^(-32b-1).                       (7)

Square A log2 R times, rounding down to h' after EACH squaring. All values
are bounded by 2^(2b+16); bounded integer searches therefore implement
each rounding with O(B+b) comparisons. To bound propagation, compare the
j-th approximation with exp(2^j x0/R), whose magnitude and inverse are
<=exp(b+3). In relative error, squaring gives

    r_j <=2r_(j-1)+r_(j-1)^2+h' exp(b+3).

For r_j<=2^-b, iteration of 2+2^-b over log2 R stages is <=2R (use
R<16(b+4) and b>=32). This bootstraps that inequality and yields final
absolute error at most

    2^(5b+32) [4h'+2^(-32b-1)+h'] <=2^(-26b+1).

For example exp(b+3)<2^(2b+6), R<16(b+4)<2^b, and log2 R<b bound all
factors in this loose estimate; its resulting relative errors are far below
2^-b, verifying the bootstrap assumption at every earlier stage. The
additional error between exp(x0) and exp(x) is <=2^(2b+8)2^-32b.
Together the absolute exponential error is <2^-20b. Consequently final
approximation A_final+2^-10b is a genuine upper enclosure of exp(x), with
excess <=2^(1-10b). Multiply by H<=1 and round up to h. Its excess over
the true new H is <=2h, as used in Section 4. An underflow result h also
has excess <=h. Rejected components cannot occur in a selected low score.

The exact initial log sum has polynomially bounded encoding, as does x0;
all later stored numbers are B-bit dyadics plus O(b) integer bits. Negative
bounded rounding is implemented by shifting to a nonnegative bounded
interval before binary search. Every step is a charged +,-,*,/,comparison
or bounded control operation. No arbitrary-real floor, free logarithm,
unbounded rational exponent or unbounded-precision library is invoked.
check_bounded_exponential.py implements this construction with direct bounded
integer dyadic rounding as a diagnostic convenience. Its ten 130-digit
Decimal comparisons and two guard checks are numerical smoke tests only;
the universal certification is the preceding error argument.

## 6. Total operations, space, encodings and novelty boundary

Write p=1+ceil(log2(n+2))+ceil(log2(1/eta+2)); all precision indices are O(p),
q=O(eta^-2), J,Jc=O(eta^-1 p), M<=min(m,n^2(Jc+1)), and
E<=MJ. After compression log(E+2)=O(p), so D=O(p). Creating and sorting
events costs O(MJ p). The shared probability compiler costs
O(J(q+p)p) plus its O(Jq) envelope/storage. Bucket identification and the
bounded map cost O((m+n)p^2). Ordinary zero-length SSSP costs O((M+n)p).

The pass-2 bound, including its two endpoint solves, is conservatively

    O(E + (M+n)(1+q^2 D^2) q^4 [p^2+log(n+2)]).

Here p^2 covers event lookup, upward label rounding and all bounded numeric
operations; the q^4 charge already includes forming the clock-product
expectations. Parent-only activity tests, incident-only graph scans and
persistent blocks are part of that algorithm, not optional assumptions.
Their persistent storage is O(nq^2+E+nq^2D^2(q^2+log(n+2))) plus graph,
coefficient tables and reused static scratch. An O(Mq^2) scratch bound is
also harmless. Per-target binary search costs O(p log(n+2)); n such searches
do not add n full static runs. Stored target values/IDs need O(n) records.
Every displayed term is <=O((m+n)eta^-12 p^8), after increasing an absolute
constant (the deliberately conservative p^8 covers the smaller terms).
Absorbing log(1/eta) factors into extra powers of 1/epsilon, universal
exponents a=20,b=100 and a sufficiently large absolute K satisfy source.md.
No dependence on aspect, magnitude or input precision occurs in these counts.

At a query, one static solve on M=poly(n,1/epsilon) edges, followed by at
most N decisions and q^2 polynomial(p)-cost candidate evaluations per edge,
is polynomial in n, log(n+2),1/epsilon plus output. Scratch is covered by the
same near-linear preprocessing space bound, even while keeping the persistent
representation. No unrestricted n-by-scaled-length DP is being used.

For rational inputs, original edge comparisons/events and SSSP sums have
polynomial encoding in the input and n,m. Mean, probability and DP grids
have O(p)-bit indices; DP products temporarily have O(p+log q) bits and
are rounded before reuse. Recursion clips stored dyadics, so denominators
never accumulate with recursion depth. The query log series has degree O(p)
and polynomial input-encoding growth, followed by fixed-precision arithmetic.
Control integers have O(log(n+m+1/epsilon)) bits, up to fixed constants.

Nearest verified primary comparisons and bounded search limitations are in
research-pass3-literature.md. The clock DP and the conditional-expectation
potential are prior work of Ashvinkumar; recursive offline activation and
multiplicative counting are prior work of Gorkiewicz--Karczmarz. The claimed
new contribution is their nonadditive whole-vertex boundary integration,
with first-hit pricing, bounded-value regularization, clock-compatible
clipping/finite-rank rounding, and edge-local scale coverage; together these
remove ALL numerical-aspect dependence for ALL targets, including witnesses
and arbitrary parallel/zero edges in the frozen model. Merely repeating
single-target reduction, ordinary SSSP, a CDF approximation or the numerical
subroutine would not be the claimed innovation. Correctness, originality
and theoretical significance of this complete combination require fresh
critical review. No mathematical/innovation/venue verdict has been invented.

Known remaining proof gaps identified by this proposer: none in this claimed
scope. This is a proposal for audit, not a certificate that no gap exists.
