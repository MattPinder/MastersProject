# 9 August 2016

Useful tools to install:  
* PROKKA  
* Pathway Tools  
* RAST  

Things to try:  
* Submission to NCBI Prokaryotic Genome Annotation Pipeline?  
* PANNZER  
* AGeS  

Raw data:  
* combined-revcomp-unitig-1-2.fasta  

# 10 August 2016

NCBI PGAP seems to be only for those ready to submit a genome - unsuitable

Downloaded myRAST to my laptop, will compare results with those obtained
previously (no version number given in Oskar's documentation, though he
appears to have used the web-based version).

Pathway Tools would not have the full range of pathway/genome databases if
installed on my computer, so may attempt on Albiorix at a later date.

Uploaded fasta to RAST web service using default settings, for comparison
with results obtained by Oskar.

Attempting to get GitHub to work - succeeded in syncing local git repository
with online GitHub account.

Downloaded Excel spreadsheet of RAST results and compared with Oskar's most
recent .gbk file; contrary to his observations, a small proportion of the
genes predicted by RAST had names. These names sometimes conflicted with the
names found by Oskar, however, despite consistent locations and functions.

Using output from myRAST, compared EC number of random protein with the KEGG
database. Several gene names found (species-dependent), but unsure how to
determine which is the appropriate name for Kordia. In any case, would be too
time-consuming to name all 4000+ Kordia genes in this way...

# 11 August 2016

Had to stop myRAST's final step - Compute correspondences - part-way yesterday,
so re-running the analysis while I look at yesterday's output, which looks
alright so far.

Attempting to work out how the software Oskar used came to the conclusions it
did about certain proteins' identities, as some are not immediately apparent
via e.g. BLASTing.

Submitted fasta to GeneMarkS, to see what is returned.
The information which was returned was similar to the previous predictions,
with a few extra overlapping portions, but only sequences, no names.

Submitted fasta to Glimmer web service on NCBI, to see what is returned.
As with GeneMarkS, this returns only location predictions, not names.

BLASTP search of 2053006..2053860 (Periplasmic binding protein-like II; no name)
returned a hit spanning almost the whole protein with an E-value of 4.12e-160
for 'PBP2_Ca3427_like' (a hypothetical protein...).
When performing a similar search with Kordia sp. proteins which have already
been given names in the previous analysis, the results I receive are
inconsistent; I don't get the same name as was found previously...

List of annotation pipelines which might be useful:
https://omictools.com/genome-annotation-category

# 12 August 2016

While browsing the online version of RAST, I found that there are some
indications of gene names to be found, although these may contradict the
list of genes that Oskar made. For example, online RAST identifies two copies
of RNA polymerase sigma factor RpoE, whereas Oskar notes 6 copies.

Process:  
* Take the first identified gene from the V5 genbank file: rpsU.  
* According to the Excel exported from RAST, it is classified as 'Ribosome SSU
bacterial', so go to this page in the RAST analysis, and look at 'Subsystem
Spreadsheet'.  
* No rpsU heading, so look under S21p (the product) - one hit, labelled 1, as
this is the first 'pegged' result.  
* After clicking on '1', run Psi-Blast; this opens a Psi-Blast window (first
hit Kordia jejudonensis) which identifies rpsU as a specific hit (with E-value
of 4.63e-14).  

Test the above process with the next gene in the genbank file - an unnamed
alpha-amylase gene.  
Two hits in conserved domains database with very high E-values:  
* AmyAc_arch_bac_plant_AmyA has an E-value of 6.62e-121, and is labelled as
a specific hit, BUT has a Ca binding site missing...  
* PRK09441 covers a wider part of the protein, and has an E-value of 3.29e-165  

Found reason for conflict between gene list and genbank files - Oskar's V2
gene list was compiled early in the project, so doesn't sync up with later
findings in the more recent genbank files...  
Made an alphabetical list of genes from V5 genbank, and uploaded to github.

Investigating InterPro, could shed light on potential functions of the many
'hypothetical proteins' from previous analyses; as it is still in active
development, hopefully it should provide SOME insight.  
Thus far, 'insight' has been rare, as the web tool is providing only small
amounts of information regarding the hypothetical proteins, such as an
occasional matching domain...

Still unsure how the previously-used software comes to some of its conclusions
about gene identities; PSI-BLASTing glpE_1 seems to show PspE as a better
match for the gene...

### Questions after week 1
Oskar's software - PROKKA, System Tools, etc. - yielded certain results,
whereas I am able to find apparent results in addition to these which seem
to obtain better E-values in a RAST -> PSI-BLAST -> CDD search. Why?  

# 15 August 2016

Attempted to use the myRAST Shell on Windows to generate a list of gene
aliases, however operating this is not as intuitive as it would be on Linux,
so may have to wait until myRAST is installed on Albiorix...

myRAST acting up on my computer; have uninstalled but must wait until website
is back online before I can reinstall...

If PROKKA etc. can be installed on Albiorix, if the databases have been
updated in the last few months since Oskar's work was done, then perhaps more
information can be obtained.

Manual PfamScan can give at least a general idea of what the hypothetical
proteins may be in some cases, e.g. PROKKA_00107 from 'PROKKA_K-sp_V5.gbk'
apparently contains a 'Cro/C1-type HTH DNA-binding domain'. Again, this would
be time-consuming to check manually for all of the proteins labelled as
hypothetical in the .gbk file...

Some K. algicida protein sequences are present on NCBI, including some with
gene names. Checking manually (yet again), I found that PROKKA_01500 from the
aforemetioned .gbk file bears a resemblance to the preprotein translocase
subunit YajC found on NCBI (http://www.ncbi.nlm.nih.gov/protein/WP_050765224.1).
Judging by where the alignment starts and ends vs. the K. algicida sequence,
the gene predictor MAY have made a mistake in the alignment...  
K. sp.:  
MIAVLYFLIIAPSLKKQKKEKKFMASVKKGDRVITKSGIHGKIVELNDKDFTCVIETGAGKIKFERAALSVEASARLNNPPAKK  
K. alg.:  
MVVVVYFFILAPSIKRQKKEKNFMASIKKGDRVITKSGIHGKVVELNDKDHTCVIETGAGKIKFERAALSADATLRLNKPPSEKK  

# 16 August 2016

Small victory?  
Took a partial list of proteins labelled 'Hypothetical protein' in
myRAST_export.xls, and ran it through Batch Web CD-Search Tool
(http://www.ncbi.nlm.nih.gov/Structure/bwrpsb/bwrpsb.cgi); some of those
labelled as specific hits included gene names; after comparing a few of these
to Oskar's V5 genbank file, found one of his with no gene name but which
identified a heavy metal-associated domain, which agrees with the CD search's
claim that the gene is the copper chaperone CopZ. Subsequent BLASTP gave a
(perhaps tenuous) match - 68% identity, 4e-37 E-value, 100% coverage - to
K. zhangzhouensis's 'heavy metal transporter' gene. Right now, CopZ is my
best guess. Once again, however, this gene-by-gene checking is too slow to
be very useful...

Copied the V5 genbank file and deleted all named genes to give me a full list
of those I need to name.

### To do  
1. Pathway Tools webinars, paper and installation  
2. Start updating genbank file (/note field to give reason why)  
3. Potentially restructure the Kordia directory; add updated version of
genbank file to, e.g. '01_Annotation' folder  

# 17 August 2016

Cut apart the genbank file, now contains only the products and sequences of
the unnamed proteins (filename: AUP2). Also copied the V5 genbank file and
renamed V6, so all genes named hereafter will be added to this file; the
note field of the genbank file should be used to justify the naming of each
gene.

Running the new file through NCBI batch CD-Search Tool again, and will make
a note of any promising results.  
(Still running; Search-ID QM3-qcdsearch-29D17B06C7A6E9DA)

# 18 August 2016

Searching 'Kordia' under NCBI's protein search reveals ~8000 non-hypothetical
results, some of which are named. I am installing Blast+ on my local computer so
that I can query the fasta file of these results with the unnamed proteins file.

* Read up on HGAP - Alvar's thesis  
* Set up new Kordia folder on Bioinformatics Group Github page  
* Note: md5sum software for ensuring files are copied correctly 

Made several updates to PROKKA V6 based on local BLAST (including one gene name!),
using an e-value cutoff of 0.01 to get rid of some of the worse results. To get
more gene names, however, perhaps attempt to use a (nucleotide?) database for a
more well-annotated bacterium?

# 24 August 2016

Rerunning local BLASTP with more stringent e-value criterion:  
C:\Users\Matt\Desktop\PROJECT\blast-2.4.0+\bin> blastp -db ../db/Kordia -query
../../AUP2_reformatted_2.txt -out AUP_Test_Results_2 -evalue 1e-040

* Check how to set up and configure PROKKA databases; [appears to be possible] (https://github.com/tseemann/prokka/issues/95)

Created new branch in the kordia_pathway_analysis repository in which to store my
own work.

Have written a script to test the workings of PROKKA, output, etc.
Require tbl2asn 23.0 or higher...

* Create editable folder to store PROKKA DBs (confirm where!)
* Download 3x .gbk files for Kordia and make a PROKKA database (see Oskar's readme for details)
* Find out why the database creation didn't work!  

# 25 August 2016

prokka-genbank_to_fasta_db does not run because it is looking for parent.pm in the
wrong place. Check how to edit @INC to look at
/usr/local/packages/perl-5.14.4/lib/5.14.4/parent.pm

Downloaded Blast2GO, in case this can give any useful information.  
Exporting a DNA fasta file from myRAST for use as input.  
Running blastn first to see if anything new comes up.  

Local BLAST vs database of species shown as similar in Blast2GO?  
e.g. Flavobacterium psychrophilum, Lutibacter, etc.

Downloading and installing Pathway Tools...  
IMPORTANT: Pathway Tools does NOT require gene NAMES to construct pathways; it only
requires protein products. Therefore, NAMING the unnamed genes is not as important
as finding a function for the proteins listed as hypothetical.

Try and finish running Blast2GO and Pathway Tools overnight; currently only part of
the way through...

# 26 August 2016

Pathway Tools finished; obtain pathway overview to see current state of play  
Blast2GO crashed in the night; continue and see how far it gets today

Pathway Tools has finished creating the Pathway Overview; as expected, a lot
still to do.

Potential task - write a Python script which defines the region 'CDS' to 'CDS'
as an object, and extracts it if the term 'hypothetical' or 'putative' appears.  
OR  
Find out if I can extract certain records using BioPython...

Converted V5 .gbk to fasta online; can now extract hypothetical protein
sequences more easily for analysis (hopefully...)

/db/prokka - writeable folder for PROKKA databases

Read HGAP paper, SMRT portal manual

http://albiorix.bioenv.gu.se:8081

* /nobackup/data5/Skeletonema_marinoi_microbiome_project
* Create 01_Assemblies
* Add subdirectories for each sample, and a further subdirectory for each
assembly run; once there is a README.md in each folder, can push to GitLab.

### For Monday

Scrutinise results of #6; potential problems with data transfer...
Run jobs 7 and 8

# 27 August 2016

Started jobs 7 and 8; will wait until Monday to check over all results from
first assembly attempts.

# 29 August 2016

Downloaded reports of first assembly attempts and uploaded them to GitLab.

Number of bases in #6 same on both preliminary and first assembly; should
be okay...

Add fasta files to repository; check which... Polished reads

Added Sum of Contig Lengths table to 01_assemblies readme

Blastx of single-unitig samples 4 & 8

Folder structure changed to simplify BLAST script syntax

Startd a Google Docs page to make [notes for my thesis] (https://docs.google.com/document/d/1_l0IFS5Dkj8g38A57gzm-sVaJx63IGsWnzQb567rwWc/edit?usp=sharing).

BLAST search appears to be stuck in the queue - double-check when /nobackup
is brought back online...

# 30 August 2016

runBlast_16442.sge still stuck in queue. Will have to remove and retry...

SMRT Portal on Albiorix ALSO seems to be down...

SMRT Portal back up and running; only two jobs completed successfully, must rerun the rest:

| Sample | Job # | New Job # | New Job Status |
|--------|-------|-----------|----------------|
| 1 #2   | 16447 | 16457     | Failed         |
| 2 #2   | 16448 | 16458     |                |
| 2 #3   | 16449 | 16459     | Failed         |
| 3 #2   | 16450 | N/A       | -              |
| 5 #2   | 16451 | 16460     | Failed         |
| 5 #3   | 16452 | 16461     |                |
| 6 #2   | 16453 | 16462     | Failed         |
| 6 #3   | 16454 | 16463     | Failed         |
| 6 #4   | 16455 | 16464     | Failed         |
| 7 #2   | 16456 | N/A       | -              |

Checked completed results of samples 3 and 7. Both show a dramatic spike in unitig numbers;
3 jumped from 5 back up to 28, and 7 jumped from 4 to 30...

Run sample #3 @ 18k	Failed  
Run sample #7 @ 19k

__Assembly jobs seem to take around 7 hours__

__blastx jobs for pb_359_4 and pb_459_8 are now running on Annotation-1, now permissions have been
altered; may take a very long time...__

prokka-genbank_to_fasta_db still giving some very strange errors... Check?

In order to use prokka-genbank_to_fasta_db, must install CD-HIT program...

Created new HMM database from TIGR; placed in /db/prokka so must use --hmms flag in Prokka
to point to it; have attempted this with Prokka_Test_2...

Assembly jobs to rerun:

* 16457 - pb_359_1-25000_Rerun
* 16459 - pb_359_2-10000_Rerun
* 16460 - pb_359_5-15000_Rerun
* 16462 - pb_359_6-10000_Rerun
* 16463 - pb_359_6-9000_Rerun
* 16464 - pb_359_6_8000_Rerun
* 16465 - pb_359_3-18000

All of the above jobs have failed; perhaps I have overtaxed Albiorix, so will wait until the
other jobs have finished running (completing/failing) before retrying the above...

In addition, Prokka_Test_2 has been pushed back into Pending, and node0 is showing an error...
When rerun, Prokka_Test_2 showed no difference to original Prokka_Test; TIGR HMM database
seems to have been ignored... [May have to put the files into the read-only Prokka db folder,
or rewrite a line in the Prokka files to look elsewhere for db files] (https://github.com/tseemann/prokka/issues/95).

### To do

* Rerun the five [six] outstanding jobs which crashed earlier - job 16468 crashed AGAIN...
	* Jobs that need to be rerun: 16460, 16462, 16463, 16464, 16465, 16468
	* Potentially check in the evening if other jobs are complete...
* Get Prokka file redirected to look at /db/prokka for its databases (move whole folder?), as
--hmms option doesn't work in getting Prokka to search the TIGR database
* Get cd-hit installed in order to create Kordia database from NCBI .gbk files

## Evening

* Restarted jobs 16460 (now 16469) and 16462 (now 16470)
* 16467 has completed; download relevant files in the morning!

# 31 August 2016

Of yesterday's assembly jobs, only 16466 and 16467 completed... Made an Excel spreadsheet for personal
reference as to which jobs have worked and not.

Started jobs 16471, 16472 and 16473 - wait for these to complete before proceeding with more.

Jobs to submit:

| Type of job     | Title                  | ID of job to copy | Submitted? | Result |
|-----------------|------------------------|-------------------|------------|--------|
| New             | pb_359_1-18000         | N/A               | 16474      |        |
| New             | pb_359_7-21000         | N/A               | 16475      |        |
| Resubmission    | pb_359_6-10000_Rerun_3 | 16470             | 16476      | Failed |
| Resubmission    | pb_359_6-9000_Rerun_2  | 16463             | 16477      | Failed |
| Resubmission    | pb_359_6-8000_Rerun_2  | 16464             | 16478      | Failed |
| Resubmission    | pb_359_2-10000_Rerun_4 | 16471             | 16479      | Failed |
| Resubmission    | pb_359_5-15000_Rerun_4 | 16473             | 16480      | Failed |
| (Still running) | pb_359_3-18000_Rerun   | N/A               | 16472      |        |

With luck, jobs 16471-3 SHOULD be done ~5pm, so could potentially kick off new jobs before going
home this evening; failing that, kick off tonight...

16471 and 16473 failed... 16472 still running

'df -h' command checks disk space; 'ls -l /tmp' to check files in the /tmp folder (possible that
files aren't being deleted after a crash...?)

Looking at 'ls -ltr /tmp', it appears that some temporary files aren't even being removed
after a SUCCESSFUL assembly!

Log files of both successful and unsuccessful assemblies make no reference to removing old
files...

SMRT analysis temporary directory has been moved, so will start all outstanding jobs in an
attempt to test the system

New jobs started since the change - 16474, 16475, 16476, 16477, 16478, 16479, 16480  
Still running - 16472

Note - cd-hit is already installed! cd-hit/v4.6.5

* Double-check syntax for running Python jobs on Albiorix.

Tweaked Create_PROKKA_Database.sge to load cd-hit, as this seemed to be causing problems previously.

Create_PROKKA_Database.sge still throws an error message, so have [posted on the Prokka GitHub page] (https://github.com/tseemann/prokka/issues/192)
to request assistance from the developer...

Job 16477, 16476, 16478, 16479 and 16480 failed...

Out of curiosity, which stage did the above jobs crash on?

|  Job  | Failure stage                              | Duration before fail |
|-------|--------------------------------------------|----------------------|
| 16476 | PreAssemblerDagcon/hgapCorrection_002of006 | 200.29 minutes       |
| 16477 | PreAssemblerDagcon/hgapCorrection_001of006 | 189.18 minutes       |
| 16478 | PreAssemblerDagcon/hgapCorrection_004of006 | 204.54 minutes       |
| 16479 | PreAssemblerDagcon/hgapCorrection_003of006 | 206.60 minutes       |
| 16480 | PreAssemblerDagcon/hgapCorrection_003of006 | 212.24 minutes       |

I've seen other failures at different stages, but all of these have failed at the same major phase...  
Does the hgapCorrection process require a huge number of cores?

Places at which other jobs have failed:

|  Job  | Failure stage                              | Duration before fail |
|-------|--------------------------------------------|----------------------|
| 16447 | Mapping/align_002of003 *                   | 304.89 minutes *     |
| 16448 | PreAssemblerDagcon/hgapCorrection_003of006 | 262.79 minutes       |
| 16449 | PreAssemblerDagcon/hgapCorrection_001of006 | 276.99 minutes       |
| 16451 | PreAssemblerDagcon/hgapCorrection_004of006 | 314.72 minutes       |
| 16452 | No obvious error... *                      | 1013.47 minutes *    |
| 16453 | PreAssemblerDagcon/hgapCorrection_001of006 | 260.06 minutes       |
| 16454 | PreAssemblerDagcon/hgapCorrection_002of006 | 287.36 minutes       |
| 16455 | PreAssemblerDagcon/hgapCorrection_003of006 | 279.02 minutes       |
| 16457 | Mapping/align_001of003 *                   | 291.89 minutes *     |
| 16459 | PreAssemblerDagcon/hgapCorrection_005of006 | 191.43 minutes       |
| 16460 | PreAssemblerDagcon/hgapCorrection_006of006 | 247.81 minutes       |
| 16462 | PreAssemblerDagcon/hgapCorrection_001of006 | 229.72 minutes       |
| 16463 | PreAssemblerDagcon/hgapCorrection_003of006 | 252.81 minutes       |
| 16464 | PreAssemblerDagcon/hgapCorrection_005of006 | 256.72 minutes       |
| 16465 | PreAssemblerDagcon/hgapCorrection_004of006 | 194.30 minutes       |
| 16468 | PreAssemblerDagcon/hgapCorrection_006of006 | 68.10 minutes        |
| 16469 | PreAssemblerDagcon/hgapCorrection_001of006 | 92.18 minutes        |
| 16470 | PreAssemblerDagcon/hgapCorrection_003of006 | 74.36 minutes        |
| 16471 | PreAssemblerDagcon/hgapCorrection_003of006 | 85.34 minutes        |
| 16473 | PreAssemblerDagcon/hgapCorrection_005of006 | 104.05 minutes       |

### For Thursday

* Search smrtanalysis home directory (sudo su smrtanalysis) for log files (check SMRT Portal manual)
to determine source of crashes

* Also search SGE manual to see if it possible to make a process ONLY go to a single host (as some
jobs appear to have been spread across multiple nodes)

* Jobs still running - 16472 (3 18k), 16474 (1 18k), 16475 (7 21k)
 
* Jobs to repeat - 16476 (6 10k), 16477 (6 9k), 16478 (6 8k), 16479 (2 10k), 16480 (5 15k)

## Evening

Completed jobs - 16472 (3 18k), 16474 (1 18k), 16475 (7 21k)

Restarting the other jobs: 

* (16476) #6: 10000 - 16481
* (16477) #6: 9000 - 16482
* (16478) #6: 8000 - 16483
* (16479) #2: 10000 - 16484
* (16780) #5: 15000 - 16485

# 1 September 2016

All other running jobs failed; attempting to troubleshoot the issue of persistent failures...

Logs for failed processes share this error:  
__IOError: [Errno 28] No space left on device__

Is it possible to move the tmpdir folder to somewhere other than /tmp?

Regarding assemblies that have been successful: three pb_359_7 assemblies have returned
a result of 4 polished unitigs. Investigate further to determine which of these should
be analysed further.  
My first impression is that I should go down the middle and use the 20k (16445) result.

Jobs to rerun:

|    Job                 | Rerun of ID | New  ID |
|------------------------|-------------|---------|
| pb_359_2-10000_Rerun_6 | 16484       | 16490   |
| pb_359_5-15000_Rerun_6 | 16485       |         |
| pb_359_6-10000_Rerun_7 | 16489       | 16491   |
| pb_359_6-9000_Rerun_5  | 16487       |         |
| pb_359_6-8000_Rerun_5  | 16488       |         |
| pb_359_1-???           |             |         |
| pb_359_3-???           |             |         |

Jobs 16490 (+ 16492) and 16491 insta-failed with no log after redirecting tmpdir to another partition.  
Apparent cause - redirecting tmpdir was moving it to another drive, so the mkdir command
was pointing somewhere that didn't exist.

Rather than redirecting tmpdir into another folder, making a tmpdir directory.  
Attempting to run pb_359_6-10000_Rerun_8 (16493) using this configuration...  
Cautiously attempting pb_359_2-10000_Rerun_8 (16494)

Summary of current status of the samples

| Sample     | Status                                                              |
|------------|---------------------------------------------------------------------|
| pb_359_1   | Requires additional assembly job(s)                                 |
| pb_359_2   | Running assembly job                                                |
| pb_359_3   | Requires additional assembly job(s)                                 |
| pb_359_4   | Waiting for rough phylogeny indicator from blastx (still running)   |
| pb_359_5   | Waiting to run assembly job                                         |
| pb_359_6   | Running assembly job; more waiting to be run                        |
| pb_359_7   | Will run blastx once _4 and _8 are complete (16445)                 |
| pb_359_8   | Waiting for rough phylogeny indicator from blastx (still running)   |
| Kordia sp. | Attempting to identify remaining hypothetical proteins using Prokka |

# 2 September 2016

New jobs are taking hours longer than previously. Why...?

How to proceed with remaining samples?
* 1 - 9 polished contigs at 18k and 20k seed read length; push up a little to 21k?
* 2 - 10k seed read length gives 3 polished contigs, number has fallen along with SRL; retry at 8k?
* 3 - 5 polished contigs at 18k and 20k seed read length; push up a little to 21k also?
* 5 - 16495 failed; rerun
* 6 - 8k, 9k and 10k SRL all give 9 polished contigs; step down to 7k?

Initiated the following jobs:
* pb_359_1-21000 (ID - 16498)
* pb_359_2-8000 (ID - 16499)
* pb_359_3-21000 (ID - 16500)
* pb_359_6-7000 (ID - 16501)

Removed '|quiver' from the fasta files as this can apparently cause some issues.  
__Keep an eye on the blastx jobs; this may cause the job to fail inadvertently...__

Rerun pb_359_5-15000 (Rerun 7) (ID - 16502)

P_CeleraAssembler.runCaHgap previously took ~85 minutes; now takes __~552__ minutes

blastx command notes:
* -query_loc command:
 * `-query_loc X-Y`, where X and Y are the limits
 * For fasta files with a single contig, set an arbitrary number of bases to check (e.g. first 5%?)
 * For fastas with multiple contigs, use fp.py --length --header <NAME_OF_FASTA_FILE> | sort -n -r > <NAME_OF_OUTPUT_FILE>
to determine the length of the contigs, then set -query_loc slightly longer than the second contig
* Use 40 cores each to speed things along (progress has been too slow when working with the WHOLE genome
__and__ using only 10 cores, so using less material and more cores should give us faster results

## To Do
* __Reformat 01_assemblies readme with job ID numbers in seed read length columns as with the other tables__
* Blastx for pb_359_7

### Blastx:
* _4: -query_loc 1-175000
* _7 (ID 16445): -query_loc 1-275000
* _8: -query_loc 1-300000

## Evening

* pb_359_1-21000 (ID - 16498) - Done - Retry with 19k
* pb_359_3-21000 (ID - 16500) - Done - Retry with 19k

* pb_359_2-8000 (ID - 16499)
* pb_359_6-7000 (ID - 16501)
* pb_359_5-15000_Rerun_7 (ID - 16502)

* Started pb_359_1-19000 (ID - 16503) - Will be final attempt
* Started pb_359_3-19000 (ID - 16504) - Will be final attempt

# 3 September 2016

Job statuses

| Job ID | Job name               | Status | Downloaded? |
|--------|------------------------|--------|-------------|
| 16499  | pb_359_2-8000          | Done   | Yes         |
| 16501  | pb_359_6-7000          | Done   | Yes         |
| 16502  | pb_359_5-15000_Rerun_7 | Failed | ...         |
| 16503  | pb_359_1-19000         | Done   | Yes         |
| 16504  | pb_359_3-19000         | Done   | Yes         |

Resubmitted 16502 as 16505; changed Genome Size to 4.7m instead of 4.4m, in case erroneous input here
was the cause of the persistent failure even after the hardware problems had been addressed

Try _2 and _6 at 6k - Will be final attempt

Low point of 1 - 9 contigs
Low point of 3 - 5 contigs

Running jobs:
* pb_359_5-15000_Rerun_8 - 16505
* pb_359_2-6000 - 16506
* pb_359_6-6000 - 16507

## Current status of samples
* _1 - contigs have reached a low; examine
* _2 - one final assembly attempt
* _3 - contigs have reached a low; examine
* _4 - blastx (check results)
* _5 - still assembling...
* _6 - one final assembly attempt
* _7 - blastx (check results)
* _8 - blastx (check results)

### Reminder  
Reformat Job ID table
