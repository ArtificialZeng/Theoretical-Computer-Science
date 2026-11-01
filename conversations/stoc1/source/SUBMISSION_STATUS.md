# 修订 2 状态

当前主稿按审稿意见改为具名、单栏、Letter、1 inch 页边距，仍使用本工作区 acmart 模板。正文和参考文献均至少 11 PDF pt；首页包含用户提供的四位作者及通讯作者。文件继续命名为 1.pdf。

标题现为 Representation and Preprocessing in Grammar-Constrained Decoding: Stack Indexes and Online Completion Lower Bounds。共 12 页，含首页、所有证明、辅助附录及参考文献。

已完成：逐项文字/结构修订、显式分类器规模与分块表权衡、类型结果附属定位、真实有限验证、PDF 内嵌代码包、21 条文献的主要来源/元数据核验（20 条官方导出，llguidance 保留原记录）。

尚未完成：
- citation-check-skill 第二遍论述支持性核验；必须先确认 audit/citations/claims_pass1.md。
- 通过 paper-framework-figure-studio-pro 生成并插入新架构图；其首次 bootstrap 及逐阶段规则要求明确的下一步指令。旧 TikZ 已存档，当前正文不含新架构图。
- 独立的人类数学审查和新颖性认证。本文并未解决一般 LR(1) 最坏情况加速或给出任意 grammar-constrained decoding 的完整紧界。

主要来源仍按 https://acm-stoc.org/stoc2027/stoc2027-cfp.html 的投稿版式要求处理；没有执行任何投稿、外部发布、邮件或视频上传。

构建：latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build 1.tex
代码包：artifact/tpc-artifact.zip，标识 tpc-completion-r2-20261031。
审稿逐项记录：audit/response_to_review.md。
书目审计：audit/references/reference_audit.md。
