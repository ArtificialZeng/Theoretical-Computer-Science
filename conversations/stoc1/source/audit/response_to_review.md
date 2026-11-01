# 审稿意见逐项修改记录（2026-10-31，修订 2）

| 优先级/意见 | 修改及证据 | 状态 |
|---|---|---|
| P0 单栏、11pt、1 inch、Letter | 主入口仍使用工作区 acmart；改为 manuscript/nonacm，明确 Letter/1 inch。正文、摘要、表格、参考文献使用 11.1 TeX pt，PDF 提取为约 11.06 PDF pt。首页独立；全稿目前 12 页。 | 已完成 |
| P0 作者与通讯作者 | 已按用户顺序列出 Zijian Zeng、Jiayin Cao、Weinan Dai、Rui Wang，机构、邮箱均按提供内容；Zijian Zeng 标注 corresponding author。未猜测校区或补造城市。 | 已完成 |
| P1 标题/摘要收紧 | 标题改为 Representation and Preprocessing in Grammar-Constrained Decoding: Stack Indexes and Online Completion Lower Bounds。摘要分三段，强调 tightness 仅限矩阵族指数。 | 已完成 |
| P1 上界预处理过弱 | 引入 s=O(g(M+1)(D+L+1)) 的联合 NFA 状态界，给出明确 2^{O(s)} 编译端点与分块参数 b 的静态空间/查询/更新公式及完整构造证明。 | 已完成局部理论扩展；未宣称普适最优 |
| P1 与 PSC 距离 | 明确 regularity/reversal/subset/block tabulation 是标准工具，贡献定位为 exact completion 的编译/查询/提交核算；保留待独立判断的新颖性。 | 定位已修正，新颖性未认证 |
| P1 NFA Acceptance/regex indexing | 新增 TheoretiCS 2024 NFA Acceptance 与 Algorithms 2021 regex indexing；区分静态对象、在线对象和答案语义。官方 BibTeX 已导出。 | 元数据已核验；论述支持性待 Pass 2 |
| P2 主线与 2x2 例子 | Introduction 加入单位矩阵与 v=(1,0) 的例子：10#a 的 ?=1、10#aa 的 ?=0，实际提交 ! 保持后续流。OMv 置于主定理第一项。 | 已完成 |
| P2 STLC 附属定位 | 移到辅助附录，作为经典 inhabitation 推论；展开输入规模 N、O(N^2) 开放义务、上下文存储和顺序复用空间。 | 已完成 |
| P2 防御性写作 | 合并重复否定到统一 Scope；删除 Why not assert 等辩护标题，保留定理的必要假设。 | 已完成 |
| P2 验证范围 | 改为 Sanity Checks and Reproducibility；列出准确八个深度，明确 70,500 是两个连续相同完整块的前缀检查，计数包含跨实例重复。 | 已完成 |
| P2 artifact 可取用 | 源码、构建命令、原始结果和内容哈希 manifest 已打包，并通过 PDF 文件附件注释真正嵌入；无需外部上传或账户。 | 已完成，附件字节待最终检查 |
| P2 表规模与内存 | 新增通用 NFA 分块实现/独立集合 oracle；穷举 256 个二状态双符号 NFA，真实比较 258,048 次 mask；编译 Dyck L=1..5 的行数组，报告序列化载荷；区分有效行 1,488 bytes 和含零行分配的 1,536 bytes，不当作 RSS。 | 已完成，原始结果在 artifact/block_results.json |
| Figure 1 输入前提/采样复杂度 | 原 TikZ 已存档并从当前正文移除。新图必须以 deterministic PDA + compatible lexer 为输入，并将外部 sampling 放在 mask 复杂度之外。用户指定技能处于首次 bootstrap，尚未获 S0 或跳过等待的明确指令。 | 待图形阶段选择 |
| 拼写 qery | 新稿使用 Grammar size and query predicate；未发现当前源文出现 qery。 | 已完成 |
| 每条参考文献 | 三个子 agent 分批逐条核验 21 条主要来源，20 官方导出原样替换，1 软件条目保留；同步 20 个 key，机械检查 21/21 无缺项。 | Bib 审计已完成；语义核验待确认 |
| AI 披露 | 指明受实质影响的章节、实现和文献工作，列明实际有限验证，不声称人类已独立核验尚未核验的内容。 | 已完成 |

## 当前未完成的用户目标

1. citation-check-skill 的第二遍要求先确认提取清单；异步确认已提出，尚未收到回答。不能将元数据通过写成所有论述均已通过。
2. paper-framework-figure-studio-pro 首次入口要求 plan-only；已提供执行方式选择，尚未收到回答。未生成任何候选图或虚构 S0 完成。
3. 严格新颖性、任意 LR(1) 最坏情况提交时间和通用 tight characterization 仍未建立。新分块权衡是明确的构造界，不被包装成独立认证的新成果。
