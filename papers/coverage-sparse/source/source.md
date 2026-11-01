# Frozen research question

User request, verbatim: 请自动选题搜题,并且按照**The 59th ACM Symposium on Theory of Computing (STOC 2027)模板写submission ready的pdf**

Autonomously selected original question: What is the exact worst-case correlation gap of nonnegative weighted coverage functions when pairwise independence is imposed only on the edges of a k-colorable graph, or a graph of maximum degree k-1? Can the extremal gap persist with only linearly many tested pairs and with one-sided multiplicative errors in their second moments?

For finite V, a simple graph G=(V,E), x in [0,1]^V, define D_G(x) to consist of laws of S⊆V with P(i∈S)=x_i and P(i,j∈S)=x_i x_j for each ij∈E. Nonedges carry no restrictions, and this is not a dependency-graph definition. Let f_G(x)=max_{D_G(x)} E f(S), and f^+(x)=max over laws with only the marginal constraints. A weighted coverage function is f(S)=Σ_H w_H 1{S∩H≠∅}, w_H≥0, with a finite feature family. Restrict ratios to f^+(x)>0. The original question asks for the supremum of f^+(x)/f_G(x) over all finite such objects and χ(G)≤k, for every integer k≥1, and separately Δ(G)≤k-1. Approximate constraints replace edge equalities by P(i,j∈S)≤(1+δ)x_i x_j with fixed δ≥0.

The scope is coverage functions. No claim is made to solve the analogous question for arbitrary monotone submodular functions or to prove that the resulting contribution meets a conference's acceptance threshold.
