# Fixed extraction for affected release
Advisory citation-check-skill invoked. Extraction pass only. Verification is a separate later pass. Autonomous bounded release was already authorized.

[C01] | Attribution / Existence / exact mathematical statement | main.tex line 1

\documentclass[manuscript,11pt,screen,nonacm]{acmart}
\geometry{letterpaper,margin=1in,heightrounded=false,headheight=14pt,footskip=24pt}
\fancypagestyle{submission}{\fancyhf{}\fancyfoot[C]{\normalfont\normalsize\thepage}
  \renewcommand{\headrulewidth}{0pt}\renewcommand{\footrulewidth}{0pt}}
\setcopyright{none}
\settopmatter{printacmref=false,printccs=false,printfolios=true}
\acmDOI{}\acmISBN{}\acmVolume{}\acmNumber{}
% This is an unsubmitted manuscript. Keep the official class unchanged,
% and disable hyperxmp's automatic ACM publisher/journal inference.
\makeatletter\let\hyxmp@parse@acmart\relax\makeatother
\hypersetup{keeppdfinfo=true,colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue,
 pdftitle={Certified Expected-Cost Optimization for Robust Ski Rental},
 pdfauthor={Zijian Zeng, Jiayin Cao, Weinan Dai, Rui Wang, Fei Ding},
 pdfpublisher={},pdfpubtype={},pdfmetalang={en},
 pdfcontactemail={1002266693@ucsiuniversity.edu.my, 2795820153@qq.com, 21725058@zju.edu.cn, 2002007@nut.edu.cn, dingfei@email.ncu.edu.cn},
 pdfcontactaddress={UCSI University; Ningbo University; Zhejiang University; Nanchang Institute of Technology; Alibaba Group},
 pdfsubject={Robust randomized ski rental with distributional advice},
 pdfkeywords={ski rental, distributional advice, robustness, exact optimization}}
\renewcommand{\bibliofont}{\normalfont\normalsize}
\captionsetup{font=normalsize,labelfont={bf,normalsize},textfont=normalsize}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\DeclareMathOperator{\supp}{supp}
\newcommand{\E}{\mathbb E}
\newcommand{\Q}{\mathcal F}
\newcommand{\Pp}{\mathcal P}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usepackage{algorithm}
\usepackage{needspace}
\title{Certified Expected-Cost Optimization for Robust Ski Rental}
\author{Zijian Zeng}
\affiliation{\institution{UCSI University}\city{}\country{Malaysia}}
\email{1002266693@ucsiuniversity.edu.my}
\author{Jiayin Cao}
\affiliation{\institution{Ningbo University}\city{}\country{China}}
\email{2795820153@qq.com}
\author{Weinan Dai}
\affiliation{\institution{Zhejiang University}\city{}\country{China}}
\email{21725058@zju.edu.cn}
\author{Rui Wang}
\affiliation{\institution{Nanchang Institute of Technology}\city{}\country{China}}
\email{2002007@nut.edu.cn}
\author{Fei Ding}
\affiliation{\institution{Alibaba Group}\city{}\country{China}}
\email{dingfei@email.ncu.edu.cn}
\authorsaddresses{\normalsize\begin{tabular}{@{}ll@{}}
Zijian Zeng & \href{mailto:1002266693@ucsiuniversity.edu.my}{1002266693@ucsiuniversity.edu.my}\\
Jiayin Cao & \href{mailto:2795820153@qq.com}{2795820153@qq.com}\\
Weinan Dai & \href{mailto:21725058@zju.edu.cn}{21725058@zju.edu.cn}\\
Rui Wang & \href{mailto:2002007@nut.edu.cn}{2002007@nut.edu.cn}\\
Fei Ding & \href{mailto:dingfei@email.ncu.edu.cn}{dingfei@email.ncu.edu.cn}
\end{tabular}\spacefactor=3000}
\date{}
\begin{document}
\singlespacing
\begin{abstract}
\normalsize
We study discrete ski rental with integer purchase cost $b\ge2$, a finite
rational forecast of season length, and a prescribed expected competitive
ratio at every actual integer horizon. We give an exact algorithm that
minimizes forecast expected cost and returns matching primal and dual
certificates on the unbounded horizon and buy-day domains. It uses a
triangular prefix optimization, normalizes the policy by increasing a dual
price, and recovers the robustness constraint through one moment price.
An optimum needs at most $b+1$ buy-days, including at most two days at or
after $b$. For the uniform forecast on $\{1,\ldots,b\}$, we derive all $b$
affine decreasing pieces of the value frontier and its constant continuation,
prove uniqueness up to robustness two, and show that both support bounds
are sharp. The underlying capped-geometric policy is credited to prior
one-hot-forecast work. An exact example separates expected-cost optimization
from a published minimum-support-level inference; a pinned software
reproduction gives a third, distinct value. The algorithm has polynomial
bit time in numerical $b$ and the binary input length.
\end{abstract}
\hypersetup{pageanchor=false}
\maketitle
\hypersetup{pdftitle={Certified Expected-Cost Optimization for Robust Ski Rental},
 pdfauthor={Zijian Zeng, Jiayin Cao, Weinan Dai, Rui Wang, Fei Ding},
 pdfpublisher={},pdfpubtype={},pdfsubject={Robust randomized ski rental with distributional advice},
 pdfkeywords={ski rental, distributional advice, robustness, exact optimization}}
\enlargethispage{-12pt}\thispagestyle{empty}\clearpage
\setcounter{page}{1}\hypersetup{pageanchor=true}\pagestyle{submission}

[C02] | Attribution / Existence / exact mathematical statement | main.tex line 109

A small example explains why the choice of objective matters. At $b=3$,
$R=3/2$, and $p=(2/5,3/5)$ on horizons one and two, the global optimum is
$39/20$. Restricting the policy to the smallest feasible level of its raw
support costs instead gives $11/5$. The publisher-linked software, in six
specified calls at one pinned version, returns a law costing $12/5$.
Section~\ref{sec:separation} proves the first two statements and records the
last as a finite software observation. This separates the optimality
inference in Kim and Fan's published Appendix D.2~\cite{pmlr-v306-kim26l}
from both ideal support feasibility and literal implementation behavior.

[C03] | Attribution / Existence / exact mathematical statement | main.tex line 129

A generic rational LP already gives polynomial bit time after the finite
reduction. Our contribution is the explicit construction and its structural
consequences, with the same numerical-$b$ runtime model. In particular, the
moment row contains $t-1$, which may be large when a forecast horizon is
binary encoded; only the prefix block has coefficients bounded by $b$.
Tardos's matrix-dependent arithmetic bound~\cite{Tardos_1986} therefore
does not make this whole matrix small. Arithmetic-step bounds and bit time
are distinct, and we claim neither a strongly polynomial algorithm nor an
asymptotic improvement over general LP.

[C04] | Attribution / Existence / exact mathematical statement | main.tex line 139

\paragraph{Context and closest results.}
Classical rent-or-buy analysis grew from snoopy caching~\cite{Karlin1988};
randomization gives the limiting ratio $e/(e-1)$~\cite{Karlin1994}.
Point-prediction robustness--consistency tradeoffs and LP methods appear in
Purohit, Svitkina and Kumar~\cite{NEURIPS2018_73a427ba} and Wei and
Zhang~\cite{NEURIPS2020_5bd844f1}. Li, Christianson and Li~\cite{Li_2026}
develop prediction-specific Pareto optimization, equalizing distributions
and primal--dual constructions. Their inspected preprint's randomized
strong-optimality statements are asymptotic in $b$.

[C05] | Attribution / Existence / exact mathematical statement | main.tex line 149

The nearest model is Kim and Fan~\cite{pmlr-v306-kim26l}. We use their
Lemma 5.1 robustness reduction and credit their geometric and gap
recurrences. The uniform policy below coincides with their Theorem C.1(ii) in Appendix C.4
one-hot-$b$ optimizer when $R-1\le1-1/b$, and is another one-hot-$b$ optimum
above that cut. The uniform contribution is its expected-objective frontier
and uniqueness analysis, with this underlying policy structure retained.

[C06] | Attribution / Existence / exact mathematical statement | main.tex line 156

Distributional learning~\cite{pmlr-v139-diakonikolas21a} combines a learned
policy with a robust baseline and does provide per-instance guarantees;
we optimize exactly at each supplied $p,R$. Besbes, Ma and
Mouchtaki~\cite{Besbes_2025} use heterogeneous data and known-radius
shift to study additive regret. Cui and Dinitz~\cite{pmlr-v306-cui26a}
consider unknown Wasserstein prediction error and additionally interpolate
with robustness. Their benchmark is a policy knowing the true distribution.
Khanafer, Kodialam and Puttaswamy~\cite{Khanafer_2013} use horizon-moment
information; our moment is instead a property of the buying-day law.
Tail-risk constraints~\cite{Dinitz_2024,10.1007/978-3-032-06706-7_6}
bound the probability of a large realized ratio, while here an expected-ratio
cap is fixed at each horizon. Hartline, Johnsen and
Shah~\cite{hartline_et_al:LIPIcs.ITCS.2026.75} study finite binary-weather
sequences, with a distribution-knowing benchmark in their prior-independent
analysis and a separate subgame-optimality criterion.

[C07] | Attribution / Existence / exact mathematical statement | main.tex line 172

Set $a=b-1$, $r=R-1$, $K=rb$, and
\begin{equation}\label{eq:S}
 S=\{1,\ldots,b\}\cup\{d+1:p_d>0,\ d\ge b\}.
\end{equation}
\begin{theorem}\label{thm:main}
For every input above, the explicit algorithm in Sections~\ref{sec:oracle}
and~\ref{sec:price} returns an expected-cost minimizing robust law $f$,
supported on $S$, with at most two support days $t\ge b$ and at most $b+1$
support days in all. It returns rational $\lambda\ge0$, $y_x\ge0$ for
$1\le x<b$, and $\alpha\in\mathbb Q$ such that
\begin{align}
 g(t)+\lambda(t-1)+\sum_{x=t}^{b-1}(b+t-1-x)y_x&\ge\alpha
           &&(t\ge1),\label{eq:certificate}\\
 J_p(f)&=\alpha-r\sum_{x=1}^{b-1}xy_x-\lambda K.\label{eq:equality}
\end{align}
Empty sums are zero. Let $q_R$ be the denominator of $R$, $q_p$ the least
common multiple of the probability denominators, and
\begin{equation}\label{eq:bound}
 D=b!b^b,\qquad H=q_pq_RD,\qquad L=b+\max S,\qquad Z=2LH^4.
\end{equation}
After computing $g$ on $S$, the algorithm uses $O(\log Z)$ calls to an
$O(b^2+|S|)$ rational-operation oracle. All intermediate bit lengths and
the total bit time are polynomial in numerical $b$ and binary input length.
\end{theorem}

[C08] | Attribution / Existence / exact mathematical statement | main.tex line 197

Figure~\ref{fig:pipeline} shows how the two prices separate normalization
from robustness. The resulting certificates can be checked using the
prefix constraints, one moment, and finitely many inequalities on $S$.
\begin{figure}[ht]
\centering
\begin{tikzpicture}[>=Stealth,every node/.style={font=\normalsize},
 box/.style={draw,rounded corners,align=center,inner sep=5pt}]
\node[box] (g) at (0,0) {$g$ on $S$};
\node[box] (pre) at (2.7,0) {Prefix elimination\\normalization price $\alpha$};
\node[box] (price) at (6.3,0) {Moment price $\lambda$\\exact bisection};
\node[box] (mix) at (10.2,0) {Policy mixture\\primal/dual certificate};
\draw[->] (g)--(pre);\draw[->] (pre)--(price);\draw[->] (price)--(mix);
\end{tikzpicture}
\caption{The normalized prefix oracle is called at adjusted costs
$g(t)+\lambda(t-1)$; the final mixture enforces the moment cap.}
\Description{Forecast costs enter the normalized prefix oracle, then moment-price bisection, then an optimal mixture and its dual certificate.}
\label{fig:pipeline}
\end{figure}

[C09] | Attribution / Existence / exact mathematical statement | main.tex line 223

The published Appendix D.2, printed page 30, states:
\begin{quote}
``Therefore the optimal objective value equals the minimum feasible h,
which can be found by binary search.''
\end{quote}
Here $h$ is the raw support level, not a dual-adjusted expected objective.
The following example refutes that inference in the published model
\cite{pmlr-v306-kim26l}; it also applies to the corresponding arXiv v1 passage.

[C10] | Attribution / Existence / exact mathematical statement | main.tex line 232

\Needspace{12\baselineskip}
\begin{proposition}\label{prop:separation}
For $b=3$, $R=3/2$, $p_1=2/5$, $p_2=3/5$, the global expected-cost
minimum is $39/20$, whereas $h_*=14/5$ and the unique feasible law at this
minimum support level has expected cost $11/5$.
\end{proposition}
\begin{proof}
Direct summation gives $g=(3,14/5,8/5,8/5,\ldots)$.
Robustness implies $\mu(f):=\E(T-1)\le3/2$, as proved in Section~\ref{sec:reduction}.
For all $t\ge1$, $g(t)+(7/10)(t-1)\ge3$, with equality only at 1 and 3.
Hence $J_p(f)\ge39/20$. The law $(f_1,f_3)=(1/4,3/4)$ attains this bound.
Its costs at actual horizons 1, 2 and $x\ge3$ are $3/2,9/4,9/2$, so it is robust.
Below level $14/5$, all allowed days are at least 3 and have moment at least 2.
At level $14/5$, $f_1=0$. The horizon-two constraint gives $2f_2\le1$,
while $\mu\ge2-f_2$. The cap forces $f_2=1/2$ and all remaining mass at
3. This robust law has $J_p=11/5$, proving the assertions.
\end{proof}

[C11] | Attribution / Existence / exact mathematical statement | main.tex line 250

\begin{table}[ht]
\centering\normalsize
\caption{Three distinct quantities for Proposition~\ref{prop:separation}.
The last column is the raw support objective $H(f)$ whose minimum is $h_*$.
The software row is a finite observation; the other two rows are exact optima.}
\label{tab:separation}
\begin{tabular}{lcccc}
\toprule
Meaning & $(f_1,f_2,f_3)$ & $J_p$ & $\mu$ & $H(f)$\\
\midrule
Global expected-cost optimum & $(1/4,0,3/4)$ & $39/20$ & $3/2$ & $3$\\
Minimum support-level law & $(0,1/2,1/2)$ & $11/5$ & $3/2$ & $14/5$\\
Pinned software output & $(1/4,3/8,3/8)$ & $12/5$ & $9/8$ & $3$\\
\bottomrule
\end{tabular}
\end{table}

[C12] | Attribution / Existence / exact mathematical statement | main.tex line 267

\paragraph{Published software observation.}
We executed the unchanged \texttt{SkiRentalOptimizer} class in both
optimizer files supporting Figure 1 and Table 2 in the publisher-linked
repository. The exact pinned version, file hashes and calls are supplied
in the reproduction supplement.
For constructor arguments $(3,1.5,[1,2],[.4,.6])$ and tolerances
$10^{-5},10^{-9},10^{-12}$, all six calls returned the last law in
Table~\ref{tab:separation}, at levels approximately 3. Both classes rejected
$14/5$ and accepted 3 in the documented feasibility calls. At level 3 the
construction temporarily assigns day-three mass $9/16$, reaching internal
mass $19/16$, before its existing correction leaves $3/8$. Evaluating the
returned law in the original model gives moment $9/8$ and horizon costs
$3/2,3,33/8$ at $1,2,x\ge3$, respectively. Thus the policy is robust and
costs $12/5$. These calls concern the pinned files and tolerances; the
support-level counterexample holds independently of their numerical behavior.

[C13] | Attribution / Existence / exact mathematical statement | main.tex line 283

\paragraph{A different normalization changes the optimum.}
Dividing $J_p$ by the fixed $\E_p\min(X,b)$ preserves all optimizers.
In contrast, for $b=3,R=3/2,p_1=p_2=1/2$, define
$k(t)=\E_p[C_t(X)/\min(X,b)]$. Here
$g=(3,5/2,3/2,\ldots)$ and $k=(9/4,3/2,1,\ldots)$.
The global inequalities
\[
 g(t)+\tfrac34(t-1)\ge3,\qquad
 k(t)+\tfrac12(t-1)\ge2
\]
are equalities only on $\{1,3\}$ and $\{2,3\}$, respectively.
Together with $\mu\le3/2$, they prove unique optimal laws
$(f_1,f_3)=(1/4,3/4)$ for $J_p$, value $15/8$, and
$(f_2,f_3)=(1/2,1/2)$ for $\E_f k(T)$, value $5/4$.
Both laws satisfy the prefix rows. Their cross-objective values are
$21/16$ and $2$, respectively.

[C14] | Attribution / Existence / exact mathematical statement | main.tex line 300

\section{Robustness and finite support}\label{sec:reduction}
Expanding the expected cost gives
\[
 \E C_T(x)=x+\sum_{t\le x}(t-1)f_t+(b-x)\sum_{t\le x}f_t.
\]
For each fixed $t$, the cost is nondecreasing in $x$ and converges to
$b+t-1$. Monotone convergence shows that~\eqref{eq:robust} implies
$\mu(f):=\E(T-1)\le K$. Conversely, this moment bound and the $a$ prefix
inequalities
\begin{equation}\label{eq:prefix}
 \sum_{t\le x}(a+t-x)f_t\le rx,\qquad 1\le x\le a,
\end{equation}
imply~\eqref{eq:robust}: the displayed inequalities cover $x<b$, and
$\E C_T(x)\le b+\mu(f)\le Rb$ covers $x\ge b$.
This is the robustness reduction of~\cite[Lemma 5.1]{pmlr-v306-kim26l}.

[C15] | Attribution / Existence / exact mathematical statement | main.tex line 316

For $t\ge b$, let $s$ be the largest member of $S\cap[b,\infty)$ not
exceeding $t$. No positive forecast atom lies in $[s,t-1]$, so
\begin{equation}\label{eq:dominance}
 g(t)-g(s)=(t-s)\Pr_{X\sim p}[X\ge t]\ge0.
\end{equation}
Moving mass from $t$ to $s$ decreases its moment, preserves every prefix
constraint, and does not increase its objective. The same dominance holds
for $g(t)+\lambda(t-1)$ when $\lambda\ge0$.
This elementary reduction extends the point-prediction support principle
of~\cite[Appendix E.1, arXiv v1]{li2025predictionspecificdesignlearningaugmentedalgorithms}.

[C16] | Attribution / Existence / exact mathematical statement | main.tex line 374

For $B=\{s_1<\cdots<s_k\}\subseteq[a]$, write $v(B)$ for the prefix
schedule supported on $B$ with the prefix constraints tight at those days.
With $s_0=F_0=0$, subtracting consecutive tight constraints gives
\begin{equation}\label{eq:gap}
 v(B)_{s_j}=\frac{s_j-s_{j-1}}a(r+F_{j-1}),\qquad
 F_j=r\left[\prod_{\ell=1}^j
       \left(1+\frac{s_\ell-s_{\ell-1}}a\right)-1\right].
\end{equation}
Here $F_j$ is the accumulated mass. The geometric and gap updates
are those of~\cite[Appendix D.3--D.4]{pmlr-v306-kim26l}.
These schedules are feasible in $\Pp$ but can have mass above one.
Inserting an active day strictly increases the mass: splitting a gap
$u+v$ replaces $1+(u+v)/a$ by
$(1+u/a)(1+v/a)=1+(u+v)/a+uv/a^2$; appending a day adds a factor greater
than one.

[C17] | Attribution / Existence / exact mathematical statement | main.tex line 427

\begin{algorithm}[ht]
\caption{Normalized prefix sweep: costs $c$ on $S$; output $f,\alpha,y$.}
\label{alg:sweep}
\begin{enumerate}
\item Choose a cheapest tail day $t_\star\ge b$. Set $B=\varnothing$ and
$\alpha=\min(c_{t_\star},c_1,\ldots,c_a)$.
\item Add all zero-slack inactive days to $B$; use~\eqref{eq:y} to update
$y$. Let $v_-,v_+$ be the schedules before and after this event, with
masses $m_-,m_+$.
\item If $m_-<1\le m_+$, return the zero-tail law
\begin{equation}\label{eq:massmix}
 f=(1-\eta)v_-+\eta v_+,\qquad \eta=(1-m_-)/(m_+-m_-).
\end{equation}
\item If $\alpha=c_{t_\star}$, fill $1-m_+$ at $t_\star$ and return.
Otherwise advance to the smaller of $c_{t_\star}$ and the next inactive
root $\alpha+\sigma_i/\delta_i$, then repeat from step 2.
\end{enumerate}
\end{algorithm}
At activation, all added dual coordinates are zero, so the old dual
coordinates and current slacks remain unchanged. Activating simultaneous
zero slacks together fixes the convention for ties, including an activation
at the tail cap. The crossing test precedes tail filling.

[C18] | Attribution / Existence / exact mathematical statement | main.tex line 450

\begin{lemma}\label{lem:oracle}
The sweep returns a minimizer of $\sum_{t\in S}c_tf_t$ on $\Q$,
attaining~\eqref{eq:oracledual}, with at most one tail day. It takes
$O(b^2+|S|)$ rational operations.
\end{lemma}
\begin{proof}
At a mass crossing both $v_-$ and $v_+$ minimize the unnormalized prefix
problem at the activation price. Every positive old $y_i$ corresponds to
a tight constraint in both schedules, and new $y_i$ equal zero. Their
mixture~\eqref{eq:massmix} is prefix feasible, has mass one, and attains
the normalized dual bound. When the tail cap is reached first, $v(B)$
attains the prefix bound and the remaining mass has cost exactly $\alpha$,
again giving equality. Positivity of the speeds and strict mass increase establish termination.

[C19] | Attribution / Existence / exact mathematical statement | main.tex line 487

\begin{figure}[ht]
\centering
\begin{tikzpicture}[x=.85cm,y=.65cm,>=Stealth,
 every node/.style={font=\normalsize}]
\draw[->] (0,.1)--(6.6,.1) node[right] {$\lambda$};
\draw[->] (0,.1)--(0,5.3) node[above] {$q(\lambda)$};
\draw[densely dashed,gray] (0,.7)--(6,4.9);
\draw[densely dashed,gray] (0,1.9)--(6,3.7);
\draw[very thick,blue] (0,.7)--(3,2.8)--(6,3.7);
\draw[dashed] (2.1,.1)--(2.1,2.17);
\draw[dashed] (3.9,.1)--(3.9,3.07);
\draw[dotted] (3,.1)--(3,2.8);
\fill[blue] (3,2.8) circle[radius=2pt];
\node[below] at (2.1,.1) {$\lambda_-$};
\node[below] at (3,.1) {$\kappa$};
\node[below] at (3.9,.1) {$\lambda_+$};
\node[anchor=west,align=left] at (7,4.1)
 {$\ell_-(\lambda)=J_p(f_-)+\lambda\mu(f_-)$\\$\mu(f_-)>K$};
\node[anchor=west,align=left] at (7,2.2)
 {$\ell_+(\lambda)=J_p(f_+)+\lambda\mu(f_+)$\\$\mu(f_+)\le K$};
\end{tikzpicture}
\caption{Local schematic around the isolated price $\kappa$. The blue lower
envelope changes from the higher-moment policy to the lower-moment policy;
both are optimal at the intersection. The dashed verticals show the bracket.}
\Description{Two affine policy lines intersect at kappa. Their concave lower
envelope has a larger slope on the left than on the right. Bracket endpoints
lambda minus and lambda plus lie on the two sides of the intersection.}
\label{fig:envelope}
\end{figure}

[C20] | Attribution / Existence / exact mathematical statement | main.tex line 517

\begin{lemma}\label{lem:isolation}
With $Z$ from~\eqref{eq:bound}, price $Z+1$ supplies a right endpoint.
After $O(\log Z)$ bisection steps the bracket contains a common optimal
price for both stored policies, recoverable exactly from their costs and
moments.
\end{lemma}
\begin{proof}
A vertex of $\Q$ has at most $b$ positive coordinates. Its coordinates
are obtained from normalization and independent tight prefix rows, with
integer coefficients of magnitude at most $b$. Their determinant has
absolute value at most $D=b!b^b$. Cramer's rule gives a common coordinate
denominator $q_R|\det|$. Its objective and moment therefore each have
denominator at most $H$, and lie in $[0,L]$.

[C21] | Attribution / Existence / exact mathematical statement | main.tex line 569

\begin{algorithm}[ht]
\caption{Exact moment-price recovery; $Z$ is defined in~\eqref{eq:bound}.}
\label{alg:price}
\begin{enumerate}
\item Run Algorithm~\ref{alg:sweep} at $\lambda=0$. If $\mu\le K$, return
this policy and its dual. Otherwise store it as $f_-$ at $\lambda_-=0$.
\item Store the output at $\lambda_+=Z+1$ as $f_+$.
While $\lambda_+-\lambda_-\ge1/Z^2$, query the midpoint price.
If its moment exceeds $K$, replace the left endpoint; otherwise replace
the right endpoint.
\item Recover $\kappa,\theta,f$ by~\eqref{eq:recover}. Run the sweep at
$\kappa$ to obtain its dual and return $f,\kappa,\alpha,y$.
\end{enumerate}
\end{algorithm}

[C22] | Attribution / Existence / exact mathematical statement | main.tex line 659

\begin{theorem}\label{thm:uniform}
For the uniform forecast, $1=r_0>\cdots>r_b=\rho_b-1$.
If $r_j\le r\le r_{j-1}$, the unique optimal law is
\begin{equation}\label{eq:uniformpolicy}
 f_i=rz_i\ (i<j),\qquad
 f_j=\frac{b-r(b+C_{j-1})}{b+1-j},\qquad
 f_{b+1}=1-\sum_{i\le j}f_i,
\end{equation}
with all other masses zero. Adjacent formulas agree at shared endpoints.
Its value on segment $j$ is $m+\lambda_j b+s_jr$.
For $R\ge2$, day $b+1$ alone is optimal with value $m$.
The value has exactly $b$ strictly decreasing affine pieces followed by
this plateau. The shared frontier representation, a single policy/value
query, and a dual query each take $O(b)$ rational operations; every rational
uses $O(b\log b+\operatorname{len}(R))$ bits.
For $r_b<r<r_{b-1}$, all $b+1$ masses on $\{1,\ldots,b+1\}$ are positive.
Thus both support bounds of Theorem~\ref{thm:main} are simultaneously sharp.
\end{theorem}

[C23] | Attribution / Existence / exact mathematical statement | main.tex line 678

The capped-geometric law in~\eqref{eq:uniformpolicy} agrees with the known
one-hot-$b$ optimizer in the range described in Section~\ref{sec:intro}.
The plateau's unconstrained forecast behavior also appears in the discrete
Bayesian model of Kang, Park and Fan~\cite{kang2025learningaugmentedskirentaldiscrete}.
We prove the frontier and uniqueness using its forecast-specific dual.

[C24] | Attribution / Existence / exact mathematical statement | main.tex line 753

\begin{figure}[ht]
\centering
\begin{tikzpicture}[x=10cm,y=2.5cm,>=Stealth,every node/.style={font=\normalsize}]
\draw[->] (1.38,1.85)--(2.13,1.85) node[right] {$R$};
\draw[->] (1.38,1.85)--(1.38,3.02) node[above] {$J^*(R)$};
\draw[thick,blue] (1.421052632,2.842105263)--(1.5,2.625)--(1.666666667,2.333333333)--(2,2)--(2.1,2);
\foreach \x/\y in {1.421052632/2.842105263,1.5/2.625,1.666666667/2.333333333,2/2}
  \fill[blue] (\x,\y) circle[radius=1.7pt];
\node[below left] at (1.421052632,1.85) {$27/19$};
\node[below right] at (1.5,1.85) {$3/2$};
\node[below] at (1.666666667,1.85) {$5/3$};
\node[below] at (2,1.85) {$2$};
\node[above right] at (1.421052632,2.842105263) {$54/19$};
\node[above right] at (1.5,2.625) {$21/8$};
\node[above right] at (1.666666667,2.333333333) {$7/3$};
\node[above] at (2.045,2) {$2$};
\end{tikzpicture}
\caption{The exact uniform frontier at $b=3$: three affine pieces and the
plateau. On $27/19<R<3/2$, the unique optimum needs all four buy-days.}
\Description{For purchase cost three and a uniform forecast, the value decreases through the four exact endpoint values shown, then stays constant at two.}
\label{fig:frontier}
\end{figure}

[C25] | Attribution / Existence / exact mathematical statement | main.tex line 776

\paragraph{Further questions.}
Further directions include worst-case bounds on frontier size, direct
structural formulas for arbitrary forecasts, and improved dependence on
numerical $b$. The general-forecast structural frontier is left for future work.
