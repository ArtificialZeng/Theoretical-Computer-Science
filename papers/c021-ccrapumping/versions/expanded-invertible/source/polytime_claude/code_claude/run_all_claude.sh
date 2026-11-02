#!/bin/sh
# Re-run all sanity checks with the final code; logs in ../logs_claude/final_*.log
cd "$(dirname "$0")"
L=../logs_claude
python3 test_paper_examples_claude.py > $L/final_paper_examples.log 2>&1
for fam in qu_yes qu_rand tor_yes tor_rand; do python3 test_random_claude.py 101 40 $fam > $L/final_rand_$fam.log 2>&1; done
for fam in deepqu_yes deepqu_no; do python3 test_deep_claude.py 102 60 $fam > $L/final_deep_$fam.log 2>&1; done
for fam in deep_yes deep_no deep2_yes2 deep2_no; do python3 test_deep_claude.py 103 30 $fam > $L/final_deep_$fam.log 2>&1; done
python3 test_big_claude.py 104 4 4 3 > $L/final_big_s4_m3.log 2>&1
python3 test_ccra_claude.py 105 150 > $L/final_ccra_seed105.log 2>&1
