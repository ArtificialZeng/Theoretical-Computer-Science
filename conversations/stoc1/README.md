# Representation and Preprocessing in Grammar-Constrained Decoding: Stack Indexes and Online Completion Lower Bounds

[PDF](paper.pdf) · [Original source ZIP](source.zip) · [Browse source](source/) · [Status and review records](provenance/) · [All conversations](../README.md)

## Abstract

Online grammar-constrained token completion with separate grammar, vocabulary, and stream parameters. The manuscript gives an OMv-based square-root single-stream barrier and a stronger independently initialized multi-stream barrier, plus regular-stack indexes with explicit exponential compilation and charged parser work. General LR(1) worst-case acceleration and STOC-level novelty remain unestablished.

## 中文摘要

研究语法约束解码中的在线 token 可完成性，并分开计算文法、词表和流长度。稿件给出基于 OMv 的单流平方根屏障与独立多流屏障，以及显式计入指数编译成本和解析提交工作的栈索引。一般 LR(1) 最坏情况加速与 STOC 级独立创新仍未建立。

## Scope and reproduction

This is the existing stoc1 manuscript, preserved byte-for-byte with its author list. It is not a newly accepted resolution under the continuous-research gate. Current source-status and originality limitations remain visible in `provenance/`. No conference acceptance or external peer review is implied.

From the repository root:

```sh
python3 scripts/check_conversations.py --paper stoc1
```

The script verifies the original PDF/ZIP hashes and every expanded source byte, runs the documented finite checks, and clean-builds the paper on disposable copies. Requirements: Python 3.10+, a TeX distribution with latexmk and Poppler; Rust. It does not rerun all external corpus or whole-analyzer experiments. Original package instructions are in `source/`.

The general targets of grammar decoding, LR(1) repair and unrestricted interprocedural dataflow were not fully solved by these scoped manuscripts. Known automata hardness and imported APSP/SSSP algorithms retain their attribution. See the [comparative assessment](../../RANKING.zh-CN.md).

## Synchronization validation limitation

The PDF clean-build passed. Executable mathematical checks were **not rerun** because `rustc` was unavailable; both check scripts import the Rust-backed library. The exit-127 dependency record is retained. Install Rust to run the documented full command. Existing archived results are preserved without representing them as newly verified here.
