#!/bin/bash
#SBATCH --partition=hort503-01-s18
#SBATCH --account=hort503-01-s18
#SBATCH --job-name=BLAST
#SBATCH --output=BLAST_%a.out
#SBATCH --error=BLAST_%a.err
#SBATCH --array=0-9


module add blast


IDs=(`find . -name "*.fa"`)

ID=${IDs[$SLURM_ARRAY_TASK_ID]}

blastp\
 -query ${ID}\
 -db /data/hort503_01_s18/example-data/swissprot\
 -outfmt "6 qacc sacc stitle pident length mismatch gapopen qstart qend sstart send evalue bitscore"
