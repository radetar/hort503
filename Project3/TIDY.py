
import pandas as pd
import numpy as np

BLAST = pd.read_table('BLAST.txt', names = ["Query Accession", "Subject Accession", "Subject Title", "Percent Identity","Alignment length", "Number of mismatches", "Number of Gaps", "Start of Query Alignment", "End of Query Alignment","Start of Subject Alignment","End of Subject Alignment", "E value","Bitscore"])


BLAST_A =BLAST['Query Accession'].value_counts()
BLAST_A.head()


BLAST_B = BLAST_A.to_frame()
BLAST_B.columns=['Hits']
BLAST_B['Protien'] = BLAST_B.index
BLAST_B=BLAST_B.reset_index()
BLAST_C=BLAST_B[['Protien','Hits']]


BLAST_C.to_csv("BLAST_hits.txt", sep="\t")

