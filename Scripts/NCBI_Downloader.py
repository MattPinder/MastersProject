#!/usr/bin/env python

#NCBI Downloader, version 3

#Import relevant modules

import sys
import os
import gzip
import ftplib
import argparse

##################################################

parser = argparse.ArgumentParser(description='Downloads files of the specified type from the specified list of bacterial genera from the NCBI ftp site.')
parser.add_argument('NameList', metavar='list', type=str, help='File containing a list of bacterial genera.')
parser.add_argument('FileType', metavar='type', type=str, help='File extension to download. Currently tested with .faa and .gbff. Note: .fna files are \
                                                               problematic; see GitHub page readme for details.')
args = parser.parse_args()

##################################################

#Recognise input file as list of species

infile = sys.argv[1]
filetype = sys.argv[2]
genus_list = []
species_list = []
all_bacteria = []

Summary = open('Download_Summary.txt', 'wb')

#Check file type starts with a .

if not filetype.startswith('.'):
	filetype = '.' + filetype
filezip = str(filetype + '.gz')

#Warn user when downloading untested file types

if not filetype == '.faa' and not filetype == '.gbff':
	print 'Note: You are searching for an untested file type.\nFiles may download incorrectly.'

#Save contents of input file to list/dictionary - done

with open(infile) as f:
        genus_list = f.read().splitlines()

Summary.write('List of unrepresented genera:\n')

#Find species in the selected genuses and save their names to species list

ftp = ftplib.FTP("ftp.wip.ncbi.nlm.nih.gov")
ftp.login()
ftp.cwd("genomes")
ftp.cwd("refseq")
ftp.cwd("bacteria")
all_bacteria = ftp.nlst()
for genus in genus_list:
        for bact in all_bacteria:
                if genus in str(bact):
                        species_list.append(bact)
			print bact + ' found.'
for genus in genus_list:
	if genus not in str(species_list):
		print 'No species found in genus ' + genus + '. Mwap mwap.'
		Summary.write(genus + '\n')

#Specify dictionary to include species and RefSeq ID - done

spec_dict = {}

#For each entry, check the RefSeq ID and save it to the list/dictionary,
#then use this to delve into the file structure and download the desired
#file type with the correct species name.

Summary.write('\nList of species with no ' + filetype + ' file:\n')

for species in species_list:
	if os.path.isfile(species + filezip) == True:
		print species + filezip + ' is already present; skipping...'
		continue
	elif os.path.isfile(species + filetype) == True:
		print species + filetype + ' is already present; skipping...'
                continue
	else:
		ftp = ftplib.FTP("ftp.wip.ncbi.nlm.nih.gov")
		ftp.login()
		ftp.cwd("genomes")
		ftp.cwd("refseq")
		ftp.cwd("bacteria")
		ftp.cwd(species)
		try:
			ftp.cwd("latest_assembly_versions")
		except ftplib.error_perm:
			print '\nLatest assembly not found for ' + species + '.'
			Summary.write(species + '; no latest assembly\n')
			continue

#If multiple entries exist in the 'Latest assembly version' folder, the bottom one will be chosen

		spec_dict[species] = ftp.nlst()[-1]
		ftp.cwd(spec_dict[species])
		f = ftp.nlst()
		for entry in f:
			if entry.endswith('genomic' + filezip) or entry.endswith('protein' + filezip):
				print '\n' + species + filezip + ' found.'
				Zip = open(species + filezip, 'wb')
				ftp.retrbinary('RETR %s' % entry, Zip.write)
				print species + filezip + ' downloaded.'
				Zip.close()
		if filezip not in str(f):
			print '\n' + species + filezip + ' not found.'
			Summary.write(species + '; no ' + filezip + ' file found\n')

# Unzip the files and replace all blank spaces with underscores (to prevent 'duplicate entries')

print '\n'
Summary.write('\nSuccessfully downloaded species:\n')

for species in species_list:
	if os.path.isfile(species + filetype) == True:
		print species + filetype + ' already exists; ' + species + filezip + ' will be removed.'
		if os.path.isfile(species + filezip) == True:
			os.remove(species + filezip)
		continue

	elif os.path.isfile(species + filezip) == True:
		inF = gzip.open(species + filezip, 'rb')
		midF1 = inF.read()
		outF = open(species + filetype, 'wb')
		if filetype == '.faa':
			midF2 = midF1.replace(' ', '_')
			outF.write(midF2)
			print species + filezip + ' unzipped; header spaces replaced with underscores.'
		else:
			outF.write(midF1)
			print species + filezip + ' unzipped.'
		inF.close()
		outF.close()
		os.remove(species + filezip)
		print species + filezip + ' deleted.\n'

for species in species_list:
        if os.path.isfile(species + filetype) == True:
		Summary.write(species + '\n')

Summary.close()

print 'All files downloaded and unzipped.\nSummary of results saved to Download_Summary.txt.'
