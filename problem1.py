#!/usr/bin/python

import glob

# concatenates all lines in the list into a single string
def concat_list_lines(l):
    s = ""
    for line in l:
        s += line
    return s

# returns name of the sequence, the sequence itself (lowercase), and its length, all in tuple
def process_seq_file(filename):
    f = open(filename, "r")
    lines = f.read().splitlines()
    # name is first line, starting from after the first character '>'
    seq_name = lines[0][1:]
    seq = concat_list_lines(lines[1:]).lower()
    seq_len = len(seq)
    f.close()
    return (seq_name, seq, seq_len)

# creates a log file with the appropriate header
def create_log_file():
    f = open("combined_seq.log", "w")
    f.write("sequence_name,length\n")
    return f

def process_seq_files(filenames):
    # open the output and log files for writing
    output_file = open("combined.seq", "w")
    log_file = create_log_file()
    for filename in filenames:
        # process file and write to output
        (seq_name, seq, seq_len) = process_seq_file(filename)
        output_file.write(">%s\n" % seq_name)
        output_file.write("%s\n" % seq)

        # record in log
        log_file.write("%s,%d\n" % (seq_name, seq_len))

    output_file.close()
    log_file.close()

def main():
    seq_files = glob.glob("*.seq")
    process_seq_files(seq_files)

if __name__ == '__main__':
    main()