#!/bin/bash
#SBATCH	--partition=hort503-01-s18
#SBATCH --account=hort503-01-s18
#SBATCH --job-name=Ass14_celegens
#SBATCH --output=Ass14.out
#SBATCH --error=Ass14.err


export query=$1
export db=$2
export output=$3

muscle -in $query -out $query.aln
hmmbuild $query.aln.hmm $query.aln
hmmsearch $query.aln.hmm $db > $output
