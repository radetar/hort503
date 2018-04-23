#!/bin/bash
#SBATCH --partition=hort503-01-s18
#SBATCH --account=hort503-01-s18
#SBATCH --job-name=Assn14_2
#SBATCH --output=Assn14_2.out
#SBATCH --error=Assn14_2.error

hmmbuild p450s.fast.aln.hmm p450s.fasta.aln


