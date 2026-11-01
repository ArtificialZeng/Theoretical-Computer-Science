# Precise problem and triage disposition

The original input is preserved verbatim in `source.md` (SHA-256
`3ec230456a31ba9b004000be9e79c74a77636a28a31e9b4eec31918f5ab305ed`).
This document interprets that input; it does not replace or weaken it.

## Objects, information, and quantifiers

For each integer n >= 1 let U and V be disjoint labelled sets of size n.
The realized input is a simple unweighted bipartite graph G=(U,V,E) with
deg_G(x) <= 2 for every x in U union V, and an arbitrary permutation pi of V.
Isolated vertices are allowed; components are paths, even cycles, and isolated
vertices. The algorithm knows U, n, and the identifiers used in the advice,
but not E, pi, future neighborhoods, or the component decomposition.
At time t, pi(t) and its entire neighborhood are revealed. The algorithm
irrevocably selects an unused neighbor or leaves that vertex unmatched.
Its output M is an integral matching contained in E.

Advice is exactly a table a:V -> U union {bottom}, with no repeated non-bottom
value. Thus A={(a(v),v):a(v) != bottom} is a matching in the complete bipartite
graph on the labels. A need not be contained in E and need not be maximum.
This reading reconciles the source's phrase "feasible integral matching"
with its explicit permission for advised edges to be absent. Requiring A to
be feasible in the realized G would define a different problem. There are no
annotations, alternative label encodings, or additional predictions. The
table does reveal its own proposed pairs, as explicitly authorized by source.

Let OPT(G) be the maximum matching cardinality. For c,r in [0,1], the target
is the set of pairs for which one randomized online algorithm family B exists
such that, simultaneously, for every n,G,pi:

* For every matching A contained in E with |A|=OPT(G),
  E[|B(G,pi,A)|] >= c OPT(G).
* For every advice table A of the form above,
  E[|B(G,pi,A)|] >= r OPT(G).

Expectation is over the algorithm's private randomness; G, pi, and A are
fixed independently of that randomness (the standard oblivious adversary
reading). The source does not explicitly distinguish adaptive adversaries.
All recorded impossibility examples are fixed inputs and therefore also
apply against adaptive adversaries; no adaptive achievability claim is made.
Consistency is required for every optimal advised matching, not just one
oracle-selected optimum. Guarantees are multiplicative with no additive loss,
uniform in n; OPT=0 is vacuous. No running-time bound is imposed by the source.
The requested frontier is the coordinatewise maximal boundary of this
downward-closed achievable set, or a substantively sharp parameter regime.

## Closest inspected results and exact overlap

Choo, Gouleakis, Ling, and Bhattacharyya, *Online bipartite matching with
imperfect advice*, arXiv:2405.09784v3, Section 3, Theorem 3.1 and its extension
in Appendix A, give c+r <= 3/2 (c >= 1/2). Their graphs are disjoint unions of
three-edge paths. Consequently their obstruction already has degree at most
two on BOTH sides. The endpoint (c,r)=(1,1/2) obstruction is also already known.
An independent direct verification in this exact matching-table model is in
`evidence/known-obstruction.md`; it requires no graph-valued advice.

Jin and Ma, *Online Bipartite Matching with Advice: Tight Robustness-Consistency
Tradeoffs for the Two-Stage Model*, arXiv:2206.11397, Section 3.1,
Proposition 3.1 and Figure 3, explicitly use the same two-by-two Z graph for
unweighted matching. Their two-stage achievability theorem cannot be
transferred to arbitrary vertex-by-vertex arrivals. Their consistency benchmark
also compares with following first-stage advice, rather than only requiring
performance on globally optimal full advice tables.

Bhangale, Chakraborty, and Harsha, *Optimal Online Bipartite Matching in
Degree-2 Graphs*, ISAAC 2025, Theorem 1, treat G(n,2), with only ONLINE degree
bounded. Their randomized integral ratio is about 0.717772; Theorem 2's 3/4
ratio concerns fractional matching. Neither statement establishes the exact
randomized integral optimum on G(2,2). Their Section 4.1 hardness construction
has offline vertices appearing in multiple phases, so that hardness does not
automatically obey this project's offline degree restriction.

Primary URLs, inspected locations, and limitations are recorded in
`literature/triage-sources.md`. Source status: **status-uncertain** for the
full G(2,2) frontier; **known** for the proposed degree-two linear obstruction.
The original question is neither proved nor disproved here.

## Original triage decision (historical)

**Park**, following source.md's explicit instruction to park when known
lower-bound constructions already satisfy the degree restriction. There is
no accepted novel contribution and no manuscript. The established obstruction
is an equivalence of examples, not an equivalence of the complete frontiers.
The basic (1,1/2) guarantee from advice-first greedy completion is routine and
does not justify a separate paper.

Nearest prior result X: the known degree-two Z-graph bound c+r <= 3/2.
Potential delta Y, not admitted: a previously unestablished sharp achievability
regime for sequential randomized integral G(2,2) matching. Verification route Z:
first establish the exact advice-free G(2,2) baseline, then seek a matching
upper/lower tradeoff beyond routine interpolation and screen its novelty.

One next test, only if reopening is authorized: inspect and verify the
two-sided-degree-two randomized integral baseline, asking specifically whether
3/4 is achievable on all paths and even cycles under arbitrary online order.
A positive proof would make simple mixing with the routine (1,1/2) algorithm
meet the already-known linear obstruction, and would require a value/novelty
check before any new project is admitted. No such proof is asserted here.

## Authorized reopening and research-pass delta

Requirements.md explicitly reopened this lead after the triage by supplying
candidate-argument.md and exact parent checks. That file is an unaccepted seed,
not an audit. The research target is the degree-aware achievability and the
cycle advice frontier; the known degree-two obstruction is not rebranded.
The source text and all quantifiers above are unchanged.

Research pass 1 proposes the complete formulas, for every requested c in [0,1],

    r_D(c)=min{3/4,3/2-c} on maximum degree two on both sides;
    r_C(c)=min{7/8,7/4-c} on the 2-regular subclass.

A complete analytic argument is in evidence/frontier-proof.md and independent
finite checks in evidence/check_frontiers.py and evidence/frontier-checks.json.
These are researcher claims awaiting fresh mathematical and value review.
The cycle 7/8 baseline, its algorithm, and its orientation method are known:
Fàbrega--Muñoz (2018), Proposition 2, and Feng et al. (2025), Algorithm 2.
The proposed delta is the advice-preserving priority rule, the exact advice
frontiers, and the path component analysis; interpolation itself is standard.
Primary comparisons and explicit significance/novelty limits are in
literature/research-comparison.md. Full original resolution is proposed only
under the frozen fixed oblivious graph/order/advice reading above. No adaptive,
fractional, weighted, or online-degree-only theorem is claimed.

Current handoff: candidate for fresh referee. No mathematical acceptance,
manuscript, PDF, or release has occurred. If the fresh referee identifies
equivalence or insufficient substance, park without creating a paper.
