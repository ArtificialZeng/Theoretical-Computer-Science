# Fresh mathematical referee report

**Verdict: accept the complete frozen candidate.**

Referee job: `coverage-sparse-referee-20ee9a6fefc3`.
Snapshot digest: `639fb67b280db040c9a3c5059288d96a35e8cb02d493e698aaf573087cfca4e8`.
Candidate: `resolution-paper`, original status `proved`.

This report covers the exact statement in the frozen `claim.json`, including
all revision additions. It does not inherit an earlier acceptance. I read the
original statement, its precise interpretation, the snapshot, and its listed
evidence and relevant primary-source statements. I did not read the owner's
checkpoint/state, prior verdicts, earlier job transcripts, progress summaries,
historical drafts, or earlier audits. No agents or other model processes were
used. This is a fresh model-context mathematical review, not external peer
review or a claim of statistical independence.

## 1. Scope and input integrity

All 23 frozen files (claim plus its listed evidence) were rehashed successfully
before and after the fresh computation. The canonical mapping digest matches
the snapshot. `source.md` retains SHA-256
`eb7061a17cead0bc8cc0e4426f3f8260ac3137dd23b6f4813d8f4952b00ec731`.
No frozen input was edited, and the submitted verifier was not run because its
normal execution would overwrite a frozen output file.

The accepted scope comprises:

* All four coverage class suprema, for every integer k >= 1, for chi(G) <= k
  and Delta(G) <= k-1, with equality moments or the stated fixed finite
  nonnegative multiplicative upper errors.
* The normalized Cartesian witness's finite heterogeneous-error certificate,
  uniform additive and multiplicative specializations, and the stated
  sufficient growing-error regimes.
* The all-m exact matching-witness formulas, their equality ratio, the
  necessary-and-sufficient convergence scales for that witness, and the
  extended-real scaled-error limit formulas.
* All five exact finite optima with rational primal and dual certificates.
* The full t-wise finite sandwich, its uniform analytic rate and square-size
  subsequence, with the known limit and family attributed to prior work.
* The k-call sampler conversion given a proper coloring and access to a law.

Nothing in this acceptance replaces a failed part by a weaker contribution.
The original graph-class question is resolved at its stated coverage scope;
the acceptance also covers the added statements. A general fixed-graph formula,
arbitrary monotone-submodular extension, necessary edge-budget bound, and venue
suitability are not asserted in the candidate.

## 2. Reconstruction of the class upper bound

Partition V into k independent color classes C_c, including empty classes when
needed. Independently sample S_c from an arbitrary input law D and keep S_c
only on C_c. Each vertex retains its exact marginal. Edge endpoints belong to
different independent calls, so their joint inclusion probability is x_i*x_j.
Thus the converted law is feasible for equality moments, and for every stated
nonnegative upper error.

For a feature H, put a_c = P_D(S hits H intersect C_c), s = sum a_c, and
b = P_D(S hits H). The union bound gives b <= min(1,s). The output hits H
with probability 1-product(1-a_c), at least h(s)=1-(1-s/k)^k by AM-GM.
For k >= 2, h is increasing and concave on [0,k], and h(0)=0,
h(1)=alpha_k. On s <= 1 its chord gives h(s) >= alpha_k*s; on s >= 1
monotonicity gives h(s) >= alpha_k. Hence output hit probability is at least
alpha_k*b. Nonnegative feature weights allow summing this inequality for one
common output law, without choosing separate laws for individual features.

Apply the conversion to a maximizing marginal law to obtain
f_G^eq >= alpha_k*f^+. A finite maximum-degree-(k-1) graph has a proper
k-coloring by greedy coloring. For k=1 both graph classes have no edges and
the ratio is exactly one. The same construction proves the sampler assertion
using k independent calls; no procedure for finding an optimal input law is
implicitly assumed. Dependence inside a color class is unrestricted.

## 3. Independent reconstruction of sparse tightness and error bounds

Use m disjoint k-cliques, x_i=1/m, and all k^m transversal features with
weight k^(-m). For occupancies a_r, direct counting gives
f(S)=1-product_r(1-a_r/k). Uniform selection of one entire block has the
required marginals and coverage one, proving f^+=1. The normalization and
edge count m*binom(k,2)=n(k-1)/2 are exact. Evaluation from block counts does
not require listing all features.

Here is an independent way to check the key local collision inequality. For
Z distributed as Binomial(a,1/k),

    (1-1/k)^a - (1-a/k) = E[Z] - P(Z>=1)
                             = E[(Z-1)_+] <= E[binom(Z,2)]
                             = binom(a,2)/k^2.

This also proves nonnegativity. With q=1-1/k, T=sum a_r and
C=sum binom(a_r,2), telescoping products of factors in [0,1] yields

    f(S) <= 1-q^T+C/k^2.

Since T is bounded and g(t)=1-q^t is concave, Jensen gives
E[g(T)] <= g(E T)=g(k)=alpha_k. Equivalently, the dossier's rational
pointwise certificate follows from the discrete supporting line of slope
q^k/k at integer k. Its forward differences q^t/k decrease with t, so it
is valid on both sides of k, including T=0. There is no unproved limiting
exchange or assumption that the continuous tangent has that rational slope.

For heterogeneous errors, E C <= m*binom(k,2)/m^2 + sum_E e_ij.
Average the pointwise inequality to obtain

    f_G,e^up <= min{1, alpha_k+(k-1)/(2*k*m)+sum_E e_ij/k^2}.

The lower bound alpha_k follows from the conversion and f^+=1. Substitution
of e_ij=epsilon and e_ij=delta/m^2 gives exactly the claimed additive and
multiplicative formulas. Equality-feasible laws are upper-feasible at delta=0.
These arguments hold for arbitrary finite nonnegative real budgets, not just
rational test values.

On each instance, enlarging the feasible set lowers the ratio. Together with
B_k subset C_k, the smallest of the four class suprema is the upper-moment
one on B_k, and the largest is the equality-moment one on C_k. All are at most
1/alpha_k. For fixed k and finite delta, the witness gives a ratio at least
1/[alpha_k+(1+delta)(k-1)/(2*k*m)], tending to 1/alpha_k as m grows.
This proves all four equalities, including the direction that would not follow
merely by deleting constraints from an all-pairs example.

For fixed k, the same bounds squeeze the denominators to alpha_k when
delta_m/m -> 0 or m*epsilon_m -> 0. Multiplicative excess on one edge is
delta_m/m^2 in absolute probability units. No arbitrary growing-error or
sample-complexity assertion is needed.

## 4. Exact matching formulas and transition

For k=2,m>=2, independently reconstruct two marginal-preserving laws. Choosing
two distinct uniform blocks and one fair vertex per block gives zero edge
moments and value 3/4. Choosing one uniform full block gives edge moment 1/m
and value one. Both laws have each vertex marginal 1/m. Mixing the latter
with weight t gives edge moment t/m and value 3/4+t/4.

For multiplicative upper errors take t=min{1,(1+delta)/m}; for additive
errors take t=min{1,1/m+m*epsilon}. Their values meet the capped collision
upper bound. For equality take t=1/m, which satisfies each edge equality
exactly and meets its upper bound. This proves all three exact formulas and
the equality ratio 4m/(3m+1). At m=1 every vertex is forced present, giving
one in all models; the same formulas give one without invoking the
undefined two-distinct-block experiment.

The scaled-error limit statements follow directly from these exact formulas
and min{1,u}. For arbitrary nonnegative sequences, min{1,u_m}->0 forces
u_m->0, proving necessity as well as sufficiency for this witness. The
additional 1/m term vanishes; extended-real limit c=infinity gives saturation
at one. No necessity claim is made for arbitrary graph instances.

## 5. Five finite optima: fresh exact verification

The symmetry reduction is valid: permutations of blocks and independent
within-block vertex permutations preserve the uniform data, objective, and
constraints. The group is transitive separately on vertices and tested edges.
Uniform profile orbits therefore have marginal E T/(mk) and edge moment
E C/[m*binom(k,2)], and every listed primal mixture lifts to a feasible law.

I wrote and ran `audit/referee-20ee9a6fefc3-verify.py`, importing neither
submitted program. It explicitly lists transversal features and evaluates
their hit indicators on every labeled subset, reconstructs each primal law,
and checks normalization, every individual marginal, every tested pair,
objective, every pointwise dual constraint, and matching dual objective with
exact fractions. This verifies the product-count identity independently of
using it to evaluate the finite objective. Upper-model dual collision
coefficients were checked nonnegative.

| k,m | model | all labeled subsets checked | exact optimum |
|---|---|---:|---:|
| 2,2 | equality | 16 | 7/8 |
| 2,3 | equality | 64 | 5/6 |
| 3,2 | equality | 64 | 5/6 |
| 3,3 | equality | 512 | 65/81 |
| 3,3 | upper, delta=1 | 512 | 73/81 |

The rational primal and dual values coincide in every case. Thus exact
optimality follows from finite weak duality, with no reliance on a numerical
optimizer's status. The two 3,3 rows use all 20 profile orbits and all 512
labeled subsets in each model.

Additional fresh exact checks covered 558 local collision inequalities for
k=2..32; 3,193 integer supporting-line cases T=0..6k; 12,819 sorted profiles
for k=2..7,m=1..7; 292 equality/additive/multiplicative matching coupling
cases for m=1..20; 25 explicit law conversions on five vertices including
zero/one marginals and all 800 feature tests; and five full product-law
enumerations. Exact constants for k=2..6 were recomputed. All passed.
Their finite ranges supplement the analytic proofs; they are not extrapolated
into infinite-parameter results. Output is saved in
`audit/referee-20ee9a6fefc3-verification.json`.

## 6. Full t-wise hierarchy and analytic rate

For 2<=t<=n, product feasibility gives f_t>=alpha_m, because each feature
contains m independent Bernoulli(1/m) variables under the product law.
Every t-wise law satisfies every within-block pair equality; hence
f_t<=min{1,U}, U=alpha_k+(k-1)/(2*k*m). Since f^+=1, the claimed reciprocal
sandwich follows. The product expectation depends on m, not k. In particular
k=2,m=3,t=n=6 has value 19/27<3/4; the frozen candidate correctly avoids
the false alpha_k lower bound for this hierarchy.

Let a=1-1/e. For j>=2, logarithm inequalities give
a<=alpha_j<=a+1/(e*j)<=a+1/j. In particular U>=a and
U-a<=1/k+1/(2m). Therefore

    0 <= 1/a-1/f_t <= 1/a-1/U
                         = (U-a)/(a*U)
                         <= (1/k+1/(2m))/a^2.

This holds uniformly over the whole stated t range. Both k,m tending to
infinity squeeze the ratios to the known limit. Substitution k=m=s,
n=s^2 gives exactly 3/[2*a^2*sqrt(n)]. This is the stated square-size
subsequence, not a claim for every integer ground-set size with that
parametrization.

## 7. Boundaries, sources, contribution, and remaining work

All optimization sets are nonempty compact finite probability polytopes;
the product law is feasible, including at zero/one marginals. A positive
coverage numerator entails a positive-weight feature with a positive
marginal, so its product expectation and every relevant denominator are
positive. Empty features, zero weights, empty color classes, and edgeless
graphs create no exception. The k=1 and m=1 endpoints have separate valid
arguments. All collision coefficients used with upper constraints have the
correct sign. The limits keep the exact parameters stated in the claim.

The focused primary-source comparison is recorded in
`audit/referee-20ee9a6fefc3-source-comparison.md`. It confirms attribution of
the Cartesian family, classical constant, two-group ingredient, and known
all-pairs/t-wise limit. It also confirms the RN2025 mutual-versus-pairwise
correction and the listed publisher metadata. No equivalent complete sparse
fixed-k theorem or matching perturbation refinement was identified in this
bounded screen; this is not proof of priority.

The finite within-block certificate is a nontrivial useful delta: it proves
extremality survives removal of all cross-block tests, resolves the fixed-k
graph hierarchy, and controls aggregate perturbations. The exact matching
coupling gives a sharp stability threshold in an identified family. The
finite t-wise sandwich is a coherent consequence, and the color sampler is
a concrete conditional conversion. These merit the claimed modest
contribution without treating known ingredients or the known limit as new.

No unresolved mathematical gap was found in any assertion of the frozen
candidate. Writing, all 19 response items, official formatting, authors,
citations in the eventual manuscript, build, and every-page visual review
remain separate WRITE/RELEASE tasks. This acceptance creates no manuscript,
PDF, external submission, or venue-fit certification. The structural
`check-math` result is saved separately and is not mathematical proof.
