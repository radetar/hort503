#!/bin/bash
#SBATCH --partition=hort503-01-s18
#SBATCH --account=hort503-01-s18
#SBATCH --job-name=Assn14_1

muscle -in uniprot.fasta -out p450s.fasta.aln

