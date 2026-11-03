# 未解決の研究記録：二故障下の指定点対到達可能性

[en](README.md) · [zh](README.zh-CN.md) · [de](README.de.md) · [fr](README.fr.md) · [ja](README.ja.md)

**UNRESOLVED — RESEARCH RECORDS, NO PAPER/PDF**

ユーザーが明示的に追加した一回を含む四回の時間制限付き研究後も、元の問題は未解決である。本ディレクトリは Markdown の議論、有限の厳密検査、ソースコードを保存する。論文でも、元の問題の完全な証明・反例でも、submission_ready の成果でもない。

目標は、任意の二個以下の頂点・辺の混合故障後も、指定された p 個の有向点対の到達可能性を同時に保つ、O-tilde(n+n sqrt(p)) 辺の原図部分グラフを多項式時間で構成することである。確認した一次資料では、上界 O(n^(4/3) p^(1/3)) と下界 Omega(n sqrt(p)) の隔たりが残る。

いくつかの強い補助命題には反例がある。戻り辺を標本化する帰着と三本の辺素な経路の被覆により一部の必須辺を扱えるが、全体の辺数上界は未証明である。以下の密度不等式は十分条件であり、元の問題に対する必要性は証明されていない。

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

Researcher: Zijian Zeng, UCSI University, 1002266693@ucsiuniversity.edu.my. 未解決の研究記録として本リポジトリに保存する。変更しないソースアーカイブには作成時のメタデータが残り、現在の公開状態は本ページに記す。


第四回では、完全共有セレクターの特定の族について高々 8t+p 辺の構成を証明し、その必須な中心辺を特徴付けた。一般の元問題と全体の密度上界は未解決のままである。

[Fourth-pass proof and exact finite coverage](source/proofs/research-960416a85f25-math.md). Earlier pass notes preserve their historical budgets and decisions. Reproduction additionally requires a C++17 compiler (`c++`, `clang++` or `g++`). Only original source files are included; compiled binaries and third-party text caches are excluded.

再現用の一時コピーでのみ、期限切れの絶対研究締切を確認する一つのアサーションを除く。数学的検査と有限の対象範囲はすべて保持する。元のソースと最初の失敗パッケージを保存し、新たな研究回には数えない。

[Unified index](../../README.md) · [Source ZIP](source.zip) · [Reproduction](REPRODUCE.md)
