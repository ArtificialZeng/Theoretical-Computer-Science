# 当前版本状态：revision 2

- `3.pdf`：18 页非匿名单栏评审稿；标题页、12 页正文、附录及参考文献。11pt，四周 1.05 英寸，Letter。
- 已录入用户提供的五位人类作者、单位与邮箱，顺序不变；Zijian Zeng 为通讯作者。
- `response-to-reviewers.md`：对照审稿报告逐项列出修改与页码。
- `3-source.zip`：本版全部构建依赖与可复现实验；原 9 页匿名版见 `history/revision-1/`。
- 实际公开 artifact：https://github.com/ArtificialZeng/musub-artifact，版本 musub-r2，提交 `87ad1b7f6e5c603a94bdbe2e1fb6a71cc70c8f2c`。

理论主线是已知 automata hardness 向共享无环类型图的语义转移，包含三字段与纯函数编码、O(log n) 高度限制、递归宽度障碍，以及标准商图/乘积上界与有限访问上界。已补充并正面比较 2025 年 Drabik、Dürr、Frei、Mazowiecki、Węgrzycki 的 Lemma 6.4。

原来的“按回边数近线性”主张在共享图模型下与 OVH 冲突，仍没有恢复为定理。一般递归函数集合论类型的 union-width 主张也没有被宣称证明；有限 Boolean-record 结果移至附录。

本次新增 smaller-half quotient 实现、阶段计时、两组状态访问数及统一 n_v+n_e 规模。DefinitelyTyped 投影接受率仍为 6.79%，只支持该投影子集的统计。无完整 tsc/Scala 编译器性能结论。

官方评审格式和署名问题已修正，但独立人工证明/新颖性复核、真人视频、作者责任声明和实际投稿仍需作者完成。没有提交 HotCRP；GitHub 只发布了经用户授权的 artifact。
