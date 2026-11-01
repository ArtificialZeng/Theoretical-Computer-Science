# Research pass 1: finite exclusions and the remaining gluing kernel

Job `c012-upcycles-research-cfe911474960`, 2026-11-01. Original status:
**unresolved**. Candidate kind: **none**. This is a research record, not a
manuscript or an independently accepted mathematical claim. The immutable
question is still existence of ANY nontrivial upcycle with d>1 over ANY finite
alphabet and order. No finite negative result settles it.

## Exact initial test

`research1_sat.py` creates one Boolean per ordinary global cyclic position.
For every unordered pair of ordinary positions p,q used in a comparison, a
shared gate z is constrained by all four clauses for z=(x_p XOR x_q).
For each distinct pair of starting indices i,j, its clause requires at least
one mismatch at an offset ordinary in both n-windows. Identical-position XORs
are false, never free mismatch flags. Distinct starts actually make p=q
impossible here, but the implementation handles it explicitly.

Two partial windows have a common total completion exactly when they have no
ordinary mismatch. Thus these clauses are equivalent to pairwise disjoint
coverage. Each window has d independent wildcard occurrences and covers 2^d
total words. With L=2^(n-d), pairwise disjointness is equivalent to covering
every total word exactly once. The first ordinary bit is fixed to 0 only in
unpinned searches: complementing all ordinary bits preserves every mismatch,
so this excludes no isomorphism class.

All 28 weight-2 masks and all 56 weight-3 masks on n=8 are covered by the
rotation/reversal orbits in `triage-sanity.json`. Rotating/reversing a cyclic
partial word preserves uniqueness; no arbitrary coordinate permutations are
used. There are four weight-2 classes and five weight-3 classes. One weight-3
class, `*.*..*..`, is excluded by the source's Corollary 8.7. The eight remaining
representatives all returned UNSAT:

| d | Mask | Result |
|---|---|---|
| 2 | `**......` | UNSAT |
| 2 | `*.*.....` | UNSAT |
| 2 | `*..*....` | UNSAT |
| 2 | `*...*...` | UNSAT |
| 3 | `***.....` | UNSAT |
| 3 | `**.*....` | UNSAT |
| 3 | `**..*...` | UNSAT |
| 3 | `*.*.*...` | UNSAT |

Every run finished below 1.52 seconds under its predeclared 60-second cap.
The CNFs, full logs, metadata and LRAT certificates are in `research1-sat/`.
The independent standard-library checker `research1_lrat_check.py` verified
all eight certificates (and all three negative controls), checking every RUP
addition through a final empty clause. It rejects unsupported negative RAT
hints. `research1-proof-checks.json` records hashes and addition counts.
This validates these CNFs; the completeness/symmetry argument above remains
part of their mathematical interpretation, not something the checker proves.

Benchmarks pinned the exact source n4d1 and first n8d1 words; both were SAT
and their models passed independent expansion. A flipped n4 bit, an all-zero
n4 filling and a flipped n8 bit were UNSAT. All 64 ordinary assignments in
the fixed n4d1 frame agree between the generated formula and literal coverage.
`research1-checker-controls.json` records acceptance of a tiny genuine proof,
rejection of three deliberate invalid/incomplete proofs, and all 16 truth-table
rows of the cardinality recurrence used below.

## Failure analysis: tiling versus cyclic overlap

For a mask with minimal period m, any actual cycle has exactly L/m windows of
each distinct mask orientation. Omit overlap and choose that many tiles
(ordinary assignments) of each orientation so their subcubes partition Q_n.
This necessary phase-balanced exact-cover relaxation is implemented separately
in `research1_relaxation.py` with exact cardinality recurrences.

All four d2 classes are SAT in this relaxation. Each saved model has 64 tiles
and an independently verified 256-entry all-one coverage array. None of these
particular models can be glued directly: they have vertices of zero in/out
degree in the literal overlap graph. All four surviving d3 classes are UNSAT
already in the relaxation; the independent LRAT checker verified all four
certificates (`research1-relaxation-proof-checks.json`). This is a finite
balanced-tiling obstruction, not a general obstruction to d>1.

An attempted simpler obstruction used Fourier subsets private to one
orientation. If S is a nonempty subset of ordinary coordinates contained in
only that orientation, the signs of the selected assignments must sum to zero
on S: sum the cube partition identity against the character chi_S. All other
tiles integrate to zero because S meets a wildcard. With four tiles in each
d3 orientation, normalized local codes satisfying all these private constraints
still exist: respectively 57, 8, 16 and 15. Thus private Fourier constraints
alone do not explain the UNSAT results; shared constraints matter. This is
an observed failure of this local argument, not a no-go theorem for Fourier
methods. Code and exact reproduced counts are retained.

## A changed construction method and a precise unresolved kernel

For fixed binary n,d and mask orbit, form a directed graph whose possible edges
are all partial n-tiles in those orientations. The edge for tile t goes from
t[:-1] to t[1:]. Select edges so that:

1. Their subcubes partition Q_n exactly once.
2. Each literal partial-(n-1)-word vertex has equal selected indegree and outdegree.
3. All selected edges belong to one weakly connected component.

For L=2^(n-d)>n and 0<d<n these three conditions are equivalent to an upcycle
with the prescribed mask orbit. Necessity follows by taking its successive
windows, which cannot repeat a tile. For sufficiency, a finite balanced weakly
connected directed graph has an Euler circuit: follow unused outgoing edges
until a closed walk forms, then splice further closed walks until all edges
are used; balance prevents getting stuck except at the start. Read the first
character of each edge in that circuit. Consecutive edge labels agree in their
n-1 overlapping characters, including across the closing edge. Consequently
the length-n cyclic windows of the resulting length-L partial word are exactly
the selected tiles. Their unique coverage, d and nontriviality follow from
condition 1 and the fixed frames. This elementary encoding lemma is a research
tool; no independent novelty or publication value is asserted for it.

`research1_euler.py` encodes conditions 1 and 2 only. Each binary vertex has at
most two incoming and two outgoing possible edges, so equality is imposed by
explicitly forbidding every unequal incident-bit assignment. It then checks
condition 3 on each SAT model, constructs an Euler tour when possible, and
performs independent literal verification. Both pinned known source controls
recovered connected tours and passed. The flipped n4 control was UNSAT.

The adjacent-star n8d2 frame `**......` is UNSAT even with only conditions 1–2;
its certificate is independently checked. The period-4 frame `*...*...` is SAT
with four components of 16 edges each. The initial global-position certificate
already excludes a connected solution for this fixed finite case, giving a
useful negative control for any future connectivity implementation.

The changed constructive test n12d3, frame `...*...*...*`, has 2048 tile
selectors and 37376 clauses. It is SAT in conditions 1–2. The saved model
selects 512 tiles and has 22 components: 21 of length 24, one of length 8.
`research1_extract_families.py` extracts a closed Euler word per component and
literally checks that their windows together cover all 4096 binary 12-words
once, with three wildcards per window. The saved four-component n8d2 model is
checked in the same way. These are multiple-cycle objects, NOT upcycles.
The tori literature already studies universal partial quasi-families, so that
terminology and the general idea are prior work, not innovations claimed here.

The remaining kernel in this construction is explicit: can the n12d3 tile
partition be selected with a connected literal-overlap graph? The saved model
does not answer that. This fixed-parameter kernel is sufficient for a positive
answer to the original question, but is not equivalent to the unrestricted
original existential statement.

## One next test

Implement sound, guarded connectivity cuts on the n12d3 Euler exact-cover
formulation, benchmark them against n4d1 SAT and the certified n8d2 period-4
UNSAT case, then allow at most 20 refinement rounds and 180 total solver-wall
seconds, each call at most 30 seconds. Choose the selected tile r covering the
constant zero word as a root edge. For a disconnected selected component with
vertex set S not containing r's endpoints, and any possible internal edge e,
the necessary cut is

  (not y_r) OR (not y_e) OR (OR y_f for edges f leaving S).

It is sound: if r and e are retained in a connected balanced selection, there
must be an edge leaving S. The guards are essential; do not forbid a component
unconditionally when a later solution could lie entirely inside its vertices.
Every connected model must produce an exact 512-character word, recompute
n-periodicity and d=3, and have a 4096-entry all-one literal count array.
UNSAT concerns only this fixed frame; unknown/stagnation warrants parking or
a separately justified structural change, not cap escalation.

## Current primary sources and publication limits

Rechecked the [2026 publisher](https://link.springer.com/article/10.1007/s10623-026-01841-x)
Question 9.2 and Remark 6.6 and the [current arXiv record](https://arxiv.org/abs/2310.13067)
(latest version v3, 14 April 2025). Three current searches covered upcycles,
diamondicity, d>1 and 2025/2026 construction follow-ups; no full resolution
was located. The [author-cited code repository](https://github.com/wcarey-gmu/universal-partial-words)
describes a randomized/pruned tree search and a partial n8 data list, not an
inspected resolution. [Universal partial tori](https://link.springer.com/article/10.1007/s10623-025-01609-9),
Sections 8–9, defines quasi-families and discusses their relation to the known
diamondicity-one setting. These bounded checks do not prove priority of any
finite observation or method here. See the three saved web-confirmation JSONs.

No claim.json, review request, manuscript or PDF is justified under the project
policy. All original alphabets/orders outside the tested cases remain open
within this job; even n12d3 connectedness has not been searched yet. Pass 1 has
genuinely new finite certificates and an independently verified changed-method
artifact, so one more bounded pass has a concrete positive-witness test.
