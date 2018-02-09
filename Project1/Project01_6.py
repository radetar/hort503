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

start=0
finish = 4

def get_read(fq,start,finish):
    raw_read = fq.read().splitlines()[start:finish]
    if raw_read:
        start += 4
        finish += 4
        return(raw_read, start, finish)
    else:
        return(False)


raw_read1 = get_read(fq,start,finish)
print(raw_read1)############ just a test
raw_read2 = get_read(fq,start,finish)
print(raw_read2)
print(start)
print(finish)
#raw_read2 = get_read(fq,start,finish)
#raw_read3 = get_read(fq,start,finish)




#def trim_read_front(raw_read, min_q, min_size):
    #trimmed_bases = 0

    #for i in raw_read[3]:
        #number = ord(i) - 33
        #if number <= min_q:
            #trimmed_bases += 1
        #else:
            #trimmed_read = [raw_read[0],raw_read[1][trimmed_bases:], raw_read[2], raw_read[3][trimmed_bases:]]
            #if len(trimmed_read[1]) >= min_size:
                #return(trimmed_read)
            #else:
                #return(False)





#trimmed_read = trim_read_front(raw_read, 30, 30)


#print(raw_read2)
#print(raw_read3)
#print(trimmed_read) #################just a test
#print(len(raw_read[1])) #######################just a test
#print(len(trimmed_read[1])) #####################just a test



#def main(argv):


#main(argv)
