# stoc3 修订版交付索引

- `3.pdf`：18 页 STOC 2027 单栏署名评审稿，含全部证明、附录与参考文献。
- `3.tex`、`references.bib`：主源文件；`revisions/r2/bench-tables.tex` 和 `bench-plot.tex` 是由实测 JSON 生成的输入文件。
- `3-source.zip`：完整构建与复现包。
- `response-to-reviewers.md`：逐条修改说明及正文页码。
- `research_status.md`：当前已证明结论与待作者完成事项。
- `estimated_values.md`：数字来源台账，本版仍无估算实验数字。
- `artifact/README.md`：本地实验与公开版本的复现入口。
- `qa/r2/publication.json`、`remote-verification.json`：公开版本标识与远端文件哈希核对。

公开 artifact：https://github.com/ArtificialZeng/musub-artifact/releases/tag/musub-r2。

构建：在此目录执行 `./build-paper.sh`。需要 TeX Live、latexmk、TikZ/PGFPlots、BibTeX 与 alphaurl。

原匿名 sigconf 版本保存在 `history/revision-1/`。本版按后续审稿意见改为官方评审版式，不再沿用旧的 12 页 camera-ready 限制。
