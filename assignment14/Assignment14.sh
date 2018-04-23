#!/bin/bash
#SBATCH --partition=hort503-01-s18
#SBATCH --account=hort503-01-s18
#SBATCH --job-name=Assn14

muscle -in uniprot.fasta -out p450s.fasta.aln

hmmbuild p450s.fast.aln.hmm p450s.fasta.aln

hmmsearch p450s.fasta.aln.hmm dmel-all-translation-r6.21.fasta

