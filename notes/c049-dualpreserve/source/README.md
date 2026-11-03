# Unresolved research records: dual-fault pairwise reachability

[en](README.md) · [zh](README.zh-CN.md) · [de](README.de.md) · [fr](README.fr.md) · [ja](README.ja.md)

**UNRESOLVED — RESEARCH RECORDS, NO PAPER/PDF**

The original problem remains unresolved after four bounded research passes, including the single additional pass explicitly authorized by the user. This folder contains Markdown arguments, exact finite checks and source code. It is not a manuscript, a full proof, a counterexample to the original problem, or a submission-ready result.

The target is a polynomial algorithm producing an actual input-edge subgraph of size O-tilde(n+n sqrt(p)) that preserves all p directed demand pairs simultaneously under every set of at most two mixed vertex/edge failures. The inspected primary bounds remain O(n^(4/3) p^(1/3)) above and Omega(n sqrt(p)) below.

Several stronger proposed proof lemmas fail. A sampled-return-edge reduction and a direct cover for demands with three edge-disjoint paths handle some critical edges, but the remaining global edge count is unproved. The final sufficient density inequality is stated below; it has not been established as necessary for the original problem.

- [Frozen original / 原始完整问题](ORIGINAL_PROBLEM.md)
- [Pass 1: flow/cut coverage and its limits](proofs/research-67929c1f9552-math.md)
- [Pass 2: the high-beta core counterexample](proofs/research-c6b2b0ea3f71-math.md)
- [Pass 3: orientation energy and the remaining gap](proofs/research-2396269cbd5d-math.md)
- [Code](code/) · [Original finite results](results/) · [Provenance](manifest.json)

Remaining sufficient inequality (unproved): for every edge-critical (G,P) and nonempty U,

`|E(G[U])|^2 <= C n(p+1)|U| log(n+2)^c`.

Here n counts the entire original graph, including all selector vertices.

Run all declared finite checks on disposable copies with Python 3.10+ (standard library only):

```sh
python3 -B reproduce.py
```

These finite checks do not prove an asymptotic bound. The directory excludes raw model transcripts, credentials and third-party full-text caches. Its mathematical arguments have not passed a fresh acceptance review. Substantial research and code assistance used OpenAI Codex; internal model checks are not external peer review.

Researcher: Zijian Zeng, UCSI University, 1002266693@ucsiuniversity.edu.my. Local preparation only; publication requires the user's revised finalization decision.


The fourth pass proves an at-most-8t+p-edge certificate for a specified fully shared selector family and classifies its critical core edges. The full original and global density inequality remain unresolved.

[Fourth-pass proof and exact finite coverage](proofs/research-960416a85f25-math.md). Earlier pass notes preserve their historical budgets and decisions. Reproduction additionally requires a C++17 compiler (`c++`, `clang++` or `g++`). Only original source files are included; compiled binaries and third-party text caches are excluded.

In the disposable reproduction copy, one expired absolute research-deadline assertion is omitted. All mathematical assertions and finite case ranges are retained. The original source and first failed package are preserved; this is a portability adapter, not a new research run.
