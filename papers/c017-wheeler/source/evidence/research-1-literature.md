# Current primary-source comparison for research pass 1

Job c017-wheeler-research-8ca2b0cef7a6; inspected 2026-11-01 UTC.
This is a bounded literature screen, not an exhaustive priority claim or a
fresh referee novelty verdict. Search results from third-party reviews were
not used as mathematical premises.

1. Giovanna D'Agostino and Andrea Paradiso, *Finite-State Transducers in the
   Wheeler Setting*, arXiv:2606.29405v3, revised 13 August 2026.
   Primary abstract/history: https://arxiv.org/abs/2606.29405
   Primary full text: https://arxiv.org/html/2606.29405v3
   The live abstract still names v3 as current. Rechecked Definition 4
   (finite convex partitions, either weak orientation per piece), Definition 5
   (total reaching-language order and transition-output piecewise monotonicity
   at each state), and Section 4 (membership decidability stated unresolved,
   distinct from equivalent realization and minimization). The proof proposed
   here addresses that exact machine-membership question, including erasing
   outputs. No quotient or Choffrut characterization result is a dependency.

2. Ruben Becker, Davide Cenzato, Sung-Hwan Kim, Bojana Kodric, Alberto Policriti
   and Nicola Prezza, *Optimal Wheeler Language Recognition*,
   arXiv:2306.04737v2, revised 18 December 2023.
   https://arxiv.org/abs/2306.04737
   Rechecked primary abstract: the O(mn) result decides whether a DFA's accepted
   language admits a Wheeler presentation. It is not the transition-output
   condition or this full transducer membership problem. No claim about the
   paper's full proof or absence of useful techniques is made.

3. Giovanna D'Agostino, Davide Martincigh and Alberto Policriti,
   *Ordering Regular Languages: A Danger Zone*, 2021.
   https://ceur-ws.org/Vol-3072/paper5.pdf
   Rechecked primary abstract and opening structural definitions. It treats
   Wheeler automata/languages and alphabet-order variants; the graph conventions
   are stronger than the literal reaching-language condition in the frozen
   source. The proposed block proof derives what it needs directly and does
   not import those stronger graph hypotheses or an output algorithm.

4. Emmanuel Filiot, Nathan Lhote and Pierre-Alain Reynier,
   *Lexicographic Transductions of Finite Words*, MFCS 2025,
   LIPIcs 345, 50:1-50:18, DOI 10.4230/LIPIcs.MFCS.2025.50.
   https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2025.50
   Rechecked official primary abstract/metadata: lexicographic transductions
   concern exponential-growth models, MSO set interpretations and inverse
   regularity. The inspected statement is not a finite piecewise colex
   monotonicity decision. No exhaustive full-text exclusion is claimed.

Queries repeated during this research job included exact 'Wheeler transducers'
membership/decidability/algorithm; 'piecewise monotone' transducer/decidability;
rational functions lexicographic order preserving decidable; finite state
transducer finite piecewise monotonicity lexicographic order; and lexicographic
monotonicity sequential decidable transducers. No inspected primary result
already resolving the exact current-v3 membership problem was found. The search
also produced unrelated prefix-order monotonicity, output-origin order, numerical
hysteresis and lexicographic-output-construction notions; none was treated as
an equivalent theorem. The source itself is the nearest verified prior result.

## Proposed substantive delta, conditional on fresh review

The proposed algorithm is a complete finite original-scope decision, with a
conservative polynomial upper bound, not a corollary deciding only input order
or one-piece output monotonicity. Its additional structural step classifies
cyclic components: a branching component can only survive with globally
monotone state functions, while a simple cycle has an exact two-side annular
criterion and at most two pieces per state. Rejecting components construct
single-pump disjoint-turn certificates. This changes the unbounded partition
quantifier into finitely many exact tests on independent regular output ranges.
That is the claimed mathematical contribution and potential theoretical value;
its originality and significance must be decided by the actual fresh referee.
