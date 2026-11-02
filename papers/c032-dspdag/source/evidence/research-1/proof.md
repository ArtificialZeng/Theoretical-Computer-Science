# Proposed resolution: Boolean batching of minimum-frontier transitions

Proposer: c032-dspdag-research-2c4a21894757. Research proof packet, not a manuscript or independent audit. Original authority: ../../source.md. No acceptance or venue assessment is asserted.

## Exact theorem and model

For three prescribed terminal pairs in an arbitrary positive-weight DAG with n vertices, detection of vertex-disjoint paths that are shortest for their respective pairs in the ORIGINAL graph is deterministic in O(m+n+n^(1+alpha)) source-model word operations, where alpha=log_2(7)<3. It uses O(n^3) words. In particular, k=3 and delta=1/10 answer AVW Open Problem 3 positively. Even charging O(log^2 n) elementary bit arithmetic per matrix operation gives O(n^3.9), in addition to original-weight preprocessing. No unique-shortest-path, width, sparsity, integrality, distances-given or reporting promise is used.

As in AVW Proposition 11, preprocessing uses O(m+n) original-weight additions/comparisons for each of the three sources. This is the same input-weight arithmetic assumption as the source baseline; unbounded weight encoding is not claimed to be free. If original weights have B-bit encodings, its bit cost must additionally be charged (e.g. O((m+n)(B+log n)) with ordinary integer additions/comparisons). As usual for the source's n-only bound, the graph has O(n^2) input arcs; if parallel-arc encoding is allowed, the unavoidable additional O(m) input scan remains explicit. All NEW algebraic operands have O(log n) bits, independently of original edge weights. Thus the result is in the source model, not a claim of n-only complexity for arbitrarily many input-weight bits.

The strict vertex-disjoint convention used by AVW Section 4.1 is proved first, including cross-path terminal collisions. An explicit reduction below also covers the usual convention allowing shared endpoints. Either convention has the same exponent, so the introductory 'internally' terminology does not narrow the result.

## 1. Labelled acyclic graphs and terminal completion

Compute d_i(v)=dist_G(s_i,v) by topological relaxation in the ORIGINAL graph. If some t_i is unreachable, return NO. Let E_i contain exactly original edges (u,v) with finite d_i(u) and d_i(v)=d_i(u)+w(u,v). Every s_i--t_i path in E_i has length d_i(t_i), by telescoping; every original shortest path uses only E_i. This is AVW Proposition 11, not an innovation here.

Under strict vertex disjointness, if the six terminal occurrences of different paths share a vertex, return NO. The equality s_i=t_i within one pair is allowed: that path is necessarily trivial in a DAG. Give each label a private new sink z_i after ALL original vertices in the common topological order, and add only the label-i edge t_i->z_i. The requested family exists iff there are disjoint labelled s_i--z_i paths in these graphs: delete the final edge in one direction, append it in the other. All edges of every label go forward in one common topological order. Write N=O(n) for this order's size, padded to a power of two by isolated vertices. There is no shortestness assertion about added edges; shortestness was already enforced in the original E_i.

Private sinks address early targets: a token can finish at z_i while any unfinished token is still at an original vertex, hence smaller than z_i. It never has to leave z_i before all tokens reach their private sinks. Intersections with other paths' original targets or sources are still ordinary vertex collisions, so are forbidden. Sources and sinks retain their labels.

The algorithm below actually solves the more general problem of three labelled allowed-edge subgraphs on a common DAG order; it does not assume that their edge sets coincide.

## 2. Exact frontier graph

Use ranks 0,...,N-1. A state q=(q_1,q_2,q_3) is valid iff its coordinates are pairwise distinct. Its rank is rho(q)=min(q_1,q_2,q_3). Seed F(s_1,s_2,s_3)=1, all other entries zero. From a valid q, let i be its unique minimum coordinate, u=q_i. For every edge (u,x) of label i, add the transition q -> q[i:=x] iff the target is valid. Necessarily x>u, and every unchanged coordinate is >u, so rho strictly increases.

**Frontier lemma.** Reachability of (z_1,z_2,z_3) in this state graph is equivalent to the requested disjoint labelled paths.

For soundness, along a state walk append each moved edge to its labelled prefix. The coordinate always records that prefix's last vertex. Every abandoned prefix vertex was the unique minimum when abandoned; since rho strictly increases, all abandoned vertices are strictly smaller than every coordinate of the present state. A new vertex x>u cannot equal any abandoned vertex. Validity of the new tuple prevents equality with another current prefix endpoint. Thus induction proves disjoint prefixes, and a state walk to the sink tuple gives the desired paths.

For completeness, fix disjoint labelled s_i--z_i paths. Starting at the source tuple, advance the unique minimum token along its fixed path. If some path is unfinished, the minimum token cannot be a finished sink: every unfinished position is an original vertex, smaller than every z_i. The chosen step therefore exists. The new tuple is valid by disjointness. Every step consumes one path edge, so the process terminates at the sink tuple. This proves the lemma. It also explains why F at an arbitrary tuple should NOT be equated with all possible disjoint prefixes; only frontier-state reachability is used.

Let A_i(u,x) be label i's Boolean adjacency matrix. Equivalently every valid target p receives, for each i and each u<rho(p), the contribution

    F(p[i:=u]) AND A_i(u,p_i).

The minimum-coordinate condition, rather than a total ordering on all tuple entries, is what permits the following schedule.

## 3. Recursive schedule and exact invariant

Solve(l,r) finalizes all state entries with rho in [l,r]. At call entry all transitions whose source rank is <l and whose target rank lies in [l,r] have already been applied, and no entry of a smaller rank will change. Seeds remain present throughout. For l=r return: no transition has equal source/target rank. Otherwise h=(l+r)//2, L=[l,h], R=[h+1,r], and b=|L|=|R| (power-of-two padding). Execute:

1. Solve(l,h).
2. For each moved label i apply exactly all transitions with source minimum in L and target minimum in R, using products defined below.
3. Solve(h+1,r).

All source entries in step 2 are final by step 1, and step 2 writes only entries with minimum in R. This proves the call invariant by induction. More explicitly, each transition u=rho(source)<v=rho(target) is applied at the unique recursion node whose left half contains u and right half contains v. No transition or dependency is omitted.

Here are the exact products for step 2. Fix label i, and list the other labels as j,k. Put S=[h+1,N-1], T=[r+1,N-1]. For a context c=(y,z), define

    B(c,u)=F(q),  q_i=u, q_j=y, q_k=z,  u in L.
    C(u,x)=A_i(u,x).

Only contexts y,z in S are used, so the source minimum is indeed u. Invalid source tuples have B=0. A Boolean product D=B C gives all one-edge contributions for these fixed contexts. Partition the outputs into the following three disjoint classes:

    A: contexts S x S,       changed coordinate x in R;
    B: contexts R x S,       changed coordinate x in T;
    C: contexts T x R,       changed coordinate x in T.

They exhaust all outputs with every coordinate >h and at least one coordinate in R, i.e. exactly target minimum in R. When the moved coordinate is in T, the first unchanged coordinate in R selects B or C. Ignore outputs with repeated coordinates, and OR the others into F. Thus every product represents precisely the transition rule. The fixed-context rows do not discard path-label information or merge witness requirements across different contexts: each nonzero matrix entry has one actual predecessor tuple and one label-i edge. The proof uses no unsupported witness factorization.

A single unmasked product writing all target minima >h would be too expensive at small recursion nodes. The R/T output partition is essential, and is the substantive scheduling step.

## 4. Complete cost, including packing/scattering

Use square b-by-b products, padding final row/column groups by zeros. There are at most N^2 context rows in class A and b output columns. Hence at most ceil(N^2/b)=O(N^2/b) square products. Class B has at most bN context rows and at most N output columns; hence O((bN/b)(N/b))=O(N^2/b) square products. The same holds for C. Three moved labels only change constants. Since N and b are powers of two and N/b>=1, padding/ceilings obey these bounds uniformly down to b=1.

Each square product costs O(b^alpha) arithmetic operations by the seven-product Strassen recursion. Filling both factors, reading the O(b^2) output, applying repeated-coordinate masks and OR-scattering cost O(b^2), which is included because alpha>2. It is permissible to repack the same source block for different output-column blocks: this cost is charged for EVERY square product, not assumed free. Enumerating rows/columns, including zero/invalid contexts, obeys the same bound. A node therefore costs O(N^2 b^(alpha-1)).

At a level of nodes with half-size b there are N/(2b) nodes. Its cost is O(N^3 b^(alpha-2)). Summing over b=1,2,...,N/2 (powers of two), alpha>2 gives O(N^(alpha+1)). Initializing/scanning the N^3 table and O(N^2) adjacency matrices is included. No N^3 work is charged at each of N recursion nodes: the explicit block schedule above is required. Recursive traversal needs only the table, adjacency, current O(b^2) block workspace and O(log N) stack, for O(N^3) words.

For clarity, Boolean products are evaluated as integer products of 0/1 matrices followed by the test '>0', NOT parity products. Strassen subtraction is performed over integers. At depth d its input entries have magnitude at most 2^d; leaf products are at most b^2; recombination sums at most four terms per level, so all intermediate integers have magnitude at most b^4 (up to a fixed constant). They thus have O(log N) bits. Unit-cost word arithmetic is sufficient. Even elementary O(log^2 N)-cost multiplication yields O(N^(1+alpha) log^2 N) arithmetic-bit work. Since 7^10<2^29, alpha<2.9; more precisely alpha<2.81, so this is O(n^3.9). Hence delta=1/10 is a conservative valid constant, without any appeal to the best current matrix exponent. In the source word model the stronger unrounded exponent 1+alpha holds.

## 5. Endpoint convention extension

If disjointness permits a vertex to be shared only as an endpoint of BOTH paths, let U be all terminal vertices. Remove each original v in U from the shared-vertex universe. For every label i having v as an endpoint make one private copy v_i; label i may use only its own endpoint copies. A label for which v is not an endpoint cannot visit v. Map original tight edges to these copies in their own label, and forbid entering its own source or leaving its own target except for the completion edge. Copies of one original vertex occupy consecutive positions at its original topological rank; no original edge joins equal original ranks. Shared nonterminals retain one shared copy. There are at most six endpoint copies plus N nonterminals. Mapping paths in either direction proves equivalence: common endpoints are separated, and every illegal internal intersection remains a shared-vertex collision (or is forbidden as a terminal visit). For s_i=t_i keep its one private endpoint and its completion edge, so the zero-edge original path is represented.

If 'internally disjoint' is instead read in the weaker sense that ONLY two internal-vertex sets must be disjoint, keep also a shared internal copy of each v in U for labels for which v is not an endpoint. This permits an endpoint/internal coincidence and still forbids two internal uses. Mapping has the same elementary equivalence proof. Under strict vertex disjointness no copying is done and repeated endpoints of different paths are immediately infeasible. Thus all these endpoint interpretations are explicitly accommodated rather than silently choosing a restriction.

## 6. Evidence, dependencies and remaining review obligations

The self-contained proof depends only on topological shortest-path relaxation, the frontier lemma proved above, the explicit recursion/product invariant, and Strassen's seven-product multiplication identities. Tests in frontier_check.py implement the actual square-product schedule using exact-integer Strassen (not a simulated uncharged dense tensor operation); all 684 tested entire state tables match the scalar recurrence, and all final answers match independent shortest-path enumeration. See frontier-check.json for exact finite coverage. These are bug checks, not the proof of the theorem.

No mathematical gap is currently identified by the proposer. Correctness of the recursive invariant, its globally charged data movement, the terminal normalizations, source-model compatibility, novelty and substantive significance require a fresh adversarial referee. No independent review has yet occurred. The claimed substantive delta is a polynomial exponent saving for ALL weighted DAG instances at k=3, directly answering the immutable existential question; it is not the known frontier recurrence, shortest-path preprocessing, or Strassen algorithm alone. Current bounded primary-source searches found no matching result; this is not a priority certificate. No manuscript/PDF is authorized at this stage.
