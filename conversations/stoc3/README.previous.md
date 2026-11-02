# Is Quadratic Subtyping Optimal? Conditional Hardness on Shared Acyclic Type Graphs

[PDF](paper.pdf) · [Original source ZIP](source.zip) · [Browse source](source/) · [Status and review records](provenance/) · [All conversations](../README.md)

## Abstract

Transfers known OV-based automata-intersection hardness to structural subtyping on shared acyclic type graphs: a conditional quadratic barrier even for three fixed record fields or arrow-only types. Equality is almost linear; quotient-size and finite-access upper bounds explain tractable representations. The main novelty question is whether this semantic transfer is substantial beyond the known automata reduction. The current full PDF has 18 pages.

## 中文摘要

把已有基于 OV 的自动机交非空困难性转移到共享无环类型图上的结构子类型判定：即使只有三个固定 record 字段或仅使用函数箭头，也有条件二次下界；等价判定近线性，并给出商图规模与有限访问参数上界。主要风险是语义转移相对已有自动机归约的独立增量。当前完整 PDF 为 18 页。

## Scope and reproduction

This is the existing stoc3 manuscript, preserved byte-for-byte with its author list. It is not a newly accepted resolution under the continuous-research gate. Current source-status and originality limitations remain visible in `provenance/`. No conference acceptance or external peer review is implied.

From the repository root:

```sh
python3 scripts/check_conversations.py --paper stoc3
```

The script verifies the original PDF/ZIP hashes and every expanded source byte, runs the documented finite checks, and clean-builds the paper on disposable copies. Requirements: Python 3.10+, a TeX distribution with latexmk and Poppler; Node.js/npm (npm ci installs the pinned TypeScript dependency). It does not rerun all external corpus or whole-analyzer experiments. Original package instructions are in `source/`.

The general targets of grammar decoding, LR(1) repair and unrestricted interprocedural dataflow were not fully solved by these scoped manuscripts. Known automata hardness and imported APSP/SSSP algorithms retain their attribution. See the [comparative assessment](../../RANKING.zh-CN.md).
