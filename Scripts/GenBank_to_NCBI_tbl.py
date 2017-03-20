#!/usr/bin/env python

#GenBank to NCBI .tbl convertor
#Formerly protein_id Adder, version 2.1


#Import relevant modules

from Bio import SeqIO
import sys
import os.path
import re
import argparse

##################################################

parser = argparse.ArgumentParser(description='Converts a GenBank file to a .tbl file, with the addition of the protein_id field required by NCBI.')
parser.add_argument('inFile', metavar='file', type=str, help='File path of GenBank to be converted.')
parser.add_argument('centreID', metavar='centreID', type=str, help='Enter unique centre identifier, to be used in the protein_id field.')
args = parser.parse_args()

##################################################

#Specify and read the input file, and recognise the centre identifier

GenBank1 = sys.argv[1]
CENTRE_ID = sys.argv[2]

INPUT = SeqIO.read(open(GenBank1,"r"), "genbank")
outFile = os.path.splitext(GenBank1)[0] + ".tbl"

#Ensure output file doesn't already exist

if os.path.isfile(outFile) == True:
	print "Warning: Output file " + outFile + " already exists. Process exiting..."
	sys.exit(0)

#Ensure that the input file is in GenBank format

print "Input file: " + GenBank1
print "Unique centre identifier: " + CENTRE_ID

if not os.path.basename(GenBank1).endswith('.gb') and not os.path.basename(GenBank1).endswith('.gbk'):
	print "Input file does not appear to be in the GenBank format."
	sys.exit(0)

#Create output file

OUTPUT = open(outFile, 'wb')

#Print top line of the file

OUTPUT.write(">Features " + INPUT.name + "\n")

#Iterate over and print each entry in the file, but if it is designated as CDS, add a protein_id field beneath the product field, with the relevant value
#This section may be overcomplicated, as it is copied heavily from GenBank_OUTPUT_v4.6.py

regex = re.compile('[^0-9:]')
allFeatures = len(INPUT.features)

for locus in range(1,allFeatures):
	regex.sub('', str(INPUT.features[locus].location))
	wrongco = regex.sub('', str(INPUT.features[locus].location))
	colon = wrongco.partition(":")
	begin = int(colon[0]) + 1
	end = colon[2]

	if INPUT.features[locus].type == "CDS":

		if "-" in str(INPUT.features[locus].location):
			OUTPUT.write(end + "\t" + str(begin) + "\tgene\n")
		elif "+" in str(INPUT.features[locus].location):
			OUTPUT.write(str(begin) + "\t" + end + "\tgene\n")
		if "gene" in INPUT.features[locus].qualifiers:
			OUTPUT.write("\t\t\tgene\t" + re.sub("\['|'\]|\[\"|\"\]","",str(INPUT.features[locus].qualifiers['gene'])) + "\n")
		OUTPUT.write("\t\t\tlocus_tag\t" + re.sub("\['|'\]|\[\"|\"\]","",str(INPUT.features[locus].qualifiers['locus_tag'])) + "\n")
		if "-" in str(INPUT.features[locus].location):
			OUTPUT.write(end + "\t" + str(begin) + "\tCDS\n")
		elif "+" in str(INPUT.features[locus].location):
			OUTPUT.write(str(begin) + "\t" + end + "\tCDS\n")
		OUTPUT.write("\t\t\tproduct\t" + re.sub("\['|'\]|\[\"|\"\]","",str(INPUT.features[locus].qualifiers['product'])) + "\n")
		
		if "EC_number" in INPUT.features[locus].qualifiers:
			for number in INPUT.features[locus].qualifiers['EC_number']:
				OUTPUT.write("\t\t\tEC_number\t" + re.sub("\['|'\]|\[\"|\"\]","",number) + "\n")
		if "note" in INPUT.features[locus].qualifiers:
			for notes in INPUT.features[locus].qualifiers['note']:
				if not re.sub("\['|'\]|\[\"|\"\]","",notes).endswith(".gb") and not re.sub("\['|'\]|\[\"|\"\]","",notes).endswith(".gbk") and \
				not re.sub("\['|'\]|\[\"|\"\]","",notes).endswith("hypothetical"):
					OUTPUT.write("\t\t\tnote\t" + re.sub("\['|'\]|\[\"|\"\]","",notes) + "\n")
		if "inference" in INPUT.features[locus].qualifiers:
			for inferences in INPUT.features[locus].qualifiers['inference']:
				OUTPUT.write("\t\t\tinference\t" + re.sub("\['|'\]|\[\"|\"\]","",inferences) + "\n")
		OUTPUT.write("\t\t\tprotein_id\tgnl|" + CENTRE_ID + "|" + re.sub("\['|'\]|\[\"|\"\]","",str(INPUT.features[locus].qualifiers['locus_tag'])) + "\n")

	if INPUT.features[locus].type == "rRNA":
		if "-" in str(INPUT.features[locus].location):
			OUTPUT.write(end + "\t" + str(begin) + "\tgene\n")
		elif "+" in str(INPUT.features[locus].location):
			OUTPUT.write(str(begin) + "\t" + end + "\tgene\n")
		OUTPUT.write("\t\t\tlocus_tag\t" + re.sub("\['|'\]|\[\"|\"\]","",str(INPUT.features[locus].qualifiers['locus_tag'])) + "\n")
		if "-" in str(INPUT.features[locus].location):
			OUTPUT.write(end + "\t" + str(begin) + "\trRNA\n")
		elif "+" in str(INPUT.features[locus].location):
			OUTPUT.write(str(begin) + "\t" + end + "\trRNA\n")
		OUTPUT.write("\t\t\tproduct\t" + re.sub("\['|'\]|\[\"|\"\]","",str(INPUT.features[locus].qualifiers['product'])) + "\n")
		if "inference" in INPUT.features[locus].qualifiers:
                        for inferences in INPUT.features[locus].qualifiers['inference']:
                                OUTPUT.write("\t\t\tinference\t" + re.sub("\['|'\]|\[\"|\"\]","",inferences) + "\n")

	if INPUT.features[locus].type == "tRNA":
		if "-" in str(INPUT.features[locus].location):
			OUTPUT.write(end + "\t" + str(begin) + "\tgene\n")
		elif "+" in str(INPUT.features[locus].location):
			OUTPUT.write(str(begin) + "\t" + end + "\tgene\n")
                OUTPUT.write("\t\t\tlocus_tag\t" + re.sub("\['|'\]|\[\"|\"\]","",str(INPUT.features[locus].qualifiers['locus_tag'])) + "\n")
		if "-" in str(INPUT.features[locus].location):
                        OUTPUT.write(end + "\t" + str(begin) + "\ttRNA\n")
                elif "+" in str(INPUT.features[locus].location):
                        OUTPUT.write(str(begin) + "\t" + end + "\ttRNA\n")
                OUTPUT.write("\t\t\tproduct\t" + re.sub("\['|'\]|\[\"|\"\]","",str(INPUT.features[locus].qualifiers['product'])) + "\n")
		if "note" in INPUT.features[locus].qualifiers:
			for notes in INPUT.features[locus].qualifiers['note']:
				OUTPUT.write("\t\t\tnote\t" + re.sub("\['|'\]|\[\"|\"\]","",notes) + "\n")
                if "inference" in INPUT.features[locus].qualifiers:
                        for inferences in INPUT.features[locus].qualifiers['inference']:
                                OUTPUT.write("\t\t\tinference\t" + re.sub("\['|'\]|\[\"|\"\]","",inferences) + "\n")

	if INPUT.features[locus].type == "tmRNA":
		if "-" in str(INPUT.features[locus].location):
                        OUTPUT.write(end + "\t" + str(begin) + "\tgene\n")
                elif "+" in str(INPUT.features[locus].location):
                        OUTPUT.write(str(begin) + "\t" + end + "\tgene\n")
		if "gene" in INPUT.features[locus].qualifiers:
                        OUTPUT.write("\t\t\tgene\t" + re.sub("\['|'\]|\[\"|\"\]","",str(INPUT.features[locus].qualifiers['gene'])) + "\n")
                OUTPUT.write("\t\t\tlocus_tag\t" + re.sub("\['|'\]|\[\"|\"\]","",str(INPUT.features[locus].qualifiers['locus_tag'])) + "\n")
		if "-" in str(INPUT.features[locus].location):
                        OUTPUT.write(end + "\t" + str(begin) + "\ttmRNA\n")
                elif "+" in str(INPUT.features[locus].location):
                        OUTPUT.write(str(begin) + "\t" + end + "\ttmRNA\n")
                OUTPUT.write("\t\t\tproduct\t" + re.sub("\['|'\]|\[\"|\"\]","",str(INPUT.features[locus].qualifiers['product'])) + "\n")
                if "inference" in INPUT.features[locus].qualifiers:
                        for inferences in INPUT.features[locus].qualifiers['inference']:
                                OUTPUT.write("\t\t\tinference\t" + re.sub("\['|'\]|\[\"|\"\]","",inferences) + "\n")

	if INPUT.features[locus].type == "misc_RNA":
		if "-" in str(INPUT.features[locus].location):
                        OUTPUT.write(end + "\t" + str(begin) + "\tgene\n")
                elif "+" in str(INPUT.features[locus].location):
                        OUTPUT.write(str(begin) + "\t" + end + "\tgene\n")
		OUTPUT.write("\t\t\tlocus_tag\t" + re.sub("\['|'\]|\[\"|\"\]","",str(INPUT.features[locus].qualifiers['locus_tag'])) + "\n")
		if "-" in str(INPUT.features[locus].location):
                        OUTPUT.write(end + "\t" + str(begin) + "\tncRNA\n")
                elif "+" in str(INPUT.features[locus].location):
                        OUTPUT.write(str(begin) + "\t" + end + "\tncRNA\n")
		OUTPUT.write("\t\t\tncRNA_class\t" + re.sub("\['|'\]|\[\"|\"\]","",str(INPUT.features[locus].qualifiers['product'])) + "\n")


print "File converted, and all protein_id fields added."
print "Output saved to " + outFile + "."
