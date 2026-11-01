# Delegated classical-reference audit

Checked 2026-10-31. Five sources verified individually against original publisher/proceedings records. This helper made no manuscript, bibliography, frozen-input, or PDF changes. No further agents or model processes were launched. The scope was read-only research plus these audit artifacts.

`classical-verified.bib` concatenates five unmodified official exports. Prefer its keys below; there were no existing keys for these sources in the assigned task. Individual raw files, URLs, hashes, locators, and access limitations are recorded in `classical-audit.json`. The parent owns insertion, citation-key synchronization, and compilation.

| Official key | Verified publication | DOI | Preferred raw export |
|---|---|---|---|
| `Karlin1988` | Anna R. Karlin, Mark S. Manasse, Larry Rudolph, Daniel D. Sleator. *Competitive snoopy caching*. Algorithmica 3(1), 79–119, November 1988. | `10.1007/BF01762111` | `snoopy1988-springer.bib` |
| `Karlin1994` | A. R. Karlin, M. S. Manasse, L. A. McGeoch, S. Owicki. *Competitive randomized algorithms for nonuniform problems*. Algorithmica 11(6), 542–571, June 1994. | `10.1007/BF01189993` | `nonuniform1994-springer.bib` |
| `NEURIPS2018_73a427ba` | Manish Purohit, Zoya Svitkina, Ravi Kumar. *Improving Online Algorithms via ML Predictions*. Advances in Neural Information Processing Systems 31, 2018. Curran pagination 9661–9670; official BibTeX leaves pages blank. | Not supplied by official export | `purohit2018-official.bib` |
| `NEURIPS2020_5bd844f1` | Alexander Wei, Fred Zhang. *Optimal Robustness-Consistency Trade-offs for Learning-Augmented Online Algorithms*. Advances in Neural Information Processing Systems 33, 8042–8053, 2020. | Not supplied by official export | `weizhang2020-official.bib` |
| `Tardos_1986` | Éva Tardos. *A Strongly Polynomial Algorithm to Solve Combinatorial Linear Programs*. Operations Research 34(2), 250–256, April 1986. | `10.1287/opre.34.2.250` | `tardos1986-crossref.bib` |

## 1. Karlin–Manasse–Rudolph–Sleator 1988

[Springer original record](https://link.springer.com/article/10.1007/BF01762111) and [Springer BibTeX export](https://citation-needed.springer.com/v2/references/10.1007/BF01762111?format=bibtex&flavour=citation) verify the metadata. Prefer Springer issue 1 over Crossref's issue 1–4. A secondary search snippet's starting page 77 conflicts with the publisher's 79 and was rejected.

The [original journal scan hosted at MIT](https://courses.csail.mit.edu/6.895/fall03/handouts/papers/snoopy-cache.pdf) was visually inspected and OCR-read through its first nine PDF pages. Section 1 explains competitive analysis; Theorem 3.1 supplies the factor-two lower bound for the specified caching model; Theorem 4.1 gives the matching direct-mapped algorithm. Exact short evidence: “Algorithm dsc is strongly 2-competitive” (Theorem 4.1; source PDF page 7).

Safe related-work statement: classical competitive analysis of rent-or-buy decisions has roots in snoopy caching. Do not claim this source proves the manuscript's exact fixed-b discrete formula. OCR is only a finding aid; source images remain authoritative.

## 2. Karlin–Manasse–McGeoch–Owicki 1994

[Springer original record](https://link.springer.com/article/10.1007/BF01189993) and [native export](https://citation-needed.springer.com/v2/references/10.1007/BF01189993?format=bibtex&flavour=citation) verify journal metadata. The journal abstract supports optimal randomized ratios approaching e/(e−1) against an oblivious adversary. It compares these with deterministic factor 2. Journal full text was not obtained.

The [MIT original PDF](https://courses.csail.mit.edu/6.895/fall03/handouts/papers/karlin.pdf) is instead the **SODA 1990 proceedings version**, Chapter 33, printed pages 301–309. Its first page spells the fourth author Susan Owicki; an additional middle initial was not verified. Section 2.2, Theorems 1–2, use the snoopy-caching ratio e_p/(e_p−1), with e_p=(1+1/p)^p. Section 3.1, Theorem 7, treats continuous spin-block and gives e/(e−1).

Safe statement: randomization improves the classical factor-two benchmark to the optimal limiting ratio e/(e−1). These checked formulas do **not** directly establish the manuscript's fixed-b discrete rho_b.

## 3. Purohit–Svitkina–Kumar 2018

The [official NeurIPS record](https://proceedings.neurips.cc/paper/2018/hash/73a427badebe0e32caa2e1fc7530b7f3-Abstract.html), [original PDF](https://proceedings.neurips.cc/paper_files/paper/2018/file/73a427badebe0e32caa2e1fc7530b7f3-Paper.pdf), and [official export](https://proceedings.neurips.cc/paper_files/paper/2018/file/73a427badebe0e32caa2e1fc7530b7f3-Bibtex.bib) were checked. The [Curran primary TOC](https://www.proceedings.com/content/048/048413webtoc.pdf), printed page li / PDF page 51, starts this article at 9661 and the next at 9671; combined with the ten-page original PDF, this supports 9661–9670. The unmodified official export retains `pages = {}`.

Sections 2.2–2.3, Theorems 2.2–2.3, establish parameterized robustness-consistency guarantees using a prediction of season length. The deterministic guarantee is (1+1/λ)-robust and (1+λ)-consistent. Their randomized algorithm uses geometric purchase-time probabilities.

Safe statement: learning-augmented ski rental uses point predictions to improve good-prediction performance while preserving worst-case guarantees. The paper3 objective instead averages cost under a supplied finite forecast distribution. No DOI was found in the checked official export; none should be invented.

## 4. Wei–Zhang 2020

The [official proceedings record](https://papers.neurips.cc/paper_files/paper/2020/hash/5bd844f11fa520d54fa5edec06ea2507-Abstract.html), [original PDF](https://papers.neurips.cc/paper_files/paper/2020/file/5bd844f11fa520d54fa5edec06ea2507-Paper.pdf), [supplement](https://papers.neurips.cc/paper_files/paper/2020/file/5bd844f11fa520d54fa5edec06ea2507-Supplemental.pdf), and [official BibTeX](https://papers.neurips.cc/paper_files/paper/10398-/bibtex) were checked.

Theorem 1.2 states the lower bound β ≥ γ log(1+1/(γ−1)). Section 2.2, equations (2.1)–(2.4), formulates purchase-time probabilities with linear robustness and consistency constraints. Appendix A, Lemmas A.1–A.3, reduces this infinite LP in the long-prediction regime y ≥ 2B−1. The proof ends by taking B→∞ to obtain the logarithmic curve.

Safe statement: robustness-consistency tradeoffs and LP formulations already have substantive prior art. Describe the new oracle's specific objective and structure; do not claim the first infinite-to-finite robustness LP reduction, nor attribute the exact fixed-b frontier to this asymptotic bound. The official export supplies no DOI.

## 5. Tardos 1986 and the complexity comparison

The [original INFORMS publisher record](https://pubsonline.informs.org/doi/10.1287/opre.34.2.250) and [official Crossref BibTeX](https://api.crossref.org/works/10.1287/opre.34.2.250/transform/application/x-bibtex) verify metadata. Publisher-native citation download returned 403; the official Crossref export is preserved unchanged. PDF access returned 403 or redirected to the abstract; no original theorem number or full-proof verification is claimed.

The publisher abstract states that the arithmetic-step bound depends on number sizes in the constraint matrix and is independent of those in objective and right-hand-side vectors. Short exact evidence: “independent of the size of the numbers in the right-hand side and objective vectors”. This does not assert bit running time independent of reading or manipulating these encodings.

Application to paper3 is an inference from that statement and the displayed LP: the moment row contains t−1, and a sparse forecast can have t vastly larger than b. Thus its displayed constraint matrix is **not generally bounded by b**. An O(b)-column reduction alone does not establish horizon-encoding-independent arithmetic complexity via Tardos. A special reformulation might change this comparison, but requires a separate argument.

## Suggested minimal introduction content

Use the first two references for the classical competitive-analysis lineage and the e/(e−1) limiting benchmark. Use Purohit et al. and Wei–Zhang for point-prediction robustness-consistency tradeoffs and the existing LP perspective. Explain that this manuscript minimizes expected cost under a finite forecast distribution subject to uniform robustness. Cite Tardos only with the precise matrix-size versus objective/right-hand-side distinction. Keep the manuscript's discrete rho_b calculation self-contained.

No novelty, venue-fit, or submission claim is established by this bounded audit.
