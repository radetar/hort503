#"""A Python script that performs simple read trimming of a FASTQ file.

#.. module:: Project01
#   :platform: Unix, Windows
#   :synopsis: This script receives as input a FASTQ file and a set of arguments
#      that control trimming. A new FASTQ file is generated containing only
#      trimmed reads that meet the given requirements.

#.. moduleauthor:: Rachael DeTar



from sys import argv

script, fq = argv

def get_read(fq):
    fq = open(fq)
    raw_read = fq.read().splitlines()[0:4]
    if raw_read:
        return(raw_read)
    else:
        return(False)


raw_read = get_read(fq)




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





trimmed_read = trim_read_front(raw_read, 30, 30)

print(raw_read)############ just a test
print(trimmed_read) #################just a test
print(len(raw_read[1])) #######################just a test
print(len(trimmed_read[1])) #####################just a test



#def main(argv):


#main(argv)
