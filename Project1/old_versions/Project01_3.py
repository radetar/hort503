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
    read_1 = fq.readlines()[0:4]
    #print(read_1)#get rid of this later
    return(read_1)

get_read(fq)



def trim_read_front(read_1, min_q, min_size):
    trimmed_bases = 0

    for i in read_1[3]:
        number = ord(i) - 33
        if number <= min_q:
            trimmed_bases += 1
        else:
            trimmed_read = [read_1[0],read_1[1][trimmed_bases:], read_1[2], read_1[3][trimmed_bases:]]
            if len(trimmed_read[1]) >= min_size:
                #print(trimmed_read) for testing purposes only
                return(trimmed_read)
            else:
                return(False)




read_1 = ["blah", "aaabbbaaa","somebullshit","###jjj###"]

trim_read_front(read_1, 5, 6)
    #while read[3] <= min_q
        #append_to_list = False
    #if append_to_list = True:
        #for i in read:
            #read2.append
    #if len(read2[3])
