# Fresh mathematical review

Job: `c037-msthalf-referee-9071a36d85a3`.
Frozen mathematical snapshot:
`d0a2fbd366a632f17366053e75f1a37a1254cc80a92e14c60a7d14734548277b`.

**Verdict: accept the frozen resolution-paper in its full original scope.**
The original affirmative statement is proved. The contribution passes the
substantive innovation gate. The separate fresh STOC assessment is
`working_paper`; mathematical acceptance is not a venue decision or release
authorization. No manuscript or PDF is produced by this review.

## Review boundary and original scope

I read the immutable original, its precise interpretation, the claim and
listed frozen proof, literature, code, data and primary text. I reconstructed
the proof from definitions rather than treating proposer checks as an audit.
I did not read checkpoint/state files, previous reviews or job transcripts,
and did not open the unlisted supervisor proof files referenced by the
mandatory phase-start note. No agents or additional model processes were
used. Every frozen file hash and the canonical snapshot digest were checked;
there were no mismatches. The original source hash remains
`d45cd6730fe3f8685cb796b9d75ebe8e7926c1584021d045a282021749e45128`.

The accepted quantifiers are exactly those in source.md: for every fixed
real 0<=p<1/2, an explicit finite no-query algorithm has expected TRUE cost
at most C_p max(1,ln n) MST(d), for all n>=2, all finite n-point metrics,
and every omniscient post-mask arbitrary finite replacement rule. Nothing
requires a metric observation matrix, bounded aspect ratio, oblivious
replacement values or a computational efficiency assumption. The returned
object is a tree on the original vertices. No negative resolution, efficient
algorithm or new lower bound is accepted.

## 1. Independent reconstruction of the central transfer argument

Let the distinct metric points be in order v_1,...,v_n. The nonnegative
weights w_i give coordinates t_i and total W. Let H have at least eta|A||B|
edges in every disjoint rectangle with both sides at least r, and suppose
d(u,v)<=|t_u-t_v| on H. Here r>=1 and 0<eta<=1.

For a set S of m>=2r vertices, uniformly sample ordered disjoint r-subsets
A,B of S. An unordered edge of H[S] crosses with probability
2r^2/(m(m-1)). The rectangle hypothesis and linearity of expectation imply
|E(H[S])|>=eta m(m-1)/2. Thus H[S] has a vertex of degree at least
eta(m-1). In particular, for L=ceil(2r/eta), any 2L-set contains a star
with r distinct leaves, since eta(2L-1)>=4r-eta>=r. This is hereditary
density on the actual set of interest, rather than a global degree claim.

Write D_i=d(v_i,v_{i+1}). Cheap edges, D_i<=64w_i, sum to at most 64W.
For every other edge attach I_i=[t_i-D_i/64,t_i+D_i/64]. If x belongs
to I_i, its first endpoint is at distance at most D_i/64 from x in
coordinate, and the second at distance less than D_i/32, since
w_i<D_i/64. Both are therefore strictly within D_i/32. These inequalities
hold at closed endpoints and when w_i=0.

If 2(L+r) intervals cover x, an edge-index parity class supplies L+r
vertex-disjoint path edges. Sort those edges by true length, take L bottom
edges and r top edges, and let D0 be the maximum bottom length. All 2L
bottom endpoints have coordinate distance less than D0/32 from x. Choose
the star there and denote its leaves by B. Domination on its two spokes
gives d(b,b')<D0/8 for all leaves b,b'. For any top edge aa' of length
D>=D0 and any b in B, both coordinate distances q(a,b),q(a',b) are
less than (D+D0)/32<=D/16.

If both top endpoints have any H-neighbor in B, their neighbors can be
different: the metric path through those two leaves gives
D<D/16+D0/8+D/16<=D/4, a contradiction. Hence one endpoint of each
top edge has no H-neighbor anywhere in B. Pick such an endpoint from each
top edge. The matching makes the resulting r-set A disjoint from B.
Its empty rectangle contradicts positive density. This proves a uniform
overlap bound below 2(L+r), hence at most 8r/eta. The matching step and
the stronger “no neighbor anywhere” conclusion are both essential and valid.

All these intervals lie in [-Dmax/64,W+Dmax/64]. Integration gives
sum_expensive D_i <= (256r/eta)W+(8r/eta)Dmax. Triangle inequality along
a true MST gives Dmax<=diam(d)<=MST(d). Adding 64W and using r/eta>=1
establishes exactly the frozen strengthened bound

    sum_i D_i <= (320r/eta) W + (8r/eta) MST(d).

This is a single integral over all scales, so there is no hidden additional
logarithm or aspect-ratio dependence. If n<2r the density assumption is
vacuous, but the alleged high-overlap matching configuration is impossible;
the proof remains valid. If W=0 and rectangles exist the assumptions force
a contradiction, since a strictly positive metric cannot be dominated on
any H-edge by zero. In the vacuous case the final inequality still holds.
Tied true lengths cause no difficulty. No ultrametric assumption is used.

## 2. Repair benchmark and probability checks

Fix a true MST and its first-visit Euler order, independently of the mask.
Let a_i be the intervening true tour lengths, whose total is at most 2M,
where M=MST(d). True distances are bounded by the corresponding weighted
order walks. For a marked consecutive pair, a candidate third vertex
repairs it when both incident pairs are unmarked. For this fixed source
pair the tested unordered pairs for distinct candidates are all distinct,
so the candidate successes are independent with probability
alpha=(1-p)^2. They also exclude the original pair. The union bound
Pr(F^c)<=(n-1)(1-alpha)^(n-2) is valid for all n, including n=2 with the
stated exponent-zero convention.

On F the retained edges and two-edge repairs form a connected all-unmarked
graph; removing cycles gives an all-unmarked spanning tree T0. Set
X=c_d(T0) on F and zero outside it. Every source edge pays its own a_i
once; an excursion pays twice on the additional order edges. For an edge
j to be paid additionally by source i<j, the selected candidate must lie
past j, so no intermediate candidate u_{i+2},...,u_j succeeds. The
nearest-order-position rule guarantees this implication irrespective of
the other side or ties. The probability is at most beta^(j-i-1), where
beta=1-alpha. The symmetric argument holds for i>j. Thus each a_j has
expected coefficient at most 1+4/alpha and

    E[X] <= 2(1+4/alpha) M = B_p M.

No independence between repairs is claimed, and no conditioning on F is
inserted into the geometric calculation. Cycle deletion only decreases
nonnegative cost. This independently verifies the stated unconditional
form of the known repair mechanism from Anand et al., Lemma 3.2, including
the small-n issue in that source's asymptotic high-probability formulation.

Choose a fixed rational pi with p<=pi<1/2, epsilon=(1-2pi)/8,
eta=1-2pi-2epsilon>0, R=ceil(20epsilon^-2), and
r=R ceil(log_2 n). A disjoint a-by-b rectangle has independent marks;
Hoeffding gives probability at most exp(-2epsilon^2 ab) that its marked
fraction exceeds pi+epsilon. Since ab>=r(a+b)/2 and there are at most
n^(a+b) set pairs, the total failure probability is bounded by

    sum_(a,b>=r) n^[-19(a+b)]
      = n^(-38r)/(1-n^-19)^2 <= n^-12.

I checked the direction of each inequality and the n>=2 constants. If no
qualifying rectangle exists the event holds surely. This event E is uniform
over all rectangles before replacement values are chosen, so it is valid
for data-dependent tree selection and an omniscient adversary.

## 3. Observability, finite algorithm and expected true cost

Clipping negative observations preserves all unmarked entries. Enumeration
of the finitely many labeled trees, and all pairs of disjoint subsets, is
an explicit finite procedure in the stipulated exact-arithmetic model.
Tree weights are clipped observations. Qualification asks for fraction
1-pi-epsilon of observed pairs dominated by weighted tree-path distances
in every rectangle of side size at least r. Minimum cost and lexicographic
tie rules are well-defined over a finite nonempty candidate set. In its
absence the specified fixed path is still a valid output. The preorder
also always gives a spanning path on the original points.

For every fixed p a rational pi in the indicated range can be hardcoded
in A_p; it need not be computed from an arbitrary-real representation of p.
This is consistent with the existential quantifier over A_p and adds no
bit-complexity promise. Integer doubling computes ceil(log_2 n).

On E intersect F every unmarked pair is dominated by the all-unmarked
comparison tree T0, using the TRUE triangle inequality. Hence T0 qualifies,
and the selected observed tree cost is at most X. For the selected tree,
let H be its dominating pairs that are also unmarked. In each rectangle
its density is at least
(1-pi-epsilon)-(pi+epsilon)=eta. This graph is used only in the analysis.
The algorithm never receives the mask, H, d, or T0.

For the selected preorder, the observed Euler-segment weights w_i are
nonnegative, with W<=2X. Any weighted tree path is no longer than the
connecting Euler walk; consequently d(u,v)<=y_T(u,v)<=q(u,v) on H.
The transfer theorem therefore yields, pointwise on E intersect F,

    Y <= (320r/eta)(2X+M).

Using X>=0 and its unconditional expectation gives a contribution at
most (320r/eta)(2B_p+1)M. Neither E and F nor the selected tree need be
independent. Off this event EVERY possible tree has true cost at most
(n-1)diam(d)<=(n-1)M, regardless of observed values. The complementary
expectation is therefore at most

    [(n-1)n^-12+(n-1)^2 beta^(n-2)] M
      <= [1+2/alpha^3] M.

The last bound follows from the exact nonnegative series
sum_(n>=2) n(n-1) beta^(n-2)=2/(1-beta)^3. It remains valid at beta=0
with 0^0=1. Finally r<=R(1+1/ln 2)max(1,ln n). All constants are finite
for fixed p<1/2 and independent of n, the metric, its aspect ratio and
the adversarial values. Pointwise uniformity in the replacements also
covers randomized adversarial rules by averaging. This proves the exact
original affirmative statement without a parameter restriction or hidden
oracle. I found no mathematical gap.

## 4. Fresh computation actually performed

I wrote and ran `audit/referee_verify.py`, without importing or executing
the proposer scripts and without changing frozen files. Results are in
`audit/referee-verification.json`:

- 160 saved metric instances, 680,960 triangle checks, and 2,802,752
  explicit disjoint r-by-r rectangles were independently checked.
- Rational interval integration, endpoint overlap, the strengthened transfer
  inequality and the 778 expensive edges were checked. MST costs were
  recomputed with Kruskal rather than the saved verifier's Prim method.
- Every pair mask for n=2,...,6 was independently enumerated: 33,866 masks.
  The repair cost was computed directly as two weighted-line distances,
  rather than accumulating the proposer's coefficient array. Exact failure
  probabilities and indicator-weighted costs agreed at p=0,1/3,2/5,49/100;
  all 20 probability/size comparisons satisfied the analytic bounds.
- 150 exact rational constant checks covered small r and small eta.
  Frozen hashes were verified before and after the computations.

These are finite consistency checks, not a universal proof, and the sampled
metrics do not exhaust metric space. The saved overlap maximum of four is
an observation only, not the proved universal bound. Acceptance rests on
the argument reconstructed above.

## 5. Current novelty, substantive value and limitations

The fresh primary-source comparison and search terms are recorded in
`audit/referee-literature.md`. The nearest unrestricted upper bound is
Anand et al., arXiv:2610.40594v1, Theorems 1.4/5.3, for p<1/4. Their
repair benchmark, minimum-certificate selection and preorder output are
credited prior components. Their Lemma 5.6 relies on a common-good-neighbor
argument that needs a good-pair fraction exceeding one half. The candidate
instead uses positive hereditary rectangle density, a star among shorter
overlapping edges and endpoint exclusion on longer ones. This supplies a
genuinely different deterministic implication and removes the entire
remaining threshold gap. The interval integral prevents an additional
logarithmic factor. This is not a routine substitution into the prior lemma
or a small subsidiary counterexample.

Bateni et al., COLT 2024, Theorem 4, requires metric weak observations; it
does not imply this arbitrary-observation result. Its Theorem 32 supplies
a logarithmic obstruction at p=1/3, where the candidate gives a matching
order upper bound. I do not infer such a lower bound at all p from that
statement. The present theorem is not a claim of a constant approximation
or efficient implementation.

The half boundary is substantive rather than an arbitrary parameter gain.
Anand et al., Theorem 1.5, gives a linear obstruction there. Their displayed
two-cluster construction uses a pseudometric. For comparison with this
project's strictly positive metrics, use intracluster distance delta>0 and
intercluster distance 1. For p>=1/2 the same pairwise adversary outputs
delta with probability 1-p independently of the hidden balanced partition:
it outputs 1 on marked within-cluster pairs, and delta on marked
cross-cluster pairs with probability (1-p)/p. The observation matrix is
independent of the partition. Any output tree then has expected crossing
edge count 2 floor(n/2) ceil(n/2)/n, whereas the true optimum is
1+(n-2)delta. Taking delta=n^-2 retains an Omega(n) ratio. This is a
standard strict-metric regularization of that credited prior obstruction,
not a new lower-bound contribution or an alteration to the candidate.

The current arXiv primary record displays only v1. The fresh bounded search
identified no equivalent full-gap theorem. This supports novelty relative
to the checked literature and does not certify absolute priority. The
independent metric transfer and full information-theoretic threshold
resolution provide substantive mathematical value even though the
algorithm inherits exhaustive enumeration and no additional objective is
analyzed. Efficiency, general applications, final manuscript production,
and release checks remain separate tasks, not gaps in the accepted theorem.

## Final judgment

Accept `resolution-paper`, original status `proved`, at precisely the frozen
scope. The mathematical gap list is empty. Record the innovation assessment
in `audit/innovation.json`. Retain the conservative `working_paper` label
from `audit/stoc-assessment.json`: the new conceptual step is credible, but
its broader consequences and the competitive STOC significance of an
inefficient single-problem threshold completion remain uncertain. No
acceptance probability, external review, venue decision, artifact release,
or permission to submit is asserted. The required structural check-math
result is recorded separately in `audit/check-math-result.json`.
