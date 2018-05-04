#!/bin/bash
#SBATCH --partition=hort503-01-s18
#SBATCH --account=hort503-01-s18
#SBATCH --job-name=SPLIT
#SBATCH --output=COMBINE.out
#SBATCH --error=COMBINE.err
#SBATCH --time=0-02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1

cat BLAST_[0-9].out >> BLAST.txt
