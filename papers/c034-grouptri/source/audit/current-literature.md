# Fresh primary-source comparison

Job: c034-grouptri-referee-e6a7f319b8fe.
Checked 2026-11-02 UTC during this referee job. This is a bounded independent
comparison, not an exhaustive priority certificate.

1. Ruhollah Majdoddin, *Thin matrix products up to D <= N^0.172 and lossless
   reductions for 3SUM, Exact Triangle and APSP, with 3SUM over abelian groups
   and a dichotomy for coordinatewise problems*,
   [arXiv:2610.17420](https://arxiv.org/abs/2610.17420).
   The live primary record displayed v1 only, submitted 12 October 2026.
   I read the frozen PDF's Section 19 Model, Definition 2.1, Corollary 9.1
   and its instantiation of H, Section 16, Definition 21.1, Theorem 21.3
   and its proof, Corollary 21.7, Remark 21.8, Propositions 21.9--21.10 and
   Open Problem 21.12. Theorem 21.3 gives deterministic time
   O(p^6 n^(3-epsilon*gamma) log^6 n) for elementary groups of polynomial
   order. Corollary 9.1(b) supplies epsilon=1/14, gamma=0.077, rather than
   an assumed new primitive. The later propositions require a small
   quotient-zero population or limited incident residue diversity; they
   do not imply the full bounded-exponent theorem. The PDF explicitly
   leaves the unrestricted Z_4 case and the full question open.

2. Timothy M. Chan, Virginia Vassilevska Williams and Yinzhan Xu,
   *Fredman's Trick Meets Dominance Product: Fine-Grained Complexity of
   Unweighted APSP, 3SUM Counting, and More*,
   [arXiv:2303.14572](https://arxiv.org/abs/2303.14572), Theorem 5.1,
   printed pp. 18--19. The live record displayed v1 only and identifies
   the paper with STOC 2023. I read the complete decomposition construction,
   correctness and update argument, and its preprocessed-universe application.
   It has cubic initial preprocessing, unlike its subsequent update bound.
   Its high-frequency equations are the candidate's edgewise potential
   identities. These identities and the frequency/hitting decomposition
   must be attributed to this prior work. Replacing the initialization and
   using the identities to solve a non-split group extension are the relevant
   changes; the candidate is not a new triangle decomposition theorem.

3. Nathan Sheffield, Virginia Vassilevska Williams and Zoe Xi,
   *The Limits of Black-Box Reductions for All-Pairs Triangle Detection*,
   [arXiv:2608.19092](https://arxiv.org/abs/2608.19092), introduction and
   Section 2.3. The live record displayed v1 only, submitted 19 August 2026.
   Generic detection/all-edge/listing relationships are already prior tools.
   Their quantitative upper and lower bounds do not conflict with the
   deliberately lossy capped routine, which lists at most n^(3-theta)
   outputs and does not assert a tight listing equivalence. No new generic
   listing reduction is accepted as a contribution here.

4. Neha Pant and Ryan Williams,
   *Beating Trivial Time for Tricky Triangle Tasks*,
   [arXiv:2606.27727v1](https://arxiv.org/html/2606.27727v1), Definition 24
   and Theorem 4 in Section 5.2. The primary text concerns polynomially
   bounded integer weights and an expected time
   O(n^3 log(w)/w^(3/2)). With logarithmic word size this is a logarithmic
   improvement, not the bounded-exponent group theorem with a fixed power
   saving. It does not supply a competing full resolution.

I also opened the primary author's current
[repository README](https://github.com/Majdoddin/formal-math) and
[groups README](https://raw.githubusercontent.com/Majdoddin/formal-math/main/groups/README.md).
The latter lists algebraic correctness formalizations for Theorem 21.3 and
explicitly excludes its running time and call legality from the formalized
claims. I did not build the repository, pin a new commit, or infer a runtime
certificate from its README. Its displayed scope supplies no all-exponent
algorithm absent from the PDF.

Independent search queries included:

- `"Exact Triangle" "abelian" "exponent" algorithm`
- `"Exact Triangle" "quotient" "kernel"`
- `"Exact Triangle" "group" "decomposition"`
- `"Exact Triangle" "group extension" algorithm`
- `"bounded exponent" "subcubic"`
- `"bounded-exponent" "triangle" algorithm`
- `"triangle decomposition" "finite abelian groups" algorithm`
- `"Exact Triangle" "cyclic" "group" subcubic`
- `"2610.17420" "21.12"`

Many results used the unrelated categorical meaning of exact triangle; they
were not used as evidence. No equivalent full closure theorem was located
in the primary material inspected or these bounded searches. That finding
supports the qualified novelty assessment; it does not establish universal
priority or external acceptance. The mathematical review uses the stated
elementary backend as a prior theorem, not a fresh formal audit of all 130
pages of its matrix dependencies.
