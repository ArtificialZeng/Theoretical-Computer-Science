# Research-pass comparison and novelty limits

Job `robust-stopping-research-a43d444f406e`; inspected 2026-10-31 Asia/Shanghai
(2026-10-30 UTC). This supplements, and does not replace, `triage-screen.md`.
The proposed contribution is a corrected certified optimizer. No recognized
open-problem status, priority guarantee or venue judgment is asserted.

- [Kim--Fan, arXiv:2603.29233v1](https://arxiv.org/html/2603.29233v1):
  current primary HTML inspected again at Section 5, Appendix D.2--D.4
  (HTML lines 1563--1616), and D.8 (1739 onward). D.2 explicitly identifies
  the expected-cost optimum with the smallest feasible raw support-cost
  level. The separation in `evidence/triage-findings.md` refutes precisely
  that inference, even granting a perfect support feasibility oracle.
  D.3--D.4 already contain the consecutive geometric recurrence and the
  gap-atom recurrence, equations (30)--(31). These recurrences, Lemma 5.1,
  the one-hot theorem C.1 and the existence of an LP formulation are prior
  ingredients. The proposed delta is backward dual elimination, a provably
  nested normalization activation sweep for arbitrary costs, and an exact
  moment-price/primal recovery algorithm with bit bounds and certificates.
  This is not a claim that geometric prefix schedules themselves are new.
- [Diakonikolas--Kontonis--Tzamos--Vakilian--Zarifis,
  ICML 2021](https://proceedings.mlr.press/v139/diakonikolas21a/diakonikolas21a.pdf):
  full primary PDF opened; definitions on pp. 1--2, Section 2.1 on pp. 3--4,
  and Corollary 2.8 / Theorem 2.9 on p. 5 inspected. Their unconstrained
  known-distribution optimum is a deterministic threshold; they learn it
  from samples and combine strategies for robustness. The inspected
  statements do not give the exact optimum under an arbitrary prescribed
  pointwise robustness cap. Generic strategy mixing is established prior
  art and is not claimed as the new step here.
- [Kang--Park--Fan, AAAI 2026, DOI 10.1609/aaai.v40i43.40991](https://ojs.aaai.org/index.php/AAAI/article/view/40991/44952):
  primary publisher PDF inspected, pp. 1--3, especially the finite-horizon
  model, Algorithm 1 and equation (3). It uses a posterior expected-rental
  decision rule and evaluates its expected-cost ratio under a prior. The
  displayed algorithm has no input R and does not perform the prescribed
  hard pointwise constrained randomized optimization considered here.
  No assertion is made about the correctness of its other claims; only
  this model/algorithm distinction was needed for the present comparison.
- [Cardas--Perotin--Simon, arXiv:2610.26214v1](https://arxiv.org/html/2610.26214):
  primary HTML Sections 1--3.1 inspected (lines 43--79). Their signal arrival
  is correlated with the adversarial horizon and their policy responds to
  that signal. Our stopping law is drawn independently before the unknown
  horizon and receives no such signal. This is a different information model.
- [Dong--Zeng--Chen, Online Algorithms for Automotive Idling Reduction with
  Effective Statistics, author PDF](https://www.mhchen.com/papers/idling.car.TCAD.15.pdf):
  primary author PDF abstract and Sections II--III model overview inspected.
  It considers a worst-case distribution constrained by short-stop mean and
  long-stop probability, and develops Lagrangian/LP methods. This is prior
  art for constrained ski rental and dual methods, rather than evidence that
  Lagrangian optimization is new here. The specified adversary and objective
  differ from a known arbitrary forecast with an externally fixed robustness
  cap. Its complete technical appendices were not re-audited in this pass.

The required Cui--Dinitz arXiv:2602.21104, Hartline--Johnsen--Shah ITCS 2026 /
arXiv:2403.10451, prediction-specific arXiv:2510.14887 and interval-robust
arXiv:2601.06813 comparisons remain documented in `triage-screen.md`.
The primary arXiv:2510.14887 HTML was reopened, including its Appendix D.1
and support-reduction statement E.1. Its one-hot/equalizing and primal-dual
constructions must be credited; the present candidate claims a general
forecast optimizer, not another one-hot frontier theorem.

Searches this pass included “ski rental randomized arbitrary distribution
expected cost hard robustness exact optimal linear program”, “ski rental
prefix dual distribution”, “ski rental distributional parametric”, “ski rental
backward linear distribution”, “ski rental Lagrangian distribution”, and
“triangular linear programming greedy algorithm constraints”. Only primary
papers were relied on for the comparisons above; search snippets merely
located them. No equivalent of the complete proposed activation-sweep and
exact moment-price algorithm was found in these inspected sources. This is
a bounded search statement, not proof of priority or a guarantee against a
known general optimization theorem. A fresh referee must judge whether the
repair adds enough mathematical value beyond standard reductions. No full
historical duplicate registry was available, as already recorded in triage.
