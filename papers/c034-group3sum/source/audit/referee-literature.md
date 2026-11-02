# Fresh primary-literature comparison

Job: `c034-group3sum-referee-f77368142a77`. Checked 2026-11-02 UTC.
Snapshot: `15a73043f23436b1592a376f95f678e39919b724da29d1fc7773757f6a82f52a`.

The preserved local primary PDF/text and matrix HTML in the frozen snapshot
were read directly at the exact positions reported in `audit/math.md`.
Live primary checks:

1. [Majdoddin, arXiv:2610.17420](https://arxiv.org/abs/2610.17420): submission
   history displayed v1 only, dated 12 October 2026. Nearest group algorithm:
   Theorem 19.17, exponent dividing p^2; target: Open Problem 19.26. Generic
   consequence: Lemma 20.3(d), Lemma 20.4(a), Remark 20.6. The frozen source's
   proposed layer induction is prior motivation, not the candidate's novelty.
2. [Alman and Vassilevska Williams, arXiv:2610.06783v1, Section 4.1](https://arxiv.org/html/2610.06783v1):
   Corollary 26 has N>=D^18, integer inputs of magnitude N^O(1), preprocessing
   O(N^2/D^0.063), and individual query cost O(D^0.437). At most N^2/sqrt(D)
   prescribed positions fit the stated total call bound. Only 0/1 inputs are
   needed here. This directly supports the candidate's actual primitive.
3. [Author's current group README](https://raw.githubusercontent.com/Majdoddin/formal-math/main/groups/README.md):
   still describes the p^2 group theorem. It explicitly does not formalize
   running times. I did not inspect other projects or run its Lean development.
4. [Chan, Itakura, Ma and Yu, arXiv:2610.42012v1](https://arxiv.org/html/2610.42012):
   new primary follow-up dated 30 October 2026. Inspected Theorem 2.3 and its
   hashing proof, and the Section 3 convolution setting. It treats integer sums
   using random-prime residues, affine scrambling and carry-free encodings. It
   supplies no claimed all-bounded-exponent group algorithm, and its integer
   hashing is not a valid homomorphism construction for the candidate's torsion
   inputs. Its stronger integer k-SUM/real-input conclusions are not claimed
   as consequences of this packet.

Fresh query families: `3SUM bounded exponent abelian groups randomized algorithm
Majdoddin`; `3SUM divisor bounded groups`; `2610.17420`; `3SUM abelian groups
exponent algorithm`; `3SUM Z_8 algorithm`; `3SUM bounded exponent randomized`;
`3SUM abelian 2610`; `3SUM torsion algorithm`; `3SUM Majdoddin randomized group`.
Nonprimary results were only search leads, not support for scientific claims.

No primary equivalent resolving the all-M target was found in this bounded
search. No exhaustive citation-network survey or priority certificate is claimed;
unindexed, unpublished and later work remain possible. This limitation is
reported separately from proof correctness and from the venue-quality judgment.
