# Research pass 2: bounded primary-source recheck

Job `c017-wheeler-research-98a17f8eb2fd`; checked live 2026-11-01.
This supplements the unchanged membership comparison in
`evidence/research-1-literature.md`. It is neither a priority guarantee nor a
fresh novelty verdict. Only primary sources are used as mathematical premises.

1. D'Agostino and Paradiso, *Finite-State Transducers in the Wheeler Setting*,
   [arXiv:2606.29405v3](https://arxiv.org/html/2606.29405v3), 13 August 2026.
   The [live version history](https://arxiv.org/abs/2606.29405) still lists v3.
   Sections 2-3 define the frozen machine property. Section 4 still explicitly
   poses membership and equivalent Wheeler realizability as decision problems.
   Section 3.2, Remark 3 already gives the statewise residual-LCP identity and
   monotonicity transfer used here. Theorem 3.1 characterizes realizable functions
   by finite index and a monotonicity condition; it is not an effective algorithm
   for checking those conditions. Lemma 8 isolates epsilon. The current reduction
   gives an explicit terminating construction via a different, output-free
   convex-color relation followed by the membership decider. These known
   identities, the convex-refinement idea and epsilon isolation must be credited.
   The source's unary floor-length example is an adverse control, not a new example.

2. Marie-Pierre Béal and Olivier Carton, *Computing the prefix of an automaton*,
   RAIRO Theoretical Informatics and Applications 34(6) (2000), 503-514,
   [original journal scan](https://www.numdam.org/item/ITA_2000__34_6_503_0.pdf),
   [publisher/archive record](https://www.numdam.org/item/ITA_2000__34_6_503_0/).
   Inspected the abstract and introductory account of normalization and
   minimization, especially pp. 503-504 and the beginning of Section 2. It
   identifies prefix pushing followed by ordinary minimization as the known
   sequential minimization route and explicitly accommodates empty-labeled
   cycles. Thus the onward normalization/merging ingredient is classical.
   The present proof supplies a direct regular-range LCP algorithm and complete
   residual-equivalence argument, without transferring that paper's runtime bound.

3. Achim Blumensath, *Automatic Structures*, diploma thesis, RWTH Aachen,
   October 1999, [author's original scan](https://www.fi.muni.cz/~blumens/Publications/AutStr.pdf).
   Inspected the existing local original `intake/blumensath-1999-automatic.pdf`,
   Sections 2.1, 3.1 (Theorem 3.4) and 3.2 (Definition 3.9 and Proposition 3.10).
   The scan's text extraction is imperfect, but the definitions and proof text
   are readable. Theorem 3.4 selects regular least representatives to obtain
   an injective presentation. Section 3.2 constructs first-order queries using
   Boolean operations and projection, explicitly accounting for longer tuple
   components by padding. These are exactly the standard ingredients needed
   for E and Rep. The local extracted text is an input aid, not original work.
   The [official LICS 2000 record](https://lics.siglog.org/archive/2000/BlumensathGradel-AutomaticStructures.html)
   confirms Blumensath and Grädel, *Automatic Structures*, pp. 51-62, and its
   effective first-order-query result. No arbitrary rational-relation closure
   is used or inferred.

Additional live queries included `"Wheeler transducers" "decidability"
realizability`, `"Wheeler" "transducer" "equivalent" 2026`,
`"Wheeler transducer" "realizability" decidability canonical`,
`"Wheeler transducers" algorithm decidable realizability`, and classical
subsequential longest-common-prefix/minimization terms. A University of Udine
institutional record for the same title appeared in search, describing the
characterizations rather than a new decision algorithm; direct retrieval
returned a cache miss, so no unavailable text is relied on. Third-party paper
summaries and obsolete-v2 criticism were excluded as proof or novelty premises.
Searches found no inspected current primary equivalent decision theorem.

**Value boundary.** The new realizability consequence is a useful effective
connection of the membership theorem to the second explicit source question.
Its normalization, LCP identity, convex right-invariance and regular quotient
machinery are known/routine ingredients. It does not supply an independent
innovation sufficient for a separate paper; the combined candidate's substantive
delta remains the complete SCC criterion for the original membership problem.
No polynomial realizability bound, optimality, minimization, practical indexing
improvement, STOC quality or external acceptance is claimed. Fresh review must
assess the exact combined scope against these sources and current equivalents.
