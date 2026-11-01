# Primary-source checks in the fresh referee pass

Job: robust-stopping-referee-e4128dd151f7. Checked 2026-10-31 UTC
(2026-11-01 Asia/Shanghai). These are bounded comparisons, not priority
certificates. The mathematical decision concerns the frozen snapshot only.

- [Kim--Fan, arXiv v1](https://arxiv.org/html/2603.29233v1):
  inspected the frozen original HTML and live primary text at Section 5,
  C.4 Theorem C.1(ii), and D.2--D.7. The robustness reduction and geometric
  schedules are prior results. C.1 at y=b indeed supplies the same capped
  geometric law on the range stated in the frozen overlap analysis. D.2
  explicitly equates support-level feasibility with the expected optimum.
  The exact separating instance refutes that inference. Algorithm 3's tail
  scan and moment updates support the frozen warning about literal-code
  ambiguity. The current [PMLR record](https://proceedings.mlr.press/v306/kim26l.html)
  confirms ICML 2026 publication and links software; the frozen claim does
  not assert any particular output of that software or equality between
  versions. This referee did not inspect the additional unfrozen code files.
- [Li--Christianson--Li, arXiv v1](https://arxiv.org/html/2510.14887v1):
  inspected Section 5.2, E.1 Lemma 1 and adjacent equalizing-distribution
  formulas. Finite support [b] union {y+1}, geometric equalization,
  prediction-specific Pareto optimization, and LP methods are substantial
  prior ingredients. The inspected results concern a point prediction y;
  they do not state this arbitrary-forecast activation oracle or the full
  uniform expected-cost frontier. Their asymptotic qualifications must be
  retained when cited.
- [Diakonikolas--Kontonis--Tzamos--Vakilian--Zarifis](https://proceedings.mlr.press/v139/diakonikolas21a/diakonikolas21a.pdf):
  inspected the model and Corollary 2.8/Theorem 2.9 on printed page 6.
  The strategy combination has a per-instance bound, and the learning
  guarantee covers log-concave distributions. Thus claiming this prior
  work lacks pointwise robustness would be inaccurate. The inspected
  theorems do not identify the exact forecast optimum at each prescribed
  hard competitive cap.
- [Cui--Dinitz](https://arxiv.org/html/2602.21104v1): inspected Section 2
  and Theorem 1. Their benchmark is the policy optimal for the unknown
  true distribution, with additive loss controlled by Wasserstein error.
  That differs from minimizing a known-forecast expectation subject to an
  externally prescribed pointwise cap.
- [Hartline--Johnsen--Shah, ITCS 2026](https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/html/LIPIcs.ITCS.2026.75/LIPIcs.ITCS.2026.75.html):
  inspected the finite good/bad weather-sequence model and robust-design
  framework. The prior-independent and subgame benchmarks differ from
  this fixed advice objective. Their generic game/LP tools remain prior art.

Fresh searches combined ski rental with uniform, robustness, frontier,
distributional advice, optimal randomized linear program, and activation/
dual/prefix. No exact duplicate of the combined theorem was located.
The historical moment-constrained/DRO literature was not comprehensively
re-audited; the frozen literature screen states those limits. Neither
these searches nor the gate prove priority or venue significance.

Two anchor-click requests on the Li primary HTML failed in the web tool;
opening its primary URL and finding/reading the relevant numbered passages
succeeded. This navigation failure is not used as mathematical evidence.
