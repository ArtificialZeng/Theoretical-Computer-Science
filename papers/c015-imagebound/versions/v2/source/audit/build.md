# Fresh build review

Job: c015-imagebound-release-2bbd673a9c35. Verdict: accept. Label retained: working_paper.

Read the existing complete compiler log `manuscript/c015-imagebound-write-b795278c1e36/working_paper.log`, BibTeX log and recorder, and independently compiled all ZIP-listed sources in a previously empty `evidence/c015-imagebound-release-2bbd673a9c35/portable-build/` directory using latexmk -pdf -jobname=working_paper -interaction=nonstopmode -halt-on-error main.tex. This succeeded (exit 0), without external project-local inputs. The real final logs have no fatal errors, undefined references/citations, LaTeX/package/class warnings, overfull or underfull boxes. BibTeX used exactly three entries and issued zero warnings.

The rebuilt BBL and complete extracted text equal the frozen version. A fresh 125-dpi render of every rebuilt page equals the corresponding inspected original PNG byte-for-byte. PDF bytes differ because this is a fresh compiler run; the active frozen PDF was never replaced. Reproduction is a build/presentation check, not a mathematical test. `evidence/c015-imagebound-release-2bbd673a9c35/portable-build-results.json` and page-comparison.json record the comparisons. The generated source ZIP is `evidence/c015-imagebound-release-2bbd673a9c35/working_paper_sources.zip`; it is an auxiliary reproduction artifact, not an activated deliverable.

The active PDF has six nonempty, selectable-text letter-size pages (612 by 792 points), below the user's twelve-total-page cap. All fifteen font subsets are embedded. The title metadata agrees with the manuscript; displayed sole author/contact agree with authors.json. The PDF is unencrypted and contains no JavaScript. Layout is single-column 11pt with one-inch margins, and the separate title page carries the sole named author. The official current STOC 2027 CFP permits named authors and requires this basic format. Numeric ACM references are allowed, although the CFP expresses a preference for alphanumeric labels. Substantial AI use is explicitly disclosed on page 6.

The official acmart.cls and ACM-Reference-Format.bst compare byte-for-byte equal to the supplied official distribution. No source, frozen mathematical evidence or active PDF was modified. No external submission/contact occurred. Actual check-math passed; release still depends on the fresh final gate.

Original log SHA-256: 9b30eadcee993d979938d5ee5b6b60e927b74b70f143ce35010875740feef605
Snapshot: cb1b52760e44f40d39212ae4e2487e31dff8bbdea70ba237a86a02d321ed9f7e
Manuscript: 0b0a26f7526dc9b1387c6717bfb131d92f985b87e259fd50d4c89f0e27da96de
PDF: b2c1af7888a6e47966549882d4c977cefcaf4527cea394aaf4d57d8b62eabefb
