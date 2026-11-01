# Experimental value provenance — revision 2

No imputed, estimated, or inferred-as-measured experimental values appear in the revised PDF.

- Tables 3–4 and Figure 3 (left) are generated from the newly measured splitter runs in `artifact/bench-results.json`, including all seven repetitions, phase times, end-to-end total, sizes and state counts.
- `n_v`, `n_e` and `n=n_v+n_e` are counted directly from generated input graphs. `2*qG*qH` is the exact product-state-space upper bound computed from the quotient sizes.
- Figure 3 (right), corpus paragraphs and Appendix B use the retained original corpus measurements in `artifact/corpus-summary.json`, `corpus-roots.json` and `corpus-queries.json`. No new corpus timing is implied.
- 6.79% is the rounded coverage ratio 4072/59949; it is not an estimate of whole-language coverage or typical code.
- 225, 2000, 3000, four frontend judgments, and 17*19=323 are enumerated check counts or exact mathematical quantities.
- Old Moore benchmark timings are preserved in history and are not relabeled as splitter timings or decomposed after the fact.

No missing tsc, Amadio–Cardelli, Palsberg–Zhao, or Scala compiler timings are filled with surrogate numbers.
