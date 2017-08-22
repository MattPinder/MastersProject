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
subunit YajC found on NCBI](http://www.ncbi.nlm.nih.gov/protein/WP_050765224.1).
Judging by where the alignment starts and ends vs. the _K. algicida_ sequence,
the gene predictor MAY have made a mistake in the alignment...  
_Kordia sp._:  
MIAVLYFLIIAPSLKKQKKEKKFMASVKKGDRVITKSGIHGKIVELNDKDFTCVIETGAGKIKFERAALSVEASARLNNPPAKK  
_Kordia algicida_:  
MVVVVYFFILAPSIKRQKKEKNFMASIKKGDRVITKSGIHGKVVELNDKDHTCVIETGAGKIKFERAALSADATLRLNKPPSEKK  

# 16 August 2016

Small victory?  
Took a partial list of proteins labelled 'Hypothetical protein' in
myRAST_export.xls, and ran it through [Batch Web CD-Search Tool](http://www.ncbi.nlm.nih.gov/Structure/bwrpsb/bwrpsb.cgi);
some of those labelled as specific hits included gene names; after comparing a few of these
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
  * [Discovery of _Sphingorhabdus sp. M41_ published just a few months ago](http://www.sciencedirect.com/science/article/pii/S0168165616301961).
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
  * [Found associated with dinoflagellates](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC427730/),
involved in dimethylsulfoniopropionate metabolism ([DMSP metabolism in _S. marinoi_](http://www.sciencedirect.com/science/article/pii/S0022098111005429)).
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
longest contig ([see article](http://www.ncbi.nlm.nih.gov/pubmed/25278561)).

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
    * Longer contig generates longer sequence, adding support to the idea of collapsed repeats (though spike remains)

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
* Judging by [this PacBio poster](http://www.pacb.com/wp-content/uploads/low-input-long-read-for-complete-microbial-genomes-metagenomic-community-analysis.pdf),
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
  * All have bubbles...



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
* FigTree 1.4.3 appears faster than 1.4.2 on my computer for handling huge trees, so
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

  * pb_359_5-8
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
    biopolymers, such as cellulose, chitin, and pectin"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4646686/)

*_3, _5 and _7 only species predicted to have alginate-related pathways (other species seem to
possess some alginate-related genes, however...)
  * All three have components of the alginate degradation pathway
    * _5 has one component (algL alginate lyase)
    * _3 has two components (algE7 alginate lyase and kdgK 2-dehydro-3-deoxygluconokinase)
    * _7 has two components (algE7 alginate lyase and kdgK 2-dehydro-3-deoxygluconokinase)
  * _5 (Marinobacter) contains all components of the alginate biosynthesis II pathway

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
[Genome announcement of Roseovarius mucosus](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4511512/)

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
    From [Genomic and metabolic analysis of fluoranthene degradation pathway in Celeribacter indicus P73T](http://www.nature.com/articles/srep07741)
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
* Compare lists of proteins unique to R3 and DSM 17069

# 25 January 2017

## uvrABC genes
* Blast R3 sequences against DSM 17069
  * Listed as 'excinuclease ABC subunit', rather than uvrABC; still present...

* vapC found on R3 short plasmid is the toxin part of a toxin/antitoxin system
  * Neutralised by vapB, which appears absent...

* Purpose of R3 short plasmid appears to be mercuric resistance, but DSM 17069 also seems to have this capacity...

* Purpose of R3 long plasmid:
  * Phosphate/phosophonate uptake?
  * Cobalt-zinc-cadmium resistance?
    * At least one copper resistance gene, too
  * Type IV secretion system?
  * A lot of mitochondria-related genes
    * Many pertaining to cytochrome C (inner mitochondrial membrane)
    * Cardiolipin synthase A (inner mitochondrial membrane)
      * Mitochondria hypothesised to derive from alphaproteobacteria, so perhaps unsurprising...
  * entS enterobactin exporter (strongest known siderophore)
    * But, no enterobactin itself, plus entS also on chromosome...

  * "... there is experimental evidence that cytochrome biosynthesis genes are involved in
   copper resistance in Pseudomonas fluorescens"
   (Yang H, Liu MY, Romeo T: Coordinate genetic regulation of glycogen catabolism and biosynthesis in Escherichia colivia the CsrA gene product.
   J Bacteriol. 1996, 178 (4): 1012-1017.)

| Plasmid           | Possible function    |
|-------------------|----------------------|
| pb_359_2 - Plas 1 | See above (R3 long)  |
| pb_359_2 - Plas 2 | See above (R3 short) |
| pb_359_3 - Plas 1 | ?                    |
| pb_359_3 - Plas 2 | Mercury resistance?  |

* Loktanella short plasmid seems to contain largely the same genes as R3 short plasmid...
  * Blastn reveals that the two plasmids are almost identical...

| pb_359_5 plasmid  | Mercury resistance? Copper resistance? Type IV secretion? |
| pb_359_6 - Plas 1 | [Long; check again] |
| pb_359_6 - Plas 2 | [Long; check again] |
| pb_359_6 - Plas 3 | [Long; check again] |
| pb_359_6 - Plas 4 | Alkane degradation (alk genes)? Carbon monoxide dehydrogenase (cox genes)? |
| pb_359_6 - Plas 5 | Phosphonate metabolism (phn genes)? |
| pb_359_6 - Plas 6 | Amino acid transport (liv genes + braC)? Type IV secretion? |
| pb_359_6 - Plas 7 | ? |

* Sulfitobacter plasmids have genes for fructoselysine and psicoselysine degradation; carbon source?

* Blast all plasmids against one another?

| pb_359_7 - Plas 1 | [Long; check again] |
| pb_359_7 - Plas 2 | ? |
| pb_359_7 - Plas 3 | ? |

* Antarctobacter plasmids have genes for phosphatidylcholine biosynthesis; interaction with S. marinoi?
* Antarctobacter seems to have many copies of leukotoxin gene over chromosome and plasmids

| pb_359_8 plasmid  | Transposition (tra genes)? Many hypothetical proteins... |

* Blastn all-vs-all; get .xml output for all hits with E value >9,000
  * Roseovarius plasmid 1 vs Sulfitobacter plasmid 7 (18,619)
  * Roseovarius plasmid 2 vs Loktanella plasmid 2 (26,797)
  * Loktanella plasmid 1 vs Loktanella chromosome (11,625)
  * Sulfitobacter chromosome vs Sulfitobacter plasmid 2 (11,326)
  * Sulfitobacter plasmid 5 vs Sulfitobacter plasmid 7 (9,310)

* Copy across fasta sequences and run Blasts with .xml output

# 26 January 2017

## Blastn .xml

* Roseovarius plasmid 2 vs Loktanella plasmid 2 is the only one which shows such dramatic similarity

## Other samples
* pb_359_3 - compare to Loktanella vestfoldensis
* pb_359_4 - wait
* pb_359_5 - compare to Marinobacter algicola
* pb_359_6 - compare to Sulfitobacter pseudonitzschiae
* pb_359_7 - wait
* pb_359_8 - compare to Arenibacter algicola

## Workflow
* Compare phage regions to related species
* Check synteny with most closely related species (type species if a strain?)
* Compare plasmids
* Identify unique regions to try and identify unique functions?

## pb_359_3 vs L. vestfoldensis DSM 16212(T)

* DSM 16212 assembly contains 45 contigs... Most have matches to pb_359_3
  * The matches are generally in the mid-80% similarity range...
  * Contigs with no match:
    * NZ_KB908004 - hypothetical and CRISPR-related genes
    * NZ_KB908005 - primarily hypothetical proteins
    * NZ_KB908007 - various genes
    * NZ_KB908008 - [check GenBank]
    * NZ_KB908011 - [check GenBank]
    * NZ_KB908012 - [check GenBank]
    * NZ_KB908014 - [check GenBank]
    * NZ_KB908017 - [check GenBank]

* Running DSM 16212 through Pathway Tools

* Check 'intact' phage regions of pb_359_3 against L. vestfoldensis DSM 16212
  * Region 3 matches NZ_KB907974.1 Loktanella vestfoldensis DSM 16212 genomic scaffold H147DRAFT_scaffold00002.2 (mid-80% match)
  * Region 6 has 4 matches of <2,000bp

## pb_359_5 vs M. algicola DG893(T)

* DG893 assembly contains >100 contigs
  * Two short hits on plasmid; many long hits to chromosome
  * Chromosome hits have 89%-98% identity to pb_359_5

## pb_359_6 vs S. pseudonitzschiae H3(T)

* H3 assembly contains 80 contigs
  * Many long hits to the chromosome
  * Hits to plasmids rather fragmented

## pb_359_8 vs A. algicola TG409(T)

* TG409 has only 3 contigs; easier to make comparisons
* All 3 contigs seem to map to pb_359_8's chromosome
* A few short (1,936, 212, 63) matches to two of the TG409 contigs on the plasmid; 1,936 region identical in both matches
  * Check 8,328 - 10,243 on pb_359_8 plasmid
    * Putative transposase and tyrosine recombinase XerD

# 27 January 2017

## pb_359_8 vs A. algicola TG409(T)
* Double-checking matching regions
  * Contig 1: ~1,850,000 - ~4,335,519 on Chromosome
  * Contig 2: ~5,300,000 (9.1 Kb match) on Chromosome
  * Contig 3: ~4,372,000 - ~1,857,451 on Chromosome
* Arenibacter contigs match very well to the pb_359_8 chromosome (>95% identity)

# 30 January 2017

## 16S check
* pb_359_2 - 1472bp according to previous analyses
  * Check GenBank: 1456bp and 1456bp
  * complement(1417291..1418746) and complement(1684905..1686360)
  * Cut these from the GenBank file and reBlast them
* pb_359_3 - 1468bp according to previous analyses
  * Check GenBank:  1451bp and 1451bp
  * complement(2602128..2603578) and complement(3237731..3239181)
  * Cut from fasta, ready to reBlast
* pb_359_4 - 1497bp according to previous analyses
  * Check GenBank: 1477bp and 1477bp
  * complement(1530498..1531974) and complement(1540929..1542405)
  * Cut from fasta, ready to reBlast
* pb_359_5 - 1547bp according to previous analyses
  * Check GenBank: 1528bp, 1528bp and 1528bp
  * complement(2845442..2846969), complement(3612280..3613807) and complement(3824765..3826292)
  * Cut from fasta, ready to reBlast
* pb_359_6 - 1467bp according to previous analyses
  * Check GenBank: 1450bp and 1450bp
  * complement(2846175..2847624) and complement(160074..161523) (third contig)
  * Cut from fasta, ready to reBlast
* pb_359_7 - 1458bp according to previous analyses
  * Check GenBank: 1441bp and 1441bp
  * 1369387..1370827 and 2482487..2483927
  * Cut from fasta, ready to reBlast
* pb_359_8 - 1531bp according to previous analyses
  * Check GenBank: 1512bp, 1512bp and 1512bp
  * complement(552372..553883), complement(5511478..5512989) and complement(5716748..5718259)
  * Cut from fasta, ready to reBlast

* Ensure that 16S paragraph contains BLASTn reference, database used, and the acc. no., query cover and identity of the best hit
  * Edited announcement paper paragraphs to relate specifically to the 16S sequences predicted using RNAmmer 1.2

# 31 January 2017

## pb_359_3 - Loktanella vestfoldensis [strain name]
Find genes which are suggestive of symbiosis/parasitism
* Export and compare type strain pathways

* 2x Rhamnan synthesis protein F genes found in pb_359_3 but not in type strain
  * https://www.ebi.ac.uk/interpro/entry/IPR007739
  * Pathogenic factor??
  * Rhamnose produced by diatoms!

* Tungstate uptake and usage
  * tupABC operon
  * Seemingly absent in the type strain?

* uvrABC only annotated in pb_359_3 - are they present in type strain?
  * Again, labelled as excinuclease ABC subunit... Still present




* Check paper:
  * http://bmcevolbiol.biomedcentral.com/articles/10.1186/1471-2148-8-30


* Compare pb_359_4 to genome of Sphingorhabdus sp. M41?

# 1 February 2017

GitLab acting up; push from laptop to Albiorix when able

## pb_359_4
* No phosphatidylcholine synthase?
  * Phosphatidylcholine biosynthesis V pathway - check
  * One required gene present, one missing
* No acyl-homoserine-lactone synthase? (no autoinducer synthesis/quorum sensing?)
  * AI-2 transporter genes present...
* Presence of cob(II)yrinate a,c-diamide biosynthesis II (vitamin B12 synthesis)

* Trehalose utilisation - relevant?
* Little evidence of type IV secretion system

## pb_359_5
* Two adenosylcobalamin salvage pathways? - check
* cob(II)yrinate a,c-diamide biosynthesis II pathway - check
  * Cobalamin biosynthesis protein CobD
* No phosphatidylcholine synthase?
* No autoinducer?
  * AI-2 transporter genes present...
  * Autoinducer 2 sensor kinase/phosphatase LuxQ genes present
* Abundance of mercuric resistance proteins
* Putative siderophore-related proteins
* Tungstate uptake and usage
  * TupABC operon
  * One tungstate-related protein in type strain

## pb_359_6
* Three adenosylcobalamin salvage pathways? - check
* autoinducer AI-1 biosynthesis AND autoinducer AI-2 degradation
* cob(II)yrinate a,c-diamide biosynthesis II
* 2x cobalamin biosynthesis protein
* 3x Invasion associated locus B (IalB) protein
* 2x leukotoxin genes
* Luminescence regulatory protein LuxO?
  * From UniProt - "LuxO and sigma-54 have also a role in activating the production of siderophore and in regulating the rugose colony morphology phenotype."
* Presence of phosphatidylcholine synthase
* Putative siderophore-related proteins
* Multiple copies of the TupABC tungstate operon
  * Seemingly absent from type strain

## pb_359_7
* Two adenosylcobalamin salvage pathways? - check
* cob(II)yrinate a,c-diamide biosynthesis II
* phosphatidylcholine biosynthesis VI
  * Presence of phosphatidylcholine synthase
* 2x cobalamin biosynthesis protein
* 2x Invasion associated locus B (IalB) protein
* Abundance of leukotoxin genes
  * Also leukotoxin-activating lysine-acyltransferase LtxC
* Contains only TupA of tungstate use operon

# pb_359_8
* 1x adenosylcobalamin salvage pathway - check
* Autoinducer AI-2 degradation
* phosphatidylcholine biosynthesis V
  * No phosphatidylcholine synthase?
* 'pheromone autoinducer 2 transporter'


## Other
* Check presence/absence of flagellar proteins - pb_359_5 has many, but did pb_359_4?
  * Compare reports of motility

* Read up and check genes for all types of secretion system, not just Type IV

* Imelysin?

* Presence/absence of 'precorrin' genes (involved in vit B12 synthesis?)

* (pb_359_2 also contains tungstate operon tupABC)

| Sample   | Comparable species                | Comparable species motile?                       | Flagellar genes?                        |
|----------|-----------------------------------|--------------------------------------------------|-----------------------------------------|
| pb_359_2 | R. mucosus (type strain)          | Motility rarely observed                         | Many flagella-related genes in pb_359_2 |
| pb_359_3 | L. vestfoldensis (type strain)    | Motility not observed (genus)                    | Many flagella-related genes in pb_359_3 |
| pb_359_4 | Sphingorhabdus (genus)            | Motile or non-motile                             | Few flagella-related genes in pb_359_4  |
| pb_359_5 | M. algicola (type strain)         | Motile ('single, non-sheathed, polar flagellum') | Many flagella-related genes in pb_359_5 |
| pb_359_6 | S. pseudonitzschiae (type strain) | Non-motile                                       | Few flagella-related genes in pb_359_6  |
| pb_359_7 | Antarctobacter (genus)            | 'Daughter cells may be motile'                   | Many flagella-related genes in pb_359_7 |
| pb_359_8 | A. algicola (type strain)         | Non-motile                                       | Two flagella-related genes in pb_359_8  |

  * Conflicts with Flagella observations by Oskar?

* Tungstate-using samples
  * pb_359_2
  * pb_359_3
  * pb_359_5
  * pb_359_6
  * (Only tupA in pb_359_7)
  * Rhodobacteraceae and Alteromonadaceae

# 2 February 2017

## Marinobacter algicola vs pb_359_5
* (Note: M. algicola lives in association with a dinoflagellate)
* M. algicola has adenosylcobalamin biosynthesis from cobyrinate a,c-diamide I and II pathways; pb_359_5 doesn't
* pb_359_5 has biotin biosynthesis pathways, M. algicola doesn't
* Siderophore-related genes in M. algicola; putative siderophore-related genes in pb_359_5
* pb_359_5 has a gene for 'strictosidine synthase' - interesting?

## Sulfitobacter pseudonitzschiae vs pb_359_6
* Many more multidrug resistance genes in pb_359_6 than in type strain
* Both have phosphatidylcholine synthase gene

## Arenibacter algicola vs pb_359_8
* pb_359_8 lacking chloramphenicol acetyltransferase
* pb_359_8 contains additional transposon proteins?
* A. algicola has a syringomycin biosynthesis enzyme that pb_359_8 seems to lack
  * Present in plant pathogens...



* Compare presence/absence of the following between pb_359_X and type strains, and among each other
  * transposon- and phage-related genes
  * resistance genes (drugs/metals)
  * General metal-related genes
    * Tungsten/tungstate, copper, mercury, etc.
  * Presence of tungstate genes vs # of molybdenum-associated genes?
  * -ycin genes (antibiotics, either resistance or production)


## pb_359_8 vs A. algicola - contigs
* pb_359_8 has two contigs; A. algicola type strain has three
* Two longest A. algicola contigs map together to cover the entire pb_359_8 chromosome
* Few short regions match the pb_359_8 plasmid... Largely unique

## pb_359_6 vs S. pseudonitzschiae - contigs
* Sixth Falcon contig (plasmid 5) of pb_359_6 has only a few hits to S. pseudonitzschiae
* Fourth Falcon contig (plasmid 3) of pb_359_6 only appears to match S. pseudonitzschiae in patches
* Around half of Third Falcon contig (plasmid 2) of pb_359_6 matches contig11 of S. pseudonitzschiae




## Leukotoxins
* pb_359_2 and _7 have an abundance of leukotoxin genes
  * pb_359_2 - 15
  * pb_359_3 - 1, plus Leukotoxin export ATP-binding protein LtxB
  * pb_359_4 - none
  * pb_359_5 - none
  * pb_359_6 - 2
  * pb_359_7 - 15, plus Leukotoxin-activating lysine-acyltransferase LtxC

* Leukotoxins only appear to affect white-blood cells... similar sequence...?
* Check pb_359_2:
  * BlastP of the first leukotoxin gene in pb_359_2 gave an excellent hit to a 5'-nucleotidase in R. sp. TM1035 (~99% identity)
  * Second: among others, matches Ca2+-binding protein, RTX toxin-related [Roseovarius azorensis] (best match to a hypo. from TM1035)
  * Third: aggregation factor core protein MAFp3 [Roseovarius sp. TM1035]
  * Fourth: type I secretion protein [Roseovarius sp. TM1035]  (also similar to RTX toxin [Roseovarius mucosus DSM 17069])
  * Fifth: Large exoprotein [Roseovarius sp. TM1035]
  * Sixth: rhizobiocin/RTX toxin [Roseovarius sp. TM1035]
  * Seventh: type I secretion protein [Roseovarius sp. TM1035] (some similarity to Hemolysin-type calcium-binding repeat (2 copies) [Roseovarius mucosus DSM 17069])
  * Eighth: rhizobiocin/RTX toxin [Roseovarius sp. TM1035]
  * Ninth: Hemolysin-type calcium-binding region [Roseovarius sp. TM1035]
  * Tenth: No great matches, but second hit is Ca2+-binding protein, RTX toxin-related [Rhizobium loessense]
  * Eleventh: Haem peroxidase?
  * Twelfth: Ca2+-binding protein, RTX toxin-related [Rhizobium loessense] ? (only accounts for the second-half of the protein; first half had no good hits)
  * Thirteenth: Nidogen, extracellular region [Roseovarius sp. TM1035]
  * Fourteenth: Hemolysin-type calcium-binding protein [Roseovarius sp. TM1035]
  * Fifteenth: Hemolysin-type calcium-binding region, RTX [Roseovarius sp. TM1035]

* Check pb_359_7:
  * TO DO ON FRIDAY

# 3 February 2017

## pb_359_7

* Check identity of pb_359_7 'leukotoxins' using BlastP
  * 'Leukotoxin-activating lysine-acyltransferase LtxC': toxin/cytolysin-activating lysine-acyltransferase (only ~80% cover and ~40% identity)
  * First: Hemolysin-type calcium-binding repeat-containing protein [Mameliella alba] (better hits are to 'hypothetical proteins')
  * Second: Hemolysin-type calcium-binding repeat-containing protein [Yangia pacifica] (better hits to type I secretion target repeat protein and hypo. proteins)
  * Third: putative Ca2+-binding protein [Rhodobacteraceae bacterium HLUCCO07] (better hits to type I secretion target repeat protein and hypo. proteins)
  * Fourth: 5'-nucleotidase [Mameliella alba]
  * Fifth: Hemolysin-type calcium-binding repeat-containing protein [Mameliella alba]
  * Sixth: Hemolysin-type calcium-binding repeat-containing protein [Mameliella alba] 
  * Seventh: Hemolysin-type calcium-binding repeat-containing protein [Mameliella alba] (many better hits to hypothetical proteins)
  * Eighth: Hemolysin-type calcium-binding repeat-containing protein [Mameliella alba] (many better hits to hypothetical proteins)
  * Ninth: 5'-nucleotidase [Mameliella alba] (several better hit to hypothetical proteins)
  * Tenth: Hemolysin-type calcium-binding repeat-containing protein [Mameliella alba] (many better hits to hypothetical proteins)
  * Eleventh: Hemolysin-type calcium-binding repeat-containing protein [Mameliella alba]
  * Twelfth: Hemolysin-type calcium-binding repeat-containing protein [Mameliella alba]
  * Thirteenth: Hemolysin-type calcium-binding repeat-containing protein [Mameliella alba] (many better hits to hypothetical proteins)
  * Fourteenth: Hemolysin-type calcium-binding repeat-containing protein [Mameliella alba] (many better hits to hypothetical proteins)
  * Fifteenth: 5'-nucleotidase [Mameliella alba]

## Leukotoxin/hemolysin
* Hemolysin forms transmembrane pores in red blood cells and mammalian cells
* Leukotoxin disturbs the lysosomal membrane so the contents enter the cytosol, causing cell death

* Algicidal compound of DHQ25
  * "... cells of xenic A. tamarense treated  with  culture  filtrate  of  DHQ25 exhibited rounding  and  loss  of  cell  wall  integrity. 
Cells were disrupted, and cellular substances were  decomposed  and  released  with  increased  exposure time."
  * http://onlinelibrary.wiley.com/doi/10.1111/j.1472-765X.2010.02936.x/pdf

* Algicidal compound of Brevibacterium sp. BS01
  * "Morphological analysis revealed structural alterations in A. tamarense with algal cells losing the integrity of their organelles"
  * https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4633486/

* Prediction - pb_359_2 and _7 may be algicidal
  * pb_359_7 has no autoinducer predicted in Pathway Tools...

* Pairwise alignment between similar regions? e.g. pb_359_2 plasmids vs type strain
  * pb_359_2 vs scaffold14; high 90s similarity, but hard to know best way to compare the two and get measurable comparison...

## Things to do for thesis

* Gather papers regarding other bacteria-diatom interactions
* Double-check whether Consensus, consensus_names or a combination should be used
* Include results of preliminary BLASTs
* Condense 'primary' and 'secondary' annotations down into one; 'primary' can probably be ignored as family is discernable from preliminary BLAST?
* How reliable a source is SILVA for 16S data; no information on whether or not the sequences are complete...
* BLASTn/Blast Viewer, or Mauve? - visualise for closeness to related strains
* Rerun trees including an outgroup (e.g. from different order)
* Take printscreens of coverage graphs from SMRT Viewer to show coverage? (or are these too numerous/unnecessary...?)
* Take some printscreens from Pathway Tools, showing relevant/interesting pathways
* Tabulate 16S search results

* Check state of S. marinoi annotation

* Check bacterial-diatom adhesion systems
  * BUT bacteria don't have to adhere to be within the phycosphere - biofilms?
* Any more information on use of tungsten by bacteria?

# 6 February 2017

## Select outgroups for phylogenetic analysis - choose an adjacent class/order
* Rhodobacteraceae - use X
* Sphingomonadaceae - use Erythromonadaceae + one from further out
* Alteromonadaceae - use X
* Flavobacteriaceae - use X

* Trees will be too big using full order trees; have to take a subsample; take outgroup from adjacent branch of the tree

* Syntax: $ ./phylophlan.py -i my_genomes_to_insert --nproc 16
  * .faa input

* pb_359_2:
  * All Roseovarius and Roseobacter sequences, plus Thalassobius as outgroup
    * Roseovarius mucosus downloaded manually; no 'latest assembly version' found...
    * Roseovarius sp. BRH_c41 downloaded manually; no 'latest assembly version' found...

* pb_359_3:
  * All Loktanella, plus Donghicola, Oceanicola, Wenxinia, Rubellimicrobium and Ketogulonicigenium, plus Octadecabacter as outgroup
    * Download Roseobacter sp. CCS2 manually; rest of Roseobacter in different group...

* pb_359_4:
  * All Sphingorhabdus, Sphingopyxis and Blastomonas, plus Sandarakinorhabdus as outgroup

* pb_359_5:
  * Subset of Marinobacter, plus Agarivorans as outgroup
    * M. subterrani, sp. YWL01, manganoxydans, sp. CP1, sp. EhC06, sp. EhN04, adhaerens, sp. Hb8, similis, lipolyticus, sp. HL-58, algicola, sp. MCTG268 and salarius

* pb_359_6:
  * All Sulfitobacter, Roseobacter (except CCS2, SK209-2-6 and MED193), Tateyamaria and Oceanibulbus, plus Nautella as outgroup

* pb_359_7:
  * All Antarctobacter (if any exist), Tropicibacter naphthalenivorans, Sagittula stellata, Rhodobacteraceae bacterium PD-2, Mameliella alba, Ponticoccus sp. SJ5A-1,
    and Ruegeria sp. PBVC088, with Citreicella as outgroup

* pb_359_8:
  * All Arenibacter, Cellulophaga, Sediminicola, Maribacter and Zobellia, plus Muricauda as outgroup

* All jobs running at 8 cores each
  * Taking much longer than I had remembered...
  * Because the -u flag was supposed to be used, not the -i flag...

## pb_359_2
* From https://www.ncbi.nlm.nih.gov/bioproject/19363:
  * "Roseovarius sp. TM1035. This strain was isolated from the dinoflagellate Pfiesteria piscicida and actively metabolizes the dinoflagellate secondary product
    dimethylsulfoniopropionate (DMSP)."
* Miller & Belas - "Dimethylsulfoniopropionate Metabolism by Pfiesteria-Associated Roseobacter spp."
  * https://www.ncbi.nlm.nih.gov/pmc/articles/PMC427730/
* All but final step apparently present in pb_359_2
* Roseovarius mucosus has all genes for dmdABCD genes in an operon...?
  * Checked vs Ruegeria dmdD (TblastN), but the only hit isn't very convincing...

* Toxins present in DSM 17069 - 6 RTX toxins

## Trees
* May be approaching this from the wrong angle...
* Take a representative species or two from a variety of genera, and tree those?
* Also rename file to be only 'pb_359_X'
* Remove 'sp.' species
* Choose an outgroup from further away in the tree
  * pb_359_2 - try Hyphomonas? Still in order Rhodobacterales, but not in family Rhodobacteraceae
    * Roseobacter denitrificans still appears outside of the expected area...

* Check re: best way to generate good trees...
  * Currently re-downloading Rhodobacteraceae fastas; still need an outgroup, something from outside Rhodobacteraceae?

# 7 February 2017

## Pathways
* Make list of relevant pathways and interesting genes
* Interesting results
  * Toxins - Roseovarius and Antarctobacter have 15 'leukotoxin' genes each
  * Mercury resistance - Marinobacter has 13 genes potentially related to mercuric resistance
  * Cadmium resistance - Arenibacter has 12 genes potentially related to cadmium resistance
  * Drug resistance - Sphingorhabdus has 14 genes related to glyoxalase/bleomycin resistance, and 13 related to multidrug resistance
  * Phosphatidylcholine biosynthesis - Marinobacter doesn't seem to have any phosphatidylcholine biosynthesis pathways
    * M. shengliensis and M. hydrocarbonoclasticus (and others?) seem to produce phosphatidylcholine...



Interesting - "Although cadmium has no known biological function in higher organisms,
a cadmium-dependent carbonic anhydrase has been found in marine diatoms."  
(From Wikipedia)
* Relationship between diatoms, bacteria and heavy metals?


* pb_359_4 and _8 contain one or two of the genes required for prodigiosin biosynthesis
* pb_359_6 contains a rhamnolipid biosynthesis gene

* See also:
  * http://www.sciencedirect.com/science/article/pii/S073497501530029X
  * Algicidal microorganisms and secreted algicides: New tools to induce microalgal cell disruption


## Trees
* pb_359_2 - Take representatives from:
  * Roseovarius, Pseudooceanicola, Roseivivax, Jannaschia, Thalassobius,
    Oceanibulbus, Sulfitobacter, Ruegeria, Leisingera, Loktanella, Paracoccus,
    Rhodobacter


## To do
* Check for degradation of the following polysaccharides:
  * Agar, alginate, chitin, cellulose, fucoidan, laminarin, pectin, pullulan, starch, xylan

* Check pb_359_2 job compared to other attempted trees

# 8 February 2017

## pb_359_6
* Re: Sulfitobacter and diatoms:
  * http://onlinelibrary.wiley.com/doi/10.1111/j.1438-8677.2008.00040.x/abstract;jsessionid=70C450C00E3E37C96D94608D17D6991E.f03t03

## Trees
* pb_359_2 tree always seems to split into three...
* Arenibacter algicola may also be a poor choice to include, as it always extends further than the other branches...
* Include two other species from a non-Rhodobacteraceae Rhodobacterales genus?
  * Try Hyphomonas? Otherwise try non-Rhodobacterales alphaproteobacterium
  * Reason for issues with previous iterations - no rooting; attempt midpoint rooting
* 8_Feb_PM_2_pb_359_2.tree.nwk appears to be a good basis for the pb_359_2 tree; include pb_359_3, _6 and _7 to form a single Rhodobacteraceae tree
  * Outgroup - Hyphomonas (within Hyphomonadaceae, sister family to Rhodobacteraceae within order Rhodobacterales)


* For pb_359_4, include in tree of Sphingomonadaceae; outgroup - member of Erythromonadaceae? Sister family within order Sphingomonadales
  * Outgroup - Erythrobacter
  * Considering the lack of represented genera in this family, would it be better to include Erythromonadaceae in the tree and have an outgroup from another class?

* For pb_359_5, include in tree of Alteromonadaceae; outgroup - member of XXX? Sister family within order Alteromonadales
  * Outgroup - 

* For pb_359_8, include in tree of Flavobacteriaceae; outgroup - member of XXX? Sister family within order Flavobacteriales
  * Outgroup - 


* Rhodo_Tree has been trimmed; if a monophyletic group is made up entirely of a single genus, then the group is reduced to a single representative species


## To do
* Check new Rhodo tree

* Consider changing the pb_359_4 tree to include Erythro genera and use another class as outgroup
  * Kordia? From order Kordiimonadales, class Alphaproteobacteria
    * [THIS IS INCORRECT!]
  * Check new pb_359_4 tree (Kordia outgroup)

* Decide on outgroups for pb_359_5 (Altero) and pb_359_8 (Flavo) trees

# 9 February 2017

## Trees
Checking new Rhodo and pb_359_4 trees:
* Rhodo - Seems to have worked, but need to trim out some branches - 94 tips down to at least 50?
* pb_359_4 - Also seems okay, but need to trim out the excess branches - 99 tips down to at least 50 again?

* For pb_359_5 - include order Alteromonadales? Few represented genera in Alteromonadaceae alone
  * Running with Kordia as an outgroup [CHANGE OUTGROUP!]

* Kordia is not an Alphaproteobacteria... Choose an alternative outgroup for the above...
  * For pb_359_4 - Brucella? (Rhizobiales)
  * For pb_359_5 - Escherichia? (Enterobacterales)
  * For pb_359_8 - Bacteroides? (Bacteroidales)

* Tree statuses:
  * Rhodo - outgroup decided (Hyphomonas, sister family), need to remove branches to resize tree
  * pb_359_4 - outgroup decided (Brucella, sister order), other branches need to be reduced to resize tree
  * pb_359_5 - outgroup needs to be added (old one must be removed), other branched need to be reduced to resize tree
  * pb_359_8 - outgroup decided (Bacteroides, sister class), check results and remove excess branches
    * May need to change outgroup to something within Flavobacteriales, outside Flavobacteriaceae
    * New outgroup - two members of Crocinitomicaceae; sister family under Flavobacteriales

* Rhodo provisionally done - 50 species

## To do
* Commit latest pb_359_8 tree
* View pb_359_4, _5 and _8 trees and continue to remove branches to reach a suitable size for the report

# 10 February 2017

## Scripts
* Script folders tidied up
* NCBI Downloader scripts combined into one; user now specifies desired file extension
* GenBank_Consensus and GenBank_Consensus_Names not combined; will need to work out how to combine functionality

## Trees
Provisional final trees for all 4 groups; now need to generate complete trees for supplementary material



## To do
* Currently running PhyloPhlAn for full trees; add these to GitHub and include a descriptive readme
  * Include date of retrieval of sequences, and which sequences were left out (_sp._)
  * Mention that Roseovarius mucosus has been 'suppressed'

# 13 February 2017

## Trees
'Final' trees moved to repository; readme mentions relevant information

* pb_359_5 is shown on its own branch next to Marinobacter algicola and M. salarius
  * Is it definitely most closely related to M. algicola?

## Preliminary Blasts

Preliminary blastx not done for all final assemblies - rerun





## To do
* Run other blastx analyses?
* Save full tree


# 14 February 2017

## Trees
Full tree may not save after problems last night... Restarted
* Full tree complete and uploaded

## Preliminary Blasts
Rerun pb_359_4 Blast from yesterday (failed)

## Pathway Tools
Test capacity for a multi-species pathway file

* Number of pathways

| Sample   | Consensus | Consensus_Names |
|----------|-----------|-----------------|
| pb_359_2 | **284**   | 283             |
| pb_359_3 | 300       | **303**         |
| pb_359_4 | **237**   | 235             |
| pb_359_5 | 261       | 261             |
| pb_359_6 | 302       | **307**         |
| pb_359_7 | 290       | **297**         |
| pb_359_8 | 256       | **257**         |

## 16S

Is it viable to check other databases and accept matches to regions of a genome not explicitly listed as '16S'?
* 08_16S/CHECKME.md


## To do

Still waiting for pb_359_4 Blast on node0


# 15 February 2017

## Pathway Tools

'Error: Duplicate genetic element ID NIL' shows up even when only trying to combine two species...
* Unsure if the program will work as intended

Manual annotation refinement using pathway hole filler in Pathway Tools?

## Report

* Ensure that citations are correct and consistent
* Is doi or full link the best option?

* Can't access SMRT Portal?

# 16 February 2016

## BLAST
BLAST still acting up; already have 16S and phylogeny for determining taxonomy,
BLAST seems imprecise and surplus... Perhaps mention earlier BLAST results
when relevant

## Ros. P2 vs Lok. P2
Reinvestigate these two plasmids' similarity
* All of Roseovarius plasmid is accounted for in these areas - 100% identity
* Areas in Loktanella not covered by Roseovarius:
  * 1 - 2,106
    * Part of Tn3 transposase DDE domain protein
  * 16,616 - 18,152
    * Hypothetical protein and transposase
  * 27,780 - 31,556
    * Tn3 transposase DDE domain protein, DNA-invertase hin, and end of conjugal transfer protein TraG
  * 37,730 - 39,380
    * Mercuric reductase (merA) and hypothetical protein
* BLASTn-ing the unique areas - two don't match anything (BLASTn), two match other Rhodobacteraceae sequences
* BLASTx-ing the unique areas reveals that all of them match transposases

* Do the unique regions exist on the Roseovarius chromosome/large plasmid?
  * No BLASTn hits at all
* Are the unique regions present on other Loktanella replicons?
  * Common to either one or both other replicons

## Trees
pb_359_Rhodo subsampled tree is much too wide - any way to thin it down to fit on a page?
* Try removing Stappia indica

pb_359_5 subsampled tree looks a little untidy on account of Marinobacterium litorale
* Try removing it
* Still long; remove Ferrimonas and Shewanella?


## Gene transfer
BLAST all pb_359 samples vs Skeletonema to check for gene transfer
* s*********a b******a
* Question: How to tell if a hit truly IS a result of HGT?
* Check article:
  * http://onlinelibrary.wiley.com/doi/10.1111/1462-2920.12854/full


## To do
* Check pb_359_5 tree with trims made


# 17 February 2017

## Tree
Settings for exporting trees from FigTree:
* Expansion ~half way
* Align tip labels
* Highlight pb_359 in blue
* Appearance - line weight 2
* Tip labels - 18 Arial Bold
* Tip shapes - 6 circles
* Node labels - label, 12 Arial Bold
* Scale bar - 14, line weight 2

## Genome sizes

Double-check genome/chromosome sizes vs genus:

* pb_359_2 (Roseovarius) - 4,381,426 / 4,170,996
  * Range - 3.67 Mb - 6.06 Mb
  * Acceptable genome size
  * R. mucosus genome size - 4.24 Mb
* pb_359_3 (Loktanella) - 3,987,360 / 3,836,950
  * Range - 3.18 Mb - 4.20 Mb
  * Acceptable genome size
  * L. vestfoldensis genome size - 3.72 Mb
* pb_359_4 (Sphingorhabdus) - 3,479,724 / 3,479,724
  * Range - 3.33 Mb - 3.54 Mb
  * Acceptable genome size
* pb_359_5 (Marinobacter) - 4,630,160 / 4,386,892
  * Range - 3.15 Mb - 5.35 Mb
  * Acceptable genome size
  * M. algicola genome size - 4.41 Mb
  * M. salarius genome size - 4.61 Mb
* pb_359_6 (Sulfitobacter) - 5,121,602 / 3,572,445
  * Range - 3.45 Mb - 4.94 Mb
  * Chromosome - acceptable chromosome size
  * S. pseudonitzschiae genome size - 4.94 Mb
* pb_359_7 (Antarctobacter) - 5,331,190 / 4,723,013
  * No information available
* pb_359_8 (Arenibacter) - 5,857,781 / 5,793,053
  * Range - 4.36 Mb - 5.66 Mb
  * Genome a little too big?
  * A. algicola genome size - 5.55 Mb

# 20 February 2017

## Pathway Tools

Checked ambiguous entries in RoseoConsensusBase vs. UniProtKB
* One pathway deleted, three new ones predicted
* Problem when trying to further refine the list - when checking vs UniProtKB, many of the results have an EC number of X.X.X.-,
which is non-specific. Should this be entered into Pathway Tools, or would this be too general?

## Secondary metabolites

Check no. of secondary metabolites per bacterium
* Tools:
  * antiSmash
  * Dark Horse
  * BioCompass (when available)
* FIND WAY TO GET A LIST OF SECONDARY METABOLITES - PATHWAY TOOLS DOESN'T SEEM TO HAVE SUCH A FUNCTION...


## Things to check
* Small plasmids in Roseovarius + Loktanella: Almost the same!

* Marinobacter identity - algicola or salarius??
  * Re: checking the 16S:
    * Closest named species - Marinobacter salarius strain R9SW1 (based on complete genome and partial sequence)
      * Score: 2811 bits (1522) / 2784 bits (1507)
      * Expect: 0.0 / 0.0
      * Identities: 1539/1547 (99%) / 1524/1532 (99%)
      * Gaps: 1/1547 (0%) / 1/1532 (0%)
      * Query cover: 100% / 99% (4,616,532bp / 1531bp vs 1547bp)
      * Note: searching nr/nt database

    * Closest named species - Marinobacter algicola strain DG893 (based on partial sequence)
      * Score: 2731 bits (1479)
      * Expect: 0.0
      * Identities: 1483/1485 (99%)
      * Gaps: 0/1485
      * Query cover: 95% (1485bp vs 1547bp)
      * Note: searching 16S-specific database
      * Note: best full sequence is Marinobacter adhaerens, but 25 differing bases, inc. 4 gaps

  * Re: phylogenetic tree:
    * salarius and algicola share a MRCA; step above that is pb_359_5
    * MRCA with salarius; step above that is algicola (in trimmed tree)

* List of predicted genes/pathways - are these relevant to mention?

* Semester end date - June 2nd

* SMRT Portal not working?

* Sometimes the GenBank with MORE gene names yields LESS pathways; select all of one type, or case-by-case?

* Pathway Tools - EC number inclusion - include X.X.X.- results?





## To do
Lists of secondary metabolites
* Must run antiSmash on a contig-by-contig basis...
  * Remember to check pb_359_3 antiSmash bookmark
  * Check 'symbiotically important' succinoglycan - http://www.sciencedirect.com/science/article/pii/009286749390418P?via%3Dihub
  * Also check pb_359_4 antiSmash bookmark

Identical short plasmids
* Look for signs of phage on the identical short plasmids
* Check VirSorter/PHASTER results
* (Show Mats results from PHASTER on Thursday)

# 21 February 2017

## antiSMASH
Cut GenBank files into per-contig files, then run through antiSMASH (appears to only handle one contig at a time?)
* Seems to be handling everything at once; the contigs just don't contain any secondary metabolite clusters



## To do

Find full-length algicola and salarius 16S sequences from NCBI; compare G+C content AND synteny/gene content in general
* Double-check description papers (if in doubt, go for earliest-described species)
  * Discuss taxonomic considerations in report
* Compare directly to 16S

* Subsample closest ~25 species into tree, not bredth of coverage across order/family

* Always prioritise more pathways in GenBank/Pathway Tools

* Include incomplete EC numbers
  * Make Pathway Tools files available on GitHub

* SMRT Portal now running again

* Report draft in early May

* Test antiSMASH - splice two chromosomes into one GenBank to see if it handles multiple contigs
  * Put antiSMASH results/percentages of genes for secondary metabolites into report
  * List metabolites

## Tree subsampling

* Rhodo; Hyphomonas as outgroup (2 + 11 + 11 + 12 + 11 = 47 total)

  * Hyphomonas x 2

  * pb_359_7
  * Marinovum algicola
  * Marivita hallyeonensis
  * [Roseivivax x 4] - collapse
  * Salipiger mucosus
  * Pelagibaca x 2
  * Thiobacimonas profunda
  * Mameliella alba
  * Sagittula stellata
  * Tropicibacter naphthalenivorans

  * pb_359_2
  * [Pseudooceanicola x 3] - collapse
  * Sediminimonas qiaohouensis
  * Roseovarius x 8

  * pb_359_6
  * Tateyamaria omphalii
  * [Roseobacter x 2] - collapse
  * Oceanibulbus indolifex
  * Sulfitobacter x 8

  * pb_359_3
  * Oceanicola granulosus
  * Loktanella x 6
  * [Rubellimicrobium x 2] - collapse
  * Ketogulonicigenium vulgare
  * [Wenxinia x 2] - collapse

* pb_359_4; Brucella as outgroup (36 total)

  * Brucella x 2

  * pb_359_4
  * Sphingorhabdus marina
  * Sphingopyxis x 6
  * [Croceicoccus x 4] - collapse
  * [Novosphingobium x 15] - collapse
  * Altererythrobacter x 7
  * Porphyrobacter x 6
  * Erythrobacter x 8
  * Citromicrobium bathyomarinum
  * Sphingomonas jaspsi
  * Sphingomonas astaxanthinifaciens

* pb_359_5; Escherichia as outgroup (43 total)

  * Escherichia x 2

  * pb_359_5
  * Marinobacter x 16
  * [Marinobacterium x 5] - collapse
  * [Idiomarina x 9] - collapse
  * Lacimicrobium alkaliphilum
  * Aliiglaciecola lipolytica
  * Paraglaciecola x 6
  * Pseudoalteromonas atlantica
  * Aestuariibacter x 2
  * [Glaciecola x 3] - collapse
  * Salinimonas chungwhensis
  * Alteromonas x 9

* pb_359_8; Crocinitomix and Fluviicola as outgroup (24 total)

  * Crocinitomix catalasitica
  * Fluviicola taffensis

  * pb_359_8
  * Robiginitalea biformata
  * Eudorea adtriatica
  * Pseudozobellia thermophila
  * [Zobellia x 2] - collapse
  * [Maribacter x 6] - collapse
  * Arenibacter x 5
  * [Cellulophaga x 5] - collapse
  * Spongiibacterium flavum
  * Muricauda x 3
  * Croceitalea dokdonensis
  * Joostella marina
  * Galbibacter marinus
  * Sinomicrobium oceani
  * Zhouia amlolytica
  * Imtechella halotolerans

## 16S
Rechecking pb_359_5 16S:
* Check against all three databases and save best hits
  * nr/nt - 2x M. salarius
  * refseq_genomic - M. algicola
  * bacteria/archaea 16S - M. algicola partial + M. adhaerens complete

* Align hits and find the best match (individual PSAs would be better than MSAs...)

* pb_359_5 - 3 x 16S sequences
  * 1 + 2 = identical (column 1)
  * 3 = 1bp difference (column 2)

* nr/nt salarius 1 (rev com):
  * Length: 1532 (pb_359_5 = 1528; M. salarius = 1531)
  * Identity:    1519/1532 (99.2%)	1520/1532 (99.2%)
  * Similarity:  1519/1532 (99.2%)	1520/1532 (99.2%)
  * Gaps:           5/1532 ( 0.3%)	5/1532 ( 0.3%)
  * Score: 	7553.0			7562.0

* nr/nt salarius 2:
  * Length: 1528 (pb_359_5 = 1528; M. salarius = 1527)
  * Identity:    1519/1528 (99.4%)	1520/1528 (99.5%)
  * Similarity:  1519/1528 (99.4%)	1520/1528 (99.5%)
  * Gaps:           1/1528 ( 0.1%)	1/1528 ( 0.1%)
  * Score:	7553.0			7562.0

* refseq_genomic algicola:
  * Length: 1528 (pb_359_5 and M. algicola = same length)
  * Identity:    1525/1528 (99.8%)	1526/1528 (99.9%)
  * Similarity:  1525/1528 (99.8%)	1526/1528 (99.9%)
  * Gaps:           0/1528 ( 0.0%)	0/1528 ( 0.0%)
  * Score: 	7613.0			7622.0

* 16S algicola partial (rev com):
  * Length: 1528 (pb_359_5 = 1528; M. algicola = 1485)
  * Identity:    1482/1528 (97.0%)	1483/1528 (97.1%)
  * Similarity:  1482/1528 (97.0%)	1483/1528 (97.1%)
  * Gaps:          43/1528 ( 2.8%)	43/1528 ( 2.8%)
  * Score: 	7398.0			7407.0

(* If pb_359_5 trimmed to match ends of M. algicola partial sequence...
   * Length: 1485
   * Identity:   1482/1485 (99.8%)	1483/1485 (99.9%)
   * Similarity: 1482/1485 (99.8%)	1483/1485 (99.9%)
   * Gaps:          0/1485 ( 0.0%)	0/1485 ( 0.0%)
   * Score: 	7398.0			7407.0)

* 16S adhaerens complete:
  * Length: 1535/1534 (pb_359_5 = 1528; M. adhaerens = 1532)
  * Identity:    1507/1535 (98.2%)	1505/1534 (98.1%)
  * Similarity:  1507/1535 (98.2%)	1505/1534 (98.1%)
  * Gaps:          10/1535 ( 0.7%)	8/1534 ( 0.5%)
  * Score: 	7403.0			7401.0



* pb_359_4 submitted and completed
* pb_359_5 submitted and completed
* pb_359_8 submitted and completed
* Rhodo tree submitted and completed
  * New trees provisionally added to report

# 22 February 2017

## ClustalW tree for 16S sequences
* Based on tree obtained from ClustalW alignment (http://www.genome.jp/tools/clustalw/), seems likely
that the species is, indeed, M. algicola.

## antiSMASH
* Currently all been done using 'pb_359_X_Consensus.gbk'; need to make final decision on which one to use based on
number of predicted pathways.

| Sample   | Consensus | Consensus_Names     |
|----------|-----------|---------------------|
| pb_359_2 | **284**   | 283                 |
| pb_359_3 | 300       | **303**             |
| pb_359_4 | **237**   | 235                 |
| pb_359_5 | 261       | **261** (more info) |
| pb_359_6 | 302       | **307**             |
| pb_359_7 | 290       | **297**             |
| pb_359_8 | 256       | **257**             |


# 23 February 2017

## antiSMASH
Number of 2' metabolite cluster genes vs whole genome (%age)
* Compared to cyanos from presentation - ~14%

## Pathway Tools

Include incomplete EC numbers to go for maximum number of predictions
* Move all files out of default file and start afresh?
* Make Pathway Tools files available on GitHub


* Search conjugation genes
  * Searching with the term 'conjug'
    * pb_359_2 - 4 hits (0 plasmid hits)
    * pb_359_3 - 12 hits (of which 3 plasmid hits)
    * pb_359_4 - 11 hits
    * pb_359_5 - 4 hits (all plasmid hits)
    * pb_359_6 - 12 hits (of which 10 plasmid hits)
    * pb_359_7 - 1 hit (0 plasmid hits)
    * pb_359_8 - 33 hits (of which 6 plasmid hits)

* Run type strain gbk through antiSMASH?
  * Check results vs. pb_359

* Double-check copy no. of plasmids

* List of genes on each Sulfito plasmid
  * Needs formatting...

## Plasmid copy number
Compare coverage for chromosome to coverage for plasmids

| Sample   | Chrom. cover | Plasmid cover                                 |
|----------|--------------|-----------------------------------------------|
| pb_359_2 | ~140x        | ~120x, ~150x                                  |
| pb_359_3 | ~180x        | ~90x, ~120x                                   |
| pb_359_4 | ~100x        | -                                             |
| pb_359_5 | ~210x        | ~350x                                         |
| pb_359_6 | ~170x        | ~170x, ~160x, ~170x, ~130x, ~150x, ~80x, ~90x |
| pb_359_7 | ~180x        | ~200x, ~160x, ~140x                           |
| pb_359_8 | ~170x        | ~450x                                         |

## Sulfitobacter and plasmids
* Sulfitobacter sp. AM1-D1 has [five plasmids](http://www.genome.jp/kegg-bin/show_organism?org=suam),
albeit somewhat smaller than those in pb_359_6.


## To do
Continue gene-checking in pb_359_2 in Pathway Tools


# 24 February 2017

## Pathway Tools refinement
If UniProtKB gives an incomplete EC number, accept Pathway Tools predictions that would be applicable
* If UniProtKB gives 1.2.3.-, for example, accept 1.2.3.4)
* EXCEPTION: if Pathway Tools suggests the general pathway (1.2.3.-), accept that and not the specific one (1.2.3.4)

* pb_359_2 - pathways increased from 284 to 290
* pb_359_3 - pathways increased from 303 to 305

## % predictions for 2' metabolite clusters

* pb_359_2 - 4,184 CDSs in genome, 3,959 CDSs in chromosome, 154 2' metabolite cluster genes
  * As a percentage - 3.68% of genome (or 3.89% of chromosome)
* pb_359_3 - 3,952 CDSs in genome, 3,811 CDSs in chromosome, 125 2' metabolite cluster genes
  * As a percentage - 3.16% of genome (or 3.28% of chromosome)
* pb_359_4 - 3,348 CDSs in genome, 104 2' metabolite cluster genes
  * As a percentage - 3.11%
* pb_359_5 - 4,277 CDSs in genome, 4,011 CDSs in chromosome, 103 2' metabolite cluster genes
  * As a percentage - 2.41% of genome (or 2.57% of chromosome)
* pb_359_6 - 4,967 CDSs in genome, 3,497 CDSs in chromosome, 196 2' metabolite cluster genes
  * As a percentage - 3.95% of genome (or 5.60% of chromosome)
* pb_359_7 - 5,098 CDSs in genome, 4,504 CDSs in chromosome, 209 2' metabolite cluster genes (190 on chromosome)
  * As a percentage - 4.10% of genome (or 4.22% of chromosome)
* pb_359_8 - 4,984 CDSs in genome, 4,901 CDSs in chromosome, 160 2' metabolite cluster genes
  * As a percentage - 3.21% of genome (or 3.26% of chromosome)

## To do

* Continue refinements of annotation using UniProtKB

# 27 February 2017

## pb_359_2 Leukotoxin BLASTp - best hits
* IAEOHLKH_00090: 5' nucleotidase
* IAEOHLKH_00466: putative calcium-binding proteins
* IAEOHLKH_00488: aggregation factor core protein MAFp3
* IAEOHLKH_01179: type I secretion protein
* IAEOHLKH_01809: large exoprotein
* IAEOHLKH_01818: rhizobiocin/RTX toxin
* IAEOHLKH_02005: type I secretion protein
* IAEOHLKH_02307: rhizobiocin/RTX toxin
* IAEOHLKH_02309: hemolysin-type calcium-binding region
* IAEOHLKH_02820: [mainly poor hits]
* IAEOHLKH_02860: hypothetical proteins
* IAEOHLKH_02884: [mainly poor hits, to second-half of protein]
* IAEOHLKH_03603: nidogen, extracellular region
* IAEOHLKH_03940: hemolysin-type calcium-binding protein
* IAEOHLKH_03943: hemolysin-type calcium-binding region, RTX

## Pathway Tools prediction refinement
* pb_359_4 - pathways increased from 237 to 241
* pb_359_5 - pathways increased from 261 to 264 (forgot to set new version...)


# 28 February 2017

## Pathway Tools prediction refinement
* pb_359_6 - pathways increased from 307 to 313
* pb_359_7 - pathways increased from 297 to 307

* Next step - v1.2 of the database could attempt to implement the Pathway Hole Filler?
* Continue checking function of pb_359_6 plasmids

# 01 March 2017

## Pathway Tools prediction refinement
* pb_359_8 - pathways increased from 257 to 259

## Pathway Tools prediction summary

| Sample   | Before | After | Diff | PHF | Diff |
|----------|--------|-------|------|-----|------|
| pb_359_2 | 284    | 290   | +6   | 296 | +6   |
| pb_359_3 | 303    | 305   | +2   | 311 | +6   |
| pb_359_4 | 237    | 241   | +4   | 249 | +8   |
| pb_359_5 | 261    | 264   | +3   | 271 | +7   |
| pb_359_6 | 307    | 313   | +6   | 321 | +8   |
| pb_359_7 | 297    | 307   | +10  | 320 | +13  |
| pb_359_8 | 257    | 259   | +2   | 268 | +9   |

## pb_359_6 Plasmids
* Individually inputted into Pathway Tools
* Individual lists of (non-hypothetical) gene products created

* Question - how are these plasmids being maintained...?
  * 7 plasmids would constitute an enormour metabolic cost to maintain,
    especially with them being so big...

* Each plasmid has an antitoxin gene; this may contribute

| Plasmid | Size (bp) | Protein genes | RNA genes | Pathways |
|---------|-----------|---------------|-----------|----------|
| 1       | 428,095   | 412           | 3         | 36       |
| 2       | 292,917   | 255           | 6         | 21       |
| 3       | 284,777   | 277           | 3         | 23       |
| 4       | 209,222   | 193           | -         | 19       |
| 5       | 142,107   | 152           | -         | 5        |
| 6       | 99,245    | 93            | -         | 8        |
| 7       | 92,794    | 88            | -         | 6        |

# 2 March 2017

## pb_359_6 Plasmids
* Do the plasmids provide functions that the chromosome doesn't?
  * No unique pathways in plasmid 1
  * **arsenate detoxification II (glutaredoxin)** unique to plasmid 2
    * Only 'arsen' search result on the chromosome - **arsenite oxidation II (respiratory)**
    * False positive... (see below)
  * **NAD biosynthesis I (from aspartate)** unique to plasmid 3
    * Only 'NAD biosynthesis' search result on the chromosome - **NAD biosynthesis from 2-amino-3-carboxymuconate semialdehyde**
    * Another false positive... (see below)
  * No unique pathways in plasmid 4
  * No unique pathways in plasmid 5
  * No unique pathways in plasmid 6
  * No unique pathways in plasmid 7
  * No unique proteins in any plasmid

* The files compared to the plasmid files were for the whole genome;
predictions for plasmids are changing depending on the presence of absence of the chromosome...
  * Arsenate oxidation II (respiratory) - predicted genes (full) - aioA_2, aioA_1, aioB
  * Arsenate detoxification II (glutaredoxin) - predicted genes (plasmid 2) - arsC (missing 3.6.3.16)
    * arsC also exists on the chromosome...

  * NAD biosynthesis from 2-amino-3-carboxymuconate semialdehyde - predicted genes (full) - nadC, nadD (also MOLFBGNK_02398), nadE
  * NAD biosynthesis I (from aspartate) - predicted genes (plasmid 3) - nadB, nadA, nadC; lower part of the pathway missing (6.3.1.5 not covered by chromosome;
    2.7.7.18 and 6.3.5.1 are covered)
    * Seems to be another false positive...


* Double-checked plasmid sizes of Sulfitobacter sp. AM1-D1
  * Plasmids not in size order; this strain also contains some large plasmids (largest 348,874 bp)
  * "Complete genome sequence of Sulfitobacter sp. AM1-D1, a toxic bacteria associated with marine dinoflagellate Alexandrium minutum in East China Sea"
    * Sadly, paper has not been published yet (submitted Dec 2016)

* Sulfitobacter guttiformis has three plasmids, including one megaplasmid


* Pathway Tools analysis rerun using just pb_359_6 chromosome; pathway and protein lists exported

* Study on number and size of plasmids (within Enterobacteriaceae, not Rhodobacteraceae)
  * http://www.sciencedirect.com/science/article/pii/S0147619X02001075
  * "From 0 to 7 co-resident plasmids were detected within individual bacterial strains"
    * 7 is at the top end, so Sulfitobacter's other contigs may truly be plasmids...
    * Plasmids greater than 256 Kbp found (cf. ~428 Kbp of pb_359_6 largest plasmid)
* Megaplasmids present in Sinorhizobium (2x plasmids greater than 1 Mb)
  * https://academic.oup.com/femsec/article-lookup/doi/10.1111/j.1574-6941.2008.00505.x
  * "However, these data do raise the possibility that plasmid size is under the same ecological constraints as chromosome size,
   with larger genomes associated with more complex, heterogeneous environments, such as soil."
* Megaplasmids seen in other Rhodobacteraceae
  * Silicibacter pomeroyi has a megaplasmid of ~491 Kbp

* Problem - is there evidence of large plasmids AND high numbers of different plasmids in the same species/strain?

## Pathway Tools
Pathway Hole Filler can take 8+ hours; try on plasmid, let chromosomes run overnight
* Smallest pb_359_6 plasmid has too few pathways/proteins to act as training data; need at least 50.
* Running on Sphingorhabdus (pb_359_4), as it is both the smallest chromosome and has the lowest no. of contigs.
  * Process took about an hour; selected top candidate in all cases, and rejected any pathways with less than half of components.

# 3 March 2017

## Blast
* Blast pb_359_6 against Sulfitobacter sp. AM1-D1
  * Plenty of hits, but not many huge, almost-perfect matches (a lot of the hits on the chromosome seem to contain ~1% gaps)

## Pathway Hole Filling
* Continue to use Pathway Hole Filler on samples (ensure that a new version number of each KB is created for this)

## To do
* Check for any informative differences now that Assign Probable Enzymes and Pathway Hole Filler have been run.
* Compare results of VirSorter and PHASTER.
* Work on poster and report.

# 6 March 2017

## PHASTER vs VirSorter
* pb_359_2
  * PHASTER prediction locations: 667953-681826, 3056898-3082821, 3609563-3684676 (All intact)
  * VirSorter prediction locations: 3610619-3693782 (cat 5), 2982393-3083217 (cat 6)
    * Two potential matches; PHASTER predicts one more sequence (scored 140/150, but only 18 proteins present)

* pb_359_3
  * PHASTER prediction locations: 60063-86985 (incomplete), 107037-127863 (incomplete), 1708018-1725675 (intact), 2554203-2572760 (questionable)
				  2754039-2758904 (incomplete), 3665970-3700784 (intact) (+ Plasmid 1 - 61435-79659 (incomplete))
  * VirSorter prediction locations: 3084744-3178263 (cat 5), 3670268-3705289 (cat 5), 2495680-2580684 (cat 5) (all chromosome)
                                    3792356-3836998 (cat 6), 2353020-2408937 (cat 6), 3352207-3404798 (cat 6), 826707-869949 (cat 6) (all chromosome)
    * Two potential matches, one slightly tenuous; overall, not much match-up between the two predictions
      * **Double-check the prediction methods for the two programs**

* pb_359_4
  * PHASTER prediction locations: 1788211-1822735 (incomplete), 2885186-2900516 (intact)
  * VirSorter prediction locations: 222024-275593 (cat 5), 2172724-2202648 (cat 6)
    * No overlap

* pb_359_5
  * PHASTER prediction locations: 2007744-2045050 (incomplete)
  * VirSorter prediction locations: 2557585-2612619 (cat 5)
    * No overlap

* pb_359_6
  * PHASTER prediction locations: 2070068-2092886 (questionable) (+ Plasmid 1 -	36405-69679 (intact); Plasmid 3 - 223862-249633 (incomplete);
				  Plasmid 5 - 118518-129108 (incomplete))
  * VirSorter prediction locations: 2068135-2080179 (cat 5), 1718446-1731079 (cat 5) (+ Plasmid 1 - 316148-414273 (cat 6))
    * Two potential matches

* pb_359_7
  * PHASTER prediction locations: 1720004-1743048 (questionable), 3102869-3117957 (intact), 3498867-3508923 (incomplete), 4649429-4662956 (incomplete)
				  (+ Plasmid 1 - 2509-36730 (intact), 279460-305254 (incomplete); Plasmid 3 - 54137-60779 (incomplete))
  * VirSorter prediction locations: 3376495-3395782 (cat 5), 3179443-3194320 (cat 6), 3878522-3896803 (cat 6)
    * Hits in the right areas, but no direct overlap

* pb_359_8
  * PHASTER prediction locations: 3802794-3809819 (questionable), 4318764-4331621 (questionable)
  * VirSorter prediction locations: 443338-516457 (cat 6)
    * No overlap

* The two methods appear to have comparable detection ability for phages; unsure about prophages, as the VirSorter paper doesn't mention its categories 4-6

## Pathway Tools
* DL and compare pathway/protein lists between v1.0 and v1.2 databases
* Wrote a script to reformat

## Compare old and new pathway/protein files
Interesting observations:
* pb_359_4 now appears to show a cellulose biosynthesis pathway
  * Only the bcsC subunit... bcsA and bcsB are 'necessary and sufficient' to form cellulose chains in vitro.
* pb_359_6 now appears to show a polyethylene terephthalate (PET) degradation pathway
  * One of the two components is currently predicted, so not a definite...
* pb_359_7 now appears to show cellulose biosynthesis AND polyethylene terephthalate (PET) degradation pathways
  * As with pb_359_4, only bcsC currently predicted
  * As with pb_359_6, only one PET degradation component currently predicted
* Cardiolipin biosynthesis I has been added to all species' pathway lists
* Apparently no interesting (from the perspective of this project) new pathways inferred from the refinement steps

# 7 March 2017

## NCBI
Upload sequence (and annotation?) to NCBI for pb_359_2
* https://www.ncbi.nlm.nih.gov/genbank/genomesubmit/
* Check conventions for naming annotation loci
  * Cannot contain underscores, so will try to register ROSMUCR3
  * This alteration has been made in the GenBank file, pending acceptance

Steps to follow:
1. Establish a BioProject (including all S. marinoi microbiome project samples?)
2. Register each organism as a BioSample (can be submitted in batch if required)
3. 


## Things to check
* At locus 00589 is a gene nylB'. Why is there an apostrophe??
* At locus 01105 is a gene hdl IVa. How to deal with the space??
* At locus 01742 is a gene sat/cysC. Is this valid??
* At locus 02210 is a gene Y2-aiiA. Is this valid??
* At locus 03888 is a gene absAa. Is this valid??

* Remove /inference fields which say 'similar to AA sequence:[custom database]'

* Start from `grep "/product=\"H" test | sort | uniq`
  * Use `sed -i 's/\"Imely/\"imely/g' test` format to replace upper-case beginnings

# 8 March 2017

## NCBI
* Remember to add grants to the BioProject
* Need raw reads - available in H5 format from SMRT portal, but impractical to move these via repository; access denied to relevant area on Albiorix...
  * Where is base modification file? Would this come from Falcon output or from Resequencing?
* Site to convert GenBank files to .tbl and .fsa: https://chlorobox.mpimp-golm.mpg.de/GenBank2Sequin.html
* Submission to NCBI requires a protein_id field of format	gnl|XXXX|locus_tag	for CDS entries, where XXXX is a unique centre identifier
* No obvious way to add this, so will attempt to make a Python script for it
  * Use GotUniMarDep as centre identifier; can always change with `sed` later
  * Written protein_id_Adder.py script for this purpose

* Certain fields still need to be removed from the .tbl files
  * transl_table
  * codon_start
* Strain needs to be changed in .fsa files
* Header and filename needs to be checked on both .tbl AND .fsa files

### Submission guidelines

* "Your lab must have sequenced the genome or paid to have it sequenced or been part of the collaboration that sequenced it.
  You cannot submit a genome that you have downloaded from a web site or similar place."
  * COMPLETE

* "The sequence submission must represent a sequence that occurs biologically in the organism. Do not randomly combine the contigs to create a single sequence;
  you must keep them separate (a traditional WGS submission) or join them with runs of Ns into the correct order and orientation (a gapped WGS submission).
  If you keep them separate in a traditional submission, you can provide the information to assemble them into scaffolds and/or chromosomes or plasmids
  with an AGP file (//www.ncbi.nlm.nih.gov/genbank/wgs.submit#agp)."
  * COMPLETE

* "Register the source information for each genome in the BioSample database. Multiple BioSamples can be pre-registered at once, with the Batch option.
  For isolated unicellular organisms, chose the appropriate Pathogen package (Clinical or host-associated pathogen OR Environmental, food or other pathogen)
  or the Microbe package. If the same sample is used for two different genome assemblies, then use the same BioSample for both."
  * BIOSAMPLE REGISTRATION ONGOING; MUST DOUBLE-CHECK DETAILS

* "Each genome must belong to a BioProject. Genomes sequenced as part of the same research effort can belong to a single multi-isolate or to a multi-species
  BioProject.  When more BioSamples are added to a BioProject, the assigned locus_tag prefixes are added to the locustagprefix.txt file in the BioProject
  submission portal, https://submit.ncbi.nlm.nih.gov/subs/bioproject/."
  * BIOPROJECT REGISTRATION ONGOING; MUST DOUBLE-CHECK DETAILS

* "Raw reads should be submitted to SRA. If the genome was sequenced using PacBio sequencing technology, please also submit to SRA the base modification files,
  eg the motif_summary.csv file. If you have any questions about SRA, contact sra@ncbi.nlm.nih.gov."
  * FIND RAW READS ON ALBIORIX (DOWNLOAD FROM SMRT PORTAL IF NECESSARY)
  * FIND BASE MODIFICATION FILES FROM FALCON/SMRT PORTAL?

* "Annotation is not required, but if annotation is provided it must be biologically valid and the product names should follow the
  UniProt-Protein Naming Guidelines."
  * SEEMS TO BE COMPLETE NOW

* "NCBI's Prokaryotic Genomes Annotation Pipeline (NCBI_PGAP) is used to annotate prokaryotic RefSeq genomes and is available for GenBank submissions, by request.
  No changes by the submitter are needed to make this annotation ready for GenBank submission. Note that all complete prokaryotic genomes will be run through
  NCBI_PGAP for a basic integrity check, to see that the genome contains some required elements like RNAs and has low levels of pseudogenes/frameshifted genes.
  The genome will not be released with this annotation unless you ask us to include it."
  * NOT REQUIRED; ANNOTATION DONE VIA PROKKA

* "Provide relevant chromosome, plasmid or organellar assignment information for any sequences in the fasta definition line, as described below."
  * ONGOING

### Data files
1. Fasta File
  * "Put the sequences into fasta format of the sequences. These files have the suffix .fsa. Each sequence has a definition line beginning with a '>' and a unique
   identifier, eg contig001, contig002, etc."
  * PROVISIONALLY COMPLETE, MAY NEED TO BE CHECKED AND REDONE...

2. "A template file with submitter, publication, BioProject and BioSample information."
  * NEEDS TO BE COMPLETED; SEE TEMPLATE

3. "The Genome-Assembly-Data Structured Comment which includes the assembly method and version, the genome coverage and the sequencing technologies can be
    created on the Structured Comment Template page."
  * COMPLETE - DOWNLOADED AS genome.asm

4. "Annotation files, if appropriate. These correspond to and have the same basenames as the .fsa files, but have the suffix .tbl. The .tbl files have a 5-column
   tab-delimited format, as described in the annotation instruction pages. Be sure to read the annotation requirements in the appropriate annotation guidelines."
  * COMPLETE

5. "Quality scores of the sequences. These files correspond to and have the same basenames as the .fsa files, but have the suffix .qvl.
   The quality scores are optional, but desired."
  * QUALITY SCORES UNAVAILABLE...

## To do

* Finish registering BioProject and BioSample (double-check details with Mats)
* Obtain raw reads and base modification files from SMRT Portal/Falcon file
* Check that fasta and contig names are acceptable
* Complete general template
  * Specifically, Sequence Authors
* Follow the 'Create your submission' instructions [here](https://www.ncbi.nlm.nih.gov/genbank/genomesubmit/)

# 9 March 2017

## protein_id_Adder.py
* Redo script to simply output the file as a .tbl file...
  * Version 2 of the script has been written, and appears to be working as intended

## NCBI
Be sure to double-check naming conventions...

## Leukotoxin
* As the pb_359_2 leukotoxin genes were just labelled as 'leukotoxin', genes of similar function may have been
  found in the other species, but by a different name. Grep alternative search terms based on the BLAST results.

  * 5' nucleotidase - fairly frequent in other species
  * hemolysin-type calcium-binding region - common
  * type I secretion protein - common primarily among Rhodobacteraceae
  * putative calcium-binding proteins - relatively uncommon

  * aggregation factor core protein MAFp3 - no other matches
  * large exoprotein - no other matches, but vague
  * rhizobiocin/RTX toxin - no other matches to rhizobiocin
  * nidogen, extracellular region - no other matches

# 10 March 2017

## To do
If system will cooperate, rerun 10% BLASTs on the final assemblies...
* Failing that, use results from original HGAP assemblies (this is stated in the report...)

# 13 March 2017

## NCBI Submission

* Finish registering BioProject and BioSample (double-check details with Mats)
* Obtain raw reads and base modification files from SMRT Portal/Falcon file
* Check that fasta and contig names are acceptable
* Complete general template
  * Specifically, Sequence Authors
* Follow the 'Create your submission' instructions [here](https://www.ncbi.nlm.nih.gov/genbank/genomesubmit/)

## More functional searches
* Siderophores
  * Marinobacter and Sulfitobacter seem most likely to produce siderophores
    * Both species contain a multitude of required genes - High numbers of hits when grepping 'siderophore' (including on Sulfitobacter plasmids),
      and presence of related genes checked (http://onlinelibrary.wiley.com/doi/10.1046/j.1365-2958.2002.02951.x/full)
      * Fhu hydroxamate uptake family - fhuABCD in Marinobacter, fhuAC in Sulfitobacter
      * TonB (energy transducer) present in both
    * Marinobacter siderophore cluster (serobactin) noted by antiSMASH
    * Sulfitobacter siderophore cluster (vicibactin) noted by antiSMASH
    * 'Putative siderophore biosynthesis protein SbnA' noted for Marinobacter
    * 'Enterobactin synthase component D' noted for Sulfitobacter

  * Pathway Tools
    * Marinobacter - 2/4 components predicted for aerobactin biosynthesis
      * 5/7 components predicted for enterobactin biosynthesis
    * Sulfitobacter - 2/4 components predicted for aerobactin biosynthesis

  * Roseovarius and Sphingorhabdus - enterobactin biosynthesis predicted
    * Roseovarius - 4/7 components predicted
    * Sphingorhabdus - 3/7 components predicted

  * Curiously, more species seem to code for 'Vibriobactin utilization protein' ViuB than actually produce it.
    * Multiple bacteria scrounging off of two species actually producing vibriobactin/siderophore?
      * Xenosiderophores - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3832793/

* Auxins - indole-3-acetate / indole-3-acetic acid biosynthesis pathway
  * Plant hormone, seen in other diatom-microbe interactions
  * Roseovarius - 2/2 predicted for indole-3-acetate biosynthesis IV (bacteria)
  * Marinobacter - 1/1 predicted for indole-3-acetate biosynthesis V (bacteria and fungi)
  * Sulfitobacter - 2/2 predicted for indole-3-acetate biosynthesis III (bacteria)
    * 2/2 predicted for indole-3-acetate biosynthesis IV (bacteria)
  * Antarctobacter - 2/2 predicted for indole-3-acetate biosynthesis IV (bacteria)
    * 1/1 predicted for indole-3-acetate biosynthesis V (bacteria and fungi)

* Chitin degradation II (Vibrio) pathway
  * Chitin degradation demonstrated in at least one algicidal species - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4763246/
  * Roseovarius - 2/4 components predicted
  * Loktanella - 2/4 components predicted
  * Sphingorhabdus - 2/4 components predicted
  * Sulfitobacter - 2/4 components predicted
  * Antarctobacter - 2/4 components predicted
  * Arenibacter - 2/4 components predicted
  * As the 2 components predicted are the same protein, and the same two steps are predicted in each example, unconvincing...

(Replace R05AC with RO5AC)
* Complete Grants section of BioProject
* Generating modification files on SMRT Portal... Check tomorrow

* BioSample submitted, awaiting confirmation...

## To do
* Look into other experiments which have investigated diatom microbiomes
* Check SMRT Portal, download relevant modification files for SRA submission
* Rename contigs? e.g. RosMucR3_chrom, RosMucR3_longplas, RosMucR3_shortplas?
* Check xml requirements

# 14 March 2017

## NCBI
* Biosample accession - SAMN06564448

* Files required for SRA submission:
  * modifications.csv
  * motifs.gff
  * motifs_summary.csv
* Files downloaded; need to be decompressed


## Diatom-bacteria interactions
* Look into 'roseobacticides'

# 15 March 2017

## NCBI
Raw data stored at /home/smrtanalysis/userdata/inputs_dropbox/pb_359/rawdata/pb_359-2/run1/B01_1/Analysis_Results

* XML preparation is unnecessary - see email from SRA

* Checksums for files
  * RosMucR3_modifications.csv	9499b9e417f2866f2cf0b04461b90eab
  * RosMucR3_motifs.gff		a4a79df700dcc853d3e874d6e0562b7f
  * RosMucR3_motif_summary.csv	1b0ace9555cad09b954e150fe4315749

* Seems like .fsa files may need to be merged - awaiting reply from NCBI
  * If this is the case, what about the .tbl files?
* tbl2asn may need updating...

* tbl2asn command to be run from C:\Users\matt_\Desktop\PROJECT\Skeletonema_marinoi_microbiome_project\SubmissionPreparations\RosMucSMR3\NCBI
  * ..\..\..\..\tbl2asn\tbl2asn.exe -p . -t RosMucSMR3_Template.sbt -M n -Z discrep -w RosMucSMR3_StructuredComment.asm

* tbl2asn run on Windows, has returned a mass of error messages for the pb_359_2 records; attempt to solve
  * Protein product containing '?'/ ending in '_'
    * Offending character removed; change noted in note field
  * Protein product named 'Agrobacterium tumefaciens protein'
    * Renamed as 'hypothetical protein' (most BLASTp results concur); change noted in note field

* Checking additional errors
  * https://blast2go-apps.github.io/ncbi-submission/user_manual/NCBI_Submission_b2g_App_DOC.pdf

# 16 March 2017

## NCBI
* Receiving a lot of errors about wrong start/stop codons, but no data on WHICH genes are causing the error...
  * Concatenating all contigs into one file doesn't work
  * Issue with printing locations of sequences on the complementary strand
    * GenBank to .tbl script fixed

* All other errors fixed; only major issue remaining is DBLinkProblem; this may fix itself once a BioProject is assigned
  * Template will need to be redone afterwards
  * Conflicting gene names present but harder to fix - 555 instances
  * Small, non-critical issues addressed such as products ending in ] and _, and some instances of products of kDa weights
    * Where relevant, original names have been included in a note

# 17 March 2017

## pb_359_7
* Double-check classification of pb_359_7 as Antarctobacter; 16S check not convincing...
  * Similarities to genera Ruegeria and Mameliella
  * Based on PhyloPhlAn analysis, more closely related to Mameliella (Ruegeria is in another clade, closer to Sulfitobacter)
  * 16S shows pb_359_7 sequences assorting with Antarctobacter; Mameliella and Ruegeria form their own clade
    * Download more 16S sequences for a broader survey
  * Re-classify as Mameliella?

## Report
* Add results of 16S searches; tabulate

## To do
* Add 16S results table to report
* Continue 16S checks on pb_359_7
  * List of sequences saved; may need to reverse-complement some of these...

# 20 March 2017

## pb_359_7
* MUSCLE alignment on EBI will only accept 500 sequences; 875 were taken from SILVA; take 500 longest?
  * 500 longest obtained; pb_359_7 nestled within Antarctobacter, but negative branch lengths according to MUSCLE?
  * SILVA can only pinpoint pb_359_7 down as far as Rhodobacteraceae family...
* Reassured of the identity of pb_359_7, based on 16S; unfortunate that no full-length 16S sequences exist for Antarctobacter in NCBI...
  * Best way to represent this for report?

## Genome Announcements
* Include accession no. AND locus tag of 16S matches?

## To do
* Generate 16S tree for pb_359_7 with sequences from Ruegeria, Mameliella and Antarctobacter where available...
  * NCBI or SILVA?
    * NCBI has a lot of Ruegeria sequences; Mameliella and Antarctobacter more manageable
    * Only RefSeq sequences for Ruegeria? Reduces number down to 20...

# 21 March 2017

## pb_359_7
* Search for 16S sequences for Ruegeria, Mameliella and Antarctobacter (plus a couple of sequences as an outgroup?)
  * 21x Antarctobacter sequences (all partial, but only selected those sequences over 1 Kb)
  * 6x Mameliella sequences (all partial, but only selected those sequences over 1 Kb)
  * 19x Ruegeria sequences (two complete, rest partial; over 1,000 search results so only those from RefSeq selected)
* Remove sequences with N and R in case this complicates the analysis?

(* Process:
  * Antarctobacter, Mameliella and Ruegeria identified primarily through 16S searches
  * Search 'genus AND 16S[title]' on NCBI Nucleotide
  * Exclude any hits less than 1 Kb
  * For Ruegeria, as there were 1,000+ hits, only those from RefSeq were selected
  * Sagittula stellata included as outgroup
  * Any hits with Ns or Rs in the sequence were excluded, to prevent any complications in the analysis
  * Hits concatenated and inputted into ClustalW to produce a gapped alignment
  * Gapped alignment run through FastTree
  * Tree file visualised in FigTree)

* New strategy - run pb_359_7 16S through BLASTn using nr/nt, RefSeq_genomic and 16S databases, and run top four results from each through ClustalW

## To do

* Retry RefSeq_genomic search vs pb_359_7 16S sequence; keeps failing...
  * If this can be made to work, run through ClustalW and obtain tree

# 22 March 2017

## NCBI

Still waiting for response from NCBI re: BLASTN and refseq_genomic
* Known issue, resolution underway

# 23 March 2017

## Roseovarius mucosus

* New strain designation: SMR3
* New plasmid names: pSMR3-1 and pSMR3-2

## BLASTn
* Blast pb_359_2 16S against Roseovarius sp. TM1035 to confirm stats
* Align R. mucosus type strain 16S against pb_359_2 to get full length identity comparison
  * Type strain DSM 17069 - their predicted 16S was shorter, but trimming ours or lengthening theirs
  * Found to have 99.8% similarity with both iterations of the type strain



## To do
* Complete pb_359_2 PhyloPhlAn comparison underway, check in the morning
* Await NCBI email regarding the DBLink errors from tbl2asn

# 24 March 2017

## PhyloPhlAn
Completed pb_359_2 vs all Rhodobacteraceae tree
* Closest to Roseovarius sp. TM1035; this clade shares MRCA with Roseovarius mucosus

## Genome submission
.sqn files currently being checked on NCBI's [Genome Submission Check Tool](https://www.ncbi.nlm.nih.gov/genomes/frameshifts/frameshifts.cgi)

## NCBI checker
* Overlap found in two places on long plasmid
  * dctM + dctQ - 50 bp overlap, precedent in type strain
  * ParB + 'regulator' - 62 bp overlap, BLASTx in the region finds no regulator, only ParB...
* Two potential truncations on the long plasmid
  * 04025 - ~200 bp 5' truncation?
  * 04182 - ~250 bp 5' truncation?

* One potential truncation on the short plasmid
  * 04237 - ~50 bp downstream and ~50 bp upstream missing?

* Chromosome check ongoing...


## To Check
OrcID

* pSMR3-1 has a gene which appears to cross the divide between the start and end of the linearised sequence
  * Sequence submitted as-is, but see if this can be fixed for an update
* See whether the chromosome came up with any issues...

# 27 March 2017

## NCBI
Still waiting for processing of pb_359_2 genome to complete; chromosome showed many errors in the final check,
so this may come back with requests for corrections...


## CeMEB
Title and abstract for poster sent to Eva Marie
* Formatting and wording on poster itself almost done; size changed to A0 for ease of printing
  * Remember to select high quality print-out

# 28 March 2017

## pb_359_2 Upload
Comments received from NCBI:

1. Some ncRNAs are not RNAs, but are signals
  * Ask to have them included as a note on the feature

2. cspA (cold shock protein A) ncRNA has an incorrect span
  * Check other Rhodobacteraceae sequences (Roseovarius sp. TM1035?) in search of true span
  * BLASTp of this sequence vs. refseq_genomic primarily reveals identical/near-identical sequences, of the same length (68aa). However, one Roseovarius sequence
    is longer on the 5' end

3. Four potential pseudogenes
  * Check statistics of matches, see whether they are convincing
    * ROSMUCSMR3_00650 / ROSMUCSMR3_00649: Sum BLAST scores of hits to try and find most convincing hit
      * gi|568303274|ref|YP_008975559.1| Putative phage tail protein/GTA TIM-barrel-like domain protein (also has the smallest insert; Occam's Razor)
    * ROSMUCSMR3_01411 / ROSMUCSMR3_01410
      * gi|56695436|ref|YP_165784.1| glutamate/glutamine/aspartate/asparagine ABC transporter (only narrowly the best hit... Check vs R. sp. TM1035?)
    * ROSMUCSMR3_03399 / ROSMUCSMR3_03398
      * gi|507516730|ref|YP_008038347.1| group 1 glycosyl transferase - **not convinced enough; should remain as two genes**
    * ROSMUCSMR3_03409 / ROSMUCSMR3_03408
      * gi|377807456|ref|YP_004978648.1| Phytanoyl-CoA dioxygenase (seems to be best match but not amazing; R. sp. TM1035 seems more convincing)

4. Send motif_summary.csv, OR upload to SRA along with raw reads
  * Will be uploading to SRA anyway

5. CHECK IF LOCUS_TAG NUMBERING WILL BE AFFECTED, AND IF THIS WILL
   CARRY OVER TO THE OTHER CONTIGS

## Report
Should pb_359_5 16S tree be extended to the same size as the pb_359_7 16S tree


## SRA
Double-check metadata for pb_359_2 sequence run
* Files required:
  * motifs.gff.gz
  * modifications.csv.gz
  * motif_summary.csv
  * m160816_190022_42203_c101086032550000001823265803091732_s1_p0.bas.h5
  * m160816_190022_42203_c101086032550000001823265803091732_s1_p0.3.bax.h5
  * m160816_190022_42203_c101086032550000001823265803091732_s1_p0.2.bax.h5
  * m160816_190022_42203_c101086032550000001823265803091732_s1_p0.1.bax.h5
* Files CAN be compressed (.gz), and archived (.tar) if wanted

* Copy assembly files (as superuser) and tarball them
  * /home/smrtanalysis/userdata/inputs_dropbox/pb_359/rawdata/pb_359-2/run1/B01_1/Analysis_Results/m160816_190022_42203_c101086032550000001823265803091732_s1_p0.bas.h5
  * /home/smrtanalysis/userdata/inputs_dropbox/pb_359/rawdata/pb_359-2/run1/B01_1/Analysis_Results/m160816_190022_42203_c101086032550000001823265803091732_s1_p0.1.bax.h5
  * /home/smrtanalysis/userdata/inputs_dropbox/pb_359/rawdata/pb_359-2/run1/B01_1/Analysis_Results/m160816_190022_42203_c101086032550000001823265803091732_s1_p0.2.bax.h5
  * /home/smrtanalysis/userdata/inputs_dropbox/pb_359/rawdata/pb_359-2/run1/B01_1/Analysis_Results/m160816_190022_42203_c101086032550000001823265803091732_s1_p0.3.bax.h5

* Double-check metadata tomorrow...
* Double-check rules for ftp; file created at NCBI ftp site but unable to submit
  * `ftp ftp-private.ncbi.nlm.nih.gov`
    * Username: subftp
    * Password: w4pYB9VQ
  * `cd uploads/matt_pinder13@hotmail.com_n7ATBk2o/SAMN06564448_RosMucSMR3`
  * `put ~/MastersProject/Roseovarius_mucosus_SMR3_assembly.tar.gz`

# 29 March 2017

## NCBI Uploads
* Genome data accepted as accession number CP020474, CP020475 and CP020476
* SRA data needs to be uploaded via ftp
  * Must be in directory containing file to transfer; linking through other directories doesn't work
* Additional data (motifs, methylation, etc.) needs to be uploaded via Supplementary Files
  * Files too big to be transferred via Git, how to save Windows-side for upload?
  * Mobaxterm has built-in rsync capabilities
    * .gz files must be unzipped on Albiorix, 7zip doesn't seem to handle this well
* SRA data uploaded; once processing complete and files have been accepted, delete raw reads from microbiome project directory to save space
* Supplementary files uploading...

## pb_359_2
Run NCBI-generated GenBank file through Pathway Tools
* Initial no. of pathways: 284
* After Assign Probable Enzymes: 288
* After Pathway Hole Filler: 295

## To do
Retry uploading the Supplementary files
* Retry installing Aspera Connect?

Update details re: pathways in pb_359_2


# 30 March 2017

## NCBI
Still need to upload Supplementary Files; waiting on reply from SRA regarding upload issues

## Report
Redo Marinobacter 16S tree; need to obtain additional results from 16S BLASTn
* Redo Antarctobacter too; trim all ends to line up

## To do
Update details on the GitLab repository readme file

# 31 March 2017

## 16S rRNA
Double-check exact percentages of similarity between pb_359_7 16S rRNA and BLASTn results (after trimming)
* Antarctobacter_heliothermus_DSM_11445		99.9%
* Antarctobacter_heliothermus_EL-219		99.5%
* Antarctobacter_sp_R14				99.5%
* Antarctobacter_sp_R22				99.4%
* Antarctobacter_sp_R30				99.4%
* Antarctobacter_sp_RO5				99.3%
* Mameliella_alba_CGMCC_1.7290			96.3%
* Mameliella_alba_UMTAT08			96.3%
* Ruegeria_sp_PBVC088				96.3%
* Alkalimicrobium_pacificum_F15			95.8%
* Ponticoccus_lacteus_strain_JL351		95.8%
* Sagittula_stellata_E-37			95.6%

**pb_359_7 is 99.9% similar to A. heliothermus, but pb_359_6 is only 99.2% similar to S. pseudonitzschiae; therefore,
either _7 is a strain of A. heliothermus, or _6 is not a strain of S. pseudonitzschiae**


## To do
Double-check percentages for Marinobacter 16S similarity

Add bold to Figure legends in report


# 3 April 2017

## 16S Checks

* pb_359_4 - 99.9% (trimmed) similarity to Sphingorhabdus flavimaris R-36742 (formerly Sphingopyxis flavimaris)
* pb_359_7 - 99.9% (trimmed) similarity to Antarctobacter heliothermus DSM 11445

* pb_359_6 - 99.2% (trimmed) similarity to Sulfitobacter pseudonitzschiae H3T (= DSM 26824T); is classification reliable?


Marinobacter 16S checks
* nr/nt
  * Marinobacter sp. 114Z-4 16S ribosomal RNA gene, partial sequence					JX310122.1		99.8%/99.9%
  * Marinobacter sp. 132Z-4 16S ribosomal RNA gene, partial sequence					JX310148.1		99.5%
  * Marinobacter sp. 114Z-23 16S ribosomal RNA gene, partial sequence					GU584144.1		99.5%
  * Marinobacter sp. R-28770 partial 16S rRNA gene, strain R-28770					AM944523.1		99.9%/100%
  * Marinobacter sp. R-28768 partial 16S rRNA gene, strain R-28768					AM944524.1		99.9%/100%
  * Marinobacter sp. EZ43 16S ribosomal RNA gene, partial sequence					EU704111.1		99.3%
  * Marinobacter salarius strain R9SW1 16S ribosomal RNA gene, partial sequence				KJ547705.1		99.4%/99.5%
  * Marinobacter salarius strain R9SW1, complete genome							CP007152.1		99.4%/99.5%
  * Marinobacter algicola partial 16S rRNA gene, strain 407-13						AJ294359.1		99.9%

* refseq_genomic
  * Marinobacter sp. C18 contig_42, whole genome shotgun sequence					NZ_LQXJ01000037.1	99.9%/100%
  * Marinobacter sp. MCTG268 U734DRAFT_scf7180000000032_quiver.11_C, whole genome shotgun sequence	NZ_JQMK01000002.1	99.5% + 99.9%
    * Marinobacter sp. MCTG268 U734DRAFT_scf7180000000033_quiver.14_C, whole genome shotgun sequence	NZ_JQMK01000005.1	99.5%
  * Marinobacter algicola DG893 1103407001930, whole genome shotgun sequence				NZ_ABCP01000031.1	99.8% + 99.9%
  * Marinobacter salarius strain R9SW1, complete genome							NZ_CP007152.1		99.4%/99.5%

* 16S
  * Marinobacter algicola strain DG893 16S ribosomal RNA gene, partial sequence				NR_042807.1		99.8%/99.9%
  * Marinobacter adhaerens strain HP15 16S ribosomal RNA gene, complete sequence			NR_074765.1		98.4%
  * Marinobacter adhaerens strain HP15 16S ribosomal RNA gene, partial sequence				NR_115177.1		98.4%
  * Marinobacter flavimaris strain SW-145 16S ribosomal RNA gene, partial sequence			NR_025799.1		98.0%/97.9%
  * Marinobacter sediminum strain R65 16S ribosomal RNA gene, partial sequence				NR_029028.1		97.1%
  * Marinobacter salsuginis strain SD-14B 16S ribosomal RNA gene, partial sequence			NR_044044.1		97.9%/97.5%
  * Marinobacter gudaonensis strain SL014B61A 16S ribosomal RNA gene, partial sequence			NR_043796.1		97.5%
  * Marinobacter lipolyticus strain SM-19 16S ribosomal RNA gene, partial sequence			NR_025671.1		98.0%


Arenibacter 16S checks
* nr/nt
  * Flexibacter aggregans strain BSs20185 16S ribosomal RNA gene, partial sequence			DQ514301.1		99.9%
  * Flexibacter sp. BSs20182 16S ribosomal RNA gene, partial sequence					DQ514299.1		99.9%
  * Flexibacter aggregans gene for 16S rRNA, strain:IFO 15975						AB078039.1		99.9%
  * Arenibacter sp. MBE 61 16S ribosomal RNA gene, partial sequence					KF724487.1		99.4%
  * Arenibacter palladensis strain LMG 21972 16S ribosomal RNA gene, complete sequence			NR_042188.1		99.5%
  * Arenibacter troitsensis strain NBRC 101532 16S ribosomal RNA gene, partial sequence			NR_114004.1		99.4%

* refseq_genomic
  * Arenibacter algicola strain TG409 U735DRAFT_scf7180000000011_quiver.3_C, whole genome shotgun sequence	NZ_JPOO01000003.1	99.9% (x3)
  * Arenibacter palladensis strain DSM 17539, whole genome shotgun sequence				NZ_FQUX01000024.1	99.7%
  * Sediminicola sp. YIK13, complete genome								NZ_CP010535.1		93.7% + 93.2% + 93.2%

* 16S
  * Arenibacter palladensis strain LMG 21972 16S ribosomal RNA gene, complete sequence			NR_042188.1		99.5%
  * Arenibacter troitsensis strain NBRC 101532 16S ribosomal RNA gene, partial sequence			NR_114004.1		99.4%
  * Arenibacter echinorum strain KMM 6032 16S ribosomal RNA gene, partial sequence			NR_044271.1		99.4%
  * Arenibacter hampyeongensis strain HP12 16S ribosomal RNA gene, partial sequence			NR_109412.1		97.9%
  * Arenibacter troitsensis strain KMM 3674 16S ribosomal RNA gene, partial sequence			NR_024790.1		99.4%
  * Arenibacter nanhaiticus strain NH36A 16S ribosomal RNA gene, partial sequence			NR_116526.1		95.8%
  * Arenibacter latericius strain EI10 16S ribosomal RNA gene, partial sequence				NR_024893.1		92.9%
  * Arenibacter certesii strain KMM 3941 16S ribosomal RNA gene, partial sequence			NR_025747.1		93.6%

* Flexibacter aggregans > Flexithrix dorotheae

* All three sequences - pb_359_8, Arenibacter algicola (NZ_JPOO01000003.1) and Flexithrix dorotheae (AB078039.1) - align VERY well together
* Full tree - pb_359_8 assorts with Cellulophaga (sister to Arenibacter according to small tree); Flexithrix/Flexibacter same phylum (Bacteroidetes) but different
class (Cytophagia)
  * Most likely Arenibacter algicola

## To do

* 16S section of Results largely complete; round up and begin on analysis of pathway analysis

# 4 April 2017

## 16S

* pb_359_2
  * Roseovarius mucosus strain DFL-24 16S ribosomal RNA gene, complete sequence		NR_042159	99.8%
  * Roseovarius tolerans strain EL-172 16S ribosomal RNA gene, partial sequence		NR_026405	95.7%
  * Roseovarius marisflavi strain H50 16S ribosomal RNA gene, partial sequence		NR_125678	95.4%
  * **Roseovarius mucosus** is the obvious best match

* pb_359_3
  * Loktanella vestfoldensis DSM 16212 genomic scaffold H147DRAFT_scaffold000XX.XX	NZ_ARNL00000000 99.8%
  * Loktanella agnita strain R10SW5 16S ribosomal RNA gene, partial sequence		NR_043097	96.9%
  * Loktanella maritima strain KMM 9530 16S ribosomal RNA gene, partial sequence	NR_126190	95.6%
  * Loktanella salsilacus strain R-8904 16S ribosomal RNA gene, partial sequence	NR_025539	96.1%
  * Loktanella fryxellensis strain LMG 22007 16S ribosomal RNA gene, partial sequence	NR_025607	95.6%
  * Loktanella salsilacus strain NBRC 102486 16S ribosomal RNA gene, partial sequence	NR_114115	96.0%
  * **Loktanella vestfoldensis** is the obvious best match

* pb_359_4
  * Sphingorhabdus sp. M41, complete genome						CP014545	99.5%
  * Sphingopyxis flavimaris partial 16S rRNA gene, strain R-36742			FR691421	99.9%
  * Sphingorhabdus marina DSM 22363, whole genome shotgun sequence			NZ_FSQW01000002	97.6%
  * Sphingorhabdus pacifica strain n34 16S ribosomal RNA, partial sequence		NR_134813	95.6%
  * Sphingopyxis marina strain FR1087 16S ribosomal RNA gene, partial sequence		NR_043954	98.1%
  * **Sphingopyxis flavimaris** is the obvious best match (now **Sphingorhabdus flavimaris**)

* pb_359_5
  * See yesterday's results
  * Marinobacter salarius has 99.4%/99.5% similarity, but **Marinobacter algicola** has 99.8%/99.9% similarity
    * Some unnamed species have 99.9%/100% similarity

* pb_359_6
  * Sulfitobacter sp. SAG13 16S ribosomal RNA gene, partial sequence			KX268604			99.9%
  * Sulfitobacter pseudonitzschiae strain H3 16S ribosomal RNA gene, complete sequence	KF006321			99.2%
  * Staleya guttiformis gene for 16S ribosomal RNA, partial sequence, strain: R16	AB607871			99.2%
  * Staleya guttiformis gene for 16S ribosomal RNA, partial sequence, strain: R28	AB607880			98.8%
  * Sulfitobacter guttiformis strain PM-3 16S ribosomal RNA gene, partial sequence	JQ675546			98.5%
  * Sulfitobacter donghicola strain DSW-25 16S ribosomal RNA gene, partial sequence	NR_044164			97.2%
  * Sulfitobacter sp. 20_GPM-1509m N517DRAFT_scaffold00003.3_C, whole genome shotgun sequence	NZ_JIBC01000005		99.2%
  * Sulfitobacter pseudonitzschiae strain DSM 26824, whole genome shotgun sequence	NZ_FQVP01000024			99.2%
  * Sulfitobacter pseudonitzschiae strain H3 contig37, whole genome shotgun sequence	NZ_JAMD01000037			99.2%
  * Sulfitobacter donghicola contig23_scaffold23, whole genome shotgun sequence		NZ_JAMC01000023			97.2%
  * Sulfitobacter donghicola KCTC12864_contig5, whole genome shotgun sequence		NZ_JASF01000005			97.2%
  * Sulfitobacter donghicola strain DSW-25 16S ribosomal RNA gene, partial sequence	NR_044164			97.2%
  * Sulfitobacter dubius strain KMM 3554 16S ribosomal RNA gene, partial sequence	NR_025691			96.6%
  * Roseobacter litoralis strain Och 149 16S ribosomal RNA gene, complete sequence	NR_074143			96.0%
  * Sulfitobacter mediterraneus strain CH-B427 16S ribosomal RNA gene, partial sequence	NR_026472			96.6%
  * Sulfitobacter delicatus strain KMM 3584 16S ribosomal RNA gene, partial sequence	NR_025692			96.2%
  * Sulfitobacter geojensis strain MM-124 16S ribosomal RNA, partial sequence		NR_134204			96.3%
  * Sulfitobacter noctilucicola strain NB-77 16S ribosomal RNA, partial sequence	NR_134206			96.2%
  * Staleya guttiformis (Sulfitobacter guttiformis) a good hit, but so is **Sulfitobacter pseudonitzschiae** and that agrees with the PhyloPhlAn
    * Still only 99.2%... Sulfitobacter sp. SAG13 99.9%

* pb_359_7
  * See yesterday's results
  * **Antarctobacter heliothermus** is the obvious best match

* pb_359_8
  * See yesterday's results
  * Both Flexibacter aggregans (Flexithrix dorotheae) and **Arenibacter algicola** scored 99.9%, but A. algicola agrees with PhyloPhlan

## pb_359_6

Still unconvinced re: identity of pb_359_6, given only 99.2% 16S identity
* Create super-tree of ALL Rhodo species, named and unnamed
  * pb_359_6 is a sister species to the clade S. pseudonitzschiae + S. sp. 20_GPM-1509m


## To do
Add siderophore predictions to report table

# 5 April 2017


Check GC content of Marinobacter species vs. pb_359_5

Precedent for plasmids in Marinobacter/M. algicola?


# 6 April 2017

## To do today
* Check GC contents
* Precedent for Marinobacter/M. algicola plasmids?
  * Precedent for plasmids in Marinobacter, but not specifically in M. algicola

## GC content

* pb_359_2
  * Average 60.9%, chrom 60.9%, plas 60.1% + 58.3%
  * Roseovarius mucosus DSM 17069 - 61.9% (25 contigs/17 scaffolds)

* pb_359_3
  * Average 60.7%, chrom 60.8%, plas 57.4% + 58.2%
  * Loktanella vestfoldensis DSM 16212 - 61.8% (49 contigs/45 scaffolds)
  * Loktanella vestfoldensis SKA53 - 59.9% (14 contigs/3 scaffolds)

* pb_359_4
  * Average 58.0%, chrom 58.0%
  * Sphingorhabdus flavimaris - unknown
    * Sphingorhabdus marina - 57.4%
    * Sphingorhabdus sp. M41 - 56.7%

* pb_359_5
  * Average 57.0%, chrom 57.2%, plas 53.7%
  * Marinobacter algicola DG893 - 57.0%

* pb_359_6
  * Average 59.5%, chrom 59.5%, plas 58.4% + 58.8% + 58.4% + 56.8% + 60.3% + 60.7% + 58.9%
  * Sulfitobacter pseudonitzschiae H3 - 61.7%
  * Sulfitobacter pseudonitzschiae DSM 26824 - 61.7%
  * Sulfitobacter guttiformis KCTC 32187 - 56.1%

* pb_359_7
  * Average 61.5%, chrom 61.6%, plas 60.3% + 62.8% + 60.4%
  * Antarctobacter heliothermus DSM 11445 - 62.68%
  * Mameliella alba UMTAT08 - 65.0%
  * Mameliella alba CGMCC 1.7290 - 65.2%

* pb_359_8
  * Average 39.8%, chrom 39.8%, plas 43.8%
  * Arenibacter algicola TG409 - 39.7%
  * Flexithrix dorotheae DSM 6795 - 36.3%

## Genome sizes

* pb_359_2
  * Total 4,381,426, chrom 4,170,996, plas 180,135 + 30,295
  * Roseovarius mucosus DSM 17069 - 4,247,720

* pb_359_3
  * Total 3,987,360, chrom 3,836,950, plas 111,030 + 39,380
  * Loktanella vestfoldensis DSM 16212 - 3,721,600
  * Loktanella vestfoldensis SKA53 - 3,066,850

* pb_359_4
  * Total 3,479,724, chrom 3,479,724
  * Sphingorhabdus flavimaris - unknown
    * Sphingorhabdus marina - 3,547,930
    * Sphingorhabdus sp. M41 - 3,339,520

* pb_359_5
  * Total 4,630,160, chrom 4,386,892, plas 243,268
  * Marinobacter algicola DG893 - 4,413,000

* pb_359_6
  * Total 5,121,602, chrom 3,572,445, plas 428,095 + 292,917 + 284,777 + 209,222 + 142,107 + 99,245 + 92,794
  * Sulfitobacter pseudonitzschiae H3 - 4,945,290
  * Sulfitobacter pseudonitzschiae DSM 26824 - 4,951,640
  * Sulfitobacter guttiformis KCTC 32187 - 3,976,670

* pb_359_7
  * Total 5,331,190, chrom 4,723,013, plas 372,263 + 154,467 + 81,447
  * Antarctobacter heliothermus DSM 11445 - 5,174,374
  * Mameliella alba UMTAT08 - 5,837,380
  * Mameliella alba CGMCC 1.7290 - 5,258,330

* pb_359_8
  * Total 5,857,781, chrom 5,793,053, plas 64,728
  * Arenibacter algicola TG409 - 5,550,230
  * Flexithrix dorotheae DSM 6795 - 9,536,820


## Marinobacter

* pb_359_5 very similar to both M. algicola and M. salarius in terms of G+C content and assembly size
  * How do M. algicola and M. salarius compare to each other?
    * Similar but not perfectly identical...

| Trait                            | M. algicola                                        | M. salarius                              |
|----------------------------------|----------------------------------------------------|------------------------------------------|
| **Gram stain**                   | Negative                                           | Negative                                 |
| **Oxidase**                      | Positive                                           | Positive                                 |
| **Catalase**                     | Positive                                           | Positive                                 |
| Spore forming?                   | No                                                 | ?                                        |
| **Shape**                        | Rod                                                | Rod                                      |
| Size                             | 1.6-2.5 x 0.45-0.55 um                             | 1.9-3.2 x 0.40-0.72 um                   |
| Occurence                        | Single cells/pairs/short chains                    | ?                                        |
| **Motility**                     | Single, non-sheathed, polar flagellum              | Single polar flagellum                   |
| Growth in salt                   | 1-9%, 1-12% (optimal 3-6%)                         | 0.5-20% (none at 0% or 25%)              |
| **Temperature**                  | 5-40C (optimal 25-30C)                             | 4-40C (optimal 25-30C)                   |
| **pH**                           | 5-10 (optimal 7.5)                                 | 6-9 (optimal 7.5)                        |
| **Nitrate/nitrite reduction**    | Negative                                           | Negative                                 |
| **Aerobic growth**               | Positive                                           | Positive                                 |
| Anaerobic growth                 | With nitrate and acetate, not glucose              | ?                                        |
| **Hydrolysis**                   | Tweens 40 and 80 and starch, not gelatin or casein | Tweens 40 and 80 and starch, not gelatin |
| Urease                           | Strain-dependent                                   | ?                                        |
| Arginine dihydrolase activity    | Positive                                           | Negative                                 |
| **Indole activity**              | Negative                                           | Negative                                 |
| **B-glucosidase activity**       | Negative                                           | Negative                                 |
| **B-galactosidase activity**     | Negative                                           | Negative                                 |
| **Utilisation of glycerol**      | Positive                                           | Positive                                 |
| **Utilisation of D-fructose**    | Positive                                           | Positive                                 |
| Utilisation of D-glucose         | Positive                                           | Negative                                 |
| **Utilisation of maltose**       | Positive                                           | Positive                                 |
| Utilisation of D-mannitol        | Strain-dependent                                   | Negative                                 |
| Utilisation of sucrose           | Negative                                           | Negative                                 |
| Utilisation of citric acid       | Positive                                           | Negative                                 |
| Utilisation of DL-lactic acid    | Positive                                           | Positive                                 |
| Utilisation of cis-aconitic acid | Positive                                           | Negative                                 |
| Utilisation of D-gluconic acid   | Positive                                           | Negative                                 |
| Utilisation of L-alanine         | Strain-dependent                                   | Weakly positive                          |
| Utilisation of L-leucine         | Positive                                           | Weakly positive                          |
| Utilisation of L-phenylalanine   | Positive                                           | Negative                                 |
| Utilisation of L-proline         | Positive                                           | Positive                                 |
| Sole carbon/energy source        | n-hexadecane, n-tetradecane, other carbon sources  | ?                                        |
| Main fatty acids                 | C16:0 (22.0%-25.5%)                                | C16:01                                   |
|                                  | C16:1 w7 c/iso-C15:0 2-OH (19.5%-20.5%)            | C16:1 w7c                                |
|                                  | C18:1 w9c (9.7%-11.5%)                             | C18:1 w9c                                |
|                                  | C12:0 3-OH (8.7%-10.0%)                            | C18:1 w7c                                |
| Principal isoprenoid quinone     | Q-9                                                | ?                                        |
| G+C content                      | 54%-55% (NCBI says 57%)                            | 57.1%                                    |


Gene no.:  
_5 - 4,277  
algicola - 3,960  
salarius - 3,036



## To do
* Work on Marinobacter [species] SMR5 submission
* Email NCBI re: submission
  * Waiting on response...
* Check 16S on SILVA? Way to grab best hits?

* Check through descriptions of Marinobacter for one that matches pb_359_5 character profile
  * Double-check algicola and salarius papers for similar species with different flagellar structure?


# 7 April 2017

## Marinobacter

Search for description papers of Marinobacter species, and see if they match the profile of pb_359_5
* In particular, look for ones with a 'MF' (non-polar?) flagellum, and oxidase-negative

(* Marinobacter koreensis - 16Ss shorter, but only 0-2 differences in the matching regions
  * DQ097526.1 - 96% query cover, 2/3 mismatches, 0 gaps
  * AB274772.1 - 80% query cover, 0/1 mismatches, 0 gaps
  * JF789469.1 - 56% query cover, 1/2 mismatches, 1 gap

* Amylase +++ in pb_359_5, but starch not hydrolysed in M. koreensis)

* Redone capitals as far as M, start on N on Monday


# 10 April 2017

## Marinobacter
* MF = Multiple flagella
* Oxidase test perhaps not the most reliable indicator (level of blueness in the stain is subjective)

* Most common lipids in pb_359_5
  * 16:0
  * 16:1d?2
  * 18:1d9
  * 18:1d?1

* Narrowed down results to those species which don't specify 'single flagellum'
  * 16S vs nr/nt, top results for salarius, algicola, koreensis, adhaerens, similis; none in the shortlist...
  * refseq_genomic, top results for algicola, salarius, adhaerens, lipolyticus, similis, subterrani, etc... lipolyticus is on the shortlist
    * lipolyticus only 97.8% similar...
  * 16S DB, top results algicola, adhaerens, flavimaris, sediminum, salsuginis, gudaoensis, etc... sediminum is on the shortlist
    * sediminum only 97.1% similar...

* Double-check colours and the agar type associated with them (pb_359_5 grown on MA)

# 11 April 2017

## Marinobacter

* Compare Marinobacter guineae to pb_359_5
  * 16S - Massive 5' gaps in the alignment...
  * 

* Searches for 'variable flagellar number' always bring up eukaryotes and/or mutants, rather than wild strains

* Marinobacter lutaoensis has 'one to several' polar flagella; precedent for subspecies...?

* Searching random sequences of ~2000 bp in BLASTn (nr/nt)
  * First 1920 bases - M. salarius, 1 substitution
  * About 9000 bases in - M. salarius, 15 substitutions, 1 gap
  * About 100,000 bases in - M. salarius, 6 substitutions, 1 gap
  * About 200,000 bases in - M. salarius, 24 substitutions
  * About 1,000,000 bases in - M. salarius, 42 substitutions
  * About 2,000,000 bases in - M. salarius, 22 substitutions, 3 gaps
  * About 3,000,000 bases in - Only short hits
  * About 4,000,000 bases in - M. salarius, 95% identity, 97% query cover
  * Almost at the end - M. salarius, 36 substitutions, 1 gap

* Repeat with refseq_genomic
  * First 1920 bases - M. salarius, 1 substitution
    * M. algicola, 90% query cover, 93% identity
  * About 9000 bases in - M. salarius, 15 substitutions, 1 gap
    * M. algicola, 38 substitutions, 6 gaps
  * About 100,000 bases in - M. salarius, 6 substitutions, 1 gap
    * M. algicola, 100% query cover, 90% identity
  * About 200,000 bases in - M. salarius, 24 substitutions
    * M. algicola, 99% query cover, 93% identity
  * About 1,000,000 bases in - M. salarius, 42 substitutions
    * M. algicola, 99% query cover, 94% identity
  * About 2,000,000 bases in - M. salarius, 22 substitutions, 3 gaps
    * M. algicola, 100% query cover, 89% identity
  * About 3,000,000 bases in - Seems like a rearrangement has taken place; big gap in the middle where nothing is present... (490 to 1344 of the query)
  * About 4,000,000 bases in - M. salarius, 97% query cover, 95% identity
    * M. algicola, 100% query cover, 93% identity
  * Almost at the end - 33 substitutions, 1 gap
    * M. algicola, 99% query cover, 92% identity

  * Beginning of plasmid - No matches...
  * About 100,000 bases in - Marinobacter aquaeolei (now M. hydrocarbonoclasticus), 38% query cover, 75% identity
  * About 200,000 bases in - No matches...

* BLASTn results are starting to look like Marinobacter salarius rather than Marinobacter algicola

# 12 April 2017

## Marinobacter

See whether there are core genes/pathways that will help to distinguish between the two Marinobacter species
* Based on the fatty acid content, it appears most likely that pb_359_5 is M. salarius
  * Another M. algicola 'type strain', M. algicola LMG 23835T, apparently has similar fatty acid stats...

Identify unique pathways/proteins in M. algicola/salarius relative to each other, then see how many are shared by pb_359_5
* M. algicola seems to share more unique pathways and proteins with pb_359_5, but M. salarius has more hypotheticals, so could be an annotation issue

Based on the M. salarius announcement paper, compare gyrB and rpoD genes for each species vs. pb_359_5
* Identity score

|             | gyrB  | rpoD   |
|-------------|-------|--------|
| M. algicola | 99.4% | 99.7%  | (check DNA)
| M. salarius | 99.9% | 99.8%* |

* Similarity score

|             | gyrB | rpoD  |
|-------------|------|-------|
| M. algicola | 100% | 100%  | (check DNA)
| M. salarius | 100% | 100%* |

* rpoD of M. salarius has been pseudogenised; 1 bp missing ~2/3 of the way through the gene
  * Scores above reflect replacement of the deleted base

On the basis of other gene markers (see Sims_and_Diffs.md file), it was decided that pb_359_5 should be classified as **M. salarius**



## To do
Is it possible to copy certain elements of a Git repository into a new repository, but retain their version history information?

Begin process of registering BioSample for M. salarius SMR5

# 13 April 2017

## Marinobacter salarius strain SMR5
* BioSample submitted - SAMN06718375
* Next step: WGS
  * Put the sequence files through the relevant checks

* Consistency checker not working, but will attempt upload anyway and address issues if they are pointed out to me

* Reads submitted to SRA; need to generate additional files in SMRT Portal

## To do

* Edit tbl conversion script to remove notes containing 'note From *.gb' and 'inference Similar to *.fasta' lines

* Check pb_359_6 vs. Sulfitobacter pseudonitzschiae on gyrB, rpoB and rpoD for similarity, to determine if they are the same species

* Check PhyloPhlAn results including all Alteromonadaceae (REMEMBER TO INCLUDE E. coli AND E. albertii OUTGROUP!)

# 18 April 2017

## M. salarius SMR5
* Preparing to upload the supplementary material for this organism (pending accession no.)
  * Example command for ftp transfer from Albiorix to laptop:
    * rsync -hav matt@albiorix.bioenv.gu.se:/nobackup/data5/Skeletonema_marinoi_microbiome_project/SubmissionPreparations/MarSalSMR5/SRA/motif_summary.csv .

* Check PhyloPhlAn - Aside from M. salarius and M. algicola, M. sp. C18, M. sp. MCTG268, M. sp. HL-58 and M. lipolyticus were also found in the clade

* Try to find dmdD sequences from other Marinobacter species and BLAST against SMR5
  * crt appears to fill the hole, according to Pathway Hole Filler

## Species names
* pb_359_2 - Roseovarius mucosus - final designation
 * pb_359_3 - Loktanella vestfoldensis - very confident - check anyway
 * pb_359_4 - Sphingorhabdus flavimaris - fairly confident - CHECK REQUIRED
* pb_359_5 - Marinobacter salarius - final designation
 * pb_359_6 - Sulfitobacter pseudonitzschiae - fairly confident - CHECK REQUIRED
 * pb_359_7 - Antarctobacter heliothermus - fairly confident - CHECK REQUIRED
 * pb_359_8 - Arenibacter algicola - very confident - check anyway

* Find gyrB, rpoD and rpoB for all species
  * Cannot reliably identify rpoD in pb_359_; try again later?

* Search NCBI nucleotide database for Loktanella vestfoldensis rpoD, and go to the NZ_... contig and search for rpoD (may be under sigma subunit)
* Run pairwise alignment on pb_359_3 vs DSM 16212 and SKA53, then DSM 16212 vs SKA53, and note the results in the appropriate file in 05_results/pb_359_3
* Repeat the above for all species where possible

# 19 April 2017

## Marker genes
* pb_359_3 - relatively low scores (>90%) but within the bounds of two strains' similarity to one another
* pb_359_4 - only 16S available for Sphingorhabdus/Sphyngopyxis flavimaris, but this is a 99.9% similarity
  * CHECK LIPIDS?
* pb_359_6 - Marker genes were 100% identical between S. pseudoniitzschiae strains, but not identical to pb_359_6...
  * Check lipids, re-think classification...

* Complete pb_359_7/8

# 20 April 2017

## Marker genes
* pb_359_7 - Only partial sequences available for gyrB and rpoB from A. heliothermus DSM 11445; nothing from EL-219, and nothing for rpoD
  * Check lipids
* pb_359_8 - >99% identity on all three markers found; rpoD not found in pb_359_8, but the three sequences in A. algicola TG409 differ a lot from one another
  * Fairly confident on classification, but double-check lipids

## Strain designations

* SMR1 - Sulfitobacter (pb_359_6)
* SMR3 - Roseovarius (pb_359_2)
* SMR4r - Loktanella (pb_359_3)
* SMR4y - Sphingorhabdus (pb_359_4)
* SMR5 - Marinobacter (pb_359_5)
* (SMR6w - Maribacter; N/A)
* SMS3 - Antarctobacter (pb_359_7)
* SMS7 - Arenibacter (pb_359_8)

| Strain   | Prediction                     | Markers                                                                                                           |
|----------|--------------------------------|-------------------------------------------------------------------------------------------------------------------|
| pb_359_3 | Loktanella vestfoldensis       | 99.8% identity on 16S; ~90% identity on gyrB, rpoB and rpoD, but same as between L. vestfoldensis strains         |
| pb_359_4 | Sphingorhabdus flavimaris      | 99.9% identity on 16S; no other marker information available... (refseq_genomic BLASTn - best hit to S. M41)      |
| pb_359_6 | Sulfitobacter pseudonitzschiae | 99.2% identity on 16S; ~89%-93% identity on gyrB, rpoB and rpoD, but 100% between S. pseudo strains               |
| pb_359_7 | Antarctobacter heliothermus    | 99.5%/99.9% identity on 16S; 88.1% identity on gyrB, 92.6% on rpoB (both partial)                                 |
| pb_359_8 | Arenibacter algicola           | 99.9% identity on 16S; >99% identity on gyrB and rpoB (refseq_genomic BLASTn - best hits to A. algicola and C-21) |

* Re: G+C content - based on R. mucosus description paper, a G+C difference of +/- 2% appears to be acceptable between strains of the same species
  * On the G+C content basis, all of the predictions qualify

| Strain   | Prediction                     | Lipids                                                                      | G+C content                         |
|----------|--------------------------------|-----------------------------------------------------------------------------|-------------------------------------|
| pb_359_3 | Loktanella vestfoldensis       | Lipid composition similar to L. vestfoldensis AND L.salsilacus/fryxellensis | _3 = 60.8%; L. vest = 62.1% - 63.1% |
| pb_359_4 | Sphingorhabdus flavimaris      | Not perfect but somewhat comparable                                         | _4 = 58.0%; S. flavi = 58%          |
| pb_359_6 | Sulfitobacter pseudonitzschiae | ???                                                                         | _6 = 59.5%; S. pseudo = 61.7%       |
| pb_359_7 | Antarctobacter heliothermus    | Lipid composition similar to A. heliothermus (and other similar species)    | _7 = 61.6%; A. helio = 62.3%        |
| pb_359_8 | Arenibacter algicola           | Similar to A. algicola vs. other Arenibacter species, particularly C17:1    | _8 = 39.8%; A. algicola = 41.9%     |

| Strain   | Prediction                     | Other comparisons                                                             | Conclusion                   |
|----------|--------------------------------|-------------------------------------------------------------------------------|------------------------------|
| pb_359_3 | Loktanella vestfoldensis       | Correct shape + colour (colour variable among Loktanella)                     | Loktanella vestfoldensis     | *
| pb_359_4 | Sphingorhabdus flavimaris      | Correct shape + colour, growth temps slightly different (no genome available) | ?                            | *
| pb_359_6 | Sulfitobacter pseudonitzschiae | Correct shape + colour, similar growth temps, assembly size + gene no.        | ?                            | *
| pb_359_7 | Antarctobacter heliothermus    | Right shape, different colour, similar growth temps, assembly size + gene no. | ?                            | *
| pb_359_8 | Arenibacter algicola           | Correct shape + colour (same for a lot of Arenibacter...)                     | Arenibacter algicola         | *

* pb_359_6 stats, to compare with other Sulfitobacter species
  * G+C = 59.9%
  * Assembly size = 5,121,602 bp
  * CDS = 4,967
* No other Sulfitobacter species has such a large assembly size/so many CDS


* S. pseudo strains - where were the two taken from?
* Ns before/after Antarcto molecules to achieve same length of marker gene

* All species and strain names now decided

# 21 April 2017

* Double-check features of pb_359_2 and pb_359_5 for completeness

| Feature       | pb_359_2 vs R. mucosus                   | pb_359_5 vs M. salarius                                                       |
|---------------|------------------------------------------|-------------------------------------------------------------------------------|
| 16S           | 99.8% identity                           | 99.4/5% identity (99.9% vs. algicola)                                         |
| gyrB          | 99.0% identity                           | 99.5% identity (94.1% vs. algicola)                                           |
| rpoB          | 93.6% identity                           | 99.8% identity (95.6% vs. algicola)                                           |
| rpoD          | 92.7% identity (0.3% gaps)               | 99.5% identity (95.4% vs. algicola)                                           |
| Lipids        | Matches well (also to other Roseovarius) | M. salarius closest type strain; algicola non-type strain also close          |
| G+C           | 60.85% vs. 61.90%/62.9%/60.9%            | 57.0% vs. 57.1% (57.0% vs. algicola)                                          |
| Genome size   | 4.38 Mb vs. 4.24 Mb                      | 4.63 Mbp vs. 4.62 Mbp (4.41 Mbp vs. algicola)                                 |
| # of genes    | 4,101 vs. 3,790                          | 4,277 vs. 2,973 (+ 1,352 pseudogenes) (3,960 (+ 63 pseudogenes) vs. algicola) |
| Shape/colours | Pink/red rods vs. whitish/pink rods      | White rods vs. non-pigmented/creamy rods (creamy/beige vs. algicola)          |


## To do

WRITE UP A TUTORIAL (ALBIORIX WIKI) FOR NCBI SUBMISSION

UPDATE # of CDS and other features for R. mucosus in report

# 24 April 2017

## Antarctobacter

Genome size - 5,174,374 bp  
No. of protein-coding genes - 5197

## Alterations to be made to the pb_359_5 submission
* MARSALSMR5_00556 (cspA ncRNA) removed, as completely overlapped the subsequent cspC cold shock protein gene (which matches the one in the type strain)
* MARSALSMR5_01807 (cspA ncRNA) removed, as completely overlapped the subsequent cspA cold shock protein gene (which matches the one in the type strain)
* MARSALSMR5_02982 (cspA ncRNA) removed, as completely overlapped the subsequent cspE cold shock protein gene (which matches the one in the type strain)

* MARSALSMR5_02000 (bacteria_large_SRP) removed; two overlapping SRPs (large and small), and the bacteria_smalll_SRP is the same size as that in the type strain

* MARSALSMR5_00224 and MARSALSMR5_00225 merged as a pseudogene
* MARSALSMR5_00615 and MARSALSMR5_00616 merged as a pseudogene
* MARSALSMR5_01194 and MARSALSMR5_01195 merged as a pseudogene (frameshift)
* MARSALSMR5_02424 and MARSALSMR5_02425 merged as a pseudogene
* MARSALSMR5_02441 and MARSALSMR5_02442 merged as a pseudogene
* MARSALSMR5_03121 and MARSALSMR5_03122 merged as a pseudogene (frameshift)
* MARSALSMR5_04217 / MARSALSMR5_04218

Genome resubmitted

# 28 April 2017

## pb_359_5
Adjust figures based on the NCBI annotation
* Only the chromosome has been processed so far; email NCBI if plasmid has not been processed by the end of the day

# 2 May 2017

## pb_359_5
* Data has now been released; re-check figures for features

| Feature      | Chrom | Plas | Total |
|--------------|-------|------|-------|
| CDS (total)  | 3999  | 264  | 4263  |
| Pseudo       | 6     | 1    | 7     |
| Hypothetical | 577   | 178  | 755   |
| Named        | 2411  | 40   | 2451  |
| tRNA         | 51    | 0    | 51    |
| rRNA         | 9     | 0    | 9     |
| tmRNA        | 1     | 0    | 1     |
| ncRNA        | 10    | 1    | 11    |
| misc_binding | 0     | 0    | 0     |
| Pathways     | -     | -    | 

* Pathways at start - 261
* Pathways after manual assignment - 
* Pathways after Pathway Hole Filler - 

## To do
* Write Albiorix wiki page on NCBI submission
* Work on thesis
* Run enzyme assignment (make notes) and pathway hole filler on SMR5 (post-submission version)
* Get .fna and .faa files for each genome
* Look into making separate Git repositories for each species, inc. version history
* Upload supplementary data for MarSalSMR5 to NCBI (from a different computer?)
  * May need to reinstate the Aspira workaround for Firefox
* Complete Probable Enzyme Table for MarSalSMR5 post-NCBI check
* Re-download the .faa files for each species, but replace locus data with replicon name
  * One .fasta and .faa per species
  * http://rocaplab.ocean.washington.edu/tools/genbank_to_fasta

# 3 May 2017

## Useful command
* To add a pattern to the end of all fasta header lines
  * `sed '/^>/ s/$/pattern/' file`

## To do
* Write Albiorix wiki page on NCBI submission
* Work on thesis
* Look into making separate Git repositories for each species, inc. version history
* Upload supplementary data for MarSalSMR5 to NCBI (from a different computer?)
  * May need to reinstate the Aspira workaround for Firefox
* Plot bacterial genomes as a circle (see Zostera chloroplast supplementary from Nature)
* Loktanella genome submission

## Done

* Get .fna and .faa files for each genome
* Re-download the .faa files for each species, but replace locus data with replicon name
  * One .fasta and .faa per species
  * http://rocaplab.ocean.washington.edu/tools/genbank_to_fasta
* Run enzyme assignment (make notes) and pathway hole filler on SMR5 (post-submission version)
* Complete Probable Enzyme Table for MarSalSMR5 post-NCBI check
* Copy summary of all bacterial interesting features (inc. virus information) and send to Skeletonema group

# 4 May 2017

## pb_359_5

* Pathways at start - 261
* Pathways after manual assignment - 265
* Pathways after Pathway Hole Filler - 270

## Info to send to Skeletonema group
* Ensure that pb_359 names are replaced with species + strain names

* Information on interesting features (pathways + searches)
* Information on secondary metabolite analysis
* Information on viruses

* Information compiled and sent

## Remaining to-do list
* Write Albiorix wiki page on NCBI submission
* Work on thesis
* Look into making separate Git repositories for each species, inc. version history
* Upload supplementary data for MarSalSMR5 to NCBI (from a different computer?)
  * May need to reinstate the Aspira workaround for Firefox
* Plot bacterial genomes as a circle (see Zostera chloroplast supplementary from Nature)
* Loktanella genome submission

# 5 May 2017

List actual genes present in each pathway/search result - Done
Visualise Roseo + Lokta plasmids (and chromosome)

# 8 May 2017

## Circos
Circular visualisation software for genomes download
* Some issues with Perl modules on Windows; check where these are installed, so that the program can find them

# 9 May 2017

Finish formatting the last few thesis citations...

# 10 May 2017

Thesis work

# 11 May 2017

Thesis work

# 12 May 2017

Thesis work

# 15 May 2017

Thesis work

# 16 May 2017

## Thesis
Updated to version 1.1 of thesis

## Circos
* Open Perl command line and change directory
  * `cd C:\Users\matt_\Desktop\PROJECT\circos-0.69-5\bin`

* Downloading required modules, as trying to run Circos as-is fails
  * Requires CPAN module (found in Start folder for Strawberry Perl)
  * Modules installed

* Circos requires a .conf configuration file to specify what it is drawing
  * Research required syntax

* Tutorials downloaded; base syntax off of these?
  * Read tutorials/find course info from the website
  * http://circos.ca/tutorials/lessons/quick_guide/
  * http://circos.ca/documentation/course/

* Important first to know WHAT I'm intending to show...

# 17 May 2017

Thesis work

## M. salarius strain SMR5 paper
Added a few lines and references

## GitLab repository readme
Began updating the GitLab main readme

# 18 May 2017

Re-examine phosphate-related genes?
Interkingdom quorum sensing?
Choline uptake?
* Genes labelled 'choline transporter' present in some genomes; check gene names




Before summer: Get M. salarius paper submitted, and submit other genomes to NCBI
Pathway Analysis of S marinoi + Thalassosira and phaeo

Nature podcast - beneficial double knockout study (13 April)

Useful link: http://www.nature.com.secure.sci-hub.io/articles/nmicrobiol201665

# 19 May 2017

## Pathway Tools
Important note - Pathway Tools Cellular Overview poster output is in PostScript (.ps) format, so requires
a program such as EPS/PS Viewer to view and convert to a conventional image type

## Albiorix tutorial
Continue work on the NCBI upload tutorial, while amending the Loktanella files

# 22 May 2017

## Albiorix tutorial
Next - amend Loktanella files and then continue the tutorial with Step 5

# 23 May 2017

## Loktanella vestfoldensis
* "1635 genes overlap another gene on the same strand"!
* Need to BLASTx overlapping genes to identify pseudogenes...
* Run https://www.ncbi.nlm.nih.gov/genomes/frameshifts/frameshifts.cgi on all three contigs

# 24 May 2017

## Marinobacter salarius
Methylation data submitted via Albiorix
* `ssh -X -Y username@albiorix.bioenv.gu.se`
* `firefox &`

## Loktanella vestfoldensis
* Started methylation analysis of pb_359_3 ready for submission after genome is submitted
* NCBI submission portal is claiming that there are sequence gaps...
  * All sequences now accepted, unsure why it was claiming that there were gaps...
* Require sudo rights to copy the raw reads from /home/smrtanalysis

# 29 May 2017

Thesis work

# 30 May 2017

Thesis work

## To do
Investigate genes claiming to be for 'toxin coregulated pilus biosynthesis' on Marinobacter plasmid?
* May be wrongly-labelled secretion proteins, based on BLASTp of one of the genes

# 31 May 2017
Thesis work

## To do
Update Loktanella numbers on GitLab main README
* After Assign Probable Enzymes - 309 pathways
  * After Pathway Hole Filler - 317 pathways

New Loktanella figures post-NCBI submission:
* CDS - 3936
* Named - 2180
  * For finding named gene number in GenBank: `grep -A1 " CDS " filename.gb | grep "/gene=" | wc -l`
* Hypothetical - 669
* Pseudogenes - 8
* tRNA - 45
* tmRNA - 1
* rRNA - 6
* ncRNA - 19
* Misc. binding - 0
* Pathways - 317

Proteins with assigned function for each species:
* R. mucosus (pb_359_2) - 3542
* L. vestfoldensis (pb_359_3) - 3267
* S. flavimaris (pb_359_4) - 2530
* M. salarius (pb_359_5) - 3508
* S. pseudonitzsciae (pb_359_6) - 3919
* A. heliothermus (pb_359_7) - 3948
* A. algicola (pb_359_8) - 3515

# 1 June 2017

Thesis submitted

R. mucosus SMR3 genome announcement published

# 2 June 2017

Thesis re-submitted with amended genome announcement reference

## Immediate to-do list
* Finish thesis defence PowerPoint

## Future work
* Complete genome papers for Marinobacter and Loktanella
* Upload remaining genomes, starting with Sphingorhabdus
  * BioSample for Sphingorhabdus registered

## Useful time-saving tip for Falcon
If you want to rerun an assembly with slightly different settings, remove/rename the 2-asm-falcon folder and rerun the script;
the generation of preassembled reads etc. will be skipped

## Useful website for drawing plasmid genomes
http://ogdraw.mpimp-golm.mpg.de/index.shtml

## Priority - Assembly of the S. marinoi RO5 chloroplast (and mitochondria?)
### Chloroplast
* Make a Blast DB out of the contigs of RO5 (/nobackup/data5/Skeletonema_marinoi_genome_project/01_Assembly/FALCON_1.8.2/RO5/seed_read_10k/10_2-asm-falcon/)
* Query the database with the ST54 chloroplast genome (in home directory)
* See section 2.2 of https://www.nature.com/article-assets/npg/nature/journal/v530/n7590/extref/nature16548-s1.pdf regarding assembly of chloroplast genome
  * Assembly should have [end of IR region] [SSC region] [IR region] [LSC region] [start of IR region]
  * Once this has been identified, paste inversion of IR region onto the end of the LSC region, and trim front end of SSC
    * Start at beginning of first gene in SSC?

### Mitochondria
* Blast RO5 contigs vs. mitochondrial assembly from another diatom genome? (ST54 mito not available)

### BLASTn results
First BLASTn of ST54 chloroplast vs. RO5 database only got hits on a few small pieces of the chloroplast genome...
* Attempt with a_ctg? Or p_ctg + a_ctg combined database?


Search for bacterial respiration/sulfate-usage genes in Skeletonema genome

# 7 June 2017

Thesis defence complete!
* Check reasons for phosphatidylcholine's (and succinoglycan's) importance in bacteria-eukaryote interactions

## S. marinoi R05 chloroplast
* How similar are diatom chloroplast genomes - can they be compared between S. marinoi and other species?
  * [P. tricornutum and T. pseudonana (and Odontella sinensis) show similarities](https://doi.org/10.1007/s00438-006-0199-4)
    * "The chloroplast genomes of the pennate diatom Phaeodactylum tricornutum and the centric diatom Thalassiosira pseudonana have been completely sequenced
and are compared with those of other secondary plastids of the red lineage: the centric diatom Odontella sinensis, the haptophyte Emiliania huxleyi, and the
cryptophyte Guillardia theta. All five chromist genomes are compact, with small intergenic regions and no introns. The three diatom genomes are similar in gene
content with 127-130 protein-coding genes, and genes for 27 tRNAs, three ribosomal RNAs and two small RNAs (tmRNA and signal recognition particle RNA). All three
genomes have open-reading frames corresponding to ORFs148, 355 and 380 of O. sinensis, which have been assigned the names ycf88, ycf89 and ycf90. Gene order is
not strictly conserved, but there are a number of conserved gene clusters showing remnants of red algal origin. The acpP, tsf and psb28 genes appear to be on the
way from the plastid to the host nucleus, indicating that endosymbiotic gene transfer is a continuing process."

* BLASTn hits comparing ST54 chloroplast genome to database of RO5 contigs
  * Best matches
    * ~9.4 kb hit on a ~9.2 kb contig - complete contig
      * 000341F 000049492:E~000049492:E~000212722:B~000212722:B ctg_linear 9210 2224
    * ~7.4 kb hit (and ~1.5 kb hit) (slightly overlapped, so ~9 kb overall) on a ~9 kb contig - complete contig
      * 000342F 000112110:E~000112110:E~000157366:B~000157366:B ctg_linear 9024 3901
    * ~6.4 kb hit (and ~0.5 kb hit) (only slightly separated, so ~7 kb overall) on a ~12.7 kb contig - doesn't match complete contig...
      * 000317F 000104389:E~000035561:B~000070978:E~000070978:E ctg_linear 12755 8869
  * Okay matches
    * 2x ~1 kb hits on a ~46.6 kb contig - these are inverted - IR region? (Only 1 kb; how long is IR supposed to be...?)
      * 000198F 000187197:E~NA~000215021:B~000187197:E ctg_linear 46612 261070
  * Other matches
    * 33 bp hit on a ~1.3 mb contig
      * 000013F 000334707:B~000344960:E~000029879:E~000339826:B ctg_linear 1344556 6153684
    * 30 bp hit on a ~1.9 mb contig
      * 000002F 000266224:B~000210826:B~000175585:B~000235253:E ctg_linear 1932284 8825238

* Assuming that the three 'best match' contigs form the complete assembly (including areas not found by BLAST), this would give a ~20.7 kb construct
  * ST54 chloroplast 127 kb...
  * Adding the 'okay' match would only give a ~67.3 kb construct

* Other diatom chloroplasts contain ~160 genes (genes in the IR are only counted once)
  * ~4 overlapping genes
  * 0 introns
  * ~120 ATG start codons
  * ~5 GTG start codons

* BLASTn of RO5 contigs to self generates too big of an output file; try something else...

## RO5 mitochondrion
* **000198F 000187197:E~NA~000215021:B~000187197:E ctg_linear 46612 261070** appears to be a mitochondrial contig

## To do
Check the other two contigs of relatively low G+C content

# 8 June 2017

## S. marinoi organelles
* Start a Materials and Methods file in a new Git repository - done
  * See Zostera paper supplementary for structure (inc. SRL and other FALCON parameters, as these differ from the nuclear genome settings)
* Ensure that chloroplast can circularise (19x SMRT cells vs. reversed reference in SMRT Portal)
* Find diatom mitochondrial reference to check for S. marinoi mitochondrial genome
* Map Illumina reads
* Move on to annotation

* Check sequencing tech used for pre-existing S. marinoi mito genome; if Illumina, may have been difficulty resolving repeats, which would explain apparent
length diff vs. RO5
* Check for S. marinoi mito genome paper

* [Repeats in diatom mito genomes](http://www.sciencedirect.com/science/article/pii/S0378111911000527)

* Mito circ tests submitted along with chloro; check in morning

# 9 June 2017

All overnight SMRT Portal jobs failed due to lack of space
* Jobs - 16707, 16708, 16713, 16714, 16716, 16717
  * Compress and store these jobs elsewhere, then run them one at a time...
  * Inadequate permissions...
  * Enormous old microbiome project directory; tar and compress these files if possible
* Files have been compressed and moved to data5 - move to e.g. sparc1?
* Rerunning chloroplast reverse job; run jobs one at a time from now on
  * File sizes currently 80G (016719) and 16K (016720-016723)
  * Free space on partition1 - 232G

# 12 June 2017

* SMRT Portal (reverse) jobs have all run; is the coverage convincing...?
  * Re-running the short mitochondrial sequence (regular sequence) to check whether the full pattern is two peaks and one trough, or just one trough
    * Should be complete ~1pm

* sparc1 data11 - make microbiome folder, move old microbiome backups from data5 to new folder on sparc1 data11
  * Permission denied, will need to get access

* Check reads in SMRT View for chloro + mito, see if the low regions are consistently covered by full reads, if there are lots of errors, etc.
  * Chloroplast - lots of red in the trough and second peak, first peak fairly has only ~1 red read
  * Mito long - lots of red in the trough; some in the peaks
  * Mito short - lots of red in the trough; some in the peaks

* Rerun Falcon with different parameter values?
  * Top chloroplast hits were achieved with 20k SRL
    * 20k currently highest SRL; go higher?
  * Top mito hits were achieved with 15k SRL
    * But no better results were found in 20k...?


* Set Map QV threshold in SMRT Portal Resequencing?

* Coverage acceptable for chloroplast; realign so that sequence starts with start codon of first gene in SSR region?
* Check CPGAVAS + DOGMA (see Zostera paper) for annotation of chloroplast
  * DOGMA userid - Matt_Pinder2
    * PW - *maets*
  * CPGAVAS ID - 149725777623118
    * Results relatively consistent with expectations from T. pseudonana and P. tricornutum
      * Protein-coding genes - 125 (-10 = 115)
      * tRNA - 32 (-3/4 = 28/29)
      * rRNA - 6 (-3 = 3)
    * IR regions - ccsA to trnP-TGG OR rrn16S
      * Protein-coding genes - 10
      * tRNA - 3 or 4
      * rRNA - 3
    * Some inconsistencies exist between CPGAVAS and DOGMA results
      * CPGAVAS consistently includes extra codons at the end of a coding region cf. DOGMA
        * This could be the result of CPGAVAS including the stop codon *, and DOGMA not

* Mitochondrial genome coverage
  * Many low quality reads mapping to certain mito regions, inc. large predicted deletions...
  * Rerun Resequencing but set Mapping -> Maximum Divergence to 5%
  * Need ~100G on partition1 before I can safely run the analysis...
* Mitochondrial annotation?

## Chloroplast gene content
Conflicts between DOGMA and CPGAVAS

| Position | DOGMA                                      | CPGAVAS            |
|----------|--------------------------------------------|--------------------|
| ~8630    | Two tufA hits with possible infB within    | tufA               |
| ~10300   | -                                          | trnL-TAA           |
| ~19700   | ycf46                                      | -                  |
| ~21300   | rpl34                                      | -                  |
| ~26000   | -                                          | trnL-TAG           |
| ~26000   | rpl32                                      | -                  |
| ~26800   | -                                          | rrn5S              |
| ~31000   | ycf89                                      | -                  |
| ~32000   | -                                          | trnP-TGG           |
| ~34000   | ycf41                                      | -                  |
| ~39000   | ycf90                                      | -                  |
| ~42000   | secG overlapping ycf47                     | secG               |
| ~48000   | -                                          | trnS-GCT, trnI-CAT |
| ~48000   | ycf33                                      | -                  |
| ~49000   | -                                          | trnT-TGT           |
| ~52000   | psaM                                       | -                  |
| ~74000   | ycf45                                      | -                  |
| ~76000   | Three ycf42 hits with possible bas1 within | -                  |
| ~78000   | psbB overlaid on psi_psbT                  | psbB               |
| ~85000   | ycf16 overlaid on sufC                     | ycf16              |
| ~86000   | Two ycf24 hits with possible sufB within   | ycf24              |
| ~87000   | rbcLr and rbcSr                            | rbcL and rbcS      |
| ~90000   | psbX                                       | -                  |
| ~91000   | -                                          | trnR-CCG, trnM-CAT |
| ~92000   | petF                                       | -                  |
| ~97000   | -                                          | trnP-TGG           |
| ~98000   | ycf89                                      | -                  |
| ~104000  | -                                          | rrn5S              |
| ~104000  | rpl32                                      | -                  |
| ~104000  | -                                          | trnL-TAG           |
| ~109000  | rpl34                                      | -                  |
| ~110000  | ycf46                                      | -                  |
| ~116000  | thiS and ycf40 hits overlaid               | -                  |
| ~117000  | psb28                                      | -                  |
| ~117000  | -                                          | psbW               |
| ~124000  | ycf88                                      | -                  |
| ~126500  | -                                          | rpl29              |


* Line up RO5A chloroplast genome to match ST54, using the ST54-cp header as reference (incl. info such as SRL and other settings, location of features?)
* Compare the two sequences to determine why there is an 84 bp disrepancy (and then check for seq. errors)
  * Aligning ST54 and RO5A reveals that there are no massive gaps to account for the discrepancy; biggest gaps are only 4bp each
  * Rerunning CPGAVAS with realigned sequence: ID no. 149727885030125
    * Once complete, this should be saved as a GenBank file and drawn as a circle using OGDraw
  * Rerunning DOGMA with realigned sequence: saved under Matt_Pinder2 login

* Chloroplast genome (realigned) to be uploaded to genome browser for use at the jamboree; check file requirements (GFF or GBK?)
* Take another look at the mitochondrial genome(s)...
  * Get some kind of annotation...

# 13 June 2017

## Mito genome
Rerunning (short) mito genome using 5% divergence threshold
* Entirely unsuccessful...

* Regarding the preliminary sequences, after corrections the new lengths are:
  * Long - 46,734 bp
  * Short - 46,377 bp
* Most of this difference appears in large blocks of gaps
  * Compared to JK029 mitochondrion (from Korea) - only 38,515 bp
  * RO5 samples show 31.3% G+C, JK029 shows 29.7%

## Organelles
Copied files to data5 Skeletonema_marinoi_genome_project, under 08_RO5_Organelles
* Files for the genome browser being saved under 08_RO5_Organelles/Chloroplast/Files_for_Browser

* Files were using un-corrected reads... redownload and rerun
  * Genome length now 127,193 - only 13 bp shorter than ST54
  * Reannotating
    * CPGAVAS - 149734343341758
    * DOGMA - RO5_Chloroplast_Corrected_and_Realigned

* BLAST search highlighted sequences close to mito of JK029
  * Matches lower down the rankings may be the most accurate if the sequences are suitably diverged
  * Retry with some other hits...
    * Seed read 12k - 000272F 000003247:E~000116290:E~000099470:E~000003247:E ctg_linear 41646 198742
  * Try rerunning the FALCON assemblies with higher SRL?

* Attempting a preliminary annotation of mito genome with DOGMA produced very poor results...
  * Attempting with MITOFY... Poor results again

* Start manual curation of chloroplast genome

# 14 June 2017

Jamboree Day 1

# 15 June 2017

Jamboree Day 2
* Examine coverage for primary vs. associated contigs on S. marinoi genome?

# 16 June 2017

Jamboree Day 3

# 19 June 2017

Priority - bacterial genomes or chloroplast?
* Work on mitochondrion when memory allows

* Compare cp intron-including gene models vs. transcript
* Note which contigs of the reference genome assembly are from the chloroplast
* Upload results to Git
* Read mapping
* Once annotation is ~complete, generate GenBank and run through OGDraw

* Mito next week
* Bacteria over the summer

* Investigate possible LSC flippage vs. T. pseudonana
  * Identify boundary
  * DONE - Look at ycf1? - not apparently present
  * DONE - Attempt to locate ffs (signal recognition particle RNA) after dnaB
  * DONE - Attempt to locate ssra (tmRNA) between psbV and rpl19
  * rRNA sequences out of sync with one another vs. T. pseudonana

* CHECK ORIENTATIONS OF RRNAs
* Write findings + M&M section
* MAUVE analysis

# 21 June 2017

Additional annotation notes:
* First trnM-CAT (~61,000) appears to be false positive as too long and not present in T. pseudonana (or S. costatum apparently)
* Determine orientation of rRNAs
* Prokka labels ycf46 as ftsH - investigate
* Prokka labels rbcR as cysL - investigate
* Prokka labels ycf39 as azoB - investigate
* psbL not predicted by Prokka...
* ycf33 not predicted by Prokka...
* Check sequences, e.g. of ftsH (~63,000)
* rpl33 not predicted by Prokka...
* Prokka labels dnaB as dnaC - investigate
* Prokka labels atpD as atpH - investigate
* Prokka labels atpH as atpE - investigate
* Prokka labels atpI as atpB - investigate
* 

trnL-CAA missing  
trnL-TAG present instead (twice)  
2 trnM-CAT (outside of repeat region!)  
Repeat region - trnP-TGG, trnI-GAT, trnA-TGC, trnL-TAG  
trnI-CAT -> trnM-CAT?

Run chloroplast genome through Prokka to get second opinion on the tRNAs?
* Prokka supports current rRNA orientation
How to verify tRNAs and rRNAs



In S. marinoi, check region:
* trnP-TGG and psaJ (44742-45057)
* psaA and trnP-TGG (97727-109102)

In T. pseudonana, check region between:
* psaJ and trnP-TGG (65074-65404)
* trnP-TGG and psaA (128661-2401)


Cut point 44887-44888 and 108953-108954, about 75bp from trnP-TGG

Deletions:
* T deletion @ 70,127-70,128 (rpl33)
* A deletion @ 71,629-71,630 (rpoB)
* T deletion @ 117,274-117,275 (rbcR)
* T (or C) deletion @ 122,109-122,110 (ycf46)

Inverted repeats between trnP-TGG and ccsA

BLASTp all protein sequences 'to identify obvious errors'

Decrease MAUVE resolution for general overview?
* DL Fragilariopsis and MAUVE align with the others (+ Phaeo)
  * DL other diatom genomes
  * Individual RO5 alignments?
* Are there any genes on the break point where the inversion occurs?

# 22 June 2017

Get other diatom cp-genomes
* Fragilariopsis cylindrus (FIND!)
* Pseudo-nitzschia multiseries
* Eunotia naegelii
* Fistulifera solaris
* Didymosphenia geminata
* etc...

-----
T. pseudonana

cgtaaa ataaaaaact ctaataaaaa  
ttcgctaatt attgtttatt aacagtgtaa tttaattgta agacaaaaaa ttgt

acaatttttt gtcttacaat taaattacac  
tgttaataaa caataattag cgaattttta ttagagtttt ttattttacg

-----

In T. pseudonana, the 80 bp leading from trnP-UGG to the end of the IR is the same (albeit inverted) in both instances
* Check vs. S. marinoi
* In P. tricornutum, this region is 110bp long

-----

Phaeo

a gtcaaagact cattaaattg aagttttcaa aatacccaca  
cccatgataa cgaatttctt gaaattagac aaggtttaaa attgttttga aaattctaag  
caagaatta

taattc ttgcttagaa ttttcaaaac aattttaaac cttgtctaat  
ttcaagaaat tcgttatcat gggtgtgggt attttgaaaa cttcaattta atgagtcttt  
gact

-----

* Low 'unmatched' areas of RO5 vs T. pseudonana in MAUVE correspond to the IR - why?

Suspected extent of IR:
* IRa (ends with rps16) - 108,954 - 4 (18,244 bp)
* IRb - 26,640 - 44,887 (18,248 bp)

Thalassiosira pseudonana's IR region is 18,337 bp, so this would appear accurate

* RO5 SSC - 26,635
* RO5 LSC - 64,066

Total length - 127,193

-26,635----18,248----64,066----18,244-

| Feature | RO5           | T. pseudonana | P. tricornutum |
|---------|---------------|---------------|----------------|
| Genome  | 127,193       | 128,814       | 117,369        |
| IR      | 18,244/18,248 | 18,337        | 6,912          |
| SSC     | 26,635        | 26,889        | 39,871         |
| LSC     | 64,066        | 65,250        | 63,674         |

* Any other mention of non-identical inverted repeats?

* ST54 IRs same length and identical...

# 26 June 2017

Why is MAUVE not showing similarity in the inverted repeat regions?
* Align the repeats of RO5 and T. pseudonana (and P. tricornutum)
* Regions to align (approximate)
  * RO5 - 30,456 - 44,726 / 108,894 - end
  * T. pseudonana (realigned) - 30,743 - 45,301 / 110,618 - end
  * P. tricornutum (realigned) - 27,200 - 37,256 / 100,370 - end
* Trimming one IR from the end of the sequence fixes the issue (see 'Conserved Gene Order and Expanded Inverted Repeats
Characterize Plastid Genomes of Thalassiosirales')
  * Using mauveAligner instead of progressiveMauve (mauveAligner used in other chloroplast papers) shows the inverted repeats
aligned incorrectly UNLESS one is removed as above...

* T. pseudonana (unaligned) region to include: 83581- + -65250

* Does IR overlap the RO5 wraparound? i.e. Does it include part of rps16?
  * IR extends 4bp into rps16 (cf. 8bp in T. pseudonana)

* New limits for IRs in RO5
  * IRa (ends with rps16) - 108,954 - 4 (18,244 bp)
  * IRb - 26,640 - 44,887 (18,248 bp)
  * Numbers above corrected

| Feature | **IR can't overlap gene**   | IR can overlap gene              |
|---------|-----------------------------|----------------------------------|
| SSC     | 1 -> 26,643 = 26,643        | 5 -> 26,639 = 26,635             |
| IRb     | 26,644 -> 44,887 = 18,244   | 26,640 -> 44,887 = 18,248        |
| LSC     | 44,888 -> 108,953 = 64,066  | 44,888 -> 108,953 = 64,066       |
| IRa     | 108,954 -> 127,193 = 18,240 | 108,954 -> 127,193 -> 4 = 18,244 |
|         | Accept for now              |                                  |


Can't access SMRT Portal...
* When available, try to delete failed jobs to make room for mitochondrial analyses

* Q1 - Does the SSC region start with the stop codon of rps16, or does it start 5bp into the gene?
  * Appear to be some instances of a chloroplast gene straddling this boundary (e.g. T. pseudonana)
* Q2 - Should one IR be removed from MAUVE alignment in order to show the alignment of the IRs?
  * When old MAUVE is used and one IR isn't removed, MAUVE aligns them in reverse... 

* Cut each sequence to start with the SSC (disregarding the gene overlap), and removing IRa
  * RO5 (aligned to rps16)	- 5 -> 108,953 (108,949 bp)
  * T. pseudonana (unaligned)	- 83,589 -> 128,814 -> 65,250 ()
  * P. tricornutum (unaligned)	- 70,587 -> 117,369 -> 63,674 ()

* Unless P. tricornutum can be included and the IRs remain, use OLDMAUVE_RO5_Thala

* **Double-check and tidy up RNA start/stop**




(* Check reasons for phosphatidylcholine's (and succinoglycan's) importance in bacteria-eukaryote interactions)

## Mitochondrial assembly attempt
* Trying a 17k SRL mito assembly
  * overlap_filtering_setting = --max_diff 70 --max_cov 110 --min_cov 5 --bestn 10 --n_core 6
  * Good hit: 000019F 000024568:E~000030828:B~000005413:B~000024568:E ctg_linear 41543 158632

* Trying a resequencing based on another potential hit from 12k SRL data set
  * 000272F 000003247:E~000116290:E~000099470:E~000003247:E ctg_linear 41646 198742

* Would running one of the Resequencing results through Resequencing again be able to confirm if the result from before was accurate?
  * Before - After
    * Short (16723): 46611 - 46377
    * Long (16721): 46929 - 46734
    * Third (16730): 43570 - 43595

* Others to try from pre-existing assemblies?:
  * Length 46612 - number_5
  * Length 47628 - number_4
  * Length 41543 - 17k_1

## To do
* Check on new mitochondrial assembly attempt - FALCON
* Check on mitochondrial circularisation attempt - SMRT Portal
  * Should one of the previous attempts be rerun as a further polishing attempt?
* Check all chloroplast RNAs vs. T. pseudonana

# 27 June 2017

## Chloroplast
* tRNAs seem to line up with T. pseudonana
* rRNAs seem to line up with T. pseudonana
* ssrA seems to line up with T. pseudonana
* ffs seems to line up with T. pseudonana
  * Sequences should be BLASTed, as there appear to be substitutions...

* PROKKA predicts ccsA to be much longer; investigate
  * May be other examples
    * psbC
* DONE - Add locations of IRs, SSC and LSC
* DONE - Revise locus tags (renumber to include those skipped by PROKKA)
* Check product names/sequences
* DONE - Add gene names to tRNAs?
* Make final decision on strange trnM-CAT

## Mitochondrion
Circularisation attempt in SMRT Portal poor...

Running new attempts:
* number_4 - job 16736 (done)
* number_5 - job 16737 (check tomorrow)
* 17k_1 - job 16738

## TO DO
* RETRY OGDRAW WITH CHLORO_RO5.GBK
* Check number_5 job and kick off 17k_1 job
* Investigate remaining issues with chloroplast annotation

# 28 June 2017

## Mitochondrion
* Number 4	- Still an area of low coverage, though off to one side...
* Number 5	- Still an area of low coverage in the centre
* 17k_1		- Not terrible but still questionable...

* Starting 17k_2 (overlap_filtering_setting = --max_diff 400 --max_cov 2200 --min_cov 5 --bestn 10 --n_core 6)
* Good hit same stats as previous run - 000022F 000024568:E~000030828:B~000005413:B~000024568:E ctg_linear 41543 158632
  * 17k_1 -				000019F 000024568:E~000030828:B~000005413:B~000024568:E ctg_linear 41543 158632

* Starting 17k_3 (overlap_filtering_setting = --max_diff 800 --max_cov 1200 --min_cov 5 --bestn 10 --n_core 6)
* Good hit same stats as previous runs - 000021F 000024568:E~000030828:B~000005413:B~000024568:E ctg_linear 41543 158632

* Switch to 18k?
  * 18k job running...

* In SMRT Portal, running a re-reversed second Quiver of 17k_1, after first run (16743)
  * Consider running the direct output of first round as well?
    * Dip is in the centre so long reads needed to correct the trough...
  * Second round appears to have improved coverage. Try one more round?

* Run an annotation on the current mitogenome (Prokka?) and see WHERE the problem area is
  * Problem area does appear to be repeat region; align multiple assembly attempts and see whether this accounts for all potential errors
* Experiment with 18k SRL Falcon once it has finished
  * Try other parameter values for 17k (not ones taken from the previous experiments which gave identical results to one another...)

# 29 June 2017

## Mitochondrion
Aligning corrected sequences to see whether the coverage dips are consistently in the repeat region (6kb - 6.1kb into the sequence of 17k_1_quiver2)
* 17k_1_quiver2 used as reference (41,522 bp)
  * vs. 17k_1 (41,522 bp)	- Same length, 2 gaps...
  * vs. Short (46,377 bp)	- Big gap at 7,196 (on 17k_1), of around 5kb, with a few smaller gaps after
  * vs. Long (46,734 bp)	- One ~50bp gap at 4,649 (on 17k_1), then big gap at 5,338 of around 5kb
  * vs. Third (43,595 bp)	- Big gap at 5,320 (on 17k_1), of around 2kb
  * vs. Fourth (47,656 bp)	- Big gap at 7,196 (on 17k_1), of around 6kb
  * vs. Fifth (46,365 bp)	- Big gap at 7,196 (on 17k_1), of around 5kb, with a few smaller gaps after
* Aligning these large multi-kb gaps shows that the gaps are, indeed, repeats
  * In reference, spans from 4,458 (or 4,533) - 7,196

* 18k attempt also started - job 16746 - still a dip in the repeat region (41,521 bp)
  * Three diffs vs. 17k_1_quiver2
* 19k attempt waiting to start - job 16747 - big, strange dip in repeat region (38,922 bp)
* Rerunning 17k_1 in Resequencing but with 10k minimum polymerase read length - job 16748 - still a dip in the repeat region (41,521 bp)
  * Three diffs vs. 17k_1_quiver2


* "In T. pseudonana, the enzyme that catalyzes the first step of the urea cycle [carbamoyl phosphate synthase (CPS III)]
   appears to be targeted to mitochondria (table S4)"
  * http://science.sciencemag.org/content/306/5693/79
  * No apparent evidence of CPS in S. marinoi mitochondrial genome
    * Possibly in P. tricornutum

* Run another job through Quiver a second time to determine where issues lie - indels in the genome or just the repeat region?
  * Run third through Quiver again - closest in length to T. pseudonana - Job 16750
    * Maybe run fourth through later as it is the longest? - Job 16751

* Repeat sequence	- GAAACACGATTTGAGCCTTATAGGGTACCATATAATGCATTATGGCTTAGACCCTTATAGCATAAGGCTCTGTT
  * Possibly		- GAGCCTTATAGGGTACCATATAATGCATTATGGCTTAGACCCTTATAGCATAAGGCTCTGTTGAAACACGATTT
* In T. pseudonana	- GAGGTCCGATTTAAGCCGTTTGTAGAACGGATATTTCACACTATGTGAAATACCCGTTTGTAGAACGGGTATTTT
  * Reportedly		- AAGCCGTTTGTAGAACGGATATTTCACACTATGTGAAATACCCGTTTGTAGAACGGGTATTTTGAGGTCCGATTT


* When done, compare quiver2 Third (16750) with quiver2 17k_1
  * Do the same for quiver2 Fourth (16751) as well


## Preliminary annotation
* Loci 5 and 6 (subunit L) appear to be two parts of the same protein?
* 13-15 false positive?
* 16 and 17 (subunit N) appear to be two parts of the same protein?
* 40 and 41 (subunit H/8) appear to be two parts of the same protein?
* 32 false positive?
* 55-57 (chain 3/subunit G) appear to be three parts of the same protein?
* 62 and 63 (chain 5) appear to be two parts of the same protein?
* 64 and 65 (subunit D) appear to be two parts of the same protein?
* 66 and 67 (cytochrome b) appear to be two parts of the same protein?
* 70 false positive?
* Check wraparound...

# 30 June 2017

## Mitochondrion assembly

* 10k polymerase attempt yielded no better results - increasing to 35k
* Round 2 quiver of Third and Fourth complete; compare to 17k_1
  * Even after second round of quiver, discrepancies still remain between the three attempts (half a dozen single bases outside of the repeat region)

* Deleted some old jobs to make room
  * Low_Max_Div_RO5_Mito_Short_Circ_Test_Reverse_Attempt_2 (ref: RO5_Mito_short_Reverse, Maximum divergence 5%)
  * RO5_Mito_Fifth_Circ_Test_Reverse_2 (ref: RO5_Mito_Fifth_Reverse, normal parameters)

* Currently most-used template - 17k_1 - may be causing reads spanning the true length of the repeat region to be discarded
  * Retry 35k polymerase cutoff analysis with Third and Fourth, in case one of these represents the correct length


* Sequences flanking repeat region (search term for preassembled reads?) 48 ----- 81
  * TTCCCCTTATATTATGATCAAAATTTGAAAAAAGGAAAAAACACTATT ---------- AATAGAGCCTTATGTTATAAGGGTTTGTGTCATAATGCATTACATGTTCCTGAATCCTAGATTAAACTATACCGAGAAAAA
  * TTTTTCTCGGTATAGTTTAATCTAGGATTCAGGAACATGTAATGCATTATGACACAAACCCTTATAACATAAGGCTCTATT ---------- AATAGTGTTTTTTCCTTTTTTCAAATTTTGATCATAATATAAGGGGAA
    * Need better flanking region than the 48mer...
     * 70bp a little upstream
     * CCGGCCCGGTTCCCGGCCCGGTTCCCGGCCCGGTTCCCGGCCCGGTTCCCGGCCCGGTTCCCGGCCCGGT
     * Still nothing...


* grep against /nobackup/data5/Skeletonema_marinoi_genome_project/00_Data/pb_354/subreads_from_resequencing_on_Albiorix/filtered_subreads_NO_ADAPTER.fasta ?
  * 2.3m raw reads...
  * 275.3m lines...
  * BLASTn using database of S. marinoi raw reads

## Mitochondrion annotation

* Mito uses translation table 4, not 11. Specify this in another Prokka run
  * This made minimal difference; only the addition of some Ws to the ends of genes (one gene name added, one tRNA identity switched?)




## Chloroplast

Compare 'pseudogenes' with other diatom cp-genomes in NCBI
* Check rpl33, rpoB and ycf46
  * Also check lengthened rbcR (also vs. rbcR')
* rpl33 (9aa), should be 195bp
  * MAKIKVLEY
* rpoB (187aa), should be 4149bp
  * MNYTTALPDFIEMQRVSFCWFIAQGLNEELTSFSRIYDFSQNTEYILFGQEYSLVKPVYNIVRAKKYTAN
    YSAQLVIPLEVRNKKTNIIKYHSKFPIINLPLMTSSATFVINGCERVIVSQIIRSPGVYFEKNKHQKKNK
    KVKRVISSEIGKLKNFTPPSEILPTESRLYFLKSRVKKKLISDKKRK
  * Contradiction with transcript data...
* ycf46 (388aa), should be 1494bp
  * MKFTDELTLLLKARYPIIYINTIEEDRVEYIIRKYIKTSLNRSIYSWDFIDGYTNNPNNEGFAKRNPVQA
    LELVERLTAQTPALFLLKDFNRFLTDVSISRKLKNISRILKLQPKTIIIIGSDLNIPKELYDLITVLQFQ
    LPVESEINYELKRLIDSLNIEIEPQVLESLTRACQGLSLERIRRVLSKIIATYKTIDENSINLLLNEKKQ
    IISQTEILEYWSANETISKIGGVDNLKNWLKKRKTSFGIQASNYGLPTPRGLLLVGIQGTGKSLTAKAIA
    TEWQLPLLKLDVGKLFGGIVGESESRLRQMIEVAETISPCILWIDEIDKAFSNNVNTGDSGTSNRVLATF
    ISWLSEKTKPVFVVATANNVELLPLEIIRKGRFDEIFF
  * ycf46' (497aa)
    * MKFTDELTLLLKARYPIIYINTIEEDRVEYIIRKYIKTSLNRSIYSWDFIDGYTNNPNNEGFAKRNPVQA
      LELVERLTAQTPALFLLKDFNRFLTDVSISRKLKNISRILKLQPKTIIIIGSDLNIPKELYDLITVLQFQ
      LPVESEINYELKRLIDSLNIEIEPQVLESLTRACQGLSLERIRRVLSKIIATYKTIDENSINLLLNEKKQ
      IISQTEILEYWSANETISKIGGVDNLKNWLKKRKTSFGIQASNYGLPTPRGLLLVGIQGTGKSLTAKAIA
      TEWQLPLLKLDVGKLFGGIVGESESRLRQMIEVAETISPCILWIDEIDKAFSNNVNTGDSGTSNRVLATF
      ISWLSEKTKPVFVVATANNVELLPLEIIRKGRFDEIFFLDLPQKQEREQIFKIHIQEFRPNRWESFDYSK
      LAQLSDSFSGAEIRQSIIEAMYHAFYEKREFTTEDICLALTQLIPLSQLENDQTLKLKNWAVSGRIRLAS
      SKIIPMN
* rbcR (310aa), 933bp 
  * MVLPFTLQQLRIFKAIASEKSFTQAAEILFVSQPSLSKQIKTLENRLGILLLNRTGNKIFLTEAGIVFLQ
    YAERILALCEESCRALNDLKDGERGNLKVGASQTIGAYLMPRVLTLFAQSYPQINLNIDIDSTRIIAKKV
    ADRIIDIAIVGGDIPTGLKKNLEIEDFVEDELILIIPKSHPFARKKKKKISKEDLYHLNFITLNSNSTIH
    KFIDNILIQNNIQTKQFNTIMELNSIEAIKTAVSLGLGAAFVSSSSIEKEIELKTVEIITIENIKITRTL
    SIITNTDSHRSKAFDFFIMNYGYLKTYNFI
  * rbcR' (307aa), 924bp
    * MVLPFTLQQLRIFKAIASEKSFTQAAEILFVSQPSLSKQIKTLENRLGILLLNRTGNKIFLTEAGIVFLQ
      YAERILALCEESCRALNDLKDGERGNLKVGASQTIGAYLMPRVLTLFAQSYPQINLNIDIDSTRIIAKKV
      ADRIIDIAIVGGDIPTGLKKNLEIEDFVEDELILIIPKSHPFARKKKKKISKEDLYHLNFITLNSNSTIH
      KFIDNILIQNNIQTKQFNTIMELNSIEAIKTAVSLGLGAAFVSSSSIEKEIELKTVEIITIENIKITRTL
      SIITNTDSHRSKAFDFFYNELWLLKNL



## To do
Extract the reads from S_marinoi_raw_reads which hit the end 81mer, and see where they start/end - align them?
* Find out why they don't appear to hit the section at the start of the repeat...

# 3 July 2017

## Mitochondrion

Use fp.py to grep the best hits to the reverse sequence

(* Sequences flanking repeat region (search term for preassembled reads?) 48 ----- 81
  * TTCCCCTTATATTATGATCAAAATTTGAAAAAAGGAAAAAACACTATT ---------- AATAGAGCCTTATGTTATAAGGGTTTGTGTCATAATGCATTACATGTTCCTGAATCCTAGATTAAACTATACCGAGAAAAA
  * TTTTTCTCGGTATAGTTTAATCTAGGATTCAGGAACATGTAATGCATTATGACACAAACCCTTATAACATAAGGCTCTATT ---------- AATAGTGTTTTTTCCTTTTTTCAAATTTTGATCATAATATAAGGGGAA
    * Need better flanking region than the 48mer...
     * 70bp a little upstream
     * CCGGCCCGGTTCCCGGCCCGGTTCCCGGCCCGGTTCCCGGCCCGGTTCCCGGCCCGGTTCCCGGCCCGGT
     * Still nothing...)

* No good alignment; check whether the sequences span the repeat region

* Two sequences seem to span the repeat region, albeit with different numbers of repeats
  * ~108 repeats found in m160810_080809_42203_c101084512550000001823238903091755_s1_p0/93737/11172_21805
  * ~103 repeats found in m160907_093109_42203_c101088662550000001823265803091707_s1_p0/59477/0_17561

* Check results of Upstream_Test



## Sphingo

Check NCBI consistency checker re: SphFlaSMR4y

# 4 July 2017

Find instances where both downstream and (one of the) upstream sequences hit the same read
* Upstream_1
  * m160810_080809_42203_c101084512550000001823238903091755_s1_p0/93737/11172_21805
  * m160907_135022_42203_c101088552550000001823265803091740_s1_p0/84347/631_10058
* Upstream_2
  * m160809_233148_42203_c101084512550000001823238903091753_s1_p0/98665/14321_28605
  * m160907_093109_42203_c101088662550000001823265803091707_s1_p0/59477/0_17561
  * m160907_135022_42203_c101088552550000001823265803091740_s1_p0/84347/631_10058

* m160810_080809_42203_c101084512550000001823238903091755_s1_p0/93737/11172_21805
* m160907_135022_42203_c101088552550000001823265803091740_s1_p0/84347/631_10058
* m160809_233148_42203_c101084512550000001823238903091753_s1_p0/98665/14321_28605
* m160907_093109_42203_c101088662550000001823265803091707_s1_p0/59477/0_17561

## Sphingo

Consistency checked on NCBI; annotation uploaded
* Need to upload additional information

## To do
* Additional Sphingo information
* Try to align the above raw reads and determine number of repeats

# 5 July 2017

Number of repeats in mito genome
* Span1 - 108 repeats
* Span2 - 76 repeats
* Span3 - 108 repeats
* Span4 - 103 repeats

Compare this to the previous runs through SMRT Portal
* Long		- 108 repeats (some apparently truncated repeats)
* Short 	- 103 repeats (some longer/shorter variants)
* Third		- 65 repeats (one slightly longer)
* Fourth	- 120 repeats
* Fifth		- 103 repeats (some longer/shorter variants)
* 17k_1		- 37 repeats
* 18k		- 37 repeats
* 19k		- 13 repeats (starts in low quality region however)

Used upstream and downstream regions 100bp to check for any additional reads to check:
* m160809_233148_42203_c101084512550000001823238903091753_s1_p0/98665/0_14272
* m160906_163330_42203_c101088662550000001823265803091704_s1_p0/110484/0_16498
* m160906_225243_42203_c101088662550000001823265803091705_s1_p0/61208/0_13107
* m160907_135022_42203_c101088552550000001823265803091740_s1_p0/84347/19711_29680

* Span5 - 108 repeats
* Span6 - 40 repeats
* Span7 - 87 repeats (one VERY extended)
* Span8 - 76 (last one extended)

* As the 19k assembly appears to be of poor quality, delete job to increase space
  * 16747: RO5_Mito_19k_1_Circ_Test_Reverse, RO5_Mito_19k_1_Reverse reference, normal parameters

## Microbiome

Remaining modification analyses prepared for once the current Mito job is complete
* Raw reads will also be required

* Check extraction details for ST54, specifically:
  * Isolation source - top-layer sediment?
  * Collection date - 2009?
  * Geographic location - Sweden: Oresund?
  * Depth - 14m?
  * Environment biome - marine sediment?
* Waiting on reply from Anna regarding these details


## To do
* Check Mito polish job on SMRT Portal and then run the remaining bacterial modification analyses
* Wait for Anna's reply, then submit final two BioSample registrations
* If Mito polish job doesn't return good results, try making a custom number of repeats and see what the coverage does
* Polish annotations for Sulfitobacter, Antarctobacter and Arenibacter (perform corrections on GenBank file rather than .tbl files?)
* Check Anna's request re: genes

# 6 July 2017

## Bacteria
Registration of last BioSamples complete (for the 7 initial bacteria); can proceed to inspection and submission of the annotations
* Sphingo genome accepted; must upload raw reads (ask Mats later)

## Mito
On round 2 Long resequencing, check ~17,450 - ~25,330
  * 106 repeats, one elongated (19,458-19,546)

## Sulphur metabolism search
* Any instances of SO4 -> H2S pathways in the microbiome?
* If so, any homologues in Skeletonema?
* "We have been discussing a bit on how in the world Skeletonema survive 100 years in the sediment. How can they respire? We know that they respire NO3.
But NO3 disappear completely at 10 cm depth (in best case).  What is left below is SO4. There are many bacteria capable of reducing SO4 with the end product H2S.
If you have time at some point would you be willing to look if any of those bacteria are sequenced? and if the pathway is confirmed and genes annotated?
The idea I had was if we could look in the Skeletonema genome for homologous sequences.
If you could,  just make a brief look. I do not really have any support that this is the case, more than plain sediment chemistry and a feeling that they have
to respire (although at a very low level) over the course of 100 years."

* Most of the bacteria appear to have instances of sulfate reduction pathways

## To do
* Move on to Sulfitobacter genome
* Further investigation of repeats issue
  * Clear space for further analyses?

# 7 July 2017

## Sulphur metabolism
Add extra information to the annotations, e.g. species, any publications
* Acc. nos. added, but no truly relevant publications found

Report on findings from sulfate search; also check Plaza browser

# 10 July 2017

## Sulphur metabolism
Sulfate results found for incorrect pathway - sulfate assimilation rather than dissimilation...
* Search for components of the latter pathway
* No convincing evidence... See Sulfur_metabolism in home folder

## Bacterial genome uploads
* Sphingorhabdus flavimaris files all uploaded, can proceed to paper
* Check frameshift results for Sulfitobacter
  * Chrom

  * pSMR1-1

  * pSMR1-2
    * 
  * pSMR1-3 - Overlaps - one accepted as a frameshift (04499 removed)
    * Frameshifts - 04335 removed; single-base mutation = premature stop codon mid-protein
    * Truncations - a few potential truncations noted
    * Missing AAs? - tRNA(Asp) removed
  * pSMR1-4 - One overlap, which appears to highlight a massively truncated protein... This has been noted
    * Possible truncations - Unconvinced by the two possible truncations highlighted
  * pSMR1-5 - A few overlaps, but no obvious frameshifts, etc. for dismissal
    * Possible truncations - one of the predictions is convincingly a true truncation, this has been noted
  * pSMR1-6 - Two overlaps between decent proteins and hypotheticals, but no evidence to dismiss (e.g. obvious frameshift)
    * Should hypothetical protein be removed from annotation?
    * Match hypothetical proteins in other species so leave for now
  * pSMR1-7 - No issues

## Mitochondrial genome
* Artificially create a 50-repeat reference, and check coverage
  * Third quiver2 as a base (reference RO5_Mito_50_repeat_(Third_quiver2)), default settings
  * Job 16765
* Download consensus, and delete to make space...
* Problem - low-repeat assemblies have more support in the trough because longer-repeat reads are mapping (poorly?) to the trough...
  * Change max divergence? 5% worked poorly, but compare raw read divergence to other assemblies to see what level of divergence is allowable
  * Start with 10%, move up to 12%/15%?
* Start with 10% - job 16766 (RO5_Mito_long_Quiver1 reference, 10% max divergence)
  * Only one spanning read (...98665)
  * Delete to make space
* 15% - 



## To do
* Continue pSMR1-2 checks, and finish -1 and Chrom
* Check results of 15% mito job

# 11 July 2017

## Mito

* 15% divergence on Long reference produces an unsupported longer repeat on the 28th repeat; try with shorter repeat #
* Attempting job with Third quiver1 reference - job 16768 (15% divergence, RO5_Mito_Third_Quiver1_Reverse reference)
  * Still some supporting reads as with the Long reference...
  * HOW TO PROCEED?
* Deleted for space

## Sulfitobacter

* pSMR1-1
  * 5011 removed; frameshift(?) of 5010 (exact nature uncertain...)
  * 4658-4659 (pSMR1-1) removed; frameshift of 4657
  * 4768 removed; frameshift of 4767
* Chrom
  * 00152 removed - massive overlap with 00151 and no BLASTx matches
  * 00091 (ncRNA cspA) removed; totally overlapped 00092 cspA gene (which is identical to type strain version)
  * 00686 removed - overlaps with 00687 and no BLASTp matches
  * 00153 removed - overlaps with 00154 and no BLASTp matches
  * 01683 removed - frameshift of 01682
  * 01726 removed - overlaps with 01725 and no BLASTp matches

BLAST website is being unusably slow; begin alterations of Antarcto and Areni

## pb_359_7/8


---

## To do

* Continue Sulfitobacter checks from 01901/01902 overlap (+ frameshifts, truncations and 'missing' RNAs)
* Continue checking Ant_Are (start from R)
* Think about the repeat problem some more...

# 12 July 2017

## Mito repeats

Third - 65 repeats
Third quiver2 repeats 26,401 - 31,211
In reference -		26,414 - 31,229

5' end - Over a dozen fall just short of crossing
3' end - Over a dozen fall just short of crossing
Around 14 that span the whole length (4 near-misses)
Verdict - Too short


Long - 106 -> 108 repeats
Long quiver2 repeats 17,460 - 25,319
In reference		17,460 - 25,414
(Odd repeat - 19,458 - 19,547

5' end - 3 fall just short of crossing
3' end - None fall just short of crossing
Around 15 that span the whole length (2 near-misses)
Verdict - around the right length

Question - the long 28th read in Long_quiver2 (shorter read in Long_quiver1) - is this true or merely an artifact?
* Fix length, upload reference and try again
  * Job 16770
  * Correction is made, so can't confirm or deny its veracity...



## Sulfitobacter annotation polishing

* 02833 removed, pseudogene along with 02832
* 02304 removed, pseudogene along with 02303
* 03400 removed, pseudogene along with 03399
* 03553-03555 removed - incorporated into 00001B


## To do
* Continue checking domains for Sulfitobacter, rerun tbl2asn and submit (ask re. formatting of the wraparound gene?) (Domains_to_check.txt file)
* Continue formatting of Ant_Are
* Any other things to try re. repeat region?

# 13 July 2017

## Sulfitobacter annotation
* First gene on chromosome apparently wraps around, but may be pseudogenised, so has been noted as potentially missing the N-terminus
  * Annotation files submitted to NCBI for checking

## Antarctobacter and Arenibacter
* .sqn files generated - submitted to consistency checker
* Replicon checklist
  * AntHelSMS3_Chrom - 
  * AntHelSMS3_pSMS3-1 - 
  * AntHelSMS3_pSMS3-2 - Checked
  * AntHelSMS3_pSMS3-3 - 
  * AreAlgSMS7_Chrom - 
  * AreAlgSMS7_pSMS7 - 
Complete the above ^

NOTE - Add Acc. Nos. before uploading methylation data!


## Pathway Tools
Run NCBI Sphingo through Pathway Tools and update feature figures

# 14 July 2017

* Get NCBI Sphingo to run through Pathway Tools

* Continue checking AntHelSMS3 and AreAlgSMS7 in consistency checker (AntHelSMS3_Chrom failed, retry)

* Upload and submit raw reads; accession number required for methylation data...
  * Raw reads all submitted, ensure they are accepted

## Pathway Tools
Sphingorhabdus flavimaris from 249 to 247 pathways after NCBI checks (+ Assign Probable Enzymes and Pathway Hole Filler)
* # of pathways has dipped slightly...

## Genome papers
Continue working on genome papers; ensure figures are up-to-date and observe formatting of R. mucosus paper


Checking annotations - Start from AreAlgSMS7_Chrom : Partial Overlaps : _02016 + _02017

NCBI still very slow...

# 17 July 2017

* Realign mito genome to after the repeat region and begin annotation attempt
  * Using Third_quiver2 or Fourth_quiver2
  * First post-repeat gene predicted at 35529 (Fourth_quiver2) (but contains a LOT of stops WITHIN the prediction...)

  * Prelim Prokka annotation ready, waiting for MITOS annotation (Third_quiver2), then can realign the contig to start at the first post-repeat gene start/stop
    * Then rerun annotation(s)

* Upload methylation data for Sulfitobacter, now an accession number has been assigned
  * Uploaded; Sulfitobacter complete. When data is released in ~2 days, rerun Pathway Tools
* Finish polishing the annotations for Antarctobacter and Arenibacter


* Replicon checklist
  * AntHelSMS3_Chrom - Checked
  * AntHelSMS3_pSMS3-1 - Checked
  * AntHelSMS3_pSMS3-2 - Checked
  * AntHelSMS3_pSMS3-3 - Checked
  * AreAlgSMS7_Chrom - Checked
  * AreAlgSMS7_pSMS7 - Checked

Note - AreAlgSMS7_Chrom seems to have a lot of in-frame stop codons pseudogenising various genes

(start from AreAlgSMS7_Chrom - 02597)

# 18 July 2017

Where do the T. pseudonana and P. tricornutum mitogenomes start?

Arenibacter algicola SMS7 submitted
* Upload methylation data once an accession number is assigned (if NCBI don't highlight any issues)

Start from AntHelSMS3_Chrom frameshifts - 2672/3

# 19 July 2017

Antarctobacter heliothermus genome submitted

## To do
* Work on mito genome
* Download Sulfitobacter genome from NCBI and run through Pathway Tools + extras
* Update figures in the WIP genome papers

# 20 July 2017

Moved RO5 organelle folder to data5

Mito appears to contain many in-frame stop codons BUT, it should use translation table 4, NOT 11
* Check 'in-frame stop codons' using table 4, rather than 11

* Rename/reannotate tRNAs in RO5.gbk - Ts -> Us, and adhere to conventions of other diatom genome annotations
* rRNAs need checking, especially the initial rRNA which appears to overlap several tRNAs

# 21 July 2017

Check distance between flanking motifs of repeat regions, and find assembly with a repeat region of about this **length**, rather than focusing on # of reps
* Ask Magnus re: mitochondrial annotation

2 new bacterial genomes - pb_398 - now in home directory (use subreads)

ST54 raw data - pb_354 (untreated) in SMRT portal, 11 SMRT cells
* '3cells' was a first test
  * Check if 3cells are included in the other 11; if not, run together
    * Otherwise, just use bigger one
* Second run - pb_77 - 'axenic' (antibiotic treated)
* Run separately, maybe combine later?
* ~10k SRL, but change other settings

* Run analyses in data 5, 8 and/or 7

SulPseSMR1 released; run through Pathway Tools
* Running...
  * 307 pathways
  * After Assign Probable Enzymes - 313
  * After Pathway Hole Filler - 321
    * Did SulPseSMR1 always have predictions for vit B12 production? Two new pathways inferred...

Skype Friday morning

## pb_398_001 and pb_398_002 assemblies
* Falcon assemblies - start with 10k SRL in both instances
  * Fastq doesn't appear to work - are there Fasta files available instead?

Convert fastq to fasta:  

cat input_file.fastq | awk 'NR%4==1{printf ">%s\n", substr($0,2)}NR%4==2{print}' > output_file.fa
* (If compressed: zcat input_file.fastq.gz | awk 'NR%4==1{printf ">%s\n", substr($0,2)}NR%4==2{print}' > output_file.fa)

Initial 10k SRL:
* pb_398_001 - 17 contigs, ~9.5 Mb
* pb_398_002 - 8 contigs, ~5.1 Mb

15k SRL:
* pb_398_001 - 4 contigs, ~63.8 Kb
* pb_398_002 - 29 contigs, ~614.7 Kb

20k SRL:
* pb_398_001 - No result
* pb_398_002 - No result

12k SRL:
* pb_398_001 - 88 contigs, ~6.5 Mb
* pb_398_002 - 8 contigs, ~5.1 Mb

## Arenibacter algicola SMS7
Accession numbers - CP022515 and CP022516



## To do
* Update figures for Sulfitobacter pseudonitzschiae post-NCBI
* Check distance between flanking motifs of repeat regions, and find assembly with a repeat region of about this **length**, rather than focusing on # of reps
* Continue trying to assemble two new bacterial genomes; convert other fastq files and assemble ST54 in Falcon (see above re: 3cells)
  * Check results of 7k Falcon assemblies for pb_398_00X

* 3cells appear to be present in full read file (double check using grep -A)
* Check results of 10k Falcon assemblies for 2x ST54 data sets

# 24 July 2017

## pb_398_00X
* Put preliminary (7k) assemblies into SILVA and try to obtain a preliminary genus/species identity
  * Doesn't appear to find anything; try RNAmmer or Metaxa2
  * pb_398_001 - possibly Sulfitobacter or Marinobacter
  * pb_398_002 - Sulfitobacter?
    * Looking at genome sizes, could 001 be a mixed S. pseudo + M. sal sample, and 002 be a S. pseudo sample?
    * pb_398_002 contig # consistent with this
    * pb_398_001 inconsistent; would expect 10 contigs

* Attempting 11k Falcon of pb_398_00X
  * Attempt 10.6k? Attempt Canu?

* pb_398_002 vs pb_359_6 - 10.6k Falcon

|       | pb_359_6  | pb_398_002 |
|-------|-----------|------------|
| Total | 5,121,602 | 5,125,074  |
| Chrom | 3,572,445 | 3,571,298  |
| Plas1 |   428,095 |   427,966  |
| Plas2 |   292,917 |   292,827  |
| Plas3 |   284,777 |   284,706  |
| Plas4 |   209,222 |   209,134  |
| Plas5 |   142,107 |   142,088  |
| Plas6 |    99,245 |    99,216  |
| Plas7 |    92,794 |    92,715  |

When aligned, these sequences are VERY similar to one another (>99% similarity)

## ST54

10k run results:
* pb_354 - 470 contigs
* pb_77 - 109 contigs

* Try an initial Metaxa2 analysis to get a rough idea of which bacteria I can expect to find
  * pb_354 - All Skeletonema, mito and chloro; no bacteria??
  * pb_77 - 2x Skeletonema, 1x Flavobacteriaceae
    * Check this sequence in SILVA: Kordia...

Run new assemblies and rerun Metaxa2
* Try Canu once one or two more Falcon assemblies have been run, and an estimated genome size can be reliably included
* 15k failed for pb_77; try 12k, then 7k (for both samples)
  * Then start tinkering with other settings

## Mitochondrion
Check size of repeat region as predicted by the spanning raw reads (length in bp, not number of repeats)
* Span1 - 7796 bp (108 repeats)
* Span2 - 5730 bp (76 repeats)
* Span3 - 8309 bp (108 repeats)
* Span4 - 7601 bp (103 repeats)
* Span5 - 8299 bp (108 repeats)
* Span6 - 3006 bp (40 repeats)
* Span7 - 7438 bp (87 repeats)
* Span8 - 5693 bp (76 repeats)
  * Span9 - 7646 bp (111 repeats)
Length of repeat region still not close to constant...


## To do
* Check results of ongoing ST54 Falcon runs
* Check results of 2x PhyloPhlAn runs (and move files appropriately)
* Any more ideas on resolving the repeat issue)


# 25 July 2017

## Useful command
To sum numbers, one per line:
`awk '{s+=$1} END {print s}'`

## ST54 Falcon
15k completed, 7k and 12k still ongoing
* 12k complete, 7k still ongoing

* Attempt Canu on pb_354 with genomeSize of 80.5m (estimate from Falcon assembly sizes)

* As pb_77 has had poor results, try tweaking other parameters
  * Try lowering max_diff from 500 to 400
    * No difference
  * Try lowering min_cov from 3 to 2
    * More contigs, slightly longer
  * Try lowering bestn from 10 to 8
    * No difference

## PhyloPhlAn
Rerun analyses to ensure that comparisons are all up-to-date
* Delete some of the zipped files in PhyloPhlAn folder; excessive duplication

Comparisons
* pb_359_2 - Roseovarius
  * Moved own uploaded file out of folder; moved 'suppressed' version in
* pb_359_3 - Loktanella
  * Moved own uploaded file out of folder
* pb_359_4 - Sphingorhabdus
  * Moved own uploaded file out of folder
* pb_359_5 - Marinobacter
  * Moved own uploaded file out of folder
* pb_359_6 - Sulfitobacter
  * Moved own uploaded file out of folder
* pb_359_7 - Antarctobacter
  * Own file isn't there yet (A. heliothermus DSM 11445T uploaded a week ago)
* pb_359_8 - Arenibacter
  * Own file isn't there yet (A. algicola TG409T there instead)

16S notes
* pb_359_2 - 2x identical sequences
* pb_359_3 - 2x identical sequences
* pb_359_4 - 2x identical sequences
* pb_359_5 - 3x sequences (one differs by a single base sub)
* pb_359_6 - 2x identical sequences (inc. one on plasmid?)
* pb_359_7 - 2x identical sequences
* pb_359_8 - 3x identical sequences


## To do
* Check Rhodo PhyloPhlAn to confirm figures
  * Continue work on the genome announcements as a whole
* Download pb_359_8 from NCBI when able (releases on 26th) and await pb_359_7
* Repeat problem...
* Check 2x assembly attempts for pb_354
  * Falcon + Canu
* Consider running new Falcon jobs for other SRLs than 7k


# 26 July 2017

## ST54
* pb_354 7k Falcon crashed; restarted
* pb_354 Canu crashed; restarted

* Changing parameters of pb_77 7k Falcon appears to have no effect; try 10k instead

* Trying pb_77 in Canu with the same parameter (80.5m) as pb_354...




## pb_398

* pb_398_002 apparently Sulfitobacter pseudonitzschiae
  * Sequences non-identical - 2 substitutions
  * vs. pb_359_6, 2 subs in one, perfect match in the other

* pb_398_001 16S sequences matched to Sulfitobacter and Marinobacter; potentially mixed sample?
  * One sequence has its best match to Marinobacter algicola (similarly to pb_359_5; compare)
    * Manually searching reveals two such regions in pb_398_001
    * These match perfectly with one of the 16S regions in pb_359_5
  * Two (identical) sequences have their best matches to Sulfitobacter mediterraneus (compare to pb_359_6)
    * Identical to pb_359_6
  * Run Canu with 4.5m genomeSize (parameter used for M. salarius)

  * Compare pb_398_001 (10.6k Falcon) with pb_359_5 and _6, check whether evidence can be found of this being a mixed sample
    * Seems likely; try again with 4.5m Canu when complete

# 27 July 2017

* pb_354 - Falcon - 7k still running

* Check pb_354 and pb_77 80.5m Canu runs
  * pb_354 complete
  * pb_77 complete

* Check pb_398_001 4.5m Canu run
  * Run complete

## pb_398_001

Results of 4.5m Canu
* 15 contigs, two of which are roughly the same size as those in pb_359_5
  * Compare in Mauve

# pb_354 and pb_77

pb_354 80.5m Canu
* 1404 contigs, totalling ~115 Mb
  * Size range - 8,031 to 712,488
  * Not even big enough for a bacterial chromosome...

pb_77 80.5m Canu
* 195 contigs, totalling ~17 Mb
  * Size range - 2,404 to 4,069,201
  * Three contigs bigger than 1 Mb
    * All apparently belong to bacteria!

Run this info through Metaxa2
* pb_354
  * 6 sequences found, all Skeletonema

* pb_77
  * 6 sequences found:
    * tig00000003     Bacteria;Proteobacteria;Alphaproteobacteria;Rhodobacterales;Rhodobacteraceae    97.2    1322    80.80
      * 2,436,254 bp - Bacterial chromosome?
      * New?
      * BlastN of 16S database predicts Sulfitobacter

    * tig00000007     Chloroplast;;;;;        99.57   1409    97.99
      * 122,694 bp - approximately correct size of S. marinoi chloroplast

    * tig00000039     Eukaryota;Chromalveolata;Stramenopiles;Diatomea;Bacillariophytina;Mediophyceae;Skeletonema      100     1718    99.71
      * 22,481 bp - Skeletonema...

    * tig00000251     Bacteria;Proteobacteria;Alphaproteobacteria;Rhizobiales;Rhodobiaceae;Parvibaculum;alpha proteobacterium NAMAF008;       98.96   1346    100
      * 12,880 bp - ???
      * Matches a species found by Alvar

    * tig00000531     Bacteria;Bacteroidetes;Flavobacteria;Flavobacteriales;Flavobacteriaceae 96.85   1492    80.15
      * 4,069,201 bp - Bacterial chromosome?
      * Kordia?

    * tig00000534     Bacteria;Proteobacteria;Gammaproteobacteria     94.2    1413    89.48
      * 2,680,853 bp - Bacterial chromosome?
      * Congregibacter?

| Contig      | Length (bp) | Classification                        | Match in SILVA          | Vs. Alvar's findings                   |
|-------------|-------------|---------------------------------------|-------------------------|----------------------------------------|
| tig00000003 | 2,436,254   | Rhodobacteraceae                      | None...                 | ???                                    |
| tig00000251 |    12,880   | Parvibaculum                          | Uncultured Rhodobiaceae | Fragment, but Alvar's also fragmented? |
| tig00000531 | 4,069,201   | Flavobacteriaceae (Kordia?)           | Kordia (algicida?)      | Maybe ~1 Mb too short?                 |
| tig00000534 | 2,680,853   | Gammaproteobacteria (Congregibacter?) | None...                 | Maybe ~1 Mb too short?

* Attempt to circularise the three large contigs?
  * Is there space on disk?
    * Only 62 Gb... Any way to cut space?
  * Delete jobs from SMRT Portal:
    * 16770 - RO5_Mito_Long_Quiver_28th_Repeat_Normalised reference, other HGAP settings normal
    * 16700 - RS_Modification_and_Motif_Analysis.1 - pb_359_2_All_Contigs reference (results saved in SubmissionPreparations/RosMucSMR3/SRA)
    * 16701 - RS_Modification_and_Motif_Analysis.1 - pb_359_5_Canu_Trimmed reference (results saved in SubmissionPreparations/MarSalSMR5/SRA)
    * 16703 - RS_Modification_and_Motif_Analysis.1 - pb_359_3_All_Contigs reference (results saved in SubmissionPreparations/LokVesSMR4r/SRA)
    * 16760 - RS_Modification_and_Motif_Analysis.1 - pb_359_4_Canu_Trimmed_reupload reference (results saved in SubmissionPreparations/SphFlaSMR4y/SRA)
    * 16761 - RS_Modification_and_Motif_Analysis.1 - pb_359_6_All_Contigs reference (results saved in SubmissionPreparations/SulPseSMR1/SRA)
    * 16762 - RS_Modification_and_Motif_Analysis.1 - pb_359_7_Canu_Trimmed reference (results saved in SubmissionPreparations/AntHelSMS3/SRA)
    * 16763 - RS_Modification_and_Motif_Analysis.1 - pb_359_8_17k_Falcon_Assembly reference (results saved in SubmissionPreparations/AreAlgSMS7/SRA)
  * 205 Gb available
    * Need to trim first
    * (Negative covStat, likely to be repetitive...? According to Canu manual)
* Circularisation
  * None appear to circularise correctly...

* Keep an eye on pb_354 Falcon seed_read_7k job; taking a long time and generating very large files
  * Job deleted - files growing too large to be practical
  * Over 120 Gb; log file alone was 10 Gb
* As previous Canu runs produced no circularisable bacterial contigs, attempt with a new parameter
  * genomeSize 55m (predicted size of the S. marinoi genome)

## To do
* Check the above Canu jobs
* Continue working on genome announcement papers

# 28 July 2017

## Arenibacter algicola SMS7
Released on NCBI - rerun through Pathway Tools and update feature numbers
* Feature numbers updated
* Pathway Tools (originally 268 pathways)
  * First run                     - 258
  * After Assign Probable Enzymes - 
  * After Pathway Hole Filler     - 


## ST54 Canu
Check 55m jobs
* pb_354

* pb_77


## To do
* Verify that pb_398_00X are duplicate samples
* Run contig overlap graphs (R) for Falcon assemblies (p.47 of https://scilifelab.github.io/courses/assembly/1611/files/PacBio_Assembly.pdf)
  * DONE - Make a list of contig lengths (sorted) and save them
    * DONE - `fp.py --length FILE.fa | sort -n -r > FILE_Length.txt`
    * DONE -  One for primary, one for associated
  * DONE - Generate `sg_edges_to_GFA.py > Sm_Ref_v1.gfa`
    * DONE - Can view in Bandage (redownload?)
* Add the above commands to the runFalcon.sge script for automation (string graph script needs automating)
* Look at quality score in fastq file for mito repeats region reads?
  * DONE - Finish AreAlgSMS7 Assign Probable Enzymes, then proceed to Pathway Hole Filler


# 14 August 2017
* Finish 'Assign Probably Enzymes' jobs
* Check ST54 55m Canu jobs?
* See above

## Arenibacter algicola SMS7
* Completing Pathway Tools analyses (originally 268 pathways)
  * First run                     - 258
  * After Assign Probable Enzymes - 259
  * After Pathway Hole Filler     - 268
  * No change!

## Antarctobacter heliothermus SMS3 (originally 320 pathways)
* Feature numbers updated on GitLab
  * First run                     - 295
  * After Assign Probable Enzymes - 302
  * After Pathway Hole Filler     - 315
  * Five less than before...

## Assembly graphs for Falcon assemblies
* Bandage reinstalled on local machine

* Add these commands to runFalcon.sge scripts:
fp.py --length 2-asm-falcon/p_ctg.fa | sort -n -r > 2-asm-falcon/p_ctg_length.txt
fp.py --length 2-asm-falcon/a_ctg.fa | sort -n -r > 2-asm-falcon/a_ctg_length.txt
(# sg_edges_to_GFA.py > String_Graph.gfa)

* sg_edges_to_GFA.py cannot be run, find a way to automate this
  * Needs to be run from the 2-asm-falcon subdirectory, not the seed_read_Xk directory

## Contig overlap graph syntax for R

$ R 
> library(MASS) 
> data <- read.table("ovlp_stats.txt") 
> plot(data$V3,data$v4) 
> z <- kde2d(data$V3,data$v4) 
> contour(z,add=TRUE)

* Double-check syntax to output graph to file

## Still to-do
* Verify that pb_398_00X are duplicate samples
* Run contig overlap graphs (R) for Falcon assemblies (p.47 of https://scilifelab.github.io/courses/assembly/1611/files/PacBio_Assembly.pdf)
* Look at quality score in fastq file for mito repeats region reads?
* Find way to automate string graph generation from Falcon
  * DONE (AWAITING FEEDBACK) - Update announcement papers
* Attempt to assemble/circularise bacterial genomes from within ST54 S. marioni genomes





# 15 August 2017

## Announcement papers
Genome feature figures now up-to-date; must include details on interesting features...
* R. mucosus announcement - 436 words

* Double-check crt result in DMSP superpathway of M. salarius when MetaCyc is available again...

* Papers updated, need to determine which other information to include in the shorter papers...

## Mito repeat region
* Don't have fastq file for ...
  * Do any fastq files exist for pb_354 in e.g. SMRT Portal?
  * FASTQ file located in SMRT Portal job directories (can't access raw SMRT Portal data due to permissions)
    * Example: /home/smrtanalysis/userdata/jobs/016/016759/data/filtered_subreads.fastq
    * Quality scores seem very low overall...
* Find repeat sections from each raw read
  * m160810_080809_42203_c101084512550000001823238903091755_s1_p0/93737/11172_21805	2447-10242	AAAC-GTTC
  * m160907_135022_42203_c101088552550000001823265803091740_s1_p0/84347/631_10058	1007-6737	GAAC-TCCT
  * m160809_233148_42203_c101084512550000001823238903091753_s1_p0/98665/14321_28605	2986-11294	GAAA-GTTC
  * m160907_093109_42203_c101088662550000001823265803091707_s1_p0/59477/0_17561		2090-9690	GAAA-TTCT
  * m160809_233148_42203_c101084512550000001823238903091753_s1_p0/98665/0_14272		2967-11265	AACA-TTTC
  * m160906_163330_42203_c101088662550000001823265803091704_s1_p0/110484/0_16498	998-4003	AAGC-TTTC
  * m160906_225243_42203_c101088662550000001823265803091705_s1_p0/61208/0_13107		4093-11530	GAAA-TGTT
  * m160907_135022_42203_c101088552550000001823265803091740_s1_p0/84347/19711_29680	1590-7282	GGAA-TGTT

  * head -n4 Repeat_Spanning_Raw_Reads.fastq | cut -c2447-10242 > TRIMMED_Repeat_Spanning_Raw_Reads.fastq
  * head -n8 Repeat_Spanning_Raw_Reads.fastq | tail -n4 | cut -c1007-6737 >> TRIMMED_Repeat_Spanning_Raw_Reads.fastq
  * head -n12 Repeat_Spanning_Raw_Reads.fastq | tail -n4 | cut -c2986-11294 >> TRIMMED_Repeat_Spanning_Raw_Reads.fastq
  * head -n16 Repeat_Spanning_Raw_Reads.fastq | tail -n4 | cut -c2090-9690 >> TRIMMED_Repeat_Spanning_Raw_Reads.fastq
  * tail -n16 Repeat_Spanning_Raw_Reads.fastq | head -n4 | cut -c2967-11265 >> TRIMMED_Repeat_Spanning_Raw_Reads.fastq
  * tail -n12 Repeat_Spanning_Raw_Reads.fastq | head -n4 | cut -c998-4003 >> TRIMMED_Repeat_Spanning_Raw_Reads.fastq
  * tail -n8 Repeat_Spanning_Raw_Reads.fastq | head -n4 | cut -c4093-11530 >> TRIMMED_Repeat_Spanning_Raw_Reads.fastq
  * tail -n4 Repeat_Spanning_Raw_Reads.fastq | cut -c1590-7282 >> TRIMMED_Repeat_Spanning_Raw_Reads.fastq

* To count each character X in each line of file Y
  * `tr -d -c 'X\n' < Y | awk '{ print length; }'`
* `sed G`
  * Adds a newline after each output line

* Massive extension in one of the repeat regions has low quality; can rule this out

* Calculated quality percentages for each repeat region; IS THERE SOFTWARE THAT CAN GENERATE A HEATMAP OF THIS INFORMATION?

## pb_398_00X
* Email Oskar re: physical characteristics of pb_398_001 and _002
  * No physical data yet, aside from looking similar to Sulfitobacter and having slightly-similar qualities re: antibiotics


# 16 August 2017

## Mito repeat region
Running FastQC on each spanning sequence
* Trough in span 7 (the extended read)
* Trough in span 4 (103 reps)

* Average quality scores:
  * Span1	m160810_080809_42203_c101084512550000001823238903091755_s1_p0/93737/11172_21805		10.57824525
  * Span2	m160907_135022_42203_c101088552550000001823265803091740_s1_p0/84347/631_10058		11.24777526
  * Span3	m160809_233148_42203_c101084512550000001823238903091753_s1_p0/98665/14321_28605		10.90071007
  * Span4	m160907_093109_42203_c101088662550000001823265803091707_s1_p0/59477/0_17561		11.0078937
  * Span5	m160809_233148_42203_c101084512550000001823238903091753_s1_p0/98665/0_14272		9.868538378
  * Span6	m160906_163330_42203_c101088662550000001823265803091704_s1_p0/110484/0_16498		10.26779774
  * Span7	m160906_225243_42203_c101088662550000001823265803091705_s1_p0/61208/0_13107		10.09438021
  * Span8	m160907_135022_42203_c101088552550000001823265803091740_s1_p0/84347/19711_29680		11.16318286

* Highest averages (those above 11) belong to:
  * Span 2 - 76 reps
  * Span 4 - 103 reps - This does have a quality dip in the middle...
  * Span 8 - 76 reps (last one very extended, which does have noticably lower average quality)

* Lowest average - Span 5 (<10) - 108 reps

### Repeat number evidence

* Of the eight spanning hits:
  * Three show 108 reps
  * Two show 76 reps
  * One each of 103, 87, 40 reps

* Highest average FASTQ scores (>11):
  * Span 2 (76 reps)
  * Span 4 (103 reps)
  * Span 8 (76 reps) (low quality at the start where initial repeat is very (falsely) extended)

* Lowest average FASTQ score (<10):
  * Span 5 (108 reps)

* Double-check FULL read quality, not just repeat region
  * Lowest (<10):  Span 6 (40 reps)
  * Highest (>11): Span 2 (76 reps)
    * Spans 4 (103 reps) and 8 (76 reps) close behind once again

* 76 reps generally produces better quality results?

(See also Excel spreadsheet)
(Can check in FastQC)

## pb_398
Have pb_398_001 and pb_398_002 been compared to pb_359_5 and pb_359_6 for ALL of the relevant assemblies?
* pb_398_001 (Canu 4.5m)
* pb_398_001 (Falcon 10.6k)
* pb_398_002 (Falcon 10.6k)
* pb_359_5 (Canu 4.5m)
* pb_359_6 (Falcon 10.6k)

* Check percantage similarity between pb_398_00X and pb_359_X
  * pb_398_002 vs pb_359_6 (Sulfito) (Falcon)

| Replicon | 002 length | Sulf length | % ID  |
|----------|------------|-------------|-------|
| Total    |  5,125,074 |   5,121,602 |   -   |
| Chrom	   |  3,571,298 |   3,572,445 | 
| pSMR1-1  |    427,966 |     428,095 | 99.9% |
| pSMR1-2  |    292,827 |     292,917 | 99.9% |
| pSMR1-3  |    284,706 |     284,777 | 99.9% |
| pSMR1-4  |    209,134 |     209,222 | 99.9% |
| pSMR1-5  |    142,088 |     142,107 | 99.9% |
| pSMR1-6  |     99,216 |      99,245 | 99.9% |
| pSMR1-7  |     92,715 |      92,794 | 99.8% |

  * pb_398_001 vs pb_359_5 (Marino) (Canu)

| Replicon | 001 length | Marino length | % ID  |
|----------|------------|---------------|-------|
| Total    |  4,642,139 |     4,630,160 |   -   |
| Chrom    |  4,398,909 |     4,386,892 |       | (tig00000013)
| pSMR5    |    243,230 |       243,268 | 98.8% | (tig00000000_rev_comp) (two long gaps, one in each; rearrangement or limited misassembly?)

  * pb_398_001 vs pb_359_6 (Sulfito) (Falcon)

| Replicon | 001 length | Sulf length | % ID  |
|----------|------------|-------------|-------|
| Total    |            |   5,121,602 |   -   |
| Chrom    |            |   3,572,445 |       | (Multiple...)
| pSMR1-1  |    427,911 |     428,095 | 99.9% | (21)
| pSMR1-2  |269,041(..?)|     292,917 | 91.8% | (000008F_rev_comp) (gap as expected)
| pSMR1-3  |    284,657 |     284,777 | 99.9% | (22)
| pSMR1-4  |    209,124 |     209,222 | 99.9% | (24)
| pSMR1-5  |122,994(..?)|     142,107 | 86.5% | (000011F) (20k gap as expected)
| pSMR1-6  |28,663 (...)|      99,245 |       | (000019F_rev_comp)
| pSMR1-7  |31,268 (...)|      92,794 |       | (000018F)

Any way to align sequences longer than 1Mb and get a % identity score without having to slice the sequence?


## To do
* Align longer sequences
* Double-check 16S sequences for pb_398...

* Contig overlap graphs in R for Falcon sequences (ST54 data)
  * cd 1-preads_ovl
  * module load FALCON/v1.8.2
  * fc_ovlp_stats --fofn merge-gather/las.fofn > ovlp_stats.txt
    * 'AssertionError' - problem with Falcon script?
      * Other Falcon versions on Albiorix throw a 'DistributionNotFound' error

  * $ R
    > library(MASS)
    > data <- read.table("ovlp_stats.txt")
    > plot(data$V3,data$v4)
    > z <- kde2d(data$V3,data$v4)
    > contour(z,add=TRUE)


# 17 August 2017

## pb_398 Identity checks
* pb_398_001 - Sulfitobacter + Marinobacter mix (S. pseudonitzschiae + M. salarius?)
  * 16S checks
     * Based on 10.6k Falcon (Sulfito)
       * Metaxa2 predicts 3 16S sequences - 1x Marinobacter (should be 3...), 2x Sulfitobacter
       * Searching conserved 5' region (50bp, identical between Marino and Sulfito) reveals 5 potential 16S regions, as expected
         * Marino sequences - two identical, _1 differs from the _2 and _3 by +1 bp and 1 bp substitution
           * _1 vs pb_359_5 1+2 - +1bp, 1bp sub
           * _1 vs pb_359_5 3   - +1bp
           * _2+_3 vs pb_359_5 1+2 - identical
           * _2+_3 vs pb_359_5 3   - 1bp sub
           * SMR5 top BLASTn result; vs M. salarius R9SW1 - 99.4% (R9SW1 predicted longer, but longer parts match in _001)
         * Sulfito sequences - both identical
           * _1+_2 vs pb_359_6 1+2 - identical
           * SMR1 top BLASTn result; vs S. pseudonitzschiae H3 - 99.2% (H3 16S is shorter at the 5' end)

     * Based on 4.5m Canu (Marino)
       * Metaxa2 predicts 3 16S sequences - 1x Marinobacter (should be 3...), 2x Sulfitobacter
       * Searching conserved 5' region (50bp, identical between Marino and Sulfito) reveals 5 potential 16S, as expected
         * Marino sequences - two identical, _3 differs from _1 and _2 by 1bp substitution
           * _1+_2 vs pb_359_5 1+2 - identical
           * _1+_2 vs pb_359_5 3   - 1bp sub
           * _3 vs pb_359_5 1+2 - 1bp sub
           * _3 vs pb_359_5 3   - identical
           * SMR5 top BLASTn result; vs M. salarius R9SW1 - 99.4%/99.5%
         * Sulfito sequences - both identical
           * _1+_2 vs pb_359_6 1+2 - identical
           * SMR1 top BLASTn result; vs S. pseudonitzschiae H3 - 99.2%

* pb_398_002 - Sulfitobacter (pseudonitzschiae?)
  * Assembly size and contig number/sizes are consistent
  * 16S checks
    * Compared to pb_359_6: 0/1bp sub (002_Plas1 copy identical to pb_359_6; 002_Chrom copy 1bp substitution vs _6)
    * SMR1 top BLASTn result; vs S. pseudonitzschiae H3 - 99.2% (H3 16S is shorter at the 5' end)

* Issues with the Canu assembly of pb_398_001, but evidence seems to suggest that:
  * pb_398_001 = Marinobacter salarius (SMR5?)
  * pb_398_002 = Sulfitobacter pseudonitzschiae (SMR1?)



## Points for Skype Call

* Mito repeats
  * See /nobackup/data5/Skeletonema_marinoi_genome_project/08_RO5_Organelles/Mito_Repeats_Evidence.md
  * See more in-depth statistics in Excel spreadsheet?
  * 76 reps the best result?
  * WOULD REPEAT LENGTH DIFFER BETWEEN MITOCHONDRIA IN AN INDIVIDUAL CELL?
  * LOOK AT RAW READ QUALITY INDIVIDUALLY TO ELIMINATE LOW-QUALITY REGIONS
    * FIND ASSEMBLY WITH # OF REPEATS CLOSEST TO THE BEST-QUALITY RAWS
    * CHECK STRINGENCY OF SETTINGS AND SPANNING READS OF e.g. 'THIRD', AND IF ALL LOOKS WELL THEN GO WITH THIS (NOTE THIS IN M&M SECTION)
      * RETRY MITOS AND DOGMA ANNOTATORS
      * USE TRANSLATION TABLE 4
      * HOLD FIRE FOR NOW UNTIL ILLUMINA DATA ARRIVES

* Identities of pb_398 samples
  * See /nobackup/data5/Skeletonema_marinoi_microbiome_project/01_assemblies/pb_398/README.md
  * pb_398_001 = S. pseudonitzschiae + M. salarius
  * pb_398_002 = S. pseudonitzschiae
    * Oskar - "I have not performed much characterization on the two new ones, although they appear very similar to each other and slightly to the Sulfitobacter.
               This is only based on appearance and antibiotic production. (Though they seem to differ in severeness in antibiotic amount)"
  * Supported by 16S evidence and contig lengths/identities (particularly pb_398_002)
    * !!!Check pb_359_5 assemblies, try Falcon parameters which gave 2-contig results, try to get good results for both Sulfito AND Marino

* Contig overlap graphs
  * 'AssertionError' when running fc_ovlp_stats; problem with Falcon script?

* String graphs and lists of contig length
  * !!!Need to find a way to automate graph production in runFalcon.sge script
    * Graph generation script should run in subdirectory, find syntax (should be simple?)

* Find bacterial sequences in ST54
  * !!!Ongoing...
  * See below re. pb_354
  * BLAST 16S OF pb_77 SULFITOBACTER

* Announcement papers
  * !!!Feedback? Need to know what else to include if necessary (see notes in Google Docs)
    * Are pathways with elements missing still worthy of inclusion in the announcement papers?
  * Double-check crt result in DMSP superpathway of M. salarius when MetaCyc is available again...
  * INCLUDE DETAILS ON INCOMPLETE PATHWAYS IF INTERESTING

* Is pb_354 from ST54 or RO5?
  * pb_354 present in ST54 directory in ~/PacBio_raw_data
  * pb_354 used for RO5 jobs in SMRT Portal, including those for the mitochondrial assembly
  * Seems most likely that pb_354 is from RO5
    * This might explain why 'untreated' sample apparently has no bacteria
  * pb_354 BELONGS TO RO5


## pb_398_002 vs S. pseudonitzschiae SMR1 - difference in antibiotic sensitivity

Searching for large stretches (>3) of missing bases in genes that may have relevance to antibiotic sensitivity
* Chromosome (pt1)
  * pb_398_002 shows 4 deletions, 1 insertion and 1 substitution in 'penicillin-binding protein 2' mrdA gene
  * (phnH and phnG, involved in 'organic phosphonate catabolic process', appear to have undergone many deletions in pb_398_002 vs. SMR1)
  * (Mutations in ftsH and hflC?)
* Chromosome (pt2)
  * (Mutations in 2x B12 binding proteins)
  * pb_398_002 shows 12bp deletion in katA catalase gene, 'involved in resistance to paraquat when fur is absent and to tert-butyl hydroperoxide' (http://www.uniprot.org/uniprot/Q2FYU7)
  * pb_398_002 shows 2 deletions and 1 substitution in phosphoglucomutase pgm gene, useful vs antimicrobial peptides? (https://www.ncbi.nlm.nih.gov/pubmed/19589833)
  * pb_398_002 shows scattered deletions/mutations in "antilisterial bacteriocin subtilosin biosynthesis protein AlbA", involved in production of antibacterials (http://www.uniprot.org/uniprot/O07623)
* Chromosome (pt3)
  * ?
* Chromosome (pt4)
  * In pt3 and pt4, multiple genes pertaining to vitamin B12 appear to differ between pb_398_002 and SMR1
* Plasmid 1
  * pb_398_002 missing a chunk ~8bp in 'acylase ACY 1' acyI gene
    * GO biological process - response to antibiotic (http://www.uniprot.org/uniprot/P15557)
* Plasmid 2
  * ?
* Plasmid 3
  * pb_398_002 missing a chunk ~6bp in 'rhodocoxin reductase' thcD gene
    * Required for herbicide degradation, but may still be of interest
  * (Massive differences in 'von Willebrand factor type A domain protein' (SULPSESMR1_04358))
* Plasmid 4
  * ?
* Plasmid 5
  * ?
* Plasmid 6
  * ?
* Plasmid 7
  * ?

## To do
* See above
* Determine where the predicted differences between pb_398_002 and S. pseudonitzschiae SMR1 are
  * Could this influence the difference in antibiotic sensitivity?
  * Try with pb_398_001 and SMR1 (and SMR5) if cleaner assemblies can be obtained

|                     | SMR1 vs pb_398_002 |
|---------------------|--------------------------------|
| -900,000            | 899608/900483 (99.9%)		674/900483 ( 0.1%)	SMR1 - 900292	|
| 900,001-1,800,000   | 899810/900321 (99.9%)		416/900321 ( 0.0%)	SMR1 - 900226	|
| 1,800,001-2,700,000 | 899646/900594 (99.9%)		827/900594 ( 0.1%)	SMR1 - 900361	|
| 2,700,001-          | 870975/871730 (99.9%)		596/871730 ( 0.1%)	SMR1 - 871566 (_002 - 871298)	|


# 18 August 2017

See capitals above:
* In announcement papers, include details on incomplete pathways if there is a decent amount of evidence for them
* Blast 16S of pb_77 bacteria, in particular Sulfitobacter (not predicted by Alvar)
* Re: mito repeats
  * WOULD REPEAT LENGTH DIFFER BETWEEN MITOCHONDRIA IN AN INDIVIDUAL CELL?
  * LOOK AT RAW READ QUALITY INDIVIDUALLY TO ELIMINATE LOW-QUALITY REGIONS
    * FIND ASSEMBLY WITH # OF REPEATS CLOSEST TO THE BEST-QUALITY RAWS
    * CHECK STRINGENCY OF SETTINGS AND SPANNING READS OF e.g. 'THIRD', AND IF ALL LOOKS WELL THEN GO WITH THIS (NOTE THIS IN M&M SECTION)
      * RETRY MITOS AND DOGMA ANNOTATORS
      * USE TRANSLATION TABLE 4
      * HOLD FIRE FOR NOW UNTIL ILLUMINA DATA ARRIVES

## ST54 bacteria

* pb_77 16S of unidentified species
  * Appears to be either Sulfitobacter or Tateyamaria
    * If Sulfito, doesn't seem to be SMR1

* Three of the four predicted bacterial species appear on long contigs

* Previous attempt to circularise failed...
  * Can't find any data for this; retry
  * grep tig00000003, tig00000531 and tig00000534 (tig00000251 currently too short)

* pb_77 (Canu 80.5m) doesn't circularise; obvious gaps when checking the reversed sequence
  * Template wasn't trimmed... DELETE JOB ON SMRT PORTAL?
  * Doesn't seem to be overlap in either Canu 80.5m or 55m... Try another set of parameters?


# 22 August 2017

## RO5 Mitogenome
* Go through the fastq files individually
* Select the most likely assembly size based on what has been obtained, and ensure that it circularises
* Repeat lengths of spanning reads - 108, 76, 108, 103, 108, 40, 87, 76
  * Spans 4 and 7 have large dips in quality in the middle - 108, 76, 108, 108, 40, 76
  * Span 5 has some areas of particularly low/middling coverage (i.e. few of the higher-quality symbols) - 108, 76, 108, 40, 76
    * 1, 2, 3, 6, 8 remaining
  * 1 has a couple of short stretches of lower quality, but otherwise okay
  * 2 has generally good quality throughout
  * 3 has generally good quality throughout
  * 6 has low quality at the start, but otherwise okay
  * 8 has low quality at the ends, but otherwise okay
* After two polishes, none of the assemblies show either 108 or 76 repeats; for completeness, attempt 16k SRL Falcon

## ST54 bacteria
Circularising the genomes is proving difficult
* How big is the expected overlap at the ends of contigs, based on the overlaps seen in the pb_359 samples?
  * If no useful information can be gained from the previous attempt at circularisation, delete it to save space
* Is it worth trying a new assembly size?
  * Sum the S. marinoi genome size (inc. chloroplast + mito) plus the predicted genome sizes of Kordia, Sulfito, Parvibaculum and Congregibacter
    * 55m + 127k + 46k (estimate) + 5.5m + 3.6m + 3.9m + 2.4m (much too small for a Sulfitobacter...)
    * ~75m, accounting for increased Sulfitobacter genome size and possible plasmids
    * Rerunning Canu, check later...
      * If the above fails, try 16.8m Canu job? (pb_77 Canu jobs have been producing this result)
    * Genome stats appear to be the same as for previous assemblies; attempting with 16.8m...
      * Different from previous assemblies; check 16S
      * 'Kordia' and 'Congregibacter' may now be complete
      * selfBlast on tig00000000 and tig00000232
      * Based on selfBlast, try removing start (-c4963-) or end (-c-3586076)
        * No goood results for 'Kordia', it seems...

## Genome announcements
Begin rewording the papers and adding additional details as necessary


## pb_354
Continue compressing this data just in case it's needed



## To do
* Check results of pb_77 75m Canu
  * If required, attempt 16.8m Canu?
    * Attempting...

* Check results of 16k RO5 Falcon assembly (mito repeat resolution)
  * Afterwards, make final decision re: repeat region

* T. pseudonana vs. P. tricornutum comparison paper mentions a '183nt inverted repeat' bracketing the repeat array
  * Does this exist in S. marinoi?
    * T. pseudonana repeat is 75bp, S. marinoi's is apparently 74bp, so similar in this regard...
    * T. pseudonana repeats are slightly variable; have RO5 repeats been overcorrected by Quiver?

* Check T. oceanica mitogenome (and if there are any other new, related mitogenomes?)

* Check SMRT Portal job re: possible Congregibacter
