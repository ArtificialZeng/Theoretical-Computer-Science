# Release operations

The first read-only official-vendor comparison used the distribution parent instead of its nested acmart directory and raised FileNotFoundError after successful PDF rendering. The comparison was rerun against actual files beneath the user-designated official distribution; this operational failure is not mathematical evidence. Both clean/build commands succeeded. No frozen evidence, source.md, counters or usage records were changed.

The PDF skill was read and its artifact-operation marker completed successfully before the first source edit/PDF rebuild in this release context. No agent or background worker was launched.
