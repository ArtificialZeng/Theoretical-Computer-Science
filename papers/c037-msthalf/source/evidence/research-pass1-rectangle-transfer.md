# Rectangle transfer: verified two-level case and unresolved multiscale kernel

Job: c037-msthalf-research-82a59cd9a4af; research pass 1. Mathematical status:
original unresolved, no candidate. This is a research record, not a manuscript,
fresh referee report, novelty certificate or venue assessment.

## 1. Precise deterministic kernel

Let v_1,...,v_n be an order, w_i>=0, t_1=0 and
 t_j=sum_{i<j} w_i; put q(v_i,v_j)=|t_i-t_j| and W=sum_i w_i.
Let d be the true metric. A graph H is dominated when
 d(u,v)<=q(u,v) for each edge of H.
Assume every disjoint A,B, |A|,|B|>=r, has at least eta|A||B|
H-edges, where eta>0 and r is a positive integer. The proposed sufficient
transfer theorem is

    sum_{i=1}^{n-1} d(v_i,v_{i+1})
      <= K_eta r [ W + MST(d) ].                         (K)

It is UNPROVED here for general metrics, and also unproved here for arbitrary
multiscale ultrametrics. It is sufficient, not claimed equivalent to the
immutable source. The proof below needs only one H-edge per large rectangle.
Testing all disjoint r-by-r rectangles suffices for the density formulation:
average the density over independently uniform r-subsets of arbitrary larger
A,B. This averaging is deterministic, not a claim about adaptive mask samples.

For a weighted tree and its Euler preorder shortcut, let w_i be the total
observed edge length on the corresponding Euler-tour segment. Then W is at
most twice the observed tree cost, and tree-path distance is at most q.
Thus the same H is dominated in this order. H is used solely in the proof;
the observable algorithm below does not receive it.

## 2. Uniform mask feasibility, independently checked

Fix p<1/2, epsilon=(1-2p)/8, eta=1-2p-2epsilon=3(1-2p)/4>0.
For n>=2 put r=ceil(20 epsilon^(-2) ln n). For disjoint A,B of sizes a,b>=r,
the independent mask has ab independent Bernoulli(p) entries. Hoeffding's
inequality bounds an excess above (p+epsilon)ab by exp(-2 epsilon^2 ab).
Because ab>=r(a+b)/2 and there are at most n^(a+b) such pairs of sets,
the union failure probability is at most

 sum_{a,b>=r} n^[-19(a+b)]
   <= n^(-38r)/(1-n^(-19))^2 <= n^(-12).

Extending the sum beyond n only enlarges it. When 2r>n the assertion is
vacuous, and every tree has true cost <=(n-1)MST(d)<2r MST(d).
This event E concerns the mask alone and is uniform over every subsequently
selected metric/tree/order and every post-mask replacement rule.

An explicit observable procedure enumerates the finitely many spanning trees,
weights their edges by clipped observations y>=0, and retains trees satisfying

    for all disjoint A,B with |A|,|B|>=r,
    at least (1-p-epsilon)|A||B| pairs satisfy
    y(u,v) <= observed_tree_path_distance(u,v).

Choose a tree of minimum total observed cost; break ties lexicographically by
its sorted edge list. Return its preorder shortcut using root 1 and increasing
vertex labels for child order. If none exists, return the increasing-label
path. All checks are finite and use only observations. This realizes the
supervisor's tree certificate rather than assuming a real-valued candidate
metric minimizer exists; no correctness claim for general metrics follows.

On E, a retained tree has at least eta fraction pairs that are BOTH unmarked
and dominating in every large rectangle. On the source tree-repair event F
(Lemma 3.2, verified primary input), there is an all-unmarked comparison tree
T0 with E[c_d(T0) 1_F] <= B_p MST(d), for sufficiently large n and some finite
B_p. All its unmarked pairs dominate by the true triangle inequality. Hence
on E intersect F it is retained and the selected observed cost is <=c_d(T0).
No independence of the selected tree or F and E is used. In particular,

 E[c_d(T0) 1_(E intersect F)] <= E[c_d(T0) 1_F].

If (K) holds, apply it on E intersect F and use W<=2 observed_cost(T).
Outside that event every output tree/path has cost <=(n-1)MST(d); failure
probability <=n^(-10)+n^(-12). This gives the original expected O_p(log n)
bound. Finitely many small n are handled by increasing the p-dependent
constant. This implication is conditional on (K), not a solution.

## 3. Proved positive result for all two-level cluster metrics

Suppose X is partitioned into k>=2 nonempty clusters, with d(u,v)=delta>0
within clusters (u!=v), and d(u,v)=M>=delta across clusters. These are metrics,
with arbitrary k, cluster sizes and aspect ratio M/delta. Then

    MST(d)=(n-k)delta+(k-1)M.

Under the assumptions in Section 1, the following bound holds:

    c_d(order) <= 4r W + (4r+1) MST(d).                  (T)

Proof. Partition the order positions into nonempty bins according to
floor(t_i/M). Their number B is at most floor(W/M)+1. Each bin is a contiguous
subsequence, including when weights are zero. Its q-diameter is strictly less
than M, so H has no cross-cluster edge within the bin.

A bin therefore cannot contain disjoint r-sets whose cluster colors are
disjoint. If one color has at least r vertices, fewer than r vertices have
other colors; otherwise choose r of that color and r of the rest. Consequently
there are at most 2(r-1) color changes in this bin. If every color has at most
r-1 vertices, greedily collect whole colors until collecting between r and
2r-2 vertices. If the bin had at least 3r-2 vertices, at least r of the
remaining vertices would have disjoint colors, again a contradiction. Thus
this second kind of bin has at most 3r-3 vertices. If its total size is less
than r, the same conclusion needed below is immediate. For r=1 only the first
case occurs and every bin is monochromatic.

In all cases a bin has at most 3r color changes (a loose bound). Counting also
at most B-1 changes between bins gives at most (3r+1)B<=4r(W/M+1)
cross-cluster consecutive pairs. Therefore

 c_d(order) <= (n-1)delta + M * 4r(W/M+1)
             <= MST(d) + 4rW + 4rM
             <= 4rW + (4r+1)MST(d).

Here MST(d)>=(n-1)delta and MST(d)>=M. For k=1, every consecutive pair costs
delta and c_d(order)=MST(d), with no certificate needed. This proves (T).
No good labels are used to choose the output order. Combined with Section 2,
the observable finite algorithm has expected O_p(log n) true-cost ratio on
ALL two-level cluster metrics for every fixed p<1/2, including adaptive
omniscient replacements. This is a restricted theorem only, and does not
resolve source.md or establish independent novelty/significance.

## 4. Small-side loss is necessary for this deterministic kernel

Fix 0<eta<1 and integers r>=2, s=floor((1-eta)r)>=1. Use two clusters:
one with s vertices and another with at least s+1 vertices. Give all order
edges weight delta, and alternate every vertex of the small cluster with
distinct large-cluster vertices before listing the remaining large-cluster
vertices. Take M>(n-1)delta. H consists of all within-cluster pairs; these
are dominated. For arbitrary disjoint A,B, a,b>=r, write x,y for the numbers
of small-cluster points they contain. Since x+y<=s, the cross-cluster (bad)
fraction is

    x/a + y/b - 2xy/(ab) <= (x+y)/r <= s/r <= 1-eta.

Thus H satisfies the full rectangle density condition, not just nonemptiness.
The order has 2s intercluster edges, W=(n-1)delta, and
MST=(n-2)delta+M. Its cost divided by W+MST tends to 2s as M/delta tends to
infinity with n,r fixed. Hence a bound independent of r cannot replace (K)
for fixed eta<1; a linear loss in r is genuinely needed by this deterministic
certificate. This is neither an all-algorithm lower bound nor a frequent mask
construction. It is not a disproof of the original expected guarantee.

## 5. Exact finite checks and their limits

`rectangle_cluster_check.py` enumerates all restricted-growth cluster orders
for 2<=n<=8, 2<=k<=6, r=2,3 where 2r<=n. It checks densities corresponding
to p=1/3,2/5,49/100 and the epsilon above, optimizing only a uniform order-step
weight at leading intercluster scale. Every disjoint r-by-r rectangle is
checked. Maximal examples are then verified again at M=10^6 with exact
rational arithmetic. Output: `rectangle-cluster-check.json`.

The finite search covers 31,317 density/order configurations and 6,536,826
rectangle/configuration tests. Its largest leading cost/(W+MST) ratios are
21/10 for r=2 and 4 for r=3, for each of the three specified p values.
These finite maxima are NOT claimed optimal for all weights, n or metrics.
They do not prove (T); the independent written argument above does.

`rectangle_multiscale_check.py` tests all 7! orders of each of five explicit
metrics: a line, and balanced/comb ultrametrics with bases 2 and 10. It
optimizes only uniform order weights using exact rational rectangle thresholds.
The saved JSON states exact coverage and extrema: 25,200 orders and 4,410,000
rectangle/order tests, with largest cost/(W+MST) ratio 11/4 in this tested
family. This is a bounded attack on (K), not exhaustive verification of
multiscale metrics.

## 6. Remaining obstacle and one next test

The two-level proof pays the observed order length W at a SINGLE distance
scale M. Applying it independently at many scales reuses W and does not prove
(K); an extra logarithmic loss would miss the frozen O_p(log n) target because
r already grows as log n. The source's common-good-neighbor charging also
cannot simply be restored by positive rectangle density. Neither failure is
a lower bound for arbitrary algorithms.

Next test: prove or falsify (K) first for arbitrary ultrametrics using the
rooted cluster hierarchy, with a charging invariant that pays each order
weight only O_eta(r) times and charges the rest to
sum_internal height(node)*(number_of_children(node)-1)=MST(d).
Allow arbitrary heights, depth, unequal cluster sizes and nonuniform order
weights. A falsification must give a parametrized family whose exact ratio
c_d(order)/(r(W+MST(d))) is unbounded while every rectangle condition holds.
A positive hierarchy proof should identify whether it extends to general
metrics; ultrametrics alone still do not settle the immutable original.
Do not repeat the two-level enumeration as a new research pass.
