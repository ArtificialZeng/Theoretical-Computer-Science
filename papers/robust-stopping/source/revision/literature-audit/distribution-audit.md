# Distributional advice, moments and tail-risk audit

Bounded read-only bibliography/model audit for the paper3 revision. No manuscript,
TeX, bibliography, frozen evidence or acceptance status was changed. New files are
confined to `revision/literature-audit/distribution-*`. Raw exports and fulltext
downloads are research inputs; do not include third-party fulltexts in a source ZIP.
The requested five references have primary metadata/exports; four have inspected
fulltexts. Khanafer et al. has a primary institutional abstract but inaccessible
conference fulltext. No user-authoritative bibliography workbook was supplied.

## Verified metadata and unmodified official exports

| Reference | Verified publication record | Official raw BibTeX file / key |
|---|---|---|
| Besbes, Ma, Mouchtaki | *Beyond IID: Data-Driven Decision Making in Heterogeneous Environments*, Management Science **71**(12):10538–10555 (2025), DOI `10.1287/mnsc.2022.03448` | `distribution-beyond-iid-official.bib` / `Besbes_2025` |
| Diakonikolas, Kontonis, Tzamos, Vakilian, Zarifis | *Learning Online Algorithms with Distributional Advice*, ICML 2021, PMLR **139**:2687–2696 | `distribution-learning-advice-official.bib` / `pmlr-v139-diakonikolas21a` |
| Khanafer, Kodialam, Puttaswamy | *The constrained Ski-Rental problem and its application to online cloud cost optimization*, INFOCOM 2013:1492–1500, DOI `10.1109/INFCOM.2013.6566944` | `distribution-constrained-official.bib` / `Khanafer_2013` |
| Dinitz, Im, Lavastida, Moseley, Vassilvitskii | *Controlling Tail Risk in Online Ski-Rental*, SODA 2024:4247–4263, DOI `10.1137/1.9781611977912.147` | `distribution-tail-official.bib` / `Dinitz_2024` |
| Cui, Dinitz | *Controlling Tail Risk in Two-Slope Ski Rental*, WAOA 2025, LNCS **16077**:81–96, DOI `10.1007/978-3-032-06706-7_6` | `distribution-two-slope-official.bib` / `10.1007/978-3-032-06706-7_6` |

The first, third and fourth blocks are raw Crossref content exports. The PMLR block
is the official page's BibTeX text, with HTML entities decoded only. The fifth is
the publisher's own export. Do not normalize their keys, field order, Unicode,
abstracts or spacing. Existing `manuscript/references.bib` has none of these five
entries, so no existing key replacement is proposed. The publication-year issue
for the fifth entry is real: Springer says First Online 1 October 2025, event
WAOA 2025, print/copyright 2026, and exports `year="2026"`. Preserve that official
export and distinguish event year from publication year.

Metadata URLs:

- [INFORMS article](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.03448);
  [Crossref BibTeX](https://api.crossref.org/works/10.1287/mnsc.2022.03448/transform/application/x-bibtex).
- [PMLR article and BibTeX](https://proceedings.mlr.press/v139/diakonikolas21a.html).
- [IEEE record](https://ieeexplore.ieee.org/document/6566944);
  [Crossref BibTeX](https://api.crossref.org/works/10.1109/INFCOM.2013.6566944/transform/application/x-bibtex).
- [SIAM article](https://epubs.siam.org/doi/abs/10.1137/1.9781611977912.147);
  [Crossref BibTeX](https://api.crossref.org/works/10.1137/1.9781611977912.147/transform/application/x-bibtex).
- [Springer chapter](https://link.springer.com/chapter/10.1007/978-3-032-06706-7_6);
  [publisher BibTeX](https://citation-needed.springer.com/v2/references/10.1007/978-3-032-06706-7_6?flavour=citation&format=bibtex).

## Primary-passage mapping and comparisons

### Besbes–Ma–Mouchtaki

[Author PDF](https://willma353.github.io/papers/beyond_iid.pdf), identical arXiv
identifier [2206.09642v5](https://arxiv.org/abs/2206.09642v5), inspected at §2,
§5.2 and Appendix E. Appendix E, Eq. (E-18), printed App-25 (PDF p62), uses
continuous rental duration and horizon in `[0,M]`. The environment distribution is
unknown; historical distributions lie within a known heterogeneity radius.
Appendix E.2, Proposition E-8, printed App-27 (PDF p64), contrasts nonvanishing
SAA regret with an inflated-SAA policy achieving the optimal square-root order
in Wasserstein radius. Regret compares expected cost to the decision knowing the
true distribution. Section 5.2 also gives general regret-DRO and absolute-DRO
policies over randomized actions; their efficient computation is left open.

Suggested prose: “Besbes, Ma and Mouchtaki study ski rental within a framework
of heterogeneous historical data and known-radius distribution shift, obtaining
rate-optimal additive regret bounds. We instead optimize a supplied forecast
under a fixed pointwise competitive-ratio cap.”

No explicit equivalent of the candidate's discrete uniform frontier or sharp
`b+1` support family was found in those statements or Appendix E proofs. This is
an inspected-source comparison, not a priority conclusion.

### Diakonikolas–Kontonis–Tzamos–Vakilian–Zarifis

[Official PDF](https://proceedings.mlr.press/v139/diakonikolas21a/diakonikolas21a.pdf),
§1.1 (PDF p2), defines expected cost relative to the distribution-knowing
`OPT_D`, with i.i.d. sample access. Section 2.2 (PDF pp5–6) analyzes continuous
log-concave densities, including interval-uniform densities; the unrestricted
optimal policy buys initially or rents indefinitely. Section 2.3, Corollary 2.8
and Theorem 2.9 (PDF p6), combine a learned policy with a classical baseline.
The combiner guarantees per-instance cost at most the minimum of the advice
cost times `lambda` and baseline cost times `lambda/(lambda-1)`. Thus it can
indeed imply a pointwise expected competitive bound; saying this paper lacks
pointwise robustness would be wrong.

Suggested prose: “Diakonikolas et al. learn ski-rental policies from sampled
distributional advice and combine them with a robust baseline. Our objective is
exact forecast-cost optimization at each prescribed robustness cap.”

Their sample/approximation tradeoff and continuous log-concavity result do not
state the candidate's discrete uniform frontier. Uniform log-concavity alone
does not establish equivalence to that constrained theorem.

### Khanafer–Kodialam–Puttaswamy

Crossref's publisher-deposited authors are exactly Ali Khanafer, Murali Kodialam,
and Krishna P. N. Puttaswamy. Do not add authors from secondary search snippets,
or insert the DBLP middle initial into an unmodified official export.
The [primary Bell Labs institutional abstract](https://www.nokia.com/bell-labs/publications-and-media/publications/the-constrained-ski-rental-problem-and-its-application-to-online-cloud-cost-optimization/)
explicitly concerns known first or second moments of the number of ski days.
These are moments of the environment's horizon, whereas the draft's
`E[T-1] <= b(R-1)` is a constraint on the algorithm's buying-day law derived from
pointwise robustness.

Suggested prose: “Khanafer, Kodialam and Puttaswamy use moment information about
the horizon distribution. Our moment constraint concerns the randomized buying
day and follows from a pointwise competitiveness requirement.”

Limit: IEEE fulltext URLs returned HTTP 418/robot checks; the author research page
returned HTTP 410. No theorem/formula comparison or no-equivalence conclusion is
certified from this inaccessible conference fulltext. The institutional abstract
supports the narrow sentence above; it does not resolve the uniform-frontier
question. The 2015 journal extension has a different title and DOI and must not
be silently substituted for the 2013 conference record.

### Dinitz–Im–Lavastida–Moseley–Vassilvitskii

[Primary full version](https://arxiv.org/pdf/2308.05067), §2 (PDF p6) and §3,
Definition 1/Lemma 4 (PDF p8), define tail constraints at each adversarial horizon:
the buying-day probability that realized competitive ratio exceeds a threshold
must be at most a given tolerance. They minimize worst-case expected competitive
ratio subject to those tail constraints. Theorem 7 (PDF p8) characterizes tight
competitive/tail rows; Appendix E, Theorem 19 (PDF p24), analyzes a constructive
LP procedure. This is relevant precedent for structural optimization of
randomized ski rental. Its support truncation to buying days at most the buy
cost serves that objective; it cannot simply be imported into forecast-cost
minimization, where delayed purchases can help.

Suggested prose: “Dinitz et al. minimize worst-case expected competitive ratio
subject to high-probability tail bounds. We fix a cap on expected competitive
ratio at every horizon and minimize forecast expected cost.”

The inspected statements and construction do not present the candidate's uniform
forecast frontier. The tail bounds concern the algorithm's realized random cost,
not probability over an assumed horizon forecast.

### Cui–Dinitz two-slope tail risk

[Primary full version](https://arxiv.org/pdf/2508.06809v2), definitions (PDF p3),
Theorems 1–7 (PDF pp4–6), and algorithm sections/appendices (PDF pp28–34)
were inspected. The model retains a lower ongoing rental cost after purchase.
It minimizes worst-case expected competitive ratio under tail bounds.
Theorem 5 bounds an optimal support by a finite interval plus never-buy;
Theorem 6 gives greedy binary search with feasible value at most `OPT+epsilon`
in `O(log(1/epsilon))` iterations. Theorem 7 gives an exact LP with
`Theta(L_b/tau)` variables and constraints, using their structural bound.

Suggested prose: “Cui and Dinitz derive support structure for two-slope ski
rental with tail constraints, supporting greedy approximation and an exact LP.”

This supports crediting bounded-support and LP/greedy methods in neighboring
models; it does not establish the proposed discrete uniform fixed-cap frontier.
Use the publisher export's 2026 publication year if citing the chapter, while
describing it as the WAOA 2025 paper.

## Additional current primary leads

[Kang, Park and Fan, arXiv:2512.07313v1](https://arxiv.org/abs/2512.07313v1)
was inspected beyond the abstract. Algorithm 1 (PDF p3) takes buy cost, a finite
horizon bound and a prior, and returns a deterministic buying day. Equation (3)
uses the ratio of forecast expected cost to forecast expected offline cost.
Theorem 1 (PDF p4) treats a discrete uniform prior on `{1,...,N}`: buy immediately
when `b <= (N+1)/2`, otherwise never buy, represented by `N+1`.
For `N=b>=2` this includes the same never-buy forecast behavior as the
candidate's plateau, but no input robustness cap `R`, randomized `b`-piece
frontier, or unique `b+1` positive-support family appears in the inspected
algorithm/theorems. This is a model comparison, not an audit of all that paper's
Bayesian optimality claims. The abstract's robust-worst-case language should not
be treated as a theorem giving an exact prescribed-cap optimizer.

[Cardas, Perotin and Simon, arXiv:2610.26214](https://arxiv.org/abs/2610.26214)
studies a uniformly timed stochastic signal conditional on an adversarial
horizon. Its uniformity concerns signal arrival, rather than a supplied uniform
horizon forecast. It is a different-model lead, not evidence of an equivalent
uniform-frontier theorem.

The additional Bayesian lead also has an unmodified [official arXiv BibTeX export](https://arxiv.org/bibtex/2512.07313), saved as `distribution-bayesian-official.bib`, key `kang2025learningaugmentedskirentaldiscrete`. Its metadata names Bosun Kang, Hyejun Park and Chenglin Fan (2025). No venue is inferred.

## Search scope and limits

The comparison target was precisely: supplied `p=Uniform{1,...,b}`, expected
forecast cost, cap `E_T C(T,x) <= R min(x,b)` for every positive integer horizon,
exactly `b` affine decreasing pieces plus a plateau, and a unique optimizer with
all `b+1` buying days positive on an open robustness interval. None of the
accessible texts above explicitly states that conjunction. The Khanafer fulltext
gap remains, as do all limits of a bounded literature search. This audit does
not accept novelty, correctness, significance or venue fit.

Current searches included `ski rental "uniform distribution" "robustness"
"frontier"`, `ski rental "uniform" "b+1" "support"`, and `ski rental
"distribution" "piecewise linear" "robustness" uniform`. Discovery snippets
were not used as technical evidence. Kim–Fan uniform experiments on supports
larger than the buy cost must be distinguished from the analytic target above;
that reference and software trace are handled separately by the parent agent.

Downloads, SHA-256 hashes, URLs and access failures are recorded in
`distribution-download-provenance.json`. No manuscript build was run because this
helper's authorized write scope excluded manuscript and bibliography changes.
