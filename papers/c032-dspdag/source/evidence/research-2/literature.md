# Bounded current primary-source comparison, research pass 2

Job c032-dspdag-research-5f16f6951448, checked 2026-11-02 UTC. This is proposer
research, not a fresh referee report, exhaustive priority search, or STOC label.

## Exact target and nearest baseline

[Akmal--Vassilevska Williams--Wein, arXiv:2404.15916v2](https://arxiv.org/abs/2404.15916v2),
printed pp.2 and 41, gives the O(m n^(k-1)) DAG baseline and asks Open Problem 3
with existential fixed k>=3 and delta>0. The local input PDF/text and hashes
are in intake/primary and intake/source-inputs.json. The current primary arXiv
page still lists v2, 10 May 2024, on this check. AVW credits Fortune--Hopcroft--
Wyllie 1980 Theorem 3 and Berczi--Kobayashi 2017 Proposition 10 for the baseline
and shortest-path adaptation. Those attributions here are through the inspected
AVW primary account; the original FHW full proof was not newly obtained in R2.
The new proof rederives its own frontier semantics rather than assuming an
uninspected baseline lemma. The ICALP record is
[DOI 10.4230/LIPIcs.ICALP.2024.9](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2024.9).

[Choudhary--Kumar--Saggi, ITCS 2026 Theorem 1.1](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.39)
concerns two prescribed pairs in general directed graphs, with detection in
O(mn log n). Its official abstract also gives Min-2-DSP results. This is a
different fixed number of pairs from the three-pair dense bound in the claim.
The primary arXiv page for [2509.14588](https://arxiv.org/abs/2509.14588)
currently lists v2, 8 October 2025; its local full text is available. The
current planar result [2505.03353](https://arxiv.org/abs/2505.03353) is an FPT
algorithm for planar graphs, and the lower-bound source
[2408.03933](https://arxiv.org/abs/2408.03933) concerns approximation and
variable-parameter hardness. Neither inspected scope supplies a full
three-pair unrestricted-DAG exponent equivalent to the new claim.

## Rectangular primitive and the field actually used

[Le Gall--Urrutia, arXiv:1708.05622v2](https://arxiv.org/abs/1708.05622v2),
Table 3, gives exponent <=3.251640 for (n by n^2) times (n^2 by n).
Section 2.2, Definitions 2.2--2.5 and Theorem 2.1, specifies polynomial
degenerations over a field F and the border-rank exponent. The new proof
specializes to Q, converts one fixed degeneration by coefficient interpolation,
permutes tensor groups and specializes a fixed rational exact algorithm modulo
a prime above N. These conversion steps and their charges are supplied in the
new proof; the table alone is not asserted to imply unit-time Boolean products.
The prime choice, constant denominators, O(log N)-bit residues and bit overhead
are explicit. The local PDF/text were read at the relevant definitions/table;
they are stable scientific inputs. No fast rectangular implementation or
independent reproof of the laser-method bound has been performed in this job.

[Vassilevska Williams--Xu--Xu--Zhou, arXiv:2307.07970v2](https://arxiv.org/abs/2307.07970v2),
Introduction/Table 1, improves the arithmetic exponent to <3.250385 and
Section 3 defines the tensor formalism over F. The primary current page lists
v2, 4 November 2023. This was rechecked as a precise comparison; the numerical
corollary conservatively uses the older sufficient Le Gall--Urrutia bound.
No current-record claim is made for either exponent. Matrix multiplication,
permutation symmetry and the rational interpolation technique are prior tools.

## Generic recursion is prior work; proposed substantive difference

[Valiant, General context-free recognition in less than cubic time, 1974 report](https://people.csail.mit.edu/virgi/6.890/papers/valiantcfg.pdf),
journal version JCSS 10(2):308--315 (1975), DOI
[10.1016/S0022-0000(75)80046-8](https://doi.org/10.1016/S0022-0000(75)80046-8),
already uses divide and conquer and Boolean multiplication for closure. The
local text's introduction and summary were inspected, including its integer
modulus conversion. Thus no generic chronological-recursion or algebraic-
Boolean principle is claimed as new. The specific proposed delta is the
k-way output-minimum partition for labelled frontier transitions, b^(k-1)
context packing, and its sum across all dyadic nodes, giving the all-fixed-k
saving and the O(n^3.3) three-pair theorem. This must pass fresh scrutiny for
novelty and significance; a combination of known tools is not automatically
substantive innovation or STOC competitiveness.

A search lead titled Efficient Algorithms for k-Disjoint Paths Problems on
DAGs (Fleischer--Ge--Li--Zhu, 2007, DOI 10.1007/978-3-540-72870-2_13) was
checked via its author-hosted primary PDF search excerpt:
[author copy](https://people.iiis.tsinghua.edu.cn/~jianli/paper/disjointpath.pdf).
Its abstract specifies k paths between one common source and target with
MinMax/Balanced/MinSum objectives. That scope does not itself give the arbitrary
prescribed-pair theorem. Full opening of that URL returned an access error;
only its primary search excerpt was available, so no claim about uninspected
theorems in the body is made.

## Actual search scope and limits

Fresh queries included combinations of disjoint shortest paths, DAG, matrix
multiplication, rectangular, minimum frontier, n^{k}, 3.25, 3.3, and 2026,
plus exact searches for the older similarly titled algorithm and the primary
rectangular papers. Current arXiv versions and official ICALP/ITCS abstracts
were opened. No inspected primary statement gave the proposed exact full
bound. This bounded negative result is not proof of priority; incompletely
indexed/new work, unavailable full texts and equivalent formulations may
remain. No newly found claimed original-scope resolution was dismissed merely
for lacking a formal proof or external review. Fresh referee literature review
is still required for the new scientific snapshot.
