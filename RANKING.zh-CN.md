> Historical comparison of an earlier snapshot. For current manuscript categories and versions, use [the unified index](README.md). This older comparison neither ranks every current topic nor determines submission_ready status.

# STOC 综合比较与问题规模排序

[English](RANKING.md) · [中文](RANKING.zh-CN.md)

优先外部复核并考虑冲刺的四项是 **c015-imagebound、c017-wheeler、c009-cycle2、c002-coverage**。这只是当前材料池中的相对优势，现有证据不足以把任何一篇认定为“稳收”。主题最接近细粒度算法与复杂度的其他稿件是 stoc3、stoc4、stoc1、stoc5，但主题合适不能替代实质创新。

本表按已经取得的结果排序，不按原始宏大目标、标题、页数或代码量排序。没有可靠校准数据，不能给出可信的 30%/60% 等录用百分比；“录用可能性”采用有依据的相对排序。同梯队相邻名次不宜过度解读。此次比较读取正文、现有审查与来源记录，并重跑新增稿件的可执行检查；不是新的完整数学审稿，也不是外部同行评审。

## 按 STOC 相对竞争力从高到低

| 顺序 | 稿件 | 问题规模序 | 相对判断 | 主要依据与风险 |
|---:|---|---:|---|---|
| 1 | [c015-imagebound: 自动机死亡词层级](papers/c015-imagebound/paper.pdf) | 2 | 优先复核与冲刺 | 对每个固定 k≥2 匹配 n^(k+1) 指数，并保留二元、强连通限制；队列与时钟不变量有实质构造内容。风险是问题仍较专门。 |
| 2 | [c017-wheeler: Wheeler transducer 判定问题](papers/c017-wheeler/paper.pdf) | 1 | 优先复核与冲刺 | 解决现行模型的完整成员判定与构造性可实现性，处理擦除输出及未知数量的有限分段。O(S^13) 算法的 SCC 判据需要向广泛读者讲清并作外部复核。 |
| 3 | [c009-cycle2: 环族的全局 Sidorenko 不等式](papers/c009-cycle2/paper.pdf) | 4 | 第二优先梯队 | 把原先局部问题推进为整个无限环族的全局不等式，含等号与最优指数的强制性。数学方法较突出，算法层面的影响尚不直接。 |
| 4 | [c002-coverage: 与规模无关的非线性 discrepancy](papers/c002-coverage/paper.pdf) | 3 | 第二优先梯队 | 对完整稀疏覆盖模型消除物品数依赖，并给出构造性非线性转线性桥梁；O(t³k³) 依赖较粗，未解决一般 influence-sparse 问题。 |
| 5 | [stoc3: 结构子类型判定的二次屏障](conversations/stoc3/paper.pdf) | 5 | 较低，取决于独立创新 | 细粒度复杂度与表示敏感性很符合 STOC；但 OV 自动机困难性已有前作，新增类型语义编码是否足够独立，是核心风险。 |
| 6 | [stoc4: 动态过程间数据流](conversations/stoc4/paper.pdf) | 8 | 较低，取决于独立创新 | 动态算法及路径过程上的 OMv 障碍很自然；正面界依赖受影响电路规模、无环调用及固定分解，一般目标仍未完成，且与已有 RSM 更新机制接近。 |
| 7 | [stoc1: 语法约束解码](conversations/stoc1/paper.pdf) | 10 | 较低，取决于独立创新 | 问题及时，参数计费较认真；但一般 LR(1) 加速未完成，栈标注有经典前作，与在线 NFA 模拟的区别仍待建立。 |
| 8 | [coverage-sparse: 图约束相关性间隙](papers/coverage-sparse/paper.pdf) | 6 | 较低 | 图类精确层级与碰撞不等式干净，但构造和常数与前作重合较多；新增技术较短，主要障碍仍是重要性。 |
| 9 | [stoc5: Octagon 与 APSP 的指数等价](conversations/stoc5/paper.pdf) | 9 | 较低 | 题材很符合细粒度复杂度；但归约与经典规范化占主要部分，所引 2026 年 10 月 APSP 指数属于其他作者报告的算法，不是本稿的新突破。 |
| 10 | [stoc2: 带标记回文的语言编辑距离](conversations/stoc2/paper.pdf) | 11 | 较低 | 限定子类有匹配上下界和见证，但文法类较窄，主要围绕 Landau–Vishkin/LCE 方法，一般 LR(1) 原题仍开放。 |
| 11 | [advice-matching: 最大度二匹配中的建议鲁棒性](papers/advice-matching/paper.pdf) | 7 | 较低 | 一致性与鲁棒性精确前沿有清楚的在线算法意义，但最大度二及环的限制，使增量小于一般匹配问题。 |
| 12 | [c012-upcycles: 三个通配符的通用部分环](papers/c012-upcycles/paper.pdf) | 12 | 当前 STOC 竞争力很低 | 是原题完整、可精确核验的存在性见证；当前核心是一条有限 512 环，缺少一般构造、算法框架或广泛刻画。 |
| 13 | [curvature-noise: 持续噪声下的曲率界](papers/curvature-noise/paper.pdf) | 13 | 很低；原题部分范围 | 只在指定稀疏基数范围给出匹配渐近界，未解决无此限制的原题；参数范围和重要性是主要风险。 |
| 14 | [robust-stopping: 带证书的鲁棒滑雪租赁优化](papers/robust-stopping/paper.pdf) | 14 | 很低；原题部分范围 | 精确证书与复现有价值，但更广目标未解决，数值 b 的多项式时间并非 log b 多项式；尚未建立重要的新在线原则。 |
| 15 | [privacy-interpolation: 隐私约束概率路径](papers/privacy-interpolation/paper.pdf) | 15 | 很低；原题部分范围 | 三点分布偏离公式精确，但一般问题未解决，当前结果是这一批中最专门的。 |

## 按实际新增解决问题的大小从高到低

1. [c017-wheeler: Wheeler transducer 判定问题](papers/c017-wheeler/paper.pdf)
2. [c015-imagebound: 自动机死亡词层级](papers/c015-imagebound/paper.pdf)
3. [c002-coverage: 与规模无关的非线性 discrepancy](papers/c002-coverage/paper.pdf)
4. [c009-cycle2: 环族的全局 Sidorenko 不等式](papers/c009-cycle2/paper.pdf)
5. [stoc3: 结构子类型判定的二次屏障](conversations/stoc3/paper.pdf)
6. [coverage-sparse: 图约束相关性间隙](papers/coverage-sparse/paper.pdf)
7. [advice-matching: 最大度二匹配中的建议鲁棒性](papers/advice-matching/paper.pdf)
8. [stoc4: 动态过程间数据流](conversations/stoc4/paper.pdf)
9. [stoc5: Octagon 与 APSP 的指数等价](conversations/stoc5/paper.pdf)
10. [stoc1: 语法约束解码](conversations/stoc1/paper.pdf)
11. [stoc2: 带标记回文的语言编辑距离](conversations/stoc2/paper.pdf)
12. [c012-upcycles: 三个通配符的通用部分环](papers/c012-upcycles/paper.pdf)
13. [curvature-noise: 持续噪声下的曲率界](papers/curvature-noise/paper.pdf)
14. [robust-stopping: 带证书的鲁棒滑雪租赁优化](papers/robust-stopping/paper.pdf)
15. [privacy-interpolation: 隐私约束概率路径](papers/privacy-interpolation/paper.pdf)

## 投稿状态与范围

stoc1–stoc5 是其他对话已有稿件，保留原 PDF、源码包与署名；它们没有经过本持续研究项目的新稿完整原题解答门槛，不能据此升级其成果等级。stoc6–stoc8 仅有模板，不参与排名。三篇早期部分结果及两份方法障碍笔记的原题仍未解决，未把它们包装成新的完整解答。

stoc2 当前是匿名双栏稿，投稿前需按官方要求改为具名、单栏评审格式。stoc3 为18页、stoc5为19页；超过此前本对话提出的个人12总页要求，但官方投稿并无总页数上限，不能把二者混为一谈。此轮整理不修改原稿。

STOC 2027 要求新颖的理论贡献、可核验完整证明，以及开头12页内清楚解释重要性；每名作者最多署名5份投稿。建议先对前四项作外部专家复核，第五顺位 stoc3 的前提是证明其语义转移具有足够独立价值。上述格式与署名规则来自[官方 CFP](https://acm-stoc.org/stoc2027/stoc2027-cfp.html)。

没有把缺少系统实验当作纯理论论文的自动否决项。stoc5 的 October 2026 APSP/SSSP 界是被引用的新近原始报告，归约转移不能算成本稿独立解决 APSP；本次比较也未验证这些外部新近报告的全部证明。可执行日志只支持其明确有限范围。

本次同步验证：新增五篇的清洁编译与 PDF 文本比对均通过，stoc2–stoc5 的复现检查通过。stoc1 的两个检查入口都依赖 Rust 库，因当前缺少 rustc 未重跑，保留 exit127 记录；这不构成数学反例。
