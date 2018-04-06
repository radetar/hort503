


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
from collections import OrderedDict
from sys import argv

script, pileup= argv


putable = pd.read_table(pileup, sep="\t",header=None)



###skip lines containing *,+,-,<,>, or that have less than 10 reads
skips = ['\*','\+','\-','\<','\>']
putable= putable[putable[4].str.contains('|'.join(skips)) == False & (putable[4].str.len() >= 10)]


#replace $ or ^ with empty string
putable[4] = putable[4].str.replace('\^.|\$','', case=None, flags=0)


###GO through table line by line, initaite some counters for varaints:
SNPs = pd.DataFrame()
for index, row in putable.iterrows():
    match = 0
    bases={"A":0,"C":0,"G":0,"T":0}                        # save counts in dictionary
    for i, char in enumerate(row[5]):                      #read in bases one by one, keeping track of index
        if ord(char)-33 >= 30:                             #calculate phred, pass on reads with phred >= 30
            if re.match(",|\.", row[4][i]):
                match += 1
            elif re.match("A", row[4][i] ,re.IGNORECASE):  #count number of mismatches pertaining to each base
                bases["A"] += 1
            elif re.match("T", row[4][i] ,re.IGNORECASE):
                bases["T"] += 1
            elif re.match("C",row[4][i] ,re.IGNORECASE):
                bases["C"] += 1
            elif re.match("G", row[4][i] ,re.IGNORECASE):
                bases["G"] += 1
            else:
                print("ERROR-unknown character in pileup",row[1],row[4][i])

#check that number of mismatches per base is >=3, calc. frequency, store as a pandas dataframe
    for key,value in bases.items():
        if value >= 3:
            frequency = value/len(row[5])
            blah = pd.DataFrame(OrderedDict({"chromosome":[row[0]],"position":[row[1]],"ref_base":[row[2]],"SNP_base":[key],"frequency":[frequency]}))
            SNPs = SNPs.append(blah,ignore_index=False)
            cols=['chromosome','position','ref_base','SNP_base','frequency']
            SNPs=SNPs[cols]
#write SNPS to file
SNPs.to_csv("SNPs.txt", "\t",index=False)

#Make the plot, save a 300 dpi png

plt.figure();
SNPs.plot.bar(x ='position',y ='frequency',legend=False)
plt.ylim(0, 1.1)
plt.xlim(0,60885)
plt.xticks(np.arange(0,60881,10000))
plt.savefig("SNPs.png",dpi=300)
