# Revised mathematical self-audit — 2026-10-31

This is a self-audit, not a separate-agent, proof-assistant, or independent human review. No skills or sub-agents were used.

## A: quantitative equivalence

Closure -> APSP uses one doubled graph plus quadratic strong/tight postprocessing. The new reverse direct embedding uses one program variable per graph vertex; its two signed components are disjoint, and every complementary distance is infinite when the graph has no negative cycle. The input graph has a negative cycle exactly when the encoded system is bottom. Integer potentials witness feasible difference-only instances. Thus the positive block recovers all graph distances, and dense exponents agree.

The feasible-DAG promise uses the retained three-layer min-plus reduction and logarithmically many products for APSP. All weights remain polynomially bounded; rational closure outputs are half-integral and fit the stated word model. The explicit oracle-budget calculation remains valid. The equality of exponents contains more information than a coarse existence-of-subcubic-algorithms equivalence.

## Imported October 2026 bounds

Four exact v1 primary PDFs and theorem statements were checked; see `2026_literature_check.md`. Deterministic min-plus interfaces handle arbitrary raw closure inputs through repeated squaring and a negative-diagonal test; integer parity failure is tested afterwards. Logarithmic factors are absorbed by soft-O or n^o(1), without claiming a new APSP algorithm. No assertion depends on an active traditional cubic APSP hypothesis.

## B: feasibility/model construction

The original proof is retained. Symmetrization of an integer potential gives a half-integral antisymmetric model. Only tight edges joining half vertices constrain rounding. A conflicting SCC forces an odd equality on twice an integer; otherwise a topological rank choice rounds compatibly. Mixed-fraction and non-tight edges have enough slack. The original Lahiri–Musuvathi criterion is related to this symmetrized test in both directions. The expected near-linear bound is a composition with modern SSSP.

## C: unconditional update/query relation

The initial 4r-variable state has no paths of length two and is already canonical. r bridges activate r candidate indices. r² exact-entry queries recover the product, at cost O(r²+P(4r)+rU(4r)+r²Q(4r)). Substituting exponents yields alpha_APSP <= max{2,p,1+u,2+q}, without any hardness hypothesis. Randomized structures require the corresponding randomized exponent convention. The separate designated-cell write lower bound remains unconditional and concerns its explicit interface.

## D: bounded-width interfaces and transfer

The signed-bag lift has width at most 2t+1. Elimination costs O(n(k+1)²); records have O(n(k+1)) size. Up/down distance queries cost O(n(k+1)); reverse reinsertion computes all pairs in O(n²(k+1)). Three distance queries decode a canonical octagon entry. Integer feasibility is assumed or checked separately. The width-one quadratic output obstruction remains valid. The old APSP-based width lower bound is removed; a generic O(n²(k+1)^beta) algorithm instead transfers to an O(n^(2+beta)) min-plus algorithm. Choosing the better of width reconstruction and general APSP is an upper bound, not a matching-width optimality assertion.

## Artifact and limitations

The original 6,750 cases are retained; 500 direct embedding cases were added. The separate ELINA comparison remains 1,000 cases and 389,512 entries. Full input/output fixtures, summaries, logs and pinned kernel source are included. A randomness-free archive replay passed all cases. Finite checks do not provide formal proof certificates or establish novelty. The imported graph primitives and normalization results retain their original attribution; STOC-level originality remains for independent assessment.
