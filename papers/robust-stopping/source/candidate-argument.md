# Unaccepted parent seed: backward prefix optimization and two dual prices

This is a proof/algorithm candidate to attack, not acceptance or a novelty claim.
The triage counterexample already isolates a conceptual expected-cost versus
support-threshold error. A potentially substantive repair is the structure below,
not another implementation counterexample or merely an infinite LP restatement.
Parent has not yet implemented or independently refereed this route.

## 1. A linear optimization oracle for the relaxed prefix polytope

Write A=R-1>0, L=b-1. Ignore total probability and the tail moment temporarily.
Let P(A) be the bounded polytope of nonnegative prefix masses f_1,...,f_L with

    sum_{j<=i}(b+j-1-i)*f_j <= A*i,  i=1,...,L.

For any feasible prefix through i-1, its next upper bound is

    0<=f_i<=U_i(f_<i)=[A*i-sum_{j<i}(b+j-1-i)*f_j]/(b-1).

Crucially the numerator is always positive: using the preceding constraint it
is at least A+sum_{j<i}f_j. Thus every feasible prefix extends, and there is
no hidden backward feasibility constraint. P(A) is a triangular deformed box.

To minimize ANY linear form sum_i w_i*f_i over P(A), eliminate i=L,...,1:

    if current w_i>=0: choose f_i=0;
    if current w_i<0: choose f_i=U_i, add w_i*A*i/(b-1) to the constant,
       and update w_j <- w_j-w_i*(b+j-1-i)/(b-1) for every j<i.

After recording the zero/upper choices, reconstruct f FORWARDS by U_i.
Backward induction proves exact optimality because the eliminated variable's
feasible interval is exactly [0,U_i] for every feasible earlier prefix. Ties
can choose either endpoint. Cost O(b^2) rational operations, polynomial bit
growth by the triangular recurrence. Every vertex corresponds to zero/upper
choices; verify completeness (induction on deformed-box vertices).
This oracle is a concrete structural step beyond restating the original LP.

An O(b) arithmetic implementation seems immediate and should be independently
checked: maintain global affine corrections U,V, initially0. At index i use
`w_i=current_input_w_i+U*i+V`. If negative, update
`U <- U-w_i/(b-1)`, `V <- V-w_i*(b-1-i)/(b-1)` and
`constant <- constant+w_i*A*i/(b-1)`. These exactly aggregate the updates to
every unprocessed j<i. Reconstruct forwards with prefix mass F and moment M:
`f_i=(A*i-(b-i)*F-M)/(b-1)` on upper choices, otherwise0;
then `F+=f_i`, `M+=(i-1)*f_i`. Each phase uses constant work per day.
This does not by itself make runtime polynomial in log(b) or avoid the
output-bit issue noted below.

## 2. Tail reduction and two-dimensional dual

The correct routine dominance reduction leaves tail candidates

    T={b} union {d+1: p_d>0 and d>=b},

with duplicates removed. Between forecast support points, g_t+lambda*(t-1)
is nondecreasing for lambda>=0, so only left endpoints matter. If N<b, only
b is needed in the tail. Full support can always be truncated at max(b,N+1),
not at N+1 when N+1<b. Credit these elementary support reductions as such.

Dualize total probability with free price nu and the mean constraint with
lambda>=0. Define

    Psi(nu,lambda)=min_{f in P(A)} sum_{i<b}(g_i+lambda*(i-1)-nu)*f_i.

The full optimum is the maximum, over lambda>=0 and
nu<=min_{t in T}(g_t+lambda*(t-1)), of

    nu-lambda*A*b+Psi(nu,lambda).                     (D)

The prefix minimum and a supporting plane are supplied by the explicit
backward oracle. The tail minimum is a lower hull on points (t-1,g_t),
preprocessed from the forecast. This is a concave polyhedral problem in TWO
dual prices (three dimensions if its value is a variable), not a single raw
cost threshold. Prove strong duality from the finite support reduction.
With a rational coefficient bound supplied by the prefix recurrence, standard
exact separation/optimization (GLS/ellipsoid, with proper primary citation)
should give an exact weakly polynomial algorithm. An oracle alone is not a
bit-complexity proof: establish bounds/attainment, dual box or equivalent
rational LP argument, and primal recovery. O(poly(b,input bits)) may be
pseudopolynomial in a binary-encoded huge b; state this honestly. Exact
geometric probabilities themselves can have Omega(b log b) output bits.

## 3. At most three canonical pieces and usable certificates

Let v range over the zero/upper prefix vertices. Write a prefix in P(A) as
sum_v z_v*v, with z_v>=0 and sum z_v=1. Add nonnegative tail atom variables
y_t. The master problem has only these three resource rows:

    sum z_v=1,
    sum z_v*mass(v)+sum y_t=1,
    sum z_v*moment(v)+sum (t-1)*y_t<=A*b.

A basic optimum therefore uses at most THREE nonzero pieces in total
(including a moment slack if present): prefix vertices and tail atoms.
At least one prefix vertex is present, so at most two tail atoms are needed.
The resulting policy has at most b+1 distinct buy days. Prefix vertices can
have total mass above1; they are canonical schedules, not individually
normalized robust policies. Do not falsely call their mixture a mixture of
probability policies. Standard column-generation/primal-recovery or a direct
Caratheodory argument still needs an algorithmic proof.

A certificate is: prices (nu,lambda); <=3 pieces and weights; primal norm,
moment and prefix feasibility; each used prefix minimizes the oracle's linear
form; each used tail has g_t+lambda(t-1)=nu; complementary slackness for the
moment. Its objective equals (D), proving optimality against ALL horizons.
This offers a concrete repaired characterization even if a very fast
strongly polynomial two-price solver is outside the final claim.

## 4. Optional exact b=2 geometry

For b=2, feasibility is precisely f_1<=A and E(T-1)<=2A. Let phi(x) be the
lower convex hull cost of tail days t>=2 with mean coordinate t-1 at most x.
For z=f_1, the objective reduces to

    2*z+(1-z)*phi(2*A/(1-z)),

over 0<=z<=min(A,1), with feasible tail mean and the z=1 endpoint separately.
This perspective is piecewise linear in u=1-z; minimize at its interval
endpoints/hull breakpoints. It gives an O(N log N) exact special-case solver
and support of at most three days. Alone this special case may be too modest;
prefer the general backward-oracle/dual structure if valid and useful.

Source-compatible conceptual check: b=2,R=7/5,p_1=9/10,p_3=1/10 has
g=(2,6/5,13/10,6/5,...). Policy f_1=1/5,f_2=4/5 is feasible with cost34/25;
earliest-maximal f_1=2/5,f_2=3/5 has cost38/25. The triage b=3 separation
is already stronger than this preliminary illustration. Do not conflate
failure of a raw support threshold with failure of every possible adjusted
water-filling rule, or claim a novel general LP principle.

## 5. Possible compression (unproved, optional)

Under forecast costs, the current backward coefficients within each forecast
segment remain affine w(j)=alpha*j+beta with alpha>=0, since every negative
elimination adds a nonnegative slope. If w_i<0 at an active endpoint, the
updated slope is alpha'=alpha-w_i/(b-1)>0, and the next coefficient is
w'_{i-1}=-alpha'. Subsequent consecutive active eliminations have geometric
slope growth b/(b-1). This may batch whole segments, but exact sign handling,
intercept/constant formulas and bit complexity remain to prove. Do not add
the compressed algorithm to the claim without checking it.

All novelty, substantive value and algorithmic assertions require your fresh
research and referee checks. Do not manufacture a paper if this is only an
obvious consequence already stated in closest primary work.
