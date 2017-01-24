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

__Note on blastx:__ Jobs seem to take ~1 hour per 100,000 bases (with 40 cores)

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

# 21 September 2016

## 1 vs 6 Blast results
Similarity between the results is INCREDIBLY HIGH! Bit scores:
* 5.2763+06
* 6.328e+05
* 1.405e+05
* 4.607e+05
* 3.836e+05
* 3.069e+05
* 2.396e+05
* 1.267e+05

## pb_359_2
Barring a correction step (must research command-line quiver), this appears to be fine.
* Try original Falcon file for pb_359_2, as after the issues with sample 4 I don't fully trust Falcon...
 * Longest ('linear') contig only
* Job 16555 - circularisation appears to have been successful; will check the area of lowest coverage in
SMRT View to confirm...
 * Aside from the large spike (unresolved repeat region?), __the circular molecule appears to be sound__.
* (Meanwhile, for the remaining two results, check whether Roseovarius sp. have any known plasmids)
 * R. mucosus possesses [4 plasmids] (https://standardsingenomics.biomedcentral.com/articles/10.1186/1944-3277-10-17)
  * Second-highest match in the results for the longest contig
 * Contig 2 - highest hit to Roseovarius sp. TM1035
 * Contig 3 - highest hit to Pseudorhodobacter aquimaris (some lower hits to Roseovarius)

## Status of samples

| Sample       | Status                                                                                      |
|--------------|---------------------------------------------------------------------------------------------|
| pb_359_1     | Assembly still stuck at 8 contigs...                                                        |
| **pb_359_2** | **Long contig appears to be circular; must Quiver-correct the whole assembly**              |
| pb_359_3     | Region of low coverage in the longest contig needs investigating...                         |
| pb_359_4     | Falcon insists that it has found a circular contig, but HGAP reassembly disputes this...    |
| pb_359_5     | Trying to find a single contig Falcon assembly, as circularity of HGAP assembly is disputed |
| pb_359_6     | Assembly still stuck at 8 contigs... Suspiciously similar to pb_359_1                       |
| pb_359_7     | Region of low coverage in the longest contig needs investigating...                         |
| pb_359_8     | Trying to find a single contig Falcon assembly, as circularity of HGAP assembly is disputed |

## Edit Albiorix wiki page (subdivide the manual, etc.)

__To try:__ On sample 8, take 40k from each end of the HGAP assembly and blast them to each other...
* Overlap of ~14400 bases
 * Score = 26504 bits (14352),  Expect = 0.0
 * Identities = 14422/14450 (99%), Gaps = 28/14450 (0%)

* Retry with sample 4 and sample 5 to confirm

 * Sample 4 - More fragmented, but the pattern remains
  * Subject base 1-10163 of Last_40k
  * Query base 27173-37325 of First_40k
   * Score = 18582 bits (10062),  Expect = 0.0
   * Identities = 10138/10170 (99%), Gaps = 24/10170 (0%)
  * Subject base 4014-10163 of Last_40k
  * Query base 20759-26908 of First_40k
   * Score = 11313 bits (6126),  Expect = 0.0
   * Identities = 6142/6150 (99%), Gaps = 0/6150 (0%)
  * Subject base 1-2424 of Last_40k
  * Query base 37588-40000 of First_40k
   * Score = 4394 bits (2379),  Expect = 0.0
   * Identities = 2412/2425 (99%), Gaps = 13/2425 (1%)

 * Sample 5 - Overlap of ~ 19500 bases
  * Score = 35763 bits (19366),  Expect = 0.0
  * Identities = 19536/19605 (99%), Gaps = 63/19605 (0%)

__Useful code for removing newlines from a file__  
`tr -d '\n' < filename > output`

* Run sample 4 blast_ends test again, with xml output to view in BlastViewer?
 * For good measure, rerun all with xml output

## Falcon

Try pb_359_8 at 16k
* Same result as 15k, etc.

__Created a .gitignore file to thin out `git status` by removing Falcon output files__

## pb_359_1 and pb_359_6:
* The results so far:

 * pb_359_1
  * Minimum # of contigs: 8 (between 14k and 17k SRL)
  * Between 1 and 3 'linear' contigs
   * 1 found between 14.5k and 15.5k SRL
   * Looking at the ctg_paths files for the above, the start and end nodes are the same, implying 'circularity'

 * pb_359_6
  * Minimum # of contigs: 8 (between 10.5k and 11.5k SRL)
  * Between 2 and 5 'linear' contigs
   * 2 found between 10.5k and 10.6k
   * Looking at the ctg_paths files for the above, the start and end nodes are the same, implying 'circularity'

* Expected size of a _Sulfitobacter_ genome ranges between 3.45 and 4.95 Mb:
 * _S. pontiacus_: ~3.45 Mb
 * _S. mediterraneus_: ~4.13 Mb
 * _S. donghicola_: ~3.54 Mb
 * _S. guttiformis_: ~3.98 Mb (+ plasmids)
 * _S. noctilucicola_: ~4.09 Mb
 * _S. noctilucae_: ~3.91 Mb
 * _S. geojensis_: ~4.23 Mb
 * _S. pseudonitzschiae_: ~4.95 Mb

* Compare size of longest contig from Falcon assemblies:
 * pb_359_1: ~3.57 Mb - would be a reasonable size for a _Sulfitobacter_ genome
  * Second longest = ~0.43 Mb
 * pb_359_6: ~3.57 Mb - would be a reasonable size for a
  * Second longest = ~0.43 Mb

__Check Alvar's thesis re: handling overlap__  
Otherwise, manually trim one end of the overlap, reverse and correct using Resequencing.

# 22 September 2016

To do:
* Attempt to trim samples 4, 5 and 8 to enable true circularisation
* Try to resolve the issue with samples 1 and 6 similarity
* Find out how to Quiver-correct sample 2
* Check low-coverage areas of 3 and 7

**Making new directory for trimming attempts - 01_assemblies/pb_359_*/Trim**

## pb_359_8
* Where to trim the ends...
 * First_40k-----------------Last_40k
 * --14431                    25560--
 * -14431 from start or -14440 from end
 * Remove less bases; more bases can always be removed later
* **Remove the first 14431 of assembly 16446 and use as reference for Resequencing**
 * Assembly is 5,839,016 bases long, so trimmed assembly should be 5,824,585
 * Should begin 'GATATAGCCTACATG'
* Standard reference: job 16558 - results positive (one big spike...)
* Reversed reference: job 16559 - results positive (as above, one big spike...)

## pb_359_5
* Where to trim ends...
 * First_40k-----------------Last_40k
 * --19556                    20410--
 * -19556 from start or -19590 from end
 * Remove less bases; more bases can always be removed later
* **Remove the first 19556 of assembly 16520 and use as reference for Resequencing**
 * Assembly is 4,406,446 bases long, so trimmed assembly should be 4,386,890
 * Should begin 'TCAAAGCGGGAGGTG'
* Standard reference: job 16562 - results positive (one big spike...)
* Reversed reference: job 16563 - results positive (as above, one big spike...)

## pb_359_4 (1st)
* Where to trim ends...
 * First_40k-----------------Last_40k
 * 1-10163                27173-37325 ?
 * 4014-10163             20759-26908
 * 1-2424                 37588-40000 X
 * --2424                     37588--
 * -2424 from start or -2412 from end
 * Remove less bases; more bases can always be removed later
* **Remove last 2412 bases of assembly 16442 and use as reference for Resequencing**
 * Assembly is 3,492,548 bases long, so trimmed assembly should be 3,490,136
 * Should end 'gaagtgccttgcggg'
  * This makes an assembly of 3,490,135; be aware in case there are any single-base problems
 * Standard reference: job 16566 - results positive - constant ~100x coverage
 * Reversed reference: job 16567 - **results negative - huge dip at the breakpoint**

## pb_359_7
* 'Low coverage area' at centre point of reversed-reference Resequencing run not well-reflected
in SMRT View; in any case, the coverage is still ~100x, so not a clear break point as in some
of the other samples (e.g. pb_359_4/5/8 before trimming overlap); potentially an accetable assembly?

## pb_359_3
* Reference used - 17.1k Falcon assembly
 * SRLs giving 3 contigs range from 16600 to 17250
 * Attempt circularisation with another of these, in case results differ?

## pb_359_4 (2nd)
* Circularisation attempt failed; apparently more trimming is required, at a different point...
* Checking the first 96 bases reveals three hits:
 * Position 1
 * Position 3,479,721
 * Position 3,490,136
* As the trimming from the last of these (2,412 bases) didn't work, attempt to trim from the
first of these (12,827 bases); this would also be of a similar magnitude to the other trims
 * First_40k-----------------Last_40k
 * --10163              27173-37325--
 * -10163 from start or -12827 from end
 * Remove less bases; more bases can always be removed later
* **Remove first 10163 bases of assembly 16442 and use as reference for Resequencing**
 * Assembly is 3,492,548 bases long, so trimmed assembly should be 3,482,385
 * Should begin 'TAGTTTTTGCATTTT'
 * **Not totally convinced on this overlap, considering the Blast results...**
* Standard reference: job 16570 - X
* Reversed reference: job 16571 - X

__Question:__ After the instance of the questionable assembly of pb_359_4 in Falcon should the
suspected plasmids be subjected to an HGAP resequencing attempt to confirm their circularity?

* pb_359_1 -
* pb_359_2 - Longest contig appears to circularise; requires Quiver-correction
 * 'Plasmids' require circularisation test...
* pb_359_3 -
* pb_359_4 - Having trouble resolving the overlap issue; awaiting Resequencing...
* pb_359_5 - Appears to circularise; quality check -> annotation
* pb_359_6 -
* pb_359_7 - Seems to circularise in spite of a questionable drop found in SOME analyses...
 * 'Plasmids' require circularisation test...
* pb_359_8 - Appears to circularise; quality check -> annotation

__Tomorrow:__
* Run 1_vs_6 again with .xml output and examine
* Download the rest of the pb_359_4 second circularisation attempt files
* Pull then push git files (03 folder has been uploaded now)

# 23 September 2016

Downloaded files for the second pb_359_4 trim + circularisation attempt - another failure...  

Git now up-to-date  

1_vs_6 .xml output obtained and checked - contig for contig, the results are almost identical
* Line up the contigs and check for differences?

### Summary

* Circularised, require quality check
 * pb_359_5
 * pb_359_8

* Appears to circularise, additional genetic material needs to be checked
 * pb_359_2
 * pb_359_7

* Appear to be identical, must decide how to proceed
 * pb_359_1
 * pb_359_6

* Still having trouble circularising, explore other assemblies?
 * pb_359_4 - one last trim attempt

* Doesn't circularise well, explore low-coverage region
 * pb_359_3

## pb_359_4 (3rd)
* Gap in the circularisation of ~2 Kb
* Gap in first circularisation attempt had a gap of ~7+ Kb

* Where to trim ends...
 * First_40k-----------------Last_40k
 * --10163              27173-37325--
 * -10163 from start or -12827 from end
* **Remove last 12827 bases of assembly 16442 and use as reference for Resequencing**
 * Assembly is 3,492,548 bases long, so trimmed assembly should be 3,479,721 bases
 * Should end 'AAGTGCCCTTGCGGG'
  * This makes an assembly of 3,479,720; be aware in case there are any single-base problems
 * Standard reference: job 16574 - Appears to have been successful
 * Reversed reference: job 16575 - Appears to have been successful 

## pb_359_3
* Upon checking the breakpoint in SMRT View, the break isn't entirely clear-cut...
 * However, a LOT of reads break off at that point...
* Assembly used: Falcon 17.1k (range of 3-contig: 16.6k - 17.25k)
 * Start: TCTCACCGCTGATTGGCAAG
 * End: ACCTTGCAAAGCAATTCCGA
* Search for the sequence 'ACCTTGCAAAGCAATTCCGATCTCACCGCTGATTGGCAAG' in other assemblies:
 * 16.6k - start and end match 17.1k
 * 16.7k - present in the middle
 * 16.75k - present in the middle
 * 16.8k - present in the middle *
 * 16.9k - present in the middle
 * 17k - present in the middle
 * 17.1k - **current assembly**
 * 17.2k - present in the middle
 * 17.25k - present in the middle
* 16.8k has the second-longest of the long contigs in the 3-contig range, after 17.1k, so will
 attempt to circularise that and compare.
 * Standard reference: job 16578 - Still the peculiar high-low spike...
 * Reversed reference: job 16579 - Still the peculiar high-low spike...

>Sample_1_Contig_1
GCTTTTTGATGCCTGCACAATATCTTGCGGCGCGCCCCTCACTTAGGCGG

>Sample_1_Contig_2
TGATTTGCCGCAACCGGATTCACCCACCAGCCCCAGTGCCTCGCCTGCTG
[Reverse]

>Sample_1_Contig_3
CTTGATCCCGTATTCGGGCACCCAAATCCCGTCATCAGACTGAAACCAAA
[Reverse]

>Sample_1_Contig_4
TGCCGTGAAAAGACGAGCGTAACGCCTCACTGATAGGCCCACGCTCGATA

>Sample_1_Contig_5
TGAAGAGTCTGATCCAATCTCTTGCGGTAGCGGAATCATCAGAGACCTGT

>Sample_1_Contig_6
ATTCCCCTGTCCCGCCAAGACATGCGTCGGCGTGGATCAGCGTGCCCCCA
[Reverse]

>Sample_1_Contig_7
GCGTTGATATCGCCGGACTTCATCCGGCGGTATTCGTCGGCGATCCAGAT
[Reverse]

>Sample_1_Contig_8
GTTGAGCATCCGCGACAGCCTCTTGCGCCTTAACATGCGCCGCTGCCTTG
[Reverse]

# 26 September 2016

## pb_359_3

Could Falcon have accidentally fused the chromosomal DNA to a plasmid sequence? If so, could a
four-contig assembly be a better fit?
* 16.5k SRL assembly has 4 contigs
 * Sizes of the contigs:
  * 3,834,018
  * 110,986
  * 39,367
  * 1,870
 * Size of the contigs from the 17.1k SRL assembly
  * 3,834,121
  * 110,980
  * 39,376
* Sizes almost identical... Falcon is convinced that this assembly is correct, so where is the
discrepancy...?
 * Compare to the contig sizes from the 5-contig assembly from HGAP:
  * 2,388,684
  * 1,487,285
  * 46,106
  * 103,565
  * 69,473
 * Size difference barely comparable...

**Note:** For the HGAP assemblies yielding a single contig, the best SRL was within 2k of the
N50 read length. Same appears to be generally true for Falcon, albeit over a wider range.

To this end - try a ~12k SRL assembly for pb_359_3, and see if this generates a good result
 * Could the 28 contig result at 15k SRL have been a localised peak?
 * Job ID - 16580
  * Awaiting results...

## pb_359_1 vs pb_359_6
* If the samples are going to be spliced to match up, will need to obtain some reverse complement
sequences...
 * Relevant sample 6 sequences reverse-transcribed, start points aligned with sample 1, and new
blastn jobs submitted.
* Result - all samples showed 99% identity, <1% gaps
* Combined with the revelation that their 16S sequences are identical - **These two appear to
belong to the same species, or at least very closely-related species**

This being the case, pb_359_1 would be the best choice for testing circularisation, as this
matches the initial prediction for pb_359_1's identity (*Sulfitobacter*), as opposed to pb_359_6
(16S prediction - *Mari.*).
* pb_359_1 also has a result with a single 'linear' contig and multiple 'circular' contigs;
pb_359_6 has at least two 'linear' contigs in all results.

## pb_359_1
* Sample to use - 15k SRL
 * According to the ctg_paths file, the starting and ending nodes are the same; potentially circular
 * Standard job - 16584 - Several tall peaks, but no severe dips
 * Reversed job - 16585 - One relatively deep dip in the middle (~120x down to ~60x)
  * Definite gap in the coverage, despite a decent number of supporting reads...
  * As with sample 3, there is a large peak beside the dip...

## Observation regarding Quiver
Standard and reversed circularisation jobs using the SMRT Portal Resequencing protocol contain a
Quiver step; is it necessary to run Quiver separately afterwards for further correction...?

## Python
Started work on a Python script to automatically reverse the halves of a sequence. The file is at:  
/home/matt/MastersProject/Sequence_Reverse.py

Tomorrow:
* Check sample 3 assembly job
* Continue to check sample 1
* Attempt to fix Prokka?

# 27 September 2016

**Databases now added to Annotation-4; can run Blast on Annotation-4**

## pb_359_3
Assembly job gave 5 contigs, including a dip in the middle of the longest contig...
* Confirms that the 28 contig result before was merely a local minimum
* Compare to other jobs to see if dip is repeated - coverage dip IS present in another 5-contig assembly
* Consider - **potential issue with contamination, according to Oskar**
* Attempt builds at 11k and 14k SRL?
 * 11k job: 16585
 * 14k job: 16586

## pb_359_1 and pb_359_6
As pb_359_1 has failed to give a circularised chromosome, could pb_359_6 give a better result? Or
would it be the same?
* Compare coverage in reports from pb_359_1 and pb_359_6
 * No steep drops in either, but sample 1 has much higher overall coverage than sample 6
 * Dissimilar enough to at least attempt to circularise 6?
  * According to the 10.6k SRL ctg_paths file, theoretically circularisable...
* Will attempt two circularisation of pb_359_6 10.6k
 * Standard job: 16590
 * Reversed job: 16591

## Python
Have completed and tested my Sequence_Reverse.py script
* Location: Skeletonema_marinoi_microbiome_project/Scripts/Sequence_Reverse.py
* Syntax: `./Sequence_Reverse.py [input file] [output file]`

**Tomorrow**:
* Run two pb_359_6 jobs after adding the relevant references
* Tweak Python script to accept multiple sequences?
* Edit Albiorix wiki/manual page?

# 28 September 2016

## pb_359_3
pb_359_3 jobs failed - rerun:
 * 11k - 16592 - **running**
 * 14k - 16593 - **will run after 11k is complete; many jobs currently running, and suspicious that the last
attempt may have timed out...**

## pb_359_6
Start pb_359_6 jobs once templates are uploaded
 * Standard job: 16590 - As mentioned below, a dip exists which does not appear to be clear-cut. Could be a good assembly?
 * Reversed job: 16591 - Appears to be a dip from ~150x to ~75x, BUT no clean break; could well be a legitimate circularisation
  * Also, break not in the centre of the sequence, as one would expect of the reverse job.
  * High peak of ~140bp at ~230x coverage right before dip.

## Next steps
* **Samples 4, 5 and 8** have single-contig, Quiver-corrected assemblies (initial assembly + Resequencer consensus)
* The longest contig for **samples 2 and 7** has been circularised; must repeat this process for the plasmids
* **Samples 1 and 6** come from, presumably, the same species; must decide which to work with
* **Sample 3** still isn't circularising well; must resolve this

## Prokka
* Retry original script (for Prokka v1.11); renamed PROKKA_Test_1.5.sge
 * Breaks at custom TIGR HMM database...
 * Do I need to run `prokka --cleandb` and `prokka --setupdb` as admin to get them to work...?
  * *sudo* does not seem to recognise the 'module' command?

## To do
* Modify ./bashrc to include path to my Scripts folder, so I can run Sequence_Reverse.py without having to
specify the path each time?

# 29 September 2016

"You could try combining the reads from sample #1 and #6 in a FALCON assembly to see if that has an effect on the resulting number of contigs."

## pb_359_3
* 14k - 16593 - **running**
* 11k - 16592 - completed:
 * Contigs - 5
 * Sum of contig lengths - 4,198,061

* 11k shows massive dip in the centre of the longest contig of the ** HGAP** assembly. Compare to other 5-contig assemblies:
 * (11k - Coverage rises, massive dip just after peak, then slow fall from peak)
 * 20k - No significant drop aside from those at the ends of the assembly.
 * 18k - Sharp drop just before the end of the assembly...
 * 12k - Same sharp drop as 11k
* Blast 20k or 18k against itself, and see if there are overlaps at the end which could be removed,
and circularisation tested?
 * 20k/18k contig lengths vs contig lengths in 3-contig Falcon assemblies:
  * Falcon
   * 3,834k + 110k + 39k
  * HGAP
   * 2,388k + 1,487k + 46k + 103k + 69k
* Try Blasting the HGAP assembly (~250 Kb), and see whether the two longest contigs BOTH match Loktanella;
genome could have been split as in Alvar's investigation...

## pb_359_1 and pb_359_6
Running a Falcon job (11k SRL) for samples 1 and 6 together, to see what kind of assembly results.
* Result was 9 contigs, almost the lowest result seen (same as pb_359_1 at this SRL, but one higher than
pb_359_6 at this SRL)
* Compare contig lengths:
 * pb_359_1 - 11k: 3,580k (L), 142k (L), 99k (L), 43k (C), 209k (C), 427k (C), 284k (C), 92k (C), 292k (C)
 * pb_359_6 - 11k: 428k (L), 73k (L), 67k (L), 284k (C), 209k (C), 3,571k (C), 142k (C), 292k (C)
 * Fusion - 11k: 3,566k (L), 427k (L), 291k (L), 142k (L) 99k (L), 30k (L), 284k (C), 92k (C), 209k (C)
  * VERY similar sizes to the pb_359_1 11k assembly
  * Attempt an assembly with higher SRL, similar to pb_359_1 8-contig assemblies - 15k
* Result of 15k combined Falcon run - 9 contigs (compared to 8 and 2, respectively)
 * Compare contig lengths:
  * pb_359_1 - 15k: 3,581k (L), 292k (C), 99k (C), 92k (C), 284k (C), 141k (C), 209k (C), 427k (C)
  * pb_359_6 - 15k: 10k (L), 6k (L) - **This was a dud result**
  * Fusion - 15k: 3,573k (L), 427k (L), 292k (L), 8k (L), 209k (C), 92k (C), 99k (C), 284k (C), 141k (C)
* Out of curiosity, run a 20k assembly as this hasn't been run on either of the samples individually
 * Fusion - 20k: 40 contigs...
* Run a 13k assembly, as this is midway between 11k and 15k
 * Fusion - 13k: 9 contigs
  * Contig sizes: 3,573k (L), 427k (L), 292k (L), 142k (L), 110k (L), 30k (L), 92k (C), 284k (C), 209k (C)
  * Contig sizes very similar to 11k and 15k
* Run a 17k assembly; pb_359_1 gave 8 contigs with this SRL
 * Number of contigs: 
 * Compare contig sizes:
  * pb_359_1 - 17k: 3,532k (L), 399k (L), 257k (L), 284k (C), 92k (C), 142k (C), 99k (C), 209k (C)
  * pb_359_6 - 17k assembly not attempted
  * Fusion - 17k: **see 30 September**

## Prokka
**Databases now re-done**  
In future:
* `sudo su` (become root user)
* `module load PROKKA/vX.XX`
* `prokka --cleandb`
* `prokka --setupdb`
* `exit`

**Note:** Considering the similarities between pb_359_1 and pb_359_6, treat them as two samples of the
same organism; continue the pipeline using only one, with potential input from the other if problems
are encountered.

## Tomorrow
* Get results from Fusion 17k assembly
* Attempt to get Prokka working again

# 30 September 2016

## pb_359_3
pb_359_3 14k HGAP assembly (job 16593) failed once again. Will retry one more time, and if that fails will
attempt a 13k assembly - the 15k assembly of pb_359_5 failed, only for the 16k run to give the one-contig
assembly I had been hoping for.
* Job 16598 - **running**

__Note on blastx:__ Jobs seem to take ~1 hour per 100,000 bases (with 40 cores)

* 250,000 bp for each contig
* 250k + 250k + 46k + 103k + 69k = 718k = ~7 hours @ 40 cores
 * Currently at 8 cores - 7*5 = 35 hours
 * Started at 13:19 on 29 Sept, should be finished at ~midnight on Friday night
  * Job completed earlier than anticipated

* Results:
 * Incredibly similar results, with _Loktanella vestfoldensis_ still the supposed identity of the longest contig
 * DDE transposase still found on the shorter contigs (with one exception), again with _Confluentimicrobium_
the most likely candidate.
* Now just a case of getting as good an assembly as possible...

## pb_359_1 + pb_359_6 fusion
Final assembly attempt - 17k - completed yesterday.
* Number of contigs: 9
 * Contig sizes: 3,572k (L), 399k (L), 260k (L), 8k (L), 99k (C), 209k (C), 92k (C), 141k (C), 284k (C)
As mentioned above, will treat pb_359_1 and pb_359_6 as two samples of a single species from now on.

## Prokka

Now that the databases have been updated, will attempt to run the Prokka jobs from previously to test whether
it will now run as intended.

* Running Prokka v1.11 - gets stuck at my custom TIGR database.
 * Solution - try re-pressing TIGR database, then retry --cleandb and --setupdb (as sudo)
  * Failed
 * Solution 2 - try implementing [this workaround] (https://github.com/tseemann/prokka/issues/44)
  * Failed
 * Solution 3 - Post a message on the Github Issues page for Prokka, wait for response

## pb_359_1 and pb_359_6 circularisation
Considering the similarities between the two, the best indicator of which assembly to continue with
would probably be which one circularises the best
* pb_359_1 - There appears to be a fairly well-supported break in this assembly
* pb_359_6 - This break is less clear-cut, so this may be the better assembly

## State of circularisation attempts

| Sample(s)     | Current state                                                                                |
|---------------|----------------------------------------------------------------------------------------------|
| pb_359_1 + _6 | 8 contigs _6 appears to circularise better than _1; attempt to circularise plasmids          |
| pb_359_2      | 3 contigs, longest appears to circularise; attempt to circularise plasmids                   |
| pb_359_3      | 3 contigs, big trough in centre of longest; circularisation unsuccessful                     |
| pb_359_4      | Single contig, **seems to circularises**                                                     |
| pb_359_5      | Single contig, **circularises**                                                              |
| pb_359_7      | 4 contigs, longest appears to circularise; check patch near spike, then circularise plasmids |
| pb_359_8      | Single contig, **circularises**                                                              |

## Note
[This] (https://clydeandforth.wordpress.com/2014/06/15/de-novo-bacterial-genome-assembly-part-3/) calls the
'quality' aspect of HGAP2 into question...

## To do
* Check back for reply from TSeemann re: Prokka
 * Check the feedback from the PROKKA_Test_1.5 file
* Wait for results from pb_359_3 14k assembly; if this fails, retry at 13k
* Seek guidance re: 'gaps' in circularised assemblies and need to Quiver circularised assemblies

# 3 October 2016

## PROKKA
* Log file forwarded to software developer, to see if the custom HMM database problem can be overcome
* Script written (Refresh_Prokka_DB.sh) to automate re-pressing of Prokka databases when new ones are added
 * Must be run with sudo

## pb_359_3
* 14k assembly job completed:
 * Number of contigs - 7
 * Assembled contig length - 4,204,689

* Attempting a 10k assembly; will judge based on this whether to continue trying for a better HGAP assembly of sample 3.
 * Job ID - 16599

## pb_359_3 HGAP vs Falcon
* Database - HGAP 18k assembly
* Query - Falcon 17.1k assembly
* Result - definitely appears that Falcon combined the two longest HGAP contigs into one
 * Falcon [28,473 - 2,356,132] for longest HGAP contig ('0' or 'scf...12')
  * Query [28,473 - 2,356,132] [2,333,549 - 2,400,007]
  * HGAP [4 - 2,329,04] [2,395,840 - 2,329,392 {Reverse}]
   * 65k matches reverse compliment at end of '0'. Odd assembly error...?
 * Falcon [1 to 28,194] and [2,376,369 to 3,834,120] for second-longest HGAP contig ('1' or 'scf...13')
  * 300 bp unaccounted for from end of '1'
 * Gaps from [28,194 - 28,473] (~300 bp) and [2,356,132 - 2,376,369] (~200,000 bp)
 * Gaps don't seem to be well-bridged by HGAP...
* Regarding 'plasmids':
 * Long Falcon 'plasmid' matches with some overlap in the HGAP '2' , as expected.
 * Short Falcon 'plasmid' matches with some overlap in the HGAP '3' , as expected.
* What of HGAP '4'?

## Circularisation tests
* Samples whose potential plasmids need to be tested for circularisation:
 * 2 - 7k Falcon assembly
  * Standard job - 16610 - Seems okay
  * Reversed job - 16611 - First 'plasmid' seems okay, second has massive trough in the centre...
 * 6 - 10.6k Falcon assembly
  * Standard job - 16606 - Coverage of 'plasmids' fluctuates wildly
  * Reversed job - 16607 - No halfway troughs to suggest lack of circularisation, but 'bumpy'
coverage in 'plasmids'...
 * 7 - 6k Falcon assembly
  * Standard job - 16608 - Seems okay
  * Reversed job - 16609 - No halfway troughs to suggest lack of circularisation, but 'bumpy'
coverage in 'plasmids'...
* Judging by [this PacBio poster] (http://www.pacb.com/wp-content/uploads/low-input-long-read-for-complete-microbial-genomes-metagenomic-community-analysis.pdf),
the shape of the 'plasmid' coverage graphs is roughly what one would expect.

* Double-check circularisation for the single-contig samples
 * Perhaps make a folder saving only the coverage images?
 * 4 - pb_359_4_Third_Trimmed_Circularisation_consensus.fasta
 * 5 - pb_359_5_Trimmed_Circularisation_consensus.fasta
 * 8 - pb_359_8_Trimmed_Circularisation_consensus.fasta

* Samples 6 and 7 appear to be ready for annotation.

## Quality assurance
* pb_359_4 - one contig
 * Assembly file - pb_359_4_Third_Trimmed_Circularisation_consensus.fasta
  * Based on HGAP assembly 16442 (seed read length 10,000), with overlap trimmed.
 * When viewing centre 'breakpoint' of reversed circularisation test, many low-quality reads
appear in this area, along with a relative small trough in the assembly

* pb_359_5 - one contig
 * Assembly file - pb_359_5_Trimmed_Circularisation_consensus.fasta
  * Based on HGAP assembly 16520 (seed read length 16,000), with overlap trimmed.
 * Coverage spike to ~500x; unresolved repeat region?

* pb_359_6 - eight contigs
 * Assembly file - pb_359_6_All_Contigs_Circ_consensus.fasta
  * Based on Falcon assembly seed_read_10600
 * No particular issues

* pb_359_7 - four contigs
 * Assembly file - pb_359_7_All_Contigs_Circ_consensus.fasta
  * Based on Falcon assembly seed_read_6000
 * Slight dip on the longest contig to ~120x coverage, but this may not be a major issue

* pb_359_8 - one contig
 * Assembly file - pb_359_8_Trimmed_Circularisation_consenus.fasta
  * Based on HGAP assembly 16446 (seed read length (20,000), with overlap trimmed.
 * Coverage spike to ~430x; unresolved repeat region?

## To do
* Decide course of action for pb_359_2 regarding second 'plasmid' which doesn't circularise...
* Decide course of action for assembling pb_359_3
 * Analyse Falcon vs HGAP Blast xml
 * Check 10k SRL assembly attempt
* Double-check the results from the other assemblies to ensure confidence that they are ready
for annotation.
* Should standard or 'reversed' consensus file be used for annotation?

# 4 October 2016

## pb_359_3
* 10k assembly yields the same result of 5 contigs (sum of contig lengths - 4,192,469)
 * Dip in the longest contig; SRL now too low?
 * Will attempt a 22k SRL assembly
  * Job ID - 16612 - No improvement
* From the HGAP vs Falcon XML file, the two long HGAP contigs wrap around the Falcon result
in a way that supports the idea of a circular sequence.

* Determine whether the gaps between the HGAP contigs coincide with the drop in coverage seen
in the Falcon circularisation attempt
 * Used a different Falcon SRL for Blast and for circularisation - must standardise!
  * Falcon for HGAP vs Falcon was 17.1k; for circularisation it was 16.8k
  * Run a circularisation for 17.1k, all contigs
   * Standard job - 16615 - Short 'plasmid' shows a large dip in coverage
   * Reversed job - 16616 - Big drop in coverage in the centre of the assembly...

## Prokka
**Important:**  
rsyncToNodes.sh was incorrect - it was copying nr.* twice, instead of the prokka folder
* rsync file updates, will run and retry Prokka
 * Rerun analysis and see whether it now works - PROKKA_Test_1.7
  * Works perfectly - previous problems down to human error.

* Try using the genus feature, specifying `--genus Kordia --usegenus`, to try and resolve some
'hypothetical protein' identities
 * PROKKA_Genus_Test - 1847 'hypothetical proteins'

* Download new Prokka Bacteria kingdom database from UniProt and replace old:
 * September release to overwrite May release
  * Required installation of Swissknife Perl module
 * PROKKA_Genus_Test_2 - 1846 'hypothetical proteins' - a single hypothetical protein reduction...

* Will try to download and use new Pfam database (hasn't been updated in a long time, it seems)
 * Problem - new database is ~1.3 Tb! Will delete the old Pfam files except the core file, which
I will move to my own directory as a backup.
 * Pfam updated from release (?) to release 30.0
 * PROKKA_Genus_Test_3 - 1789 'hypothetical proteins' - a very modest improvement...

* **Must think of some additional ways to improve the number of proteins identified**

## Using Prokka on current samples
* As far as I can tell, pb_359_6 is ready for annotation. Will therefore attempt to run
Prokka on this sample
 * File used - pb_359_6_All_Contigs_Circ_consensus.fasta
  * 1052 instances of the word 'hypothetical' in the file (this includes all plasmids)
   * 713 in chromosome alone
  * 1993 named genes in chromosome
  * 3538 predicted genes in chromosome
* Add some kind of *Sulfitobacter* database?
 
## Useful commands for extracting information from genbank files, for multiple sequences
* sed -n [start],[stop]p [filename] | grep "[string]" | wc -l
* Useful strings:
 * "locus_tag"
 * "/gene"
 * "/product=\"hypothetical protein\""

## To do
* **Blast all vs all on pb_359_6, to determine if some molecules are circularising in pieces
(as with Kordia).**
* Search for 16S regions - potentially V-Extractor?
* Check for books, papers, etc. on **bacterial genomics**
* Check for papers on Sulfitobacter assemblies?
* Prevalence of transposable elements in bacteria cf. eukaryotes?

# 5 October 2016

## pb_359_6 Self-Blast

* Longest + Third contigs
 * ~7k section (100% identity)
* Fourth + Sixth contigs
 * 3k and 1k sections, ~equally spaced
* Sixth + Shortest contigs
 * 6k and 2k sections, equally spaced (one long sequence?)
* Fifth + Shortest contigs (reverse compliment)
 * 5k, 6k, 5k, 4k, 1k sections, all in roughly the correct orientation
* Seventh + Shortest contigs
 * 3k section

* Search for ~long matches between contigs.
* Set resequencing step with only reads that would span the repeat region, and ensure coverage remains high.
 * Set 13k Minimum Subread Length
 * Job 16617
  * No obvious problems, will try reverse just in case; failing that, will drop to 12k
 * Reverse - job 16618
  * Also no obvious problems...
 * Repeat above with 12k Minimum Subread Length
  * 16619 - As above...
 * Retry at 10k for good measure
  * 16620 - As above...

* Shortest contig - gap between position 8,193 and 9,552

* Check Falcon 10.6k a_ctg.fa file...
 * No alternative contigs...

* Re-perform self-blast as a standard txt output and determine the sequence of these repeated regions...?

 * Match between longest and third contig - 6133 bases (100% identity)
  * Closest match - Roseobacter cell wall-associated hydrolase; however, only 7% query coverage.
  * Some reads to bridge this whole region of the longest contig...
   * Longest - 2,841,974 - 2,848,106 (resides in a slight lull in the coverage)
    * Compared to standard Resequencing job - resides in a relative lull as well)
   * Third - 155,873 - 162,005 (relatively high coverage, but a slight dip in the centre...)
    * Compared to standard Resequencing job - high concentration of lower-quality reads...)

 * 100% identity for such a long sequence seems unusually high...
  * Spliced the contigs so that the repeat starts each contig
  * Created a combined contig with longest at start and third at end:
   []--------------------------------------[]------ (Standard)
   -----------------[]------[]--------------------- (Reversed)
    Where [] is the repeated region.
  * (Longest 3,572,445; third 292,917)
   * Reverse - expect bumps at 1,639,765 and 1,932,682
  * Use as a template for pb_359_6 assembly
   * Would expect a dramatic drop in coverage around [] if there were an issue with assembly
   * Standard job 16622 + reversed job 16623 - Does not appear to be a valid fusion...

 * Match between longest and second contig - 2758/2759 bases (99% identity, 1 gap)
  * Closest match - Oceanibulbus (multispecies) transposase (two regions)
  * Two spaced COG3547 domains. Could this be a repeat region resulting in incorrect assembly?
  * Many reads span this region of the longest contig...

* No strong evidence to suggest that the assembly is incorrect? 

## Bacterial genomics
* Rhodobacterales known to have an [abundance of plasmids] (http://onlinelibrary.wiley.com/doi/10.1111/j.1462-2920.2012.02806.x/full)

# 6 October 2016

## pb_359_2
* Regarding the shortest contig which doesn't circularise
 * All-vs-all blast to see whether it fits elsewhere?
  * Only match is ~1,500 bases with the longest contig...

## pb_359_7
* Assembly appears to be alright
 * Double-checking the self-blast xml file, no obvious areas of overlap
* Attempt Prokka
 * File used - 01_assemblies/pb_359_7/All_Contigs_Circ/pb_359_7_All_Contigs_Circ_consensus.fasta

## pb_359_5
* Only issue with this assembly is a large spike in coverage
 * Blastx spike to see if its contents are relevant
 * Appears to be involved in mercury/heavy metal detoxification- MerA (detoxification of mercury
compounds) and HMA (heavy-metal-associated domain) among them
 * Best matches to mercury(II) reductase in various *Marinobacter* species
* Run Prokka
 * File used - 01_assemblies/pb_359_5/Trim/pb_359_5_Trimmed_Circularisation_consensus.fasta

## pb_359_8
* Only issue with his assembly is a large spike in coverage
 * Blastx spike to see if its contents are relevant
 * Appears to be a transposase gene
  * Best matches to transposase in various *Zobellia* species
   * Strong matches to *Arenibacter*, the predicted genus of this organism
* Run Prokka
 * File used - 01_assemblies/pb_359_8/Trim/pb_359_8_Trimmed_Circularisation_consensus.fasta

## pb_359_4
* Questionable quality of certain areas of assembly; consider re-assembling using a higher
seed read length in HGAP
 * This should result in more reads being used to correct the assembly, which should hopefully
improve its quality.
* New job - 11k SRL (job ID: 16625)

## To do

| Sample   | Course of action                   | Future action                               |
|----------|------------------------------------|---------------------------------------------|
| pb_359_2 | Check peak near start, then Prokka | Check circularisation of shortest contig    |
| pb_359_3 | Prokka                             | Check a_ctg.fa, and troughs; repeat region? |
| pb_359_4 | Blast Falcon vs HGAP, tweak Falcon settings? |                                   |
| pb_359_5 | Prokka                             |                                             |
| pb_359_6 | Prokka                             |                                             |
| pb_359_7 | Prokka                             |                                             |
| pb_359_8 | Prokka                             |                                             |

Check:
* Can PacBio pick up mRNA sequences inadvertently? Peaks in pb_359_5 seem to stack precisely with
some genes, as though picking up only an RNA sequence...

* Will Pathway Tools use the Note field of a Genbank file?

# 7 October 2016

## Number of reads used
With one exception, all assemblies used at least 90% of reads generated
* Exception - pb_359_5 only used 85.8% or reads. Does this denote a problem with the assembly?
 * Not the smallest assembly, but has the lowest number of predicted genes thus far

## Prokka
* Start a preliminary Prokka for pb_359_3
* Check the peak at the start of pb_359_2, then Prokka
 * Blast 3,605,637 to 3,646,291
 * Not as discrete a peak as the previous one, but still almost double average coverage...
 * pb_359_2 - first part of the peak - hypothetical protein/acyl-CoA dehydrogenase (Roseovarius)
 * Second part of the peak - transposase/hypothetical protein/phage protein (Roseovarius)

## Extracting hypothetical protein sequences
* fasta2tab <FASTA_FILE> | grep "PATTERN_TO_SEARCH_FOR" | tab2fasta > <OUTPUT_FILE>
* Find protein identification website

## pb_359_4
* Blast Falcon vs HGAP assemblies
 * Good match, but reverse-complement
 * 99.9% identity, 0.1% gaps

# 10 October 2016

## Find new DBs for Prokka to aid annotation
* Will test the effectiveness of a genus-specific database
 * pb_359_5 - Marinobacter
  * M. hydrocarbonoclausticus
  * M. excellens
  * M. lipolyticus
  * M. algicola
  * M. daepoensis
  * M. santoriniensis
  * M. nanhaiticus
  * M. manganoxydans
  * M. adhaerens
   * + 2 plasmids
  * M. nitratireducens
  * M. subterrani
  * M. psychrophilus
  * M. salarius
  * M. similis
* Running pb_359_5_genus
 * Most gene names have been removed...
 * Re-run using the --addgenes option
  * No improvement...
 * Try using --hmms option to specify all HMMs before Marinobacter database
  * hmmpress /db/prokka/hmm/TIGR
  * No improvement...
 * Specifying a genus means that the Bacteria sprot database ISN'T searched...
  * Use --proteins option to specify Marinobacter database?
* New plan - cut hypothetical proteins out of the resultant Prokka files, and run
Prokka on the hypothetical file
 * Not so simple...
* Compare first and second jobs by eye?

# 14 October 2016
Transferring info from manual_check to pb_359_5_v2.gbk (missed some DUFxxx earlier in the gbk)
3336 done; 3344 next

# 17 October 2016
Completed transfer from manual_check to pb_359_2_v2.gbk
* Will check the genbank in Pathway Tools
* Will create a Pathway Tools instruction guide to remind myself how to run Pathway Tools

Run prokka 3x:
* Standard database (done)
* Standard + ALL Marinobacter (skip cd-hit step)
* Standard + non-hypothetical Marinobacter (skip cd-hit step)
 * fasta2tab <FASTA_FILE> | grep -v "PATTERN_TO_SEARCH_FOR" | tab2fasta > <OUTPUT_FILE>
 * Removed 'hypothetical', 'putative', 'unknown' and 'DUF' (capital and lower-case for the first
three)
  * Leave 'possible' results in; only a handful of hits
* **Remember to run rSync whenever you modify the database!**

* Standard only - pb_359_5
* Standard + ALL Marinobacter - pb_359_5_K+G
* Standard + non-hypothetical Marinobacter -  pb_359_5_K+G_cleaned

Results:

| Run                      | Predicted loci | Named genes | Hypothetical proteins |
|--------------------------|----------------|-------------|-----------------------|
| Standard                 | 4066           | 2357        | 833                   |
| Standard + All Mari.     | 4066           | 198         | 591                   |
| Standard + Cleaned Mari. | 4066           | 204         | 581                   |

Check whether Pathway Tools can output gbk files, and whether it can recognise gene names
from protein products (e.g. locus #3)

## pb_359_2
In preparation for Prokka annotation of pb_359_2, download *Roseovarius* genbank sequences from
NCBI:
* R. nubinhibens
* R. mucosus
* R. atlanticus
* R. indicus
* R. tolerans

## pb_359_3
In preparation for Prokka annotation of pb_359_3, download *Loktanella* genbank sequences from
NCBI:
* L. vestfoldensis
* L. cinnabarina
* L. hongkongensis

## pb_359_4
In preparation for Prokka annotation of pb_359_4, download *Sphingorhabdus* genbank sequences
from NCBI:
* S. sp. M41

## pb_359_8
In preparation for Prokka annotation of pb_359_8, download *Arenibacter* genbank sequences from
NCBI:
* A. latericius
* A. certesii
* A. algicola

 * Having trouble compiling: retry Prokka-genbank_to_fasta_db

* Prepare to present re: Pathway Tools results on Tuesday

# 18 October 2016

## pb_359_5 in Pathway Tools
* Using just the Bacterial database, Pathway Tools identifies 269 pathways
* Using Bacterial + cleaned Marinobacter, Pathway tools identifies 238 pathways

Observations:
* Polyisoprenoid biosynthesis (E. coli)
 * All components present EXCEPT for the first one - IPP -> DMAPP
  * idi gene. Check against pb_359_5 with idi gene (E. coli) as query?
  * idi gene not present in order Alteromonadales (according to NCBI)
   * ispA gene present in one Alteromonadales bacterium (according to NCBI)
  * No hits
   * **Hypothesis: Is DMAPP produced by S. marinoi (or something else in the microbiome?), and
Marinobacter takes care of the rest?**

* Guanosine -> Guanine step missing (but guanine -(hpg)-> GMP present)
* Whole 'superpathway of glyoxylate bypass and TCA' pathway present EXCEPT
(S)-malate -(malate dehydrogenase)-> oxaloacetate enzyme

## Newly-downloaded databases from NCBI
* Arenibacter database still not functioning correctly
 * No CDS data! Redownload available genbanks WITH CDS data
 * Arenibacter database now created

## Pathway Tools
New overviews created for:
* Loktanella (pb_359_3)
* Roseovarius (pb_359_2)

# 19 October 2016

## Pathway Tools
Creating Pathway Tools overviews for:
* Sulfitobacter (pb_359_6)
 * Note - RNA genes found on 'plasmids'...
* Sphingorhabdus (pb_359_7)
 * Unsuccessful - retry...

## pb_359_2
As the smallest 'plasmid' still doesn't circularise, attempt a Falcon run using 1000 SRL
* Must then put results through SMRT Portal

## Canu Assembler
Attempting assembler on pb_359_4
* Once again, a single contig is achieved, though it's apparently non-circular
 * Length - 3,486,666 bp (same region as the HGAP assembly, +/- 10 kbp)
 * Blast against itself to determine overlap
  * Trim the first 7058 bases, and reverse
  * Once some space frees up on the Annotation nodes, start the jobs to run overnight

Potentially try pb_359_6 in Canu to resolve the massive amount of 'plasmids'?
* Check results tomorrow

## Observations
* Loktanella appears to be missing some RNA genes
* Roseovaius appears to also be missing some RNA genes
 * Final step of 'superpathway of dimethylsulfonioproanoate degradation' missing

# 20 October 2016

## pb_359_6
* Canu job still waiting; cancelled, lowered # of CPUs required, and moved to another node.
 * Failed, retry from home directory

## Pathway Tools
* Marinobacter (5) - done; original and plus
* Loktanella (3) - done
* Roseovarius (2) - done
* Sulfitobacter (6) - done
* Sphingorhabdus (4) - waiting... (require pb_359_4 gbk...)
* Arenibacter (8) - done
* ??? (7) - done

## pb_359_4
* Trying circularisation of Canu assembly on SMRT Portal
 * Standard job (16628) is relatively convincing (check result near the start)
 * Reversed job (16629) also relatively convincing (no drop at the midpoint)
* Run Prokka and then attempt to build in Pathway Tools
 * Waiting...

## Current jobs

* Canu - pb_359_6 - take results, trim and reverse, put into SMRT Portal
 * One extra contig (19366 bp, 11 reads); can this be disregarded?
 * Self-blast - trim:
  * First 10,853 of tig00000000
  * First 10,000 of tig00000001
  * First 15,098 of tig00000002
  * First 12,401 of tig00000003
  * First 13,138 of tig00000004
  * First 9,000 of tig00000005
  * First 9,992 of tig00000006
  * tig00000007 has no overlap...
  * First 12,227 of tig00000008
 * Running in SMRT Portal
 * Blast vs Falcon
  * When consensus has been obtained from SMRT Portal

* Prokka - pb_359_4 - take results and put into Pathway Tools
 * Put into Pathway Tools later

## pb_359_6's numerous contigs
* Check GC content of each contig?
* Check coverage graphs/SMRT View
* Check Falcon vs Canu Blast results

# 21 October 2016

## pb_359_6
* Forgot to change the genomeSize parameter; change it now and note any difference...
 * data5 full; run analysis in home directory
 * Slight difference but nothing major
 * Zip pb_359_6

## pb_359_4
* Put into Pathway Tools
* Observations
 * Arenibacter associated with Skeletonema costatum known for PAH degradation; evidence of
this in our Arenibacter

## File compression
* tar -cf [archive].tar [existing files] | gzip > archive.tar.gz
 * Process is killed; intermediate files should be deleted, the rest should be zipped
 * pb_359_6 Canu can also be deleted; results provided no additional information

## sg_edges_to_GFA.py
* Run from inside 2-asm-falcon/ folder
* Downloaded Bandage (graph viewer)
 * Graphs automatically generated by Canu
 * Graphs must be made using the above Python script for Falcon assemblies
  * Requires 0 and 1 folders to run

* Ran on Canu graph for pb_359_4; only one contig shown...
* Running for pb_359_6 10600 SRL
 * One bubble in the 'chromosome', another in the 'largest plasmid'

* Upload Pathway Tools overview (pathways, genes, etc.) to gitlab
* Rerun prokka of Kordia?
* Check Albiorix for .ps to .pdf converter
* Check 'Secondary Metabolite Biosynthesis' for interesting products
 * E.g. trans-lycopene biosynthesis I in Arenibacter
 * Also check hormones and aromatic compounds, and other small groupings
* PowerPoint for Tuesday

# 24 October 2016

Run sg_sequences_to_GFA.py (as opposed to sg_edges_to_GFA.py);
Blast bubbles
Attempt to resolve bubbles (but keep alt. sequence)

Falcon
* Tweak 'overlap filtering options' settings based on average coverage
 (max_diff 3x, max_cov 2x, min_cov 1/4x)

Check SMRT Portal for graph file?
* gfa? Other?

[Regarding potential diatom-bacterial interactions] (http://mmbr.asm.org/content/76/3/667.full#sec-11)

# 25 October 2016

## Genome announcement papers


## Carotenoids
Check whether the yellow and red bacteria show different components of the trans-lycopene biosynthesis pathway

| Species        | Colour | Pathway details    |
|----------------|--------|--------------------|
| Arenibacter    | Yellow | All parts present  |
| Loktanella     | Red    | Final step missing |
| Roseovarius    | Red    | All parts present  |
| Sphingorhabdus | Yellow | All parts present  |

(See also - spheroidene pathway and )

## Pili
Search for pilus-related genes in the genomes
* Definite presence; will need to quantify

## Phylotaxonomic analysis

* Ensure circularisation is complete!

* Check relevant programs and methods in Alvar's thesis
 * New programs may need to be installed on the system
 * Alvar's code for DLing sequences may need to be altered

* Code for DLing sequences - genome_downloader.py
 * Can it download from ftp://ftp.wip.ncbi.nlm.nih.gov/genomes/genbank/bacteria ?
 * OR ftp://ftp.wip.ncbi.nlm.nih.gov/genomes/refseq/bacteria
* Attempting to run the script as-is...
 * Check in the morning...

# 26 October 2016

## Circularisations

| Sample # | Species        | # of contigs          | Circularisation complete?                                                                 |
|----------|----------------|-----------------------|-------------------------------------------------------------------------------------------|
| pb_359_2 | Roseovarius?   | 3 (Falcon)            | Graph - Many chromosome bubbles; Circ - Shortest contig needs work                        |
| pb_359_3 | Loktanella     | 3 (Falcon)            | Graph - 3 chromosome bubbles; Circ - Longest and shortest contigs need work               |
| pb_359_4 | Sphingorhabdus | 1 (HGAP) / 1 (Canu)   | Canu assembly seems to be okay                                                            |
| pb_359_5 | Marinobacter   | 1 (HGAP)              | Circ - appears to be okay                                                                 |
| pb_359_6 | Sulfitobacter  | 8 (Falcon) / 9 (Canu) | Circ - Canu assembly appears sound aside from short 'contig'; Graph - insufficient detail |
| pb_359_7 | ???            | 4 (Falcon)            | Graph - Many bubbles; Circ - appears to be okay                                           |
| pb_359_8 | Arenibacter    | 1 (HGAP)              | Circ - appears to be okay                                                                 |

## PhyloPhlAn

Numerous errors regarding missing modules, plus several which seem to result from not running the
program from its install folder...
**Installing to home directoy for the time being; will discuss options for a global installation later**
Usearch requires version 5.32; does not work with the latest version

## Alvar's genome_downloader.py

Change location of python install in Alvar's script
* NCBI have changed their file structure; must work out how to alter the code

# 27 October 2016

## PhyloPhlAn
Job completed for pb_359_8; adjustment made as per Alvar's instructions to include taxonomic names on the branches:  
IFS=$'\n'; for r in `cat /home/username/programs/data/ppafull.tax.txt`; do id=`echo ${r} | cut -f1`; tax=`echo ${r} | cut -f2`; sed -i "s/${id}/${id}_${tax}/g" /home/username/programs/nsegata-phylophlan-f2d78771d71d/output/job_name/genome.tree.int.nwk; done; unset IFS  
(Varied according to paths in my own directory)

The program places pb_359_8 between Maribacter and Cellulophaga; Arenibacter (the hypothesised species) is a member of the family Flavobacteriaceae (along with Maribacter and Cellulophaga), which is
thus far consistent.  
Where do other Arenibacter species sit in the tree of bacteria, relative to these other two genera?

## genome_downloader.py
Seem to have found the root of the compatability problem between Alvar's code and the NCBI ftp site; need to add 'refseq' into the file path between 'genome' and 'bacteria' partway through
the code.  
Running a four-core jobs on high_mem, plus a (one-core?) job on the login node to see whether there is any time difference.  
No difference whatsoever in time taken between 4 cores and one core. Run on login node from
now on...
The downloads didn't work - need to delve deeper into the file structure to get at the relevant
sequence files...

## General progess
* The following assemblies appear to be okay:
 * pb_359_4 (Canu) - Sphingorhabdus - PhyloPhlAn in progress...
 * pb_359_5 (HGAP) - Marinobacter - PhyloPhlAn in progress...
 * pb_359_8 (HGAP) - Arenibacter? - PhyloPhlAn has been run once; need to DL relevant related sequences to run a smaller PhyloPhlAn job

* The following assemblies need to have the bubbles in their string graphs examined:
 * pb_359_7 (Falcon) - ??? - check bubbles in Bandage...

* The following assemblies need to have their circularisation examined:
 * pb_359_2 (Falcon)
 * pb_359_3 (Falcon)

* The following assemblies need to be generally checked:
 * pb_359_6 (Falcon/Canu)

## pb_359_7
Considering the bubbles, increase the seed read length to determine whether this helps to resolve
them? Current SRL is 6k, so may have trouble spanning certain stretches...
* Values up to SRL 16000 give 4 contigs; perhaps try SRL 16k? If that works, then check
circularisation with a view to using this value instead?

* Bubbles in 6k - 11/1/1/0
* Bubbles in 16k - 1/0/0/0
 * Short path in the current bubble is 19,348 bp long, but 19k and 20k SRLs give 17 and 38
contigs, respectively...
 * An almost-perfect match exists between 000003887 and 000004729, except the latter is almost
30,000 bp (cf. almost 20,000 bp)

* Re-run Falcon job
 * Tweak 'overlap filtering options' settings based on average coverage
(max_diff 3x, max_cov 2x, min_cov 1/4x)
 * Average coverage ~180:
  * max_diff 540
  * max_cov 360
  * min_cov 45
 * Once job is finished, check the number of contigs, then create a string graph with
sg_sequences_to_GFA.py and see whether the bubble has been resolved.
 * Job came back with no results...
  * Retry with these settings, based on the recommendations of the developer:
   * max_diff 360 (2x average coverage)
   * max_cov 540 (3x average coverage)
   * min_cov 5
 * Results give 7 contigs instead... What else can be tweaked?

## pb_359_2 and pb_359_3
As these didn't circularise properly, attempt with Canu?
* Started Canu jobs in home directory (reads files still unzipped)
 * pb_359_2
  * Canu gives three contigs (bubbles file also size 0) - consistent
 * pb_359_3
  * Canu gives five contigs (bubbles file also size 0) - inconsistent with Falcon

## To do
* Adjust Falcon settings to improve assembly of pb_359_7
* Check overlap and circularisation of pb_359_2 and _3 Canu sequences
* Make sure that all files are synced to gitlab

# 28 October 2016

## pb_359_2 and _3
Check overlap, then put into SMRT Portal
* pb_359_2: 3 contigs
 * Contig 1 (tig00000000) - remove first 16,830 bases (should be 4,170,771)
 * Contig 2 (tig00000001) - remove first 14,738 bases (should be 180,122)
 * Contig 3 (tig00000002) - remove first 10,069 bases (should be 30,293)
* pb_359_3: 5 contigs
 * Contig 1 (tig00000000) - remove first 16,012 bases (should be 3,836,915)
 * Contig 2 (tig00000001) - ??? (may be a part of tig00000000)
 * Contig 3 (tig00000002) - remove first 15,928 bases (should be 111,026)
 * Contig 4 (tig00000003) - remove first 13,184 bases (should be 89,752)
 * Contig 5 (tig00000004) - remove first 18,493 bases (should be 39,355)
  * Hypothesis - Contigs 1 and 2 should be joined?

* pb_359_2 standard job - 16648 - shortest contig still a problem
* pb_359_2 reversed job - 16649 - the ends seem to join fine, but problem remains (see above)
* pb_359_3 standard job - 16650 - still problems with first and last contigs (also fourth)
* pb_359_3 reversed job - 16651 - see above

## pb_359_3
Check whether the longest and shortest contigs go together...  
Problem - self-blast was from 17k job; circularisation was from 17.1k job...  
**Must be consistent**

What I would expect - overlap between the start/end of the longest contig, and the area ~3/4 of
the way through the shortest contig.

Best hit between longest and shortest contigs (in terms of bit score): a 2,102 stretch, no gaps,
only two bp difference  
Problem - the sequence matches towards the END of the longest contig, not the start where the
coverage drop occurs...

* Spliced the longest and shortest contigs together, flanked by the shared region. Will try
this with the Resequencing protocol on SMRT Portal
* Job # 16653


## pb_359_7
Attempting Canu
* 4 contigs, consistent with Falcon
* Size 0 bubbles file
* Self-blast and circularise
 * Longest contig - trim first 15,834 bp (expected length: 4,722,943 bp)
 * Second contig - trim first 15,633 bp (expected length: 372,257 bp)
 * Third contig - trim first 18,046 bp (expected length: 154,461 bp)
 * Shortest contig - trim first 17,200 bp (expected length: 81,443 bp)

(Check any matches between different contigs...)

* Standard job - 16654
* Reversed job - 16655


* Check sample 3 splice job and download files
 * Failure

# 31 October 2016

## Checking pb_359_7 jobs
* Standard job - appears at first glance to be okay (check slight dips)
* Reversed job - also appears to be okay at first glance

Check for any matches between contigs, and coverage dips
* Match between second and third contigs of ~4kbp
 * Blasting sequence: area contains potentially two protein genes...
 * Average coverage in the two contigs is different; reasonable to assume that
they truly are different contigs?
* Coverage appears to be reasonable throughout

* pb_359_7 has now been sent to Prokka
 * Numbers of predicted loci and named genes changed fairly drastically... Investigate!
  * Ensure Prokka database has been synced correctly to all nodes

## pb_359_5 and _8
* Conflicts in the assembly cannot be verified; reperform with Canu?
 * Canu jobs started in home directory (be sure to sync results to data5 when completed)
 * Numbers of contigs inconsistent... Investigate!

# 1 November 2016

## pb_359_5 and _8
* After Canu jobs the following results were obtained:
 * pb_359_5 - 2 contigs (albeit one very poorly supported...)
 * pb_359_8 - 3 contigs, one with moderate support (and one with negative support?)
* Both 'bubbles.fasta' files are blank, however

Approximate sizes of assembly/longest contig

|          | HGAP              | Falcon             | Canu               |
|----------|-------------------|--------------------|--------------------|
| pb_359_5 | 4,406k (1 contig) | 4,384k (2 contigs) | 4,403k (2 contigs) |
| pb_359_8 | 5,839k (1 contig) | 5,822k (2 contigs) | 4,877k (3 contigs) |

For _5:
* Falcon finds a second contig of ~241k
* Canu finds a second contig of ~264k (poor support)

For _8:
* Falcon finds a second contig of ~64k
* Canu finds a second contig of ~960k
 * Canu also finds a third contig of ~87k (poor support)

For pb_359_5, genome size was previously set to 4.5m
* Attempting at 4.4m
 * No bubbles
 * Once again, 2 contigs (once again, the second contig has ~low support)

For pb_359_8, genome size was previously set to 5.3m (this appears to have been an error...)
* Attempting at 5.8m
 * No bubbles
 * Once again, 3 contigs (once again, the third contig has negative coverage)

## pb_359_2
Both Falcon and Canu are convinced that there is a third contig, but it looks like an M in
terms of coverage, with an obvious dip in the middle.
* What is contained within this contig? Blast first ~10k bases
 * None of the best hits are to Roseovarius or Roseobacter, the two proposed genera...
* Blast next ~10k bases
 * A few of the best hits are to Roseovarius
* Blast final ~10k bases for completeness
 * Again, no convincing Roseo* hits

* Looking at the self-blast results:
 * In the Falcon assembly, the shortest contig has no hits to the other two
 * The same is true in the Canu assembly



## pb_359_3
HGAP and Canu believe there are 5 contigs, whereas Falcon says there are 3
* All show massive dips in the assemblies of the longest contig; for
HGAP and Canu, these also exist in the shorter contigs...
 * The coverage always drops to ~50
* Tweak settings of Canu to try and obtain 3 contigs with it?
* Check string graph of Falcon assembly?
 * Three bubbles in the chromosome, two of which are huge.
* Self-blasts of both Canu AND Falcon assemblies give some fairly large hits between contigs...
* Alter Falcon settings re: coverage? (using 17.1k SRL as reference)
 * Average coverage 177.93 (~180)
  * max_diff: 360
  * max_cov: 540
  * min_cov: 5
 * This resulted in 9 contigs...

Re: Falcon settings on overlap:  
"What is the right numbers used for these parameters? These parameters may the most tricky ones
to be set right. If the overall coverage of the error corrected reads longer than the length cut
off is known and reasonable high (e.g. greater than 20x), it might be safe to set min_cov to be 5,
max_cov to be three times of the average coverage and the max_diff to be twice of the average
coverage."

* In Falcon, 3-contig assemblies range from SRL 16600-17250 (inclusive)
 * Resultant files have since been deleted; rerun jobs in home directory...
  * 16600, 16700, 16750, 16800, 16900, 17000, 17100, 17200, 17250
 *All have bubbles...



## pb_359_6
No blatant issues with coverage, but a curious patch in the longest contig...
* In Falcon, 8-contig assemblies range from SRL 10500-11500 (inclusive)
 * 11,400 and 11,500 both have size 0 a_ctg files; switch to these assemblies instead?
 * Problem - not circular!



## Questions:
* pb_359_2 - Can the third contig be disregarded? Poorly supported and doesn't circularise at
all...
* pb_359_3 - Why will longest contig not assemble? Similar issue with shorter contigs (working on
re-running some Falcon jobs...)
* pb_359_5 - Can the HGAP assembly be accepted, despite no string graph or bubble files to
determine conflicts?
* pb_359_6 - Can the tiny contig (poorly supported) in the Canu assembly be disregarded? Also,
can the Falcon assembly's chromosome bubble be resolved?
* pb_359_8 - Can the HGAP assembly be accepted, despite no string graph to bubble files to
determine conflicts?


* pb_359_4 and _7: Pleased with the assemblies, and genbanks have been produced. 
 * pb_359_7 still needs to be loaded into Pathway Tools
 * Both need to be run through PhyloPhlAn
  * Via home directory...
  * 4 has already been run; 7 is currently being run and must be moved from the home directory
into data5

## To do
* Rerun Pathway Tools for _4 and _7 (note which assemblies are used), and name them
such that you know they use the final assembly
* Work out why FigTree won't output images anymore!
 * Appears to output them now that Java has been updated...

# 2 November 2016

Try Figtree through Albiorix using sudo
* Would require sudo su...

## pb_359_5 and _8
Both sequences circularise well; the only issue is the coverage spike composed of many short
reads (~1-5kb), present in both samples... Can this be disregarded?
* Upload Falcon/Canu reference to see whether they also find this spike
 * 16k Falcon assemblies...
 * _5 job ID: 16662
 * _8 job ID: 16663

## pb_359_4 and _7
New Figtree strategy - max zoom, then export as jpg for inspection
* Does not work...

## Downloading files for FigTree
urlretrieve doesn't support wildcards, so may no longer be possible to automate download of the required sequences...
* Will have to download by hand?

## pb_359_6
Late observation - the longest 'plasmid' in pb_359_6 is 428k. MUCH too big for a plasmid?
* Adding together the 'chromosome' and the biggest plasmids would still give a reasonable size for a complete genome...
* Looking back at the preliminary Blast results, certain of the contigs matched Sulfitobacter, others matched Roseovarius (pb_359_2?)
 * Blast pb_359_2 and _6?
 * Falcon - _2 SRL 7k vs _6 SRL 10.6k
* Expectations:
 * pb_359_2 - Two longest contigs matched Roseovarius, smallest matched Pseudorhodobacter/Thioclava/Oceanibulbus
 * pb_359_6 - ~302k and ~104k contig matches Roseovarius, ~153k contig matches Roseo/Puniceibacterium
* Lots of matches spanning a couple of kilobases, but nothing huge EXCEPT one hit of 91% identity across ~13.7k
 * 180,096 bp contig of pb_359_2 vs 92,692 bp contig of pb_359_6
 * Blasting sequence...
  * Match of ~800 bp to 'type IV secretion system"

Add a newline after every Nth character:
sed -e "s/.\{N\}/&\n/g" < file.txt



Check assembly sizes for _5 and _8. If all assemblies come to ~ the same size, use HGAP
* pb_359_5
 * HGAP 16K   - 1 contig  - 4,406K
 * Falcon 10K - 2 contigs - 4,626K
 * Canu       - 2 contigs - 4,667K

* pb_359_5 is using only 85% of reads, cf. 90% as with the other samples. HGAP assemblies
with a higher SRL/more contigs had an assembly size more comparable to the other assemblers...
* pb_359_5 14k job?
 * 16664

* pb_359_8
 * HGAP 20K   - 1 contig  - 5,839K
 * Falcon 10K - 2 contigs - 5,886K
 * Canu       - 3 contigs - 5,924K

* pb_359_8's initial assembly (SciLifeLab) was 2 contig, but it was a slightly bigger assembly,
around the size of the Canu assembly...

## To do

* Solve size discrepancies between the various assemblies of pb_359_5 and _8
 * Check sample 5 14k job (16664) on SMRT Portal

# 3 November 2016

## pb_359_5
Job 16664 returned two contigs, the second of which measured ~250k bases, but uses ~92% of the
reads
* Previous, one-contig assembly contained only 85% of reads
 * Compared to the contig size of Marinobacter hydrocarbonoclasticus, this size is reasonable
* New hypothesis - pb_359_5 contains a chromosome plus a plasmid.
 * Attempt to circularise the Canu/Falcon assembly
 * Check string graph for 10K Falcon job
  * A lot of complex bubbles...

## genome_downloader.py
Make a fork of Alvar's code, using wget instead of urllib to extract files (wget accepts
wildcards)
* https://www.ncbi.nlm.nih.gov/books/NBK25501/
 * Useful for retrieving accession numbers?
* Need wget to be installed...


## pb_359_8
Unconvinced by the single-contig assembly of HGAP; attempt surrounding SRL values to test
the environment.
* SRL 18k - job 16667
* SRL 21k - job 16668

## CompleteCode.py
Code is approaching preliminary completion; solve problem of URL not accepting strings
as part of the address...

# 4 November 2016

## pb_359_5
Job 16666 (12k SRL) failed; retrying...
* Something preventing certain SRLS from assembling in sample 5...?

## pb_359_8
* 18k SRL (16667) - 1 contig, still a little shorter than the Falcon and Canu assemblies...
* 21k SRL (16668) - 1 contig, still a little shorter than the Falcon and Canu assemblies...

## NCBI_Downloader.py
Preliminary working version created, and seems to be working well so far. Need to add more user-friendly
components, but otherwise functional.

## To Do
* Solve problem with remaining assemblies
 * pb_359_5 may be near completion; check last job, then attempt to circularise a 2-contig assembly (Canu?)
 * pb_359_2, _3, _6, _8...
* Get a phylogenetic tree for pb_359_7 using PhyloPhlAn and NCBI_Downloader.py
* Complete creation of pb_359_4 phylogenetic tree

# 7 November 2016

## pb_359_5
12k SRL assembly of pb_359_5 complete; assembly size still comparable to Falcon and Canu
2-contig assemblies.
* Conclusion - genome is ~ 4.68Mb, with a ~4.4Mb chromosome and a ~200Kb plasmid.
* Circularisation and quality must now be checked...

Given that 2-contigs appears to be the true shape of the genome, it is feasible that the Falcon
and Canu assemblies are, in fact, accurate. Therefore, circularisation and string graph bubbles
must be checked
* String graph of 10k Falcon job - VERY bubbly, including some very complex bubbles
* Check a_ctg file sizes for other size assemblies of comparable size
 * 16k has a smaller a_ctg file (but the p_ctg file is missing...) so will perform more
Falcon assemblies around this value to try and find a minimum amount of bubbles.
 * 11k, 12k, 13k, 14k, 15k, 17k, 18k, 19k (and redo 16k for comparison)
 * Running from home directory; tar will have to be rezipped and resynced with data5
* Looking at the stats, 18k SRL has the smallest amount of alternate contig data...

## pb_359_4
Having to re-run PhyloPhlAn because of a naming error; if this persists will have to mass-replace
spaces with underscores in the FASTA headers (additional section of the code?)
* NCBI_Downloader.py has been updated as described above.
* Rerunnng PhyloPhlAn now...

## Other unfinished assemblies
* pb_359_2 - Shortest contig never circularises
* pb_359_3 - Longest and shortest contigs never circularise
* pb_359_6 - Am I convinced that all of the 'plasmids' in this sequence are legitimate?
* pb_359_8 - Conflict in assembly sizes and numbers of contigs...

## pb_359_8
Assembly size of 15k SRL is comparable to the previously-checked 10k SRL, BUT a_ctg.fa is blank!
* Run sg_sequences_to_GFA.py and check this assembly instead.
 * Despite the emptiness of the a_ctg.fa file, the other a_ctg* files weren't empty, and so
the resultant string graph still contains some bubbles...
 * Try some other assembly sizes?
  * Are the bubbles relevant, if the a_ctg.fa file is empty?
  * Cannot find an explanation of the difference between a_ctg_all.fa, a_ctg_base.fa,
a_ctg_base_tiling_path, a_ctg.fa and a_ctg_tiling_path...
 * The bubble in the 'plasmid' occurs between two nodes of ~17.7Kb and ~19.6Kb
 * BLASTing vs the ~17.7k node shows extensive repetition...
  * Would a SRL of 18K resolve this?
 * Attempt 18K and a few surrounding values...
  * 17k, 18k, 19k
 * Running from home directory; tar will have to be rezipped and resynced with data5
 * 17k yielded 2 contigs; 18k yielded 4, 19k yielded 8...
 * 18k and 19k have 0 file size on all a_ctg files...

## pb_359_7
Phylotaxonomic group must be identified in order to shrink the tree.
* PhyloPhlAn 1.4.3 appears faster than 1.4.2 on my computer for handling huge trees, so
should be able to sift through more easily.
 * Dowload sequences from family Rhodobacteraceae
 * Running PhyloPhlAn job...

* pb_359_4 running PhyloPhlAn
* pb_359_5 running Falcon
* pb_359_8 running Falcon

* pb_359_7 running PhyloPhlAn

* pb_359_2 - massive coverage dips
* pb_359_3 - massive coverage dips
* pb_359_6 - so many contigs

# 8 November 2016

## PhyloPhlAn
Samples ran successfully, will visualise them in Figtree...
* pb_359_4 - May be worth searching GenBank for sequences alongside RefSeq, but seems likely at
first glance that this is a species of Sphingorhabdus, as predicted.
* pb_359_7 - Stands alone, seems related to Mameliella alba and Ruegeria sp. PBVC088, but
might be worth looking at GenBank as well, as no Antarctobacter species were found in RefSeq...

## pb_359_8
Try 17.5k Falcon assembly?
* 17k gives 2 contigs but bubbles remain; 18k (and 19k) give more contigs, but no bubbles...
 * Job submitted; will need to redo the tar and gzip files...
 * Result - 4 contigs, but with a_ctg* files of non-zero size...
* Check whether the 17k assembly gives serious bubbles in the string graph, and if it will
circularise...
 * Standard job - 16672
 * Reversed job - 16673
 * Two bubbles in the long contig, and not circular...

## pb_359_5
Remove some files to make the .tar file manageable...
Retain files with smallest a_ctg* files; keep 17/18/19



* pb_359_2 - COVERAGE DIPS
* pb_359_3 - COVERAGE DIPS
* pb_359_4 - Improve annotation? Otherwise write report
* pb_359_5 - MUST RESOLVE STRING GRAPH BUBBLES
* pb_359_6 - RESOLVE MASS OF CONTIGS
* pb_359_7 - Improve annotation and tree? Otherwise write report
* pb_359_8 - MUST RESOLVE STRING GRAPH BUBBLES

## pb_359_6
pb_359_6 10.6k Falcon assembly has a single chromosome bubble
* Rerun sample 6 jobs to double-check whether any of these give better results in terms of
bubbles?
 * This has been done, unsuccessfully

Note: Canu jobs have not been tested in SMRT Portal for samples 5 or 8...

* pb_359_5
 * HGAP 16K   - 1 contig  - 4,406K
 * Falcon 10K - 2 contigs - 4,626K
 * Canu       - 2 contigs - 4,667K

* pb_359_8
 * HGAP 20K   - 1 contig  - 5,839K
 * Falcon 10K - 2 contigs - 5,886K
 * Canu       - 3 contigs - 5,924K

Check these two for circularisation...?
* Use pb_359_5 version rather than pb_359_5_2
* Use pb_359_8_2 version rather than pb_359_8
 * Canu results must first be trimmed...
 * Before trimming, must be blasted

## To do:
* Check overlap in samples 5 and 8 Canu, with a view to trimming and circularising them...

# 9 November 2016

## pb_359_8
Surprisingly, despite yesterday's comments, the 17k Falcon assembly SEEMS to circularise.
* Still need to address the bubbles in the string graph, however...

## Canu
Trim the Canu assemblies of samples 5 and 8
* pb_359_5
 * Longest contig: trim first 17,082 bases (length: 4,403,956 to 4,386,874)
 * Shortest contig: trim first 21,124 bases (length: 264,537 to 243,413) - questionable...
 * Standard job - 16676
 * Reversed job - 16677
* pb_359_8
 * Longest contig: trim first 
 * Middle contig: trim first
 * Shortest contig: trim first
  * Attempt when BlastViewer decides to work...

## pb_359_5
Recently-announced species of Marinobacter (http://genomea.asm.org/content/4/5/e00937-16.full),
compare to pb_359_5 once assembly is complete.

In preparation for pb_359_5 phylotaxonomic placement, downloading Alteromonadaceae family
sequences for comparison.
* REMEMBER TO INCLUDE pb_359_5 .faa FILE ITSELF IN THE ANALYSIS!!!
* Making a preliminary tree or the sample
 * Based on this, it would appear that both sample 5 AND the above-mentioned species (MCTG268)
are very closely related, alongside M. salarius.

After checking the Canu assembly, the second contig circularises poorly BUT even the low-coverage
area is at ~200x. The overlap wasn't entirely clean, so perhaps this needs to be reassessed?

## pb_359_8
Still need to assess 'circularisation' of pb_359_8, if BlastViewer will work...
* Download Flavobacteriaceae

# 10 November 2016

## pb_359_8
* Downloading files for small tree.
 * Building preliminary tree...
 * Preliminary tree supports its placement as a species of Arenibacter
* BlastViewer STILL not working... Attempt to redo the Blast analysis and see whether it's just
a fluke that the first file isn't working.
 * There are 2000+ HSPs in one of the contigs alone. Feasible that it's just taking a long time
to load on account of the number of hits. Will leave it for a few hours and see if it works...

## PhyloPhlAn
While waiting for BlastViewer, will attempt to make preliminary trees for the other three
samples:
* pb_359_2
 * Pre-emptively download files based on 16S prediction; Roseovarius, so DL Rhodobacteraceae
  * Can just transfer over from pb_359_7
 * Closest relatives do, indeed, appear to be Roseovarius
* pb_359_3
 * Pre-emptively download files based on 16S prediction; Loktanella, so DL Rhodobacteraceae
  * Can just transfer over from pb_359_7
 * Closest relatives do, indeed, appear to be Loktanella (esp. vestfoldensis)
 * Combine pb_359_2 and _3 trees?
* pb_359_6
 * Pre-emptively download files based on 16S prediction; Sulfitobacter, so DL Rhodobacteraceae
  * Can just transfer over from pb_359_7
 * Seems (distantly) related to Sulfitobacter?
 * Combine pb_359_2, _3 and _7?

Attempt individual big trees, then if they hypothesis is correct, can combine them into a small
tree.

## pb_359_2 and _3
Both of these assemblies give at least contig with a massive dip in coverage. How to resolve?
* Altering settings in Falcon? If so, which ones?
 * Rerunning pb_359_2 15k job; see how this compares to the 7k that is my current standard
 * pb_359_3 17.1k has a couple of big bubbles, plus there's something not right about the
smallest contig...

## pb_359_5
After asking about the Canu assembly of pb_359_5, and the results of the circularisation, the
result appears to be acceptable.
* Although coverage on the short contig is on average ~350, with a dip to ~200, 200x coverage
is still very high, and the reads supporting it are long (most are between 11Kb and 24Kb)
 * In this case, annotation should be performed on this assembly in Prokka.

## Marinobacter
Things to compare between pb_359_5 and MCTG268:
* # of genes
* 16S sequence similarity
* GC ratio
* Synteny (test with MAUVE)
* Etc. 

## Currently-running jobs
* pb_359_5 Prokka

# 11 November 2016

## pb_359_5
Prokka has now completed its annotation:
* The numbers for the longest contig are comparable to the previous assemblies
* There were additional genes found on the new second contig, implying that these had, indeed,
simply been missed in the previous assemblies

* Make individual tree - done
* Run through Pathway Tools - ongoing

* Comparison to MCTG268 (http://genomea.asm.org/content/4/5/e00937-16.full)
 * Only one of the contigs from MCTG268 had any matches at all to the shorter plasmid.
  * BLAST this section of pb_359_5 shortest contig: 140,128 - 152,004
   * 150,579 - 152,004 (10,451 - 11,876)
   * 149,705 - 150,355 (9,577 - 10,227)
   * 140,128 - 140,799 (1 - 671)
  * Top two almost match to a superfamily I DNA/RNA helicase from M. hydrocarbonoclasticus
  * Blast the above individually...
   * Good match to superfamily I DNA/RNA helicase from M. hydrocarbonoclasticus
   * Mediocre matches to five Marinobacter proteins; best: superfamily I DNA/RNA helicase
    * M. hydocarbonoclasticus
   * Mediocre matches to two M. hydrocarbonoclasticus hypothetical proteins
  * Blasting the best two matches together gets a good match to the same DNA/RNA helicase across
the whole length of the query

* Tried installing Mauve but the program will not cooperate.
* 16S sequence similarity - check SILVA database

# 14 November 2016

## pb_359_5
Mauve now installed; running an alignment between pb_359_5 and MCTG268

## Unassembled Samples
* pb_359_2:
 * Regarding the shortest contig - the coverage dip could appear exaggerated solely due to the
short size of the contig.
 * Double-check longest-contig peak, but otherwise accept assembly for the time being.
* pb_359_3:
 * Regarding the shortest contig - as above, coverage difference may appear exaggerated on
accoung of short contig size.
 * Dip in longest contig coverage may be due to a long, unresolved repeat region; check this,
but otherwise accept for the time being.
* pb_359_6:
 * Coverage across all contigs is relatively consistent; accept for the time being.
* pb_359_8:
 * HGAP (after trim) - 5,824,585 - one contig
  * Falcon - 5,855,311 - two contigs BUT more reads used.

Assemblies to move forward with:

| Sample   | Assembly to now use | Reservations                         |
|----------|---------------------|--------------------------------------|
| pb_359_2 | Falcon 7k (?)       | Peak in contig 1, trough in contig 3 |
| pb_359_3 | Falcon 17.1k        | Troughs in contigs 1 and 3           |
| pb_359_6 | Falcon 10.6k        | # of contigs, bubble in string graph |
| pb_359_8 | Falcon 17k          | ?                                    |

Sample 8 must be redone, as all others used the correct file for the 'test runs'
* For PhyloPhlAn, the file `pb_359_8_2.faa` was renamed to `pb_359_8.faa` to simplify the output

## pb_359_8
* Phylogenetic tree completed; viewing in Figtree
 * Position still similar to previously; close to Arenibacter algicola and A. sp. C-21
* Pathway Tools compilation ongoing

## Metaxa2
Can be used to extract 16S rRNA sequences

* pb_359_2 - compare to Roseovarius sp. TM1035 (or R. mucosus)
 * Metaxa also agrees with Roseovarius classification
 * Downloading all Roseovarius and Roseobacter sequences from SILVA
 * Appears to match exactly to TM1035, but the TM1035 reference is longer; reverse the Blast
and check whether the full-length TM1035 sequence appears in pb_359_2

* pb_359_3 - compare to Loktanella vestfoldensis (or sp. S4079, CCS2, 1ANDIMAR09, 5RATIMAR09)
 * Metaxa also agrees with Loktanella classification
 * Downloading all Loktanella sequences from SILVA
 * Best matches are to 'Loktanella; uncultured bacterium', but these are still not perfect matches
  * 2 mismatches; by comparison, L. vestfoldensis differs by 3 bp

* pb_359_4 - compare to Sphingorhabdus sp. M41 (or Sphingopyxis baekryugensis)
 * Note: Metaxa classifies the sequence as Sphingopyxis, not Sphingorhabdus...
* pb_359_5 - compare to Marinobacter sp. MCTG268 and M. salarius (or M. algicola)
 * Metaxa also agrees with Mariobacter classification
* pb_359_6 - compare to Sulfitobacter pseudonitzschiae and sp. 20_GPM-1509m
 * Note:  Metaxa finds TWO 16S sequences, both agreeing with the Sulfitobacter classification
* pb_359_7 - compare to Mameliella alba, Ruegeria sp. PBVC088, and various Antarctobacter
 * Note: Metaxa can only classify it down to the family Rhodobacteraceae; no genus classification
 * Antarctobacter sequences do exist within Metaxa2; could this belong to a new genus??
* pb_359_8 - compare to Arenibacter sp. C-21 and A. algicola (or A. latericius and A. certesii)
 * Metaxa also agrees with Arenibacter classification




## To do
* Mapping Illumina data back to PacBio assemblies for confirmation?
* Are the two Sulfitobacter 16S sequences identical?
* Use SILVA to get related sequences and then compare them to those extracted with Metaxa2
 * Check which genus/genera are closest to pb_359_X
 * Download sequences from SILVA, then use these as a blastn database against which to blast our
sequence.

# 15 November 2016

## Metaxa2
Continuing to download and compare sequences from SILVA using Metaxa2:
* pb_359_4:
 * Downloading all Sphingorhabdus and Sphingopyxis sequences from SILVA
 * Best matches to Sphingorhabdus flavimaris and Sphingopyxis sp. ZS1-22
  * 2 mismatches to both of the above; both differences seem to be at the same residue in each species

* pb_359_5:
 * Downloading all Marinobacter sequences from SILVA
 * Appears to match exactly to 'Marinobacter; uncultured bacterium', 'bacterium ROC5-1', Marinobacter
sp. R-28770 and Marinobacter sp. R-28768, but the reference sequences are longer; reverse the Blast
and check whether the full-length reference sequences appear in pb_359_5
 * Three matches to MCTG268 - 2 mismatches in one, and 6 mismatches + 2 gaps in the other two

* pb_359_6:
 * Downloading all Sulfitobacter, Oceanibulbus and Roseobacter sequences from SILVA
 * Both pb_359_6 sequences appear to match exactly to Sulfitobacter sp. DFL-23 and Sulfitobacter sp. DG885,
although none of the sequences match for the full length; reverse the Blast and check whether the full-length
reference sequences appear in pb_359_6

* pb_359_7:
 * Downloading all Mameliella, Ruegeria and Antarctobacter sequences from SILVA
 * Appears to match exactly to Antarctobacter sp. 667-12, although the sequence doesn't match the full length;
reverse the Blast and check whether the full-length reference sequence appears in pb_359_7

* pb_359_8:
 * Downloading all Arenibacter, Sediminicola and Cellulophaga sequences from SILVA
 * Best matches to two Arenibacter algicola sequences
  * Single mismatch, at the same residue in both cases

## Mauve
* pb_359_5 vs MCTG268
 * A majority of the sequences appear to be syntenic; however, there are a couple of areas which appear to be
large inversions...
 * Based on the similarity between 16S sequences and the high degree of synteny, it seems likely that these two
may belong to the same species...



## Possible next step
As found in Alvar's thesis - use Mauve to align our genomes to a reference obtaining good Blast hits, to assess
whether our genome can be considered complete, or if there are obvious exclusions.

* Re-check KAAS?

* Look for full-length 16S sequences on GenBank/SILVA
* 16S tree between closely-related species
* MrBayes

* Rerun sample 7 through Pathway Tools

# 16 November 2016

## 16S search
Very few full/complete 16S sequences for the species of interest...
Within complete genome sequences there exist regions labelled as rRNA; at the top of the GenBank files, there
is a list of how many 'complete' or 'partial' 16S sequences exist in the assembly... Label as 'from X', but
otherwise accept as complete.

* Samples retrieved for pb_359_2
* Samples retrieved for pb_359_3
* Samples retrieved for pb_359_4
 * Are Sphingorhabdus and Sphingopyxis the same...?
* Sample retrieval for pb_359_5 is ongoing...

# 17 November 2016

## 16S Search
Continuing with yesterday's search for full 16S sequences to compare with pb_359_X

* Samples retrieved for pb_359_5
* Samples retrieved for pb_359_6
* Samples retrieved for pb_359_7
 * No complete Antarctobacter 16S sequences found...
* Sample retrieval for pb_359_8 is ongoing...

Tip - when searching among scaffolds/contigs of whole genome shotgun sequences, search 'tRNA-Ile' as well;
there is usually such a sequence adjacent to the 16S sequence (investigate).

# 18 November 2016

## 16S Search
* Samples retrieved for pb_359_8

## PhyloPhlAn
* Run 16S sequences together
* 16S samples from the same species have been concatenated together into a single fasta; may
need to separate out by strain, or separate out individual sequences again.
 * Running pb_359_2 as an initial test
 * PhyloPhlAn accepts amino acid sequences, not nucleotide sequences; cannot use 16S sequences...

## ClustalW
Run through the 16S sequences with ClustalW and see which align most closely to pb_359_X
* http://www.genome.jp/tools-bin/clustalw

* pb_359_2
 * Closest match is to Roseovarius sp. TM1035, although the R. sp. TM1035 sequences are longer;
closest NAMED species is Roseovarius mucosus (2), whose sequence is even shorter than pb_359_2,
and three mismatches exist within the sequence.
 * Blast these sequences against pb_359_2 complete assembly.

* pb_359_3
 * Closest match is to one of the Loktanella vestfoldensis sequences (1), but three mismatches
still exist, and pb_359_3's sequence is shorter.
 * Blast the sequence against pb_359_3 complete assembly, along with the other L. vestfoldensis
sequences.

* pb_359_4
 * Closest match is to Sphingorhabdus sp. M41 (1 & 2), but six mismatches still exist, and
pb_359_4's sequence is shorter.
 * Blast the sequence against pb_359_4 complete assembly.

* pb_359_5
 * Closest match is to Marinobacter sp. MCTG268 (2), but three mismatches still exist, and
pb_359_5's sequence is shorter.
 * Blast the sequence against pb_359_5 complete assembly.

* pb_359_6
 * Closest match is to Sulfitobacter pseudonitzschiae, but with similarity to S. guttiformis;
pb_359_6 sequences are shorter than all of these.
 * Blast the sequences against pb_359_6 complete assembly.

* pb_359_7
 * Closest matches are to Sagittula stellata and to Rhodobacteraceae bacterium PD-2, but neither
of these are particularly close
 * Need to find complete Antarctobacter sequences...

* pb_359_8
 * Closest matches are to Sediminicola sp. YIK13 (1) and Cellulophaga lytica, not to Arenibacter!
 * The two are more closely related to each other than to pb_359_8...

## 16S things to do

* pb_359_2
 * Using pb_359_2 as the database, use the following queries:
  * Roseovarius sp. TM1035
  * Roseovarius mucosus

* pb_359_3
 * Using pb_359_3 as the database, use the following queries:
  * Loktanella vestfoldensis
  * Loktanella sp. S4029
  * Loktanella sp. 1ANDIMAR09
  * Loktanella sp. 5RATIMAR09
  * Roseobacter sp. CCS2

* pb_359_4
 * Using pb_359_4 as the database, use the following queries:
  * Sphingorhabdus sp. M41
  * Sphingopyxis baekryungensis
  * Any other available Sphingorhabdus sequences

* pb_359_5
 * Using pb_359_5 as the database, use the following queries:
  * Marinobacter salarius
  * Marinobacter sp. MCTG268

* pb_359_6
 * Using pb_359_6 as the database, use the following queries:
  * Sulfitobacter pseudonitzschiae
  * Sulfitobacter sp. 20_GPM_1509m
  * Sulfitobacter guttiformis

* pb_359_7
 * Using pb_359_7 as the database, use the following queries:
  * Mameliella alba
  * Ruegeria sp. PBVC088
  * Sagittula stellata
  * Rhodobacteraceae bacterium PD-2
  * Any available Antarctobacter sequences

* pb_359_8
 * Using pb_359_8 as the database, use the following queries:
  * Arenibacter algicola
  * Arenibacter sp. C-21
  * Sediminicola sp. YIK13
  * Cellulophaga lytica
  * Any other available Arenibacter sequences

Set up query using concatenation of all SILVA and NCBI hits, then search for '100%', ensuring
that the length of the query is equal (more or less) to the length of the hit itself

* Copy Sample_X_Comparison.fasta and [Genus]_16S.fasta into 02_blast/pb_359_X/16S_Reverse
* Use tr to replace white spaces in the SILVA sequences with underscores
* Remove pb_359_X from the NCBI results
* Append SILVA/NCBI onto the ends of FASTA headers as appropriate
* Concatenate the two files into one and delete the old files
* Run blast and search for 100% results


* 100% and 99% hits:
 * pb_359_2

| ID (SILVA)                   | Sample                                | Score (Match/Query length) |
|------------------------------|---------------------------------------|----------------------------|
| ABCL01000006.163548.164995   | Roseovarius_sp._TM1035                | 1448/1448                  |
| AJ294351.1.1370              | Roseovarius_mucosus                   | 1370/1370                  |
| ABCL01000005.367769.369216   | Roseovarius_sp._TM1035                | 1448/1448                  |
| HM538455.1.1322              | Roseovarius_sp._CR-CO6                | 1322/1322                  |
| -                            | Roseovarius_sp._TM1035_1              | 1472/1472                  |
| -                            | Roseovarius_sp._TM1035_2              | 1472/1472                  |
| -                            | Roseovarius_sp._TM1035_3              | 1472/1472                  |
| ABCL01000012.1.1910          | Roseovarius_sp._TM1035                | 1906/1910                  |
| KF733617.1.1460              | uncultured_Rhodobacteraceae_bacterium | 1454/1460                  |
| LADY01000051.4345.5818       | Roseovarius_sp._BRH_c41               | 1458/1474 (2 gaps)         |
| -                            | Roseovarius_sp._217                   | 1457/1474 (2 gaps)         |
| -                            | Roseovarius_sp._MCTG156_2b_2          | 1456/1474 (2 gaps)         |
| -                            | Roseovarius_sp._MCTG156_2b_1          | 1456/1474 (2 gaps)         |
| KJ814050.1.1429              | uncultured_bacterium                  | 1422/1425                  |
| KC442852.1.1462              | uncultured_bacterium                  | 1446/1462 (3 gaps)         |
| FJ516848.1.1431              | uncultured_Rhodobacteraceae_bacterium | 1423/1431                  |
| HM591393.1.1430              | uncultured_bacterium                  | 1420/1427 (1 gap)          |
| AAMV01000002.66945.68394     | Roseovarius_sp._217                   | 1433/1450 (2 gaps)         |
| JQLS01000008.4005738.4007187 | Roseovarius_sp._MCTG156(2b)           | 1432/1450 (2 gaps)         |
| JQLS01000008.2958404.2959853 | Roseovarius_sp._MCTG156(2b)           | 1432/1450 (2 gaps)         |
| AB159203.1.1410              | iodide-oxidizing_bacterium_RB-2A      | 1402/1406                  |
| GU437447.1.1445              | uncultured_bacterium                  | 1417/1432 (3 gaps)         |
...
(See 02_blast/pb_359_2/16S_Full/Sample_2_Best_Results.md for the full list)

 * pb_359_3
Check results

 * pb_359_4
Check results

 *pb_359_5-8
Run Blasts

# 21 November 2016

sed 's/\(^>.*\)/\1_SILVA/' input_file > output_file
sed 's/\(^>.*\)/\1_NCBI/' input_file > output_file

(or use -i flag if you're SURE of the command...)

grep -A 4 ">" pb_359_2_16S_Reverse.BLASTn.txt | grep -B 4 -e"100%" | sed 's/Bacteria;Proteobacteria;Alphaproteobacteria;Rhodobacterales;Rhodobacteraceae;Roseovarius;//g' > test
grep -A 4 ">" pb_359_2_16S_Reverse.BLASTn.txt | grep -B 4 -e"99%" | sed 's/Bacteria;Proteobacteria;Alphaproteobacteria;Rhodobacterales;Rhodobacteraceae;Roseovarius;//g' >> test

## 16S

After extracting the results, the following named species appear to be the most closely-related to our samples,
having 16S similarity of 99% or 100%:

* pb_359_2
 * Roseovarius mucosus
  * Strain DSM 17069
* pb_359_3
 * Loktanella vestfoldensis
  * Strain DSM 16212
  * Strain SKA53
* pb_359_4
 * Sphingorhabdus flavimaris - no genome sequence on NCBI or JGI
  * Previously known as Sphingopyxis flavimaris
 * Agrobacterium luteum - no genome sequence on NCBI or JGI
* pb_359_5
 * Marinobacter algicola
  * Strain DG893
 * Marinobacter salarius
 * Marinobacter koreensis - no genome sequence on NCBI or JGI
* pb_359_6
 * Sulfitobacter pseudonitzschiae
 * Sulfitobacter guttiformis
 * Sulfitobacter donghicola
* pb_359_7
 * Antarctobacter heliothermus - no genome sequence on NCBI
  * Found at http://genome.jgi.doe.gov/AnthelDSM11445_FD/AnthelDSM11445_FD.download.html
* pb_359_8
 * Arenibacter algicola
 * Flexithrix dorotheae
 * Arenibacter palladensis - no genome seqence on NCBI
  * Found at http://genome.jgi.doe.gov/ArepalAR_2009_79_FD/ArepalAR_2009_79_FD.download.html
  * Comparing to MAR_2009_79, rather than DSM 17539, as the quality is higher (improved draft cf. minimal draft)
 * Arenibacter troitsensis - no genome seqence on NCBI
  * Found at http://genome.jgi.doe.gov/AretroDSM19835_FD/AretroDSM19835_FD.download.html
 * Arenibacter echinorum - no genome seqence on NCBI
  * Found at http://genome.jgi.doe.gov/AreechDSM23522_FD/AreechDSM23522_FD.download.html

Obtain sequences for these samples and run them through Mauve
* Select pb_359_X first, then the other sample.
* (pb_359_5 vs MCTG268 was accidentally deleted; this has been rerun)
 * (New screenshot is required, however...)

Finish making READMEs in pb_359_8

Sync up git repos

# 22 November 2016

Repository is '7 GB too big'? Must compress files to reduce this...
* As no HGAP assemblies were used as final assemblies, will tar and zip all HGAP results
* Deleted the huge subread files (can be redownloaded from SMRT Portal)
* Despite these deletion, the error remains unchanged; may need to use the `git filter-branch`
command...
* Using the `du -sh */`, can pinpoint which folders are using the most space
* Removed most Canu files except for the .sge and any trimmed assemblies
* The repository itself is now fine; the `.git` folder is now the issue
 * Attempting `git gc --aggressive --prune` to see if the size of /git/pack/object can be reduced

* git reflog expire --expire=now --all && git gc --prune=now --aggressive

## Mauve
VERY close match between pb_359_5 and Marinobacter algicola DG893

## Note of the final assemblies used:

| Sample   | Assembler + SRL |
|----------|-----------------|
| pb_359_2 | Falcon 7k       |
| pb_359_3 | Falcon 17.1k    |
| pb_359_4 | Canu            |
| pb_359_5 | Canu            |
| pb_359_6 | Falcon 10.6k    |
| pb_359_7 | Canu            |
| pb_359_8 | Falcon 17k      |


## Important

By aligning related 16S sequences from GenBank, can identify the conserved beginning and end
sequences for the 16S sequence; this can then be extracted and saved into a separate fasta.  
**This is a priority**


## Mauve
Start from reorder 12 on S. pseudon vs _6

# 23 November 2016

## GitLab
A second Git repository - **Skeletonema_marinoi_microbiome_project_copy** - has now been
created; this should retain no memory of the now-deleted huge files from earlier.  
Plan of action:
* Add branch `mats` from original repository to this one
* Delete original repository
* Rename new repository to that of the original
* Sync files up, and be careful about what is committed and pushed

## 16S extraction

Full 16S sequences must be extracted from each sample:
* Check matches in Blast results, cut ~100bp up- and downsteam of the longst matches, then
perform multiple sequence alignment (http://www.genome.jp/tools/clustalw/) and trim according
to closest matches

* pb_359_2 (2x identical sequences):
TTAGAAAGGAGGTGATCCAGCCGCAGGTTCCCCTACGGCTACCTTGTTACGACTTCACCCCAGTCGCTGAGCCTACCGTGGCCGGCTGCC
TCCTCTTGCGAGGTTAGCGCACCGTCGTCGGGTAGACCCAACTCCCATGGTGTGACGGGCGGTGTGTACAAGGCCCGGGAACGTATTCAC
CGCGTCATGCTGTTACGCGATTACTAGCGATTCCGACTTCATGGGGTCGAGTTGCAGACCCCAATCCGAACTGAGATGGCTTTTTGGGAT
TAACCCATTGTCACCACCATTGTAGCACGTGTGTAGCCCAACCCGTAAGGGCCATGAGGACTTGACGTCATCCACACCTTCCTCCCGCTT
ATCACGGGCAGTTTCCATAGAGTGCCCAGCTTAACCTGCTGGCAACTAGGGATGTGGGTTGCGCTCGTTGCCGGACTTAACCGAACATCT
CACGACACGAGCTGACGACAGCCATGCAGCACCTGTGTGATATCCAGCCGAACTGACGAAACCATCTCTGGTAACTACGATATCCATGTC
AAGGGTTGGTAAGGTTCTGCGCGTTGCTTCGAATTAAACCACATGCTCCACCGCTTGTGCGGGCCCCCGTCAATTCCTTTGAGTTTTAAT
CTTGCGACCGTACTCCCCAGGCGGAATGCTTAATCCGTTAGGTGTGTCACCGACAAGCATGCTTGCCGACGACTGGCATTCATCGTTTAC
GGTGTGGACTACCAGGGTATCTAATCCTGTTTGCTCCCCACACTTTCGCACCTCAGCGTCAGTATCGAGCCAGTGAGCCGCCTTCGCCAC
TGGTGTTCCTCCGAATATCTACGAATTTCACCTCTACACTCGGAATTCCACTCACCTCTCTCGAACTCTAGACTGGGAGTTTTGGAGGCC
GTTCCAGGGTTGAGCCCTGGGATTTCACCCCCAACTTTCCAATCCGCCTACGTGCGCTTTACGCCCAGTAATTCCGAACAACGCTAACCC
CCTCCGTATTACCGCGGCTGCTGGCACGGAGTTAGCCGGGGTTTCTTTACCAGATACTGTCATTATCATCTCTGGCGAAAGAGCTTTACG
ACCCTAAGGCCTTCGTCACTCACGCGGCATGGCTAGATCAGGCTTGCGCCCATTGTCTAAGATTCCCCACTGCTGCCTCCCGTAGGAGTC
TGGGCCGTGTCTCAGTCCCAGTGTGGCTGATCATCCTCTAAAACCAGCTATGGATCGTAGGCTTGGTAGGCCATTACCCCACCAACTACC
TAATCCAACGCGGGCCGATCCTCCTCCGATAAATCTTTCCCCCAAAGGGCGTATGCGGTATTACTCACCGTTTCCAGTGGCTATCCCGCA
GAAGAGGGTACGTTCCCACGCGTTACTCACCCGTCCGCCGCTAACCCGAAGGTTCGCTCGACTTGCATGTGTTAGGCCTGCCGCCAGCGT
TCGTTCTGAGCCAGGATCAAACTCTCAAGTTG

* pb_359_3 (2x identical sequences): (bracketed bases - unsure whether to include)
TTAGAAAGGAGGTGATCCAGCCGCAGGTTCCCCTACGGCTACCTTGTTACGACTTCACCCCAGTCGCTGAGCTCACCGTGGTCCGCTGCC
CCCATTGCTGGTTGGCGCACGGCCTTCGGGTAAACCCAACTCCCATGGTGTGACGGGCGGTGTGTACAAGGCCCGGGAACGTATTCACCG
CGTCATGCTGTTACGCGATTACTAGCGATTCCGACTTCATGGGGTCGAGTTGCAGACCCCAATCCGAACTGAGACATCTTTTGGAGATTA
ACCCATTGTAGATGCCATTGTAGCACGTGTGTAGCCCAACCCGTAAGGGCCATGAGGACTTGACGTCATCCACACCTTCCTCCCGCTTAT
CACGGGCAGTTTCTCTAGAGTGCCCAACTAAATGATGGCAACTAAAGATGTGGGTTGCGCTCGTTGCCGGACTTAACCGAACATCTCACG
ACACGAGCTGACGACAGCCATGCAGCACCTGTCACTCTGTCTCTTACGAGAAAACCTGGTCTCCCAGGCGGTCAGAGGATGTCAAGGGTT
GGTAAGGTTCTGCGCGTTGCTTCGAATTAAACCACATGCTCCACCGCTTGTGCGGGCCCCCGTCAATTCCTTTGAGTTTTAATCTTGCGA
CCGTACTCCCCAGGCGGAATGCTTAATCCGTTAGGTGTGACACCGAAGGGCAAGCCCCCCGACGTCTGGCATTCATCGTTTACGGTGTGG
ACTACCAGGGTATCTAATCCTGTTTGCTCCCCACACTTTCGCACCTCAGCGTCAGTATCGAGCCAGTGAGCCGCCTTCGCCACTGGTGTT
CCTCCAAATATCTACGAATTTCACCTCTACACTTGGAATTCCACTCACCTCTCTCGAACTCTAGACTGGGAGTTTACAAGGCAGTTCCAG
GGTTGAGCCCTGGGATTTCACCCCATACTTTCCAATCCGCCTACGTGCGCTTTACGCCCAGTAATTCCGAACAACGCTAACCCCCTCCGT
ATTACCGCGGCTGCTGGCACGGAGTTAGCCGGGGTTTCTTTACCAGATACTGTCATTATCATCTCTGGCGAAAGAGCTTTACGACCCTAA
GGCCTTCGTCACTCACGCGGCATGGCTAGATCAGGCTTGCGCCCATTGTCTAAGATTCCCCACTGCTGCCTCCCGTAGGAGTCTGGGCCG
TGTCTCAGTCCCAGTGTTGCTGATCATCCTCTCAAACCAGCTACTGATCGTAGACTTGGTAGGCCATTACCCCACCAACTATCTAATCAG
ACGCGGGCTAATCCTTCACCGATAAATCTTTCCCCAAAAGGGCGTATACGGTATTACTCCCAGTTTCCCGAGGCTATTCCGTAGTGAAGG
GTATATTCCCACGCGTTACTAACCCGTCCGCCGCTAGACCCGAAGGTCTCGCTCGACTTGCATGTGTTAGGCCTGCCGCCAGCGTTCGTT
CTGAGCCAGGATCAAACTCTCAAGTTGA(AA)

* pb_359_4 (2x near-identical sequences):
CCTTAGAAAGGAGGTGATCCAGCCGCAGGTTCCCCTACGGCTACCTTGTTACGACTTCACCCCAGTCGCTGAACCCACCGTGGTTGGCTG
CCTCTCTTGCGAGTTAGCGCACCAGCTTCGGGTTGATCCAACTCCCATGGTGTGACGGGCGGTGTGTACAAGGCCTGGGAACGTATTCAC
CGCGGCATGCTGATCCGCGATTACTAGCGATTCCGCCTTCATGCTCTCGAGTTGCAGAGAACAATCCGAACTGAGACGGTTTTTAGAGAT
TAGCATCTTCTCGCGAAGTAGCTGCCCACTGTCACCGCCATTGTAGCACGTGTGTAGCCCAGCGTGTAAGGGCCATGAGGACTTGACGTC
ATCCCCACCTTCCTCCGGCTTATCACCGGCGGTCTCTTTAGAGTGCCCAACCAAATGGTAGCAACTAAAGATAGGGGTTGCGCTCGTTGC
GGGACTTAACCCAACATCTCACGACACGAGCTGACGACAGCCATGCAGCACCTGTCACTGATCCAGCCGAGCTGAAGGAAACCATCTCTG
GTATCCGCGATCAGGATGTCAAACGCTGGTAAGGTTCTGCGCGTTGCGTCGAATTAAACCACATGCTCCACCGCTTGTGCAGGCCCCCGT
CAATTCCTTTGAGTTTTAATCTTGCGACCGTACTCCCCAGGCGGATAACTTAATGCGTTAGCTGCGCCACCAAAGCCCTGTGGGCCCTAG
CAGCTAGTTATCATCGTTTACGGCGTGGACTACCAGGGTATCTAATCCTGTTTGCTCCCCACGCTTTCGCACCTCAGCGTCAATACTTGT
CCAGCGAGTCGCCTTCGCCACTGGTGTTCTTCCGAATATCTACGAATTTCACCTCTACACTCGGAATTCCACTCGCCTCTCCAAGATTCT
AGTCACCTAGTTTCAAAGGCAGTTCCGGAGTTGAGCTCCGGGCTTTCACCTCTGACTTGAGTAACCGCCTACGCGCGCTTTACGCCCAGT
AATTCCGAACAACGCTAGCTCCCTCCGTATTACCGCGGCTGCTGGCACGGAGTTAGCCGGAGCTTATTCTCCAGGTACTGTCATTATCAT
CCCTGGTAAAAGAGCTTTACAACCCTAAGGCCTTCATCACTCACGCGGCATTGCTGGATCAGGCTTTCGCCCATTGTCCAATATTCCCCA
CTGCTGCCTCCCGTAGGAGTCTGGGCCGTGTCTCAGTCCCAGTGTGGCTGATCATCCTCTCAGACCAGCTAAAGATCGTCGCCTTGGTGA
GCCTTTACCTCACCAACAAGCTAATCTTACGCGGGTTCATCAAAGGGCGATAAATCTTTGGTCCGAAGACATTATGCGGTATTAGCTCAA
ATTTCTCTGAGTTATTCCGCACCCTATGGTAGATCCCCACGCGTTACGCACCCGTGCGCCACTAGATCCGAAGATCTCGTTCGACTTGCA
TGTGTTAAGCATGCCGCCAGCGTTCGTTCTGAGCCAGGATCAAACTCTCAAGTTTGATGTCCTGTAATGGTGGCACAA**G**CCGAAGCTTGC
AATCCACCGAAACAGCTTCATTTCAAGG

CCTTAGAAAGGAGGTGATCCAGCCGCAGGTTCCCCTACGGCTACCTTGTTACGACTTCACCCCAGTCGCTGAACCCACCGTGGTTGGCTG
CCTCTCTTGCGAGTTAGCGCACCAGCTTCGGGTTGATCCAACTCCCATGGTGTGACGGGCGGTGTGTACAAGGCCTGGGAACGTATTCAC
CGCGGCATGCTGATCCGCGATTACTAGCGATTCCGCCTTCATGCTCTCGAGTTGCAGAGAACAATCCGAACTGAGACGGTTTTTAGAGAT
TAGCATCTTCTCGCGAAGTAGCTGCCCACTGTCACCGCCATTGTAGCACGTGTGTAGCCCAGCGTGTAAGGGCCATGAGGACTTGACGTC
ATCCCCACCTTCCTCCGGCTTATCACCGGCGGTCTCTTTAGAGTGCCCAACCAAATGGTAGCAACTAAAGATAGGGGTTGCGCTCGTTGC
GGGACTTAACCCAACATCTCACGACACGAGCTGACGACAGCCATGCAGCACCTGTCACTGATCCAGCCGAGCTGAAGGAAACCATCTCTG
GTATCCGCGATCAGGATGTCAAACGCTGGTAAGGTTCTGCGCGTTGCGTCGAATTAAACCACATGCTCCACCGCTTGTGCAGGCCCCCGT
CAATTCCTTTGAGTTTTAATCTTGCGACCGTACTCCCCAGGCGGATAACTTAATGCGTTAGCTGCGCCACCAAAGCCCTGTGGGCCCTAG
CAGCTAGTTATCATCGTTTACGGCGTGGACTACCAGGGTATCTAATCCTGTTTGCTCCCCACGCTTTCGCACCTCAGCGTCAATACTTGT
CCAGCGAGTCGCCTTCGCCACTGGTGTTCTTCCGAATATCTACGAATTTCACCTCTACACTCGGAATTCCACTCGCCTCTCCAAGATTCT
AGTCACCTAGTTTCAAAGGCAGTTCCGGAGTTGAGCTCCGGGCTTTCACCTCTGACTTGAGTAACCGCCTACGCGCGCTTTACGCCCAGT
AATTCCGAACAACGCTAGCTCCCTCCGTATTACCGCGGCTGCTGGCACGGAGTTAGCCGGAGCTTATTCTCCAGGTACTGTCATTATCAT
CCCTGGTAAAAGAGCTTTACAACCCTAAGGCCTTCATCACTCACGCGGCATTGCTGGATCAGGCTTTCGCCCATTGTCCAATATTCCCCA
CTGCTGCCTCCCGTAGGAGTCTGGGCCGTGTCTCAGTCCCAGTGTGGCTGATCATCCTCTCAGACCAGCTAAAGATCGTCGCCTTGGTGA
GCCTTTACCTCACCAACAAGCTAATCTTACGCGGGTTCATCAAAGGGCGATAAATCTTTGGTCCGAAGACATTATGCGGTATTAGCTCAA
ATTTCTCTGAGTTATTCCGCACCCTATGGTAGATCCCCACGCGTTACGCACCCGTGCGCCACTAGATCCGAAGATCTCGTTCGACTTGCA
TGTGTTAAGCATGCCGCCAGCGTTCGTTCTGAGCCAGGATCAAACTCTCAAGTTTGATGTCCTGTAATGGTGGCACAA**A**CCGAAGCTTGC
AATCCACCGAAACAGCTTCATTTCAAGG

* pb_359_5 (2x identical sequences + 1x near-identical): (bracketed bases - unsure whether to include)
 * 2x:
CTTCGTTTAAGGAGGTGATCCAGCCGCAGGTTCCCCTACGGCTACCTTGTTACGACTTCACCCCAGTCATGAACCACACCGTGGTGATCG
TCCTCCCGAAGGTTAGACTAACCACTTCTGGTGCAATCCACTCCCATGGTGTGACGGGCGGTGTGTACAAGGCCCGGGAACGTATTCACC
GCGACATTCTGATTCGCGATTACTAGCGATTCCGACTTCACGGAGTCGAGTTGCAGACTCCGATCCGGACTACGATGCGTTTTGTGAGAT
TAGCTCCCCCTCGCGGGTTTGCAGCCCTCTGTACGCACCATTGTAGCACGTGTGTAGCCCTGGCCGTAAGGGCCATGATGACCTGACGTC
ATCCCCACCTTCCTCCGGTTTGTCACCGGCAGTCTCCCTAGAGTTCTCAGCCGAACTGCTAGCAACTAGGGATAGGGGTTGCGCTCGTTA
CGGGACTTAACCCAACATCTCACGACACGAGCTGACGACGGCCATGCAGCACCTGTGTCAGAGTTCCCGAAGGCACCAATCCATCTCTGG
AAAGTTCTCTGCATGTCAAGGCCAGGTAAGGTTCTTCGCGTTGCGTCGAATTAAACCACATGCTCCACCGCTTGTGCGGGCCCCCGTCAA
TTCATTTGAGTTTTAACCTTGCGGCCGTACTCCCCAGGCGGTCAACTTAGTGCGTTAGCTGCGCCACTAAGACTTCAAGAGTCCCAACGG
CTAGTTGACATCGTTTACAGCGTGGACTACCAGGGTATCTAATCCTGTTTGCTCCCCACGCTTTCGCACCTCAGTGTCAGTATTGGTCCA
GAGTGCCGCCTTCGCCACTGGTGTTCCTTCCTATATCTACGCATTTCACCGCTACACAGGAAATTCCACACTCCTCTACCATACTCTAGC
CTGACAGTTCGAAATGCCGTTCCCAGGTTGAGCCCGGGGCTTTCACATCTCGCTTATCAAACCACCTACGCGCGCTTTACGCCCAGTAAT
TCCGATTAACGCTTGCACCCTCCGTATTACCGCGGCTGCTGGCACGGAGTTAGCCGGTGCTTCTTCTGTGAGTAACGTCAAGCCTCACGA
GTATTAGTCGT**C**AGGTTTTCCTCCTCACTGAAAGTGCTTTACAACCCGAAAGCCTTCTTCACACACGCGGCATGGCTGGATCAGGGTTGC
CCCCATTGTCCAATATTCCCCACTGCTGCCTCCCGTAGGAGTTCGGGCCGTGTCTCAGTCCCGATGTGGCTGATCATCCTCTCAGACCAG
CTACGGATCGTCGCCTTGGTAGGCTCTTACCCCACCAACTAGCTAATCCGACATAGGCACATCCAATAGCGCAAGGTCCGAAGATCCCCT
GCTTTCCCCCAAAGGGCGTATGCGGTATTAATCCGGGTTTCCCCGGGCTATCCCCCACTACTGGGCAGTTTCCTATGCATTACTCACCCG
TCCGCCGCTCGTCAGCGGGGAGCAAGCTCCCCCTGTTACCGCTCGACTTGCATGTGTTAAGCCTGCCGCCAGCGTTCAATCTGAGCCATG
ATCAAACTCTTCAGTTT(A)

 * 1x:
CTTCGTTTAAGGAGGTGATCCAGCCGCAGGTTCCCCTACGGCTACCTTGTTACGACTTCACCCCAGTCATGAACCACACCGTGGTGATCG
TCCTCCCGAAGGTTAGACTAACCACTTCTGGTGCAATCCACTCCCATGGTGTGACGGGCGGTGTGTACAAGGCCCGGGAACGTATTCACC
GCGACATTCTGATTCGCGATTACTAGCGATTCCGACTTCACGGAGTCGAGTTGCAGACTCCGATCCGGACTACGATGCGTTTTGTGAGAT
TAGCTCCCCCTCGCGGGTTTGCAGCCCTCTGTACGCACCATTGTAGCACGTGTGTAGCCCTGGCCGTAAGGGCCATGATGACCTGACGTC
ATCCCCACCTTCCTCCGGTTTGTCACCGGCAGTCTCCCTAGAGTTCTCAGCCGAACTGCTAGCAACTAGGGATAGGGGTTGCGCTCGTTA
CGGGACTTAACCCAACATCTCACGACACGAGCTGACGACGGCCATGCAGCACCTGTGTCAGAGTTCCCGAAGGCACCAATCCATCTCTGG
AAAGTTCTCTGCATGTCAAGGCCAGGTAAGGTTCTTCGCGTTGCGTCGAATTAAACCACATGCTCCACCGCTTGTGCGGGCCCCCGTCAA
TTCATTTGAGTTTTAACCTTGCGGCCGTACTCCCCAGGCGGTCAACTTAGTGCGTTAGCTGCGCCACTAAGACTTCAAGAGTCCCAACGG
CTAGTTGACATCGTTTACAGCGTGGACTACCAGGGTATCTAATCCTGTTTGCTCCCCACGCTTTCGCACCTCAGTGTCAGTATTGGTCCA
GAGTGCCGCCTTCGCCACTGGTGTTCCTTCCTATATCTACGCATTTCACCGCTACACAGGAAATTCCACACTCCTCTACCATACTCTAGC
CTGACAGTTCGAAATGCCGTTCCCAGGTTGAGCCCGGGGCTTTCACATCTCGCTTATCAAACCACCTACGCGCGCTTTACGCCCAGTAAT
TCCGATTAACGCTTGCACCCTCCGTATTACCGCGGCTGCTGGCACGGAGTTAGCCGGTGCTTCTTCTGTGAGTAACGTCAAGCCTCACGA
GTATTAGTCGT**A**AGGTTTTCCTCCTCACTGAAAGTGCTTTACAACCCGAAAGCCTTCTTCACACACGCGGCATGGCTGGATCAGGGTTGC
CCCCATTGTCCAATATTCCCCACTGCTGCCTCCCGTAGGAGTTCGGGCCGTGTCTCAGTCCCGATGTGGCTGATCATCCTCTCAGACCAG
CTACGGATCGTCGCCTTGGTAGGCTCTTACCCCACCAACTAGCTAATCCGACATAGGCACATCCAATAGCGCAAGGTCCGAAGATCCCCT
GCTTTCCCCCAAAGGGCGTATGCGGTATTAATCCGGGTTTCCCCGGGCTATCCCCCACTACTGGGCAGTTTCCTATGCATTACTCACCCG
TCCGCCGCTCGTCAGCGGGGAGCAAGCTCCCCCTGTTACCGCTCGACTTGCATGTGTTAAGCCTGCCGCCAGCGTTCAATCTGAGCCATG
ATCAAACTCTTCAGTTT(A)

* pb_359_6 (2x identical sequences (Longest Contig, and Third Contig)):
 * Metaxa2 found two sequences which differ wildly from the result found by Blast
 * The Blast result is the reverse complement of the Metaxa2 result

TTAGAAAGGAGGTGATCCAGCCGCAGGTTCCCCTACGGCTACCTTGTTACGACTTCACCCCAGTCGCTGATCCTACCGTGGTCCGCTGCC
TCCTCGAAAGGTTGGCGCACGGCCGTCGGGTAGAACCAACTCCCATGGTGTGACGGGCGGTGTGTACAAGGCCCGGGAACGTATTCACCG
CGTCATGCTGTTACGCGATTACTAGCGATTCCGACTTCATGGGGTCGAGTTGCAGACCCCAATCCGAACTGAGACATCTTTTGGGGATTA
ACCCACTGTAGATGCCATTGTAGCACGTGTGTAGCCCAACCCGTAAGGGCCATGAGGACTTGACGTCATCCACACCTTCCTCCCGCTTAT
CACGGGCAGTTTCTTTAGAGTGCCCAGCCGAACTGCTGGCAACTAAAGATGTGGGTTGCGCTCGTTGCCGGACTTAACCGAACATCTCAC
GACACGAGCTGACGACAGCCATGCAGCACCTGTGCACTGGTCCCGAAGGAAAGTCCCATCTCTGGGATTGTCCAGGCATGTCAAGGGTTG
GTAAGGTTCTGCGCGTTGCTTCGAATTAAACCACATGCTCCACCGCTTGTGCGGGCCCCCGTCAATTCCTTTGAGTTTTAATCTTGCGAC
CGTACTCCCCAGGCGGAATGCTTAATCCGTTAGGTGTGTCACCGAACAGTATACTGCCCGACGACTGGCATTCATCGTTTACGGTGTGGA
CTACCAGGGTATCTAATCCTGTTTGCTCCCCACACTTTCGCACCTCAGCGTCAGTATCGAGCCAGTGAGCCGCCTTCGCCACTGGTGTTC
CTCCGAATATCTACGAATTTCACCTCTACACTCGGAATTCCACTCACCTCTCTCGAACTCAAGACCAGGAGTTTTGGAGGCAGTTCCAGG
GTTGAGCCCTGGGATTTCACCCCCAACTTTCTGATCCGCCTACGTGCGCTTTACGCCCAGTAATTCCGAACAACGCTAACCCCCTCCGTA
TTACCGCGGCTGCTGGCACGGAGTTAGCCGGGGTTTCTTTACCAGGTACTGTCATTATCATCCCTGGCGAAAGTGCTTTACGACCCTAAG
GCCTTCATCACACACGCGGCATGGCTAGATCAGGCTTGCGCCCATTGTCTAAGATTCCCCACTGCTGCCTCCCGTAGGAGTCTGGGCCGT
GTCTCAGTCCCAGTGTTGCTGATCATCCTCTAAAACCAGCTAAAGATCGTAGACTTGGTAGGCCATTACCCCACCAACTATCTAATCTTA
CGCGGGCTGATCCTTCTCCGATAAATCTTTCCCCCGAAGGGCGTATATGGTATTACTCTCAGTTTCCCGAGGCTATTCCATAGAGAAGGG
TACATTCCCACGCGTTACTAACCCGTCCGCCGCTCGCCCCGAAGGGTGCGCTCGACTTGCATGTGTTAGGCCTGCCGCCAGCGTTCGTTC
TGAGCCAGGATCAAACTCTCAAGTTGA

* pb_359_7 (2x identical sequences):
TCAACTTGAGAGTTTGATCCTGGCTCAGAACGAACGCTGGCGGCAGGCCTAACACATGCAAGTCGTGCGCGCCCTTCGGGGTGAGCGGCG
GACGGGTGAGTAACGCGTGGGAATATGCCCTTCTGTTGAGGATAGCCCTGGGAAACTGGGAGTAATACTCGATACGCCCTACGGGGGAAG
GAAGGATTAGCCCGCGTTAGATTAGGTAGTTGGTGAGGTAATGGCTCACCAAGCCTACGATCTATAGCTGGTTTTAGAGGATGATCAGCC
ACACTGGGACTGAGACACGGCCCAGACTCCTACGGGAGGCAGCAGTGGGGAATCTTAGACAATGGGCGCAAGCCTGATCTAGCCATGCCG
CGTGAGTGATGAAGGCCTTAGGGTCGTAAAGCTCTTTCGCCAGGGATGATAATGACAGTACCTGGTAAAGAAACCCCGGCTAACTCCGTG
CCAGCAGCCGCGGTAATACGGAGGGGGTTAGCGTTGTTCGGAATTACTGGGCGTAAAGCGCGCGTAGGCGGACCAGAAAGTATGGGGTGA
AATCCCGGGGCTCAACCCCGGAACTGCCTCATAAACTCCTGGTCTTGAGTTCGAGAGAGGTGAGTGGAATTCCGAGTGTAGAGGTGAAAT
TCGTAGATATTCGGAGGAACACCAGTGGCGAAGGCGGCTCACTGGCTCGATACTGACGCTGAGGTGCGAAAGTGTGGGGAGCAAACAGGA
TTAGATACCCTGGTAGTCCACACCGTAAACGATGAATGCCAGTCGTCGGCAAGCATGCTTGTCGGTGACACACCTAACGGATTAAGCATT
CCGCCTGGGGAGTACGGTCGCAAGATTAAAACTCAAAGGAATTGACGGGGGCCCGCACAAGCGGTGGAGCATGTGGTTTAATTCGAAGCA
ACGCGCAGAACCTTACCAACCCTTGACATACTTGTCGTCGCTCCAGAGATGGAGCTTTCAGTTAGGCTGGACAAGATACAGGTGCTGCAT
GGCTGTCGTCAGCTCGTGTCGTGAGATGTTCGGTTAAGTCCGGCAACGAGCGCAACCCACATCTTCAGTTGCCAGCAGTTCGGCTGGGCA
CTCTGGAGAAACTGCCCGTGATAAGCGGGAGGAAGGTGTGGATGACGTCAAGTCCTCATGGCCCTTACGGGTTGGGCTACACACGTGCTA
CAATGGCATCTACAATGGGTTAATCCCCAAAAGATGTCTCAGTTCGGATTGGGGTCTGCAACTCGACCCCATGAAGTCGGAATCGCTAGT
AATCGCGTAACAGCATGACGCGGTGAATACGTTCCCGGGCCTTGTACACACCGCCCGTCACACCATGGGAGTTGGTTCTACCTGACGGCC
GTGCGCTAACCTTCGGGAGGCAGCGGACCACGGTAGGATCAGCGACTGGGGTGAAGTCGTAACAAGGTAGCCGTAGGGGAACCTGCGGCT
GGATCACCTCCTTTCTAA

* pb_359_8 (3x identical sequences):
TCTAGAAAGGAGGTGTTCCAGCCGCACCTTCCGGTACGGCTACCTTGTTACGACTTAGCCCTAGTTACCGATCTTGCCCTAGGCCGCTCC
TTGCGGTGACGGACTTCAGGCACTCCCGGCTTCCATGGCTTGACGGGCGGTGTGTACAAGGCCCGGGAACGTATTCACCGGATCATGGCT
GATATCCGATTACTAGCGATTCCAGCTTCACGGGGTCGAGTTGCAGACCCCGATCCGAACTGTGACCGGTTTTATAGATTCGCTCCTGGT
TGCCCAGTGGCTGCTCTCTGTACCGGCCATTGTAGCACGTGTGTGGCCCAGGACGTAAGGGCCGTGATGATTTGACGTCATCCCCACCTT
CCTCGCGGTTTGCACCGGCAGTCCCGTTAGAGTCCCCATCTTTACATGCTGGCAACTAACGGCAGGGGTTGCGCTCGTTATAGGACTTAA
CCTGACACCTCACGGCACGAGCTGACGACAACCATGCAGCACCTTGTGATCTGCCCGAAGGAGGCTCTATCTCTAAAGCTGTCAGACCAC
ATTTAAGCCCTGGTAAGGTTCCTCGCGTATCATCGAATTAAACCACATGCTCCACCGCTTGTGCGGGCCCCCGTCAATTCCTTTGAGTTT
CATCCTTGCGGACGTACTCCCCAGGTGGGATACTTATCACTTTCGCTTGGCCGCCCAGATTTGCATCCGGACAGCTAGTATCCATCGTTT
ACGGCGTGGACTACCAGGGTATCTAATCCTGTTCGCTCCCCACGCTTTCGTCCATCAGCGTCAGTATATGGTTAGTAACCTGCCTTCGCA
ATCGGTATTCTATGTAATATCTATGCATTTCACCGCTACACTACATATTCTAGTTACTTCACCATAACTCAAGACCACCAGTATCAAGGG
CAATTCTACGGTTGAGCCGCAGACTTTCACCCCTGACTTAATGGCCCGCCTACGGACCCTTTAAACCCAATGATTCCGGATAACGCTCGG
ATCCTCCGTATTACCGCGGCTGCTGGCACGGAGTTAGCCGATCCTTATTCTTACGGTACCGTCAGAGGGGCACACGTGCCCCTTGTTCTT
CCCGTACAAAAGCAGTTTACAATCCATAGGACCGTCTTCCTGCACGCGGCATGGCTGGATCAGGCTCCCGCCCATTGTCCAATATTCCTC
ACTGCTGCCTCCCGTAGGAGTCTGGTCCGTGTCTCAGTACCAGTGTGGGGGATCCCCCTCTCAGGGCCCCTACCCATCGCTGCCTTGGTA
AGCCGTTACCTTACCAACTAACTAATGGGACGCATAGTCATCCTGTACCGTAGCCTTTAATGTATAAGCGATGCCGCTAATACATACCAT
GGGGCATTAATCCAAATTTCTCTGGGCTATTCCCCAGTACAGGGCAGATTCTATACGCGTTGCGCACCCGTGCGCCGGTCGCCGGCGGAT
AAGCAAGCTTATCCCCGCTGCCCCTCGACTTGCATGTGTTAGGCCTGCCGCTAGCGTTCATCCTGAGCCAGGATCAAACTCTTCATCGTT
G

* Odd bases on 3 and 5...
 * Trim

* Finish the Arenibacter echinorum Mauve reordering, and continue with the last few from _8

* Blast 16Ss against NCBI, download full sequence, calculate similarity scores, find most
closely-related named species.
 * If no tool exists for determining similarity, make one

* Commit to git copy

# 24 November 2016

## 16S
Regarding the hanging bases on the 16S sequences, go with majority rule and trim them off

* pb_359_2:
 * Closest named species - Roseovarius mucosus strain DFL-24
  * Score: 2427 bits (1314)
  * Expect: 0.0
  * Identities: 1320/1323(99%)
  * Gaps: 0/1323(0%)
  * Strand: Plus/Minus
  * Query cover: 89% (1323bp vs 1472bp)

* pb_359_3:
 * Closest named species - Loktanella vestfoldensis strain R-9477 (based on partial sequence)
  * Score: 2634 bits (1426)
  * Expect: 0.0
  * Identities: 1435/1440 (99%)
  * Gaps: 0/1440 (0%)
  * Strand: Plus/Minus
  * Query cover: 98% (1449bp vs 1468bp)
  * Note: best full sequence is Leisingera methylohalidivorans, but almost 100 differing bases

* pb_359_4:
 * Closest named species - Sphingopyxis flavimaris strain R-36742 (based on partial sequence)
  * Score: 2651 bits (1435)
  * Expect: 0.0
  * Identities: 1439/1441 (99%)
  * Gaps: 0/1441 (0%)
  * Strand: Plus/Minus
  * Query cover: 92% (1441bp vs 1558bp)
  * Note: same stats against both variants of pb_359_4 16S - differs at same base?
  * Note: best full sequence is Novosphingobium pentaromativorans, but almost 80 differing bases

* pb_359_5:
 * Closest named species - Marinobacter salarius strain R9SW1 (based on complete genome and partial sequence)
  * Score: 2811 bits (1522) / 2784 bits (1507)
  * Expect: 0.0 / 0.0
  * Identities: 1539/1547 (99%) / 1524/1532 (99%)
  * Gaps: 1/1547 (0%) / 1/1532 (0%)
  * Strand: Plus/Plus / Plus/Minus
  * Query cover: 100% / 99% (4,616,532bp / 1531bp vs 1547bp)
  * Note: searching nr/nt database
 * Closest named species - Marinobacter algicola strain DG893 (based on partial sequence)
  * Score: 2731 bits (1479)
  * Expect: 0.0
  * Identities: 1483/1485 (99%)
  * Gaps: 0/1485
  * Strand: Plus/Minus
  * Query cover: 95% (1485bp vs 1547bp)
  * Note: searching 16S-specific database
  * Note: best full sequence is Marinobacter adhaerens, but 25 differing bases, inc. 4 gaps

* pb_359_6:
 * Closest named species - Sulfitobacter pseudonitzschiae strain H3
 * Score: 2573 bits (1393)
 * Expect: 0.0
 * Identities: 1417/1428 (99%)
 * Gaps: 4/1428 (0%)
 * Strand: Plus/Minus
 * Query cover: 97% (1426bp vs 1467bp)
 * Note: Identical results found in partial 16S of 'Staleya guttiformis' (deprecated term for
Sulfitobacter

* pb_359_7:
 * Closest named species - Antarctobacter heliothermus strain EL-219 (based on partial sequence)
  * Score: 2549 bits (1380)
  * Expect: 0.0
  * Identities: 1395/1402 (99%)
  * Gaps: 2/1402 (0%)
  * Strand: Plus/Plus
  * Query cover: 96% (1400bp vs 1458bp)
  * Note: best full sequence is Dinoroseobacter shibae, but ~100 differing bases inc. 19 gaps

* pb_359_8:
 * Closest named species - Flexibacter aggregans strain BSs20185 (based on partial sequence)
  * Score: 2732 bits (1479)
  * Expect: 0.0
  * Identities: 1482/1483 (99%)
  * Gaps: 1/1483 (0%)
  * Strand: Plus/Minus
  * Query cover: 96% (1486bp vs 1531bp)
 * Closest named species - Arenibacter palladensis strain LMG 21972 (based on complete sequence)
  * Score: 2682 bits (1452)
  * Expect 0.0
  * Identities: 1468/1476 (99%)
  * Gaps: 0/1476 (0%)
  * Strand: Plus/Minus
  * Query cover: 96% (1476bp vs 1531bp)

* Next step for 16S comparison: pairwise sequence alignment?

* Note: 99% may not be a high enough similarity score to account for all possible matches
 * https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2045242/
* Need to use local alignment, given the size difference between some of the sequences...

* Use E. coli 16S to determine start/stop?
* RNAmmer
 * RNAmmer prediction for pb_359_2 is 1456 (x2 sequences); 16 bases shorter, but gets
the same match stats as the longer prediction

* CCTCCT at 3' end? (binding to Shine-Delgarno sequence)
 * Problem - in the case of pb_359_2, at least, there is a CCTCCT and an AGGAGG sequence;
which is 'forward' and which is 'reverse'?

* When performing multiple sequence alignment, ENSURE ALL SEQUENCES ARE GOING IN THE SAME
DIRECTION! This has produced a much more convincing result!
 * pb_359_2 - Begins with CAACTTGAGAGT, ends with CCTCCTTTCTAA
  * Alternatively - begins with TTAGAAAGGAGG, ends with ACTCTCAAGTTG
  * The latter agrees with the results found in the genome
 * pb_359_3 - Begins with TCAACTTGAGAGT, ends with CCTCCTTTCTAA
  * Alternatively - begins with TTAGAAAGGAGG, ends with ACTCTCAAGTTGA
  * The latter agrees with the results found in the genome
 * pb_359_4 - Begins with TCAAACTTGAGAGT, ends with CCTCCTTTCTAAGG
  * Alternatively - begins with CCTTAGAAAGGAGG, ends with ACTCTCAAGTTTGA
  * After a little trimming of previous 16S guess, the latter agrees with the results found in
the genome
 * pb_359_5 - Begins with AAACTGAAGAGT, ends with CCTCCTTAAACGAAG
  * Alternatively, begins with CTTCGTTTAAGGAGG, ends with ACTCTTCAGTTT
  * The latter agrees with the results found in the genome
 * pb_359_6 - Begins with TCAACTTGAGAGT, ends with CCTCCTTTCTAA
  * Alternatively, begins with TTAGAAAGGAGG, ends with ACTCTCAAGTTGA
  * The latter agrees with the results found in the genome
 * pb_359_7 - Begins with TCAACTTGAGAGT, ends with CCTCCTTTCTAA
  * Alternatively, begins with TTAGAAAGGAGG, ends with ACTCTCAAGTTGA
  * The former agrees with the results found in the genome
 * pb_359_8 - Begins with TCTAGAAAGGAGG, ends with ACTCTTCATCGTTG
  * Alternatively, begins with CAACGATGAAGAGT, ends with CCTCCTTTCTAGA
  * The former agrees with the results found in the genome

## Presumed identities of the samples

| Sample   | Phylum         | Class               | Order            | Family            | Genus          | 16S 5'                | 16S 3'             |
|----------|----------------|---------------------|------------------|-------------------|----------------|-----------------------|--------------------|
| pb_359_2 | Proteobacteria | Alphaproteobacteria | Rhodobacterales  | Rhodobacteraceae  | Roseovarius    | --CAACTTGAGAGTTTGATCC | TCACCTCCTTTCTAA--- |
| pb_359_3 | Proteobacteria | Alphaproteobacteria | Rhodobacterales  | Rhodobacteraceae  | Loktanella     | -TCAACTTGAGAGTTTGATCC | TCACCTCCTTTCTAA--- |
| pb_359_4 | Proteobacteria | Alphaproteobacteria | Sphingomonadales | Sphingomonadaceae | Sphingorhabdus | TCAAACTTGAGAGTTTGATCC | TCACCTCCTTTCTAAGG- |
| pb_359_5 | Proteobacteria | Gammaproteobacteria | Alteromonadales  | Alteromonadaceae  | Marinobacter   | --AAACTGAAGAGTTTGATCA | TCACCTCCTTAAACGAAG |
| pb_359_6 | Proteobacteria | Alphaproteobacteria | Rhodobacterales  | Rhodobacteraceae  | Sulfitobacter  | -TCAACTTGAGAGTTTGATCC | TCACCTCCTTTCTAA--- |
| pb_359_7 | Proteobacteria | Alphaproteobacteria | Rhodobacterales  | Rhodobacteraceae  | Antarctobacter | -TCAACTTGAGAGTTTGATCC | TCACCTCCTTTCTAA--- |
| pb_359_8 | Bacteroidetes  | Flavobacteriia      | Flavobacteriales | Flavobacteriaceae | Arenibacter    | CAACGATGAAGAGTTTGATCC | ACACCTCCTTTCTAGA-- |

* pb_359_7 is in the opposite alignment to the other samples...
* All sequences but pb_359_7 reversed so that all contained the CCTCCT near the end
* Observation - very clear differences between different phyla/classes/orders/families
 * Note: Possible that one or two bases at the ends are missing...?
  * Specifically - Should there be a T at the start of pb_359_2's sequence?

* Is RNAmmer cutting off at the first CCT?
 * All sequences start with AGAGTTTGATC and end with TGCGGCTGGA(T/A)CACCT
 * Seems to be making conservative guesses...
* Metaxa2 - also conservative?
 * Unsure what to make of Metaxa2 results; pb_359_8 in particular is twice as long as the others...

## Mauve
Arenibacter echinorum 'Move contigs' keeps crashing; run the others and then retry?

# 25 November 2016

## 16S
* Aim - tabulate the closest 16S matches AND the closest NAMED 16S matches for each species

## To do
* Finish calculating percentages, and obtain the rest of the required information

# 28 November 2016

## 16S
* Obtain information on uncultured species closely related to our species

## Gitlab
* Repository on data5 has been compressed
 * Repository on personal laptop must also be compressed...

* To do:
 * Delete repository on Gitlab
 * Rename _copy repository
 * Point existing repositories to the new one
  * git remote set-url origin [new SSH address]
  * git remote set-url --push origin [new SSH address]

Re: partial sequences:
* Compare Oskar's data with species description

* Add note on within-sequence differences for Marinobacter comparison (10bp)


* Retrieve genome announcements and taxonomic descriptions for the species which MAY be other strains of pb_359_X

# 29 November 2016

## Similar species to investigate
* pb_359_2
 * Roseovarius mucosus DSM 17069
  * R. mucosus description downloaded
  * R. mucosus genome announcement downloaded
* pb_359_3
 * Loktanella vestfoldensis DSM 16212 (= R-9477)
  * L. vestfoldensis description downloaded
  * REQUIRE GENOME ANNOUNCEMENT
* pb_359_4
 * Sphingorhabdus sp. M41
  * S. sp. M41 genome announcement downloaded
  * REQUIRE TAXONOMIC DESCRIPTION
 * Sphingopyxis flavimaris strain R-36742
  * Note: reclassified as Sphingorhabdus flavimaris (paper downloaded)
  * S. flavimaris description (type strain SW-151, not R-36742) downloaded
  * REQUIRE GENOME ANNOUNCEMENT
  * S. flavimaris R-36742 not sequenced (environmental sample)
* pb_359_5
 * Marinobacter algicola DG893
  * M. algicola description downloaded
  * REQUIRE GENOME ANNOUNCEMENT
 * Marinobacter sp. MCTG268
  * M. sp. MCTG268 genome announcement downloaded 
  * REQUIRE TAXONOMIC DESCRIPTION
* pb_359_6
 * Sulfitobacter pseudonitzschiae strain H3
* pb_359_7
 * Antarctobacter heliothermus strain EL-21
  * Partial sequence...
* pb_359_8
 * Arenibacter algicola strain TG409


Send Oskar email with names of closest species; in particular, similar species
to Sphingorhabdus and Antarctobacter

Make a list of the species in the relevant taxonomic groups, with hyperlinks to the relevant papers
* Highlight those species with a high 16S similarity to pb_359_X (95% and above)
 * NCBI currently very slow...

* Wednesday - start from pb_359_5

# 30 November 2016

## Observation requiring further investigation...
* Initial GC-MS of Skeletonema marinoi (not axenic, so including the microbiome...) indicated the
presence of a precursor to domoic acid; this toxin is associated with the diatom Pseudo-nitzschia.
 * pb_359_6 may be Sulfitobacter pseudonitzschiae...
 * Need to know which genes are responsible for domoic acid biosynthesis...

## Rearrangement
* 16S details are currently scattered, so will move 16S folders into a single place

## Question
How should we define a bacterial species, with regard to whether pb_359_X correspond to existing
species?
* From "The bacterial species definition in the genomic era" - Konstantinidis, Ramette & Tiedje:
"ANI is the average nucleotide identity of the total genomic sequence shared between two strains,
and our previous studies suggest that ANI is an exceptionally robust and sensitive method for
measuring evolutionary relatedness among closely related bacterial strains, i.e. those showing
higher than 60% ANI, which, typically, corresponds to greater than 97% 16S rRNA gene sequence
identity."
* Evolutionary and ecological relatedness?

## Taxonomy
* pb_359_5 results complete; _6, _7 and _8 need completing
 * BlastN acting up...

# 1 December 2016

## Mauve results
* pb_359_2 and Roseovarius mucosus seem moderately well aligned, although there are some areas
which don't line up.
* pb_359_3 and Loktanella vestfoldensis DSM 16212 line up fairly well, although SKA53 shows
a lot of rearrangement.
* pb_359_5 and Marinobacter algicola DG893 align almost perfectly.
 * MCTG268 is also a close match, but not quite as good as M. algicola.
* pb_359_6 doesn't show hugely convincing results vs. any of the Sulfitobacter species.
* pb_359_7 and Antarctobacter heliothermus give a very good alignment.
* pb_359_8 and Arenibacter algicola give a very good alignment.
 * Arenibacter palladensis also gives a good alignment.
 * Arenibacter troitsensis also gives a good alignment.

* Attempting to run longest contig of pb_359_6 vs Sulfitobacter pseudonitzschiae, the closest
named species to pb_359_6 in terms of 16S rRNA similarity

## Notes on closely-related species
* pb_359_2 - Roseovarius mucosus
 * Associated with a dinoflagellate (a different group of marine plankton to diatoms)
* pb_359_3 - Loktanella vestfoldensis
 * Found in microbial mats in the Antarctic
* pb_359_4 - Sphingorhabdus flavimaris
 * Found in the Yellow Sea, Korea; isolated from sea water...
* pb_359_5 - Marinobacter algicola
 * Found associated with dinoflagellates (two species known for producing toxins)
* pb_359_6 - Sulfitobacter pseudonitzschiae
 * Associated with toxic marine diatom Pseudo-nitzschia
* pb_359_7 - Antarctobacter heliothermus
 * Found at varying depths in an Antarctic lake
* pb_359_8 - Arenibacter algicola
 * Associated with Skeletonema costatum

## Interesting paper re: diatom-microbiome interaction (Pseudo-nitzschia)
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3869016/

* From Supplementary Material - "The family Rhodobacteraceae is highly represented
(56 - 98%) in all 3 Pseudo-nitzschia species"
 * Predisposition for Rhodobacteraceae to be associated with diatoms? 4/7 of our species
were from this family
* "Consequently, OTUs homologous to Sulfitobacter, Roseobacter, Phaeobacter, Rhodobacter and
Sphingophyxis are all common associates of the three Pseudo-nitzschia species (Figure S3).
Marinobacter, Alteromonas, Roseobacter and Sulfitobacter are also commonly reported to be
associated with several marine phytoplankton species, and can be considered as the core
microbiome of marine phytoplankton."
 * These, or closely-related genera, account for 4/7 of our species
* "Remarkably, bacteria-free Pseudo-nitzschia consistently have low fitness, suggesting that
microbiota do indeed have a significant role in the well-being of diatom hosts, just like in
animal and plant host-microbiota systems"
 * Consistent with S. marinoi
* Roseo(bacter/varius) - parasitic?
* + DA = - bacterial diversity
* **Note**: Pseudo-nitzschia only distantly related to Skeletonema; Thalassiosira more closely related...

# 2 December 2016

## Annotation
Potential improvements:
* Any more databases to add?
* Consider installing RNAmmer for rRNA prediction
* Use --rfam flag for ncRNA search

Having previously extracted the sequences for hypothetical proteins from the annotation .faa file,
attempting to run the results through BlastP (E-value threshold 1e-40) to see if any convincing
hits appear.

## Interesting paper re: algicidal bacteria
http://onlinelibrary.wiley.com/doi/10.1111/j.1550-7408.2004.tb00538.x/full

* Potential algicidal compounds - ectoproteases/serine proteases
* Algicidal activity only at concentrations greater than 10^6 cells/ml?

Would presence of chitinase be a potential indication of algicidal activity?
* S. costatum produces chitin, though unsure of the purpose (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2708456/)
 * pb_359_2 (Roseovarius) has downstream components of a chitin-degradation pathway
  * Polymeric compounds degradation; Beta-hexosaminidase nagZ predicted
  * Also present in _3, _4, (not _5), _6, _7 and _8
  * Also involved in anhydromuropeptide recycling... Likely false positive...


Other identified algicidal compounds - rhamnolipid biosurfactant, PG-L-1 and prodigiosin pigment

# 5 December 2016

## Announcement papers
Focus on _4 and _7

## Assemblies
Double-check assembly details to be certain that the best assembly has been chosen...  
RATIONALE FOR CHOOSING THE ASSEMBLER

| Sample | HGAP | Falcon         | Canu           |
|--------|------|----------------|----------------|
| _2     | 3    | 3 - 4,381,426* | 3 - 4,381,186  | Falcon longest, Falcon selected - OK
| _3     | 5    | 3 - 3,987,360* | 5 - 4,117,035  | Canu longer BUT questionable final contig - OK
| _4     | 1    | 1 - 3,487k     | 1 - 3,479,724* | Falcon longest BUT has a big dip - OK
| _5     | 1    | 2 - 4,391k     | 2 - 4,630,160* | Canu longest, Canu selected - OK
| _6     | 9    | 8 - 5,121,602* | 9 - 5,140,887  | Canu longer BUT questionable final contig - OK
| _7     | 4    | 4 - 5,327k     | 4 - 5,331,190* | Canu longest, Canu selected - OK
| _8     | 1    | 2 - 5,857,781* | 3 - 5,877k     | Canu longer BUT questionable final contig - OK

## Annotation
* Prokka cutoff appears to be 1e-06
* Prokka accepts a trusted list of proteins to annotate from before going to other databases;
create a family-specific .fa file and use this? Remove 'hypothetical proteins'

fasta2tab <FASTA_FILE> | grep -v "hypothetical_protein" | tab2fasta > <OUTPUT_FILE>

* Prokka running for pb_359_4, but looking at the .sge.e#### file, it doesn't appear that
any results have been obtained from Sphingomonadaceae.faa
 * May be a problem with naming conventions; perhaps replace ".1_" with ".1~~~", and remove
underscores?
 * Also remove [species name] from each entry

# 6 December 2016

## Annotation
Sphingomonadaceae.faa has been altered as described yesterday; rerunning Prokka...
* In the previous run, proteins were labelled as hypothetical as the format of the fasta header
wasn't recognised; based on the files in /db/prokka, the format should now be correct...
* Removed tildes etc., just left the name of the protein as the fasta header. Rerunning Prokka
again...
* Formatting is STILL being awkward; reviewing the PROKKA manual, it appears that the format
is VERY specific. If GenBank files can be acquired for the relevant organisms, then the
`prokka-genbank_to_fasta_db` script can be run, followed by concatenation (SEE MANUAL!)
 * Would require a reworking of the NCBI_Downloader script...

* NCBI_Downloader_GenBank.py now complete
 * **FUTURE TASK** Combine NCBI_Downloader files; add argument which states the file type you
wish to download...

* Downloading .gbff (GenBank) files
 * `prokka-genbank_to_fasta_db *.gbff > Sphingo.fasta`
 * `fasta2tab Sphingo.fasta | grep -v "hypothetical protein" | tab2fasta > Sphingo2.fasta`
  * Ensure that formatting is preserved!
 * 2-3 hypothetical proteins; fasta2tab step unnecessary?

Tomorrow - check results of second Prokka run, see if the Sphingo protein file has finally
been accepted?

# 7 December 2016

## Annotation
For pb_359_4:
* Named genes have decreased dramatically - 922 -> 88
* Decent decrease in the number of hypotheticals - 745 -> 616
* Running Pathway Tools to compare number of pathways and other results...

Try ONLY including the named genes from Sphingomonadaceae in the fasta file?
*`fasta2tab Sphingomonadaceae.fasta | grep -v "~~~~~~" | tab2fasta > Sphingomonadaceae_named.fasta`
* Number of genes drops from 91,915 to 1723...
* Attempting with Sphingomonadaceae_named.fasta - pb_359_4_3
 * Number of named genes has almost doubled vs. the first attempt - 922 -> 1724
 * Number of hypothetical proteins has increased slightly - 745 -> 818
 * Once pb_359_4_2 has completed in Pathway Tools, run _3 through it and compare results

It seems that at least one of these two approaches will produce a more informative pathway
analysis; prepare the other samples
* pb_359_2, _3, _6, _7 - Rhodobacteraceae
* pb_359_4 - Sphingomonadaceae/Erythrobacteraceae
* pb_359_5 - Alteromonadaceae
* pb_359_8 - Flavobacteriaceae

* Forgot to run the 'remove hypothetical proteins' step...
 * For Rhodobacteraceae, only 4 hypotheticals so not too big of a problem
 * For Alteromonadaceae, only 2 hypotheticals; not too big of a problem
 * For Flavobacteraceae, 26 hypotheticals - remove these

* pb_359_2 - the differences were not quite so dramatic... (rerun?)
* pb_359_3 - modest difference in the longest chromosome (rerun?)
* pb_359_5 - again, not such a huge difference... (rerun?)
* pb_359_6 - very slight difference
* pb_359_7 - big improvement
* pb_359_8 - very slight difference

Comparing the three pb_359_4 runs:

|                     | Regular | + All Sph prot | + Named Sph prots | Mega all | Mega named |
|---------------------|---------|----------------|-------------------|----------|------------|
| Pathways            | 232     | 203            | 247               | 202      | 256        |
| Enzymatic reactions | 1572    | 1257           | 1713              | 1279     | 1750       |
| Transport reactions | 27      | 7              | 18                | 7        | 20         |
| Enzymes             | 1051    | 908            | 1191              | 918      | 1168       |
| Transporters        | 23      | 13             | 29                | 13       | 25         |
| Compounds           | 1371    | 1155           | 1492              | 1175     | 1533       |

Overall, annotation appears to have improved, BUT some proteins' predicted functions have changed,
even those which had a function in the initial run. Which annotation should be trusted?
* Compromise - cat *.fasta onto the end of the Prokka database file
 * Attempt with both standard and name-only?
 * If the second concatenation gives a comparative result to '+ Named Sphingo prots', run with this
  * Don't want to overwrite better sprot results with worse Sphingo results, hence concatenation
 * If the Sphingo result is better - can it be trusted?

Compare pb_359_4_3 and pb_359_4_mega_named:
* _3: 1724 named, 818 hypothetical
* _named: 1688 named, 823 hypothetical

| Approach           | # named genes | # hypothetical | # pathways |
|--------------------|---------------|----------------|------------|
| Standard Prokka    | 922           | 745            | 232        |
| --proteins (all)   | 88            | 616            | 203        |
| --proteins (named) | 1724          | 818            | 247        |
| cat sprot all      | 122           | 617            | 202        |
| cat sprot named    | 1688          | 823            | 256        |

**Run _mega_named through Pathway Tools?**
* Can be run without creating a cellular overview, which would save time
 * In which case, run _mega_all for comparison too
 * Differences between pb_359_4 and pb_359_4_3 saved to 'Differences' file

# 8 December 2016

## Annotation
Running _mega_all and _mega_named through Pathway Tools for comparison
* As expected, _mega_named appears to give the best overall results

## Mauve
Ran pb_359_4 vs. Sphingorhabdus sp. M41 - the two appear almost identical.

### Other notes on pb_359_4
* According to [the paper where Sphingorhabdus was first proposed] (http://ijs.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.043133-0),
there is a big disconnect between Sphingorhabdus and Sphingopyxis G+C content:
 * Sphingorhabdus - 52.6%-57.8% (pb_359_4 = 58.0%)
 * Sphingopyxis - 62.3%-69.2%
* Comparing a handful of Sphingorhabdus and Sphingopyxis 16S sequences with pb_359_4,
there is a clear divide between the two genera, and pb_359_4 definitely seems to fall within
the Sphingorhabdus genus.

## Annotation
* --proteins flag using named only
 * Ensure all species have a result generated for this setting
 * 2, 3, 4, 5, 6, 
* Identify unique pathways in each bacterium

# 16S
Compare Alvar's species to pb_359_X to rule out duplicates
* None of the suspected genus names are the same
* Will compare to the Metaxa2 predictions to check for, at least, partial similarities
 * Genome4 - No close similarity (~80% similar to pb_359_4 16S)
 * Unitig0 - No close similarity (~50-60% similar to pb_359_5 16S)
 * Kordia - No close similarity (~50-60% similar to pb_359_8 16S)

## Annotation problem
Sometimes, the new annotations give a WORSE result in terms of the number of predicted pathways
* pb_359_2 - pathways have decreased from 293 to 269 - X
* pb_359_3 - pathways have decreased from 306 to 292 - X
* pb_359_4 - pathways have increased from 232 to 247 - O
* pb_359_5 - pathways have decreased from 269 to 257 - X
* pb_359_6 - pathways have decreased from 304 to 294 - X
* pb_359_7 - pathways have increased from 299 to 301 - O
* pb_359_8 - pathways have decreased from 268 to 268 - X

(Have been ticking 'circular'; does unticking make a difference...)

* pb_359_2 (Roseovarius)

|                     | Regular | + Named | vs Reg | + All Named | vs Reg |
|---------------------|---------|---------|--------|-------------|--------|
| Pathways            | 293     | 269     | Worse  | 267         | Worse  |
| Enzymatic reactions | 1917    | 1773    | Worse  | 1773        | Worse  |
| Transport reactions | 41      | 21      | Worse  | 24          | Worse  |
| Enzymes             | 1383    | 1354    | Worse  | 1319        | Worse  |
| Transporters        | 63      | 35      | Worse  | 38          | Worse  |
| Compounds           | 1638    | 1532    | Worse  | 1528        | Worse  |

* pb_359_3 (Loktanella)

|                     | Regular | + Named | vs Reg | + All Named | vs Reg |
|---------------------|---------|---------|--------|-------------|--------|
| Pathways            | 306     | 292     | Worse  | 287         | Worse  |
| Enzymatic reactions | 1928    | 1852    | Worse  | 1830        | Worse  |
| Transport reactions | 39      | 21      | Worse  | 25          | Worse  |
| Enzymes             | 1311    | 1278    | Worse  | 1260        | Worse  |
| Transporters        | 68      | 34      | Worse  | 40          | Worse  |
| Compounds           | 1659    | 1589    | Worse  | 1579        | Worse  |

* pb_359_4 (Sphingorhabdus)

|                     | Regular | + Named | vs Reg | + All Named | vs Reg |
|---------------------|---------|---------|--------|-------------|--------|
| Pathways            | 232     | 247     | Better | 228         | Worse  |
| Enzymatic reactions | 1572    | 1713    | Better | 1591        | Better |
| Transport reactions | 27      | 18      | Worse  | 19          | Worse  |
| Enzymes             | 1051    | 1191    | Better | 1149        | Better |
| Transporters        | 23      | 29      | Better | 28          | Better |
| Compounds           | 1371    | 1492    | Better | 1425        | Better |

* pb_359_5 (Marinobacter)

|                     | Regular | + Named | vs Reg | + All Named | vs Reg |
|---------------------|---------|---------|--------|-------------|--------|
| Pathways            | 269     | 257     | Worse  | 252         | Worse  |
| Enzymatic reactions | 1832    | 1734    | Worse  | 1736        | Worse  |
| Transport reactions | 35      | 14      | Worse  | 18          | Worse  |
| Enzymes             | 1332    | 1309    | Worse  | 1323        | Worse  |
| Transporters        | 42      | 27      | Worse  | 32          | Worse  |
| Compounds           | 1543    | 1459    | Worse  | 1459        | Worse  |

* pb_359_6 (Sulfitobacter)

|                     | Regular | + Named | vs Reg | + All Named | vs Reg |
|---------------------|---------|---------|--------|-------------|--------|
| Pathways            | 304     | 294     | Worse  | 279         | Worse  |
| Enzymatic reactions | 1996    | 1889    | Worse  | 1865        | Worse  |
| Transport reactions | 44      | 18      | Worse  | 23          | Worse  |
| Enzymes             | 1627    | 1612    | Worse  | 1577        | Worse  |
| Transporters        | 67      | 36      | Worse  | 43          | Worse  |
| Compounds           | 1748    | 1656    | Worse  | 1627        | Worse  |

* pb_359_7 (Antarctobacter)

|                     | Regular | + Named | vs Reg | + All Named | vs Reg |
|---------------------|---------|---------|--------|-------------|--------|
| Pathways            | 299     | 301     | Better | 291         | Worse  |
| Enzymatic reactions | 2042    | 2002    | Worse  | 1948        | Worse  |
| Transport reactions | 46      | 22      | Worse  | 24          | Worse  |
| Enzymes             | 1484    | 1670    | Better | 1645        | Better |
| Transporters        | 48      | 40      | Worse  | 43          | Worse  |
| Compounds           | 1749    | 1716    | Worse  | 1665        | Worse  |

* pb_359_8 (Arenibacter)

|                     | Regular | + Named | vs Reg | + All Named | vs Reg |
|---------------------|---------|---------|--------|-------------|--------|
| Pathways            | 268     | 262     | Worse  | 245         | Worse  |
| Enzymatic reactions | 1886    | 1849    | Worse  | 1733        | Worse  |
| Transport reactions | 19      | 15      | Worse  | 14          | Worse  |
| Enzymes             | 1486    | 1492    | Better | 1486        | Same   |
| Transporters        | 37      | 35      | Worse  | 36          | Worse  |
| Compounds           | 1559    | 1537    | Worse  | 1438        | Worse  |

* **pb_359_4 is the ONLY sample for which the --proteins [named] result is the better result...**
 * Marginally true for pb_359_7...

# 9 December 2016

# Annotation
Rerun all annotation attempts, but use a merger of ALL named proteins from the 4 previous
databases instead of just one family each.
* Modest improvement in number of named genes in all cases; now attempt Pathway Tools

## Note on Pathway Tools
Previously, I've been including the entire .gbk file as a single replicon; will try splitting
them up into their individual chromosomes and plasmids

* Go for max. number of pathways
 * Important - the number of pathways predicted doesn't correspond to the number in the
SmartTable; the numbers correlate with the number of pathways relative to one another, however
  * It includes super-pathways; these should be separated out

* Extract pathway lists from Pathway Tools and identify unique ones

# 12 December 2016

## Annotation
* pb_359_4 (Sphingorhabdus) appears to contain some components of the Enterobacterial Common
Antigen biosynthesis pathway; this pathway is supposedly restricted to Enterobacteriaceae...
 * Double-check vs. original pb_359_4 annotation
  * TDP-fucosamine acetyltransferase
   * The annotation only appears when using named genes, but no gene name is given...
   * Alternate annotation - GCN5 family acetyltransferase
  * wecB and wecC
   * As above, only appears when using named genes
   * Alternate annotation for wecC - UDP-N-acetyl-D-mannosaminuronic acid dehydrogenase
    * wecB annotation is the same

* pb_359_8 (Arenibacter) contains components of the pectin degradation II pathway
 * Pectin is present in diatom frustules
 * The top part of the pathway is present; do these enzymes have other purposes?
  * pemA and pehX - no othe purpose
  * Pathway lacks presence of digalacturonate lyase
  * Evidence of presence of downstream pathways
   * pemA not present in annotation using ALL Flavo hits, implying an unnamed hit was better
    * Unnamed hit - pectate lyase
     * Multiple pectate lyase hits in this annotation, and nowhere else
   * pehX, as above, not present in the all Flavo database-using version
    * Unnamed hit - glycoside hydrolase
 * ["It is known that the members of Flavobacteria are especially proficient in degrading various
biopolymers, such as cellulose, chitin, and pectin"] (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4646686/)

*_3, _5 and _7 only species predicted to have alginate-related pathways (other species seem to
possess some alginate-related genes, however...)
 * All three have components of the alginate degradation pathway
  * _5 has one component (algL alginate lyase)
  * _3 has two components (algE7 alginate lyase and kdgK 2-dehydro-3-deoxygluconokinase)
  * _7 has two components (algE7 alginate lyase and kdgK 2-dehydro-3-deoxygluconokinase)
 *_5 (Marinobacter) contains all components of the alginate biosynthesis II pathway

* _3, _6 and _8 contain elements of trehalose biosynthesis pathways
 * Trehalose involved in survival of desiccation
 * Implications for when Skeletonema becomes dormant; survival of microbiome?

* Look into different types of siderophores (e.g. aerobactin, enterobactin)

* Most of the species have various glycolate oxidase subunit genes, implying potential use of
glycolate as a carbon source; if released by Skeletonema? (produced by photoautotophs)
 * Only _7 seems to possess glcD; many possess glcE and an iron-sulfur subunit

* Pigments - neurosporene
 * _2, _3, _4, _5 and _8 are predicted to contain the neurosporene biosynthesis pathway
 * Under class Carotenoids Biosynthesis:
  * _2:
   * Trans-lycopene biosynthesis (all components)
    * Final step appears spontaneous, but not highlighted?
   * Spheroidene and spheroidenone biosynthesis (3/5 components)
   * Spirilloxanthin and 2,2'-diketo-spirilloxanthin biosynthesis (4/5 components)
  * _3:
   * Trans-lycopene biosynthesis (all components)
   * Spheroidene and spheroidenone biosynthesis (3/5 components)
   * Spirilloxanthin and 2,2'-diketo-spirilloxanthin biosynthesis (4/5 components)
  * _4:
   * Trans-lycopene biosynthesis (all components)
    * Enzymes present in final step, but not highlighted?
  * _5:
   * Trans-lycopene biosynthesis (3/5 components (missing first two))
  * _8:
   * Trans-lycopene biosynthesis (all components)
    * Enzymes present in final step, but not highlighted?

# 13 December 2016

## Tasks
* Add references to the announcement papers
* Continue searching for interesting pathways
 * Investigate presence of secretion pathways?

## Prokka
rRNA module now installed for Prokka; rerun annotations to include rRNA information

## Annotation
* Check on chitinase annotation
* Check for antibiotic resistance genes

# 14 December 2016

## Genome announcements
* Major references added to Google Docs versions of the announcement papers
* Rerun Prokka now that rRNA module has been installed; create a Final_Annotations folder cf. the Final_Assemblies folder?
 * Predicted number of loci are more or less consistent with the previous annotation; seems
as though some hypothetical loci were disrupted
* Consider running Prokka with the --rfam flag for ncRNA prediction?
 * Running for pb_359_2; comparison to previous run:
  * 

## Annotation
* Observation - pb_359_4 has 46 copies of the gene benD?? Involved in benzoate degradation...
 * Degradation of polychlorinated biphenyls (PCBs)?
* pb_359_7 appears to lack a tmRNA prediction, whereas all others have one; apparently this
feature is universal among eubacteria
 * SsrA-binding protein smpB is present, however...
 * Possible that Antarctobacter (relatively unstudied genus) has an unrecognised SsrA?


## Pathway Tools
Uploading yet another version of each .gbk file to Pathway Tools
* 'Final' prefix

## To do
Run _7 and _8 final annotations through Pathway Tools and double-check whether this has made
any difference to the pathways predicted; it shouldn't have done, as the number of CDSs appears
to have remained constant...

# 15 December 2016

## Pathway Tools
All final annotations now uploaded to Pathway Tools  
Number of pathways has remained constant. Identity?  
(find-replace, remove column 1 and row 1)
* Using diff - all pathways are the same

## Observations
MarR and MarA antibiotic resistance genes

## Grepping lines before and after a hit
-A (after), -B (before) and -C (before AND after)
-A7 -B1

# 16 December 2016

Start to write individual plasmids' information in the announcement papers

# 19 December 2016

To do:
* Add any relevant parameters from assembly to the announcement papers

# 9 January 2017

## pb_359_2
[Genome announcement of Roseovarius mucosus] (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4511512/)

* Two glycine betaine biosynthesis pathways - I and IV. IV is apparently a very energy-consuming process,
so is there a benefit to this redundancy...?
* Investigating absence of bacteriochlorophyll A synthesis genes in final annotation; appears in pb_359_2_2
(where Rhodobacteraceae database is searched first); in final annotation it is labelled as PUCC protein...

* Check the products/pathways on the Roseovarius plasmids and see what they contain
 * Plasmid 1 seems to contain a lot of cytochrome- and metal import/export-related genes
 * Plasmid 2 contains several genes involved in mercury resistance?
* Viewed in Pathway Tools (both final annotation and pb_359_2_2), the plasmids seem to encode no obvious pathways by themselves...
 * 2/3 components of phosphatidylcholine biosynthesis V pathway - "This pathway is found in animals, yeast, and bacteria that interact with eukaryotic cells" (BioCyc)
* Found 4x plasmids from previous R. mucosus genome (DSM 17069), but purely by eyeballing, can't see any obvious link to current plasmids...

* Check number of vitamin B12/cobalamin biosynthesis genes in each species and determine which of them have the most complete pathways; these would potentially
be the most likely ones to be involved in providing the vitamin to Skeletonema
 * Try the same thing with siderophores (and read up on the biology of siderophores)

# 10 January 2017

## pb_359_2
More reliable way of checking the plasmids - download and concatenate, then blast
* Decent long match between the longest DSM 17069 plasmid and the longest pb_359_2 plasmid:
 * 26148-74585 on DSM 17069 vs 8350-56784 on pb_359_2 (Identities = 47548/48456 (98%), Gaps = 39/48456 (0%))
  * This accounts for between one-third and one-quarter of the size of the largest plasmid of pb_359_2
  * This accounts for between one-half and one-third of the size of the largest plasmid of DSM 17069
 * Three more matches of >1000bp
* Shortest DSM 17069 plasmid had one match >1000bp; middle two plasmids had either short or no matches

Blast the pb_359_2 segment which matches the DSM 17069 plasmid
* Big section in the middle with no matches, but the closest matches are to Ruegeria mobilis, Celeribacter indicus and Marinovum algicola (all plasmid sequences)
 * Marinovum algicola isolated from a dinoflagellate...

* Regarding Celeribacter indicus:
 * "...the taxonomic distributions of the five plasmid proteomes of strain P73T were different from that of the chromosome, suggesting the chromosome and the plasmids
 may have had potentially different origins... For pP73B they matched Roseovarius (41, 28.67%) and Celeribacter (23, 16.08%)..."
From [Genomic and metabolic analysis of fluoranthene degradation pathway in Celeribacter indicus P73T] (http://www.nature.com/articles/srep07741)
 * Unfortunately, a lot of the genes on the p73B plasmid appear not to be characterised...



Put the 4x R mucosus DSM 17069 plasmids into Pathway Tools and compare to the 2x from R3
* Also enter the full DSM 17069 GenBank

| Pathway                                               | Present in R3? | Present in DSM 17069? |
|-------------------------------------------------------|----------------|-----------------------|
| Palmitate biosynthesis II (bacteria and plants)       | Yes            | -                     |
| **Phosphatidylcholine biosynthesis V**                | Yes            | Yes                   |
| Cyclopropane fatty acid (CFA) biosynthesis            | Yes            | -                     |
| Fatty acid elongation - saturated                     | Yes            | -                     |
| CMP-3-D-manno-octulosonate biosynthesis               | Yes            | -                     |
| **Glutathione-glutaredoxin redox reactions**          | Yes            | Yes                   |
| Reactive oxygen species degradation                   | Yes            | -                     |
| PRPP biosynthesis I                                   | Yes            | -                     |
| Superoxide radicals degradation                       | Yes            | -                     |
| Cellulose and hemicellulose degradation (cellulosome) | -              | Yes                   |
| L-carnitine degradation I                             | -              | Yes                   |
| L-arginine degradation V (arginine deiminase pathway) | Yes            | -                     |
| **Phenylmercury acetate degradation**                 | Yes            | Yes                   |
| 2-oxopentenoate degradation                           | -              | Yes                   |
| Pyrimidine deoxyribonucleosides degradation           | Yes            | -                     |

Align DSM 17069 plasmids and R3 plasmids in Mauve, in case ours are the results of a fusion (hence the lower numbers)?
* Doesn't appear to be a fusion... If it is, then it was very ancient perhaps?

Pathways unique to R3 (vs. DSM 17069)
* Chitobiose degradation
* Xanthan biosynthesis


Annotation pb_359_2_2 has been thus far disregarded, as most of the genes had no name; however, more had a function than with
any other annotation attempt.
* Running the resultant .gbk file through Pathway Tools to check number of pathways, in case it has more pathways than the current
'final' annotation...
 * 236 pathways, less than any other annotation...
 * However, includes pathway for 3,8-divinyl-chlorophyllide a biosynthesis (a chlorophyll intermediate)
  * This pathway is present in R mucosus DSM 17069...
  * The chlorophyll a synthase predicted in pb_359_2_2 was inferred from a sequence from Roseobacter

# 11 January 2017

## GenBank consensus script

Aim: Write a script which will make a consensus of multiple GenBank files, overwriting 'hypothetical' proteins with those
of known function.

* 1_Copy_GenBank_Header.py appears to work; can print the initial, non-record elements of the first GenBank file into the output file.
* 2_Print_GenBank_Record.py can print most of a GenBank record in the correct format
 * Need to work out newline character in translation line
 * Need to work out how to spread Inference and Note across multiple lines, one per entry
* 3_Compare_GenBank_Records.py allows a 'hypothetical protein' product in the primary GenBank to be overwritten with a non-'hypothetical protein' entry in another
 * Need to add the capacity to print the rest of the entry as well





## Blast server
Blasting pb_359_2 assembly vs. Skeletonema on the Blast server
* Username: skeletonema
* Password: b******a

Best match: ATP synthase subunit beta atpD
* Another strong match to ATP synthase subunit alpha atpA
* Phosphomethylpyrimidine synthase thiC
* Chaperone protein dnaK
* Elongation factor G fusA
* NADH-quinone oxidoreductase chain 1 nqo1


## gcPlot.py
Some regions of v. low GC content exist in pb_359_2; use gcPlot to check the locations and see what is encoded in these regions; may be viral
* See whether one can search for LOCATION-specific genes in Pathway Tools to see which pathways a particular region's genes are involved in

* Minimum value exists around 3.06 Mb; checking this region against the annotation, there is a cluster of genes:
 * 5 hypothetical proteins
 * Insertion element uncharacterised 12.0 kDa protein
 * Integrase core domain protein
* Slightly further downstream, more hypothetical proteins and transposases

## To do
Find notes on transposable elements

# 12 January 2017

## GenBank_Consensus.py
Almost complete; need to work out the formatting of the 'translation' line
* Appears to be workable without this formatting
* Need to try on a proper dataset; ensure formatting works for other types aside from CDS and tRNA
* NEED TO ACCOUNT FOR DATABASES WHICH INCLUDE MORE FEATURES THAN THEIR PREDECESSORS; THESE WILL THROW OFF THE NUMBERING

## To do
Investigate the viral component of R. mucosus R3 on Web Apollo on Albiorix

# 13 January 2017

## GenBank_Consensus.py
Script appears to be functional; only change needed is to format the 'Translation' field of each record so that it adheres
to the proper formatting, i.e. adding newlines and restricting the character limit per line to 79.
* Note: only currently works for GenBank files containing a single contig; will have to split up the others into per-contig GenBanks.

Problem - by including a tab in the CDS/tRNA/rRNA/misc line, I've inadvertently confused BioPython when it tried to interpret the resultant file
* Need to remove the tab character and replace it with the appropriate number of spaces - SOLVED
* Need to investigate propagation of the 'notes' value; should not be transferred from one file to the next...
* Need to import locus tag from primary input, not secondary input

## pb_359_2
* Split the GenBanks up into individual contigs
* Generate series of consensuses:
 * Final vs. _2 -> A
 * A vs. _3 -> B
 * B vs. _All -> C
* Check stats of C

## Git
'git status' command was bringing up a lot of untracked files
* Added a lot of files (unused Prokka outputs, .sge.*, etc.) to .gitignore
* Committed the rest of the untracked files

## To do:
* Investigate the viral component of R. mucosus R3 on Web Apollo on Albiorix
* Investigate Note problem in GenBank_Consensus script
* Fix problem with locus tags

# 16 January 2017

## To do:
* Run GenBank_Consensus script on R. mucosus
 * Attempt to fix the Note problem in the script (if Note exists, overwrite it?)
* Re-download notes on viral genomes and identify TE/viral elements in R. mucosus

## GenBank_Consensus
* Notes problem fixed - duplicate From*.gb/From*.gbk lines removed
* Running the final consensus file through Pathway Tools results in ten less pathways...
 * Why?
* TestRoseoFinal database (NewVersionTest) - running 'final' annotation in Pathway Tools
 * Doesn't yield the same number of pathways as previously
 * Conclusion: The new version of pathway tools predicts the number of pathways differently to the old versions
  * Analyses will have to be redone to check figures...
* Written a .sge script to automate the whole process of GenBank_Consensus steps

## Pathway Tools
* Rescored the original 'final' Roseovarius result; now shows either 280 or 283 pathways, depending on whether
the original is rescored, or the original file is reuploaded entirely. Either way, the consensus file appears
to give the best overall result now in terms of less hypotheticals and the same/more total pathways
 * Will redo the analyses with v20.5 of Pathway Tools (originally done in 20.0)

## To do
* Alter GenBank_Consensus.py to prioritise named genes

# 17 January 2017

## Pathway Tools
* Rerun old analyses to get a more accurate comparison of the number of pathways predicted between runs
 * All analyses must be brought forward to the new version

## GenBank_Consensus.py
* Added an expression to prioritise named genes, if one exists at a locus in the secondary input but not in the primary input
 * Running the GenBank files in reverse order through this script, from the GenBank with the most named entries to the least
 * Results in the same # of named genes, as one would expect...

## To do
* Run remaining GenBank_Consensus_4.5 files through Pathway Tools (Starting with Sphingo consensus)
* Generate GenBank_Consensus_Names output files and run THESE through Pathway Tools
* Finish writing the READMEs for the GenBank_Consensus results (6-8)

# 18 January 2017

## Pathway Tools
* For pb_359_2, Consensus_4.5 has one more pathway predicted than Consensus_Names
 * Would have expected more named genes to equal more predicted pathways
 * If this trend continues, compare the lists of pathways
* For pb_359_3, Consensus_Names had three more pathways predicted than Consensus_4.5

* Question - does it matter whether .gbk files are uploaded to Pathway Tools as per-contig files, or can
they all be uploaded as a single file...?
 * Seems to make no difference; can continue without uploading each contig separately

| Sample   | Consensus     | Consensus_Names     | Differences |
|----------|---------------|---------------------|-------------|
| pb_359_2 | **284**       | 283                 | +5/+4       |
| pb_359_3 | 300           | **303**             | +1/+5       |
| pb_359_4 | **237**       | 235                 | +2/+0       |
| pb_359_5 | **261**       | **261**             | +3/+2       |
| pb_359_6 | 302           | **307**             | +2/+7       |
| pb_359_7 | 290           | **297**             | +1/+8       |
| pb_359_8 | 256           | **257**             | +1/+3       |

* Figures don't appear to add up, as # of pathways doesn't take into account 'superpathways'

* Overall, Consensus_Names seems to give the highest # of predicted pathways
 * Use this for ALL bacteria, or select on case-by-case basis?

## VirSorter
* Checking VirSorter predictions versus VirSorter database and R. mucosus results
 * Where neither of these turn up results, attempt Blast search
 * Started making a list of proteins in the viral region in 06_VirSorter/pb_359_2/README.md
  * Try to work out if the remaining genes have a known/suspected function...

# 19 January 2017

data5 offline; working from laptop.  
BACKUP TO GITLAB AT THE END OF THE DAY

Change GenBank_Consensus scripts to remove 'Both records hypothetical' note

Trying PHASTER bacteriophage predictor (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4987931/):
* pb_359_2/Roseovarius mucosus - http://phaster.ca/batches/BB_08ded19b26
 * The previously-explored region ~3.05Mb has a score of 100 (/150), whereas two other regions have scores of 140 and 150, respectively
* pb_359_3/Loktanella - http://phaster.ca/batches/BB_8abd2fdfb8
* pb_359_4/Sphingorhabdus - http://phaster.ca/submissions/ZZ_0576f774b4
* pb_359_5/Marinobacter - http://phaster.ca/batches/BB_d095410425
* pb_359_6/Sulfitobacter - http://phaster.ca/batches/BB_7cae19f6b7
* pb_359_7/Antarctobacter - http://phaster.ca/batches/BB_c5b9d025e7
* pb_359_8/Arenibacter - http://phaster.ca/batches/BB_12bb67a072

# 20 January 2017

## PHASTER
Need to find a convenient way to convert my generated .gbk files into .faa files so that I can use them as a blast database.

## pb_359_2
* With the output from PHASTER, there appears to be at least one phage in the chromosome, up to three

## Annotations
Problem: sometimes a gene name will be mentioned in the product line but not mentioned in the name field
* Will require manual annotation
* ~150 changes made to pb_359_2_Consensus_Names
 * Not changed if the line said 'xxx-like' or 'xxx-family'

	Try these in Pathway Tools on Monday!

# 23 January 2017

## Annotations
* Running pb_359_2 manually-adjusted annotation through Pathway Tools
 * Pathways - 283
  * Vs. ~284 from previous best analyses
  * Despite addition of explicitly-named components of the bacteriochlorophyll a synthesis pathway, these still appear as gaps in the pathway...

* Comparing photosynthetic gene cluster to that in Roseovariuis mucosus DSM 17069 - VERY similar gene order
 * 39 genes in cluster
* Largest plasmid in both cases contains type IV secretion system genes
 * In general, plasmid 1 of R3 seems to be an extension of A123 plasmid in DSM 17069
 * Similarity ends ~100 Kb into R3 plasmid 1
  * rosmuc_04171 corresponds to 04123 (RÂ3
* R mucosus DSM 17069 appears to have only 265 pathways
 * Flagellar protein region rosmuc00543 - rosmuc00574 matches 01702 - 01733 (R3)

* R3 seems to be lacking sulfoquinovosyl diacylglycerol biosynthesis pathway
 * 'found in all photosynthetic organisms'?
 * R3 appears to be missing other components of photosynthetic pathways cf. DSM 17069

* Blast R3 vs DSM 17069 - Blastn
 * Long R3 plasmid appears to be a merger of two of the DSM 17069 contigs; scaffold14 has 2x 100% identical matches to R3 (78 Kb and 8 Kb)
 * Almost all 17 scaffolds of DSM 17069 map to the chromosome and longest plasmid of R3
  * Scaffolds 11 and 13 do not hit anything in R3
   * Scaffold 11 - only 1012 bp...
   * (pRosMuc_C27) Scaffold 13 - 26,795 bp - contains type IV secretory system genes, but is this not redundant? e.g. 2x VirB4 genes in DSM 17069, just 1 in R3
    * However, DSM 17069 also contains trb genes involved in P-type conjugative transfer, and plasmid segregation genes, and yhaV toxin gene
  * Scaffold 12 has a short hit on the small R3 plasmid (1,429bp)
   * 16,653 to 18,078 (scaffold12 (DSM 17069)) (Antirestriction protein in this region)
   * 968 to 2,395 (short plasmid (R3) (DNA primase TraC in this region)
   * Both a comparable size in terms of # of base pairs

| DSM 17069 plasmid | Location in R3                                                                                                                  |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------|
| A123 (123,088 bp) | ~50% of R3 large plasmid (4Kb on R3 small plasmid; plasmid transfer genes? - traG and 'mobilisation protein' (+ hypotheticals)) |
| B85 (85,327 bp)   | ??? (only hits are a few hundred bases or less)                                                                                 |
| C27 (26,795 bp)   | ??? (no hits)                                                                                                                   |
| D21 (20,721 bp)   | ~1,500 bp hit on R3 short plasmid (TraC DNA primase, or antirestriction protein)                                                |

| R3 plasmid                | Location in DSM 17069                                                                     |
|---------------------------|-------------------------------------------------------------------------------------------|
| Long plasmid (180,135 bp) | Largely spread between scaffolds 14 and 15 (scaffold15 = A123 plasmid)                    |
| Short plasmid (30,295 bp) | 4 Kb hit to scaffold15 (A123 plasmid), 1.4 Kb hit to scaffold12 (plasmid transfer genes?) |

Three shorter DSM 17069 plasmids and shortest R3 plasmid appear to be unrepresented in the other strain...
* R3 has mercury resistance?
 * Plasmid seems to be missing a vitally important gene - MerB
 * Even after various Blasts, no MerB hits in shortest plasmid...
 * Doesn't have 'broad spectrumn' resistance to organic mercury compounds
 * DSM 17069 ALSO DISPLAYS MERCURY RESISTANCE
* Three shorter plasmids in DSM 17069 contain components of phosphatidylcholine biosynthesis pathway
 * R3 contains a different version of this pathway...

Observation - DSM 17069 replicons were never tested for circularity; assumed to be linear


CHECK ON TUESDAY - ARE THE PREDICTED VIRAL REGIONS OF STRAIN R3 ALSO PRESENT IN DSM 16079?

# 24 January 2017

## R. mucosus R3 viral regions vs DSM 17069

| Phage region and stats    | Matching region in DSM 17069                                                                                                 |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------|
| 1 (13,874 bp) (score 140) | scaffold1: 655,647 - 641,752 (matches almost entire phage); region in DSM 17069 contains concentration of phage proteins     |
| 2 (25,924 bp) (score 100) | scaffold6: 173,811 - 175,733; 175,757 - 177,023; region seems to contain very general genes                                  |
| 3 (75,114 bp) (score 150) | scaffold1: 256,258 - 250,464; 250,220 - 244,751; 262,568 - 257,297; 248,815 - 244,751; 243,527 - 240,019; 256,909 - 253,057; |
|                           |            236,712 - 232,982; 243,527 - 240,712; 236,706 - 232,982; 252,653 - 250,464; 268,312 - 266,416; 268,344 - 266,756; |
|                           |            238,891 - 237,024; 232,783 - 231,656; 258,778 - 257,299; etc... (general: 231,656 - 268,344); primarily Mu-like   |
|                           |            phage proteins and hypothetical proteins; also more fragmented than for phage region 1                            |
|                           | scaffold17: 464,087 - 464,766; 2x hypothetical proteins                                                                      |

## Check R3 plasmids vs other Roseovarius/Rhodobacteraceae plasmids?
* Long plasmid - Patchy, but Blast hits to Ruegeria mobilis plasmid, Celeribacter indicus plasmid, Marinovum algicola plasmid, Phaeobacter gallaeciensis plasmid,
Confluentimicrobium sp. EMB200-NS6 plasmid, Dinoroseobacter shibae DFL-12 plasmid, etc...
 * Conclusion - conserved Rhodobacteraceae plasmid?
* Short plasmid - Even patchier, but Blast hits to Sulfitobacter sp. AM1-D1 plasmid, Roseobacter denitrificans OCh 114 plasmid, Celeribacter indicus strain P73
plasmid; worse hits to other sequences including Paracoccus denitrificans PD1222 chromosome...
 * Conclusion - check 26,302 - . - 2395 of short plasmid (conserved? region)
  * Contains primarily transfer genes and hypothetical genes - also gene for molybdopterin-guanine dinucleotide biosynthesis protein A
 * Check 7,929 - 10,035 (matches Paracoccus chromosome)
  * Contains 3-hydroxy-D-aspartate aldolase and pheylserine dehydratase

* Blastn vs. refseq_genomic using R3 long plasmid
 * Roseovarius sp. TM1035 1101493006644, whole genome shotgun sequence - Coverage: 78%, E value: 0.0, Identity: 99%
* Blastn vs refseq_genomic using R3 short plasmid
 * Sulfitobacter sp. EhC04 A4_Contig27, whole genome shotgun sequence - Coverage: 26%, E value:	0.0, Identity: 92%



## Workflow
* Compare phage regions to related species
* Check synteny with most closely related species (type species if a strain?)
* Compare plasmids
* Identify unique regions to try and identify unique functions?



## refseq_genomic Blastn vs. plasmids - list some of the best hits
* pb_359_3 long plasmid
 * Best hits to Oceanibulbus and Sulfitobacter, 99% identity but <20% coverage (E value: 0.0)
 * Ruegeria hits with 98% identity and <35% identity (E value: 0.0) - still not amazing coverage...
* pb_359_3 short plasmid
 *  Sulfitobacter sp. EhC04 A4_Contig27 - Coverage: 20%, E value: 0.0, Identity: 93%

* pb_359_5 plasmid
 *  Thalassospira xiamenensis strain MCCC 1A03005 contig22 - Coverage: 3%, E value: 0.0, Identity: 98%

* pb_359_6 Plas_1:
 * Sulfitobacter pseudonitzschiae strain DSM 26824 - Coverage: 13%, E value: 0.0, Identity: 86%
 *  Sulfitobacter sp. 20_GPM-1509m ... scaffold00006.6_C - Coverage: 15%, E value: 0.0, Identity: 87%
* pb_359_6 Plas_2:
 * Sagittula stellata E-37 1101159001451 - Coverage: 6%, E value: 0.0, Identity: 83%
 * Sulfitobacter sp. 20_GPM-1509m ... scaffold00010.10_C - Coverage: 15%, E value: 0.0, Identity: 86%
 * Sulfitobacter pseudonitzschiae strain DSM 26824 - Coverage: 16%, E value: 0.0, Identity: 86%
* pb_359_6 Plas_3:
 * Sulfitobacter sp. 20_GPM-1509m ... scaffold00003.3_C - Coverage: 7%, E value: 0.0, Identity: 93%
 * Sulfitobacter pseudonitzschiae strain DSM 26824 - Coverage: 7%, E value: 0.0, Identity: 93%
* pb_359_6 Plas_4:
 * Sulfitobacter sp. CB2047 contig_5 - Coverage: 16%, E value: 0.0, Identity: 90%
 * Litoreibacter ascidiaceicola strain DSM 100566 - Coverage: 18%, E value: 0.0, Identity: 90%
 * Celeribacter indicus strain P73 plasmid pP73B - Coverage: 10%, E value: 0.0, Identity: 93%
* pb_359_6 Plas_5:
 * Roseovarius sp. MCTG156(2b) ... quiver.4_C - Coverage: 42%, E value: 0.0, Identity: 99%
* pb_359_6 Plas_6:
 * Ruegeria mobilis strain NBRC102038 contig_13 - Coverage: 47%, E value: 0.0, Identity: 97%
 * Rhodobacteraceae bacterium O3.65 TRIHO_contig000128 - Coverage: 61%, E value: 0.0, Identity: 92%
* pb_359_6 Plas_7:
 * Celeribacter baekdonensis strain DSM 27375 - Coverage: 80%, E value: 0.0, Identity: 98%
 * Roseobacter sp. MED193 1099517003960 - Coverage: 54%, E value: 0.0, Identity: 100%

* pb_359_7 long plasmid
 * Tropicibacter naphthalenivorans scaffold 0009 - Coverage: 13%, E value: 0.0, Identity: 89%
* pb_359_7 middle plasmid
 * Marinovum algicola DG 898 plasmid pMaD4 - Coverage: 6%, E value: 0.0, Identity: 76%
* pb_359_7 short plasmid
 * Roseobacter sp. MED193 1099517003956 - Coverage: 7%, E value: 0.0, Identity: 91%
 * Rhodobacterales bacterium HTCC2654 - Coverage: 9%, E value: 0.0, Identity: 92%

* pb_359_8 plasmid
 * Muricauda lutaonensis strain CC-HSB-11 - Coverage: 3%, E value: 0.0, Identity: 81%


* CAN SEARCH USING 'WHOLE GENOME SHOTGUN CONTIGS' OPTION, but must be specific with which organisms
you search (e.g. Rhodobacteraceae), or else Blast seems to reject the query
 * This allows me to check the plasmids against whole families, rather than having to download and
Blast sequences individually, as was done with R. mucosus R3 vs DSM 17069

* R3 long plasmid finds the same two R. mucosus DSM 17069 contigs as my BlastN
* R3 short plasmid - no great matches
 * Two regions which don't seem to match anything in particular - 10035-19031 and 19655-23967
  * 2-iminobutanoate/2-iminopropanoate deaminase yabJ, D-amino acid dehydrogenase dadA1, 2-iminobutanoate/2-iminopropanoate deaminase yabJ,
    C4-dicarboxylate-binding periplasmic protein dctP, C4-dicarboxylate TRAP transporter large permease protein dctM,
    2,3-diketo-L-gulonate TRAP transporter small permease protein yiaM, HTH-type transcriptional regulator cynR, Abi-like protein, hypo
   * No good matches among Rhodobacteraceae, scattered matches among Alphaproteobacteria, no matches among diatoms (Bacillariophyceae)

  * Hypo, hypo, tRNA(fMet)-specific endonuclease vapC, restriction endonuclease bglII, S-adenosylmethionine-binding protein
   * No matches among Rhodobacteraceae, Alphaproteobacteria or diatoms



## Analyses attempted on R. mucosus strain R3
* PHASTER - phage search
 * Comparing phage regions to R. mucosus type strain (DSM 17069)
* Comparing contigs and plasmids with type strain (BlastN -> Mauve)
* Finding unique regions in each and searching for unique genes/functions (not replicated in other regions of the genome)
* BlastN unique regions of R3 (in particular, second plasmid) to identify an origin
* Compare lists of proteins unique to R3 and DSM




* UvrABC system proteins A, B and C absent from DSM 17069??
 * Problem - genes in DSM 17069 all unnamed...
