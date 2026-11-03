# Fresh bounded primary-source comparison

Job: c042-strongrsp-referee-5010e06f0ba2. Checked 2026-11-03 UTC.
Snapshot: b8a4224397c4874b51af65e8b82a4b17fef250e6e90513e63334f9d6b3b5e4e9.

* [Ashvinkumar, arXiv:2610.18337v2](https://arxiv.org/html/2610.18337v2),
  Theorem 1: deterministic single-source bicriteria RSP with time
  Otilde(m log(nW)/epsilon^9). The paragraph after Theorem 2 expressly
  distinguishes the outstanding strongly polynomial all-target problem from
  the available single-target consequence. Sections 4 and 6 supply the clock
  DP and witness potential used by the candidate. The candidate's substantive
  difference is eliminating all weight-aspect dependence for all targets,
  with a finite numerical implementation. The
  [current record](https://arxiv.org/abs/2610.18337) identifies v2, revised
  29 October 2026. A version-specific abstract fetch initially failed; the
  HTML and unversioned current record subsequently succeeded.

* [Ashvinkumar--Bernstein--Karczmarz, arXiv:2410.17179v1](https://arxiv.org/html/2410.17179v1),
  open-problem discussion and Lemma C.1: locating a cost-feasible bottleneck
  confines one target's optimum to a ratio-n interval and removes W for that
  target. The statement is explicitly for a single source-target pair. This
  neither gives the candidate's aggregate all-target bound nor invalidates
  the full-scope distinction. Appendix D addresses zero-length optima.

* [Gorkiewicz--Karczmarz, arXiv:2502.10348v1](https://arxiv.org/html/2502.10348v1),
  Theorem 1.3 and Section 6, Algorithm 4 and Lemmas 6.1--6.3: near-linear
  offline approximate ordinary SSSP using recursive activation, endpoint
  estimates and multiplicative accounting. These are real precedents, not new
  contributions here. The candidate must, and does, prove an appropriate
  nonadditive stopped-control oracle and finite-precision/clipping contract.

* An additional primary comparison surfaced in this referee's search:
  [McCauley--Moseley--Niaparast--Niaparast--Singh, Incremental Approximate
  Single-Source Shortest Paths with Predictions, ICALP 2025, Theorem 1](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.117/LIPIcs.ICALP.2025.117.html).
  Its offline ordinary-SSSP bound is
  O(m log(nW) log^3(n) loglog(n)/epsilon). It reinforces the need to credit
  the offline divide-and-conquer architecture rather than claim that idea.
  It does not state an all-target constrained-path or stochastic-boundary
  theorem. A future manuscript should include this parallel precedent.

Searches included the combinations "restricted shortest paths" / "strongly
polynomial" / "all targets" / "all-target", the source arXiv identifier,
"restricted shortest paths" / "offline" / "Poisson", and "stochastic" /
"offline incremental" / "shortest". Aggregators, automatically generated
open-problem pages, unrelated stochastic-navigation results and search snippets
were not used as mathematical evidence. No equivalent full solution was found
in the inspected primary sources. This bounded search does not prove priority.
