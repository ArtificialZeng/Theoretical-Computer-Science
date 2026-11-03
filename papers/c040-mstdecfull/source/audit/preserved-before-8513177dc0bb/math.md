# Fresh mathematical review

Job: `c040-mstdecfull-referee-c896e1b53be0` (referee).
Frozen snapshot: `bf8c82fd54c9793b5c068f18f7bb44944417a41c982a27be96486504558d316f`.

**Verdict: accept the exact frozen resolution-paper claim.** The algorithm and
proof resolve the entire immutable question, with the stronger expected
`10^15 q^-5 (log_2 n)^3 MST(d)` bound. The separate venue assessment is
**working_paper**, not submission_ready. This is an internal review, not
external peer review, a priority certificate, or a truth certificate.

## Review boundary and integrity

I read source.md, problem.md, claim.json, audit/snapshot.json and all its listed
evidence files. I read the required skill/referee/contract instructions, project
policy, outer-root-note.md and STOC quality standard. The supervisor note was
treated as an adverse-check input; its unlisted suggested intake files were not
opened. No checkpoint, scheduling state, earlier audit, transcript, or owner
session was consulted. The research checklist is frozen proposer evidence, not
an independent review. No subagent or other Codex process was used.

I recomputed all ten file hashes and the canonical snapshot digest. Every hash
matches. source.md retains SHA-256
`09b52cf01e6e36d50f3090211c0313cda0f436865507abd6c00493d5583fe9a7`.
No frozen mathematical file was edited. Supplementary checks and current-source
observations are in audit/referee-c896e1b53be0/.

## Exact scope

The statement quantifies over every fixed p<1, every finite genuine metric,
every n>=2, and every omniscient decrease-only strategy acting after the mask.
Only the observations are used. Hardwiring any positive rational q<=1-p is
expressly allowed by the original. The deterministic algorithm is therefore an
allowed classical algorithm, and its private-bit cost is exactly zero. A
spanning path is a spanning tree. For n>=2, log_2 n>=1, so the cubic guarantee
implies the original fourth-power guarantee without changing its quantifiers.
The exact arithmetic/comparison model is retained; no precision-independent
rational bit-complexity assertion is being accepted.

## Reconstruction of the argument

### Mask concentration and clique cores

For disjoint sets of sizes a,b>=r, there are ab independent unordered mask
entries. With unmarked probability at least q, Hoeffding gives the displayed
`exp(-q^2 ab/2)` failure bound. Since `ab>=r(a+b)/2`, a union bound over at most
`n^(a+b)` choices is valid. The coefficient check is
`q^2 r/4>=20 ell>28 ln n`; hence every summand is at most
`n^(-27(a+b))`. Extending the sum to a,b>=1 bounds it by
`n^-54/(1-n^-27)^2<n^-20`. Cases where the sets cannot exist are vacuous.
This event depends only on the mask, so it is available for adaptively selected
seeds, observation-dependent normalization, and every adversarial observation
simultaneously. No observation-independence assumption is used.

In an observed R-clique, apply the event to a split into two halves. Averaging
gives a point z with at least qR/4 unmarked neighbors in the other half. That
neighbor set U has size at least 32r and true radius s around z. If r points
of the clique were farther than 2s from z, all edges between them and U would
have true length greater than s, and therefore would have to be marked. This
contradicts the same rectangle event. Thus the clique has a radius-2s core of
size at least R-r. The center belongs to the seed, and may be fixed when the
seed is first selected. This is a valid argument even at high corruption
probability; it does not infer a large unmarked degree fraction near one.

### Quantile bounds, rounding and overlaps

Put e=r/R<=q/128 and tau=1-q/8. Then `1-e>tau` and
`(1-e)^2>tau`. These strict margins prove both upper quantile bounds using
D<=d, including diagonal zeros. For the lower seed comparison, if
`l=d(z,z')-2s-2s'>0`, the two radius cores must be disjoint: an intersection
would contradict the triangle inequality. Consequently their ordered cross
entries represent distinct unordered pairs even when the original seeds
overlap. The event supplies at least `(q/2)(R-r)^2>(q/8)R^2` unmarked entries
of value at least l. An integer count strictly greater than `(1-tau)M`
puts the ceil(tau M)-th order statistic at least l. If l<=0 nonnegativity
already proves the bound. No zero override for Z(S,S) is needed.

For point-set soundness, suppose r far points pass Q(x,S)<=B. They are disjoint
from the core, and each has at most qR/8 unmarked incident core entries: every
uncorrupted such entry has true and observed value greater than B. This
contradicts the rectangle lower bound `(q/2)|F|(R-r)`, since R-r>R/4.
The proof controls a whole exceptional set; it is not a pointwise
concentration assertion for an adaptively chosen point.

### Algorithm, absorption and packing

The active-object convention is essential and is explicitly present: outputs
are held separately until the next level. A selected old object is always
removed in its entirety; fresh seed members pass the singleton tests by their
clique status and admissibility. Thus partitions remain nested on every input,
representatives remain inside their clusters, and no cluster can shift its
representative more than once at a level. The forced root and DFS traversal
always produce a literal path, even on bad masks.

For a point's first absorption at scale t0, its tested predicate F is available
whether the selecting representative was fresh or old. Each subsequent
representative change at scale s moves the fixed centers by at most (A+4)s.
The dyadic sum is at most 2(A+4)t. The final representative is one of the
universally tested future cliques, independently of its selection/birth time.
The two quantile inequalities give Q(x,S_final)<=112t for every point of the
entire merged cluster. Applying set soundness once gives fewer than r outliers
outside its radius-114t ball. They do not accumulate across constituent
clusters. The remaining core contains at least R-r points and has diameter
at most 228t<256t. Singleton cores are empty; the root core is X.

Selected centers at one scale have separation greater than 28t. For a later
old object the seed comparison would otherwise have removed it. For a later
fresh seed, its core points were still active singletons when the earlier seed
was selected, and the near-center completeness inequality (5) would have
removed them. This also excludes equal centers. The true-MST doubled-tour
packing bound applies to these centers. Separately, no R remaining singletons
fit in a true diameter-t set: such a set would be admissible. Greedy true
radius-t/2 balls and the same packing bound control the leftovers. Adding
these two counts gives |C_i|<=R+4RW/t_i, including the case of no leftovers.
Summing the dyadic costs, with W>=n-1 and t_L<4W on the scale event, gives
H<=14R(L+1)W as asserted. No true distances are needed to perform these
packing arguments; they are analysis only.

### Deterministic leaf extraction

I reconstructed the lemma without assuming nested cores. For an adjacent pair
u,v with least common cluster at level j, let each endpoint first enter a core
at level k_x>=j, and let k=max(k_u,k_v). The level-k common cluster D has a
nonempty core. If D is not the root it omits at most b points, so every earlier
endpoint core of size greater than b intersects its core. For an endpoint
whose promotion cluster is D, intersection is immediate; the root case is
also immediate. The three core-diameter bounds yield d(u,v)<=3 beta 2^k.

If k=j, both endpoints are in the least-common core. Charge the level-(j-1)
child containing the left endpoint. It is a contiguous interval in any DFS
leaf order; the oriented path exits it to the right at most once. This costs
at most 2 beta times that child's scale. If k>j, charge the level-(k-1)
cluster of an endpoint promoted at k. That endpoint is an outlier there.
Each point is incident to at most two final path edges, so the cluster gets
at most twice its number of outliers of these charges. This is at most 2B
even for an empty-core cluster; every late edge costs at most 6 beta times
the cluster scale. The total factor is exactly bounded by beta(2+12B).
Repeated clusters at successive levels are distinct level-nodes, and are
already counted in H. Unknown, changing cores do not need to be computed.
This confirms the general lemma in the frozen claim, not just its algorithmic
special case. With beta=256 and B=r the product is 50176 rR(L+1)W.

### Normalization, bad masks, boundaries and runtime

For a diametral pair, choosing one long incident edge for every other point,
and including the diametral edge itself, gives n-1 distinct fixed unordered
pairs. If any is unmarked then U>=Delta/2. Thus failure probability is at most
p^(n-1), uniformly over adversaries. The transform `max(1,d/lambda)` on
distinct points preserves the metric, and applying the same transform to D
preserves both D*<=d* and equality at unmarked entries. The mask distribution
after conditioning or normalization is never asserted to be independent.
On the good scale event, Delta* is in [n^2/2,n^2]. Also
`lambda MST(d*)<=W+lambda(n-1)<=2W`, so the original metric cost bound is
100352 rR(L+1)W.

On any bad mask the path costs at most (n-1)Delta<nW; this controls unbounded
aspect ratios without conditioning away bad events. The inequality
`n p^(n-1)<=sum_{k=0}^{n-1}p^k<=1/q` also holds at p=0 with n>=2.
The total bad-event contribution is at most (1+1/q)W. Using L<=2ell,
ell<=2 log_2 n, r<=81q^-2 ell and R<=11000q^-3 ell bounds the leading
coefficient by 2145927168000, below 10^15 even after the bad contribution.
For R>n, the arbitrary label path costs less than RW and satisfies the same
loose constant. The n=2 branch is its unique edge. U=0 belongs to scale
failure and still outputs a path. The displayed algorithm covers p=0 without
using its optional separate MST implementation. No finite-bit sampling issue
remains because there is no private randomness.

All scales depend on n, not aspect ratio. Enumerating all R-sets, their pair
quantiles, and the finite future tests has at most n^(2R+O(1)) times polynomial
control overhead. R=O_q(log n) in the nontrivial branch. Rational ranks,
integer doubling, finite subset enumeration and sorting suffice; the bit
length of counters is O(R log n+log L) plus a q-dependent constant. These
costs are absorbed in the stated a_q on every execution, including failure
masks. The algorithm specification is constructive even though its enormous
asymptotic seed sizes make a complete nontrivial execution impractical here.

## Independent finite checks actually performed

The proposer's script was inspected but not executed, because its main routine
overwrites frozen evidence. I wrote a separate verifier, check_extraction.py,
without importing proposer code. It generates 96 selected binary hierarchies
on 6,8,10,12 points, with b=1,2,3 and B=b or 2b, independent per-level core
choices and repeated clusters. It constructs the exact maximal feasible
metric by shortest paths through the core-clique constraints, and enumerates
every child orientation. All 65,280 orders and 676,608 edges pass the
intersection, individual charge, charge-multiplicity and total-cost checks;
348,676 edges use late charges. The largest observed cost/H is 128/81.
These are selected fixtures, not exhaustive all-hierarchy evidence. The
shortest-path metric dominates every feasible metric by the triangle
inequality and itself satisfies the upper bounds, so testing it covers all
metrics for each fixed tested constraint system and order. This finite fact
does not replace the preceding all-hierarchy proof.

A separate exact-rational diagnostic checked the parameter strict inequalities
for six q values and ell=1..100 (600 cases). The algebraic all-q argument is
given above. No full high-quantile seed-carving execution, formal proof
assistant certification, or exhaustive adversarial-mask enumeration is claimed.

## Current primary comparison, value and limitations

The live [Anand et al. record](https://arxiv.org/abs/2610.40594) still lists only
v1. I checked its [primary Section 6](https://arxiv.org/html/2610.40594v1).
Theorem 1.2 gives an inefficient all-p logarithmic approximation; Theorem 1.3
gives the low-p quasipolynomial fourth-power bound. Definition 6.1,
Theorem 6.2 and Algorithms 1--3 supply the inherited framework.

The frozen candidate changes two mathematical mechanisms. First, its
rectangle argument bootstraps a q-fraction neighbor set into an almost-full
clique core; a mere change of constants in a low-p corrupted-degree estimate
does not establish that fact near p=1. High quantiles then retain both
completeness and set soundness throughout the full range. Second, DFS leaf
ordering permits charging final degree-two endpoints and one-exit child
intervals. The prior random-leader degree sum is thereby avoided, with an
actual exponent improvement and derandomization. The promotion/intersection
argument, hierarchy construction, future consistency tests and normalization
are credited to the prior work. Distinct actually born seeds are globally
disjoint here as well; overlap support is useful definitional completeness,
not the main innovation.

The [Fletcher--Hershkowitz publisher abstract](https://epubs.siam.org/doi/10.1137/1.9781611978971.193)
describes graph-spanning metric embeddings with larger scale growth, rather
than this hidden-core total-path-cost guarantee. Its PDF routes redirected to
the abstract; a separate direct fetch failed. I have not inspected its full
proof and do not assert absence of related internal lemmas there. The exact
final algorithm is not supplied by its stated result. The official
[Bateni et al. COLT paper](https://proceedings.mlr.press/v247/bateni24a/bateni24a.pdf)
was checked for model context and its Theorem 32; the metric-observation upper
bound there cannot be applied to arbitrary nonmetric D.

The bounded current searches recorded in literature-check.json found no
equivalent full-range quasipolynomial cubic-log algorithm or exact hidden-core
DFS lemma. This is not proof of priority or an exhaustive survey. On the
verified comparison, the two mechanisms and their complete end-to-end theorem
constitute substantive mathematical value, beyond a routine restatement or
parameter-only corollary. This justifies the innovation gate. It does not
establish a strong STOC case: the hierarchy framework is inherited, the ratio
is still far from the information-theoretic logarithmic benchmark, runtime is
still quasipolynomial, and no second application or major lower bound is
established. Technical depth and breadth require a conservative assessment.

## Final disposition

No correctness or original-scope gap remains in the exact frozen candidate on
this review. Accept as resolution-paper with original_status=proved. Retain
working_paper in the separate STOC assessment. Only a subsequent authorized
WRITE phase may prepare a manuscript after the actual structural check-math
gate passes; all build, citation, visual and release gates remain outstanding.
No manuscript, authored PDF, external submission, email or contact was made
in this job. No research counters, historical verdicts or scheduling records
were changed.
