# KF26 publication, inference, and software distinction

Checked 2026-10-31. This follow-up used only primary sources and static source inspection. No top-level benchmark script was executed. No manuscript, frozen input, source repository, or PDF was changed.

## Publication and official export

[The official PMLR record](https://proceedings.mlr.press/v306/kim26l.html) lists Jihwan Kim and Chenglin Fan, *Robust and Consistent Ski Rental with Distributional Advice*, Proceedings of the 43rd International Conference on Machine Learning, PMLR 306:57411–57444, 2026. Its native BibTeX key is `pmlr-v306-kim26l`; no DOI is supplied. The unmodified official HTML citation block is saved as `classical-kf26-official.bib`, preserving its fields, order, text, and whitespace after decoding HTML entities. If the manuscript's `KF26` entry is replaced with this publication, synchronize the key deliberately.

The [officially linked original published PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/kim26l/kim26l.pdf) was independently retrieved completely into memory: 560,062 bytes, valid PDF header and terminal EOF, successful full `pdftotext` extraction, 34 pages. SHA-256: `5c5842ff3d0d2df8b802bc9968d520410ade6a059f83b3ca9fb1ac6a8f53ec4c`. The local root copy previously reported partial was not used. Evidence is `classical-kf26-published-source.txt` and `classical-kf26-published-provenance.json`.

## Published Appendix D.2 versus arXiv v1

The critical inference appears in both the published Appendix D.2 (printed pages 29–30, sentence on page 30) and [arXiv:2603.29233v1 Appendix D.2](https://arxiv.org/html/2603.29233v1#Sx4.SS2). The published version still equates minimum feasible support level with the linear expected-cost optimum. Its single quoted sentence, 17 words, is:

> Therefore the optimal objective value equals the minimum feasible h, which can be found by binary search.

No claim that the complete documents are identical is made. The checked passage and mathematical inference are the same. The arXiv extraction duplicates some MathML/TeX symbols in its raw text; this does not change the displayed sentence. Its local excerpt is `classical-kf26-arxiv-D2-source.txt`.

## Ideal support-level problem and literal author code differ

For b=3, R=3/2, and forecast probabilities p(1)=2/5, p(2)=3/5, the original cost model gives g(1)=3, g(2)=14/5, and g(t)=8/5 for t≥3. The ideal minimum support-level problem has h*=14/5: lower levels require T≥3 and hence moment at least 2, exceeding the budget 3/2. At h*=14/5 the feasible law is f(2)=f(3)=1/2, with expected cost **11/5**. This number belongs to that conceptual support-level construction.

The [official Table 2 source at the pinned commit](https://github.com/JihwanKim4689/distributional-ski-rental/blob/0a86125f31e9e1b1abbba5bd4fde32a332860124/Table2_Consistency_Comparison_under_Fixed_Robustness.py) was independently inspected; the local checkout's HEAD matches this commit. Its unchanged class has additional boundary/moment-update behavior. Static tracing predicts:

| Candidate level | Class calculation | Outcome |
|---|---|---|
| 14/5 ≤ h < 3 | First segment contributes zero mass. Subsequent atoms give F=1/2, μ=1, then F=3/4, μ=7/4. The remaining-tail scan has no forecast day greater than b. | Rejected |
| h ≥ 3 | First geometric step gives F=1/4, μ=0. The day-2 atom adds 3/8, then the day-3 atom adds 3/8. | Accepted with total mass 1 |

Accordingly, the class's `construct_policy_pmf` is predicted to return `{1:1/4, 2:3/8, 3:3/8}`, with its `expected_cost` equal to **12/5**. Its binary search approaches level 3. This is a static trace, independently supporting the root's direct unchanged-class reproduction; this helper did not execute the class or benchmark.

The source's local updates include `mu += mass * s`, a first segment whose integer range starts at zero, scanning through b, and tail candidates restricted by `bisect_right(self.days, b)`. These details explain why the literal implementation need not match the ideal support-level construction. They are separate issues from the logical implication in Appendix D.2. Describe the conceptual counterexample and software reproduction separately, with the pinned commit and tolerance for the latter; do not attribute the conceptual **11/5** result to a literal run of this code.

The draft's expected-cost optimum on the same instance is a third quantity, **39/20**, attained by f(1)=1/4 and f(3)=3/4. Thus neither **11/5** nor **12/5** should be described as the exact expected-cost optimum.

Machine-readable metadata, the quotation count, and the static trace are in `classical-kf26-audit.json`. Empirical execution output and any final manuscript edits belong to the root task.
