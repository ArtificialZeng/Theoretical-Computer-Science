# Theoretical Computer Science

[English](README.md) · [中文](README.zh-CN.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [日本語](README.ja.md)

理論計算機科学の研究稿、再現可能なコード、厳密な証明書をまとめたリポジトリ。本リポジトリには、この継続研究の十一編と他の会話の五編、計 **16 セットの論文資料**を収録する。他に三つの会話フォルダーはテンプレートのみである。各課題について、概要、PDF、変更していないソースアーカイブ、閲覧可能なコードを用意している。

**結果の範囲に注意：**本研究系列の十一編のうち、研究記録上は八編が明示した研究目標の完全な解答に位置付けられている。初期の三編は部分結果であり、元のより一般的な問いは未解決である。これらはローカルの研究・公開確認記録で、外部査読や STOC 採択を意味しない。元の著者一覧を維持し、後の六編は Zijian Zeng の単著である。

## 論文原稿一覧

| 課題 | ページ数 | 結果の範囲 | ファイル |
|---|---:|---|---|
| `coverage-sparse` | 8 | 明示した目標の完全解答 | [PDF](papers/coverage-sparse/paper.pdf) · [ZIP](papers/coverage-sparse/source.zip) · [Code](papers/coverage-sparse/source/) · [Reproduce](papers/coverage-sparse/README.md) |
| `privacy-interpolation` | 7 | 初期の部分結果 | [PDF](papers/privacy-interpolation/paper.pdf) · [ZIP](papers/privacy-interpolation/source.zip) · [Code](papers/privacy-interpolation/source/) · [Reproduce](papers/privacy-interpolation/README.md) |
| `robust-stopping` | 11 | 初期の部分結果 | [PDF](papers/robust-stopping/paper.pdf) · [ZIP](papers/robust-stopping/source.zip) · [Code](papers/robust-stopping/source/) · [Reproduce](papers/robust-stopping/README.md) |
| `curvature-noise` | 6 | 初期の部分結果 | [PDF](papers/curvature-noise/paper.pdf) · [ZIP](papers/curvature-noise/source.zip) · [Code](papers/curvature-noise/source/) · [Reproduce](papers/curvature-noise/README.md) |
| `advice-matching` | 6 | 明示した目標の完全解答 | [PDF](papers/advice-matching/paper.pdf) · [ZIP](papers/advice-matching/source.zip) · [Code](papers/advice-matching/source/) · [Reproduce](papers/advice-matching/README.md) |
| `c002-coverage` | 7 | 明示した目標の完全解答 | [PDF](papers/c002-coverage/paper.pdf) · [ZIP](papers/c002-coverage/source.zip) · [Code](papers/c002-coverage/source/) · [Reproduce](papers/c002-coverage/README.md) |
| `c009-cycle2` | 6 | 明示した目標の完全解答 | [PDF](papers/c009-cycle2/paper.pdf) · [ZIP](papers/c009-cycle2/source.zip) · [Code](papers/c009-cycle2/source/) · [Reproduce](papers/c009-cycle2/README.md) |
| `c012-upcycles` | 5 | 明示した目標の完全解答 | [PDF](papers/c012-upcycles/paper.pdf) · [ZIP](papers/c012-upcycles/source.zip) · [Code](papers/c012-upcycles/source/) · [Reproduce](papers/c012-upcycles/README.md) |
| `c015-imagebound` | 6 | 明示した目標の完全解答 | [PDF](papers/c015-imagebound/paper.pdf) · [ZIP](papers/c015-imagebound/source.zip) · [Code](papers/c015-imagebound/source/) · [Reproduce](papers/c015-imagebound/README.md) |
| `c017-wheeler` | 10 | 明示した目標の完全解答 | [PDF](papers/c017-wheeler/paper.pdf) · [ZIP](papers/c017-wheeler/source.zip) · [Code](papers/c017-wheeler/source/) · [Reproduce](papers/c017-wheeler/README.md) |
| `c021-ccrapumping` | 9 | 明示した目標の完全解答 | [PDF](papers/c021-ccrapumping/paper.pdf) · [ZIP](papers/c021-ccrapumping/source.zip) · [Code](papers/c021-ccrapumping/source/) · [Reproduce](papers/c021-ccrapumping/README.md) |

## 各課題の研究内容

### Coverage Correlation Gaps under Graph-Constrained Pairwise Independence

**概要.** 指定した頂点対だけに独立性を課したとき、被覆関数の最適期待値がどこまで低下するかを研究する。k 彩色可能グラフ族と最大次数 k−1 以下のグラフ族について、最悪比率の上限を 1/[1−(1−1/k)^k] と厳密に求める。互いに素なクリークが極限例となり、衝突不等式から有限サイズと誤差の評価も得る。各固定グラフでの等号を主張する結果ではない。

[PDF](papers/coverage-sparse/paper.pdf) · [ZIP](papers/coverage-sparse/source.zip) · [Code](papers/coverage-sparse/source/) · [Reproduce](papers/coverage-sparse/README.md)

### Mandatory Excursions in Privacy-Constrained Probability Paths

**概要.** プライバシー制約の下で、確率の変化を端点の値の間に保てるかを調べる。二つの座標を入れ替える三点分布について、最適予算と、端点値が変わらない座標の不可避な最小ピークを求める。単調性などを要求した場合の追加費用と一般端点の証明書も示す。初期の部分結果稿であり、元の一般問題は未解決である。

[PDF](papers/privacy-interpolation/paper.pdf) · [ZIP](papers/privacy-interpolation/source.zip) · [Code](papers/privacy-interpolation/source/) · [Reproduce](papers/privacy-interpolation/README.md)

### Certified Expected-Cost Optimization for Robust Ski Rental

**概要.** 有限の有理数予測を使いながら、すべての実際の期間で期待競争比の制約を守るスキーレンタル戦略を研究する。購入日と期間を無界に扱う厳密な期待費用最適化、主・双対証明書、購入日数 b+1 以下の支持上界、均一予測の明示的な最適境界を示す。計算時間は b の数値と入力ビット長の多項式である。元のより広い問題は未解決である。

[PDF](papers/robust-stopping/paper.pdf) · [ZIP](papers/robust-stopping/source.zip) · [Code](papers/robust-stopping/source/) · [Reproduce](papers/robust-stopping/README.md)

### A Sparse-Cardinality Curvature Bound under Persistent Adversarial Noise

**概要.** 既知の曲率を持つ単調劣モジュラ関数の最大化に、持続的な乗法ノイズが与える影響を調べる。k=⌊n^α⌋、0<α<1/2、εk→∞ の範囲で、隠れ集合による下界がノイズ付き単要素値による選択法と漸近的に一致する。ノイズが消える場合の極限因子は 1−κ となる。この初期稿が解くのは当該範囲であり、元の無制限の問題ではない。

[PDF](papers/curvature-noise/paper.pdf) · [ZIP](papers/curvature-noise/source.zip) · [Code](papers/curvature-noise/source/) · [Reproduce](papers/curvature-noise/README.md)

### Matching Advice on Degree-Two Bipartite Graphs: Exact Consistency–Robustness Frontiers

**概要.** 誤りを含み得る助言を利用したオンライン二部マッチングの、一貫性と頑健性の最適なトレードオフを求める。重みなし最大次数二のグラフでの最適境界は min{3/4, 3/2−c}、サイクルでは min{7/8, 7/4−c} となる。既に露出したオフライン隣接点を優先する方式と、小さな識別不能入力による上界が一致する。敵対者は非適応的で、助言には存在しない辺も許す。

[PDF](papers/advice-matching/paper.pdf) · [ZIP](papers/advice-matching/source.zip) · [Code](papers/advice-matching/source/) · [Reproduce](papers/advice-matching/README.md)

### A Size-Independent Discrepancy Bound for Sparse Coverage Functions

**概要.** 物品数に依存しない誤差で、疎な被覆関数を均等に分割できるかを研究する。各物品が関数族全体で高々 t 個の特徴に現れる場合、k≥2 クラスへの決定的多項式時間分割で、任意の二クラス間の差異を 4kt(kt−1)² 以下にできる。大きな特徴は Hall の定理による証人で平衡化し、残りを多肢選択 Beck–Fiala 丸めで処理する。

[PDF](papers/c002-coverage/paper.pdf) · [ZIP](papers/c002-coverage/source.zip) · [Code](papers/c002-coverage/source/) · [Reproduce](papers/c002-coverage/README.md)

### A Global Sidorenko Inequality for 2-Subdivided Alternating Cycles

**概要.** 交互向きの有向サイクルの各辺を一度細分したグラフが、すべての長さで局所トーナメント Sidorenko 性質を満たすかを調べる。長さ 2ℓ の交互サイクルから得る Hℓ の準同型密度を 2^(−4ℓ) 以上と証明する。反対称行列の不等式により、定量的な強制性評価と等号条件も導く。三頂点の例族は指数 4ℓ の最適性を示す。

[PDF](papers/c009-cycle2/paper.pdf) · [ZIP](papers/c009-cycle2/source.zip) · [Code](papers/c009-cycle2/source/) · [Reproduce](papers/c009-cycle2/README.md)

### A Universal Partial Cycle with Three Wildcards per Window

**概要.** 各窓に複数のワイルドカードを含む、非自明な普遍部分サイクルの存在を示す。明示的な長さ512の二進サイクルでは、長さ12の各窓にワイルドカードが三つある。各窓の八通りの補完が、長さ12の全4096個の二進語を重複なく分割する。サイクル全体は128桁の八進数で表し、ソルバー不要の短い Python プログラムで完全検証できる。

[PDF](papers/c012-upcycles/paper.pdf) · [ZIP](papers/c012-upcycles/source.zip) · [Code](papers/c012-upcycles/source/) · [Reproduce](papers/c012-upcycles/README.md)

### Tight Mortality Bounds for Image-Bounded Nondeterministic Automata

**概要.** k-image-bounded 非決定性有限オートマトンの死亡語長の既知上界が最適であることを示す。固定した任意の k≥2 について、最短死亡語長の最大値は Θk(n^(k+1)) となる。十分大きいすべての n に対し、二文字アルファベットと強連結性を要求しても下界が成立する。待ち行列と巡回時計による構成が遅延を生み、全入力語に対する像集合の制限を保つ。

[PDF](papers/c015-imagebound/paper.pdf) · [ZIP](papers/c015-imagebound/source.zip) · [Code](papers/c015-imagebound/source/) · [Reproduce](papers/c015-imagebound/README.md)

### Deciding Membership and Realizability for Wheeler Transducers

**概要.** 出力の単調区間数が未指定でも Wheeler 性を判定できるかを研究する。部分遷移と空出力を許す有限の trim な決定性 subsequential 変換器に対して、多項式時間の判定法を与え、保守的なビット計算量上界は O(S^13) となる。分岐を持つ強連結成分と単純サイクルを別々に扱う。等価な Wheeler 実現も判定・構成できるが、その構成の多項式時間性や最小性は主張しない。

[PDF](papers/c017-wheeler/paper.pdf) · [ZIP](papers/c017-wheeler/source.zip) · [Code](papers/c017-wheeler/source/) · [Reproduce](papers/c017-wheeler/README.md)

### Uniform Pumping Does Not Characterize Copyless Cost Register Automata

**概要.** 一様ポンピング条件は、copyless な多項式コストレジスタオートマトンが計算する関数を特徴付けるか。本稿は、有理数重み付きオートマトンで認識できる関数に限っても否定する。二進語中の 1 の位置の総和は、単一の指数と有限生成部分半環で条件を満たすが、有限状態の copyless 多項式コストレジスタオートマトンでは計算できない。最小像へのレトラクションと多項式スペクトル射影から可換性の障害を導き、帰還語で有限制御を扱う。収録するのは公開確認済みの九ページ版であり、その後の拡張版は含まない。

[PDF](papers/c021-ccrapumping/paper.pdf) · [ZIP](papers/c021-ccrapumping/source.zip) · [Code](papers/c021-ccrapumping/source/) · [Reproduce](papers/c021-ccrapumping/README.md)

## 検証済み研究ノート：元の問いは未解決

二つの追加資料は、特定の証明方法の限界を示す。[二進パリティ・インターフェース](notes/tp-parity-interface/)では、共有72項目表によって対象の TP 彩色を合成できないが、元の三彩色予想を否定したわけではない。[頂点削除に沿うサイクル持ち上げの障害](notes/facet-cycle-lifting/)は、P19 の200個の極大独立集合と基礎サイクルの189頂点を比較し、ある帰納法を排除する。両資料に厳密なデータと検証コードがある。

## 再現とビルド

可搬な数学的チェックに必要なのは **Python 3.10 以降の標準ライブラリ**のみ。PDF の再ビルドには LaTeX、`latexmk`、Poppler（`pdftotext`） も必要で、未変更の公式 acmart ファイルを同梱している。スクリプトは一時コピーで動作し、アーカイブを変更しない。

以下はリポジトリのルートで実行する。個別の課題には `--all` の代わりに `--paper ID` を指定する。有限計算が検証するのは明記された範囲だけであり、一般的な証明は本文を参照。TeX の時刻情報により再ビルドした PDF のバイト列が変わることがある。

```sh
git clone https://github.com/ArtificialZeng/Theoretical-Computer-Science.git
cd Theoretical-Computer-Science
python3 scripts/verify_artifacts.py
python3 scripts/reproduce.py --all
# Optional: rebuild every PDF
python3 scripts/build_pdfs.py --all
```

## ディレクトリ構成

`papers/ID/paper.pdf` は公開 PDF、`source.zip` は元の未変更ソース、`source/` は同じ内容を閲覧するための展開版。`catalog.json` はハッシュと再現コマンド、`validation/` は実際の確認結果を記録する。出典確認の範囲とアクセス制限は各 provenance に保存されている。

## 著者と研究支援

管理者：**Zijian Zeng, UCSI University** · 1002266693@ucsiuniversity.edu.my。研究、コード、証明の検討、執筆には実質的な AI 支援を利用しており、論文原稿で開示している。同梱ファイルの既存ライセンス表示は維持する。[RIGHTS.md](RIGHTS.md) を参照。

## 他の会話の論文原稿

stoc1–stoc8 の全八フォルダーを整理した。既存の論文原稿は五編で、三フォルダーはテンプレートのみである。各原稿の独創性と結果の範囲に関する制限を保持し、継続研究で新たに承認された完全解答とは扱わない。

[stoc1–stoc8](conversations/README.md)

### Representation and Preprocessing in Grammar-Constrained Decoding: Stack Indexes and Online Completion Lower Bounds

**概要.** 文法制約付きデコードにおけるオンラインのトークン補完可能性を、文法・語彙・入力長を分けて調べる。OMv に基づく単一ストリームと複数ストリームの下界、および指数的な事前計算と解析処理を明示したスタック索引を示す。一般の LR(1) に対する高速化と STOC 水準の独創性は未確立である。

[PDF](conversations/stoc1/paper.pdf) · [ZIP](conversations/stoc1/source.zip) · [Code](conversations/stoc1/source/) · [Reproduce](conversations/stoc1/README.md)

### Syntax Repair in Near-Linear Time: Exact Bounds for Marked-Palindrome Grammars

**概要.** 固定された区切り付き回文文法への厳密な編集距離を扱う。理論上 O(n+k²) の閾値アルゴリズム、修復例、ガード付き SETH 下界と列挙法を示す。実装の計算量は O(n log²(n+2)+(k+1)²)。一般の LR(1) 問題は未解決であり、現在の匿名二段組 PDF は投稿形式の修正が必要である。

[PDF](conversations/stoc2/paper.pdf) · [ZIP](conversations/stoc2/source.zip) · [Code](conversations/stoc2/source/) · [Reproduce](conversations/stoc2/README.md)

### Is Quadratic Subtyping Optimal? Conditional Hardness on Shared Acyclic Type Graphs

**概要.** 既知の OV に基づく自動機の共通語問題の困難性を、共有された非巡回型グラフの構造的部分型判定へ移す。固定三フィールドや関数型だけでも条件付き二次下界を示し、等価性にはほぼ線形の判定法を与える。商の大きさとアクセス数による上界も扱う。既知の帰着に対する独立した貢献の大きさが主な課題で、PDF は18ページである。

[PDF](conversations/stoc3/paper.pdf) · [ZIP](conversations/stoc3/source.zip) · [Code](conversations/stoc3/source/) · [Reproduce](conversations/stoc3/README.md)

### Fully Dynamic Interprocedural Dataflow Analysis: OMv Barriers and Summary-Local TreeFlow Updates

**概要.** 全動的な手続き間データフロー解析で、要約の大域的な依存伝播コストを明示する。各手続きがパスで呼出しが浅い非巡回グラフでも OMv 下界が残る。固定分解と非巡回呼出しの下で、影響を受ける回路ゲート数や呼出し関係に基づく上界を示す。一般の元の課題、実用解析器への統合、既存 RSM 手法との差分の評価は残っている。

[PDF](conversations/stoc4/paper.pdf) · [ZIP](conversations/stoc4/source.zip) · [Code](conversations/stoc4/source/) · [Reproduce](conversations/stoc4/README.md)

### Octagons Are APSP-Complete: Fine-Grained Complexity of Weakly Relational Abstract Domains

**概要.** Octagon と zone の操作を、指数を保つ APSP 帰着、増分 min-plus の更新・問い合わせトレードオフ、実行可能性、幅に依存する再構成によって分類する。2026年10月の APSP 上界は引用した報告結果であり、新しい最短路アルゴリズムではない。固定版 ELINA カーネルの再現資料を含む。独創性の外部評価と解析器全体の実験は未完了で、PDF は19ページである。

[PDF](conversations/stoc5/paper.pdf) · [ZIP](conversations/stoc5/source.zip) · [Code](conversations/stoc5/source/) · [Reproduce](conversations/stoc5/README.md)

## 比較順位

下記の比較順位は従来の十五編を対象とする。今回追加した CCRA 九ページ版は未評価であり、拡張版は最終公開確認を待っている。

[中文：按 STOC 相对竞争力和新增解决问题大小排序](RANKING.zh-CN.md) · [English assessment](RANKING.md) · [Data](ranking.json)

```sh
python3 scripts/check_conversations.py --all
```
