#"""A Python script that performs simple read trimming of a FASTQ file.

#.. module:: Project01
#   :platform: Unix, Windows
#   :synopsis: This script receives as input a FASTQ file and a set of arguments
#      that control trimming. A new FASTQ file is generated containing only
#      trimmed reads that meet the given requirements.

#.. moduleauthor:: Rachael DeTar



from sys import argv

script, fq, fq_trim, min_q, min_size = argv

fq = open(fq)
fq_trim = open(fq_trim, 'w')


def get_read(fq):
    raw_read = list()
    n = 0
    while n <= 3:
        newline1 = fq.readline().replace('\n', '')
        raw_read.append(newline1)
        n += 1

    if raw_read[0] is not "":
        return(raw_read)
    else:
        return(False)





def trim_read_front(raw_read, min_q, min_size):
    trimmed_bases = 0

    for i in raw_read[3]:
        phred = ord(i) - 33
        if phred <= int(min_q):
            trimmed_bases += 1
        else:
            trimmed_read = [raw_read[0],raw_read[1][trimmed_bases:], raw_read[2], raw_read[3][trimmed_bases:]]
            if len(trimmed_read[1]) >= int(min_size):
                return(trimmed_read)
            else:
                return(False)







def main(argv):

    print(f"Opening your file for reading...")
    print(f"Opening new file for writing...")

    read_count = 0
    trimmed_count = 0
    removed_count = 0
    raw_read = get_read(fq)
    while raw_read is not False:
        raw_read = get_read(fq)
        #print(readmore)
        read_count += 1
        if raw_read is not False:
            trimmed_read = trim_read_front(raw_read,min_q, min_size)
            if trimmed_read is not False:
                print(trimmed_read)
                trimmed_count += 1
                #for item in trimmed_read:
                    #fq_trim.write("%s\n" % item)
                    #fq_trim.write("\n")
            else:
                removed_count += 1
        else:
            exit()

    print(f"{read_count} reads were found...")
    print(f"{removed_count} reads were removed...")
    print(f"{trimmed_count} reads were trimmed and kept...")





main(argv)
