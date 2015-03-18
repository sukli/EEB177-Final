#!/usr/bin/python

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

def main():

if __name__ == '__main__':
    main()