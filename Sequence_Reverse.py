#Define input file

#Define sequence - take bottom line from file only
sequence = ""

#Set two blank values for each half of the assembly
header = 
first_half =
second_half =

#Get length of sequence and store half of it
seq_length = len(sequence)
half_length = 
if seq_length % 2 = 0:
	half_length = seq_length / 2
else:
	half_length = (seq_length - 1) / 2

#Save the first half of the sequence to one value

#Save the second half of the sequence to the other value

#Concatenate the two halves

#Add fasta header

#Output to new file
#Must a blank file be made first?

f = open("output.fasta", "w")

f.write(str(header) + "\n" + str(first_half) + str(second_half))

f.close()
