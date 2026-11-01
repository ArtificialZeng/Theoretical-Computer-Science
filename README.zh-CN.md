# Theoretical Computer Science

[English](README.md) · [中文](README.zh-CN.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [日本語](README.ja.md)

本仓库整理理论计算机科学研究稿件、可复现代码与精确证书。本次快照包含 **10 套稿件材料**：最初五篇与之后持续研究产生的五篇。下文逐项提供研究摘要、PDF、保持原样的源码归档及可直接浏览的源码。

**请按范围标记阅读：**七篇稿件在本地记录中完整解决了各自明确的目标；三篇早期稿件属于部分结果，原始更广泛问题仍未解决。这些是本地研究与交付记录，不代表外部同行评审或 STOC 录用。原作者名单保持不变，后五篇稿件仅署名 Zijian Zeng。

## 稿件索引

| 课题 | 页数 | 结果范围 | 文件 |
|---|---:|---|---|
| `coverage-sparse` | 8 | 明确目标的完整解答 | [PDF](papers/coverage-sparse/paper.pdf) · [ZIP](papers/coverage-sparse/source.zip) · [Code](papers/coverage-sparse/source/) · [Reproduce](papers/coverage-sparse/README.md) |
| `privacy-interpolation` | 7 | 早期部分结果 | [PDF](papers/privacy-interpolation/paper.pdf) · [ZIP](papers/privacy-interpolation/source.zip) · [Code](papers/privacy-interpolation/source/) · [Reproduce](papers/privacy-interpolation/README.md) |
| `robust-stopping` | 11 | 早期部分结果 | [PDF](papers/robust-stopping/paper.pdf) · [ZIP](papers/robust-stopping/source.zip) · [Code](papers/robust-stopping/source/) · [Reproduce](papers/robust-stopping/README.md) |
| `curvature-noise` | 6 | 早期部分结果 | [PDF](papers/curvature-noise/paper.pdf) · [ZIP](papers/curvature-noise/source.zip) · [Code](papers/curvature-noise/source/) · [Reproduce](papers/curvature-noise/README.md) |
| `advice-matching` | 6 | 明确目标的完整解答 | [PDF](papers/advice-matching/paper.pdf) · [ZIP](papers/advice-matching/source.zip) · [Code](papers/advice-matching/source/) · [Reproduce](papers/advice-matching/README.md) |
| `c002-coverage` | 7 | 明确目标的完整解答 | [PDF](papers/c002-coverage/paper.pdf) · [ZIP](papers/c002-coverage/source.zip) · [Code](papers/c002-coverage/source/) · [Reproduce](papers/c002-coverage/README.md) |
| `c009-cycle2` | 6 | 明确目标的完整解答 | [PDF](papers/c009-cycle2/paper.pdf) · [ZIP](papers/c009-cycle2/source.zip) · [Code](papers/c009-cycle2/source/) · [Reproduce](papers/c009-cycle2/README.md) |
| `c012-upcycles` | 5 | 明确目标的完整解答 | [PDF](papers/c012-upcycles/paper.pdf) · [ZIP](papers/c012-upcycles/source.zip) · [Code](papers/c012-upcycles/source/) · [Reproduce](papers/c012-upcycles/README.md) |
| `c015-imagebound` | 6 | 明确目标的完整解答 | [PDF](papers/c015-imagebound/paper.pdf) · [ZIP](papers/c015-imagebound/source.zip) · [Code](papers/c015-imagebound/source/) · [Reproduce](papers/c015-imagebound/README.md) |
| `c017-wheeler` | 10 | 明确目标的完整解答 | [PDF](papers/c017-wheeler/paper.pdf) · [ZIP](papers/c017-wheeler/source.zip) · [Code](papers/c017-wheeler/source/) · [Reproduce](papers/c017-wheeler/README.md) |

## 各课题研究了什么

### Coverage Correlation Gaps under Graph-Constrained Pairwise Independence

**摘要.** 只在指定顶点对上约束独立性，会使可实现的覆盖函数期望下降多少？本文对 k 可着色图类和最大度不超过 k−1 的图类给出精确最坏比值 1/[1−(1−1/k)^k]，用不交团构造紧例，并通过碰撞不等式得到有限实例和测量误差界。结论是图类上的上确界，并非每个固定图都取到该比值。

[PDF](papers/coverage-sparse/paper.pdf) · [ZIP](papers/coverage-sparse/source.zip) · [Code](papers/coverage-sparse/source/) · [Reproduce](papers/coverage-sparse/README.md)

### Mandatory Excursions in Privacy-Constrained Probability Paths

**摘要.** 受隐私约束的概率路径，能否始终留在端点概率之间？本文对交换两个坐标的三点分布求出最优预算及第三坐标不可避免的最小峰值，并给出单调路径、端点区间受限路径的精确额外代价，以及一般端点的偏离证书。这是早期部分结果稿，原始一般问题仍未完整解决。

[PDF](papers/privacy-interpolation/paper.pdf) · [ZIP](papers/privacy-interpolation/source.zip) · [Code](papers/privacy-interpolation/source/) · [Reproduce](papers/privacy-interpolation/README.md)

### Certified Expected-Cost Optimization for Robust Ski Rental

**摘要.** 滑雪租赁策略如何利用有限有理预测，同时在每个真实时长上满足期望竞争比约束？本文在无界购买日和时长域上给出精确期望成本优化及原始、对偶证书，证明至多 b+1 个购买日的支持界，并求出均匀预测的显式前沿。运行时间对数值 b 和输入位长为多项式。原始更广泛问题仍未完整解决。

[PDF](papers/robust-stopping/paper.pdf) · [ZIP](papers/robust-stopping/source.zip) · [Code](papers/robust-stopping/source/) · [Reproduce](papers/robust-stopping/README.md)

### A Sparse-Cardinality Curvature Bound under Persistent Adversarial Noise

**摘要.** 已知曲率时，固定的乘性价值噪声如何影响子模最大化？在 k=⌊n^α⌋、0<α<1/2 且 εk→∞ 的稀疏基数范围，本文用隐藏集合构造给出与带噪单元素选择法渐近匹配的下界。噪声趋零时，极限因子为 1−κ，与精确预言机的 1−κ/e 不同。这篇早期稿只解决该范围，原始无此限制的一般问题仍开放。

[PDF](papers/curvature-noise/paper.pdf) · [ZIP](papers/curvature-noise/source.zip) · [Code](papers/curvature-noise/source/) · [Reproduce](papers/curvature-noise/README.md)

### Matching Advice on Degree-Two Bipartite Graphs: Exact Consistency–Robustness Frontiers

**摘要.** 在线二分匹配面对可能错误的匹配建议时，一致性与鲁棒性怎样权衡？对无权、最大度为二的图，本文给出精确前沿 min{3/4, 3/2−c}；对环子类，前沿为 min{7/8, 7/4−c}。优先处理已暴露离线邻点的算法达到端点，小型不可区分实例给出匹配上界。模型采用 oblivious adversary，建议允许包含不存在的边。

[PDF](papers/advice-matching/paper.pdf) · [ZIP](papers/advice-matching/source.zip) · [Code](papers/advice-matching/source/) · [Reproduce](papers/advice-matching/README.md)

### A Size-Independent Discrepancy Bound for Sparse Coverage Functions

**摘要.** 稀疏覆盖函数能否以不依赖物品总数的误差实现均衡？若每个物品在整个函数族中至多参与 t 次特征出现，本文给出确定性多项式时间的 k≥2 类划分，使任意两类的差异不超过 4kt(kt−1)²。证明用 Hall 见证平衡大特征，再用多选 Beck–Fiala 舍入控制剩余相互作用，得到只依赖 t、k 的多项式界。

[PDF](papers/c002-coverage/paper.pdf) · [ZIP](papers/c002-coverage/source.zip) · [Code](papers/c002-coverage/source/) · [Reproduce](papers/c002-coverage/README.md)

### A Global Sidorenko Inequality for 2-Subdivided Alternating Cycles

**摘要.** 每条边再细分一次的交替有向环，是否在所有长度上满足局部锦标赛 Sidorenko 性质？对交替 2ℓ 环得到的 Hℓ，本文证明其锦标赛同态密度至少为 2^(−4ℓ)。反对称矩阵不等式统一处理整个环族，并给出强制性估计与等号刻画。一个三顶点例族表明强制性指数 4ℓ 最优。

[PDF](papers/c009-cycle2/paper.pdf) · [ZIP](papers/c009-cycle2/source.zip) · [Code](papers/c009-cycle2/source/) · [Reproduce](papers/c009-cycle2/README.md)

### A Universal Partial Cycle with Three Wildcards per Window

**摘要.** 是否存在每个窗口含多个通配符的非平凡通用部分环？本文给出长度为 512 的二元环，每个长度为 12 的窗口恰含三个通配符。512 个窗口各覆盖八种补全，恰好无重复地划分全部 4096 个二元 12 字。整个环用 128 位八进制数表示，并由不依赖求解器的短 Python 程序完整核验，构成有限存在性证明。

[PDF](papers/c012-upcycles/paper.pdf) · [ZIP](papers/c012-upcycles/source.zip) · [Code](papers/c012-upcycles/source/) · [Reproduce](papers/c012-upcycles/README.md)

### Tight Mortality Bounds for Image-Bounded Nondeterministic Automata

**摘要.** k-image-bounded 非确定性自动机的已知死亡词长度上界是否紧？本文证明，对每个固定 k≥2，最短死亡词长度的最大值为 Θk(n^(k+1))。对所有充分大的 n，即便要求二元字母表和强连通性，下界仍成立。队列与循环时钟产生所需延迟，全局像集不变量保证任意输入词都不违反 k 像集限制。

[PDF](papers/c015-imagebound/paper.pdf) · [ZIP](papers/c015-imagebound/source.zip) · [Code](papers/c015-imagebound/source/) · [Reproduce](papers/c015-imagebound/README.md)

### Deciding Membership and Realizability for Wheeler Transducers

**摘要.** 输出单调区间数量未预先给定时，能否判定 Wheeler 转导器成员资格？本文对允许部分转移、擦除输出的有限精简确定性 subsequential 转导器给出多项式时间算法，保守位复杂度为 O(S^13)。分支强连通分量和简单环分别采用不同结构判据，并进一步得到等价 Wheeler 实现的可判定性与构造方法；实现构造不主张多项式时间或最小性。

[PDF](papers/c017-wheeler/paper.pdf) · [ZIP](papers/c017-wheeler/source.zip) · [Code](papers/c017-wheeler/source/) · [Reproduce](papers/c017-wheeler/README.md)

## 已验证研究笔记：原题仍未解决

另有两套材料记录证明方法的障碍。[二元奇偶接口](notes/tp-parity-interface/)证明一张共享的72项表无法合成受测 TP 图的三着色，但没有否定原始三着色猜想。[删点环提升障碍](notes/facet-cycle-lifting/)比较 P19 的200个极大独立集与基础环的189个顶点，排除一种特定归纳方案，但不是 facet-Hamiltonicity 的反例。两项均附精确证据与检查代码。

## 复现与编译

便携数学检查仅需 **Python 3.10+ 标准库**。重编译 PDF 还需 LaTeX 发行版、`latexmk` 与 Poppler（`pdftotext`），所需未修改的官方 acmart 文件已附带。脚本在临时副本上运行，保留归档源码原样。

在仓库根目录运行下列命令。单篇复现可将 `--all` 改成 `--paper ID`。有限计算只核验其注明的范围，一般性数学论证见稿件正文；TeX 时间戳可能导致重编译 PDF 的字节不同。

```sh
git clone https://github.com/ArtificialZeng/Theoretical-Computer-Science.git
cd Theoretical-Computer-Science
python3 scripts/verify_artifacts.py
python3 scripts/reproduce.py --all
# Optional: rebuild every PDF
python3 scripts/build_pdfs.py --all
```

## 目录说明

`papers/ID/paper.pdf` 为交付 PDF，`source.zip` 为保持原样的交付源码包，`source/` 提供相同文件供浏览。`catalog.json` 记录哈希与复现命令，`validation/` 记录本次实际检查。每篇 provenance 保留引用核查的适用范围，包括滑雪租赁稿件的文献访问限制。

## 作者与研究辅助

维护者：**Zijian Zeng，UCSI University** · 1002266693@ucsiuniversity.edu.my。研究、代码、证明推导与写作使用了实质性 AI 辅助，稿件中已披露。所含第三方文件保留原许可说明，见 [RIGHTS.md](RIGHTS.md)。
