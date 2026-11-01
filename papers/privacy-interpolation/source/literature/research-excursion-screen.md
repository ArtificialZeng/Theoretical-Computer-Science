# Research pass 2: excursion / shape-restriction screen

Job `privacy-interpolation-research-294f008bff48`, research pass 2.
Inspected 2026-10-31 Asia/Shanghai. Read-only primary-source research; no
external submission or account action. This is a bounded comparison, not a
proof of priority. Pass 1 and its decision remain preserved.

## Exact proposed delta and why it merits a referee

The primary result is the exact minimum reservoir peak at **every feasible
budget for every positive swapped triplet** `(c,a,b)` to `(c,b,a)`, with
`0<a<b`, `c=1-a-b>0`. This pass extends the seed beyond `b<=1/2`.
A matching piecewise binary-flow/capped-reservoir construction proves
attainment, and scalar saturation proves uniqueness at the minimum budget.
The related global comparison identifies exactly the worst price of requiring
all coordinates monotone, or merely within their endpoint ranges: the sharp
finite-distance factor is attained from three outputs onward; binary paths
have no such penalty. The exact endpoint-envelope sweep supplies reproducible
necessary excursion certificates, sharp on the whole swap family.

The mathematical payoff is a quantitative obstruction to a natural
shape-preserving extension design: a coordinate with equal endpoint
probabilities must move outside its endpoint range to attain the optimal
budget. It is now a complete continuous tradeoff and a dimension-dependent
sharp restriction cost, not the isolated old affine example. The proof is
short and elementary; the sweep is routine supporting computation. A fresh
referee must assess whether this coherent result is sufficiently substantive
and whether an equivalent constrained statement exists elsewhere. No STOC
acceptance, novelty guarantee or universal cap-feasibility theorem is claimed.

## Primary statements inspected and comparison

1. **Dong, Roth and Su, Gaussian Differential Privacy**, arXiv:1905.02383v3,
   https://arxiv.org/html/1905.02383v3 . Theorem 2.10, continuous-group-privacy
   Laplace limit (Theorem 2.14 / Proposition 2.15), and Lemma A.6 were already
   inspected in pass 1; the primary HTML was reopened in this pass. The prior
   dossier correctly derives abstract unrestricted reachability from those
   testing/Blackwell facts. That unrestricted theorem remains credited prior
   theory. This candidate does not claim it, its sorted-ROC inversion, or
   generic convex decomposition as a contribution. The new peak and shape
   restrictions are additional path constraints, and the new proof does not
   require the unrestricted reachability theorem.

2. **Lemmens and Roelands, Unique geodesics for Thompson's metric**, Annales
   de l'Institut Fourier 65(1), 315–348 (2015), DOI 10.5802/aif.2932.
   Metadata: https://numdam.org/articles/10.5802/aif.2932/ .
   Actual primary PDF inspected:
   https://aif.centre-mersenne.org/item/10.5802/aif.2932.pdf .
   Theorem 4.3 concerns unique cone geodesics under a boundary-perturbation
   condition. Theorem 5.1 characterizes ambient positive-algebra Thompson
   uniqueness by a two-point reciprocal spectrum; Theorem 5.2 concerns
   Hilbert geodesics in a positive-functional cross-section. These statements
   do not state the normalized-simplex reservoir-peak frontier or the cost of
   imposing coordinate endpoint ranges. Our uniqueness proof uses saturation
   of the binary scalar transform, and is restricted to the stated swapped
   endpoints. Difference of ambient spaces alone would not establish novelty.

3. **Qiu, Interpolation-Based Optimization for Enforcing lp-Norm Metric
   Differential Privacy in Continuous and Fine-Grained Domains**,
   arXiv:2601.09946v1 (2026), https://arxiv.org/abs/2601.09946 .
   Current abstract page verified; HTML fetch timed out. Primary cached
   `literature/privacy-interpolation.html` was inspected directly at
   Definition 3, Definitions 5–6, Proposition 3 and its Appendix B.5 proof.
   It uses log-convex scores and normalization and gives the factor-two
   normalization guarantee. This concerns a specified extension rule rather
   than the exact mandatory excursion of all admissible normalized paths.
   It does not justify identifying normalized interpolation with monotone
   output coordinates. The candidate does not allege that its guarantees
   ignore normalization or are false.

4. **Liu and Qiu, A Graph-Based Framework for Extending Metric Differential
   Privacy Mechanisms**, arXiv:2609.14125v1 (2026),
   https://arxiv.org/html/2609.14125v1 . Current primary HTML and cached
   `literature/privacy-framework.html` inspected: Section 5.2, Appendix D,
   Appendix E and Table 8. The normalized construction uses calibrated
   pre-normalization budgets (including epsilon/2). Appendix D addresses
   order independence of transform-linear scalar updates; this is distinct
   from monotonicity of each normalized output probability. Appendix E's
   envelopes are the standard Lipschitz extension ingredient underlying our
   necessary certificate. We claim no new McShane–Whitney envelope principle.
   The displayed results inspected do not supply the proposed all-budget
   minimum-peak formula or sharp shape penalty.

5. **Banerjee et al., Software for the Thompson and Funk Polygonal Geometry**,
   SoCG 2025, DOI 10.4230/LIPIcs.SoCG.2025.82. Primary full HTML inspected:
   https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/html/LIPIcs.SoCG.2025.82/LIPIcs.SoCG.2025.82.html .
   Definition 5 writes the polygonal Thompson metric as the maximum of
   forward and reverse Funk distances; Lemma 6 describes its balls and
   Lemma 8 compares them with Hilbert balls. These are relevant metric/ball
   comparisons and do not give a path-constrained reservoir frontier.
   Its metric is not automatically an intrinsic metric on a normalized
   section; the candidate makes no such identification.

6. **Soto, Bharath, Reimherr and Slavkovic, Shape And Structure Preserving
   Differential Privacy**, NeurIPS 2022. Primary abstract and introduction
   inspected:
   https://papers.neurips.cc/paper_files/paper/2022/file/9c84feb75eae1ef6389f31b3ef050b6a-Paper-Conference.pdf .
   The shape in this title concerns manifold-valued private estimation and
   geometric shape invariances, not coordinate-range constraints along a
   probability interpolation path. Only those passages were used in this
   comparison; no exhaustive full-paper exclusion is inferred.

## Search record and remaining limitations

Current queries included: differential privacy interpolation monotone;
coordinatewise monotone probability paths; mandatory excursions; privacy
interpolation overshoot; Thompson metric probability simplex; Thompson
intrinsic/length metric; normalized cone geodesics; max-relative entropy
intrinsic metric; shape-preserving and range-preserving privacy interpolation;
multiplicative interpolation probability monotone. Exact combined-phrase
queries mostly returned unrelated shape estimation, optimization interpolation,
Thompson sampling, or no direct match. Those results are not evidence of an
absence theorem. Only primary sources above support the comparisons.

No equivalent all-budget swap frontier or exact shape-restriction theorem was
found in these inspected passages. Classical constrained optimal control,
weak-metric symmetrization, and older function-algebra part-metric literature
were not exhaustively searched. No general cap-feasibility result, general
monotone optimum formula, bit-complexity improvement, or new unrestricted
Laplace/Blackwell theorem is asserted. The inaccessible alternative Numdam
PDF URL was superseded by the accessible journal PDF; Qiu's HTML timeout
was handled with its preserved primary HTML. Neither is a mathematical result.
