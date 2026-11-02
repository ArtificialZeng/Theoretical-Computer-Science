# Octagons Are APSP-Complete: Fine-Grained Complexity of Weakly Relational Abstract Domains

[PDF](paper.pdf) · [Original source ZIP](source.zip) · [Browse source](source/) · [Status and review records](provenance/) · [All conversations](../README.md)

## Abstract

Classifies octagon and zone operations through exponent-preserving reductions to APSP, an incremental min-plus update/query tradeoff, feasibility, and width-sensitive reconstruction. October 2026 APSP bounds are imported reported results rather than a new shortest-path algorithm. A pinned ELINA scalar-kernel replay accompanies the proof-oriented artifact. Independent novelty assessment and whole-analyzer studies remain outstanding. The current PDF has 19 pages.

## 中文摘要

通过保持指数的 APSP 归约，研究 octagon/zone 闭包、增量 min-plus 更新查询权衡、可行性和按宽度重建的复杂度。2026 年 10 月 APSP 界是引用的已有报告结果，本文没有新最短路算法；附带固定版本 ELINA 标量内核复现。独立新颖性评估与完整分析器实验仍待完成。当前 PDF 为 19 页。

## Scope and reproduction

This is the existing stoc5 manuscript, preserved byte-for-byte with its author list. It is not a newly accepted resolution under the continuous-research gate. Current source-status and originality limitations remain visible in `provenance/`. No conference acceptance or external peer review is implied.

From the repository root:

```sh
python3 scripts/check_conversations.py --paper stoc5
```

The script verifies the original PDF/ZIP hashes and every expanded source byte, runs the documented finite checks, and clean-builds the paper on disposable copies. Requirements: Python 3.10+, a TeX distribution with latexmk and Poppler; a C compiler, GMP and MPFR development headers. It does not rerun all external corpus or whole-analyzer experiments. Original package instructions are in `source/`.

The general targets of grammar decoding, LR(1) repair and unrestricted interprocedural dataflow were not fully solved by these scoped manuscripts. Known automata hardness and imported APSP/SSSP algorithms retain their attribution. See the [comparative assessment](../../RANKING.zh-CN.md).
