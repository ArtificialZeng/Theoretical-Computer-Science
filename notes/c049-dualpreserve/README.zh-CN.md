# 未解决研究记录：双故障成对可达性

[en](README.md) · [zh](README.zh-CN.md) · [de](README.de.md) · [fr](README.fr.md) · [ja](README.ja.md)

**UNRESOLVED — RESEARCH RECORDS, NO PAPER/PDF**

四轮有界研究（含用户明确追加的一轮）后，原问题仍未解决。本目录仅保存 Markdown 论证、有限精确检查和源代码，不是论文、原题的完整证明或反例，也不是 submission_ready 成果。

目标是在多项式时间内构造大小为 O-tilde(n+n sqrt(p)) 的原图边子图，在任意至多两次混合顶点／边故障后同时保留 p 个指定有向点对的可达性。已核查原始文献中的上界仍为 O(n^(4/3) p^(1/3))，下界为 Omega(n sqrt(p))。

若干更强的中间引理已被反例推翻。抽样返回边归约及三条边不交路径的覆盖论证能处理部分必需边，剩余全局边数界仍未证明。下面的密度界只是一个充分条件，尚未证明它对原问题也是必要条件。

- [Frozen original / 原始完整问题](source/ORIGINAL_PROBLEM.md)
- [Pass 1: flow/cut coverage and its limits](source/proofs/research-67929c1f9552-math.md)
- [Pass 2: the high-beta core counterexample](source/proofs/research-c6b2b0ea3f71-math.md)
- [Pass 3: orientation energy and the remaining gap](source/proofs/research-2396269cbd5d-math.md)
- [Code](source/code/) · [Original finite results](source/results/) · [Provenance](source/manifest.json)

Remaining sufficient inequality (unproved): for every edge-critical (G,P) and nonempty U,

`|E(G[U])|^2 <= C n(p+1)|U| log(n+2)^c`.

Here n counts the entire original graph, including all selector vertices.

Run all declared finite checks on disposable copies with Python 3.10+ (standard library only):

```sh
python3 -B source/reproduce.py
```

These finite checks do not prove an asymptotic bound. The directory excludes raw model transcripts, credentials and third-party full-text caches. Its mathematical arguments have not passed a fresh acceptance review. Substantial research and code assistance used OpenAI Codex; internal model checks are not external peer review.

Researcher: Zijian Zeng, UCSI University, 1002266693@ucsiuniversity.edu.my. 现按未解决研究记录归档于本仓库。不可变源码包保留原始打包元数据，当前公开状态以本页为准。


第四轮对指定的完全共享选择器图族给出了至多 8t+p 条边的稀疏构造，并刻画了其中的必需核心边。原题及全局密度界仍未解决。

[Fourth-pass proof and exact finite coverage](source/proofs/research-960416a85f25-math.md). Earlier pass notes preserve their historical budgets and decisions. Reproduction additionally requires a C++17 compiler (`c++`, `clang++` or `g++`). Only original source files are included; compiled binaries and third-party text caches are excluded.

复现适配器仅在临时副本中移除一条已过期的研究截止时间断言；保留全部数学断言与有限实例范围。原始脚本和首次失败包均予以保留，这不构成新的研究轮次。

[Unified index](../../README.md) · [Source ZIP](source.zip) · [Reproduction](REPRODUCE.md)
