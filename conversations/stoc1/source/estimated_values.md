# Estimated values register — revision 2

No estimated performance values appear in the manuscript. All validation and table-payload numbers are produced by artifact/verify.py or artifact/verify_blocks.py and recorded in their JSON outputs. No inferred p50/p99, model throughput, GPU timings, baseline speedups, or production integration results are reported.

The valid Dyck mask rows contain 186 u64 words (1,488 bytes). The actual Rust row arrays include one unused zero row, totaling 192 u64 words (1,536 bytes), excluding allocation/container overhead. Logical serialized payloads are not process RSS.

The generic NFA block checks and Dyck maximum-length compilation-growth data are actual computations in artifact/block_results.json. They do not constitute a general PDA compiler benchmark. No vLLM/llama.cpp or requested-model experiments have been run.
