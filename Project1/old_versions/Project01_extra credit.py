"""A Python script that performs simple read trimming of a FASTQ file.

.. module:: Project01
   :platform: Unix, Windows
   :synopsis: This script receives as input a FASTQ file and a set of arguments
      that control trimming. A new FASTQ file is generated containing only
      trimmed reads that meet the given requirements.

.. moduleauthor:: Rachael DeTar

"""

from sys import argv
script, fq, fq_trim, min_q, min_size = argv
infile= fq
outfile = fq_trim
fq = open(fq)
fq_trim = open(fq_trim, 'w')

#read in lines of a file one by one
def get_read(fq):

    """Extract a single read from a FASTQ file.

    Reads in a FASTQ file are stored in 4 lines that contain the
    sequence_id, nucleotide sequence, a second id, and a series of
    characters represeting quality scores.

    :param fq: A file handle for the FASTQ file
    :type fq: An io.TextIOBase object (created using the open() function).

    :return: a list containing 4 strings: the sequence ID, nucleotide sequence,
        second ID, and the quality score sequence. If there are no more
        sequences in the FASTQ file then this function returns False.
    :rtype: a list with four elements
    """
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

#this function removes low quality reads from the front of a read
def trim_read_front(read, min_q, min_size):
    """Trims the low quality nucleotides from the front of a reads' sequences.

    This function examines the quality score of each nucleotide sequence
    starting from the first position of the sequence. When it encouters a
    high quality score it stops trimming and returns an updated read.

    :param read: A list containing for elements in this order: the sequence ID,
        the nucleotide sequence string, a secondary identifier string, and a
        quality score string.
    :type read: a list

    :param min_q:  The minimum quality score that a nucleotide must have to
        not be trimmed (e.g. 20).
    :type min_q:  integer

    :param min_size:  The minimum size that the sequence must have after
        trimming to keep the read (e.g. 25).
    :type min_size: integer

    :return: a list just like the the get_read() function returns but with the
       low-quality reads (and corresponding quality scores) trimmed off the
       front of the string. If the remaining trimmed read is smaller than the
       desired minimum read length then this function returns False.
    :rtype: a list with four elements
    """
    trimmed_bases = 0
    for i in read[3]:
        phred = ord(i) - 33
        if phred < int(min_q):
            trimmed_bases += 1
            if trimmed_bases >= len(read[3]):
                return(False)
        else:
            trimmed_read = [read[0],read[1][trimmed_bases:], read[2], read[3][trimmed_bases:]]
            if len(trimmed_read[3]) >= int(min_size):
                return(trimmed_read)
            else:
                return(False)

#This function will remove low-quality reads from the back end of a read
def trim_read_back(read, min_q, min_size):
    trimmed_bases = 0
    for i in read[3][::-1]:
        phred = ord(i) - 33
        if phred < int(min_q):
            trimmed_bases += 1
            if trimmed_bases >= len(read[3]):
                return(False)
        else:
            trimmed_endbases= len(read[3]) - trimmed_bases
            trimmed_read = [read[0],read[1][0:trimmed_endbases], read[2], read[3][0:trimmed_endbases]]
            if len(trimmed_read[3]) >= int(min_size):
                return(trimmed_read)
            else:
                return(False)


# The main function for the script.
#This will read and trim all lines of a file, then output a .fq of trimmed reads
def main(argv):
    """The main function of this script.

    After trimming is completed, the fucntion prints out three status lines. The
    first indicates the total number of reads that were found. The second
    indicates how many reads were removed for being too short after trimming and
    the third indicates how many reas were trimmed and kept.

    The script will create a new FASTQ file of just the trimmed reads and name
    it according to the argument provided by the user when running the script.

    :param argv:  The incoming arguments to this script as
       provided by the sys.argv variable.  There must be four total arguments
       provided to the script must be in the following order

       - The filename for the input FASTQ file
       - The filename for the new output FASTQ file that this script creates
       - An integer for the minimum quality score. Anything below this at the
         beginning of each read's nucleotide sequence is trimmed off.
       - An integer indicating how large a read's nucleotide sequence must
         be after trimming in order to keep it.
    """
    print(f"Opening {infile} for reading...")
    print(f"Opening {outfile} for writing...")

    read_count = 0
    trimmed_count = 0
    removed_count = 0
    raw_read = True
    while raw_read is not False:
        raw_read = get_read(fq)
        if raw_read:
            read_count += 1
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
    fq.close()


main(argv)
