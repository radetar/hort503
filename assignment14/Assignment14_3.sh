#!/bin/bash
#SBATCH --partition=hort503-01-s18
#SBATCH --account=hort503-01-s18
#SBATCH --job-name=Assn14_3
#SBATCH --output=Assn14_3.out
#SBATCH --error=Assn14_3.err


hmmsearch p450s.fast.aln.hmm dmel-all-translation-r6.21.fasta p450s_hmmsearch_dmel.txt

