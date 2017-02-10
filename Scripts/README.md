# Sequence Reverse

## Function
Cuts a sequence in half and reattaches them in the opposite order, i.e.:
* A------B
* A---||---B
* ---BA---

## Purpose
Rearrangement of sequences to check coverage levels and determine whether
a contig is circular, when used as a reference sequence for the Resequencing
protocol on the SMRT Portal.

## Usage
`Sequence_Reverse.py [input] [output]`

* input: Specify the input fasta file.
* output: Specify a name for the output file; if the file already exists, a warning will be displayed.

## Version history

* Version 1
 * Reversal of single-record fasta files
* Version 2
 * Added code to handle multi-record fasta files
* Version 3
 * Added help page

# NCBI Downloader

## Function
Downloads files of the chosen type from the NCBI ftp site.

## Purpose
Downloading dozens of files for comparative studies (e.g. generating phylogenies)
can be time-consuming, so this script requires a file listing the desired genera,
and the file extension of the desired file type.

## Usage
`NCBI_Downloader.py [list] [filetype]`

* list: File containing a list of bacterial genera.
* filetype: File extension to download. Currently tested with .faa and .gbff.
 * Note: .fna files are problematic.

## Version history

* Version 1
 * Downloads .faa (amino acid fasta) files from NCBI ftp site
* Version 2
 * Downloads .gbff (GenBank) files from NCBI ftp site
* Version 3
 * Downloads specified file type from NCBI ftp site
 * Note: Tested with .faa and .gbff; other file types should work but may be problematic
  * .fna in particular creates problems, as there are often multiple .fna files in a folder

# GenBank Consensus Generator

## Function

Generate a consensus between two GenBank files; if an entry in the primary input is hypothetical,
the second GenBank file can fill in the blank if its own entry isn't hypothetical.

## Purpose
This script was written for the specific purpose of combining two GenBank files generated using
the Prokka prokaryotic annotation tool, which have been annotated using slightly different databases,
and therefore contain slightly different information.
The intention is that the first of the two input files contains the most entries, and hopefully the
most reliable data (in my project, the primary file contained non-CDS elements such as tRNA, rRNA and
misc elements, whereas the secondary file contained only CDS and sometimes tRNA elements).

### GenBank Consensus Generator, Names version

This version is a branch of version 4.5 which, as well as overwriting hypothetical entries in the
primary input, also overwrites unnamed entries in the primary input if the secondary input contains a named entry at the same locus.
The hope with this version is that named gene predictions will allow for more numerous and more accurate pathway predictions.

## Usage

`GenBank_Consensus.py [output] [input 1] [input 2]`
`GenBank_Consensus_Names.py [output] [input 1] [input 2]`

* out: Prefix for output files; a GenBank file and a report file will be generated.
* input 1: Primary input GenBank file. In case of conflicts at a given locus,
           the record from this file will be used. Note: this file should not
           have less records in it than the secondary input.
* input 2: Secondary input GenBank file. This file is used to overwrite
           hypothetical proteins in the primary input file. Note: this file
           should not have more records in it than the primary input.

## Version history

* Version 1
 * Original version with all features largely functional
* Version 2
 * Condensed code by defining 'WriteRecord' function
* Version 3
  * The primary input file can now be longer than the secondary input file, rather than having to have equal length
 * To account for length differences, matching records between two files now uses locus coordinates instead of locus tag
 * The summary file will now record how many loci were only present in the primary input file
* Version 4.1
 * Help feature added
 * Tabs no longer used when printing feature type
* Version 4.2
 * Product now also printed for non-CDS loci
* Version 4.3
 * Locus tag issue fixed; if locus information is taken from the secondary input file, the locus tag from the primary file is now retained
* Version 4.4
 * Notes generated in previous GenBank_Consensus steps ("From *.gb/*.gbk") no longer transferred to subsequent steps
* Version 4.5
 * Added additional parameters to account for unusual bracketing of values in GenBank libraries interpreted by BioPython
 * **This version was the basis for the alternative version, GenBank_Consensus_Names.py**
* GenBank_Consensus_Names
 * Alterations made so that a named gene would be selected in preference to an unnamed one at the same locus

## Limitations

* The current version is only intended for use with GenBank files containing a single contig; multi-contig files will not be processed correctly.
* The 'Translation' line of each locus is not correctly formatted; sequences are displayed on a single line rather than adding line breaks into long sequences.
 * For the intended purpose - comprehension by the program [Pathway Tools] (http://brg.ai.sri.com/ptools/) - this formatting issue is irrelevant.
