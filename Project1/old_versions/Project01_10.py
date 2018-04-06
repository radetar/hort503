#"""A Python script that performs simple read trimming of a FASTQ file.

#.. module:: Project01
#   :platform: Unix, Windows
#   :synopsis: This script receives as input a FASTQ file and a set of arguments
#      that control trimming. A new FASTQ file is generated containing only
#      trimmed reads that meet the given requirements.

#.. moduleauthor:: Rachael DeTar



from sys import argv

script, fq = argv
fq = open(fq)

def get_read(fq):
    raw_read = list()
    n = 0
    while n <= 3:
        newline1 = fq.readline().replace('\n', '')
        raw_read.append(newline1)
        n += 1

    if raw_read:
        return(raw_read)
    else:
        return(False)



raw_read1 = get_read(fq)#test
raw_read2 = get_read(fq)#test
raw_read3 = get_read(fq)#tes
#print(raw_read1)
#print(raw_read2)
#print(raw_read3)



def trim_read_front(raw_read, min_q, min_size):
    trimmed_bases = 0

    for i in raw_read[3]:
        number = ord(i) - 33
        if number <= min_q:
            trimmed_bases += 1
        else:
            trimmed_read = [raw_read[0],raw_read[1][trimmed_bases:], raw_read[2], raw_read[3][trimmed_bases:]]
            if len(trimmed_read[1]) >= min_size:
                return(trimmed_read)
            else:
                return(False)





trimmed_read1 = trim_read_front(raw_read1, 30, 30)######test
trimmed_read2 = trim_read_front(raw_read2, 20, 20)#############test


print(raw_read2)#####test
print(trimmed_read2) #################just a test



#def main(argv):


#main(argv)
