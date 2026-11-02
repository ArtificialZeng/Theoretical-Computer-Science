#!/bin/sh
# Re-runs every computation behind a CLAIMED result of notes_claude/dense3_claude.tex with the final
# sources, writing logs with a header (date, source checksum, command) to logs_claude/final/.
set -e
D="$(cd "$(dirname "$0")/.." && pwd)"
C="$D/code_claude"; L="$D/logs_claude"; F="$L/final"
mkdir -p "$F"
cc -O2 -o "$C/corner_bnb_final_claude" "$C/corner_bnb_v7_claude.c"
hdr() { echo "# $(date '+%Y-%m-%d %H:%M:%S %Z')  src: corner_bnb_v7_claude.c sha1 $(shasum "$C/corner_bnb_v7_claude.c" | cut -c1-12)"; echo "# cmd: $1"; }
run() { # name, env, n, cnum, cden, maxd, patternfile
  out="$F/$1.log"; cmd="$2 corner_bnb_final_claude (= v7 source) $3 $4 $5 $6 < $(basename "$7")"
  hdr "$cmd" > "$out"; env $2 "$C/corner_bnb_final_claude" $3 $4 $5 $6 < "$7" >> "$out" 2>&1; tail -1 "$out" | sed "s/^/$1: /"
}
# Theorem thm:six: 2-sparse, six functions, c = 2.99
run six_j1 "X=1" 6 299 100 10 "$L/pat_n6_j1.txt"
for j in 2 3 4 5 6; do run six_j$j "X=1" 6 299 100 60 "$L/pat_n6_j$j.txt"; done
# Theorem thm:leveled5: leveled, levels 1 on {0..s-1}, 2 elsewhere, c_v = l_v + 0.99
for n in 2 3 4 5 6; do
  smax=$((n-1)); [ $n -eq 6 ] && smax=2
  for s in $(seq 1 $smax); do
    Lv=""; for v in $(seq 0 $((n-1))); do if [ $v -lt $s ]; then Lv="$Lv,1"; else Lv="$Lv,2"; fi; done; Lv=${Lv#,}
    for j in $(seq 1 $n); do maxd=$((j*9)); [ $maxd -gt 60 ] && maxd=60
      run lev_n${n}_s${s}_j$j "LEVELS=$Lv" $n 299 100 $maxd "$L/lev/pat_n${n}_s${s}_j$j.txt"; done
  done
done
# Theorem thm:K5: full pattern, K_5 at 3.99, K_6 at 4.99; sanity K_4 at 3 (clears) and 2.99 (fails)
for j in 1 2 3 4 5; do run K5_j$j "FULL=1" 5 399 100 45 "$L/Kgen/full_j$j.txt"; done
for j in 1 2 3 4 5 6; do run K6_j$j "FULL=1" 6 499 100 54 "$L/Kgen/full_j$j.txt"; done
for j in 1 2 3 4; do run K4c3_j$j "FULL=1 NOSORT=1" 4 3 1 40 "$L/Kgen/full_j$j.txt"; done
run K4c299_j3_expectfail "FULL=1 STOPFIRST=1" 4 299 100 40 "$L/Kgen/full_j3.txt"
# sanity (expected failures / successes) for the leveled version
printf '2 0 1 0 1\n' > "$F/pair2.txt"; printf '2 0 -1 0 -1\n' > "$F/priv2.txt"; printf '3 0 -1 0 -1 0 -1\n' > "$F/priv3.txt"
run sanity_K2_levels11_expectfail "LEVELS=1,1 STOPFIRST=1" 2 199 100 20 "$F/pair2.txt"
run sanity_K2_c199_expectfail "STOPFIRST=1" 2 199 100 20 "$F/pair2.txt"
run sanity_K2_levels12_clears "LEVELS=1,2" 2 299 100 20 "$F/pair2.txt"
run sanity_K1_c099_expectfail "STOPFIRST=1" 1 99 100 20 "$F/priv2.txt"
run sanity_K1_c199_clears "X=1" 1 199 100 21 "$F/priv3.txt"
echo done
