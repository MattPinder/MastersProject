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
determine which is the appropriate name for _Kordia_. In any case, would be too
time-consuming to name all 4000+ Kordia genes in this way...

# 11 August 2016

Had to stop myRAST's final step - 'Compute correspondences' - part-way yesterday,
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
When performing a similar search with _Kordia sp._ proteins which have already
been given names in the previous analysis, the results I receive are
inconsistent; I don't get the same name as was found previously...

[List of annotation pipelines which might be useful]
(https://omictools.com/genome-annotation-category)

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
hit _Kordia jejudonensis_) which identifies rpsU as a specific hit (with E-value
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

Some _K. algicida_ protein sequences are present on NCBI, including some with
gene names. Checking manually (yet again), I found that PROKKA_01500 from the
aforemetioned .gbk file bears a resemblance to [the preprotein translocase
subunit YajC found on NCBI] (http://www.ncbi.nlm.nih.gov/protein/WP_050765224.1).
Judging by where the alignment starts and ends vs. the _K. algicida_ sequence,
the gene predictor MAY have made a mistake in the alignment...  
_Kordia sp._:  
MIAVLYFLIIAPSLKKQKKEKKFMASVKKGDRVITKSGIHGKIVELNDKDFTCVIETGAGKIKFERAALSVEASARLNNPPAKK  
_Kordia algicida_:  
MVVVVYFFILAPSIKRQKKEKNFMASIKKGDRVITKSGIHGKVVELNDKDHTCVIETGAGKIKFERAALSADATLRLNKPPSEKK  

# 16 August 2016

Small victory?  
Took a partial list of proteins labelled 'Hypothetical protein' in
myRAST_export.xls, and ran it through [Batch Web CD-Search Tool]
(http://www.ncbi.nlm.nih.gov/Structure/bwrpsb/bwrpsb.cgi); some of those
labelled as specific hits included gene names; after comparing a few of these
to Oskar's V5 genbank file, found one of his with no gene name but which
identified a heavy metal-associated domain, which agrees with the CD search's
claim that the gene is the copper chaperone CopZ. Subsequent BLASTP gave a
(perhaps tenuous) match - 68% identity, 4e-37 E-value, 100% coverage - to
_Kordia zhangzhouensis_'s 'heavy metal transporter' gene. Right now, CopZ is my
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

* Check how to set up and configure PROKKA databases; [appears to be possible]
(https://github.com/tseemann/prokka/issues/95)

Created new branch in the kordia_pathway_analysis repository in which to store my
own work.

Have written a script to test the workings of PROKKA, output, etc.
Require tbl2asn 23.0 or higher...

* Create editable folder to store PROKKA DBs (confirm where!)
* Download 3x .gbk files for _Kordia_ and make a PROKKA database (see Oskar's readme for details)
* Find out why the database creation didn't work!  

# 25 August 2016

prokka-genbank_to_fasta_db does not run because it is looking for parent.pm in the
wrong place. Check how to edit @INC to look at
/usr/local/packages/perl-5.14.4/lib/5.14.4/parent.pm

Downloaded Blast2GO, in case this can give any useful information.  
Exporting a DNA fasta file from myRAST for use as input.  
Running blastn first to see if anything new comes up.  

Local BLAST vs database of species shown as similar in Blast2GO?  
e.g. _Flavobacterium psychrophilum_, _Lutibacter_, etc.

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

Startd a Google Docs page to make [notes for my thesis]
(https://docs.google.com/document/d/1_l0IFS5Dkj8g38A57gzm-sVaJx63IGsWnzQb567rwWc/edit?usp=sharing)

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

| Sample       | Status                                                              |
|--------------|---------------------------------------------------------------------|
| pb_359_1     | Requires additional assembly job(s)                                 |
| pb_359_2     | Running assembly job                                                |
| pb_359_3     | Requires additional assembly job(s)                                 |
| pb_359_4     | Waiting for rough phylogeny indicator from blastx (still running)   |
| pb_359_5     | Waiting to run assembly job                                         |
| pb_359_6     | Running assembly job; more waiting to be run                        |
| pb_359_7     | Will run blastx once _4 and _8 are complete (16445)                 |
| pb_359_8     | Waiting for rough phylogeny indicator from blastx (still running)   |
| _Kordia sp._ | Attempting to identify remaining hypothetical proteins using Prokka |

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
 * For fastas with multiple contigs, use `fp.py --length --header <NAME_OF_FASTA_FILE> | sort -n -r > <NAME_OF_OUTPUT_FILE>`
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

## Blastx  
Rerun the three blastx jobs with double (10%) the query length to try and get more conclusive results;
currently seem to be spread across a wide number of species...

### Reminder  
Reformat Job ID table

# 5 September 2016

Investigate why pb_359_5-15000 STILL fails (16505)  
'Unable to verify output' during Celera Assembler stage...  
Rerunning the 18000 run (16508) to see whether sample 5 still assembles

One last resubmission of the three blastx jobs, this time querying 20% of the sum of contig lengths.

Summary of findings from 5% and 10% queries:
* pb_359_4
 * Both 5% and 10% queries returned the same top results; with a bit score of 2220,
___Sphingorhabdus sp. M41___ appears to be the closest match (hit #3 was from the same species,
with a bit score of 1757); hit #2 was from Sphingomonadales bacterium EhC05 (bit score 1843).
 * __Current hypothesis - member of the order Sphingomonadales, potential family
Sphingomonadaceae, potential genus Sphingorhabdus.__
  * Hits lower in the list (e.g. _Sphingobium sp. C100_ and _Erythrobacter_) support at least up to
the order Sphingomonadales.
 * Discovery of _Sphingorhabdus sp. M41_ published just a few months ago
(http://www.sciencedirect.com/science/article/pii/S0168165616301961).
 * _Sphingorhabdus sp. M41_ genome size - 3,339,521 bp
 * pb_359_4 genome size - 3,492,548 bp

* pb_359_7
 * Analysis of the longest contig returned numerous hits to different genera, however the top
three hits for both the 5% and 10% query fell under the family Rhodobacteraceae.
 * __Current hypothesis - member of the family Rhodobacteraceae.__
 * Top hits for the second and third longest contig also all fall under the Rhodobacteraceae
family, along with most of the top hits from the shortest contig; the one that didn't was still
a member of the class Alphaproteobacteria.
 * __Further attempts at assembly may be necessary, as this results is very inconclusive.__

* pb_359_8
 * Both 5% and 10% queries returned the same top results; with a bit score of 2962,
___Arenibacter algicola___ appears to be the closest match (hit #2 was from the same species,
with a bit score of 2777); hit #3 was from _Cellulophaga baltica_) (bit score 2770).
 * __Current hypothesis - member of the family Flavobacteriaceae, potential
genus Arenibacter.__
  * Hits lower in the list (e.g. _Muricauda sp. MAR_2010_75_ and _Sediminicola sp. YIK13_) support
at least up to the family Flavobacteriaceae.
 * _Arenibacter algicola_ known to associate with _Skeletonema costatum_ based on its initial discovery
(http://aem.asm.org/content/early/2013/11/04/AEM.03104-13).
 * _Arenibacter algicola_ genome size - 5,550,230 bp
 * pb_359_8 genome size - 5,839,016 bp

### Status:
* pb_359_1 - Assembly will go no lower than 9 polished contigs
 * Try assembling with seed read length 16k/17k, or attempt blastx analysis?
* pb_359_2 - Assembly will go no lower than 3 polished contigs
 * Try assembling with seed read length 5k, or __attempt blastx analysis__?
* pb_359_3 - Assembly will go no lower than 5 polished contigs (with a 6 in between...)
 * Attempt blastx analysis with 18k/20k seed read length results?
* pb_359_4 - After blastx analysis, appears to belong to the order Sphingomonadales
 * Potential family Sphingomonadaceae, potential genus Sphingorhabdus)
 * Consistent with prediction in 00_data/pb_359 readme
* pb_359_5 - Still waiting for assemblies to complete on account of errors...
* pb_359_6 - Assemby will go no lower than 9 polished contigs
 * Try assembling with seed read length 5k, or attempt blastx analysis?
* pb_359_7 - After blastx analysis, appears to belong to the famiy Rhodobacteraceae
 * May need to attempt reassembly, as genus identity is far from certain...
* pb_359_8 - After blastx analysis, appears to belong to the family Flavobacteriaceae
 * Potential genus Arenibacter (known to associate with Skeletonema)
 * Consistent with prediction in 00_data/pb_359 readme

Unable to find any good reason in the log files as to why pb_359_5-15000 continually fails; will
wait on the results of the pb_359_5-18000 test rerun before deciding how to proceed...

Cancelled blastx jobs with 20% of query length; taking a long time and unlikely to yield any
better results, when all I wanted was a rough phylogeny.  
Will run pb_359_2 at 5% and 10%, as 3 polished contigs seems somewhat reasonable.  
Will use 16458, as the shortest contig in this instance is shorter than in the other three assemblies in which
three contigs were present.

Assembly Job 16509 - copy of 16445 (used for the pb_359_7 blastx), but with a target coverage
of 25 instead of 30; hopefully this will help to bridge the gaps between contigs, in case the
problem lies in areas of low coverage.

Made blastn database of pb_359_7 assembly 16445 (`makeblastdb -in 16445.fasta -dbtype nucl`),
and queried it with itself. Awaiting results to see if contigs match themselves and each other...

Read up on minimus(?) circularisation program in Alvar's thesis

__To try:__ During the next blastx analysis, precede `blastx` with `time`; this should
output information regarding how long the job took.  
Can achieve this in retrospect with `qacct -j ####`

Time to complete 5% jobs:
 * _4: ~2 hours
 * _7: ~9.5 hours
 * _8: ~3 hours

Time to complete 10% jobs:
 * _4: ~4 hours
 * _7: ~14 hours
 * _8: ~6 hours

Time taken is roughly equivalent to the number of contigs in the file, therefore estimate that
the three contigs of pb_359_2 will take ~6 hours and ~12 hours respectively.

__Useful commands:__
* `qstat -j [Job#]` - get information on a specific job in the queue
* `qalter [Job#] -q [New queue name]` - moves a job from its current queue to a new one

# 6 September 2016

Cloned Skeletonema_marinoi_microbiome_project to my home directory, so that nobackup can be
taken offline; __remember to include this clone in push/pulls.__

Job 16508 (copy of older pb_359_5-18000 job) worked, so apparently SMRT doesn't like the
combination of sample 5 and a 15k seed read length. Retry with 16k (job 16510).

Target coverage 25 test for pb_359_7 (job 16509) returned exactly the same results as
with a target coverage of 30; retry one more time with target coverage 20 (job 16511)
before considering alternatives.

Check results for pb_359_2 blastx tests:
* Both 5% and 10% queries returned the same top results; with a bit score of 1892 and 4826
respectively, ___Roseovarius sp. TM1035___ appears to be the closest match (hit #2 of the 10%
query was from the same species, with a bit score of 4812); other hits in the top 3 were:
 * _Roseovarius mucosus_ (hit #2 in 5% query; bit score 1847)
 * _Roseovarius sp. 217_ (hit #3 in 5% query; bit score 1800)
 * _Roseovarius mucosus DSM 17069_ (hit #3 in 10% query; bit score 2498)
* __Current hypothesis - member of the genus Roseovarius.__
 * Hits lower in the list (e.g. _Actibacterium atlanticum_ and _Methyloligella halotolerans_)
support at least up to the class Alphaproteobacteria.
 * [Found associated with dinoflagellates] (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC427730/),
involved in dimethylsulfoniopropionate metabolism ([DMSP metabolism in _S. marinoi_]
(http://www.sciencedirect.com/science/article/pii/S0022098111005429)).
 * _Roseovarius sp. TM1035_ genome size - 4,209,812 bp
 * pb_359_2 genome size - 4,188,132 bp (longest contig)/ 4,415,183 (sum of polished contigs)
* _Roseovarius sp. TM1035_ also appears as the top result for the second longest contig, and
the top result of the third - _P. aquimaris_ - shares Roseovarius' family of Rhodobacteraceae.
 * __Possible need for reassembly?__

Results for pb_359_2, _4 and _8 have thus far been consistent with the preliminary 16S analyses.

__Results of pb_359_7 self-blastn:__ Results blast very well to themselves; implies that there
was an issue with the assembly?

blastn _2 to itself, to try and clarify identity of fragments  
`makeblastdb -in 16458.fasta -dbtype nucl`  
Two longest fragments blast very well to each other, but shortest does not; only one of the
fragments is from an outside source

Extracting sequences from fasta files:  
`samtools faidx [filename].fasta`  
`samtools faidx [filename].fasta [sequence name]:[start-end]`

blasting shortest fragment of _2 to nr database to try and identify it (redundant, in retrospect)

N50 read length from raw data often gives a ballpark figure for a suitable seed read length,
so will run assembly jobs for _1 and _3 at 16k SRL (16512 and 16513 respectively).

### Status:
* pb_359_1 - Attempting an assembly at 16k SRL to try and get less than 9 polished contigs
* pb_359_2 - After blastx analysis, appears to belong to the genus Roseovarius
 * Consistent with prediction in 00_data/pb_359 readme
 * Second-longest contig matches well to the longest; shortest contig matches to neither...
* pb_359_3 - Attempting an assembly at 16k SRL to try and get less than 5 polished contigs
* pb_359_4 - Potentially identified; see yesterday's status
* pb_359_5 - As 15k SRL resulted in persistent failure, yet 18k continues to work,
attempting with 16k to see if this gives any results
* pb_359_6 - ???
* pb_359_7 - All four contigs match well to each other when blastn-ed to themselves; new
approach needed in assembly...?
* pb_359_8 - Potentially identified; see yesterday's status

Started a pb_359_6-5000 job (16514) to see whether going any lower will yield a better result
than 9 polished contigs.  
At the same time, will run a blastx analysis (5% and 10%) on one of the other pb_359_6 jobs
(16496) just in case the number of contigs really won't go any lower.  
Rerunning previous self-blasts (_2 and _7) for .xml output

__Tomorrow - check up on FALCON__

Extract some matched regions in multi-contig samples and blast for identity

2x _6 jobs running
5 assembly jobs running

# 7 September 2016

All 5 assembly jobs from yesterday failed; restarted around 8am, will keep a close watch
* A lot of the jobs failed at unusual times; possible issue with the node?

| Job   | First error                  |
|-------|------------------------------|
| 16510 | 23:49 (no error reported...) |
| 16511 | 00:09                        |
| 16512 | 03:25                        |
| 16513 | 03:26                        |
| 16514 | 04:23                        |

The first of the two _6 blast jobs is STILL running...  
Still running, but some results have already been printed to the output file

Considering how long the sample 6 blast is taking for 5%, 10% job has been deleted; 5% results
so far aren't promising, in any case...  
__Current hypothesis:__ Species of Sulfitobacter, however this contradicts the results
found in the 16S analysis (_1 WAS predicted to be Sulfitobacter, however...)
* Some Sulfitobacter species __are__ known to associate with diatoms, however, including
_Sulfitobacter pseudonitzschiae_, which was the the second-highest blastx result for the
longest contig ([see article] (http://www.ncbi.nlm.nih.gov/pubmed/25278561)).

__Note on blastx:__ Jobs seem to take ~1 hour per 100,000 bases

Jobs 16516, 16517, 16519 failed; 16515 and 16518 still running for now...

__Falcon__
* Three core files - fc_run.cfg, input.fofn and runFALCON.sge - copied to directory.
* Uncorrected reads taken from SMRT Portal, in this case the filtered subreads fasta file.
* input.fofn edited with name of the above fasta file.
* Subdirectories made for seed read lengths of 14k, 15k, 16k, 17k and 18k
* Changed fc_run.cfg `length_cutoff` and `length_cutoff_pr` parameters to the respective
seed read lengths; will leave other parameters as they are for now, and see how these
assemblies compare to the Hgap assemblies

Falcon jobs have been submitted, will examine output tomorrow.  
Falcon jobs finished __very__ quickly in comparison to the jobs from Hgap...

# 8 September 2016

SMRT Portal now reports that only 16515, in fact, failed yesterday; rerunning now as 16520. 
Download 16516-9.

No change in the number of polished contigs for any of the results downloaded...  
Will most likely move on to Falcon after the final HGAP job has completed.

### Observations from Falcon run of _1:
* Used subreads from job 16439
* Five runs tried - 14k, 15k, 16k, 17k and 18k seed read length; all other options left as default
* If I have interpreted the output correctly, all runs gave 8 contigs rather than 9 or 10 as with HGAP
 * 18k has 15 contigs...
* Aside from SRL 18k (1.1 Mb), the other runs estimated a longest contig length of ~3.6 Mb.
 * Max contig length of HGAP assembly of _1 - ~3.6 Mb.
 * Second-longest contigs range in size from ~100 Kb to 1 Mb

| SRL | Note                  |
|-----|-----------------------|
| 14k | 2 linear, 6 circular  |
| 15k | 1 linear, 7 circular  |
| 16k | 2 linear, 6 circular  |
| 17k | 3 linear, 5 circular  |
| 18k | 10 linear, 5 circular |

Attempt Falcon run of _3 (16472)  
Double-check parameters to see whether anything other than SRL ought to be changed  
Range: 15k-22k (28, 6, 5, 6, 5, 8, ? contigs respectively)

Notes on Falcon config options added to 01_assembles folder

Get information on longest contig  
`head -n1 seed_read_*/2-asm-falcon/p_ctg.fa > longest_contig.txt`

### Observations from Falcon run of _3:
* Eight runs tried - 15k, 16k, 17k, 18k, 19k, 20k, 21k and 22k seed read length; all other options
left as default
* The following results were obtained:

| SRL   | Contigs | Longest contig | Note                  |
|-------|---------|----------------|-----------------------|
| 15k   | 5       | 3757283        | 3 linear, 2 circular  |
| 16k   | 6       | 3771166        | 4 linear, 2 circular  |
| 16.5k | 4       | 3842929        | 2 linear, 2 circular  |
| 17k   | 3       | 3822374        | 1 linear, 2 circular  |
| 17.5k | 4       | 3464551        | 3 linear, 1 circular  |
| 18k   | 8       | 1067916        | 7 linear, 1 circular  |
| 19k   | 21      | 426820         | 20 linear, 1 circular |
| 20k   | 26      | 290208         | All linear            |
| 21k   | 21      | 100997         | All linear            |
| 22k   | 6       | 96084          | All linear            |

 * Max contig length of HGAP assembly of _3 between 2.1 Mb and 3.8 Mb (most results sit at 2.4 Mb)
 * Second-longest contigs from Falcon range from ~23 Kb to ~0.8 Mb

Experimental attempt at 16,500 seed read length...  
Results added to the above table.

Another experimental attempt at 17,500 seed read length...  
Results added to the above table.

The 17k result of 3 contigs is a definite improvement over the ~5/6 from the HGAP assembly...

Attempting a Falcon run with sample _2, using subreads from 16458

### Observations from Falcon run of _2:
* Six runs tried - 5k, 6k, 7k, 8k, 9k and 10k seed read length; all other options left as default
* The following results were obtained:

| SRL | Contigs | Longest contig | Note                    |
|-----|---------|----------------|-------------------------|
| 5k  | 3       | 4187685        | 1 linear, 2 circular... |
| 6k  | 3       | 4185067        | 1 linear, 2 circular... |
| 7k  | 3       | 4204009        | 1 linear, 2 circular... |
| 8k  | 3       | 4183327        | 1 linear, 2 circular... |
| 9k  | 3       | 4171540        | 1 linear, 2 circular... |
| 10k | 3       | 4176707        | 1 linear, 2 circular... |

 * Max contig length of HGAP assembly of _2 ~4.2 Mb
 * Second-longest contigs from Falcon 180,096 bp for all SRLs
  * Shortest contigs all 30,281 bp

__Try:__ Run a blastx of the 17k pb_359_3 result; see whether the results from the 'linear'
contig are much different to those of the 'circular' ones

### For tomorrow:
* Check remaining results from _2 Falcon test
 * Results added to the above table
* Check results from _3 Falcon blastx analysis (if complete)

# 9 September 2016

16520 succeeded with a single contig!
200k bases appear to have gone missing...

blastx _5 1-contig result; two jobs running, 5% and 10%, as usual
* Jobs seem to take ~1 hour per 100,000 bases, so jobs should take ~2 and ~4 hours, respectively.

_3 blastx analysis

* Attempt _1 Falcon down to ~7/5k SRL
* Check coverage of contigs that have disappeared, e.g. in _8
* blastx Falcon results

Check blastx results from Falcon run of _3
* With a bit score of 1859, __Loktanella vestfoldensis__ appears to be the closest match
(hit #2 was from the same species, with a bit score of 1840); hit #3 was from Roseobacter
sp. CCS2.
* __Current hypothesis - member of the family Rhodobacteraceae, potential genus Loktanella.__
 * Hits lower in the list (e.g. Sulfitobacter) support placement in the Rhodobacteraceae.
 * [Discovery paper] (http://ijs.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.0300$
 * Loktanella vestfoldensis genome size - 3,063,691 bp
 * pb_359_2 longest contig size - 3,834,127 bp
* Consistent with 16S analysis.

| Job              | Job ID | Status  |
|------------------|--------|---------|
| _5 blastx - 5%   | 5301   | Done    |
| _5 blastx - 10%  | 5302   | Running | *
|------------------|--------|---------|
| _2 Falcon blastx | 5326   | Waiting |
|------------------|--------|---------|
| _1 Falcon - 13k  | 5305   | Done    |
| _1 Falcon - 12k  | 5306   | Done    |
| _1 Falcon - 11k  | 5307   | Done    |
| _1 Falcon - 10k  | 5308   | Done    |
| _1 Falcon - 9k   | 5309   | Done    | 
| _1 Falcon - 8k   | 5310   | Done    |
| _1 Falcon - 7k   | 5311   | Done    |
| _1 Falcon - 6k   | 5313   | Done    |
| _1 Falcon - 5k   | 5315   | Done    |
|------------------|--------|---------|
| _3 Falcon - 14k  | 5316   | Done    |
| _3 Falcon - 13k  | 5317   | Done    |
| _3 Falcon - 12k  | 5318   | Done    |
| _3 Falcon - 11k  | 5319   | Done    |
| _3 Falcon - 10k  | 5320   | Done    |
| _3 Falcon - 9k   | 5321   | Done    |
| _3 Falcon - 8k   | 5322   | Running | *
| _3 Falcon - 7k   | 5323   | Waiting |
| _3 Falcon - 6k   | 5324   | Waiting |
| _3 Falcon - 5k   | 5325   | Waiting |

Where single contigs have been obtained, where did the additional contigs go...?
* pb_359_4
 * Both the SciLifeLab assembly and our own had 1 contig and were within a kilobase of
one another in size; this should be okay.
* pb_359_5
 * The single-contig assembly size was 4,406 Kb; the two-contig assembly size was 4,670 Kb
  * Over 250 Kb lost
 * Compare 16520 (1 contig) and 16461 (2 contigs)
  * The second contig in 16461 has a very high coverage (~350 vs. 200), and length ~250 Kb
  * __Seems likely that a repeat region is the culprit, but perhaps blastn 16461 to itself to confirm?__
* pb_359_8
 * The single-contig assembly size was 5,829 Kb; the two-contig assembly size was 5,924 Kb
  * Around 100 Kb lost
 * Compare 16446 (1 contig) and SciLifeLab (2 contigs)
  * The second contig from SciLifeLab has a very high coverage (~500 vs. 150), and length ~90 Kb
  * __Seems likely that a repeat region is the culprit.__

__To do:__
* Write a tutorial for use of Quiver from the command line
* Blast two-contig results to themselves to determine where the other contig disappeared
to in the one-contig results

Blastx results from pb_359_5:  
Based on 5% results, appears to be a species of Marinobacter, which is consistent with
the 16S analysis. Still waiting on 10%...

Blastn pb_359_5 two-contig assembly (16461) to itself to see whether the high-coverage region
maps well to the larger contig.
* The match isn't perfect (bit score 1836), and some gaps are present...

New _1 Falcon runs complete - 13k to 5k
* Longest contig - new results still 3.5-3.6 Mb
* Number of contigs - still drops no lower than 8 or 9

| Sample   | One contig?                    | Next step                 |
|----------|--------------------------------|---------------------------|
| pb_359_1 | No - assemblers give 8/9       | ???                       |
| pb_359_2 | No - assemblers give 3         | Check ongoing blastx jobs |
| pb_359_3 | No - assemblers give 3+        | Check ongoing Falcon jobs |
| pb_359_4 | Yes                            | Circularise?              |
| pb_359_5 | Yes + self-blast on old contig | Circularise?              |
| pb_359_6 | No - HGAP gives 9              | Try Falcon assembly       |
| pb_359_7 | No - HGAP gives 4              | Try Falcon assembly       |
| pb_359_8 | Yes                            | Try to blastx vs. SSL     |

_6 - 16444: 12k -> 5k

_7 - 16445: 21k -> 5k

| Job    | Queue ID |
|--------|----------|
| _6 12k | 5333     | 
| _6 11k | 5334     |
| _6 10k | 5335     |
| _6  9k | 5336     |
| _6  8k | 5337     |
| _6  7k | 5338     |
| _6  6k | 5339     |
| _6  5k | 5340     |
|--------|----------|
| _7 21k | 5341     |
| _7 20k | 5342     |
| _7 19k | 5343     |
| _7 18k | 5344     |
| _7 17k | 5345     |
| _7 16k | 5346     |
| _7 15k | 5347     |
| _7 14k | 5348     |
| _7 13k | 5349     |
| _7 12k | 5350     |
| _7 11k | 5351     |
| _7 10k | 5352     |
| _7  9k | 5353     |
| _7  8k | 5354     |
| _7  7k | 5355     |
| _7  6k | 5356     |
| _7  5k | 5357     |

__Note:__ Prokka databases now storeable in public folder

[Useful page for Quiver] (http://bioinfo-master.ird.fr:8080/smrtanalysis/doc/bioinformatics-tools/GenomicConsensus/doc/HowToQuiver.html)?

Remember to update Git on Monday morning!

# 12 September 2016

Check new sample 6 and 7 assemblies

_6:  
* 12k to 5k
 * Results range from 8 contigs to 22...
 * Perhaps try a few higher SRL?
  * Perhaps investigate around 11k; longest contig 'circular'

_7:  
* 21k to 5k
 * Results bottom out at 4 contigs...

Check sample 2 Blastx:  
* Repeats the findings of the HGAP assembly's Blastx; likely Roseovarius

Check new sample 3 Falcon assembly:  
* 14k to 5k
* Updated longest_contig, number_of_contigs and second_longest_contig files
 * Still no single-contig result, and seem to have passed over the low point
 * Investigate more values around 17k, e.g. 16750 and 17250?
  * Or change other parameters?

Check sample 5 10% Blastx:  
* Results also suggest that the bacterium belongs to genus Marinobacter

__Current Falcon results:__

| Sample   | Lowest # of contigs | Longest contig | Second-longest contig |
|----------|---------------------|----------------|-----------------------|
| pb_359_1 | 8 (14k-17k)         | ~3.58 Mb       | ~427 Kb               |
| pb_359_2 | 3 (all [5k-10k])    | ~4.2 Mb        | 180,096 bp            |
| pb_359_3 | 3 (17k)             | ~3.8 Mb        | ~110 Kb               |
| pb_359_4 | ---                 | ---            | ---                   |
| pb_359_5 | ---                 | ---            | ---                   |
| pb_359_6 | 8 (11k)             | ~3.5 Mb        | ~428 Kb               |
| pb_359_7 | 4 (5k-16k)          | ~4.7 Mb        | ~372 Kb               |
| pb_359_8 | ---                 | ---            | ---                   |

May be a pointless attempt, but will try to assemble _3 at SRL 16750 and 17250,
just on the off-chance that they yield better results.

Attempt lowering the seed read length of _7 (4k, 3k, 2k), and see whether it
has any effect on the number of contigs.

Attept raising and lowering the seed read length of _2 (2-4k, 11-15k), and see
whether it has any effect on the number of contigs.

Among the 8-contig results for _1, 17k gives the shortest second contig (~400 Kb
vs. ~427 Kb). Try 16500 and 17500 SRL, just in case.

Attempt raising and lowering the seed read length of _6 (2-4k, 13-15k), and see
whether it has any effect on the number of contigs.

__Waiting for...__
* 2x _1 jobs
* 8x _2 jobs
* 2x _3 jobs
* 6x _6 jobs
* 3x _7 jobs

_3 Results:
* Both 16750 and 17250 yielded 3 contigs, so must decide whether to try more jobs in
smaller and smaller increments, or to change some more parameters.
* Longest contig and 16S analysis both support placement in the genus Loktanella,
and the second and third contigs seem to confirm placement in the family
Rhodobacteraceae (the best result in the second and third contigs come from a plasmid...)
* __Compare size of longest contig and Loktanella.__
 * Longest contig ~3.8 Mb
 * Loktanella vestfoldensis genome size ~3.1 Mb, so MUCH shorter
 * L. cinnabarina genome size ~3.9 Mb
 * L. hongkongensis genome size ~3.2 Mb, 2x plasmids (85 Kb and 103 Kb)
 * (Loktanella phage ~57 Kb...)
* __Started a self-blast job as the second and third contigs appear to match the same
 region; will see if they also match any region on the longest contig.__

_7 Results:
* All yielded 4 contigs, as before...

_2 Results:
* All yielded either 3 or 4 contigs; in the cases of 4 contigs (13k and 14k), a ~7k portion
was shaved from the longest contig.

_1 Results:
* 16.5k - gives 8 contigs, the same as previously
* 17.5k - gives 11 contigs, more than before
* Required seed read length seems to lie between ~14k and ~17k, or lower than 5?

_6 Results:
* The 15k result gives 2 contigs, however these are VERY short, so apparently 15k is much
too high...

__Regarding PROKKA:__
Must update from 1.11 to git HEAD version.

Results of _3 Falcon self-blast:
* The two shorter contigs appear to be regions of the longest one, as they appear to be
almost identical.
* Question - how to resolve this so that the genome is assembled as a whole?
* Observation - move from 17,250 SRL up to 17,500 breaks around 10% of the longest contig
off to form the fourth contig...

Results of _2 Falcon (7k) self-blast:
* The longest and second-longest contigs match each other well, whereas the shortest
matches neither.
* Question - does this matching imply an error in assembly, or merely conserved regions
between two different genomes?

Results of _7 Falcon (6k) self-blast:
* All four contigs appear to match each other fairly well, with the exception of the
two shortest, which have a slightly lower match to one another
* Question - as above, does this mean that the matching areas are conserved regions between
genomes, or mis-assembled parts of the same genome?

Results of _1 Falcon (15k) self-blast:
* Still much too fragmented to draw any useful conclusions...

---

/usr/local/packages - clone latest PROKKA repository (sudo git clone)
Find out which script includes hmmsearch (RNAmmer) variable
* Ensure that TIGR HMM loads

Use the command `rsync -hav` to update a directory with the contents of another
(will overwrite any changes, and leave other things as they are.

__Important:__ If you change the contents of a database folder, in order to push
to the nodes, run the `rsyncToNodes.sh` script

__On Tuesday:__
* Update Git!  
* Attempt to run `prokka-genbank_to_fasta_db` again with the Kordia genbank files
 * Be sure to load Prokka vX.XX (1.12-beta...) and NOT 1.11

# 13 September 2016

Yesterday's results added above and committed to repository.  
Run _6 self-blast? - If yesterday's sample 1 run is any indication, this would
yield nothing of value...

Is there any value in trying some assemblies in HGAP again using new SRLs,
tested in Falcon and giving good results, but previously untried in HGAP?
 * _1: In HGAP, tested between 15k and 25k with a minimum between 16k and 20k (9 contigs)
  * In Falcon, a minimum of 8 contigs was found between 14k and 17k
 * Try 17k in HGAP and 16.75k/17.25k in Falcon?

 * _2: In HGAP, tested between 6k and 20k, with a minimum between 6k and 12k (3 contigs)
  * In Falcon, a minimum of 3 contigs was found between 2k and 12k, and at 15k
 * Try 7k and 9k in HGAP and some intermediate values in Falcon?

 * _3: In HGAP, tested between 15k and 25k, with a minimum between 16k and 20k (5/6 contigs)
  * In Falcon, a minimum of 3/4 contigs was found between 16.5k and 17.5k
 * Try 17k in HGAP and maybe more intermediate values in Falcon?

 * _6: In HGAP, tested between 5k and 15k, with a minimum between 5k and 10k (9 contigs)
  * In Falcon, a minimum of 8 contigs was found at 11k (9 contigs between 2k and 10k)
 * Try 11k in HGAP and 10.5k/11.5k in Falcon?

 * _7: In HGAP, tested between 18k and 25k, with a minimum between 19k and 21k (4 contigs)
  * In Falcon, a minimum of 4 contigs was found between 2k and 16k
 * Try some lower values in HGAP (~10k?) and maybe more intermediate values in Falcon?

* Jobs for HGAP (save for this evening)
 * pb_359_1 - 17k - saved
 * pb_359_2 - 7k, 9k - both saved
 * pb_359_3 - 17k - saved
 * pb_359_6 - 11k - saved
 * pb_359_7 - 10k - saved

* Jobs for Falcon
 * pb_359_1 - 16.75k, 17.25k - Submitted - no improvement...
 * pb_359_2 - Intermediates
 * pb_359_3 - Intermediates
 * pb_359_6 - 10.5k, 11.5k - Submitted - both gave the same result as 11k (8 contigs, a low)
 * pb_359_7 - Intermediates

Falcon - based on areas of minimal contigs, attempt the following:
* _1 - 13.5k, 14.5k, 15.5k - submitted
* _2 - 8.5k, 9.5k, 10.5k, 16k - submitted
* _3 - 16.6k, 16.7k, 16.8k, 16.9k, 17.1k, 17.2k, 17.3k, 17.4k - submitted
* _6 - 10.6k, 10.7k, 10.8k, 10.9k, 11.1k, 11.2k, 11.3k, 11.4k - submitted
* _7 - 8.5k, 9.5k, 10.5k, 11.5k - submitted

Results:
* _1: Still yielded no better results...
 * Wait until .6, .7, .8, etc. jobs for other samples have completed before deciding
whether it is worth trying something similar with _1.

* _2: Still yielded no better results, but after 15k the number of contigs begins to
spike again.

* _3: Still yielded no better results...

* _6: Still yielded no better results...

* _7: Still yielded no better results...

__Thought:__ Try running 4, 5 or 8 through Falcon with a seed read length equal
to the one that yielded a single contig in HGAP, and check the output?

Possible problem with the previous attempts at Prokka, aside from potentially
outdated version - the K. algicida genbank file didn't have a sequence at the end...  
Genbank has been updated, and database has been created; __error message appeared about
using invalid initiator or terminator codons,__ but will attempt to use this database
and see what happens.

Kordia database files copied to `/db/prokka/genus` and RSynced to nodes

Problem - tbl2asn not loading correctly again. This occurred with the previous
prokka installation; find what was changed and amend it

__Tomorrow:__
* Check results of additional _7 Falcon assemblies
* Check results of HGAP assemblies on SMRT Portal
* Try and get new Prokka working
* Update Falcon observations table

# 14 September 2016

Download files from SMRT; pb_359_7 run failed and will be abandoned in favour of Falcon

__How does Falcon deal with circular sequences?__

Check whether Falcon can assess coverage...

Check HGAP circular options? - check literature, ask on forum...

Run results through BlastViewer as xml

Tweak project summary to send to Anders...

#### Status

| Sample   | Status                                 | Range (SRL)   | Next step           |
|----------|----------------------------------------|---------------|---------------------|
| pb_359_1 | 8 contigs ('1-3 linear, 7-5 circular') | 14k-17k       | |
| pb_359_2 | 3 contigs ('1 linear, 2 circular')     | 2k-12k, 15k   | View in BlastViewer |
| pb_359_3 | 3 contigs ('1 linear, 2 circular')     | 16.75k-17.25k | View in BlastViewer |
| pb_359_4 | Primary assembly done                  | 10k           | |
| pb_359_5 | Primary assembly done                  | 16k           | |
| pb_359_6 | 8 contigs ('2-5 linear, 3-6 circular') | 10.5k-11.5k   | |
| pb_359_7 | 4 contigs ('1/2 linear, 3/2 circular') | 2k-16k        | View in BlastViewer |
| pb_359_8 | Primary assembly done                  | 20k           | |

BlastViewer incredibly slow-moving on my machine...

Something to try - copy the first and last X bp from the long contig into separate, new contigs,
and see how they match up to one another?

The answer to the linear-circular problem in the Falcon output may lie in the ctg_paths file
(see [Falcon manual] (https://github.com/PacificBiosciences/FALCON/wiki/Manual)).  
"In some case, even a contig is marked as "ctg_linear", it can be still a circular contig
if the beginning node and the ending node are the same but it is not a "simple" path.
One can detect that by checking the beginning and ending nodes if necessary."

Sizes used for self-blasts:
* _2: 7k
* _3: 17k
* _7: 6k

__Observation:__ Appears that start and end node of sample 3 linear contig  are the same; will investigate others...  
(May be relevant - sample 3 has a non-zero `a_ctg.fa` file, which may be relevant to the 'simple' path comment above)
* Same seems to be true of sample 2 (`a_ctg.fa` has size 0)
* Same seems to be true of sample 7
* __Must check that I am understanding the Falcon files correctly; for example, check against the erroneous 2-contig
result from one of the other analyses...__

# 15 September 2016

Cutting the first 10000 characters from pb_359_2 7k Falcon assembly into Sample_2_circular_test;
blast this against the standard 7k assembly and see whether it hits twice, to the beginning and end of the longest contig
* Results - failure; only one hit found, a perfect match at the start of the contig as expected; no match at the end...

Will upload the 2-asm-falcon folder of the three aforementioned self-blasted files to the repository and sync to nodata,
not TOO big to sync to my laptop and will facilitate analyses.

Retry circular test with 7000 bases, just in case
* Results - failure; again, only a single hit was found...

_May be misunderstanding the meaning of the term 'node'..._

Comparing long contig of _2 7k Falcon and HGAP assemblies:
* Longest contig of Falcon assembly: ~4,204,009
* Longest contig of HGAP assembly: ~4,183,457
 * Discrepancy of ~20k, BUT spike in the middle of the log contig's coverage, which could be evidence of a collapsed repeat?
 * Longest contig of 12k HGAP assembly: ~4,188,132
  *Longer contig generates longer sequence, adding support to the idea of collapsed repeats (though spike remains)

### To try
Falcon indicates that the long 'linear' sequences of samples 2, 3 and 7 may in fact be circular; this should be testable in HGAP:
* Cut the long contig of the Falcon assembly in half, then reattach them in reverse: A----B -> A--|--B -> --BA--
* Upload this file as a 'reference' onto SMRT Portal
* Re-run the HGAP 2 assembler, and look at the resulting report; if the construct is truly circular, then coverage should
remain uniform, even over the breakpoint.

For a sequence of, for example 10,000 bases:
* `head -n2 filename | tail -n1 > sequence.fasta` (probably a faster way to do this)
* `cut -c-5000 sequence.fasta > first_half.fasta`
* `cut -c5001- sequence.fasta > second_half.fasta`
* `cat second_half.fasta first_half.fasta > reversed_sequence.fasta`
* Go into the file, remove the newline character (may be possible from command line) and add fasta sequence header.

__Changing from 17k Falcon assembly of sample 3 to 17.1k, as this gives a longer assembly (by 20 Kb) which may resolve repeat regions better__

Files created:
* pb_359_2_Falcon_7k_reversed_halves.fasta
* pb_359_3_Falcon_17.1k_reversed_halves.fasta
* pb_359_7_Falcon_6k_reversed_halves.fasta

__Note:__ May be a single-base indel around the join...

Creating new jobs on SMRT Portal using the references:
* 16531 - pb_359_2-Circularisation_Test
* 16532 - pb_359_3-Circularisation_Test (used 17.1k SRL for HGAP)
* 16533 - pb_359_7-Circularisation_Test (used 20k SRL for HGAP)

Probably a good idea to try the same thing using the single-contigs from samples 4,5 and 8, as these have
not been confirmed as circular yet.
* 4 - Rerun job 16442 with a reference.
 * Reference file name: pb_359_4_HGAP_reversed_halves.fasta
 * 16537 - pb_359_4-Circularisation_Test
* 5 - Rerun job 16520 with a reference.
 * Reference file name: pb_359_5_HGAP_reversed_halves.fasta
 * 16538 - pb_359_5-Circularisation_Test
* 8 - Rerun job 16446 with a reference.
 * Reference file name: pb_359_8_HGAP_reversed_halves.fasta
 * 16539 - pb_359_8-Circularisation_Test

The first step of the process for creating the reversed-halves sequence file is slightly different:
* `tr -d '\n' < filename > sequence.fasta
* Go into the file and remove the fasta header

Waiting on jobs for samples 2, 3, 4, 5, 7 and 8; this still leaves the problematic samples 1 and 6.  
Even in Falcon, these can't be brought to lower than 8 contigs.  
* Check the 15k for _1, as this gives the longest contig.
 * By the node logic used above (explained in the Falcon manual), the long contig appears circular.
* Check the 10.6k for _6, as this gives the longest contig.
 * By the node logic used above (explained in the Falcon manual), the long contig appears circular
(including a second 'linear' contig about 10% of the size of the longest).
  * The two 'linear' contigs also have a simpler unitig path according to the ctg_paths file.

Contig lengths:

| Sample   | Contig length        |
|----------|----------------------|
| pb_359_1 | 3,581,194 (linear)   |
|          |   427,863 (circular) |
|          |   292,780 (circular) |
|          |   284,602 (circular) |
|          |   209,030 (circular) |
|          |   141,938 (circular) |
|          |    99,191 (circular) |
|          |    92,749 (circular) |
|----------|----------------------|
| pb_359_6 | 3,573,472 (linear)   |
|          |   427,989 (linear)   |
|          |   292,881 (circular) |
|          |   284,711 (circular) |
|          |   209,198 (circular) |
|          |   142,087 (circular) |
|          |    92,692 (circular) |
|          |    99,190 (circular) |

Sample 1 has not yet been blastx-ed, whereas sample 6 has, with the suggestion that it is a Sulfitobacter.
Blast two longest contigs from both assemblies?
* Job 6161 - pb_359_1 15k job
* Job 6162 - pb_359_6 10.6k job

# 16 September 2016

Results from assembly jobs with template:
* _2: Results identical to the previous assembly; reference seemingly ignored.
* _3: As above, reference ignored.
* _7: As above, reference ignored.
* _4: As above, reference ignored.
* _5: Assembly failed...
* _8: As above, reference ignored.

Test - rerunning the sample 4 circularisation job, but using the *RS_Resequencing.1* protocol instead
(filtering parameters changed to match HGAP parameters for consistency). If method shows promise,
will repeat with the other samples that failed.

Blastx results: pb_359_1 complete, pb_359_6 should complete around 4.30pm.
* pb_359_1
 * Seems likely that this is a species of __Sulfitobacter__, consistent with the 16S predictions.
 * Suspiciously similar to the pb_359_6 results from previously...
  * Second contig in particular, where hits are found for the SAME protein - formate dehydrogenase -
in the SAME species...

* pb_359_6
 * Awaiting results...

Resequencing complete; results are once again IDENTICAL to the original HGAP assembly, from a look
at the coverage graph...  
blastn of regular and flipped sequences to confirm that the reversal has been successful?
Perfect match; halves have not been reversed...  
Halves now reversed, reference being reuploaded.  
Job being rerun as 16542

Double-check other assemblies; all appear to be okay. Will put the issue with sample 4's reversal
down to human error.

Job 16542 complete. Massive trough in the results around the break point, seems to suggest that this
isn't truly a circular molecule? Will have to investigate...  
Will try samples 5 and 8 in the same way to double-check if the results are the same.
* Sample 5: 16543 - pb_359_5-Circularisation_Test - Result same as before, with a massive trough at the break point.
* Sample 8: 16544 - pb_359_8-Circularisation_Test_2 - As above.  
Will retry with samples 2, 3 and 7:
* Sample 2: 16545 - pb_359_2-Circularisation_Test_2
* Sample 3: 16546 - pb_359_3-Circularisation_Test_2
* Sample 7: 16547 - pb_359_7-Circularisation_Test_2

__Observation:__  
Around the area of the trough, the reports say that there are one or two single-base insertions. Is it
possible that there is a base missing from the end of the assembly which would seal the loop?  
__Something to try__ - run a Falcon job on one of the one-contig HGAP data sets, and see whether the
assembly starts and ends in the same places as the HGAP job.

# 19 September 2016

* Summarise pb_359_6 Blast results
 * Results very similar to those of the HGAP assembly, AND similar to those of 
* DL three circularisation reports
 * pb_359_2 - Coverage over centre not terrible
 * pb_359_3 - Drop in the centre, but still ~50x coverage
 * pb_359_7 - Drop in the centre, but still ~100x coverage

| Sample   | Reference    | Circularisation summary   |
|----------|--------------|---------------------------|
| pb_359_2 | Falcon 7k    | Seems to circularise      |
| pb_359_3 | Falcon 17.1k | Coverage drops to ~50...  |
| pb_359_4 | HGAP 16442   | Coverage drops to ~10...  |
| pb_359_5 | HGAP 16520   | Coverage drops to ~10...  |
| pb_359_7 | Falcon 6k    | Coverage drops to ~100... |
| pb_359_8 | HGAP 16446   | Coverage drops to ~10...  |

Saved consensus sequences to the repository; removing newline characters so that line breaks don't
interfere with searches.

HGAP assemblies are consistently worse than Falcon when it comes to coverage upon flipping halves.
Rerun HGAP jobs in Falcon?  
Run #4 first as a test, and observe results
* Download subread fasta for #4 - Done
* Run in Falcon with the same SRL parameters as for HGAP - Done
 * 40 'linear' contigs obtained from Falcon; attempt other SRL parameters
 * 5k SRL gives a single contig. Will try a few more values to see if longer contigs attainable
  * 3k-7k SRL - 3,487 Kb (or 3,488 Kb) vs 3,492 Kb from HGAP
* Ensure that only a single contig is obtained, and ensure size is comparable
 * Single contig, but ~5k discrepancy...
* Split and reverse-rejoin the two halves of the contig
* Run the result through the resequencer on SMRT Portal
* Check the coverage report

__Note:__ Previous sample 4, 5 and 8 references incorrectly labelled as Falcon; names changed to HGAP,
but ID remains erroneous...

Started job for sample 4 - 16549 - Downloaded  
First two jobs from samples 5 and 8 yielded multiple contigs; going down to 5k SRL

# 20 September 2016

## Falcon

Check 5 and 8 Falcons...
* No success with 5k - try with 3k and 7k

Falcon jobs:
* Sample 5:
 * 3k - 2 contigs, longest 4,384,754 bp
 * 7k - 2 contigs, longest 4,384,754 bp
  * Given the current pattern, should probably go up to 20k SRL
 * 20k - 5 contigs, longest ~1,812k bp
 * 2k - As above (2 contig result)
* Sample 8:
 * 3k - 2 contigs, longest 5,822,105 bp
 * 7k - 2 contigs, longest ~5,822k bp
 * 15k - As above

## SMRT Portal

Regarding sample 4 - massive drop around 1/4 of the way through the sequence, despite cutting
the sequence down the centre; try resequencing using the original sequence as a reference?
* Note - Reference fastas cannot have whitespace in the header line

Running sample 4 resequencing with original, un-inverted Falcon assembly as reference
* Job 16551
 * Obtained a similar coverage pattern for the original Falcon file as for the inverted file.
However, there is a sharp drop in coverage to around ~20x (cf. ~110x) in both results; why?
* SMRT View: 
 * Very low coverage around the area; not sure if this can be trusted...
 * Falcon assembled something that the reads don't back up... How?

## Prokka

Regarding Prokka - tbl2asn still giving problems in the new version; last time the new version
had to be downloaded, so:
* Rename old version just in case
* Copy the new version from prokka-1.11/binaries/linux into prokka-head/binaries/linux
* See if Prokka works, and if so, delete the old version

Prokka now loads tbl2asn, BUT fails during the HMM check and leaves a lot of large files behind...
 * Retry with old PROKKA build...
  * Old version passes the first sets of HMMs, but fails on my custom one...
 * Tried manually loading HMM module
  * No improvement
 * Try resetting the databases using --cleandb and --setupdb (and use old PROKKA build)
  * (May need to try again as root user, as comes up with some issues...)
  * Same error as before, failing on custom DB

Check SMRTView results for circularisation coverage at break points

Blastn samples 1 and 6 against each other
* Sample 1: 15k SRL
* Sample 6: 10.6k SRL

Any noted phenomenon of extra-chromosomal material in Sulfitobacter? e.g. lots of plasmids...
* S. guttiformis - 3 plasmids
 * Only species that seems to have plasmids (according to NCBI...)

Tonight:
* Git push from home directory to nobackup
* Finish blast script
* Run job
