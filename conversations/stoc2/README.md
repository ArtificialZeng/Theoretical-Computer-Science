# Syntax Repair in Near-Linear Time: Exact Bounds for Marked-Palindrome Grammars

[PDF](paper.pdf) · [Original source ZIP](source.zip) · [Browse source](source/) · [Status and review records](provenance/) · [All conversations](../README.md)

## Abstract

Exact language edit distance for fixed marked-palindrome grammars: a theoretical O(n+k²) threshold algorithm with witness recovery, a guarded SETH lower bound, and enumeration results. The supplied indexed implementation uses O(n log²(n+2)+(k+1)²) time. The general LR(1) problem remains unresolved; the current PDF is anonymous and two-column and needs STOC review-format correction.

## 中文摘要

研究固定带标记回文文法的精确语言编辑距离，给出理论 O(n+k²) 阈值算法、修复见证、带守卫的 SETH 下界和枚举结果。所附索引实现为 O(n log²(n+2)+(k+1)²)。一般 LR(1) 原题仍未解决；当前 PDF 为匿名双栏，投稿前还需修正版式。

## Scope and reproduction

This is the existing stoc2 manuscript, preserved byte-for-byte with its author list. It is not a newly accepted resolution under the continuous-research gate. Current source-status and originality limitations remain visible in `provenance/`. No conference acceptance or external peer review is implied.

From the repository root:

```sh
python3 scripts/check_conversations.py --paper stoc2
```

The script verifies the original PDF/ZIP hashes and every expanded source byte, runs the documented finite checks, and clean-builds the paper on disposable copies. Requirements: Python 3.10+, a TeX distribution with latexmk and Poppler; Python standard library only for the mathematical checks. It does not rerun all external corpus or whole-analyzer experiments. Original package instructions are in `source/`.

The general targets of grammar decoding, LR(1) repair and unrestricted interprocedural dataflow were not fully solved by these scoped manuscripts. Known automata hardness and imported APSP/SSSP algorithms retain their attribution. See the [comparative assessment](../../RANKING.zh-CN.md).
