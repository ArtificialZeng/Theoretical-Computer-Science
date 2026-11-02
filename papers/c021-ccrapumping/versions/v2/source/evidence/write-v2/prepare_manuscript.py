from pathlib import Path
import hashlib,json
root=Path('.')
old=(root/'history/v1/manuscript/main.tex').read_text()
head=old[:old.index('\\title{')]
head += r'''\newcommand{\tr}{\operatorname{tr}}
\newcommand{\vecop}{\operatorname{vec}}
\title{Copyless Realizability of Unipotent Weighted Automata\\and a Uniform Pumping Separation}
\author{Zijian Zeng}
\affiliation{\institution{UCSI University}\country{Malaysia}}
\email{1002266693@ucsiuniversity.edu.my}
\renewcommand{\shortauthors}{Zijian Zeng}
\begin{document}
\begin{abstract}
\normalsize
We characterize copyless realizability for rational weighted-automaton functions whose minimal representation has unipotent matrices for every word. Such a function is recognized by a deterministic finite-state copyless polynomial cost register automaton if and only if its minimal letter matrices commute, equivalently if it is a rational polynomial in the letter counts. The theorem permits arbitrary finite control, any finite number of registers, arbitrary rational constants, and singular or nonlinear updates.

The proof compresses minimum-rank copyless transformations to affine coordinate permutations while preserving the full observable subquotient. Their unipotent factors commute. Common return blocks then recover the entire minimal weighted algebra, removing finite control. Standard exact linear algebra gives polynomial-bit-time recognition of the unipotent sector and copyless membership within it. For explicitly listed scattered-pattern sums, membership admits polynomial-size copyless synthesis or equal-Parikh negative certificates of length at most twice the natural representation dimension.

As a consequence, we prove nonrecognizability of the position-sum function proposed by Mazowiecki, Puch and Smertnig. It satisfies their uniform pumping condition with one finitely generated subsemiring $\Z[1/2]$ and the single exponent $m=1$, for all prefixes, repeated words and suffixes, including the characteristic-zero coefficient-sum requirements. This disproves sufficiency of that condition among weighted-automaton recognizable functions.
\end{abstract}
\maketitle
\thispagestyle{plain}
\clearpage

\section{Results and context}
A cost register automaton reads a word from left to right, updates finitely many registers, and evaluates an output expression. The copyless restriction permits each old register at most once across an update and at most once in the output. Registers may be added, multiplied, merged or reset; finite-state control may select different updates for the same letter. We study which rational weighted-automaton functions admit such computations. All realizability statements below concern this full polynomial model, with arbitrary rational constants and no fixed register bound.

A weighted representation has the form $f(w)=\lambda M_w\gamma$, with $M_{uv}=M_uM_v$. Minimality means that the reachable row span and the observable column span are full; minimal representations are unique up to simultaneous similarity. A matrix $M$ of dimension $d$ is \emph{unipotent} if $(M-I)^d=0$. We call a nonzero recognizable function \emph{all-word unipotent} if every word matrix of its minimal representation is unipotent. This property is intrinsic to the function. Individually unipotent letter matrices do not suffice: $I+E_{12}$ and $I+E_{21}$ in dimension two have a product of trace three.

\begin{theorem}\label{thm:characterization}
For a nonzero all-word-unipotent recognizable function $f:\Sigma^*\to\Q$, the following are equivalent:
\begin{enumerate}
\item $f$ has a deterministic finite-state polynomial $\Q$-CCRA;
\item the letter matrices of its minimal representation commute pairwise;
\item $f$ is invariant under permutations of input positions;
\item $f(w)$ is a rational polynomial in the counts $(|w|_a)_{a\in\Sigma}$.
\end{enumerate}
The zero function has a constant-zero one-state realization.
\end{theorem}

\begin{theorem}\label{thm:decision}
From a rational weighted representation, all-word unipotence of the minimal representation is decidable in polynomial bit time. Within this sector, $\Q$-CCRA realizability is decidable in polynomial bit time.
\end{theorem}

For words $w,p$, let $[w:p]$ count scattered embeddings of $p$ into $w$, with $[w:\eps]=1$. Explicit pattern sums provide a natural constructive instance.
\begin{theorem}\label{thm:patterns}
Given explicitly listed words $p$ over a finite explicitly given alphabet and binary-encoded rational coefficients $c_p$, put
\[
 f(w)=\sum_p c_p[w:p],\qquad D=\sum_p(|p|+1).
\]
Copyless realizability is equivalent to permutation invariance and is decidable in polynomial bit time. A YES instance admits a one-state copyless realization of polynomial encoding size with at most $\sum_p|p|$ registers. A NO instance admits computable words $uabv$ and $ubav$, each of length at most $2D$, with different values. Empty patterns, repeated patterns, negative coefficients and rational cancellations are allowed. An empty list is an immediate constant-zero YES instance.
\end{theorem}

The structural theorem also resolves a question left by the pumping theory of Mazowiecki, Puch and Smertnig~\cite{MPS26}. Their uniform necessary condition tests all sequences $f(uw^{m(n+1)}v)$ with one coefficient semiring and one exponent $m$ for every triple $(u,w,v)$. Their Section~3.2 conjectures insufficiency even among recognizable functions and proposes the witness
\begin{equation}\label{eq:witness}
 f(b_1\cdots b_j)=\sum_{i=1}^j i b_i,\qquad b_i\in\{0,1\}.
\end{equation}
\begin{theorem}\label{thm:main}
The function in~\eqref{eq:witness} is weighted recognizable and satisfies the source's uniform $R$-generable exponential-polynomial condition with $R=\Z[1/2]$ and $m=1$, including every characteristic-zero degree-coefficient sum. No finite-state polynomial $\Q$-CCRA recognizes it.
\end{theorem}
Thus the proposed sufficiency implication over fields is false, as witnessed over $\Q$. The pumping calculation is already in~\cite[Example~26]{MPS26} and~\cite[Appendix~B.4]{MPSfull}; the missing assertion settled here is nonrecognizability in the full model.

\paragraph{Mechanism and significance.}
Unary pumping information sees one repeated action at a time. Our obstruction concerns how different minimal actions interact. Squarefree monomials linearize copyless updates, but the minimal weighted space is an invariant subquotient, not a subset of registers. A minimum-rank word yields a copyless retraction whose pullback is a polynomial projection. That projection acts identically on the minimal quotient and compresses every letter to an affine coordinate permutation. After taking powers, their unipotent factors are translations in common coordinates and commute. To handle finite control, common return blocks are chosen so that polynomial unipotent roots recover every original letter matrix. Their algebra and both minimality spans survive. This gives a characterization of an infinite sector, rather than only a separation for one function.

\paragraph{Closest prior work.}
The squarefree translation is known~\cite[Lemma~50]{MPSfull}; we include its short proof. The normal-form and reset analysis of Mazowiecki and Riveros~\cite{MR19} supplies important structural context. In particular, their Proposition~3 and Lemma~5 use a non-zero semiring hypothesis, unavailable for arbitrary signed rational computations; they do not justify a cancellation-free reduction here. Puch and Smertnig~\cite[Theorem~3.4, Corollary~3.5 and Proposition~9.4]{PS24} study invertible weighted representations and block-triangular monomial covers. Noncommuting unitriangular matrices already have monomial diagonal blocks, so these cover results do not yield the present copyless obstruction.

Polynomial-time commutativity testing for rational series via minimal matrices is explicitly recalled by Clemente~\cite[Introduction]{C25}; his Theorem~1 extends decidability to effective prevarieties. His later work~\cite{C26} classifies bilinear associative commutative products of series and establishes equivalence decidability for the corresponding polynomial automata. These are distinct from deciding existence of a copyless realization. We use established minimization, commutator and trace tests; the realizability transfer is what makes them decide copylessness in the sector of Theorem~\ref{thm:characterization}. Minimization for linear and affine CRA~\cite{BLR24} likewise concerns a different restriction. The contribution asserted here is the minimum-rank observable compression, its commuting-unipotent obstruction, and the finite-control transfer retaining the entire minimal algebra. No general CCRA-membership algorithm, positive-characteristic extension or polynomial-size synthesis from arbitrary compact weighted representations is asserted.

'''
pre=old[old.index('\\section{Models, pumping, and minimal representations}'):old.index('\\section{A retraction')]
pre=pre.replace('It is reachable if the columns $B_w o$ span its space, observable if the rows $\\lambda B_w$ span its dual, and minimal if both conditions hold.', 'It is minimal if the rows $\\lambda B_w$ span its dual and the columns $B_w o$ span its space.')
core=old[old.index('\\section{A retraction'):old.index('\\section{The uniform pumping')]
# The obstruction is now an internal structural theorem, stated at its proof.
core=core.replace('\\begin{proof}[Proof of Theorem~\\ref{thm:obstruction}]',r'''\begin{theorem}\label{thm:obstruction}
If the minimal weighted letter matrices of a one-state polynomial $\Q$-CCRA are unipotent, they commute pairwise.
\end{theorem}
\begin{proof}''')
extension=r'''
\section{Finite control and the full minimal algebra}\label{sec:control}
We prove the difficult implication of Theorem~\ref{thm:characterization}. Suppose a finite-state $\Q$-CCRA recognizes a nonzero all-word-unipotent function, with minimal representation $(\lambda,(M_a)_a,\gamma)$ of dimension $d$. Let $\mathcal A$ be the unital algebra generated by its letter matrices.

Choose a reachable bottom strongly connected component $C$ of the complete control graph. Words act as transformations of this nonempty closed set. Choose a word $t$ with smallest image size $r\geq1$. Its square has the same rank, so $t$ permutes its image. With $N=r!$, the word $e=t^N$ has image $R$ of size $r$ and fixes every element of $R$. Empty words cause no exception.

For each letter $a$, the transformation of $eae$ has image contained in $R$. Its image on $R$ equals its image on $C$, since the first $e$ maps $C$ onto $R$ and fixes $R$. Minimum rank forces that image to have size $r$. Thus $eae$ permutes $R$, and
\[
 h_* =e,\qquad h_a=(eae)^N
\]
all fix every state of $R$. Choose $q\in R$ and an actual prefix $p$ reaching it. Composed updates along these return blocks, the valuation after $p$, and the output at $q$ define a one-state CCRA for $g(z)=f(p h(z))$ over the block alphabet. Composition preserves copylessness. Its displayed weighted representation on the original $d$-dimensional space has initial row $\lambda M_p$, final column $\gamma$, and block matrices
\[
 B_*=M_e,\qquad B_a=(M_eM_aM_e)^N.
\]
All these are word matrices and are unipotent. Let $\mathcal B$ be their unital algebra. Clearly $\mathcal B\subseteq\mathcal A$. Conversely,
\[
 M_e^{-1}=\sum_{j=0}^{d-1}(I-M_e)^j\in\mathcal B.
\]
The matrix $U_a=M_eM_aM_e$ is also a word matrix, hence unipotent. The finite root identity~\eqref{eq:root} with exponent $N$ gives
\[
 U_a=\sum_{j=0}^{d-1}\binom{1/N}{j}(B_a-I)^j\in\mathcal B,
 \qquad M_a=M_e^{-1}U_aM_e^{-1}\in\mathcal B.
\]
Therefore $\mathcal A=\mathcal B$. This equality uses all-word unipotence, not just unipotence of the original letters.

The block representation remains minimal. Its observable columns span $\mathcal B\gamma=\mathcal A\gamma=\Q^d$. The matrix $M_p$ is a unit of $\mathcal A$, its inverse being a finite polynomial in $I-M_p$. Hence its reachable rows span
\[
 \lambda M_p\mathcal B=\lambda M_p\mathcal A
   =\lambda\mathcal A=(\Q^d)^*.
\]
The span of monoid words equals the algebra span, so these are the actual two minimality spans of $g$. Theorem~\ref{thm:obstruction} makes the displayed block matrices commute. Their algebra $\mathcal B=\mathcal A$ is commutative, and all original $M_a$ commute. No size bound on the return words is needed: this is an existence proof, and the decision algorithm does not construct the original control graph.

\begin{proof}[Completion of Theorem~\ref{thm:characterization}]
The preceding argument proves (1)$\Rightarrow$(2). For (2)$\Rightarrow$(4), write $M_a=I+N_a$, with $N_a^d=0$, and use commutativity to obtain
\[
 f(w)=\lambda\prod_{a\in\Sigma}
 \left(\sum_{j=0}^{d-1}\binom{|w|_a}{j}N_a^j\right)\gamma.
\]
This is a rational polynomial in the counts. Clearly (4)$\Rightarrow$(3). If (3) holds, for all $u,v,a,b$ we have
\[
 \lambda M_u(M_aM_b-M_bM_a)M_v\gamma=0.
\]
Full reachable and observable spans imply $M_aM_b=M_bM_a$, proving (3)$\Rightarrow$(2). Finally, (4)$\Rightarrow$(1) follows by allocating a separate counter register for every occurrence of a count variable in each expanded monomial. Each register starts at zero, increments on its letter and is otherwise unchanged. Use each register once in its monomial and sum the disjoint products with rational coefficients. Every old register occurs only in its own update and once in the output. Constants require no registers. This proves existence, without a polynomial-size claim for a polynomial expanded from compact matrices. Zero is realized by a constant-zero machine.
\end{proof}

\section{Effective recognition and explicit pattern sums}\label{sec:algorithms}
\subsection{Testing the unipotent sector}
For $d\geq1$, the following universal trace criterion holds:
\begin{equation}\label{eq:trace}
 (\forall w\ M_w\text{ unipotent})
 \quad\Longleftrightarrow\quad
 (\forall w\ \tr(M_w)=d).
\end{equation}
Only the reverse direction needs proof. Fix $w$; the trace condition on $w^j$, $1\leq j\leq d$, gives $\tr(M_w^j)=d$. Newton identities determine the characteristic polynomial to be $(T-1)^d$, and Cayley--Hamilton gives $(M_w-I)^d=0$.

Build the invariant span of $(\vecop(M_w),1)$ in dimension $d^2+1$, starting with $(\vecop(I),1)$ and closing under
\[
 (\vecop(X),c)\longmapsto(\vecop(XM_a),c).
\]
Breadth-first basis closure decides whether the linear functional $\tr(X)-dc$ vanishes on the entire span, which is exactly~\eqref{eq:trace}. Retained basis vectors are actual word vectors, of length at most $d^2$: a plateau in the increasing word-length spans already gives invariance. This is a universal linear-algebra decision, rather than a finite test presumed sufficient without proof. First minimize the supplied representation; an invisible eigenvalue, for example $2$, must not reject a property of the function's minimal action. Handle the zero function separately. If the promise passes, pairwise commutator tests decide realizability by Theorem~\ref{thm:characterization}.

For completeness, these algorithms have polynomial \emph{bit} complexity. Let $n$ and $L$ be the supplied dimension and total binary encoding length. A common denominator for all entries has $O(L)$ bits. Entries of a length-$k$ product have $O(k(L+\log(n+1))+L)$ bits, by scaling to integer matrices and bounding their sums of products. Reachable and observable basis words have length at most $n-1$, and generated candidates have length at most $n$. Coordinate changes and exact rank tests involve minors of polynomial-bit matrices. Hadamard's bound and fraction-free elimination give polynomial bit bounds for minimization and for the resulting matrices. The trace-span basis words have length at most $d^2$, with candidates at most $d^2+1$, so the same bounds apply. There are at most $d^2+1$ retained vectors and polynomially many letter extensions. Commutator testing is also polynomial. This proves Theorem~\ref{thm:decision}; the linear-algebra tools themselves are established ones, as discussed in Section~1.

\subsection{Pattern representations and negative certificates}
For $p=p_1\cdots p_\ell$, take states $0,\ldots,\ell$ and matrices
\[
 T_a=I+\sum_{i:p_i=a}E_{i-1,i},
 \qquad\lambda=e_0^{\mathsf T},\quad\gamma=e_\ell.
\]
Here indices start at zero. A run either stays put or advances one edge on an input letter; even for adjacent repeated pattern letters it cannot advance twice in one step. Thus it counts exactly $[w:p]$. Direct sums, with each initial row scaled by $c_p$, give a representation of dimension $D$. All word matrices are upper unitriangular. Unipotence descends to the minimal invariant subquotient, including under cancellations. Theorem~\ref{thm:characterization} therefore applies.

For an explicit algorithm, minimization is unnecessary. Build bases of reachable rows $r=\lambda T_u$ and observable columns $c=T_v\gamma$, retaining word vectors with $|u|,|v|\leq D-1$. Test
\[
 r(T_aT_b-T_bT_a)c
\]
for all basis rows, basis columns and letters. A nonzero scalar returns the words $uabv,ubav$, with distinct values and lengths at most $2D$. If all vanish, bilinearity gives invariance under adjacent swaps in every context. These generate all permutations, so the answer is YES. A zero row or column span is YES.

Let $B$ be the coefficients' total binary length. Entries of word matrices of length $k$ count embeddings and are at most $2^k$; row entries multiply these by a single input coefficient. A common denominator has $O(B)$ bits. Retained vectors and their candidates use words of length at most $D$, hence have $O(B+D)$-bit entries. Their minors have $O(D(B+D+\log(D+1)))$ bits. Fraction-free elimination and polynomially many scalar tests give polynomial bit time, including for discarded dependent candidates.

\subsection{Positive synthesis without polynomial expansion}
Order the alphabet. On a YES instance, $f(w)=f(\operatorname{sort}(w))$. A nondecreasing pattern $p$ has
\[
 \prod_a\binom{|w|_a}{m_{p,a}},\qquad m_{p,a}=|p|_a,
\]
embeddings into the sorted word; an unsorted pattern has none. Thus this formula can be applied term by term despite negative coefficients or cancellations.

For each nondecreasing listed pattern $p$, letter $a$ and $0\leq j<m_{p,a}$, allocate a distinct register $x_{p,a,j}$ initially $-j$. Increment it on $a$ and leave it unchanged otherwise. Output
\begin{equation}\label{eq:synthesis}
 \sum_{p\ \mathrm{nondecreasing}}
 \frac{c_p}{\prod_a m_{p,a}!}\prod_{a,j}x_{p,a,j}.
\end{equation}
The falling-factorial identity proves correctness, also when a count is smaller than its required multiplicity. Empty products handle empty patterns. Every register occurs only in its own update and in one output product, making the entire expression syntactically copyless. There are at most $\sum_p|p|$ registers, polynomially many update entries and operands, and factorial denominators have $O(D\log(D+1))$ bits. Zero coefficients or repeated patterns cause no difficulty. Empty alphabets have only the empty pattern; the output is constant. This completes Theorem~\ref{thm:patterns}.

'''
pumping=old[old.index('\\section{The uniform pumping'):old.index('\\section{Return words')]
end=r'''
\begin{proof}[Completion of Theorem~\ref{thm:main}]
All word matrices of the displayed realization are unipotent, and this remains true in its minimal subquotient. Yet $f(01)=2$ and $f(10)=1$, so the function is not permutation-invariant. Theorem~\ref{thm:characterization} excludes every finite-state polynomial $\Q$-CCRA. Equivalently, the identity
\[
 f(w)=[w:1]+[w:01]+[w:11]
\]
follows by counting each $1$ and every preceding position, and Theorem~\ref{thm:patterns} supplies the same conclusion. Together with the uniform calculation above, this disproves sufficiency of the original condition over fields, using its proposed rational witness.
\end{proof}

\paragraph{Limits and computational evidence.}
The universal arguments above allow singular, reset, merge and nonlinear updates and make no inference from minimal invertibility to physical invertibility. Characteristic zero is used in finite unipotent roots. General CCRA membership outside the all-word-unipotent sector remains outside the claim, as does efficient synthesis from arbitrary compact weighted matrices. Exact rational diagnostics checked singular nonlinear transformations and observable quotients, finite controls, unipotent root recovery, signed pattern sums, synthesized machines and negative certificates. These are supporting finite checks, not substitutes for any universal proof. The stated certificate and complexity bounds follow from the mathematical arguments.

\paragraph{AI assistance.}
OpenAI Codex materially assisted proof development, primary-source comparison, exact-arithmetic diagnostics, and writing and typesetting throughout. The minimum-output route originated in supplied research material. Separate Codex contexts reconstructed the arguments and performed further exact checks; these are internal checks, not external peer review or formal verification. The text and proofs include substantial AI-generated content. No claim of human-only derivation or independent human verification is made.

\renewcommand{\bibfont}{\normalfont\normalsize}
\bibliographystyle{ACM-Reference-Format}
\bibliography{references}
\end{document}
'''
(root/'manuscript/main.tex').write_text(head+pre+core+extension+pumping+end)
with (root/'manuscript/references.bib').open('a') as f:
 f.write(r'''
@inproceedings{C25,
 author={Clemente, Lorenzo},
 title={The Commutativity Problem for Effective Varieties of Formal Series, and Applications},
 booktitle={2025 40th Annual ACM/IEEE Symposium on Logic in Computer Science (LICS)},
 pages={804--817}, year={2025}, publisher={IEEE},
 doi={10.1109/LICS65433.2025.00066},
 note={Full version arXiv:2503.21697v2}, url={https://arxiv.org/abs/2503.21697v2}
}
@inproceedings{C26,
 author={Clemente, Lorenzo}, title={Commutative Algebras of Series},
 booktitle={41st Annual Symposium on Logic in Computer Science (LICS 2026)},
 series={Leibniz International Proceedings in Informatics (LIPIcs)},
 volume={380}, pages={29:1--29:23}, year={2026},
 publisher={Schloss Dagstuhl -- Leibniz-Zentrum f{\"u}r Informatik},
 doi={10.4230/LIPIcs.LICS.2026.29},
 url={https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.LICS.2026.29}
}
@inproceedings{BLR24,
 author={Benalioua, Yahia Idriss and Lhote, Nathan and Reynier, Pierre-Alain},
 title={Minimizing Cost Register Automata over a Field},
 booktitle={49th International Symposium on Mathematical Foundations of Computer Science (MFCS 2024)},
 series={Leibniz International Proceedings in Informatics (LIPIcs)},
 volume={306}, pages={23:1--23:15}, year={2024},
 publisher={Schloss Dagstuhl -- Leibniz-Zentrum f{\"u}r Informatik},
 doi={10.4230/LIPIcs.MFCS.2024.23},
 url={https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2024.23}
}
''')
source_files=['manuscript/main.tex','manuscript/references.bib','manuscript/latexmkrc']+[str(p) for p in sorted((root/'manuscript/vendor').iterdir()) if p.is_file()]
(root/'publication.json').write_text(json.dumps({'source_files':source_files,'pdf':'manuscript/build/main.pdf','author_metadata':'authors.json','kind':'resolution-paper'},indent=2)+'\n')
(root/'checkpoint.md').write_text('''# Revision 2 writing checkpoint (in progress)\n\nJob c021-ccrapumping-write-f8f9e1107e7a. The current frozen combined claim passes check-math; the fresh report audit/math.md and innovation.json accept full original-scope resolution and the substantive unipotent-sector extension. Mathematical evidence, source.md, counters, usage and prior history remain unchanged. The earlier research checkpoint is preserved in evidence/write-v2/checkpoint-before-write.md.\n\nA single manuscript is being prepared from the accepted core and extension, using unmodified official acmart inputs, the sole author in authors.json, and complete proofs. No separate marginal paper is created. No Excel bibliography was designated. Current primary source records and STOC 2027 format/anonymity have been checked; the current CFP specifies named authors, 11pt single column, letter paper and one-inch margins. The user limit remains 12 total pages.\n\nNext test: clean-compile the combined article, verify total pages, equations, citations and every rendered page, then freeze the final source/PDF for separate release review.\n''')
print(json.dumps({'tex_words':len((head+pre+core+extension+pumping+end).split()),'source_sha256':hashlib.sha256((root/'source.md').read_bytes()).hexdigest(),'inputs':len(source_files)}))
