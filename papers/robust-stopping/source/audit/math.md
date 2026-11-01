# Fresh mathematical referee report

Job: `robust-stopping-referee-e7c6798337e7` (referee).
Snapshot: `c70f1a41d2a4a68c3ad3f996323997e58e2b037484d8e4d79a5f9e8327bd3f3d`.

**Verdict: accept the exact combined frozen claim as a result-note, with the
original problem unresolved.** This acceptance includes the published D.2
application and the six specifically bounded software observations, as well
as the general pure-bisection optimizer, complexity statements, uniform
frontier, uniqueness and sharp support results. It does not adopt a smaller
scope in place of the submitted claim.

I reconstructed the argument from the original model, read the required
revision instructions and the listed decisive evidence, and wrote a new
verifier. I did not read previous mathematical audit reports, checkpoint,
scheduling state or job transcripts. References to previous acceptance in
mandatory handoffs were not used as evidence. No mathematical candidate,
source, optimizer implementation or frozen artifact was changed. This is
a separate model-context check, not human peer review or statistical
independence.

## 1. Frozen scope and integrity

All 57 files in the snapshot match their SHA-256 entries, and its canonical
mapping hash matches the snapshot digest. The unchanged original source has
SHA-256 `9721525d4da99587f7ef8b0f276225877c55b07af8d97e03a873448bbe839b32`.
These checks were repeated after the computations. The scope restriction
`max_chord_probes=0` is essential to the stated main algorithm and was used
in all new optimizer executions. The broad task also asks about an arbitrary-
forecast complete frontier; that task remains unresolved.

The substantive inputs are the original research argument and code, the
revision's elimination/bit supplement, uniform proof and implementation,
overlap calculation, exact separation arguments, complete published PDF,
both hash-bound Python files, and the software-extension evidence. Older
seed arguments and informal handoff traces were treated as proposals. The
literal construction trace in the frozen extension correctly supersedes
the earlier intermediate-state shorthand.

## 2. Robustness, dominance and existence

Write `r=R-1`, `a=b-1` and `mu=sum(t-1)f_t`. Expanding the original cost gives

    E C_T(x) = x + sum_{t<=x}(b+t-1-x) f_t.

For each fixed buy-day the cost increases to `b+t-1`. Monotone convergence,
applied before assuming a finite moment, shows that robustness implies
`mu<=rb`. The `b-1` early rows and this moment bound are also sufficient:
for `x>=b` cost is at most `b+mu`. This handles the unbounded actual horizon;
a finite-horizon check alone would not suffice. This reduction is credited
to KF26 Lemma 5.1.

For `t>=b`, map `t` down to the last member `s<=t` of
`{b} union {d+1:p_d>0,d>=b}`. There is no positive forecast atom in
`[s,t-1]`; hence `g(t)-g(s)=(t-s)Pr[D>=t]>=0`. The map decreases moment
and leaves early constraints unchanged. It also dominates adjusted tail
cost for every nonnegative moment price. Thus the asserted finite set S
suffices for both primal optimization and extension of the dual inequality
to all omitted buy-days. Zero-probability entries do not enlarge S.

The stated classical geometric law sums to one, has every early row tight
at `rho_b`, and has moment `b(rho_b-1)`. It supplies nonemptiness at every
allowed R. The finite feasible set is compact, so an optimum is attained.

## 3. Backward elimination and normalization oracle

After removing normalization and moment, every feasible earlier prefix has
exactly the interval

    0<=z_i<=[ri-sum_{j<i}(a+j-i)z_j]/a

available at coordinate i. Its numerator is positive: the preceding row
gives a lower bound `r+sum_{j<i}z_j`. Extending later coordinates by zero
keeps later rows feasible. Therefore minimizing the last remaining linear
coefficient at its zero or upper endpoint is an equality of conditional
value functions, not merely a heuristic feasible move. Backward induction
proves the elimination rule and its dual recurrence

    y_i=max(0,[alpha-c_i-sum_{j>i}(a+i-j)y_j]/a).

Forward reconstruction attains the resulting lower bound. This closes the
earlier exposition's missing optimality step.

For a fixed active set B, differentiating its triangular dual equations
gives positive derivatives. If k is the next active index after i, the
inactive slack decreases at speed `(k-i) sum_{j>=k,j in B} h_j>0`; with
no later active index its speed is 1. Existing active multipliers increase.
Thus activation is nested and each early index enters at most once. The
canonical prefix mass is

    r [product_gaps(1+gap/a)-1],

which strictly increases when an index is inserted. Before reaching the
least tail cost, the sweep either reaches mass one or reaches the tail
cap with mass below one. At a mass crossing, the old and new schedules
are both prefix minimizers because all newly active dual multipliers are
zero. Their displayed interpolation has mass one and attains the same
dual value. At the tail cap the missing mass goes to a minimizing tail
day. Simultaneous activations and cap ties obey the same equalities.

This proves the oracle for arbitrary rational costs, including signed
costs. Suffix sums give linear work per event and there are at most b-1
events, establishing `O(b^2+|S|)` arithmetic operations. Every normalized
oracle output uses at most one tail day.

## 4. Pure bisection, exact price and bit bounds

Let Q be the finite normalized early-prefix polytope without its moment
bound. Every vertex has at most b positive coordinates. Its independent
active system is an integer matrix of order at most b with entries bounded
by b; normalization is included. Cramer's rule gives a common coordinate
denominator dividing `q_R |det|`, with `|det|<=D=b! b^b`. Consequently
vertex objective and moment each have denominators at most
`H=q_p q_R D`, and values between zero and `L=b+max S`.

Every nonnegative intersection of two distinct vertex lines
`J+lambda*mu` with different slopes has reduced numerator and denominator
at most `Z=2 L H^4`. Distinct intersection prices are separated by at
least `1/Z^2`, and all positive intersections are below or equal to Z.
At `Z+1` the oracle therefore has minimum possible moment, which is at
most `rb` by feasibility. The price-zero case returns immediately if its
moment is already feasible. Otherwise the stored endpoint moments bracket
`rb` throughout bisection.

Once the bracket is shorter than `1/Z^2`, it contains exactly one relevant
intersection. Both stored policies minimize the priced objective there.
This remains true if an endpoint output is a nonvertex tied-face mixture:
its constituent optimal lines meet at that endpoint, while the policy
from the other side extends continuously to the same intersection.
The displayed line-intersection formula recovers the price exactly, and
moment interpolation yields a normalized early-feasible policy with
moment `rb`. The recomputed dual at that price proves equality of primal
and dual values. Its all-buy-day inequality is valid by the dominance
argument above. Finite moment, bounded g and finitely many prefix terms
justify taking its expectation against every original robust law.

There are `O(log Z)` oracle calls, rather than that many total arithmetic
operations. Combining two one-tail oracle policies gives at most two tail
days and at most b+1 total support days.

The supplement's common-denominator argument is sufficient for intermediate
bits. On an active set of size k, affine dual coefficients have denominators
dividing `a^k` and `Q_c a^k`, where Q_c is a common denominator of the
original costs in this oracle call. Their magnitudes grow at most
exponentially in k, which adds only O(b) bits. Each activation root is a
ratio of coefficients from that original-cost affine system, so successive
root representations do not recursively enlarge the bound. Canonical
prefixes share denominator `q_R a^a`; normalization uses one ratio of
mass differences. Bisection prices use only `O(log Z)` denominator bits;
the final interpolation and dual solve preserve polynomial bit lengths.
Thus the stated bit time is polynomial in numerical b and input length.
Huge encoded forecast horizons enter through their binary lengths and L.
There is no polynomial-in-log(b), strong-polynomial, or LP speedup claim.

## 5. Uniform forecast theorem

Direct summation yields `g(i)=m+d_i` for `i<=b` and `g(t)=m` afterwards.
The z, A and C identities follow by subtracting successive expressions.
In particular C strictly increases, `r_0=1`, and
`r_b=(b-1)^b/[b^b-(b-1)^b]`. The partial jth mass lies between zero and
`r z_j`, since this holds at both endpoints and both differences are
affine in r. Earlier rows are tight; later unfilled rows remain feasible.

Tail nonnegativity follows at endpoints from
`M_j=sum_{i<=j}(i-1)z_i=b-(b-j)(b/a)^j<=b` and
`C_j=b A_j-M_j`, and then throughout each interval by affinity. The moment
identity is exactly `mu=rb`. Adjacent endpoint policies agree.

For segment j, the stated positive lambda and alpha, together with the
triangular equality solve on `i<j`, have strictly positive early prices.
The last such price satisfies
`a y_{j-1}=(b-j+2)/(2b)>0`, and the preceding ones follow from
`a y_i-sum_{k>i}y_k=(b+j-2i)/(2b)>0`. Their reduced costs vanish exactly
on `{1,...,j,b+1}`. For `j<t<=b` the reduced cost is
`(b+1-t)(t-j)/(2b)>0`; after b+1 it is `lambda(t-b-1)>0`.
Thus the certificate holds on the entire infinite domain.

Complementary slackness forces every optimum to those allowed days,
tightens the first j-1 rows and the moment, and uniquely determines the
displayed masses. This includes endpoints, j=1, j=b and R=2. For R>2 the
deterministic day b+1 attains the unconstrained minimum; uniqueness there
is correctly not asserted. The slope differences
`s_{j+1}-s_j=-(b+C_j)/(2b)` are strict, so all b decreasing pieces occur,
followed by the plateau. In the open lowest segment every one of the
b+1 masses is positive. Uniqueness excludes any smaller-support optimum,
even on omitted later days, establishing simultaneous sharpness.

The compact representation and query costs are O(b) rational operations;
shared denominators and geometric powers give the claimed
`O(b log b+len(R))` bits per rational. This is not an O(b) claim for
printing b dense policy vectors.

## 6. Separations and the published/software extension

At `b=3,R=3/2,p=(2/5,3/5)`, direct costs are
`g=(3,14/5,8/5,8/5,...)`. The affine bound
`g(t)+(7/10)(t-1)>=3`, equal only at 1 and 3, proves the global optimum
39/20, attained by `(f_1,f_3)=(1/4,3/4)`.
Below raw level 14/5 the allowed support has moment at least 2. At that
level `2 f_2<=1` and `mu>=2-f_2` force `f_2=f_3=1/2`, so the level is
14/5 and its unique feasible law costs 11/5. All three quantities have
distinct meanings. The correction targets the precise D.2 optimality
inference, even with an ideal feasibility checker.

For the other forecast `(1/2,1/2)`, the global bounds
`g(t)+(3/4)(t-1)>=3` and
`q(t)+(1/2)(t-1)>=2` give minima 15/8 and 5/4 for the expected-cost and
expected-per-horizon-ratio objectives respectively. Strict reduced costs
and tight moment prove uniqueness. Their other-objective values 21/16
and 2 check directly. Dividing J by the fixed expected offline optimum,
in contrast, preserves minimizers.

I independently extracted the complete hash-bound proceedings PDF and
read printed pages 7 and 29--30. The model and isolated D.2 inference are
indeed present, so the same exact separation applies to this identified
published version. The official PMLR page and its Software link were also
reopened. The source/version checks and read-only URLs are recorded in
`referee-e7c6798337e7-source-review.md`.

I inspected both frozen source classes and used a new AST loader, without
importing either proposer reproduction wrapper or running top-level
experiments. Both files, at all three literal specified tolerances, return
the claimed water levels and binary-exact masses `(1/4,3/8,3/8)`. Conversion
with `Fraction(float)` gives cost 12/5 and moment 9/8 without rounding.
Direct horizon costs are 3/2, 3 and 33/8 at horizons 1, 2 and 3; every later
horizon has cost 33/8, at most 9/2. Thus the observed policy really is robust,
despite its suboptimal expected cost. Both calls to the feasibility method
give the stated False/True results; `14/5` in these literal calls is the
Python floating argument, not a replacement exact-arithmetic implementation.

A separate line tracer confirms the construction's intermediate day-3
mass 9/16 and F=19/16; the existing correction leaves day-3 mass 3/8.
The final construction locals still have F=19/16 and mu=33/16. These
locals are not used to certify the returned law. No third-party code was
repaired. In particular, 11/5 is not mislabeled as software output.

The six software runs are finite observations about the exact frozen
hashes and supplied pinned-commit provenance. Online commit refresh was
only partly available; neither that access failure nor supplied Git
metadata is represented as a theorem or independent authentication of
repository history. The frozen observations are fully reproducible
locally. No current-head, convergence, all-tolerances or all-implementations
assertion is accepted or made by this frozen claim.

## 7. Contribution and source comparison

The nearest result is KF26's general water-filling proposal, robustness
reduction, and one-hot C.1(ii) optimizer. I checked the latter primary
statement: the uniform law is exactly its selected capped-geometric law
below `r=1-1/b`; above that cut it is another one-hot-b optimum. The claim
correctly credits this overlap. Geometric and gap recurrences and elementary
support reduction are not new contributions here. The separate source
review records the current primary checks and bounded access limitations.

Generic finite LP already gives polynomial bit time. The value of this
combined note is a proved explicit certifying replacement for an incorrect
general rule, with nested normalization and exact moment-price recovery,
plus the uniform expected-objective frontier and strict uniqueness/sharpness
analysis. This is more than an LP restatement or an implementation-only
counterexample, and the uniform family is natural rather than an arbitrary
toy restriction. It supplies a usable optimizer and witnesses in precisely
the distribution-advice model where the criticized prescription was meant
to apply. I find that combined delta sufficient for a coherent result-note.
The known one-hot law and generic LP complexity prevent stronger novelty
or algorithmic-advantage language. No exhaustive priority or venue-fit
claim is certified.

## 8. Independent finite checks and remaining limits

Run `python3 -B audit/referee-e7c6798337e7-verify.py`. It writes only the
fresh referee JSON and never rewrites frozen evidence. Its saved results
in `referee-e7c6798337e7-checks.json` include:

- 614 serialized full-model primal/dual certificates and 144 signed-cost
  oracle certificates, checked by new direct inequalities;
- 32 new pure-bisection instances, including minimum robustness, loose caps
  and zero-probability huge horizons;
- 24 independent exact vertex optimum comparisons and 96 new signed-cost
  oracle comparisons against exact vertex enumeration;
- three extra cases including a positive horizon 10^60 and a huge R numerator;
- 930 uniform certificate queries, 620 endpoint-formula comparisons, nine
  independent unique-optimum vertex comparisons, and sharp support checks
  at 21 b values through 64;
- both unchanged software classes at the six specified calls, independent
  construction traces, and three global objective-separation certificates.

Finite computations support implementation correspondence; the reconstructed
analytic arguments establish the quantified and infinite-tail claims. No
counterexample or remaining proof gap was found in the exact frozen scope.
Original general-frontier work remains unresolved. Manuscript authorship,
official formatting, complete citations, compilation, packaging and all-page
visual review belong to the subsequent writing/release phases; this audit
does not certify those deliverables or authorize external actions.
