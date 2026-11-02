# Operational build history

These events concern typesetting only; none is mathematical evidence.

1. The initial build loaded amssymb in addition to acmart's newtxmath and
   stopped at a duplicate Bbbk definition. Removed the redundant package.
2. The next manuscript-mode attempt stopped because acmart forbids changing
   its enforced one-and-a-half baseline spacing. The class was not edited.
   Switched to its official single-column acmlarge mode, retaining 11pt,
   letter paper and one-inch margins. See build-pass1.txt.
3. An initial BibTeX invocation from manuscript with an output path containing
   '..' was rejected by TeX's openout policy. See bibtex.txt. The clean build
   script instead stages the actual sources and runs BibTeX in that directory.
4. Clean builds succeeded. Supplied missing page and publisher fields from
   official DROPS, SIAM and Springer metadata. Removed overfull lines by
   rephrasing and displaying one expression. Fixed a contact-line duplicate
   comma and kept the primitive theorem on one page. Final bibliography is
   normal body size. No system package was installed.

Early warning-bearing logs are retained as build-pass*.txt. The actual final
logs are final-build.log and final-bibtex.log; only those describe the current
PDF. No success flag, mathematical audit or frozen proof was edited.
