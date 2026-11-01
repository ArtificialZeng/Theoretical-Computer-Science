# Precise reading of the frozen question

Triage provenance: `coverage-sparse-triage-8c18589f991c`, 2026-10-31
(Asia/Shanghai). The original wording is retained verbatim in immutable
`source.md`; its SHA-256 at intake is
`eb7061a17cead0bc8cc0e4426f3f8260ac3137dd23b6f4813d8f4952b00ec731`.

## Objects and optimization

Let V be any finite set, G=(V,E) a simple undirected graph, and
x in [0,1]^V. A law is a probability distribution on 2^V. Write
P_x for all laws with P(i in S)=x_i for every i in V. Define

- D_G^=(x) = {D in P_x : P_D(i,j in S)=x_i x_j for every ij in E};
- D_G,delta^le(x) = {D in P_x : P_D(i,j in S) <= (1+delta)x_i x_j
  for every ij in E}, for a fixed finite real delta >= 0.

Nonedges are unrestricted, including their joint dependence. This is a graph
of tested pairs, not a dependency graph. Both feasible sets are nonempty:
the product Bernoulli law is feasible. The <= model with delta=0 is still
different from the equality model.

A finite feature family H consists of subsets of V, each with a finite real
weight w_H >= 0. Its weighted coverage function is
f(S)=sum_H w_H 1{S intersects H}. Empty features and zero weights are harmless;
f(empty)=0. No additional normalization or explicit feature-list size bound
is imposed. Define

f^+(x)=max_{D in P_x} E_D f(S),
f_G^=(x)=max_{D in D_G^=(x)} E_D f(S), and
f_G,delta^le(x)=max_{D in D_G,delta^le(x)} E_D f(S).

These maxima exist because they optimize a linear functional on a nonempty
closed finite-dimensional probability polytope. Restrict all ratios below to
f^+(x)>0. Their denominators are positive: a positive-weight feature with a
positive marginal is hit with positive probability under the product law.

For every integer k>=1, let C_k contain all finite k-colorable graphs and let
B_k contain all finite graphs with maximum degree at most k-1 (the empty
graph causes no issue). For A=C_k and, separately, A=B_k, determine

Gamma_A^= = sup_{G in A, x, f as above; f^+(x)>0} f^+(x)/f_G^=(x).

For every fixed finite delta>=0 determine the analogous Gamma_A,delta^le.
The finite ground set size, graph, marginals, features and weights all vary
inside each supremum. This asks for a class supremum, not equality for every
fixed G. Membership uses chi(G)<=k or Delta(G)<=k-1, not equality.

## Candidate target, not an accepted result

The proposed answer in `candidate-argument.md` is that all four suprema equal
1/alpha_k, where alpha_k=1-(1-1/k)^k. For k=1 this is 1 and follows directly
from having no tested edges. For k>=2 the proposed witness is m disjoint
k-cliques, n=mk, with x_i=1/m and k^m equally weighted Cartesian features.
It has |E|=n(k-1)/2, so its pair count is linear in n for each fixed k.
The candidate finite certificate is

alpha_k <= f_G^=(x) <= alpha_k+(k-1)/(2km), f^+(x)=1,

and with <= constraints the upper error term is multiplied by 1+delta.
The limiting operation is m -> infinity with k and delta fixed. Allowing
delta to grow with m is outside that stated limit; no uniform robustness
for unbounded errors is asserted. Approaching e/(e-1) also lets k grow:
the candidate supplies O(n/epsilon) pairs for O(epsilon) accuracy, not an
optimal necessity theorem in the edge budget. The exact matching-family
formula in the candidate is subsidiary and must be checked separately.

## Prior result, proposed delta, and verification route

Ramachandra, *Dimension Dependent Correlation Gap Bounds under Restricted
Independence*, arXiv:2609.02659v1, Theorem 2 and Section 4, already supplies
the Cartesian coverage construction and an asymptotic e/(e-1) lower bound
under all-pairs independence, with both block parameters growing. It must
receive attribution. Dütting et al., *The Cost of Consistency: Submodular
Maximization with Constant Recourse*, arXiv:2412.02492, Section 3.2, supplies
closely related two-block coverage decorrelation with factor 3/4.
The fresh search also located *Online Submodular Welfare Maximization:
Computation is not the Bottleneck*, arXiv:2610.16060, Sections 1.2 and 3.1:
it uses the same Cartesian probability-coverage formula and alpha_k constant
in an online allocation model. Neither the constant nor the coverage family
itself is a proposed novelty claim. See `evidence/triage-literature.md`.

Proposed delta: a sharp fixed-k graph-class hierarchy, tight even for maximum
degree k-1 with linearly many tested pairs, together with a finite certificate
for fixed one-sided multiplicative errors. Verification route: independently
check color-class resampling, per-feature AM-GM/concavity, the deterministic
occupancy inequality and its moment averaging, all boundary cases, and
whether an existing multi-block theorem already subsumes the graph result.

Source status: `new-question`; novelty of the proposed delta is unverified.
No assertion is made that this is a recognized open problem. An arbitrary
monotone submodular extension, fixed-graph characterization, optimal edge
budget tradeoff, or STOC acceptance claim is outside the frozen scope.
