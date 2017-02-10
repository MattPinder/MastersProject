#!/usr/bin/env python

#Import relevant modules - done

import sys
import os
import gzip
import ftplib

#Recognise input file as list of species - done

infile = sys.argv[1]
genus_list = []
species_list = []
all_bacteria = []
Summary = open('Download_Summary.txt', 'wb')

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
#then use this to delve into the file structure and download the .gbff.gz
#file with the correct species name.

Summary.write('\nList of species with no .gbff file:\n')

for species in species_list:
	if os.path.isfile(species + '.gbff.gz') == True:
		print species + '.gbff.gz is already present; skipping...'
		continue
	elif os.path.isfile(species + '.gbff') == True:
		print species + '.gbff is already present; skipping...'
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
		spec_dict[species] = ftp.nlst()[-1]
		ftp.cwd(spec_dict[species])
		f = ftp.nlst()
		for entry in f:
			if entry.endswith('.gbff.gz'):
				print '\n' + species + '.gbff.gz found.'
				Zip = open(species + '.gbff.gz', 'wb')
				ftp.retrbinary('RETR %s' % entry, Zip.write)
				print species + '.gbff.gz downloaded.'
				Zip.close()
		if '.gbff.gz' not in str(f):
			print '\n' + species + '.gbff.gz not found.'
			Summary.write(species + '; no .gbff.gz file found\n')

# Unzip the files and replace all blank spaces with underscores (to prevent 'duplicate entries')

print '\n'
Summary.write('\nSuccessfully downloaded species:\n')

for species in species_list:
	if os.path.isfile(species + '.gbff') == True:
		print species + '.gbff already exists; ' + species + '.gbff.gz will be removed.'
		if os.path.isfile(species + '.gbff.gz') == True:
			os.remove(species + '.gbff.gz')
		continue

	elif os.path.isfile(species + '.gbff.gz') == True:
		inF = gzip.open(species + '.gbff.gz', 'rb')
		midF1 = inF.read()
		outF = open(species + '.gbff', 'wb')
#		midF2 = midF1.replace(' ', '_')
		outF.write(midF1)
		print species + '.gbff.gz unzipped.'

#	elif os.path.isfile(species + '.gbff.gz') == True:
#		inF = gzip.open(species + '.gbff.gz', 'rb')
#		outF = open(species + '.raw.gbff', 'w+')
#		outF.write( inF.read() )
#		print species + '.gbff.gz unzipped.'
#		outF.replace(" ", "_")
		inF.close()
		outF.close()
		os.remove(species + '.gbff.gz')
		print species + '.gbff.gz deleted.\n'

for species in species_list:
        if os.path.isfile(species + '.gbff') == True:
		Summary.write(species + '\n')

Summary.close()

print 'All files downloaded and unzipped.\nSummary of results saved to Download_Summary.txt.'
