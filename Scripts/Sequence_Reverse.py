#!/usr/bin/env python

#Sequence_Reverse, version 3

#Import sys and define input and output files

import sys
import os.path
import argparse

##################################################

parser = argparse.ArgumentParser(description='Cuts fasta sequences in half, then reattaches them in the reverse order, i.e. A----B > A--||--B > --BA--.')
parser.add_argument('input', metavar='in', type=str, help='Specify the input fasta file.')
parser.add_argument('output', metavar='out', type=str, help='Specify a name for the output file; if the file already exists, a warning will be displayed.')
args = parser.parse_args()

##################################################

#Define input and output files

inFile = sys.argv[1]
outFile = sys.argv[2]

#Ensure that the output file doesn't already exist, to prevent overwrite problems

if os.path.isfile(outFile) == True:
	print "Warning: Output file already exists. Please choose another name."
	sys.exit(0)

#Must be able to parse fasta files with multiple sequences; code for this purpose from Biopython and
#http://stackoverflow.com/questions/7654971/parsing-a-fasta-file-using-a-generator-python

def read_fasta(fasta):
    name, seq = None, []
    for line in fasta:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))

#Define the sequence length, and by extension half the sequence length.
#Save each half of the sequence to a variable, then paste those values in the opposite order.
#Note - file is opened in 'append' mode, not in 'write' mode, as this caused an overwrite issue.

with open(inFile) as fasta:
    for name, seq in read_fasta(fasta):
	seq_length = len(seq)
	half_length = ""
	if seq_length % 2 == 0:
		half_length = seq_length / 2
	else:
		half_length = (seq_length - 1) / 2
	first_half = seq[:half_length]
	last_half = seq[half_length:]
	with open(outFile, "a") as output_file:
		output_file.write(name + "_reversed" + "\n" + last_half + first_half + "\n")
		output_file.close()
