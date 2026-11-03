# Pass 2: exact ultrametric reduction and the remaining branching kernel

Job c037-msthalf-research-d9c4fc8e3237. This is a research record, not a
candidate or manuscript. The immutable source question is unresolved.

## Exact bookkeeping

Represent a finite ultrametric by its reduced rooted hierarchy. Leaves are
vertices, each internal node a has k_a>=2 children and height h_a>0, and
heights strictly increase toward the root. Distances between distinct leaves
are their least common ancestor's height. This representation allows arbitrary
depth, unequal heights and child sizes; zero-length hierarchy edges can be
contracted. For an arbitrary permutation P, let N_a be the number of its
consecutive pairs whose LCA is a. Then exactly

    cost_d(P) = sum_a h_a N_a,
    MST(d)    = sum_a h_a (k_a-1).                     (U)

The first identity partitions consecutive pairs. For the second, induction
connects the k_a child MSTs with k_a-1 edges of weight h_a. Conversely any
spanning tree must connect those child components, and Kruskal's procedure
makes exactly those merges at each height. Equivalently integrate the number
of threshold components minus one. This is standard bookkeeping, not claimed
new mathematical innovation.

## Thin-child bound: a proved partial reduction

Fix integer r>=1. At each internal node choose a largest child L_a (ties
arbitrary). Call every other child with at most r leaves small. An adjacency
whose LCA is a and with an endpoint in a small child is called a small-child
adjacency; count it once even if both endpoints are in small children.
For each a,

    # small-child adjacencies at a
       <= 2 sum_{small C child of a} |C|
       <= 2r (k_a-1).

Indeed, each leaf has at most two incidences in a path, and an LCA-a adjacency
between two different children other than L_a, or between L_a and another
child, is incident to at least one such non-largest child. The displayed
bound on small-child adjacencies is valid even when there are multiple large
children. Consequently their total true cost is at most 2r MST(d), by (U).
This uses neither the rectangle condition nor order weights.

In particular, if every node has at most one child of size >r, EVERY
permutation has true cost <=2r MST(d), regardless of q or H. Arbitrarily deep
comb hierarchies with singleton side children even satisfy 2 MST(d). Thus a
comb-only positive experiment cannot test the difficult part of (K).

The remaining adjacencies have, at their LCA, two endpoint children of size
>r, except possibly when the chosen largest child itself has size <=r (then
there are no remaining adjacencies). Call their cost B_r(P,d). Proving

    B_r(P,d) <= C_eta r [W + MST(d)]                  (B)

under the original rectangle-density/domination hypotheses is sufficient
for the original ultrametric version of (K), with constant C_eta+2.
This is a reduction inside that sufficient route, not an equivalence to
source.md and not a general metric result. (B) remains UNPROVED.

## Exact nonuniform attack and interpretation

`ultrametric_nonuniform_check.py` generates 180 finite configurations with
n in {8,12,16,24,32}, balanced/comb/random merge shapes, constant or widely
unequal integer height increments, and two deterministic sampled orders.
For each it begins with q_i=d(v_i,v_{i+1}) and performs two randomized-order
coordinate sweeps minimizing individual nonnegative INTEGER q_i, preserving
the rectangle condition. This is coordinate descent, not global optimization.
The fixed seed is 3702. The configurations check r=2 with required rectangle
edge counts 1 or 2 and, for n<=12, r=3 with count 2. For n>16 only r=2,count=1
is tested. All saved witnesses include the complete metric in order, optimized
weights, exact costs, independently recomputed MST and minimum rectangle count.

For each r-subset A, sort the H-degrees into A of all vertices outside A.
The sum of the r smallest degrees is exactly the smallest number of H-edges
in A x B over disjoint r-subsets B. This proves completeness of EACH witness's
rectangle verification; it does not make the hierarchy/weight search complete.
Larger rectangles inherit the same density by averaging over r-subsets.

The run made 17,224 exact feasibility calls and saved 180 witnesses. Its
largest cost/[r(W+MST)] is 1053/1177. No counterexample was found. That is
finite evidence only. The comb family is mathematically controlled already;
the balanced and random families test genuinely branching cases, but no
uniform theorem follows. Further attacks should focus on B_r, rather than
repeat comb or uniform-weight checks.

## Full-original dependency map

- KNOWN primary: Anand et al. arXiv:2610.40594v1, Lemma 3.2 provides an
  all-unmarked comparison tree of O_p(1) expected true cost on its event F.
- PROVED in previous research evidence: uniform mask rectangle event,
  observable minimum rectangle-dominating tree enumeration, comparison-tree
  feasibility, and failure-event expectation control.
- PROVED here as standard partial bookkeeping: (U), small-child cost <=2r MST.
- UNRESOLVED: (B) for arbitrary branching ultrametric hierarchies with
  nonuniform q, and extension from ultrametrics to all metrics with no extra
  logarithm. Naive threshold components only give a bottleneck LOWER bound
  on a general metric, so their direction cannot certify true cost.
- UNRESOLVED full target: O_p(log n) expected TRUE MST approximation for
  every fixed p<1/2 under omniscient post-mask replacements.

No all-algorithm lower bound below one half, candidate, novelty acceptance,
fresh referee, STOC assessment, claim.json or manuscript/PDF is asserted.

## A sharper, falsifiable next kernel and an exact stress family

The finite witnesses support the stronger proposed assertion

    B_r(P,d) <= 4r W                                  (B4)

using only nonemptiness of every disjoint r-by-r H-rectangle. This is
UNPROVED, not a candidate or an assertion equivalent to the original. If it
holds, the proved small-child bound gives K with 4rW+2r MST for all
ultrametrics. It would still need an all-metric extension.

A parametrized exact stress family rules out constants below 3 for a fixed
positive rectangle density, and approaches 4 as the allowed density tends
to zero. Let r>=2 and r<m<2r, n=2m, two true clusters each of size m, true
within-cluster distance delta>0 and intercluster distance M>=delta. Alternate
the cluster colors in the order, set every q step to delta except the step
between positions m and m+1, which is M. Then

    B_r = (2m-1)M, W=M+(2m-2)delta,
    MST(d)=M+(2m-2)delta.

Take H to be all pairs d<=q. All cross pairs between the two order halves
are in H, since their q-distance is at least M. For any disjoint r-sets
A,B, write a,b for their counts in the first order half, and s=a+b. Since
both order halves have m vertices,

    2r-m <= s <= m,
    #H(A,B) >= a(r-b)+(r-a)b
             = rs-2ab >= s(2r-s)/2 >= m(2r-m)/2.

The last step minimizes a concave quadratic over the stated interval,
whose endpoints have equal values. Thus the full rectangle density is at
least m(2r-m)/(2r^2), not merely positive; averaging handles larger sets.
Every root child has m>r leaves, so every order adjacency contributes to B_r.
As M/delta tends to infinity, B_r/(rW) tends to (2m-1)/r.
For even r and m=3r/2, density >=3/8 and this ratio tends to 3-1/r;
therefore no universal coefficient below 3 can hold for B_r<=C r W even
at fixed eta=3/8. Taking m=2r-1 approaches coefficient 4, with density
(2r-1)/(2r^2). This is a stress test of (B4), not its proof or a disproof
of K/source.md. It also identifies precisely why a naive coefficient 2
cannot close the large-child charge.

ONE next test for the remaining permitted pass: prove (B4), or give an
exact parametrized counterexample, for arbitrary reduced ultrametric
hierarchies, all nonnegative order weights and every graph H dominated by q
meeting all disjoint r-by-r rectangles. Charge only adjacencies whose LCA
has both endpoint children larger than r. A proof must establish a single
hierarchy-wide bound, not sum a W bound at each level. If (B4) fails, test
whether B_r<=C_eta r(W+MST) survives; no constant fitted to finite data is
established. An ultrametric proof alone is still partial to the original.
