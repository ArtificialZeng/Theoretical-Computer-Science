# 当前第一篇修订稿交接

最终题名：**Coverage Correlation Gaps under Graph-Constrained Pairwise Independence**。
发布审核作业：`coverage-sparse-release-baf234409c0d`。当前稿为
`output/pdf/main.pdf`，共 **8 页**，含独立封面与文末参考文献。
完整源文件范围见 `publication.json`；源包为
`output/source/coverage-sparse-source.zip`。逐点回复见
`response_to_reviews_zh.md`，覆盖 R1.1–R1.9、R2.1–R2.10 共 19 项。
`revision/history/` 仅为历史档案。

## 作者和版式

1. Zijian Zeng — UCSI University — 1002266693@ucsiuniversity.edu.my
2. Jiayin Cao — Ningbo University — 2795820153@qq.com
3. Weinan Dai — Zhejiang University — 21725058@zju.edu.cn
4. Rui Wang — Nanchang Institute of Technology — 2002007@nut.edu.cn
5. Fei Ding — Alibaba Group — dingfei@email.ncu.edu.cn

封面与 PDF Info/XMP 使用以上顺序；单位、邮箱来自用户，未虚构身份核验、
ORCID 或作者同意声明。沿用官方 CTAN acmart manuscript 样例及未改动的
类文件，11pt、单栏、正常单倍行距、Letter、一英寸正文页边距、非匿名、
无审稿行号。CTAN 下载和 ACM 端点 403 的真实来源见
`template/download-provenance.json`；官方原始 ZIP 仍在既定项目外位置。

## 数学与文献

新审计 `audit/math.md` 接受扩展后的全部冻结范围，包括异质/加性误差界、
增长尺度、全 m 匹配精确公式与阈值、五项有限证书和完整 t-wise 有限界。
核心问题已在 coverage 的原始范围内解决。所有冻结证据及 source.md 未改。
正文有完整证明、TikZ 科学构造图及三张精确表。一般固定图公式、分数
染色、任意单调次模推广与必要测试边数仍未解决，回复中逐项说明。

七条相关主文献覆盖基础和最近工作。RN2025 的 27/19（mutual 分母）与
三变量 pairwise-optimized 的 4/3 已在正文和回复中明确区分。已知构造、
常数、两组重采样及全 t-wise 渐近极限都有归属。没有用户 Excel 书目，
依据见 `literature/user_bibliography_check.md`，未虚构此类输入。
末尾保留两句准确说明 Codex 实质参与的 AI 方法披露。

## 复现与状态

构建：在 manuscript 目录执行
`latexmk -gg -pdf -interaction=nonstopmode -halt-on-error -outdir=../output/pdf main.tex`。
精确检查：在项目/源包根目录执行 `python3 manuscript/reproduce.py`，只读输入，
结果输出到 stdout。不要在活动审计中调用旧 verifier 的 main，它会覆盖
冻结的 verification.json；本轮只读复跑均未改动冻结数据。

本轮 RELEASE 已完成新的原始来源引用检查、干净构建和最终 8 页逐页视觉审核，
见 `audit/citations.md`、`audit/build.md`、`audit/visual.md` 与
`evidence/release/baf234409c0d/`。标题、首表位置、证明尾句与 AI 披露按
最终样式清单修复；官方类和所有冻结数学证据完全未变。精确源包入口已
只读复跑。最终源文件/PDF 将重新冻结，三项新审核绑定同一版本。监督程序
随后执行本地 publish；此前 `output/pdf/main.pdf` 为已审核构建，
`release/manifest.json` 才是激活标志。本地审核不是外部同行评议或会议录用。

仅生成本地文件，未开展其他四篇论文、外部投稿、上传或联系。
