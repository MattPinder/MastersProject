#!/usr/bin/env python

#Import sys and define input and output files - Done

import sys
inFile = sys.argv[1]
outFile = sys.argv[2]

#Define header and sequence - Done

header = ""
sequence = ""

with open(inFile, "r") as input_file:
	lines = input_file.readlines()
	for line in lines:
		if line.startswith(">") == True:
			header = line.strip("\n") + "_reversed"
		else:
			sequence = sequence + line.strip("\n")

#Determine half of sequence length - Done

seq_length = len(sequence)
half_length = ""
if seq_length % 2 == 0:
	half_length = seq_length / 2
else:
	half_length = (seq_length - 1) / 2

#Save the two halves of the sequence to separate variables

first_half = sequence[:half_length]
last_half = sequence[half_length:]

#Write sequence to output file

with open(outFile, "w") as output_file:
	output_file.write(header + "\n" + last_half + first_half)
	output_file.close()
