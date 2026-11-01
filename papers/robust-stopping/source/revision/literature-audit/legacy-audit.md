# Legacy bibliography/model audit

Completed bounded primary-source audit; no manuscript, bibliography, source or frozen evidence changes. Raw publisher BibTeX files are separate and unmodified.

## CD26 — verified publication and model attribution

The existing title, authors and preprint year are accurate. A current primary publication record is now available: **Qiming Cui and Michael Dinitz, Ski Rental with Distributional Predictions of Unknown Quality, ICML 2026, PMLR 306:21805–21828**. Use the [official PMLR record](https://proceedings.mlr.press/v306/cui26a.html) and raw export `legacy-cd26-pmlr-official.bib`; recommended exact-key mapping is `CD26` → `pmlr-v306-cui26a`. Existing citation context is `manuscript/main.tex:117–118`.

The [published fulltext](https://raw.githubusercontent.com/mlresearch/v306/main/assets/cui26a/cui26a.pdf), §§2.1–2.2, defines additive loss against the optimal policy knowing the true horizon distribution, with unknown Wasserstein-1 prediction error. Theorem 1 supplies the additive bound. Theorem 2 additionally interpolates with a multiplicative robustness guarantee; on point-mass truth this implies pointwise competitiveness. Thus an assertion that this paper lacks pointwise robustness would be false.

Supported prose: “Cui and Dinitz bound additive loss against the policy knowing the true horizon distribution when Wasserstein prediction error is unknown, and give an additional robustness interpolation. We instead exactly minimize supplied-forecast expected cost at each prescribed pointwise expected-competitive cap.”

This is arXiv:2602.21104 / ICML2026, distinct from Cui–Dinitz's two-slope tail-risk paper. No mathematical or novelty acceptance is made.

## LCL25 — publication metadata verified; journal fulltext limit retained

The [author's publication page](https://tongxin.me/research/papers/prediction-specific/) confirms the same title and authors as a POMACS 2026 publication. Publisher-deposited [Crossref metadata](https://api.crossref.org/works/10.1145/3788100) verifies **Sizhe Li, Nicolas Christianson, Tongxin Li, Prediction-Specific Design of Learning-Augmented Algorithms, Proceedings of the ACM on Measurement and Analysis of Computing Systems 10(1), 2026, pages 1–57, DOI 10.1145/3788100**. Raw official export: `legacy-lcl26-official.bib`, key `Li_2026`. Its fields remain unmodified; the export does not supply an article number.

The [primary arXiv v1 fulltext](https://arxiv.org/pdf/2510.14887v1), inspected at §5 (PDF p13), defines point-prediction consistency by the competitive ratio at prediction y, and gives two LPs. Theorems 5.2 and 5.3 explicitly state randomized strong optimality as b tends to infinity. Appendix D, Theorem D.1 (PDF p30), describes equalizing distributions. Appendix E.1, Lemma 1 (PDF p33), states support reduction to `[b]∪{y+1}`. Appendix E.5 uses primal-dual reasoning. Existing contexts: `main.tex:113–116` and `main.tex:178`.

Suggested prose: “Li, Christianson and Li develop prediction-specific Pareto optimization for point predictions, using finite support reductions, equalizing distributions and primal-dual arguments.” Preserve the asymptotic qualification with an explicit inspected-version note in the dossier.

Access/version limit: journal landing, PDF and epdf URLs returned 403. The current author pages identify the journal publication but link only its DOI. We inspected the 54-page arXiv v1, not the 57-page journal article. We do not assert journal/preprint fulltext identity, unchanged theorem numbering, or absence of an arbitrary-distribution or uniform-capped-frontier result in the inaccessible journal version. Publication-aware recommended mapping is `LCL25` → `Li_2026`; keep the arXiv v1 source mapping and access note. An exact `Appendix E.1` citation must remain explicitly bound to arXiv v1 unless journal numbering is independently checked. Raw arXiv export remains `legacy-lcl25-official.bib`, official key `li2025predictionspecificdesignlearningaugmentedalgorithms`.

## HJS26 — metadata consistent; qualify the benchmark statement

The [official Dagstuhl record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.75) and [publisher export](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.75/metadata/bibtex/download) verify **Jason Hartline, Aleck Johnsen, Anant Shah, Prior-Independent and Subgame Optimal Online Algorithms, ITCS 2026, LIPIcs 362:75:1–75:23, DOI 10.4230/LIPIcs.ITCS.2026.75**. Existing author/title/year/venue/volume/pages/DOI fields are correct. Raw export `legacy-hjs26-official.bib` additionally contains publisher identifiers/URL/URN/keywords; recommended exact key is `hartline_et_al:LIPIcs.ITCS.2026.75`.

[Primary published fulltext](https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/LIPIcs.ITCS.2026.75/LIPIcs.ITCS.2026.75.pdf), §2 Definitions 1–2 (printed 75:6), defines the distribution-knowing Bayesian policy and a worst-case ratio over an allowed distribution class. Section 2.1 (75:7) gives known finite horizon T, observed binary weather, and an unknown Bernoulli good-day probability for the prior-independent problem. Section 4.1 Definitions 19–20 (75:15) separately defines subgame optimality. Existing context: `main.tex:119–121`.

Suggested prose: “For ski rental over a known finite horizon of observed binary weather, Hartline, Johnsen and Shah compute approximate prior-independent policies against the distribution-knowing online benchmark and analyze subgame-optimal worst-case policies.” Qualify the Bayesian benchmark as the prior-independent part, rather than implying every part of their paper uses that benchmark.

## Handoff and exact key map

| Existing key | Recommended official publication key | Export |
|---|---|---|
| `LCL25` | `Li_2026` | `legacy-lcl26-official.bib` |
| `CD26` | `pmlr-v306-cui26a` | `legacy-cd26-pmlr-official.bib` |
| `HJS26` | `hartline_et_al:LIPIcs.ITCS.2026.75` | `legacy-hjs26-official.bib` |

For the LCL pinpoint preprint locator, retain/document the separate official arXiv key given above. The three cited works exist with the stated author lists. Two now have newer publication records; HJS26 needs no substantive factual correction. Source mappings and limits are in `legacy-audit.json`; download hashes/URLs/failures are in `legacy-download-provenance.json`. No source changes, frozen-evidence changes or build commands were performed. This audit makes no mathematical or novelty acceptance.
