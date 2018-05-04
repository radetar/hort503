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
    read = fq.readlines()[0:4]
    #print(read)#get rid of this later
    return(read)

get_read(fq)



def trim_read_front(read, min_q, min_size):
    trimread = list()
    newread = ""

    for i in read[3]:
        number = ord(i) - 33
        if number >= int(min_q):
            newread += i
            if len(newread)>= min_size:
                print(newread)
            else:
                print("false")



read = ["blah", "aaabbbbaaa","somebullshit","###jjjj###"]
trim_read_front(read, 5, 3)
