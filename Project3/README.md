##### HIGH THROUGHPUT PROTIEN BLAST
#####Author: Rachael DeTar
#####Date: 20180503
==================================================================================================

#Step 1: Login to Kamiak or other server. Clone scripts to personal directory:
```git clone 
==================================================================================================

#Step 2: Run SLURM Script to split fasta into 10 fasta files

```sbatch SPLIT.srun <path to file>```

OUTPUT: 10 seperate fasta files of pattern "x[a-z][a-z].fa"
==================================================================================================

#Step 3: Run SLURM Script to run Protien blast.

```sbatch BLAST.srun```

OUTPUT: 10 blast files labeled "BLAST_[0-9].out". Columns are as listed: 
1. Query accession
2. Subject accession
3. Subject title
4. Percent identity
5. Alignment length
6. Number of mismatches
7. Number of gap openings
8. Start of alignment in query
9. End of alignment in query
10. Start of alignment in subject
11. End of alignment in subject
12. Expect value
13. Bitscore
==================================================================================================

#Step 4: Combine all BLAST.sh output files into 1 file:

```sbatch COMBINE.srun```

OUTPUT: 1 file named "BLAST.txt" with format described in #3, combining all blast output files. 
===================================================================================================

#Step 5: Count the hits for each protein in the query fasta file:

```sbatch TIDY.srun```

OUTPUT: 1 output file named BLAST_hits.txt with 2 columns:
1. Protien
2. Number of hits
===================================================================================================
