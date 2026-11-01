# 曲率与持久对抗噪声：本地交接说明

本文为独立的局部结果论文（result-note），不是原始联合参数问题的完整解答。
原始问题状态仍为 unresolved。数学范围已经由另一个全新 Codex 上下文审查接受；
这属于 AI 核验，不是人类同行评审，也不代表 STOC 或任何期刊接收。

## 精确范围

在真实目标 f、全局固定且满足双边乘法误差的持久 oracle g 模型下，
证明主定理的有限查询上界：对每个允许随机化和自适应查询的算法，存在一个
与其私有随机种子无关的固定隐藏集合 H，使期望近似比不超过式 (3)。
目标具有精确总曲率 kappa，真实最优值为 k；查询集合大小不受 k 限制。

推论固定 0<=kappa<1、0<alpha<1/2，取 k=floor(n^alpha)，并要求
0<epsilon_n<1 且 epsilon_n*k 趋于无穷。对每个有固定 C,d 的 C*n^d
查询算法族，困难实例的期望近似比至多 rho_n*(1-kappa)+o(1)。
已知的 noisy-singleton 方法保证 rho_n*(1-kappa+kappa/k)，因此是加法意义的
渐近匹配；仅在 rho_n 有正下界时进一步声称相对匹配。已知方法均明确归功前作。

尚未解决：kappa=1、严格零噪声、epsilon*k 有界的过渡区、稠密基数、
精确有限 minimax 值以及高概率困难性。有限精确计算不是一般量词定理的证明。
邻近文献 Gong--Liu--Geng--Fang 的全文比较仍有访问限制；不据此断言不存在等价定理。
未提供用户指定的 Excel/BibTeX 权威文献表，因此未伪造该类引用。

## 文件与重现

- main.tex / references.bib / main.bbl：正文、参考文献源和生成的完整参考文献。
- acmart.cls：官方 CTAN acmart 2.20 原样复制；原始源码与许可在 vendor/。
- alpha.bst：本地 alpha 文献样式，完整作者名单，正文引用可点击。
- reproduce.py：仅用 Python 标准库，无网络，无外部全文依赖，只向 stdout 输出 JSON。
- REPRODUCIBILITY.md：构建命令、精确检查覆盖、软件环境与声明范围。
- SOURCE-PROVENANCE.json：模板及参考资料来源记录。

在解压目录运行：

```sh
python3 reproduce.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex
```

作者按用户要求依次为 Zijian Zeng、Jiayin Cao、Weinan Dai、Rui Wang、Fei Ding，
机构与邮箱列于封面，PDF Info 与 XMP 中作者顺序一致。单栏、11pt、单倍行距、
Letter 页面、标称一英寸边距、独立封面，含封面与参考文献总页数不超过 12。

当前属于写作阶段交接，正式引用/构建/视觉 release 审查需要另一个新上下文执行。
写作检查不代替该关卡。没有进行投稿、上传、邮件、账号操作或其他外部发布。
