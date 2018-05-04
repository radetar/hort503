


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
            if trimmed_bases >= len(raw_read[3]):
                return(False)
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
        read_count += 1
        if raw_read is not False:
            trimmed_read = trim_read_front(raw_read,min_q, min_size)
            if trimmed_read is not False:
                trimmed_count += 1
                for item in trimmed_read:
                    fq_trim.write(item)
                    fq_trim.write("\n")
            else:
                removed_count += 1

    print(f"{read_count} reads were found...")
    print(f"{removed_count} reads were removed...")
    print(f"{trimmed_count} reads were trimmed and kept...")

    fq_trim.close()



main(argv)
