# Current primary-source comparison for research revision 2

Job robust-stopping-research-cd75b220d422; checked 2026-10-31.
This is a bounded comparison, not a certificate of priority or venue fit.
Searches included combinations of ski rental, uniform forecast/distribution,
robustness, randomized optimum, Pareto frontier, support, moment constraints,
and exact optimizer. Search results located papers; the comparisons below
use the primary passages specified. No external write/account action occurred.

## Most consequential overlap

[Kim--Fan v1](https://arxiv.org/html/2603.29233v1), Sections 5.1-5.3,
Appendix C.4 Theorem C.1(ii), D.2-D.7 were inspected in the cached original
HTML and reopened in the current primary HTML. Their monotone-cost theorem
5.2 and restricted extension 5.3 do not cover the uniform cost, which has
g(1)=g(2) and then decreases. Their one-hot-b optimizer is much closer:
the uniform proposed law is exactly the C.1 selected law below R=2-1/b,
and above that cut it is another one-hot-b optimum. The complete algebra
and a direct finite check of the C.1 equation are in `prior-overlap.md` and
`prior-overlap-checks.json`. Therefore no new geometric schedule, no first
prefix-plus-tail support family, and no first route to b+1 support necessity
is claimed. The uniform value's explicit b+1 pieces, their rational
breakpoints, and its strict dual uniqueness proof are the structural
extension to be evaluated alongside the general optimizer. This overlap
substantially limits how that extension may be sold.

D.2's identified expected-cost/support-level inference and the published
Algorithm 3 fragment are addressed precisely in `kf-trace-and-normalization.md`.
The latter's indexing and candidate-tail differences prevent a claim about
a uniquely specified literal implementation output. The contradiction to
the conceptual support-threshold prescription is exact and independent
of those details. A current official PMLR record is also available at
https://proceedings.mlr.press/v306/kim26l.html (PMLR 306, 57411-57444).
The mathematical target remains arXiv v1; no assertion is made that every
later proceedings version has identical appendices or algorithm text.

[Li--Christianson--Li v1](https://arxiv.org/html/2510.14887v1), Section 5.2,
Appendices D.1-D.3 and E.1, already contains equalizing distributions,
point-prediction Pareto transformations, and support [b] union {y+1}.
These are close prior structures, not new principles of this revision.
The inspected theorems concern prediction-specific one-hot consistency;
no uniform-forecast expected-cost frontier matching theorem U was found.
That statement is a source-limited observation, not a proof of absence.

## Distributional advice, robust optimization, and different risk metrics

[Diakonikolas--Kontonis--Tzamos--Vakilian--Zarifis, ICML 2021]
(https://proceedings.mlr.press/v139/diakonikolas21a/diakonikolas21a.pdf),
Sections 1.1 and 2.1-2.3, especially Corollary 2.8 and Theorem 2.9,
includes uniform inputs as a log-concave family. Its sampling guarantees
and robust strategy-combination bound do not identify the exact constrained
uniform frontier here. Mixing and known-distribution optimization are
prior ingredients. No novelty is claimed for either general idea.

[Besbes--Ma--Mouchtaki, Beyond IID]
(https://arxiv.org/html/2206.09642v4), Appendix E model, E.1-E.2
Propositions E-7/E-8, and E.3 equation (E-28), was inspected. It treats
known-radius distributional heterogeneity and asymptotic worst-case regret,
including an inflated decision rule under Wasserstein distance. This
addresses the reviewer's important missing robust-optimization lineage.
Its decision/uncertainty model differs from an externally prescribed
pointwise competitive cap and fixed-forecast expected objective. The
inspected statements do not provide theorem U. Its model must be cited
without suggesting distributionally robust ski rental originated here.
The 2025 journal record is also cited in Cui--Dinitz's primary bibliography;
use that bibliographic record conservatively if publisher refresh fails.

[Cui--Dinitz](https://arxiv.org/html/2602.21104v1), Sections 2.2-2.3 and
its Besbes comparison, confirms the distinction between known heterogeneity
radius and unknown-error prediction guarantees. Its additive-loss metric
is not the source's fixed hard cap. Earlier source comparison in
`literature/triage-screen.md` remains available; no new exclusion is inferred
from its citation count alone.

[Wei--Zhang, NeurIPS 2020]
(https://papers.nips.cc/paper_files/paper/2020/file/5bd844f11fa520d54fa5edec06ea2507-Paper.pdf),
Theorem 1.2 and Section 2's infinite-LP lower-bound discussion, has the
classical point-prediction robustness-consistency frontier and its large-buy-
cost qualifiers. Exact LP methods, geometric policies and tradeoffs have
this established lineage; this revision is not a new general tradeoff
paradigm.

[Dinitz--Im--Lavastida--Moseley--Vassilvitskii]
(https://arxiv.org/pdf/2308.05067), Sections 1.1.1 and 3.1, studies bounds
on the probability that the realized competitive ratio exceeds a threshold,
while optimizing worst-case expected competitiveness. Its structural
active-constraint characterization is important prior art, but its extra
constraints concern policy tail risk rather than an expected forecast cost
with a prescribed worst-case cap. No equivalence to theorem U was found
in the inspected passages. Opening a nonexistent HTML v2 failed; the primary
PDF succeeded, so the failure is not treated as mathematical evidence.

[Cardas--Perotin--Simon](https://arxiv.org/html/2610.26214v1), model overview
and Section 3.1, uses a uniform signal time scaled by the adversarial horizon.
That uniform distribution is over a horizon-correlated signal; our law
receives no signal and is drawn independently before the season. Thus its
uniform terminology is not this uniform forecast family.

## Historical leads and access limits

The classical author/publisher sources for competitive snoopy caching and
competitive randomized nonuniform problems, and the Purohit--Svitkina--Kumar
NeurIPS 2018 primary paper, were located for the expanded writing phase.
Their full historical coverage has not been used as a novelty exclusion
certificate. The baseline deterministic/randomized ski-rental results
must receive their original credit. The official NeurIPS 2018 PDF is
https://papers.nips.cc/paper/8174-improving-online-algorithms-via-ml-predictions.pdf.
The primary historical author text is
https://courses.csail.mit.edu/6.895/fall03/handouts/papers/karlin.pdf.

Khanafer--Kodialam--Puttaswamy INFOCOM 2013, DOI
10.1109/INFCOM.2013.6566944, is a required moment-constrained lineage lead.
The official IEEE endpoint displayed a robot/JavaScript gate in this pass.
Its full theorem text was not inspected, and no purported exclusion or
exact theorem attribution to it is asserted. A search-hit slide deck and
secondary summaries are insufficient substitutes. Record external refresh
unavailable, retain a conservative reference, and inspect original text if
it becomes accessible; this metadata/access limit is not a veto on an
otherwise accepted clean manuscript. The new frontier's novelty relative
to every historical moment/DRO theorem is not certified.

## Generic-LP comparison and candidate decision

The old finite LP already gives generic polynomial bit-time solvability.
The new paper must not claim a speedup on that basis. The moment row contains
large t-1 coefficients, so the review's blanket matrix-entry<=b observation
is false; this does not create an asymptotic advantage for the new method.
The revised contribution remains a concrete certifying repair to the
support-level optimizer, supplemented by an explicit uniform objective
frontier and precise support necessity/uniqueness facts. A fresh referee
must assess both correctness and whether that combined delta is worthwhile,
with full knowledge of the one-hot overlap. No exact duplicate of the
complete combined statement was found in the inspected primary passages.
This bounded search does not establish priority, journal acceptance, or
STOC-level significance. The new result is not split into another paper.

## Official presentation fact checked for the future response

The [official STOC 2027 CFP]
(https://acm-stoc.org/stoc2027/stoc2027-cfp.html), submission-format and
identification paragraphs, requires named authors and a title page, then
11pt-or-larger single-column, single-space, Letter paper with one-inch
margins. It encourages references at the end. Thus the reviewer's suggested
anonymization and deletion of the title page should not be followed. The
user's <=12 total pages, exact five-author list, official unmodified class,
and AI disclosure before the final bibliography remain controlling. No
submission, upload, or author-consent action was taken.
