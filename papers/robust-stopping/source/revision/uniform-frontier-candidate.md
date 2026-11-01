# Unaccepted candidate: complete uniform-forecast frontier and sharp support

This is a parent-proposed mathematical seed for independent proof and
counterexample/known-equivalence search. No acceptance, novelty or venue claim.
Use the original discrete cost/pointwise robustness model. Let b>=2, a=b-1,
r=R-1 and p uniform on {1,...,b}. Set m=(b+1)/2 and

    z_i=b^(i-1)/a^i, i=1,...,b;
    A_j=sum_{i<=j}z_i=(b/a)^j-1;
    C_j=sum_{i<=j}(b+1-i)z_i=(2b-j)(b/a)^j-2b;
    r_j=b/(b+C_j), j=0,...,b, with A_0=C_0=0.

Then 1=r_0>r_1>...>r_b=r*=rho_b-1. All are rational.
For every r in [r_j,r_{j-1}], j=1,...,b, propose the law

    f_i=r z_i                  (1<=i<j),
    f_j=[b-r(b+C_{j-1})]/(b+1-j),
    f_{b+1}=1-sum_{i<=j}f_i,
    all other coordinates zero.

For r>=1 take f_{b+1}=1. At shared endpoints adjacent formulas agree.
Proposed theorem: this is the unique optimum for r*<=r<=1; for r>1 it
is an optimum. The optimal value is m+sum_{i<=j}d_i f_i, where

    d_i=g(i)-m=(b+1-i)(b+i-2)/(2b), 1<=i<=b.

It has exactly b strictly sloping affine pieces and the constant piece
R>=2; a compact description of all breakpoints and affine value pieces, with shared
prefix data for the policy formulas, can be produced in O(b) rational arithmetic
operations. One queried policy and its dual take O(b) operations; explicitly
listing b dense policy vectors is not claimed to take O(b). Exact bit lengths are polynomial in
b log b and the rational R encoding. The general arbitrary-forecast method
remains as previously accepted; this gives a structural contribution that
generic polynomial-time LP existence alone does not supply.

## Proposed feasibility proof

For the full first-i prefix schedule, tight constraints give f_i=r z_i.
At r_j, the moment reduction from a b+1 tail is r_j C_j=b(1-r_j).
For r_j<=r<=r_{j-1}, the displayed partial f_j is between zero and r z_j;
all later coordinates <=b are zero. This keeps every prefix constraint
feasible, by the original triangular zero-extension argument. The full
first-j schedule's moment M_j=sum_{i<=j}(i-1)z_i equals

    M_j=b-(b-j)(b/a)^j <= b,

with equality only j=b. Hence at threshold r_j the prefix mass r_j A_j
is <=1, since b A_j<=b+C_j is equivalent to M_j<=b. It is <1 for j<b.
The total mass is affine in r on each interval, so tail nonnegativity
holds throughout, including the bottom endpoint r_b where tail=0.
By construction mu(f)=b-sum_{i<=j}(b+1-i)f_i=rb. At r>=1 the sole
buy-day b+1 has moment b<=rb and minimizes all forecast costs.

## Proposed dual certificate, optimality and uniqueness

On segment j choose

    lambda_j=d_j/(b+1-j)=(b+j-2)/(2b)>0,
    alpha=m+lambda_j b.

For i<j solve the same triangular prefix dual equations with positive
prices y_i; put y_i=0 for i>=j. The last positive coordinate is

    a y_{j-1}=(b-j+2)/(2b), if j>=2.

Successive subtraction gives, for i<j-1,

    a y_i - sum_{k>i}y_k = c_{i+1}-c_i
                       = (b+j-2i)/(2b)>0,
    c_t=g(t)+lambda_j(t-1).

Thus all y_i for i<j are strictly positive, and the early reduced costs
are zero through j. For j<t<=b, reduced cost is

    d_t-lambda_j(b+1-t)=(b+1-t)(t-j)/(2b)>0.

At t=b+1 it is zero. For t>b+1 it is lambda_j(t-b-1)>0 because g(t)=m.
This is the global dual certificate. Complementary slackness holds for
the displayed policy, proving optimality without numerical LP inference.

Strict positive dual prices force the first j-1 prefix rows tight and
the moment equality; strict reduced costs force support in {1,...,j,b+1}.
These equations plus normalization uniquely determine all probabilities.
For j=1 there are no prefix rows, but the other conditions still give
uniqueness. At r=1, cost optimality restricts support to t>=b+1 and the
moment bound forces t=b+1; for r>1 uniqueness is not claimed.

## Number of pieces and sharpness

Let V_j be the affine value expression on segment j. Its r slope is

    s_j=sum_{i<j}d_i z_i-lambda_j(b+C_{j-1}).

Then s_{j+1}-s_j=-(b+C_j)/(2b)<0; s_1=-(b-1)/2<0 while the final
plateau has slope zero. Therefore every interval gives a distinct affine
piece and there are exactly b+1 pieces on R>=rho_b.

In the first open segment r_b<r<r_{b-1}, all b+1 probabilities
f_1,...,f_b,f_{b+1} are positive and the optimum is unique. Hence the
general b+1 total-support and two-tail-day bounds are simultaneously
necessary for every b, with a natural uniform forecast. This is an
explicit lower family, beyond a generic basic-feasible-solution bound.

Example b=3, R=29/20, uniform p: candidate optimum
(f1,f2,f3,f4)=(18,27,24,11)/80, mu=27/20, J=221/80;
lambda=2/3, alpha=4, (y1,y2)=(5/12,1/6). All four support days are
necessary. Breakpoints in R are 27/19,3/2,5/3,2, with respective values
54/19,21/8,7/3,2. Check all algebra and uniqueness independently.

## Required attacks

Check b=2, both endpoint choices at every breakpoint, r=r*, r=1, r>1,
interval interior, all-prefix and empty-prefix cases, nonnegative tail,
global dual signs and moment equalities. Compare with the old exact
optimizer and independent direct certificate checks. Search whether a
uniform-forecast frontier/sharp b+1 family already occurs in classical,
distribution-advice, moment-constrained or DRO ski-rental work before
claiming a new contribution. If it is known, credit it and reassess scope.
