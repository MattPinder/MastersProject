#!/usr/bin/env python

#GenBank Consensus Generator, version 4.6

#Work still needed: Format the Translation entry of each record so that it adheres
#to the standard format of max. line length 79 characters


#Import relevant modules

from Bio import SeqIO
import sys
import os.path
import re
import argparse

##################################################

parser = argparse.ArgumentParser(description='Creates a consensus between two GenBank files. If exactly one entry is hypothetical, it will be overwritten by \
                                             the other. If there is a conflict, the record from the primary input file will be used.')
parser.add_argument('output', metavar='out', type=str, help='Prefix for output files; a GenBank file and a report file will be generated.')
parser.add_argument('input1', metavar='in1', type=str, help='Primary input GenBank file. In case of conflicts at a given locus, the record from this file \
                                                            will be used. Note: this file should not have less records in it than the secondary input.')
parser.add_argument('input2', metavar='in2', type=str, help='Secondary input GenBank file. This file is used to overwrite hypothetical proteins \
                                                            in the primary input file. Note: this file should not have more records in it than the primary input.')
args = parser.parse_args()

##################################################

#Specify output and 2x input files

outFile = sys.argv[1]
GenBank1 = sys.argv[2]
GenBank2 = sys.argv[3]

Record1 = SeqIO.read(open(GenBank1,"r"), "genbank")
Record2 = SeqIO.read(open(GenBank2,"r"), "genbank")

#Ensure output file doesn't already exist

if os.path.isfile(outFile) == True:
        print "Warning: Output file already exists. Please choose another name."
        sys.exit(0)

#Ensure that the two inputs are both GenBank files

print "First input file: " + GenBank1
print "Second input file: " + GenBank2

for input in sys.argv[2:]:
        if not os.path.basename(input).endswith('.gb') and not os.path.basename(input).endswith('.gbk'):
                print "Input file does not appear to be in the GenBank format."
                sys.exit(0)

#Check that GenBank1 has more records than GenBank2

if len(Record1.features) < len(Record2.features):
        print "Warning: " + GenBank2 + " has more records than " + GenBank1 + "."
	print "The first input file must have more records than the second. Cancelling..."
        sys.exit(0)

print "Input files accepted"
print "Working..."

#Create output and summary files

Consensus = open(outFile + ".gbk", 'wb')
Summary = open(outFile + "_Report.txt", 'wb')

#Variables to save statistics to (how many entries are taken from each GenBank file)

Entries_in_GB1_only = 0
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
allFeatures1 = len(Record1.features)
allFeatures2 = len(Record2.features)

#Make a list of all loci in GenBank2; as GenBank1 may have more entries, this list is needed to check whether
#a given entry is ONLY present in GenBank1

File2Locations = []

for locus2 in range(1,allFeatures2):
	File2Locations.append(str(Record2.features[locus2].location))

#Define function to write the appropriate record to the output file

def WriteRecord(record,locus):
	regex.sub('', str(record.features[locus].location))
        wrongco = regex.sub('', str(record.features[locus].location))
        colon = wrongco.partition(":")
        begin = int(colon[0]) + 1
        end = colon[2]

	if record.features[locus].type == "CDS":
		Consensus.write("     CDS             ")
	elif record.features[locus].type == "tRNA":
		Consensus.write("     tRNA            ")
	elif record.features[locus].type == "rRNA":
		Consensus.write("     rRNA            ")
	elif record.features[locus].type == "tmRNA":
		Consensus.write("     tmRNA           ")
        elif record.features[locus].type == "misc_RNA":
		Consensus.write("     misc_RNA        ")

        if "-" in str(record.features[locus].location):
                Consensus.write("complement(" + str(begin) + ".." + end + ")\n")
        elif "+" in str(record.features[locus].location):
                Consensus.write(str(begin) + ".." + end + "\n")
	
	if "gene" in record.features[locus].qualifiers:
        	Consensus.write("                     /gene=\"" + re.sub("\['|'\]|\[\"|\"\]","",str(record.features[locus].qualifiers['gene'])) + "\"\n")
        Consensus.write("                     /locus_tag=\"" + re.sub("\['|'\]|\[\"|\"\]","",str(Record1.features[locus1].qualifiers['locus_tag'])) + "\"\n")
        if "EC_number" in record.features[locus].qualifiers:
        	Consensus.write("                     /EC_number=\"" + re.sub("\['|'\]|\[\"|\"\]","",str(record.features[locus].qualifiers['EC_number'])) + "\"\n")
        if "inference" in record.features[locus].qualifiers:
                for inferences in record.features[locus].qualifiers['inference']:
        	        Consensus.write("                     /inference=\"" + re.sub("\['|'\]|\[\"|\"\]","",inferences) + "\"\n")
        if "note" in record.features[locus].qualifiers:
                for notes in record.features[locus].qualifiers['note']:
			if not re.sub("\['|'\]|\[\"|\"\]","",notes).endswith(".gb") and not re.sub("\['|'\]|\[\"|\"\]","",notes).endswith(".gbk") and not re.sub("\['|'\]|\[\"|\"\]","",notes).endswith("hypothetical"):
	                        Consensus.write("                     /note=\"" + re.sub("\['|'\]|\[\"|\"\]","",notes) + "\"\n")
	if not str(Record1.features[locus1].location) in File2Locations:
		Consensus.write("                     /note=\"" + "Only found in " + GenBank1 + "\"\n")
	elif record.features[locus].qualifiers['product'] == ['hypothetical protein']:
		Consensus.write("                     /note=\"Both records hypothetical\"\n")
	elif record == Record1:
		Consensus.write("                     /note=\"" + "From " + GenBank1 + "\"\n")
	elif record == Record2:
		Consensus.write("                     /note=\"" + "From " + GenBank2 + "\"\n")
        if record.features[locus].type == "CDS":
		Consensus.write("                     /codon_start=\"" + re.sub("\['|'\]|\[\"|\"\]","",str(record.features[locus].qualifiers['codon_start'])) + "\"\n")
                Consensus.write("                     /transl_table=\"" + re.sub("\['|'\]|\[\"|\"\]","",str(record.features[locus].qualifiers['transl_table'])) + "\"\n")
        Consensus.write("                     /product=\"" + re.sub("\['|'\]|\[\"|\"\]","",str(record.features[locus].qualifiers['product'])) + "\"\n")
	if record.features[locus].type == "CDS":
                Consensus.write("                     /translation=\"" + re.sub("\['|'\]|\[\"|\"\]","",str(record.features[locus].qualifiers['translation'])) + "\"\n")

for locus1 in range(1,allFeatures1):
	if not str(Record1.features[locus1].location) in File2Locations:
		WriteRecord(Record1,locus1)
		Entries_from_GenBank1 += 1
		Entries_in_GB1_only += 1
	elif not Record1.features[locus1].qualifiers['product'] == ['hypothetical protein']:
		WriteRecord(Record1,locus1)
        	Entries_from_GenBank1 += 1
	else:
		for locus2 in range(1,allFeatures2):
			if str(Record1.features[locus1].location) == str(Record2.features[locus2].location) \
			   and not Record2.features[locus2].qualifiers['product'] == ['hypothetical protein']:
				WriteRecord(Record2,locus2)
				Entries_from_GenBank2 += 1
	for locus2 in range(1,allFeatures2):
		if str(Record1.features[locus1].location) == str(Record2.features[locus2].location) \
		   and Record1.features[locus1].qualifiers['product'] == ['hypothetical protein'] \
		   and Record2.features[locus2].qualifiers['product'] == ['hypothetical protein']:
			WriteRecord(Record1,locus1)
			Both_hypothetical += 1

#Once ORIGIN is reached, print the complete DNA sequence from the first GenBank
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

print "Consensus saved to " + outFile + ".gbk"

#Print statistics regarding how many records were taken from each GenBank file

Summary.write("Entries from " + GenBank1 + " = " + str(Entries_from_GenBank1) + "\n")
if Entries_in_GB1_only == 1:
	Summary.write("\t(of which " + str(Entries_in_GB1_only) + " was found only in " + GenBank1 + ")\n")
else:
	Summary.write("\t(of which " + str(Entries_in_GB1_only) + " were found only in " + GenBank1 + ")\n")
Summary.write("Entries from " + GenBank2 + " = " + str(Entries_from_GenBank2) + "\n")
Summary.write("Entries hypothetical in both files = " + str(Both_hypothetical) + "\n")
Summary.write("Total entries processed = " + str(Entries_from_GenBank1 + Entries_from_GenBank2 + Both_hypothetical))

print "Report saved to " + outFile + "_Report.txt"
