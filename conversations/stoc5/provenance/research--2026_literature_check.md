# Dated primary-source check for the October 2026 revision

Checked 2026-10-31. PDFs are cached locally under `research/sources/2026/`; the source package records their URLs and hashes rather than redistributing third-party papers.

| Key | Exact primary version | Verified theorem/model used |
|---|---|---|
| alman2026 | https://arxiv.org/abs/2610.06783v1 | Theorem 2: deterministic O(n^2.9995) APSP on graphs without negative cycles and the same min-plus bound; word RAM, polynomially bounded integer inputs. The min-plus form is used for global negative-cycle reporting. |
| karingula2026 | https://arxiv.org/abs/2610.15663v1 | Corollary 1.2: deterministic truly subcubic APSP, no negative cycles, polynomial integer weights; weaker saving, no invented matching exponent. |
| majdoddin2026 | https://arxiv.org/abs/2610.17420v1 | Corollary D / Corollary 16.1: deterministic n^(2.99450+o(1)) min-plus/APSP for each fixed polynomial magnitude bound. Cited as a reported preprint guarantee. |
| saha2026 | https://arxiv.org/abs/2610.20297v1 | Theorem 1.3: deterministic soft-O(n^2.9963432) min-plus. The manuscript rounds conservatively to soft-O(n^2.9964). Theorem 1.1 is the separate Las Vegas statement. |

The manuscript's transfer proof uses only the above algorithm interfaces and known normalization. It does not claim independent validation of the complete proofs of these preprints or peer-review acceptance. The old universal cubic APSP-hypothesis interpretation has been withdrawn from current claims.
