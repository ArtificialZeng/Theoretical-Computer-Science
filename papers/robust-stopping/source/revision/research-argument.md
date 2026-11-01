# Revision candidate: uniform frontier, uniqueness, and sharp support

Proposer: robust-stopping-research-cd75b220d422, research pass 2.
This is an argument for a new freeze and fresh referee. Previous mathematical
acceptance applies only to the old snapshot. The original `source.md` is
unchanged; its broad task remains unresolved. This file treats the new seed
as unaccepted and proves its statements independently of the seed checker.

## Exact theorem U

Fix an integer b>=2, let a=b-1, rho_b=b^b/(b^b-a^b), and let the forecast be
uniform on the integer horizons 1,...,b. Robustness is required at every
positive integer actual horizon, with the source's cost C_t(x). Write r=R-1,
m=(b+1)/2, and, for 1<=i<=b,

    z_i=b^(i-1)/a^i,
    A_j=sum_{i<=j}z_i=(b/a)^j-1,
    C_j=sum_{i<=j}(b+1-i)z_i=(2b-j)(b/a)^j-2b,
    r_j=b/(b+C_j),  j=0,...,b, with A_0=C_0=0.

Then r_0=1>r_1>...>r_b=a^b/(b^b-a^b)=rho_b-1.
For r_j<=r<=r_{j-1}, define

    f_i=r z_i                       (1<=i<j),
    f_j=[b-r(b+C_{j-1})]/(b+1-j),
    f_{b+1}=1-sum_{i<=j}f_i,

with all other entries zero. This is the unique expected-cost minimizing
R-robust law for rho_b-1<=r<=1, including all endpoints. Adjacent formulas
agree at shared endpoints. For r>=1 the deterministic law T=b+1 is optimal.
The value on segment j is

    V_j(r)=m+lambda_j b+s_j r,
    lambda_j=(b+j-2)/(2b),
    s_j=sum_{i<j}d_i z_i-lambda_j(b+C_{j-1}),
    d_i=(b+1-i)(b+i-2)/(2b).

There are exactly b strictly decreasing affine pieces followed by the
constant m on R>=2. Their shared representation (z, A, C, lambda, slopes,
intercepts, and breakpoints) takes O(b) rational arithmetic operations and
O(b) rational numbers. A policy query, its dual, and its value take O(b)
operations. Bit lengths are O(b log b+len(R)) per rational, so bit time is
polynomial in numerical b and the binary encoding of R. Listing b dense
policy vectors is not included in the O(b) claim.

For every b, at every r strictly between r_b and r_{b-1}, the unique optimum
has b+1 positive entries, with both b and b+1 present. Consequently both
the earlier general b+1 total-support bound and the two-days-at-least-b
bound are necessary, simultaneously, on this family.

## 1. Robustness equivalence and the objective

For a law f, robustness is equivalent to

    sum_{t<=x}(a+t-x) f_t <= r x      (1<=x<b),
    mu(f):=sum_t(t-1)f_t <= rb,
    f>=0, sum f=1.                                      (U1)

For completeness, the exact expected cost is x+the displayed prefix sum.
At x>=b it is bounded by b+mu. Conversely C_t(x) increases to b+t-1 as
x increases; monotone convergence forces b+mu<=Rb from the original cap.
Thus (U1) follows without assuming a finite moment in advance and is
sufficient. This is KF26 Lemma 5.1, retained as prior work.

Directly summing the b uniform forecast atoms gives

    g(t)=m+d_t (1<=t<=b),   g(t)=m (t>=b+1).             (U2)

In particular every d_t is strictly positive. The known geometric prefix
recurrence gives z_i, but neither this recurrence nor (U1) alone determines
the optimal prefix cut or the frontier below.

## 2. Closed-form feasibility for all real r in the stated intervals

The identities for A_j,C_j follow from their first values and multiplication
by b/a; alternatively subtract the j-1 expressions. Every increment of C
is positive, proving strict ordering of the r_j. Substitution at j=b gives
the asserted classical endpoint. Define also

    M_j=sum_{i<=j}(i-1)z_i=b-(b-j)(b/a)^j.

The identity is proved by the same one-step recurrence. It gives M_j<b for
j<b and M_b=b. At r=r_j the displayed law has f_i=r_j z_i for i<=j;
at r=r_{j-1} its jth mass vanishes and its earlier masses equal r z_i.
This proves agreement of adjacent formulas. Since f_j and r z_j-f_j are
affine in r and nonnegative at these two endpoints, 0<=f_j<=r z_j
throughout the interval.

For the full geometric schedule f_i=r z_i, the xth prefix row is tight:
at x=1, a f_1=r; subtracting successive tight rows yields
 a f_x=r+sum_{i<x} f_i, which z_x satisfies. Hence the first j-1 rows
are tight for our policy. If j<b, its jth row is feasible because
f_j<=r z_j. At every later prefix horizon x<b, no further mass is added,
so the row's left side decreases by the fixed nonnegative early mass when
x increases by one, while its right side increases by r. These rows are
feasible. For j=b there is no jth prefix row to check.

The normalization residual at endpoint r_j is 1-r_j A_j. It is nonnegative
because b A_j<=b+C_j is equivalent, using C_j=b A_j-M_j, to M_j<=b.
It is strictly positive for j<b and zero for j=b. The other endpoint is
the j-1 endpoint and has a positive residual, with j=1 giving residual 1.
The residual is affine in r, so it is nonnegative on the whole interval.
All entries therefore form a probability law. Finally

    mu=b-sum_{i<=j}(b+1-i)f_i=rb                      (U3)

by the formula for f_j. This proves every original robustness constraint.
For r>=1, T=b+1 has mu=b<=rb and all early prefix rows zero.

## 3. Global dual certificate and uniqueness

The following sufficient certificate applies to every original robust law:
if lambda,y_x>=0 and

    g(t)+lambda(t-1)+sum_{x=t}^{b-1}(a+t-x)y_x>=alpha  (all t>=1),

then J>=alpha-r sum_{x<b} x y_x-lambda rb. The sum over prefix rows is
finite; g is bounded and the required moment is finite by (U1), so taking
expectations is legitimate on the unbounded domain.

On segment j put lambda=lambda_j>0, alpha=m+lambda b, and y_i=0 for i>=j.
Choose y_{j-1},...,y_1 by requiring dual equality at t=j-1,...,1.
Equality at t=j is already true, since d_j=lambda(b+1-j). When j>=2,

    a y_{j-1}=(b-j+2)/(2b)>0.

Writing c_i=g(i)+lambda(i-1), subtracting adjacent equality equations gives

    a y_i-sum_{k=i+1}^{j-1}y_k=c_{i+1}-c_i
                               =(b+j-2i)/(2b)>0
                for 1<=i<j-1.                       (U4)

Backward induction proves all y_i>0 for i<j. This establishes dual
feasibility at t<=j. At j<t<=b the reduced cost is exactly

    (b+1-t)(t-j)/(2b)>0.

At t=b+1 it is zero. At every t>b+1 it is lambda(t-b-1)>0, proving the
inequality on the entire infinite set of buy-days. Thus equality holds
precisely on {1,...,j,b+1}. The constructed policy uses these days, its
first j-1 prefix constraints are tight, and (U3) saturates the moment.
Complementary slackness therefore proves optimality and the value formula.

Conversely every optimal law must make every nonnegative term in its dual
gap zero. Strict reduced costs force its support into {1,...,j,b+1}; positive
y_i force the first j-1 rows tight, and positive lambda forces mu=rb.
The triangular rows uniquely fix f_i=r z_i for i<j. Normalization and moment
then give exactly the displayed f_j and f_{b+1}. This works at both segment
endpoints even when one allowed coordinate is zero, at j=b with no residual
tail, and at j=1 with no prefix equations. Thus uniqueness includes r=1.
For r>1, (U2) shows the unconstrained minimum is m and T=b+1 attains it;
uniqueness is not asserted there.

## 4. Exact number of pieces, support necessity and arithmetic bounds

Substitution of the policy into J=m+sum d_i f_i gives V_j above. The slopes
satisfy

    s_1=-(b-1)/2<0,
    s_{j+1}-s_j=-(b+C_j)/(2b)<0.                     (U5)

The intervals are encountered in reverse j order as r increases. They
therefore have increasing but distinct negative slopes, followed by zero.
Each interval has positive length, so no segment disappears. The value is
continuous because endpoint policies agree. This proves exactly b+1 pieces.
In (r_b,r_{b-1}) take j=b. All r z_i (i<b) and f_b are positive; the tail
is affine, zero at r_b, and strictly positive at r_{b-1}. It is therefore
positive throughout the open interval. The uniqueness just proved rules
out any smaller-support optimum, including laws on omitted later days.

Compute z consecutively, accumulate A,C and W=sum d_i z_i, and generate one
row (lambda,intercept,slope,r_j) per j. These are constant many arithmetic
operations per row. Locate a query interval in one scan, compute f and its
dual via suffix sums in (U4), in O(b) operations. Powers b^j,a^j have
O(b log b) bits; all finite geometric sums share denominators dividing
a^b, and the d_i have denominator 2b. Thus their numerators and denominators,
all r_j and all slope/intercept coefficients have O(b log b) bits. Query
products and ratios add O(len(R)) bits; the triangular dual has at most b
levels and denominators dividing (2b)a^b. Explicitly summing O(b) rationals
with these common denominators keeps the same polynomial bit bound.

## 5. Independently chosen finite attacks and limits

`uniform_frontier.py` is the formula/query implementation.
`verify_uniform_frontier.py` computes costs directly from the original
forecast and checks primal and dual equality, positive dual prices, strict
reduced costs, endpoint agreement, all closed-form sum and slope identities,
and support necessity. Its probes use thirds and seeded rational fractions,
including b values absent from the seed tests. For b<=5 it separately
enumerates every finite-polytope vertex by exact Gaussian elimination;
for b<=9 it also compares the old optimizer. A finite list of reduced-cost
checks is not the proof of the infinite tail; its affine formula above is.
The saved JSON describes actual coverage. These checks are proposer evidence,
not a fresh-context review.

Known mathematical gaps in theorem U after this pass: none identified by
its proposer. The novelty screen is bounded and detailed separately; it is
not proof of priority. The general arbitrary-forecast frontier remains
uncharacterized beyond the older parametric-LP facts and pointwise optimizer.
The proposed structural addition and sharp lower family belong in the same
result note as the corrected optimizer, not a new independent paper.

## 6. Required prior-structure qualification

`prior-overlap.md` identifies this law with KF26 C.1(ii)'s one-hot-b capped
geometric optimizer for r<=1-1/b and with another one-hot-b optimum above
that cut. Thus theorem U does not introduce a new canonical distribution,
and the route to the support pattern is already available in that prior
work. Its role in the revised note is the uniform objective's explicit
frontier and uniqueness, with full credit for the underlying structure.
This limits novelty and must be visible to the fresh referee and writer.
