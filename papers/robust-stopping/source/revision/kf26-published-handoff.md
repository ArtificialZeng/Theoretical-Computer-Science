# Critical primary-source and actual-code handoff

This is new factual evidence for the user revision, not a mathematical acceptance.
The existing old report only inspected arXivv1. Root now found the current official
publication: Kim--Fan, ICML2026/PMLR306:57411--57444,
https://proceedings.mlr.press/v306/kim26l.html . Its official Software link is
https://github.com/JihwanKim4689/distributional-ski-rental . Metadata should use
raw official export pmlr-v306-kim26l if citing the published version. Native
bibliography helper independently fetched the complete official PDF (560062bytes,
SHA2565c5842ff3d0d2df8b802bc9968d520410ade6a059f83b3ca9fb1ac6a8f53ec4c)
and verified the critical D.2 statement on printedp30. See
revision/literature-audit/classical-kf26-published-source.txt and its provenance.
Do NOT use literature/kf26-published.pdf: that ROOT fetch is a 40167byte partial
file from a timeout, not a source. The helper's complete PDF is under its assigned
classical-kf26-* scope.

Permitted exact quotation from D.2 (17words; keep TOTAL KF prose quotes <=25words):
“Therefore the optimal objective value equals the minimum feasible h, which can
be found by binary search.” The claimed equivalence is expectation minimization
versus minimization of maximum raw cost on positive support; quote/pin the exact
version and distinguish these two objectives.

## Actual software, not a hypothetical trace

The repository was shallow-cloned, then root read both files before execution.
Only the unchanged SkiRentalOptimizer AST class node was loaded, with standard
math/bisect modules; no top-level experiments/plots, installs or external writes.
Root executed BOTH published source files for b=3,C=3/2, days=[1,2], probs=[.4,.6],
with tolerances1e-5,1e-9,1e-12. Every run returned PMF

    f1=1/4, f2=3/8, f3=3/8,

water level approximately3, true model cost12/5, true moment9/8. Both functions
reject h=14/5 and accept h=3. Full real records, filenames and SHA256 are in
revision/kf26-author-code-run.json. Bibliography helper independently statically
traced the same class and obtained the same result. This output is NOT11/5.

Keep three distinct rows/claims:
- Exact global optimum: f1=1/4,f3=3/4; J=39/20; moment3/2; raw support maximum3.
- Best policy at minimum raw-support level14/5: f2=f3=1/2; J=11/5; moment3/2.
- Current author software at the pinned commit: f1=1/4,f2=f3=3/8; J=12/5;
  moment9/8; water level~3. This is a finite reproduction observation, not a
  universal theorem about all implementations or versions.

At h in[14/5,3), code's first segment adds no mass; day2 adds1/2 and internal
mu=1; day3 adds1/4, totalmass3/4; its tail test scans prediction support points
strictly greaterthanb, of which there are none, and rejects. At h>=3, its
first geometric step gives F=1/4,mu=0; day2 adds3/8; day3 adds3/8 and reaches1.
Source indexing/updates differ from the ideal feasibility oracle; do not silently
repair the authors' code and label it original execution. The conceptual
support-threshold inference fails independently of these implementation details.

## Literature handoff

Complete native-helper audits/official exports are under revision/literature-audit/:
classical-sources/classical-audit.md and classical-verified.bib, plus
distribution-audit.md and distribution-*-official.bib. Inspect scope nuances:
Wei--Zhang already uses finite LPs; DKT DOES provide per-instance robustness;
Besbes2025 is known-radius distribution-shift regret; Khanafer's known moments
are of the horizon rather than of the policy; tail papers bound exceedance
probabilities. Bayesian2512.07313 covers the uniform unconstrained plateau
(buyday b+1 when support1..b), so that endpoint is background. None of the
inspected statements gives the entire candidate capped uniform frontier;
this is a bounded comparison, not proof of priority.

Pinned code commit and commit metadata:

0a86125f31e9e1b1abbba5bd4fde32a332860124
2026-05-24T22:14:26+09:00
Add files via upload
