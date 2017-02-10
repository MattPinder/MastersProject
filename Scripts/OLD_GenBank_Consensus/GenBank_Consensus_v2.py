#!/usr/bin/env python

#GenBank Consensus Generator, version 2

#Import relevant modules

from Bio import SeqIO
import sys
import os.path
import re

#Specify output and 2x input files; also create output and summary files

outFile = sys.argv[1]
GenBank1 = sys.argv[2]
GenBank2 = sys.argv[3]

Record1 = SeqIO.read(open(GenBank1,"r"), "genbank")
Record2 = SeqIO.read(open(GenBank2,"r"), "genbank")

Consensus = open(outFile + ".gbk", 'wb')
Summary = open(outFile + "_Report.txt", 'wb')

#Ensure output file doesn't already exist

if os.path.isfile(outFile) == True:
        print "Warning: Output file already exists. Please choose another name."
        sys.exit(0)

#Ensure that the two inputs are both GenBank files

for input in sys.argv[2:]:
        print os.path.basename(input)
        if not os.path.basename(input).endswith('.gb') and not os.path.basename(input).endswith('.gbk'):
                print "Input file does not appear to be in the GenBank format."
                sys.exit(0)

#Check that the number of entries in each GenBank file are the same
#THIS MUST BE CHANGED TO ENSURE THAT RECORD1 HAS MORE THAN OR EQUAL TO THE NUMBER OF FEATURES IN RECORD2

if not len(Record1.features) == len(Record2.features):
        print "Warning: The number of entries in the input files are different. Cancelling..."
        sys.exit(0)

#Variables to save statistics to (how many entries are taken from each GenBank file)

Entries_from_GenBank1 = 0
Entries_from_GenBank2 = 0
Both_hypothetical = 0

#Print top section of GenBank1

with open(GenBank1) as header:
        for line in header:
                if not line.startswith("                     /strain="):
                        Consensus.write(line)
                else:
                        Consensus.write(line)
                        break

#Iterate over each entry in the file;
#Check whether the entry in file 1 is hypothetical - if no, print to file; if yes, check the same location in file 2
#If file 2 is non-hypothetical, print from file 2; else, print from file 1

regex = re.compile('[^0-9:]')
allFeatures = len(Record1.features)

#for locus in range(1,allFeatures):
#        regex.sub('', str(Record1.features[locus].location))
#        wrongco = regex.sub('', str(Record1.features[locus].location))
#        colon = wrongco.partition(":")
#        begin = int(colon[0]) + 1
#        end = colon[2]
#        if "-" in str(Record1.features[locus].location):
#                Consensus.write("     " + Record1.features[locus].type + "\t     complement(" + str(begin) + ".." + end + ")\n")
#        elif "+" in str(Record1.features[locus].location):
#                Consensus.write("     " + Record1.features[locus].type + "\t     " + str(begin) + ".." + end + "\n")

def WriteRecord(record):
	regex.sub('', str(Record1.features[locus].location))
        wrongco = regex.sub('', str(Record1.features[locus].location))
        colon = wrongco.partition(":")
        begin = int(colon[0]) + 1
        end = colon[2]
        if "-" in str(Record1.features[locus].location):
                Consensus.write("     " + Record1.features[locus].type + "\t     complement(" + str(begin) + ".." + end + ")\n")
        elif "+" in str(Record1.features[locus].location):
                Consensus.write("     " + Record1.features[locus].type + "\t     " + str(begin) + ".." + end + "\n")
	
	if "gene" in record.features[locus].qualifiers:
        	Consensus.write("                     /gene=\"" + re.sub("\['|'\]","",str(record.features[locus].qualifiers['gene'])) + "\"\n")
        Consensus.write("                     /locus_tag=\"" + re.sub("\['|'\]","",str(record.features[locus].qualifiers['locus_tag'])) + "\"\n")
        if "EC_number" in record.features[locus].qualifiers:
        	Consensus.write("                     /EC_number=\"" + re.sub("\['|'\]","",str(record.features[locus].qualifiers['EC_number'])) + "\"\n")
        if "inference" in record.features[locus].qualifiers:
                for inferences in record.features[locus].qualifiers['inference']:
        	        Consensus.write("                     /inference=\"" + re.sub("\['|'\]","",inferences) + "\"\n")
        if "note" in record.features[locus].qualifiers:
                for notes in record.features[locus].qualifiers['note']:
                        Consensus.write("                     /note=\"" + re.sub("\['|'\]","",notes) + "\"\n")
	if record.features[locus].qualifiers['product'] == ['hypothetical protein']:
		Consensus.write("                     /note=\"Both records hypothetical\"\n") 
	elif record == Record1:
		Consensus.write("                     /note=\"" + "From " + GenBank1 + "\"\n")
	elif record == Record2:
		Consensus.write("                     /note=\"" + "From " + GenBank2 + "\"\n")
        if record.features[locus].type == "CDS":
		Consensus.write("                     /codon_start=\"" + re.sub("\['|'\]","",str(record.features[locus].qualifiers['codon_start'])) + "\"\n")
                Consensus.write("                     /transl_table=\"" + re.sub("\['|'\]","",str(record.features[locus].qualifiers['transl_table'])) + "\"\n")
        if record.features[locus].type == "CDS":
                Consensus.write("                     /product=\"" + re.sub("\['|'\]","",str(record.features[locus].qualifiers['product'])) + "\"\n")
                Consensus.write("                     /translation=\"" + re.sub("\['|'\]","",str(record.features[locus].qualifiers['translation'])) + "\"\n")
for locus in range(1,allFeatures):
	if not Record1.features[locus].qualifiers['product'] == ['hypothetical protein']:
		WriteRecord(Record1)
        	Entries_from_GenBank1 += 1
	elif not Record2.features[locus].qualifiers['product'] == ['hypothetical protein']:
		WriteRecord(Record2)
		Entries_from_GenBank2 += 1
	else:
		WriteRecord(Record1)
		Both_hypothetical += 1

print "Ding"

#Find way to add newlines after 79 characters in the translation section

#Once ORIGIN is reached, print the complete sequence from the first GenBank
#Taken from http://stackoverflow.com/questions/4595197/how-to-grab-the-lines-after-a-matched-line-in-python

def group_by_heading(some_source):
        buffer = []
        for line in some_source:
                if line.startswith("ORIGIN"):
                        if buffer: yield buffer
                        buffer = [line]
                else:
                        buffer.append( line )
        yield buffer

with open(GenBank1, "r") as source:
        for heading_and_lines in group_by_heading(source):
                heading= heading_and_lines[0]
                lines= heading_and_lines[1:]
        Consensus.write(heading)
        for element in lines:
                Consensus.write(element)

#Print statistics re: number of changes made

Summary.write("Entries from GenBank1 = " + str(Entries_from_GenBank1) + "\n")
Summary.write("Entries from GenBank2 = " + str(Entries_from_GenBank2) + "\n")
Summary.write("Remaining hypotheticals = " + str(Both_hypothetical) + "\n")
Summary.write("Total entries processed = " + str(Entries_from_GenBank1 + Entries_from_GenBank2 + Both_hypothetical))
