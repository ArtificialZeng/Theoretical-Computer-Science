# 本地交付：Deterministic Quasipolynomial MST Approximation under Decrease-Only Corruption

状态标记：**working_paper**。数学及文件交付检查与 STOC 竞争力判断分别记录。
具体依据见 STOC_ASSESSMENT.json；缺少新的明确 STOC 级别审查时保守标为 working_paper。

作者：Zijian Zeng，UCSI University，1002266693@ucsiuniversity.edu.my。
PDF共8总页（含标题及参考文献）。本地数学、新颖性/价值及发布检查
记录随源码提供；这些是AI辅助核验，不是外部人类同行评审或STOC录用判断。
一般结论由完整证明支持；计算仅覆盖脚本声明的有限范围。

使用从官方CTAN发行源下载的未修改acmart.cls。原始模板请求地址：
https://mirrors.ctan.org/macros/latex/contrib/acmart.zip；下载原始ZIP的SHA-256：93933ce58fbeffa13e23398bb523fcb68275ecc73369c6bc73b421eeef2c10de。
对应dtx/ins源文件及原始README置于源码包vendor/acmart/。
格式依据：https://acm-stoc.org/stoc2027/stoc2027-cfp.html 。投稿版为非匿名、单栏、
至少11pt、Letter纸及四周一英寸边距；本项目另遵守用户的12总页上限。

编译：进入源码包的manuscript目录，运行
`TEXINPUTS=.//: BSTINPUTS=.//: latexmk -gg -pdf -jobname=main -interaction=nonstopmode -halt-on-error -outdir=../output/pdf main.tex`。
生成的PDF位于源码包的output/pdf/main.pdf。
有限复现入口和完整命令见压缩包内REPRODUCE.md，各脚本使用Python3。
第三方论文全文不重复打包；原始链接和核验范围保留在报告中，因此源码包不含
内部数学门禁所引用的全部文献缓存。全部声明的编译输入、自己的证明和检查代码均包含。
原始网页摘录缓存也保留在内部资料中；其文件名和哈希列于交付清单。
请运行REPRODUCE.md指定的自包含正例检查，而非依赖内部文献缓存的门禁程序。

稿件披露Codex的实质性参与。这里只生成本地材料，没有外部投稿、上传或联系。
实际提交还涉及会议要求的作者讲解视频及投稿系统信息。
