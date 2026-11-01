# Fully Dynamic Interprocedural Dataflow Analysis: OMv Barriers and Summary-Local TreeFlow Updates

[PDF](paper.pdf) · [Original source ZIP](source.zip) · [Browse source](source/) · [Status and review records](provenance/) · [All conversations](../README.md)

## Abstract

Fully dynamic interprocedural dataflow with explicit global dependency costs. OMv barriers persist even for path-shaped procedures and shallow acyclic calls. A relation-circuit algorithm gives bounds parameterized by affected gates and ancestor call-target incidence, using fixed decompositions and acyclic candidate calls. The broader original characterization and production integrations remain unresolved; novelty relative to earlier RSM update machinery needs expert assessment.

## 中文摘要

研究全动态过程间数据流，并显式计入全局摘要依赖传播。即使各过程是路径、调用图无环且很浅，仍存在 OMv 屏障；关系电路算法用受影响门数和祖先调用关联量给出上界，但依赖固定分解及无环候选调用。更广泛原始刻画和真实分析器集成尚未完成，与已有 RSM 更新机制的增量需要专家复核。

## Scope and reproduction

This is the existing stoc4 manuscript, preserved byte-for-byte with its author list. It is not a newly accepted resolution under the continuous-research gate. Current source-status and originality limitations remain visible in `provenance/`. No conference acceptance or external peer review is implied.

From the repository root:

```sh
python3 scripts/check_conversations.py --paper stoc4
```

The script verifies the original PDF/ZIP hashes and every expanded source byte, runs the documented finite checks, and clean-builds the paper on disposable copies. Requirements: Python 3.10+, a TeX distribution with latexmk and Poppler; Python standard library only for the mathematical checks. It does not rerun all external corpus or whole-analyzer experiments. Original package instructions are in `source/`.

The general targets of grammar decoding, LR(1) repair and unrestricted interprocedural dataflow were not fully solved by these scoped manuscripts. Known automata hardness and imported APSP/SSSP algorithms retain their attribution. See the [comparative assessment](../../RANKING.zh-CN.md).
