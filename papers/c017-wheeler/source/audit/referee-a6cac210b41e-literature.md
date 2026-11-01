# Fresh primary-source comparison

Job: `c017-wheeler-referee-a6cac210b41e`. Checked 2026-11-01 UTC.
This is the present referee's bounded source comparison, not a priority certificate.

1. D'Agostino and Paradiso, *Finite-State Transducers in the Wheeler Setting*,
   [arXiv:2606.29405v3](https://arxiv.org/html/2606.29405v3), 13 August 2026.
   The [live history](https://arxiv.org/abs/2606.29405) still lists v3 as latest.
   I read the frozen PDF's model, Definitions 4–5, Remark 3, the finite-index
   characterization and Section 4, and independently opened the live text.
   The model agrees with source.md. Remark 3 supplies the residual-LCP identity;
   the characterization does not supply an effective membership test.

2. A newer primary publication, absent from the frozen literature notes, was
   found during this review: the same authors/title, ICTCS 2026, CEUR Workshop
   Proceedings 4269, pp. 66–70, published 19 September 2026.
   [Official proceedings](https://ceur-ws.org/Vol-4269/) and
   [complete five-page paper](https://ceur-ws.org/Vol-4269/paper46.pdf).
   I read its definition, characterization and concluding problem statement.
   Definition 3.1 retains finite piecewise monotonicity; Theorem 3.6 is a
   finite-index characterization. Section 4 on p. 69 still explicitly poses
   membership and equivalent realizability. This later version does not
   supersede the candidate with a decision theorem.

3. Béal and Carton, *Computing the prefix of an automaton*, RAIRO TIA 34(6)
   (2000), 503–514. [Journal record](https://www.numdam.org/item/ITA_2000__34_6_503_0/)
   and [original scan](https://www.numdam.org/item/ITA_2000__34_6_503_0.pdf).
   I inspected the abstract and introduction, pp. 503–504: prefix normalization
   followed by ordinary minimization is classical, including empty-labeled
   cycles. Those ingredients are not a novelty of the reviewed claim.

4. Blumensath, *Automatic Structures*, diploma thesis (1999), Theorem 3.4,
   Definition 3.9 and Proposition 3.10, printed pp. 11, 13–14.
   [Author's scan](https://www.fi.muni.cz/~blumens/Publications/AutStr.pdf).
   I read the frozen scan and inspected local renders of these pages because
   its extraction is imperfect. They justify regular representatives and
   effective first-order queries, with padding for longer quantified words.
   The [official Blumensath–Grädel LICS 2000 record, pp. 51–62](https://lics.siglog.org/archive/2000/BlumensathGradel-AutomaticStructures.html)
   independently confirms the effective-query result. The canonical convex
   quotient's automata operations are standard applications of this machinery.

5. Becker, Cenzato, Kim, Kodric, Policriti and Prezza, *Optimal Wheeler Language
   Recognition*, [arXiv:2306.04737v2](https://arxiv.org/abs/2306.04737).
   I checked the primary abstract: its O(mn) theorem concerns whether a DFA's
   language has a Wheeler realization. It does not test accumulated output
   piecewise monotonicity. I do not claim an exhaustive inspection of its proof.

6. Filiot, Lhote and Reynier, *Lexicographic Transductions of Finite Words*,
   [MFCS 2025, DOI 10.4230/LIPIcs.MFCS.2025.50](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2025.50).
   The official abstract concerns lexicographic transduction models and
   exponential growth, not the finite convex output-partition test here.

7. The auxiliary fixed-pump Presburger translation uses classical decidability.
   The Cooper scan URL in the packet timed out in this review; I do not claim
   to have refreshed that scan. The modern primary
   [Haase et al., ICALP 2024, DOI 10.4230/LIPIcs.ICALP.2024.142](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2024.142)
   was opened. No existential-block runtime is transferred to the mixed
   formulas. Neither the membership algorithm nor its polynomial bound uses
   a Presburger solver or this auxiliary verification route.

Searches included exact title and author searches; Wheeler transducer membership,
algorithm, decidability and realizability; piecewise monotonicity and colex
transducers; and SCC/finite-state variants. Third-party summaries were discovery
aids only. No inspected primary equivalent decision theorem was found. Retrieval
failures for a conference homepage, an index endpoint and web PDF screenshots
were operational limitations; the actual conference paper and local automatic
structure scan were available and read. This does not prove universal priority.

The substantive delta is the complete membership SCC criterion and its polynomial
implementation: finite convex partition existence becomes finitely many exact
regular-range tests, while every output failure has a disjoint pumped-turn
certificate. The standard normalization/automatic quotient gives a useful
combined realizability consequence. Neither standard normalization nor automatic
closure is itself an independent innovation here.
