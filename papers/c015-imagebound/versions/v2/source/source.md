# Original primary-source mortality tightness question

Stefan Kiefer and Andrew Ryzhikov, The Complexity of Reachability Problems in Strongly Connected Finite Automata, MFCS2025, DOI10.4230/LIPIcs.MFCS.2025.62, Section9 finalparagraph. PrimaryPDF inintake/primary.pdf, originalURL https://drops.dagstuhl.de/storage/00lipics/lipics-vol345-mfcs2025/LIPIcs.MFCS.2025.62/LIPIcs.MFCS.2025.62.pdf .

The authors give the upper bound n^(k+1) for shortestmortalwords in incomplete k-image-bounded NFAs, then ask verbatim: “Is this bound tight?”

Model: an NFA is a finite labelledrelationsemiautomaton on nstates, withnofixedinitial/finalstates. Eachletteractsasarelation; q.w isthesetofendstatesreachablefromq bywordw. The GLOBALpromise is |q.w|<=k forEVERYq andEVERYword, notmerelyone-stepbranchingdegree. MortalmeansQ.w=empty, i.e. no pathlabelledw startsanywhere. Incomplete meanssuchawordexists. No unambiguity, determinism, binaryalphabet orstrongconnectivitypromise is added; alphabetarbitraryfinite.

Full fixed-parameter tightness reading to investigate: for everyfixedintegerk>=2, is the n^(k+1) exponentasymptoticallynecessary? Let M_k(n) bethemaximum shortestmortalwordlength over alladmissiblen-stateNFAs andfinitealphabets. Seek c_k>0 andunbounded denseenoughstatefamilies attaining c_k*n^(k+1), or a genuinelyuniform sharperupperbound resolvingthe proposedhierarchy. k=1 is a calibrationcase, not a new contribution. Formalize the orderofquantifiers againstthe originalsourceinproblem.md; thewordtight mustnotbe interpretedjointlyforallk~n, since2^n isalwaysatrivialsubsetupperbound.

Onlycomplete resolutionofthisfullfixed-khierarchy andsubstantiveinnovationcanbecomeapublicationcandidate. A finiteNFAtable, Chinese-remainder n^k lowerbound, isolatedk2example, or theoremforonlynewrestrictedmodel stayspartial unlessfreshmathematicalreviewdemonstratesitanswerstheoriginalinfull. Do notreplacewitha questionaboutonlyletterdegrees orshortestsynchronizingwords.
