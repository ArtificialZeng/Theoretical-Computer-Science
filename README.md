# Theoretical Computer Science

[English](README.md) · [中文](README.zh-CN.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [日本語](README.ja.md)

Research manuscripts, reproducible code and exact certificates in theoretical computer science. This repository contains **16 manuscript packages**: eleven from this continuous-research collection and five from other conversations. Three additional conversation folders contain templates only. Each topic below has an abstract, a PDF, an unchanged source archive, and browseable source code.

**Read the scope labels:** Among the eleven packages in papers/, eight manuscripts are recorded as complete resolutions of their stated targets; three early manuscripts are partial-result notes whose broader original questions remain unresolved. These are local research/release records, not external peer review or STOC acceptance. The original author lists are preserved; the six later releases list Zijian Zeng as sole author.

## Manuscript index

| Topic | Pages | Scope | Files |
|---|---:|---|---|
| `coverage-sparse` | 8 | Target resolution | [PDF](papers/coverage-sparse/paper.pdf) · [ZIP](papers/coverage-sparse/source.zip) · [Code](papers/coverage-sparse/source/) · [Reproduce](papers/coverage-sparse/README.md) |
| `privacy-interpolation` | 7 | Legacy partial result | [PDF](papers/privacy-interpolation/paper.pdf) · [ZIP](papers/privacy-interpolation/source.zip) · [Code](papers/privacy-interpolation/source/) · [Reproduce](papers/privacy-interpolation/README.md) |
| `robust-stopping` | 11 | Legacy partial result | [PDF](papers/robust-stopping/paper.pdf) · [ZIP](papers/robust-stopping/source.zip) · [Code](papers/robust-stopping/source/) · [Reproduce](papers/robust-stopping/README.md) |
| `curvature-noise` | 6 | Legacy partial result | [PDF](papers/curvature-noise/paper.pdf) · [ZIP](papers/curvature-noise/source.zip) · [Code](papers/curvature-noise/source/) · [Reproduce](papers/curvature-noise/README.md) |
| `advice-matching` | 6 | Target resolution | [PDF](papers/advice-matching/paper.pdf) · [ZIP](papers/advice-matching/source.zip) · [Code](papers/advice-matching/source/) · [Reproduce](papers/advice-matching/README.md) |
| `c002-coverage` | 7 | Target resolution | [PDF](papers/c002-coverage/paper.pdf) · [ZIP](papers/c002-coverage/source.zip) · [Code](papers/c002-coverage/source/) · [Reproduce](papers/c002-coverage/README.md) |
| `c009-cycle2` | 6 | Target resolution | [PDF](papers/c009-cycle2/paper.pdf) · [ZIP](papers/c009-cycle2/source.zip) · [Code](papers/c009-cycle2/source/) · [Reproduce](papers/c009-cycle2/README.md) |
| `c012-upcycles` | 5 | Target resolution | [PDF](papers/c012-upcycles/paper.pdf) · [ZIP](papers/c012-upcycles/source.zip) · [Code](papers/c012-upcycles/source/) · [Reproduce](papers/c012-upcycles/README.md) |
| `c015-imagebound` | 6 | Target resolution | [PDF](papers/c015-imagebound/paper.pdf) · [ZIP](papers/c015-imagebound/source.zip) · [Code](papers/c015-imagebound/source/) · [Reproduce](papers/c015-imagebound/README.md) |
| `c017-wheeler` | 10 | Target resolution | [PDF](papers/c017-wheeler/paper.pdf) · [ZIP](papers/c017-wheeler/source.zip) · [Code](papers/c017-wheeler/source/) · [Reproduce](papers/c017-wheeler/README.md) |
| `c021-ccrapumping` | 9 | Target resolution | [PDF](papers/c021-ccrapumping/paper.pdf) · [ZIP](papers/c021-ccrapumping/source.zip) · [Code](papers/c021-ccrapumping/source/) · [Reproduce](papers/c021-ccrapumping/README.md) |

## What each project studies

### Coverage Correlation Gaps under Graph-Constrained Pairwise Independence

**Abstract.** How much does testing only selected pairs for independence reduce the best attainable coverage value? For k-colorable graphs and graphs of maximum degree at most k−1, the manuscript gives the exact worst-case ratio 1/[1−(1−1/k)^k]. Disjoint cliques give tight examples. A collision inequality also provides finite-instance and measurement-error bounds. The statement concerns suprema over graph classes.

[PDF](papers/coverage-sparse/paper.pdf) · [ZIP](papers/coverage-sparse/source.zip) · [Code](papers/coverage-sparse/source/) · [Reproduce](papers/coverage-sparse/README.md)

### Mandatory Excursions in Privacy-Constrained Probability Paths

**Abstract.** Can a privacy-constrained probability path stay between its endpoint probabilities? For swapped three-outcome distributions, the manuscript determines optimal budgets and the smallest unavoidable peak of the unchanged coordinate. It also derives sharp costs for monotone or endpoint-bounded paths and excursion certificates for general endpoints. This is a legacy partial-result note; the original general problem remains unresolved.

[PDF](papers/privacy-interpolation/paper.pdf) · [ZIP](papers/privacy-interpolation/source.zip) · [Code](papers/privacy-interpolation/source/) · [Reproduce](papers/privacy-interpolation/README.md)

### Certified Expected-Cost Optimization for Robust Ski Rental

**Abstract.** How should a ski-rental policy use a finite rational forecast while satisfying an expected competitive-ratio bound at every horizon? The manuscript gives exact expected-cost optimization with primal and dual certificates on unbounded buy-day and horizon domains, a support bound of b+1 days, and an explicit uniform-forecast frontier. Its running time is polynomial in numerical b and input bit length. The broader original question remains unresolved.

[PDF](papers/robust-stopping/paper.pdf) · [ZIP](papers/robust-stopping/source.zip) · [Code](papers/robust-stopping/source/) · [Reproduce](papers/robust-stopping/README.md)

### A Sparse-Cardinality Curvature Bound under Persistent Adversarial Noise

**Abstract.** How does persistent multiplicative oracle noise affect submodular maximization when curvature is known? In the sparse-cardinality regime k=⌊n^α⌋, 0<α<1/2, with εk→∞, a hidden-set construction gives an asymptotic lower bound matching noisy-singleton selection. For vanishing noise the limiting factor is 1−κ, rather than the exact-oracle benchmark 1−κ/e. This legacy note resolves that regime, not the original unrestricted problem.

[PDF](papers/curvature-noise/paper.pdf) · [ZIP](papers/curvature-noise/source.zip) · [Code](papers/curvature-noise/source/) · [Reproduce](papers/curvature-noise/README.md)

### Matching Advice on Degree-Two Bipartite Graphs: Exact Consistency–Robustness Frontiers

**Abstract.** What consistency–robustness tradeoff is possible for online bipartite matching with potentially wrong matching advice? For unweighted degree-two graphs, the exact frontier is min{3/4, 3/2−c}; on cycles it is min{7/8, 7/4−c}. An algorithm prioritizing previously exposed offline neighbors reaches the endpoints, and indistinguishable small inputs give matching upper bounds. The adversary is oblivious and advice may list absent edges.

[PDF](papers/advice-matching/paper.pdf) · [ZIP](papers/advice-matching/source.zip) · [Code](papers/advice-matching/source/) · [Reproduce](papers/advice-matching/README.md)

### A Size-Independent Discrepancy Bound for Sparse Coverage Functions

**Abstract.** Can sparse coverage functions be balanced with an error independent of the number of items? If each item belongs to at most t feature occurrences across the family, a deterministic polynomial-time partition into k≥2 classes achieves pairwise discrepancy at most 4kt(kt−1)². Hall witnesses balance large features, and multiple-choice Beck–Fiala rounding handles the remaining interactions. The result gives a polynomial bound depending only on t and k.

[PDF](papers/c002-coverage/paper.pdf) · [ZIP](papers/c002-coverage/source.zip) · [Code](papers/c002-coverage/source/) · [Reproduce](papers/c002-coverage/README.md)

### A Global Sidorenko Inequality for 2-Subdivided Alternating Cycles

**Abstract.** Do two-subdivided alternating cycles satisfy the local tournament Sidorenko property at every length? For Hℓ obtained from an alternating 2ℓ-cycle by subdividing every edge once, the manuscript proves tournament homomorphism density at least 2^(−4ℓ). A skew-symmetric matrix inequality yields the full family, a forcing estimate, and equality characterization. A three-vertex family shows the forcing exponent 4ℓ is optimal.

[PDF](papers/c009-cycle2/paper.pdf) · [ZIP](papers/c009-cycle2/source.zip) · [Code](papers/c009-cycle2/source/) · [Reproduce](papers/c009-cycle2/README.md)

### A Universal Partial Cycle with Three Wildcards per Window

**Abstract.** Does a nontrivial universal partial cycle exist with more than one wildcard per window? An explicit binary cycle of length 512 has length-12 windows containing exactly three wildcards. Its windows partition all 4096 binary 12-words into groups of eight completions. The entire cycle is encoded by 128 octal digits and checked by a short solver-free Python program, giving a finite existence proof.

[PDF](papers/c012-upcycles/paper.pdf) · [ZIP](papers/c012-upcycles/source.zip) · [Code](papers/c012-upcycles/source/) · [Reproduce](papers/c012-upcycles/README.md)

### Tight Mortality Bounds for Image-Bounded Nondeterministic Automata

**Abstract.** Is the known mortality upper bound for k-image-bounded nondeterministic automata tight? For every fixed k≥2, the manuscript proves that the maximum shortest mortal-word length is Θk(n^(k+1)). The lower bound holds for all sufficiently large n even over a binary alphabet with strongly connected automata. A queue-and-clocks construction supplies the delay, while a global image invariant preserves the restriction under every word.

[PDF](papers/c015-imagebound/paper.pdf) · [ZIP](papers/c015-imagebound/source.zip) · [Code](papers/c015-imagebound/source/) · [Reproduce](papers/c015-imagebound/README.md)

### Deciding Membership and Realizability for Wheeler Transducers

**Abstract.** Can one decide Wheeler membership when the number of output-monotonicity pieces is unspecified? The manuscript gives a polynomial-time algorithm for finite trimmed deterministic subsequential transducers, allowing partial transitions and erasing outputs; a conservative bit bound is O(S^13). Branching recurrence and simple cycles require different structural tests. Equivalent Wheeler realizability is also decidable and constructive, with no polynomial-time or minimality claim for that construction.

[PDF](papers/c017-wheeler/paper.pdf) · [ZIP](papers/c017-wheeler/source.zip) · [Code](papers/c017-wheeler/source/) · [Reproduce](papers/c017-wheeler/README.md)

### Uniform Pumping Does Not Characterize Copyless Cost Register Automata

**Abstract.** Does the uniform pumping condition characterize functions computed by copyless polynomial cost register automata? This manuscript proves that it does not, even among rational weighted-automaton functions: summing the positions of the 1s in a binary word satisfies the condition with one pumping exponent and one finitely generated subsemiring, but no finite-state copyless polynomial cost register automaton computes it. A minimum-image retraction and a polynomial spectral projection yield a commutation obstruction; return words remove finite control. This is the released nine-page separation, not the later extended revision.

[PDF](papers/c021-ccrapumping/paper.pdf) · [ZIP](papers/c021-ccrapumping/source.zip) · [Code](papers/c021-ccrapumping/source/) · [Reproduce](papers/c021-ccrapumping/README.md)

## Verified research notes: original questions still unresolved

Two additional dossiers document limitations of attempted proof methods. [The binary parity interface](notes/tp-parity-interface/) cannot combine the tested TP-graph colorings through one shared 72-entry table; the original three-coloring conjecture is not disproved. [The deletion-cycle lifting obstruction](notes/facet-cycle-lifting/) uses 200 maximal independent sets of P19 versus 189 base-cycle vertices to rule out a particular induction scheme; it is not a counterexample to facet-Hamiltonicity. Both include exact evidence and checking code.

## Reproduce and build

The portable mathematical checks require **Python 3.10+ and its standard library**. Rebuilding PDFs additionally requires a LaTeX distribution, `latexmk`, and Poppler (`pdftotext`); official unmodified acmart inputs are included. Scripts work on temporary copies so the archived sources remain intact.

Run these commands from the repository root. Use `--paper ID` instead of `--all` for one topic. Finite computations check only their documented ranges; the general mathematical arguments are in the manuscripts. TeX timestamps may change rebuilt PDF bytes.

```sh
git clone https://github.com/ArtificialZeng/Theoretical-Computer-Science.git
cd Theoretical-Computer-Science
python3 scripts/verify_artifacts.py
python3 scripts/reproduce.py --all
# Optional: rebuild every PDF
python3 scripts/build_pdfs.py --all
```

## Repository layout

`papers/ID/paper.pdf` is the released PDF; `source.zip` is the unchanged delivered source archive; `source/` exposes the same files for browsing. `catalog.json` records hashes and reproduction commands. `validation/` records the actual synchronization checks. Per-paper provenance retains citation limitations, including those of the ski-rental note.

## Authorship and assistance

Maintainer: **Zijian Zeng, UCSI University** · 1002266693@ucsiuniversity.edu.my. Research, code, proof development and manuscript preparation used substantial AI assistance, disclosed in the manuscripts. Existing third-party license notices are retained; see [RIGHTS.md](RIGHTS.md).

## Other conversation manuscripts

Eight folders stoc1–stoc8 are indexed: five existing manuscripts and three template-only folders. These scoped manuscripts retain their originality limitations and do not count as new accepted continuous-research resolutions.

[stoc1–stoc8](conversations/README.md)

### Representation and Preprocessing in Grammar-Constrained Decoding: Stack Indexes and Online Completion Lower Bounds

**Abstract.** Online grammar-constrained token completion with separate grammar, vocabulary, and stream parameters. The manuscript gives an OMv-based square-root single-stream barrier and a stronger independently initialized multi-stream barrier, plus regular-stack indexes with explicit exponential compilation and charged parser work. General LR(1) worst-case acceleration and STOC-level novelty remain unestablished.

[PDF](conversations/stoc1/paper.pdf) · [ZIP](conversations/stoc1/source.zip) · [Code](conversations/stoc1/source/) · [Reproduce](conversations/stoc1/README.md)

### Syntax Repair in Near-Linear Time: Exact Bounds for Marked-Palindrome Grammars

**Abstract.** Exact language edit distance for fixed marked-palindrome grammars: a theoretical O(n+k²) threshold algorithm with witness recovery, a guarded SETH lower bound, and enumeration results. The supplied indexed implementation uses O(n log²(n+2)+(k+1)²) time. The general LR(1) problem remains unresolved; the current PDF is anonymous and two-column and needs STOC review-format correction.

[PDF](conversations/stoc2/paper.pdf) · [ZIP](conversations/stoc2/source.zip) · [Code](conversations/stoc2/source/) · [Reproduce](conversations/stoc2/README.md)

### Is Quadratic Subtyping Optimal? Conditional Hardness on Shared Acyclic Type Graphs

**Abstract.** Transfers known OV-based automata-intersection hardness to structural subtyping on shared acyclic type graphs: a conditional quadratic barrier even for three fixed record fields or arrow-only types. Equality is almost linear; quotient-size and finite-access upper bounds explain tractable representations. The main novelty question is whether this semantic transfer is substantial beyond the known automata reduction. The current full PDF has 18 pages.

[PDF](conversations/stoc3/paper.pdf) · [ZIP](conversations/stoc3/source.zip) · [Code](conversations/stoc3/source/) · [Reproduce](conversations/stoc3/README.md)

### Fully Dynamic Interprocedural Dataflow Analysis: OMv Barriers and Summary-Local TreeFlow Updates

**Abstract.** Fully dynamic interprocedural dataflow with explicit global dependency costs. OMv barriers persist even for path-shaped procedures and shallow acyclic calls. A relation-circuit algorithm gives bounds parameterized by affected gates and ancestor call-target incidence, using fixed decompositions and acyclic candidate calls. The broader original characterization and production integrations remain unresolved; novelty relative to earlier RSM update machinery needs expert assessment.

[PDF](conversations/stoc4/paper.pdf) · [ZIP](conversations/stoc4/source.zip) · [Code](conversations/stoc4/source/) · [Reproduce](conversations/stoc4/README.md)

### Octagons Are APSP-Complete: Fine-Grained Complexity of Weakly Relational Abstract Domains

**Abstract.** Classifies octagon and zone operations through exponent-preserving reductions to APSP, an incremental min-plus update/query tradeoff, feasibility, and width-sensitive reconstruction. October 2026 APSP bounds are imported reported results rather than a new shortest-path algorithm. A pinned ELINA scalar-kernel replay accompanies the proof-oriented artifact. Independent novelty assessment and whole-analyzer studies remain outstanding. The current PDF has 19 pages.

[PDF](conversations/stoc5/paper.pdf) · [ZIP](conversations/stoc5/source.zip) · [Code](conversations/stoc5/source/) · [Reproduce](conversations/stoc5/README.md)

## Comparative ranking

The comparative ranking below covers the earlier fifteen-manuscript snapshot. The newly added CCRA v1 package has not been ranked in that assessment; its extended revision is still awaiting final release review.

[中文：按 STOC 相对竞争力和新增解决问题大小排序](RANKING.zh-CN.md) · [English assessment](RANKING.md) · [Data](ranking.json)

```sh
python3 scripts/check_conversations.py --all
```
