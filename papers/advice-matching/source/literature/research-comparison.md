# Research-pass primary-source comparison

Date: 2026-10-31 Asia/Shanghai (2026-10-30 UTC).
Job: advice-matching-research-eee7dbe89d57. This is a bounded literature
screen, not proof of priority, verified open status, or a referee verdict.

The reopening is authorized by requirements.md and candidate-argument.md.
The original triage correctly identified a known obstruction; the newly
screened target is achievability and the cycle advice frontier. The complete
proposed argument is evidence/frontier-proof.md, not the unaccepted seed.

## Known cycle optimum and same root method

Josep Fàbrega and Xavier Muñoz, *Online Matching in Regular Bipartite Graphs
with Randomized Adversary*, LNCS 11011 (2018), pp. 297–310.
DOI: https://doi.org/10.1007/978-3-319-98355-4_17
Primary full chapter:
https://link.springer.com/content/pdf/10.1007/978-3-319-98355-4_17.pdf

Inspected Section 1.1's definitions and Section 2, especially Propositions
1 and 2 and Theorem 2 (printed pp. 300–303). Proposition 2 explicitly treats
randomized algorithms on a fixed adversarial input and proves competitive
ratio at most 8/7 in the authors' inverse convention, i.e. at least 7/8 in
our convention. It contracts degree-two online vertices into edges, propagates
directions along revealed paths, and analyzes independent directions at
initial disjoint edges. This substantially overlaps the cycle portion of the
seed's root argument. Its title's randomized-adversary model does NOT leave
the usual advice-free 7/8 cycle optimum unsettled. No claim is made that our
cycle baseline, orientation method, or advice-free upper gadget is novel.

Ilan Reuven Cohen and David Wajc, *Randomized Online Matching in Regular
Graphs*, SODA 2018, pp. 960–979.
https://www.cs.cmu.edu/~dwajc/pdfs/cohen18.pdf
DOI: https://doi.org/10.1137/1.9781611975031.62

Inspected introduction and Section 8's opening paragraph (PDF p. 12).
The paper explicitly records the 7/8 obstruction from a distribution over
8-cycles. It also describes deterministic maximum-current-degree priority
as an established ingredient from Naor--Wajc. These are prior ingredients,
not proposed contributions of this project.

## Same priority algorithm in modern OCS terminology

Yilong Feng, Haolong Li, Xiaowei Wu, Shengwei Zhou, *Degree-bounded Online
Bipartite Matching: OCS vs. Ranking*, arXiv:2510.00965v1 (1 October 2025).
https://arxiv.org/html/2510.00965v1

Inspected degree-bounded definition, Section 1.1, and Algorithm 2 with the
paragraph immediately following it. Their (k,d)-bounded convention requires
OFFLINE degree AT LEAST k and ONLINE degree AT MOST d; it does not mean
maximum degree k on both sides. Nevertheless, it includes our 2-regular
subclass at k=d=2. They explicitly identify a 0.875 guarantee as known and
optimal at d=2, using two-way semi-OCS. The limiting priority f(1) arbitrarily
large makes previously seen available offline neighbors preferred over fresh
ones, with a fair tie on two fresh neighbors. This is exactly the relevant
rule E on our cycles. Consequently E itself is not a new algorithm.
The reference is Gao et al., *Improved Online Correlated Selection*, FOCS
2021; its full text was not inspected in this pass. No claim is based on an
unread theorem from that source.

## One-side degree bound is a different class

Amey Bhangale, Arghya Chakraborty, Prahladh Harsha, *Optimal Online Bipartite
Matching in Degree-2 Graphs*, ISAAC 2025, Article 13.
https://drops.dagstuhl.de/storage/00lipics/lipics-vol359-isaac2025/html/LIPIcs.ISAAC.2025.13/LIPIcs.ISAAC.2025.13.html
DOI: https://doi.org/10.4230/LIPIcs.ISAAC.2025.13

Inspected Theorems 1–2, preliminaries, and the hardness model. G(n,2)
bounds only online degree; its 0.717772 randomized integral optimum and
3/4 fractional optimum do not determine randomized integral G(2,2).
We do not dispute either theorem or assert lossless rounding of fractional
Water-Level. The degree-aware rule's 3/4 guarantee on G(2,2) is proved
analytically in our dossier, rather than inferred by changing their model.
This source was already correctly distinguished by triage.

## Advice lower bound is already known

Davin Choo, Themistoklis Gouleakis, Chun Kai Ling, Arnab Bhattacharyya,
*Online bipartite matching with imperfect advice*, arXiv:2405.09784v3,
ICML 2024. https://arxiv.org/html/2405.09784v3

Inspected Section 3, Theorem 3.1, its immediately stated extension, and the
existing project derivation. Disjoint Z paths already imply c+r<=3/2 and
the 1-consistency/1/2-robustness endpoint. The direct table-only witness is
in evidence/known-obstruction.md. Its random-arrival achievability result is
a different input model. Neither this obstruction nor its two-sided degree
restriction is proposed as new.

Billy Jin and Will Ma, *Online Bipartite Matching with Advice: Tight
Robustness-Consistency Tradeoffs for the Two-Stage Model*.
https://arxiv.org/html/2206.11397

Inspected Section 3.1 and Proposition 3.1 with its proof. It also has the
Z graph and c+r<=3/2. Two-stage batched choices and its advice-value
benchmark differ from arbitrary sequential arrivals with good advice defined
as any full optimum matching table. Batched achievability cannot be used as
our sequential algorithm. Our interpolation is standard, and is credited as
such rather than treated as a technique contribution.

## Recent prediction papers: fractional actions

Davin Choo, Billy Jin, Yongho Shin, *Learning-Augmented Online Bipartite
Fractional Matching*, NeurIPS 2025.
https://proceedings.neurips.cc/paper_files/paper/2025/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf

Inspected introduction, Theorem 3, and Section 4's integral advice definition.
Its advice table has the same matching-shaped interpretation, but PAW and
its guarantees are for fractional matching actions. The upper bounds use
larger upper-triangular constructions. The inspected material does not state
a degree-two integral or cycle frontier. This paper also explicitly discusses
the ordinary coin-flip baseline, which we do not claim as new.

Alexander Lindermayr, Nicole Megow, Lauren Paul, *Consistency–Robustness
Tradeoffs for Online Bipartite Allocation with Multiple Stages*,
arXiv:2609.15837v1 (14 September 2026).
https://arxiv.org/html/2609.15837

Inspected Theorems 1–3 and the surrounding model comparison. Their classical
one-by-one theorem is vertex-weighted FRACTIONAL matching with integral
predictions and curve C(R)=1+R+ln(1-R), for R<=1-1/e. The number of stages
and fractional decisions are substantive distinctions; there is no direct
transfer of their theorem to our randomized integral two-sided degree
restriction. Their introduction credits the separate unweighted advice
results, rather than resolving our exact restricted class.

## Search scope, contribution, and value risk

Searches included exact G(2,2), both-side degree-two online matching,
2-regular/7/8 matching, paths/cycles predictions, consistency/robustness
with degree two, and the formulas with 7/4. These located the previously
missing exact cycle baseline, its proof, and the matching semi-OCS rule.
No equivalent statement of either MATCHING-ADVICE frontier was found in the
primary passages inspected. This is a dated, bounded negative search result,
not a universal novelty assertion. Advice-bit complexity, fully online
matching, and stochastic edge arrivals surfaced, but do not by their names
establish equivalence to our fixed-order matching-table setting. Broader
backward/forward citation searching remains incomplete. A Dagstuhl page for
Cohen--Peng (ESA 2023) was located, but no full-text theorem from it is used.

Exact proposed delta for fresh review: maximum-matching advice can be used
only to break fresh-neighbor choices while retaining exhausted-neighbor
priority; a decreasing-arrival argument proves optimality for EVERY optimum
advised matching. On cycles this preserves the deterministic 3/4 guarantee
under arbitrary wrong advice, giving the endpoint (1,3/4). The common-table
8-cycle bound gives c+r<=7/4, so mixing with the known 7/8 baseline yields
the exact cycle advice frontier. The path analysis supplies the full
G(2,2) achievability side and exact component expectations, meeting the known
Z obstruction for the original frontier. These are one connected proposed
contribution, not multiple papers.

The mathematical and significance gates are separate. Much of the argument
is elementary and the cycle token method is already known; a fresh referee
must decide whether the advice-preserving lemma/frontier characterization
constitutes a useful new result or merely a routine corollary too slight
for this project. The researcher requests that check explicitly. No claim
of venue fit, acceptance, or priority is made, and no manuscript is created.

Access notes: the large third-party-hosted complete book exceeded the web
reader's size limit, but the exact Springer chapter PDF was accessible and
supplied the decisive propositions. An initial versioned arXiv request for
the 2026 paper timed out; its ordinary HTML URL subsequently supplied the
full primary text. Shell-network DNS failed; no result is inferred from that
operational failure. No full text was uploaded, submitted, or redistributed.
