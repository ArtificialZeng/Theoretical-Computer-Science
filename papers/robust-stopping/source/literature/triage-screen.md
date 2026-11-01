# Primary-source triage screen

Inspected on 2026-10-31 Asia/Shanghai (2026-10-30 UTC), job
robust-stopping-triage-ef6eadc61ec7. Source status: `status-uncertain`.
This is an autonomously posed research question, not verified open status.
No general characterization beyond the inspected claims is certified new.

- [Kim--Fan, arXiv:2603.29233v1](https://arxiv.org/html/2603.29233v1):
  cached original `rental-advice.html`; read Sections 2 and 5 and the
  complete relevant Appendices C.1--C.4 and D.1--D.8. Lemma 5.1 is exactly
  the robustness reduction. C.4 Theorem C.1 explicitly solves every one-hot
  forecast. D.2 substitutes minimum feasible support threshold for expected
  cost; D.5--D.7 also contain day/moment indexing differences. Our exact
  separation addresses the support-threshold inference, independent of
  those implementation details. Sections 3--4's deterministic stability
  results are outside this optimization target. Current web fulltext was
  also opened and displayed v1.
- [Cui--Dinitz, arXiv:2602.21104v1](https://arxiv.org/html/2602.21104v1):
  cached `rental-unknown.html`, Section 2.1 benchmark and Theorems 1--2
  inspected. The benchmark is best online policy knowing the distribution,
  and the central result bounds additive loss with unknown Wasserstein
  prediction error. Distinguish it from the source's fixed hard robustness
  and arbitrary forecast expected-cost optimization. Parsed plain text
  loses radical formatting; use original HTML math for formulas.
- [Hartline--Johnsen--Shah, ITCS 2026](https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/html/LIPIcs.ITCS.2026.75/LIPIcs.ITCS.2026.75.html):
  inspected publisher HTML Sections 2--3, especially Definitions 1--2,
  weather-sequence model, and Theorem 10. Its robust/prior-independent
  benchmark is Bayesian policy cost; the ski-rental instance includes a
  known finite sequence of good/bad weather. Also inspected
  [arXiv:2403.10451v1](https://arxiv.org/html/2403.10451v1), Section 4,
  Theorems 4.2,4.6,4.9,4.14. Generic equilibrium-computation tools are prior
  art, not a new exact solver for this specific constrained objective.
- [Prediction-Specific Design of Learning-Augmented Algorithms,
  arXiv:2510.14887](https://arxiv.org/html/2510.14887): Section 5.2 and
  Appendix D Operations A/B and Appendix E.1 Lemma 1 inspected. It has
  prediction-specific one-hot Pareto constructions, a primal/dual method,
  and support [b] union {y+1}. This is substantial prior art for any
  one-hot claim or alleged new support-reduction principle. The exact
  asymptotic qualifiers of its strong-optimality theorems must be retained.
- [Analyzing the effect of prediction accuracy on the
  distributionally-robust competitive ratio,
  arXiv:2601.06813](https://arxiv.org/html/2601.06813): Sections 3--4,
  particularly Section 4.1 equations (19)--(22), inspected. It optimizes
  weighted worst-case competitive ratios over nested prediction intervals,
  using an LP. This is different from expectation under a fixed arbitrary
  forecast, and an LP restatement would not be a substantive delta here.

Searches included exact identifier/title, “ski rental distribution expected
cost robustness optimal randomized”, “ski rental distributional advice
optimal linear programming”, “ski rental hard robustness distribution
optimal”, and “ski rental distributionally-robust competitive ratio”.
Search snippets were used only to locate sources; assertions above were
checked against primary fulltext passages. A PMLR 2021 distributional-advice
paper was found, but only its landing abstract was inspected, so its full
theorems remain a literature follow-up rather than an exclusion certificate.

Network tools: web access to primary fulltexts succeeded. Direct Python
URL downloads of three additional sources failed with DNS errors; those
sources were still read through web and are documented above. This is an
access/logging limitation, not a mathematical obstacle or priority evidence.
No nonexistent downloaded files are cited as evidence. The two existing
cached HTML files were not modified; `.txt` files are derived reading aids.

Duplicate screen: `selection.md` is the available local historical list.
One-hot forecast and water-level checking were explicitly merged into
robust-stopping; another coverage corollary was excluded as a separate
paper. No full historical registry is present in this project, so wider
duplicate clearance is incomplete. No `candidate-argument.md` was present.

Admission: advance to a bounded repaired-optimizer investigation with the
exact test in `evidence/triage-findings.md`. No novelty, acceptance, or
manuscript eligibility is established by this triage decision.
