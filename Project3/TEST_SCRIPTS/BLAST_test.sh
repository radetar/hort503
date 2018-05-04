#!/bin/bash
#SBATCH --partition=hort503-01-s18
#SBATCH --account=hort503-01-s18
#SBATCH --job-name=BLAST
#SBATCH --output=BLAST.out
#SBATCH --error=BLAST.err


module add blast

blastp\
 -query test.pep\
 -db /data/hort503_01_s18/example-data/swissprot\
 -outfmt "6 qacc sacc sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore"

