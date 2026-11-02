# Local build

Run `latexmk -C` and then `latexmk -pdf main.tex` from manuscript/. latexmkrc selects the unmodified local official acmart class and ACM bibliography style under vendor/. The output is build/main.pdf. TeX Live, latexmk and Poppler are already installed; no system packages were installed or modified.

Official inputs were copied byte for byte from the user-designated templates/acm-official/distribution/acmart directory. The manuscript uses 11pt single-column letter paper with one-inch margins, named authors as specified in the current STOC 2027 CFP, and the user's stricter cap of 12 total pages. The article has one author, Zijian Zeng, UCSI University, 1002266693@ucsiuniversity.edu.my. It includes substantial generative-AI disclosure. This is a local draft awaiting separate citation/build/visual release review, not a conference submission.
