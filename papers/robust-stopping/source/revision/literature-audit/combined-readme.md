# Consolidated verified-metadata bibliography candidate

This metadata handoff contains **12 entries**: five classical references, the published Kim–Fan paper, and six distributional references. It does not establish mathematical correctness, novelty, or venue fit. No manuscript, frozen input, raw official export, or `legacy-*` output was edited.

## Files and intended use

- `combined-build-candidate.bib`: minimal compilation candidate using official citation keys, entry types, and all bibliographic field values from the audited exports, with **five abstract fields deliberately omitted**. Source comments and entry separators were added. These candidate blocks are therefore **not completely unmodified official exports**. Untouched raw exports remain internal research inputs.
- `combined-render-adapter.bib`: an alternative for the manuscript's `alpha` style, retaining the same 12 official keys and applying the two transparent adapters below. Use one candidate when merging; do not load both together.
- `combined-provenance.json`: source URLs, raw-input SHA-256 hashes, entry metadata, and abstract-removal counts.
- `combined-key-map.json`: old-to-official mapping, new keys, and legacy references awaiting their separate audit.
- `combined-render-adapter.json`: exact adapter changes and isolated validation results.

Abstracts were removed from the compilation candidates to avoid redistributing protected source prose. The untouched official exports remain the audit record and should not be described as the modified compilation candidates.

## Exact rendering adapters

1. **`Dinitz_2024`**: entry type changed from `inbook` to `inproceedings`. No bibliographic field or value changed. The Crossref export contains the correct SODA proceedings title in `booktitle`; `alpha` ignores that field for `inbook` but renders it for `inproceedings`.
2. **`kang2025learningaugmentedskirentaldiscrete`**: added only `howpublished = {arXiv:2512.07313, \url{https://arxiv.org/abs/2512.07313}}`. Both the identifier and URL come directly from the official export's existing `eprint` and `url` fields, which remain present. `alpha` ignores those original fields for `misc`, whereas it renders `howpublished`. No venue or DOI was inferred.

All other candidate fields and values remain unchanged. `combined-build-candidate.bib` was hash-checked unchanged after creating the rendering adapter.

## Key mapping and integration boundary

The sole replacement for an existing manuscript key is **`KF26` → `pmlr-v306-kim26l`**, replacing the preprint citation with the verified ICML 2026 publication. The other 11 official keys are new additions. Preserve exact keys, including Springer's `10.1007/978-3-032-06706-7_6`.

The existing keys **`LCL25`, `CD26`, and `HJS26` are not included** in these 12-entry candidates. Their separate legacy audit is handled by the distribution helper. Merge its audited entries before replacing the manuscript bibliography; these files are not a complete replacement for every existing citation.

## Entry inventory and official sources

| Official citation key | Title | Export year | Primary metadata/export source |
|---|---|---|---|
| `Karlin1988` | Competitive snoopy caching | 1988 | [official export](https://citation-needed.springer.com/v2/references/10.1007/BF01762111?format=bibtex&flavour=citation) |
| `Karlin1994` | Competitive randomized algorithms for nonuniform problems | 1994 | [official export](https://citation-needed.springer.com/v2/references/10.1007/BF01189993?format=bibtex&flavour=citation) |
| `NEURIPS2018_73a427ba` | Improving Online Algorithms via ML Predictions | 2018 | [official export](https://proceedings.neurips.cc/paper_files/paper/2018/file/73a427badebe0e32caa2e1fc7530b7f3-Bibtex.bib) |
| `NEURIPS2020_5bd844f1` | Optimal Robustness-Consistency Trade-offs for Learning-Augmented Online Algorithms | 2020 | [official export](https://papers.neurips.cc/paper_files/paper/10398-/bibtex) |
| `Tardos_1986` | A Strongly Polynomial Algorithm to Solve Combinatorial Linear Programs | 1986 | [official export](https://api.crossref.org/works/10.1287/opre.34.2.250/transform/application/x-bibtex) |
| `pmlr-v306-kim26l` | Robust and Consistent Ski Rental with Distributional Advice | 2026 | [official export](https://proceedings.mlr.press/v306/kim26l.html#bibtex) |
| `Besbes_2025` | Beyond IID: Data-Driven Decision Making in Heterogeneous Environments | 2025 | [official export](https://api.crossref.org/works/10.1287/mnsc.2022.03448/transform/application/x-bibtex) |
| `pmlr-v139-diakonikolas21a` | Learning Online Algorithms with Distributional Advice | 2021 | [official export](https://proceedings.mlr.press/v139/diakonikolas21a.html#bibtex) |
| `Khanafer_2013` | The constrained Ski-Rental problem and its application to online cloud cost optimization | 2013 | [official export](https://api.crossref.org/works/10.1109/INFCOM.2013.6566944/transform/application/x-bibtex) |
| `Dinitz_2024` | Controlling Tail Risk in Online Ski-Rental | 2024 | [official export](https://api.crossref.org/works/10.1137/1.9781611977912.147/transform/application/x-bibtex) |
| `10.1007/978-3-032-06706-7_6` | Controlling Tail Risk in Two-Slope Ski Rental | 2026 | [official export](https://citation-needed.springer.com/v2/references/10.1007/978-3-032-06706-7_6?flavour=citation&format=bibtex) |
| `kang2025learningaugmentedskirentaldiscrete` | Learning-Augmented Ski Rental with Discrete Distributions: A Bayesian Approach | 2025 | [official export](https://arxiv.org/bibtex/2512.07313) |

## Validation and remaining limits

Both candidates passed isolated `bibtex -terse` checks with the manuscript directory's `alpha.bst`: **12 bibliography items, all expected keys, zero warnings or errors**. The adapted output explicitly renders the SODA venue and Kang's verified arXiv identifier/URL. Logs are `combined-validation.blg` and `combined-render-validation.blg`; generated metadata-only bibliographies are the corresponding `.bbl` files. No manuscript LaTeX build was run in this helper's scope.

- Purohit 2018 retains the official export's empty `pages` field. The separate classical audit records primary TOC evidence for pages 9661–9670; no silent addition was made here.
- The two-slope chapter retains Springer's publication year **2026**, despite event WAOA 2025 and first-online 2025. This is a verified distinction, not a typographical repair.
- Original fulltext access limits for Tardos and Khanafer remain as recorded in the source audits. Verified metadata does not certify every theorem or related-work claim.
- BibTeX styles can omit other supplied fields such as URLs and DOIs. The writer remains responsible for the final manuscript citation set, presentation requirements, and full build after merging separately audited legacy entries.
