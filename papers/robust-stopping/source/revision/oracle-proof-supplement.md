# Supplement to the earlier optimizer: elimination, bits, and LP comparison

Research job robust-stopping-research-cd75b220d422. The earlier evidence is
retained unchanged. This supplement makes two steps explicit, corrects the
terminology requested by the reviewer, and scopes the revised algorithm to
pure bisection. It requires a new freeze and fresh mathematical referee.

## Complete backward-elimination optimality argument

Let a=b-1 and P(r) consist of z>=0 with
 sum_{j<=i}(a+j-i)z_j<=ri, 1<=i<=a.
For every feasible partial prefix through i-1, its possible ith coordinate
is the interval [0,U_i],
 U_i=[ri-sum_{j<i}(a+j-i)z_j]/a.
For i=1 the numerator is r. For i>1 it is at least
r+sum_{j<i}z_j>0 by the preceding prefix row. Setting future coordinates
to zero keeps future rows feasible: the left side decreases with the row
index and the right side increases. Thus this interval describes all
extensions, not merely a necessary bound.

For an arbitrary linear form w*z, eliminate i=a,a-1,...,1. At a given
stage all later coordinates have been minimized out, leaving an affine
function of the remaining prefix. If its current coefficient w_i>=0,
its exact minimum on [0,U_i] is obtained at zero; if w_i<0 it is obtained
at U_i. In the second case substitution adds the constant w_i*r*i/a and
changes the earlier coefficient w_j to w_j-w_i*(a+j-i)/a. This equality
of value functions holds for every feasible preceding prefix, so induction
proves global optimality. Reconstructing the recorded zero/upper choices
forward gives an attaining feasible prefix. A zero coefficient admits both
endpoints and every point between, without changing the value.

For w_i=c_i-alpha, introduce y_i as minus the current negative coefficient
divided by a, or zero otherwise. The substitution gives exactly

 y_i=max(0,[alpha-c_i-sum_{j>i}(a+i-j)y_j]/a).

The accumulated value is -r sum_i i*y_i. Equivalently each early variable
has nonnegative reduced cost c_i-alpha+sum_{j>=i}(a+i-j)y_j. On upper
choices its row is tight, and on a positive reduced-cost choice its mass
is zero. Taking the finite sum of these equalities proves primal-dual
equality. This supplies a direct proof of the recurrence's optimality,
without assuming a general greedy or LP claim.

## Intermediate bit lengths: an explicit common-denominator argument

Fix any set B of active prefix rows, with k<=a. Express each active dual
coordinate as y_i=u_i*alpha+v_i, solving backward with zero outside B.
The triangular matrix has diagonal a and upper entries between 1 and a.
Let Q be a common denominator for the original costs c_i and let
 M=max(1,max_i |c_i|).
The recurrence shows that the denominators of u_i divide a^k and those of
v_i divide Q*a^k. Indeed every substitution divides once by a and the
maximum path length is k. Normalized off-diagonal coefficients have
absolute value at most one. Backward induction on the sum of remaining
absolute values therefore gives

 |u_i|<=2^k,  |v_i|<=2^k*M.

Every inactive reduced slack is an affine function U_i*alpha+V_i with
U_i denominator dividing a^k and V_i denominator dividing Q*a^k, and

 |U_i|<=1+a*k*2^k,
 |V_i|<=M*(1+a*k*2^k).

The activation-sweep positivity argument in the earlier proof gives
U_i<0 for every inactive row. A root -V_i/U_i is a ratio whose numerator
and denominator, after using these common denominators, are bounded by
 Q*a^k*(1+a*k*2^k)*max(1,M).
Consequently its bit length is O(log Q+log M+b log b). This is a bound in
the *original current input costs*. Each new active set defines its own
such affine system, so the bound is independent of the representation of
previous activation roots. Evaluating the y_i, slacks and slopes at any
root only adds quantities of this bounded length. Intermediate suffix
sums share the same denominators; their numerators have only O(log b)
additional bits. No iterative nesting of root-denominator bounds is needed.

A canonical primal prefix v(B) has common denominator dividing
q_R*a^a; its entries come from the recurrence
 v_{s_j}=(s_j-s_{j-1})(r+F_{j-1})/a.
The growth factor per event is at most 2, so its magnitude is bounded by
O((1+|r|)*2^a). Thus its numerator bits are
O(len(R)+b log b). Normalization takes one ratio of differences of these
masses and one convex combination, preserving a polynomial bound.

For the price search, input forecast coefficients share denominator q_p,
the lcm of probability denominators. Each adjusted cost
c_t=g(t)+lambda*(t-1) shares a denominator dividing q_p*den(lambda).
The original isolation argument bounds Z=2 L H^4, where
 D=b!*b^b, H=q_p*q_R*D, L=b+max S.
In pure bisection on [0,Z+1], after k iterations the price denominator
is at most 2^k and numerator at most (Z+1)*2^k. Here k=O(log Z), and
log Z=O(ell+b log b), where ell is the binary input length. Hence the
adjusted costs have log Q+log M polynomial in b and ell, uniformly over
all calls. Final endpoint-policy intersection, moment interpolation and
dual reconstruction use a constant number of ratios, products and sums
of polynomial-length rationals. Standard reduced rational arithmetic has
polynomial bit cost for these operations. Canonical schedules and suffix
sums have the explicit common-denominator bounds above, so intermediate
values, not merely returned outputs, are covered.

## Revised algorithm scope and terminology

Use the existing `evidence/prefix_oracle.py` with
`optimize(b,R,p,max_chord_probes=0)`. This disables the optional eight-chord
accelerator; only the proved bisection and final exact line-intersection
recovery remain in the revised main algorithm. Old code and old snapshots
are preserved. This restriction does not change its proof, value, support
bound or certificate. New saved executions are in
`revision/pure-bisection-checks.json`.

After forecast preprocessing, O(log Z) is the **number of oracle calls**.
Each oracle takes O(b^2+|S|) rational arithmetic operations. Therefore
O((b^2+|S|)*(ell+b log b)) is a **total arithmetic-operation bound**, not
an oracle-call bound. Bit running time is polynomial in numerical b and
ell. No strongly polynomial claim or generic-LP speed advantage is made.

The finite reduction already yields an explicit LP with O(b+|supp p|)
variables, b-1 early prefix rows, normalization and one moment row. Generic
polynomial-time LP algorithms already imply polynomial bit time in b and
ell; the earlier existence/complexity statement alone is not an improved
complexity guarantee. Moreover the moment coefficient is t-1, and t can
be a large encoded forecast horizon plus one. The whole constraint matrix
is not bounded by b, even though its prefix block is. This corrects the
review's stated matrix bound without claiming an advantage over Tardos.
The revised contribution is an explicit certifying construction plus the
complete uniform frontier and matching support-necessity family. The
uniform theorem has exact structural content absent from an LP existence
statement; whether it is enough for a particular venue is not a theorem.
