# Build repairs

The initial compile failed because the draft called the natbib-specific citestyle command while selecting natbib=false for standard alphanumeric BibTeX citations. Removed that command; the official class is unchanged. No mathematical claim changed. Before compilation, the Acta record was conservatively corrected to volume 63, Article 31, without an unverified issue number or page-31 interpretation. The failed log is preserved as initial-build-failure.log.

The next compile rejected changing manuscript-mode line spacing (acmart manuscript defaults to one-and-a-half spacing). Selected the official single-column acmsmall class option with 11pt, nonacm, letterpaper and one-inch geometry instead, retaining its default single spacing. Removed the line-spacing override; no class internals or class bytes were changed. The failure log is preserved as spacing-build-failure.log.

Visual inspection showed the generic environment hook did not override the inherited amsart bibliography font; replaced it with the public bibliofont command and explicitly set abstract text to normalsize. Main text, abstract and bibliography now use the selected 11pt size; the official class remains unchanged.
