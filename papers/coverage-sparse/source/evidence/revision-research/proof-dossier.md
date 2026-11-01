# Revised mathematical claim: complete proof dossier for a fresh referee

Proposer job: `coverage-sparse-research-357cde21e920`.
This dossier includes the original resolution and every mathematical addition
proposed for the first-paper revision. It is research evidence, not a new
manuscript or a referee verdict. The old acceptance does not cover this scope.

## R0. Exact interpretation and dependency ledger

Use the finite ground sets, exact marginals, nonnegative weighted coverage
functions, equality-tested graph model and upper-tested graph model defined in
`source.md` and `problem.md`. The original source is unchanged. All ratios have
positive numerator. A graph of tested pairs imposes no restrictions on nonedges.
Write C_k={G:chi(G)<=k}, B_k={G:Delta(G)<=k-1}, and
alpha_j=1-(1-1/j)^j for every positive integer j.

For the additional heterogeneous model, an edge ij has the upper constraint
P(i,j in S)<=x_i x_j+e_ij, with a specified finite real e_ij>=0. All marginal
constraints remain equalities. The product law is feasible. Compactness of the
finite probability simplex guarantees every maximum used here exists. Positive
coverage numerator implies a positive product expectation, so denominators are
positive. Empty features and zero weights cause no exception.

Dependencies are finite probability, AM-GM, concavity, greedy coloring,
geometric sums, and log(1+u)<=u. None of the mathematical conclusions depends
on a numerical optimizer, an earlier acceptance flag, or a new model context.
R1--R3 resolve the original source question. R4--R7 are revision additions;
R8 spells out the sampling implication already contained in R1. The infinite
statements below have analytic proofs. R6 also uses a complete, displayed,
finite rational certificate; its computational checks are independently
reproducible by `verify_revision.py`.

## R1. Color resampling: a feasible denominator lower bound

Let V=C_1 disjoint-union ... disjoint-union C_k be a proper coloring, with
empty classes allowed. Given any law D with marginals x, sample k independent
sets S_1,...,S_k from D and return R=union_c(S_c intersect C_c). A vertex
retains its marginal, and an edge joins different classes, hence its endpoints
have joint probability x_i x_j. Thus R is feasible for equality, multiplicative
upper errors delta>=0, and heterogeneous nonnegative upper errors.

For a feature H set a_c=P_D(S hits H intersect C_c), s=sum_c a_c, and
b=P_D(S hits H). Then b<=min(1,s). Independent sampling and AM-GM give

    P(R hits H)=1-product_c(1-a_c)>=h(s)=1-(1-s/k)^k.

For k>=2, h is increasing and concave on [0,k], with h(0)=0 and
h(1)=alpha_k. On [0,1], concavity gives h(s)>=alpha_k s; on [1,k],
monotonicity gives h(s)>=alpha_k. Therefore P(R hits H)>=alpha_k b.
Summing with nonnegative feature weights proves E f(R)>=alpha_k E_D f(S).
Apply this to a law attaining f^+(x). In particular,

    f_G^=(x)>=alpha_k f^+(x).

For k=1 there are no tested edges and all the relevant denominators equal
f^+(x), so all original ratios are one. For maximum degree at most k-1,
greedy coloring gives a proper k-coloring. No restriction on within-class
joint dependence was used.

The two-group coverage resampling calculation is a prior ingredient of
Dütting et al.; this k-group extension is elementary. The constant alpha_k
itself is also classical. The tightness under only within-block tested pairs
is the separate issue addressed next.

## R2. Normalized witness and pointwise collision certificate

Fix integers k>=2 and m>=1. Let B_1,...,B_m be disjoint k-vertex cliques and
G their union. For each transversal H containing one vertex from each block,
use coverage weight k^(-m). There are exactly k^m such features. For any S,
write a_r=|S intersect B_r|, T=sum_r a_r, C=sum_r binom(a_r,2). Counting
missed transversals gives

    f(S)=1-product_r(1-a_r/k).                         (R2.1)

Thus f(empty)=0, f(V)=1 and 0<=f(S)<=1; this is the meaning of normalized
here. The value can be evaluated from block counts in O(n+m) elementary
operations even though its explicit feature list has size k^m. This is an
arithmetic-operation statement, not a claim of constant bit cost for exact
large rationals.

Set x_i=1/m. Selecting one whole block uniformly preserves these marginals
and hits every transversal. Consequently f^+(x)=1. The graph has n=mk
vertices, chi(G)=k, Delta(G)=k-1, and |E|=m binom(k,2)=n(k-1)/2.
The coverage family is the equal-block normalization of Ramachandra (2026),
Section 4; it is not a new construction.

For q=1-1/k and every integer 0<=a<=k,

    0<=q^a-(1-a/k)<=binom(a,2)/k^2.                  (R2.2)

To prove this, let d_a=q^a-1+a/k. Then d_0=0 and
 d_(a+1)-d_a=(1/k)(1-q^a), which is between zero and a/k^2 by the geometric
sum identity. Sum these increments. In particular, for each block,
0<=A_r=1-a_r/k<=Q_r=q^(a_r)<=1. The telescoping identity for the two
products gives product_r Q_r-product_r A_r<=sum_r(Q_r-A_r)<=C/k^2.
Using (R2.1),

    f(S)<=1-q^T+C/k^2.

Let beta_k=q^k/k. Successive differences of g(t)=1-q^t are q^t/k.
For integer t>=k, summing from k to t-1 bounds each difference above by
beta_k. For t<k, summing from t to k-1 bounds each difference below by
beta_k, and rearranging gives the same supporting-line inequality. Hence,
for every integer t>=0, g(t)<=alpha_k+beta_k(t-k), and for every subset S,

    f(S)<=alpha_k+beta_k(T-k)+C/k^2.                 (R2.3)

This rational pointwise dual uses only the within-clique collision count.
It makes the sparse-information obstacle concrete: the unrestricted
whole-block law has C=binom(k,2), whereas exact tested moments force
E C=binom(k,2)/m.

Under the heterogeneous constraints, E T=k and

    E C<=m binom(k,2)/m^2+sum_{ij in E}e_ij.

Average (R2.3), using its nonnegative collision coefficient and f<=1, to get

    alpha_k<=f_{G,e}^up(x)
      <=min{1,alpha_k+(k-1)/(2km)+(1/k^2)sum_{ij in E}e_ij}.   (R2.4)

The lower bound follows from R1, or from inclusion of equality-feasible
laws. This proves the heterogeneous assertion for every nonnegative finite
real edge budget, without a uniformity or rationality assumption.

For uniform additive errors e_ij=epsilon>=0 this becomes

    alpha_k<=f_{G,epsilon}^add(x)
      <=min{1,alpha_k+(k-1)/(2k)(1/m+m epsilon)}.       (R2.5)

For multiplicative errors e_ij=delta/m^2 with delta>=0 it becomes

    alpha_k<=f_{G,delta}^up(x)
      <=min{1,alpha_k+(1+delta)(k-1)/(2km)}.           (R2.6)

Equality-feasible laws are a subset of upper-feasible laws with delta=0,
so the equality upper bound follows from (R2.6) with delta=0. When m=1,
x_i=1 forces S=V, so all these denominators are exactly one; the bounds
remain valid. This handles this endpoint separately from limiting claims.

## R3. Four class suprema by inclusion

For any fixed finite delta>=0, equality-feasible laws are upper-feasible,
so on every instance the upper-model ratio is at most the equality ratio.
Also B_k is contained in C_k. The two intermediate class suprema are each
between Gamma_up_delta(B_k) and Gamma_eq(C_k): explicitly,

    Gamma_up_delta(B_k)<=Gamma_eq(B_k)<=Gamma_eq(C_k)<=1/alpha_k,
    Gamma_up_delta(B_k)<=Gamma_up_delta(C_k)<=Gamma_eq(C_k)<=1/alpha_k.

For each fixed k>=2 and delta, the witness (R2.6) gives
Gamma_up_delta(B_k)>=1/[alpha_k+(1+delta)(k-1)/(2km)] for every integer
m>=1. Let m tend to infinity, keeping k and delta fixed. The endpoints of
both chains coincide at 1/alpha_k. Thus all four class suprema equal that
value. The k=1 endpoint was handled in R1. These are class suprema over
all finite instances, including all finite feature lists and marginals.

## R4. Growing-error consequences and absolute scales

Fix an integer k>=2. For any sequence of finite nonnegative real errors
(delta_m) with delta_m/m->0, (R2.6) and its alpha_k lower bound imply
f_{G_m,delta_m}^up(x^(m))->alpha_k and the witness ratios tend to 1/alpha_k.
For uniform additive errors epsilon_m>=0 with m epsilon_m->0, (R2.5)
gives the same conclusion. More generally, the sufficient heterogeneous
condition is sum_{ij in E(G_m)}e_ij^(m)->0 for fixed k.

The multiplicative tolerance on an individual edge is delta_m/m^2 in
absolute probability units. For fixed delta this is O(m^(-2)); even when
delta_m=o(m) it is o(1/m). There are m binom(k,2) tested edges. This
explains why the aggregate error is controlled. These are deterministic
moment constraints and do not supply a sample-complexity theorem.

## R5. Exact finite matching witness and sharp transition

For k=2, m>=2 define two laws, both with every vertex marginal 1/m.
Type A chooses an unordered pair of distinct blocks uniformly and,
independently, one uniform vertex in each chosen block. Each vertex is
included with probability (2/m)(1/2)=1/m, no tested edge is doubly active,
and coverage is 1-(1-1/2)^2=3/4. Type B chooses one whole block uniformly;
it has the same marginals, every tested edge has double-activation
probability 1/m, and coverage is one.

Mix type B with probability t and type A with probability 1-t. Each edge
moment is t/m and its coverage expectation is 3/4+t/4. With

    t=min{1,(1+delta)/m},

this law is multiplicative-upper feasible. Bound (R2.6), capped by one,
coincides with its value. Therefore for every integer m>=1 and every
finite real delta>=0,

    f_{G,delta}^up(x)=3/4+(1/4)min{1,(1+delta)/m}.     (R5.1)

For equality use t=1/m: every tested edge moment is exactly 1/m^2.
The upper bound from the delta=0 model then proves

    f_G^=(x)=3/4+1/(4m),     f^+(x)/f_G^=(x)=4m/(3m+1). (R5.2)

For uniform additive tolerance epsilon>=0, choose instead
 t=min{1,1/m+m epsilon}. Comparing with (R2.5) proves

    f_{G,epsilon}^add(x)=3/4+(1/4)min{1,1/m+m epsilon}. (R5.3)

For m=1 every vertex is forced present, giving value one in all models;
(R5.1)--(R5.3) have that same value. No type-A law is needed in that case.

Let m tend to infinity. If m epsilon_m->c in [0,infinity], allowing
c=infinity, continuity of min(1,u) on the extended nonnegative half-line
in (R5.3) gives denominator limit 3/4+(1/4)min{1,c} and ratio limit
4/[3+min{1,c}]. The same limits hold in (R5.1) if delta_m/m->c.
In particular, for arbitrary nonnegative sequences, the matching
witness denominator tends to 3/4 if and only if m epsilon_m->0
(additive), or delta_m/m->0 (multiplicative). Necessity follows because
min(1,u_m)->0 forces u_m->0 for u_m>=0. These necessity assertions
classify this specified witness family, not arbitrary graphs, marginals,
or coverage objectives. Above the saturation scale the ratio tends to one.

## R6. Exact finite LP values, with complete certificates

A profile a is the nondecreasing rearrangement of the m block occupancies.
Averaging any feasible law under permutations of blocks and independent
permutations of vertices inside blocks preserves its objective and all
uniform constraints. The group is transitive on vertices and on tested
edges. A symmetric law is a mixture of uniform subset-orbits for profiles.
For such a law an individual marginal is E T/(mk), and an individual
edge moment is E C/[m binom(k,2)]. Thus the profile constraints are
E T=k, E C=k(k-1)/(2m) for equality, or E C at most (1+delta) times
that quantity for the upper model. Every profile mixture satisfying
these aggregate constraints lifts to an individually feasible law.
Conversely, group averaging supplies the profile reduction for every law.

The following primal mixtures use uniform orbits. An omitted profile has
zero mass. The dual is the pointwise inequality f(S)<=y0+yT*T+yC*C.
For the upper model yC>=0, as required for averaging an upper constraint.

| k,m | model | primal profiles and masses | (y0,yT,yC) | optimum |
|---|---|---|---|---|
| 2,2 | equality | (0,2):1/2; (1,1):1/2 | (1/4,1/4,1/4) | 7/8 |
| 2,3 | equality | (0,0,2):1/3; (0,1,1):2/3 | (1/4,1/4,1/4) | 5/6 |
| 3,2 | equality | (0,3):1/4; (1,2):3/4 | (1/3,1/9,1/9) | 5/6 |
| 3,3 | equality | (0,0,3):1/3; (1,1,1):2/3 | (8/27,11/81,8/81) | 65/81 |
| 3,3 | upper, delta=1 | (0,0,3):2/3; (1,1,1):1/3 | (8/27,11/81,8/81) | 73/81 |

All masses sum to one. In each row E T=k and E C is the stated target
or upper cap. Thus the primal feasibility follows by the orbit-lift
argument, and its objective equals the displayed rational optimum.
For k=2 the dual also follows directly: with C=0, all occupied blocks
are singletons, and f=1-2^(-T)<=1/4+T/4 for integers T>=0. At T=0,1,2
check directly; at T>=3 the right side is at least one. If C>=1, a full
block is present, f=1 and T>=2, so 1/4+T/4+C/4>=1.
For k=3,m=2, direct substitution gives the following exhaustive slacks:

| profile | (0,0) | (0,1) | (0,2) | (0,3) | (1,1) | (1,2) | (1,3) | (2,2) | (2,3) | (3,3) |
|---|---|---|---|---|---|---|---|---|---|---|
| dual minus f | 1/3 | 1/9 | 0 | 0 | 0 | 0 | 1/9 | 1/9 | 1/3 | 2/3 |

For k=m=3 the 20 profiles below are exhaustive. Each expression depends
only on the sorted occupancies, so this table covers all 4^3 occupancy
vectors and all 2^9=512 labeled subsets. The last column is the exact
slack for y=(8/27,11/81,8/81).

| profile | slack | profile | slack |
|---|---|---|---|
| (0,0,0) | 8/27 | (1,1,1) | 0 |
| (0,0,1) | 8/81 | (1,1,2) | 7/81 |
| (0,0,2) | 0 | (1,1,3) | 22/81 |
| (0,0,3) | 0 | (1,2,2) | 20/81 |
| (0,1,1) | 1/81 | (1,2,3) | 41/81 |
| (0,1,2) | 2/81 | (1,3,3) | 68/81 |
| (0,1,3) | 11/81 | (2,2,2) | 4/9 |
| (0,2,2) | 4/27 | (2,2,3) | 20/27 |
| (0,2,3) | 10/27 | (2,3,3) | 29/27 |
| (0,3,3) | 19/27 | (3,3,3) | 38/27 |

Averaging gives 8/27+3*(11/81)+1*(8/81)=65/81 in equality,
and at most 8/27+3*(11/81)+2*(8/81)=73/81 for delta=1.
For the latter primal, type (1,1,1) has coverage 19/27 and type (0,0,3)
has coverage one, so its value is (1/3)(19/27)+2/3=73/81.
Every individual edge moment is 2/9; each vertex marginal is 1/3.
Weak duality plus the matching primal proves exact optimality; an LP
solver's success status is unnecessary.

`finite-certificates.json` serializes all five inputs and certificates.
`discover_finite.py` obtained them by exact rational profile enumeration.
The separate `verify_revision.py` imports neither that solver nor its
functions: it reconstructs orbit laws on labeled subsets and verifies
normalization, every individual marginal, every tested pair, objective,
and every pointwise dual inequality with fractions.Fraction.

## R7. Finite all-pairs and full t-wise hierarchy

For the same witness let f_t(x) be the maximum expectation over laws with
the given marginals whose indicator variables are jointly independent on
every subfamily of at most t vertices, with 2<=t<=n=mk. The product law
is feasible for every t. Each transversal feature consists of m distinct
vertices, each with marginal 1/m. Under the product law its hit probability
is alpha_m, and by normalized feature weights the expected coverage is
exactly alpha_m. This expectation depends on m, not k.

Every t-wise law in this range satisfies all pair equalities, in particular
all within-clique equalities. Constraint inclusion and R2 therefore give

    alpha_m<=f_t(x)<=min{1,U_(k,m)},
    U_(k,m)=alpha_k+(k-1)/(2km),
    1/U_(k,m)<=f^+(x)/f_t(x)<=1/alpha_m.              (R7.1)

One may improve the lower ratio bound to max{1,1/U_(k,m)}. No color-law
lower bound alpha_k is imposed on f_t: a color-resampled law may fail the
additional cross-block constraints. As an exact check of the tempting
wrong shortcut, at k=2,m=3 the mutually independent expectation is
19/27<3/4=alpha_2. In the t=n model the product law is the only feasible
law, so this is also a counterexample to a universal alpha_k lower bound
for the full hierarchy. For m=1 all values equal one.

Write a=1-1/e. For every j>=2, log(1-1/j)<=-1/j gives alpha_j>=a.
Also (1-1/j)^(j-1)=(1+1/(j-1))^(-(j-1))>=e^(-1) by
log(1+u)<=u. Multiplication by 1-1/j gives
alpha_j<=a+1/(e*j)<=a+1/j. Thus for k,m>=2 and every t in the range,

    0<=e/(e-1)-f^+(x)/f_t(x)
      <=(1/k+1/(2m))/(1-1/e)^2.                     (R7.2)

Indeed the ratio is at most 1/alpha_m<=1/a, and is at least 1/U;
1/a-1/U=(U-a)/(a*U)<= (1/k+1/(2m))/a^2 since U>=alpha_k>=a.
Consequently for any k_l,m_l tending to infinity, and ANY choices
2<=t_l<=k_l*m_l, the ratios tend uniformly to e/(e-1).
For k=m=s>=2, n=s^2 and the error in (R7.2) is at most
3/[2*(1-1/e)^2*sqrt(n)]. This is a square-size subsequence assertion.

Ramachandra (2026), Theorem 2 and Section 4, already proves the asymptotic
pairwise result using this Cartesian family and notes the t-wise
consequence. The contribution of R7 is this short explicit finite
sandwich and rate inherited from the sparse certificate; the limiting
value and family receive prior attribution.

## R8. Sampling implication and remaining mathematical boundaries

R1 is a concrete sampling conversion: given a proper k-coloring and sampler
access to ANY law D, k independent sampler calls and O(k*|V|) elementary
membership operations produce exact tested-edge moments and expected
coverage at least alpha_k E_D f. Its guarantee is simultaneous over all
nonnegative weighted coverage functions. It does not require evaluating
or explicitly listing the features. This is a reduction given a sampler,
not an algorithm for finding the maximizing law of f^+.

The newly proved exact matching statement concerns this witness with
uniform marginals and Cartesian coverage. A general fixed-graph formula,
fractional-coloring refinement, triangle-free high-chromatic case,
arbitrary monotone-submodular extension, and necessary tested-pair budget
are unresolved in this project. No conjecture about these is asserted as
a theorem. The known family and elementary resampling ingredient limit
the contribution size; no conference suitability guarantee follows.

## Verification and handoff

Run from PROJECT_DIR:

    python3 evidence/revision-research/verify_revision.py

Expected values are 7/8, 5/6, 5/6, 65/81 and 73/81. The saved output
reports the exact finite domains: 137 matching error cases with m=1..12;
11,397 sorted occupancy profiles for k=2..8,m=1..6; local inequalities
for k=2..40; and 11 full-product enumerations with n<=12. These tests are
supplementary. The analytic arguments, displayed full finite certificates,
and their completeness reductions are the decisive evidence.

Known mathematical gaps in the exact stated candidate: none found by this
researcher. Fresh mathematical review remains required. No agents,
background workers, formal proof assistant, external contact or manuscript
revision were used in this bounded job. AI assistance derived and checked
these arguments; this same-context verification is not an independent
referee. Literature comparisons and limitations are in literature-review.md.
