# Fresh mathematical referee report

Job: `c040-mstdecfull-referee-8513177dc0bb`.
Frozen snapshot: `3a7133dbcc463bfba827578e6a5a4028802dc5a73d23c647e733201b0be99d76`.

Verdict: **accept** the exact frozen resolution-paper candidate. The full
immutable original is proved, with the stronger expected quadratic logarithm.
This is an internal mathematical and contribution assessment, not external
peer review or a truth certificate. The separate STOC assessment is
**working_paper**; technical acceptance does not establish submission readiness.

## Scope and independence of this review

I reviewed source.md, problem.md, claim.json, audit/snapshot.json and the
snapshot's listed mathematical/source evidence. All 15 file hashes and the
canonical mapping digest matched before review. I did not consult checkpoint,
state, job transcripts or earlier mathematical/STOC verdicts. The mandatory
outer note was treated as a noncertifying input, and its pointed-to unfrozen
research files were not opened. Existing active audit files were preserved
byte-for-byte in audit/preserved-before-8513177dc0bb/ before replacing the
active reports; their decisions were not used to establish this verdict.

The reviewed statement is: for every fixed p<1 and hardwired rational
0<q<=1-p, a deterministic algorithm observing only D always outputs a
spanning path, has expected true cost at most
10^15 q^-5 max(1,log_2 n)^2 MST(d), and uses
n^(a_q max(1,log_2 n)) exact arithmetic/comparison and control-bit operations
on every execution, independently of aspect ratio. There are no private bits
or true-distance/label queries. Since log_2 n>=1 for n>=2, this implies the
unchanged original fourth-power target. No arbitrary-corruption theorem,
polynomial-time theorem, rational bit-cost strengthening, or negative answer
is inferred.

## Reconstructed proof and attacks

1. **Mask uniformity and seed concentration.** Write ell=ceil(log_2 n),
r=ceil(80q^-2 ell) and R=ceil(128r/q). For any disjoint a- and b-sets,
Hoeffding bounds the probability of fewer than (q/2)ab unmarked cross pairs
by exp(-q^2 ab/2). The union bound uses ab>=r(a+b)/2 and at most n^(a+b)
choices. Because 20/ln(2)-1>27, the stated geometric sum is below n^-20.
This event concerns mask bits alone. Consequently it applies to seeds, cores,
observations and normalization chosen adaptively from the full mask; no
independence of observed distances is needed.

For an observed R-clique at scale s, splitting it into halves yields a vertex
z with at least qR/4>=32r unmarked neighbors U. Every such neighbor is truly
within s of z. If r seed vertices F lay beyond 2s, U and F would be disjoint,
and all U--F edges would have true distance>s and observation<=s. That would
contradict the mask rectangle event. Thus at least R-r vertices are in the
true 2s-ball of a seed vertex. The argument remains valid when q is very small;
it does not assume a majority of pairs is unmarked.

2. **Quantiles, overlaps and rounding.** With tau=1-q/8 and r/R<=q/128,
more than tau R point-to-seed entries, and more than tau R^2 seed-to-seed
entries, meet the respective core upper bounds. The ceiling-rank convention
therefore gives those bounds literally. For the lower seed comparison, if
the center distance minus the two radii is positive, the two cores are
disjoint even when the seeds overlap. The rectangle event supplies more
than (1-tau)R^2 unmarked core pairs. They correspond to distinct unordered
pairs and each has observation at least the desired lower bound. Fewer than
tau R^2 entries can lie strictly below that bound, which proves the lower
order-statistic assertion including integer ranks. A nonpositive lower
bound follows from D>=0. Identical seeds and diagonal zeros introduce no gap.

The point soundness statement is setwise: r far vertices with Q(x,S)<=B
would be disjoint from the seed core, and each could have at most qR/8
unmarked edges to that core. The rectangle lower bound requires strictly
more, since the core has size R-r>R/4. There are fewer than r such far points
in the whole universe, rather than merely a small failure probability for
one selected point.

3. **Observable construction and nonaccumulation.** Every loop, quantile,
clique predicate, future-seed test, tie rule and output traversal uses D
only. Active objects are removed permanently within a level, so nesting and
at most one representative change per level hold. Old nonsingletons are
selected or absorbed before the loop can stop; fresh seed members are
included by admissibility. Every intermediate nonsingleton contains its
representative R-set.

For x within (A-2)t of a seed center, Q(x,S)<=At and the lower seed-comparison
bound proves every future consistency inequality. In particular a true
diameter-t R-set is admissible. For an arbitrary final cluster point, take
its first singleton absorption at t_0 and the selected representative S_0.
The point passed F at that time, including when it was a fresh seed member.
Each later representative change moves its fixed birth center by at most
(A+4)s. These dyadic distances sum to at most 2(A+4)t. The final seed was
among the original universal tests at level t, regardless of whether it
had then been selected. Combining the test with the upper seed comparison
gives Q(x,S_f)<=112t. Setwise soundness now bounds all of the final cluster's
far points together: fewer than r lie beyond 114t. This proves a core of
diameter<=228t<256t and size at least R-r>r. It does not add incoming
outlier budgets across merges. Repeated carried seeds have fixed centers.

4. **Packing and the retained outlier mass.** Selected centers at a level
are more than 28t apart. An old nearby seed would have been merged. If a
later seed is fresh, its nonempty core consists of still-active singleton
points that the earlier seed would have removed. This is a contradiction.
A doubled true MST tour bounds the number K_i of generated clusters by
1+W/t_i. Termination excludes R leftover singletons in any true diameter-t_i
set. A maximal t_i/2-separated cover and the same tour argument therefore
give N_i<=(R-1)(1+4W/t_i).

These categories exhaust each intermediate partition. Consequently
|C_i|<=R+4RW/t_i and the actual outlier total is
O_i<=rK_i+N_i<=2R+5RW/t_i. Bottom clusters contribute n to both sums;
the root contributes t_L to H and zero to Omega. Under the normalized
scale bounds, n<=2W and t_L<2n^2<=4W. Direct geometric summation verifies
both H<=14R(L+1)W and Omega<=14R(L+1)W. Giving every leftover singleton
r outliers instead would lose a logarithm; retaining its actual one
outlier is justified by its empty singleton core.

5. **Deterministic extraction, including nonnested cores.** I reconstructed
the lemma for arbitrary nested partitions under its stated core hypotheses,
not just the particular carving output. For consecutive DFS leaves u,v,
let j be their least common cluster level, and promote each endpoint from
j to its first containing core, at levels k_u,k_v. At k=max(k_u,k_v), the
common cluster D has a nonempty core because the later-promoted endpoint
belongs to it. A smaller promoted core either equals D, meets the full root,
or has more than b points while D omits at most b. Thus it intersects the
core of D. Three core diameter bounds give d(u,v)<=3 beta 2^k.

If k=j, both endpoints are in the common core and the cost is at most
beta 2^j. The level-(j-1) child containing u is a contiguous leaf interval.
This edge exits its right boundary, which can happen at most once. These
charges sum to at most 2 beta H. If k>j, the later-promoted endpoint is
an outlier at level k-1, even though its core membership need not be
monotone. Charge its cluster there, with cost<=6 beta 2^(k-1). Each point
has at most two incidences in the final path, so a level-cluster pair
receives at most twice its actual outlier count. These charges sum to
12 beta Omega. Repeated clusters are distinct level nodes; empty cores
cause no intersection assertion about an empty set. This establishes
cost(P)<=2 beta H+12 beta Omega. It does not use a physical leader-tree
preorder in place of the specified cluster-tree leaf order.

6. **Scale, expectation and boundary quantifiers.** For a fixed true
diametral pair, choose for every other vertex a distinct incident pair
of length at least Delta/2, and include the diametral pair. These n-1
distinct pairs depend only on d. If any is unmarked then U>=Delta/2,
so the bad scale probability is at most p^(n-1), uniformly over the
adversary. For U>0, lambda=2U/n^2 and d*=max(1,d/lambda) off diagonal
define a genuine metric. The diagonal stays zero, unmarked equality
persists, and D*<=d*. The random choice of lambda does not affect the
uniform mask implication. On the scale event, Delta* is in
[n^2/2,n^2], so the forced root has the required diameter.

With beta=256 the extraction and weighted bounds yield
50176 R(L+1)MST(d*). The MST flooring overhead and scaling back cost
at most a factor two for n>=2. On other masks the path still costs
less than n MST(d). The unconditional extra expectation is at most
[n^-19+n p^(n-1)]MST(d)<=(1+1/q)MST(d). This uses
n p^(n-1)<=sum_(k=0)^(n-1)p^k<=1/q, with the p=0 case literal.
The good term is at most 13246464000 q^-3(log_2 n)^2 MST(d), safely
within the claimed 10^15 q^-5 constant including failures. The n=2
unique path and R>n label path branches satisfy the bound directly;
U=0 is a valid path branch included in the scale failure estimate.

7. **Every-execution resources.** The algorithm enumerates R-subsets,
not true metric data. Clique tables, point quantiles, pair quantiles
and all future tests have N^2 times polynomial overhead for
N=binom(n,R)<=n^R. There are at most n carving iterations per level.
R=O(q^-3 log n), L=O(log n), and bounded-length integer counters
add polynomial control-bit overhead. Fixed implementation constants
are absorbed in a_q as explained in Section 9. The branches use only
bounded loops based on n,q, not the observed scale ratio. Sorting
requires exact comparisons; no arbitrary-real unit bit-cost claim
is made. Private-bit cost is exactly zero. No good-mask restriction
appears in the resource or spanning-output proof.

## Independent finite check actually performed

I wrote audit/referee-8513177dc0bb-check.py without importing or rerunning
the proposer's checker. It exhausts all 358 nested two-intermediate-level
partition chains on five labels, all 8,951 eligible core assignments for
(b,B)=(1,2),(2,3), and all compatible leaf permutations: 268,560 ordered
cases and 1,074,240 edges. Exact integer shortest-path closure gives the
entrywise largest metric satisfying the core diameter constraints, including
the root constraint. Any feasible metric is bounded above by this closure
by the triangle inequality. The script checks intersections, promotions,
immediate and late multiplicities, and the separate and total cost bounds.
All passed, including 453,120 late edges and 2,630 changing repeated-core
occurrences. The serialized result and script digest are in
audit/referee-8513177dc0bb-exact-check.json. This finite check is not the
all-n proof and does not execute the large-constant carving algorithm.

## Current primary comparison and substantive value

The fresh live [arXiv record](https://arxiv.org/abs/2610.40594) listed only
v1, dated 29 October 2026. I checked the actual [primary text](https://arxiv.org/html/2610.40594v1),
particularly Definition 2.1, Theorems 1.2/1.3, Section 6's hierarchy,
future-seed tests and extraction proof, and Theorem 7.2. Local frozen
primary text was used for the detailed comparison. The existing all-p
logarithmic algorithm is computationally unrestricted; the quasipolynomial
fourth-power theorem assumes p<=0.1. The present theorem improves both
the computational noise range and the logarithmic exponent, and makes
extraction deterministic.

This is more than a threshold-only corollary of that theorem. At a majority
of marked pairs, its fixed low quantiles can no longer certify true
inter-seed distances. The two-step rectangle bootstrap produces an almost
full hidden seed core at every fixed positive unmarked density, which
supports the replacement high quantiles. The final leaf-path extraction
changes the algorithm whose edges are charged: contiguity controls immediate
charges and final degree two controls delayed charges. Retaining the actual
outlier mass then gives a second logarithmic saving. These are coherent,
explicit changes with a stronger full-scope guarantee and a reusable
deterministic hidden-core extraction statement. I assess their combined
mathematical value as substantive. The hierarchy, universal future
consistency, normalization, packing and promotion/intersection architecture
remain credited to the source. Distinct seeds actually born are globally
disjoint, so overlapping future tests are not an essential separate novelty.
The short outlier-accounting improvement alone is not a second contribution.

The [COLT2024 primary](https://proceedings.mlr.press/v247/bateni24a.html)
and frozen full text were checked at Theorems 4--6: the square-root-log
upper bound assumes metric observations and does not subsume this nonmetric
model. The unrestricted-observation lower theorem is a different statement.
The [Fletcher--Hershkowitz SODA2026 publisher record](https://epubs.siam.org/doi/10.1137/1.9781611978971.193)
describes graph-spanning distance embeddings with logarithmic level growth,
which differs from the present dyadic total-cost hidden-core guarantee.
My ordinary View PDF attempt redirected to its access/abstract page; I
did not obtain its full proof or exclude equivalent auxiliary lemmas there.
Focused current-topic searches identified no equivalent complete all-p
quadratic-log theorem; this bounded screen is not proof of priority or
comprehensive absence. Access limitations are retained, not treated as
evidence of originality. No proof here relies on that adjacent paper.

The source's Theorem 7.2 reduces to distinguishing quietly planted colorable
graphs, with low-degree evidence for difficulty. It is not a Planted Clique
implication or a general proved polynomial-time lower bound. Its displayed
metric has zero within classes; this review asserts no genuine-metric
hardness transfer and uses no hardness premise to accept the upper theorem.

## Gaps, label and handoff

No unresolved mathematical gap remains in the exact frozen proof as reviewed.
The accepted strongest theorem resolves source.md in its full stated model.
The bounded novelty screen and adjacent full-text limitation must remain
visible in any subsequent writing. The STOC case remains uncertain in
importance, depth and breadth: this improves a recent framework substantially
but does not attain its logarithmic benchmark, make the runtime polynomial,
or demonstrate consequences beyond the stated model. The separate actual
assessment therefore assigns working_paper. No manuscript, PDF, external
submission or contact was made in this job. The structural check-math result
must pass before the normal writing/release workflow proceeds; that check
establishes file/provenance consistency, not the truth of this report.
