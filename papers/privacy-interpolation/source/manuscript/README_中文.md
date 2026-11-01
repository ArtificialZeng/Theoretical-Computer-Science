# 本地交接说明

本稿为独立的局部结果短文（result-note），原始一般插值问题仍未解决。正文只覆盖已通过当前冻结快照数学审查的三个定理；没有加入可选几何插值 Pareto 比较。

1. 对所有正的交换三元组 p=(c,a,b)、q=(c,b,a)，0<a<b、c=1-a-b>0，精确给出可行预算阈值 T*：b≤1/2 时为 log(b/a)，b>1/2 时为 log(1/[4a(1-b)])。每个 L≥T* 下最小储备坐标峰值为 max{c,1-2a exp(L/2)}，有显式达到路径；最低预算的单位区间路径唯一。
2. 端点隐私距离为 η>0 时，逐坐标单调或限定在端点范围的最优预算，与无约束最优预算之比，在 n≥3 的精确最坏值均为 2log((exp(η)+1)/2)/η，且各维均有正的达到例子。二元情形两种比值均为 1。
3. 一般端点的逐坐标峰值必要证书可用有理断点扫描和一个平方根精确求值；全部坐标的算术操作数为 O(n²+n log n)。没有断言一般上限约束的充分性、位复杂度或一般最优路径分解结论。

已知的 Laplace/Blackwell 无约束可达性、二元速度积分、仿射曲线弧长重参数化和端点包络均作为背景或标准工具，不作为新定理。研究 pass 1 的已知结果停放状态和 pass 2 计数均保持不变。文献比较只支持有限来源范围内的判断，不构成优先权证明，也不表示会议接收。

作者顺序为 Zijian Zeng（UCSI University）、Jiayin Cao（Ningbo University）、Weinan Dai（Zhejiang University）、Rui Wang（Nanchang Institute of Technology）、Fei Ding（Alibaba Group）；全部指定邮箱见封面。采用未修改的官方 acmart 2.20，单栏 11pt、单倍行距、Letter 和名义一英寸正文页边距，含独立封面及最后的参考文献，总页数以 PDF 检查记录为准，要求不超过 12。AI 段落位于参考文献之前，摘要正面陈述结果，未解决问题只在正文末尾说明一次。

复现命令（从项目或解压后的根目录运行）：

```sh
python3 manuscript/reproduce.py
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error -file-line-error manuscript/main.tex
```

只需 Python 3 标准库和已安装的 TeX Live/latexmk。输出 JSON 应为 status=passed；路径 867 条、半区间 1824 个、坐标单元 5472 个、扫描对比 3483 项。代码不覆盖冻结研究证据。源码包不含第三方论文全文，编译和精确检查不需要联网。原始来源和冻结证据保持不变。

本轮仅为 WRITE：数学审查已经由先前的独立模型上下文通过；这不是人工同行评审。写作预检也不能代替真正的新上下文 RELEASE。下一步是使用最终冻结摘要进行全引用、全页视觉、元数据、字体、日志和依赖闭包审查，再运行实际发布门禁。任何后续源文件或 PDF 修改都需重建、重新冻结和重查。本地文件生成不授权外部投稿、上传、邮件或联系，未执行这些操作。
