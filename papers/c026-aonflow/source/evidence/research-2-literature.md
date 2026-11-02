# Research-pass-2 primary-source and dependency check

Job c026-aonflow-research-02dec8252283; checked 2026-11-02 UTC. This is the
researcher's bounded literature check, not a fresh referee report or a proof of
priority. The mathematical proposal is research-2-uniform-copy-resolution.md.

## Version and exact primary passages

* [Bansal--Jambulapati--Saranurak arXiv record](https://arxiv.org/abs/2602.15015)
  still lists v2, 28 April 2026, after v1, 16 February 2026. The local supplied
  v2 text and PDF retain their manifest hashes. Its printed p.4 Theorem 3.1
  permits integral node weights including zero, measures loss by total weight,
  and promises all-demand flow expansion in remaining induced components.
* [Official ICALP 2026 article 22](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.22/LIPIcs.ICALP.2026.22.html)
  independently displays the same Theorem 3.1 and the still-explicit
  Section 5 Conjecture 5.1. Its baseline and proposed throughput interface
  obstacle agree with source.md. These live primary passages support the
  comparison; their existence does not establish scientific priority for us.
* Chekuri--Khanna--Shepherd, *Multicommodity flow, well-linked terminals, and
  routing problems*, STOC 2005, pp.183--192,
  [DOI 10.1145/1060590.1060618](https://doi.org/10.1145/1060590.1060618),
  supplied author text intake/primary/CKS2005-welllinked.txt, printed p.5
  Theorem 3.1 is the general uniform alpha-edge-flow-linked matching-rounding
  statement with unit demand and no congestion augmentation. Its footnote
  explicitly requires strengthened clustering; it is not ignored. Theorem
  3.2 is its general-graph O(log^2 k) AON consequence. Lemma 1.1, printed
  pp.2--3, supplies the earlier path-flow uniformization idea, so that idea
  itself is not claimed as new.
* Chekuri--Khanna--Shepherd, *The All-or-Nothing Multicommodity Flow Problem*,
  SIAM J. Comput. 42(4) (2013), 1467--1493,
  [DOI 10.1137/100796820](https://doi.org/10.1137/100796820), supplied author
  text intake/primary/CKS2013-AON.txt, Section 3.4 pp.1478--1483 was read
  directly, including Lemmas 3.9--3.14 and the final shared-vertex paragraph.
  Its formal Theorem 3.8 is for nice Raecke-tree instances. The proof proposal
  explicitly derives the only tree-dependent common-distribution premise
  from a uniform product flow and checks the corrected topology and exact
  bridge-congestion argument. It does not quote Theorem 3.8 verbatim for an
  input that lacks its tree. Attempts to refresh the two CKS author PDFs via
  the web tool failed (timeout/inaccessibility). The complete hashed local
  supplied primary texts were available and inspected; this is an access
  limitation, not a mathematical counterexample or missing-paper claim.
* [Anand arXiv:2610.17237](https://arxiv.org/abs/2610.17237), v1, 12 October
  2026, and its [full primary HTML](https://arxiv.org/html/2610.17237v1)
  were refreshed. This provides improved flow-expander tools; no AON claim
  was located by a text search for all-or-nothing. The present proposed
  theorem uses BJS's explicit total-integral-weight guarantee, not an
  unsupported k-sensitive substitution into Anand's n-dependent extension.

## Bounded equivalent-result search

Searches included all-or-nothing flow with 2026 approximation, exact Conjecture
5.1 with flow-expander decomposition, near-logarithmic all-or-nothing flow,
terminal copies with all-or-nothing flow, and flow-linked rounding. The official
BJS open-question passage remained the direct primary hit. Chekuri's current
[author publication list](https://chekuri.web.engr.illinois.edu/pub.html) was
also consulted; the arbitrary-demands throughput work listed there is a
different comparison and is not adopted as a congestion-1 theorem here.
No primary result giving this full target was located in this bounded refresh.
Coverage is neither exhaustive nor a priority certificate.

## Precise proposed delta and the nonroutine question

The path-copy preparation and the general uniform CKS rounding theorem are
known. BJS already gives almost-optimal total-integral-weight decomposition.
The proposed additional argument retains OLD unit occurrence bridges while
introducing uniform path copies, applies just ONE fixed integral decomposition,
charges cut paths at their common epsilon amount, and uses the OLD cuts to
turn any feasible unit copy selection into distinct ORIGINAL unit admissions.
An exact small-k branch keeps the remaining integral mass O(k^2) even if n
is enormous. Thus neither inverse fractional mass nor log n survives in the
ratio. This addresses the immutable source's full general-graph, unit-capacity,
congestion-1 algorithmic assertion and improves its recorded O(log^2 k)
baseline to log^(1+o(1)) k.

This is a short composition, and no claim is made that its ingredients or
clustering are independently new. The proposed innovation is the complete
admission-preserving reduction and its full target consequence. A fresh referee
must reject it if the reduction is already implicit/routine or the value is
insufficient under AGENTS.md. A recent explicit conjecture and a correct proof
do not by themselves establish STOC competitiveness. No venue assessment,
acceptance record, PDF or manuscript was created by this research job.
