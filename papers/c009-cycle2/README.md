# A Global Sidorenko Inequality for 2-Subdivided Alternating Cycles

[PDF](paper.pdf) · [Original source ZIP](source.zip) · [Browse source](source/) · [English index](../../README.md) · [中文](../../README.zh-CN.md) · [Deutsch](../../README.de.md) · [Français](../../README.fr.md) · [日本語](../../README.ja.md)

Do two-subdivided alternating cycles satisfy the local tournament Sidorenko property at every length? For Hℓ obtained from an alternating 2ℓ-cycle by subdividing every edge once, the manuscript proves tournament homomorphism density at least 2^(−4ℓ). A skew-symmetric matrix inequality yields the full family, a forcing estimate, and equality characterization. A three-vertex family shows the forcing exponent 4ℓ is optimal.

Scope: **resolution of the stated target**. 6 total PDF pages. Author lists and released files are preserved.

From the repository root:

```sh
python3 scripts/reproduce.py --paper c009-cycle2
python3 scripts/build_pdfs.py --paper c009-cycle2
```

Or run the mathematical checks from a writable copy of `source/`:

```sh
python3 evidence/research_exact.py
python3 audit/referee_verify.py
```

The checks use the Python standard library and verify their documented finite scope. Full proofs are in the manuscript. Original reproduction/build instructions remain inside `source/`. The root scripts run in temporary copies. Citation and local review limitations are preserved in `provenance/` and the archive; they are not external peer review.
