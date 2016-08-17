	9 August 2016
Useful tools to install:
PROKKA
Pathway Tools
RAST

Things to try:
Submission to NCBI Prokaryotic Genome Annotation Pipeline?
PANNZER
AGeS

Raw data:
combined-revcomp-unitig-1-2.fasta

	10 August 2016
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

	11 August 2016

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

	12 August 2016

While browsing the online version of RAST, I found that there are some
indications of gene names to be found, although these may contradict the
list of genes that Oskar made. For example, online RAST identifies two copies
of RNA polymerase sigma factor RpoE, whereas Oskar notes 6 copies.

Process:
*Take the first identified gene from the V5 genbank file: rpsU.
*According to the Excel exported from RAST, it is classified as 'Ribosome SSU
bacterial', so go to this page in the RAST analysis, and look at 'Subsystem
Spreadsheet'.
*No rpsU heading, so look under S21p (the product) - one hit, labelled 1, as
this is the first 'pegged' result.
*After clicking on '1', run Psi-Blast; this opens a Psi-Blast window (first
hit Kordia jejudonensis) which identifies rpsU as a specific hit (with E-value
of 4.63e-14).

Test the above process with the next gene in the genbank file - an unnamed
alpha-amylase gene.
Two hits in conserved domains database with very high E-values:
*AmyAc_arch_bac_plant_AmyA has an E-value of 6.62e-121, and is labelled as
a specific hit, BUT has a Ca binding site missing...
*PRK09441 covers a wider part of the protein, and has an E-value of 3.29e-165

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

Questions after week 1:
*Oskar's software - PROKKA, System Tools, etc. - yielded certain results,
whereas I am able to find apparent results in addition to these which seem
to obtain better E-values in a RAST -> PSI-BLAST -> CDD search. Why?

	15 August 2016

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

	16 August 2016

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

To do:
1.) Pathway Tools webinars, paper and installation
2.) Start updating genbank file (/note field to give reason why)
3.) Potentially restructure the Kordia directory; add updated version of
genbank file to, e.g. '01_Annotation' folder

	17 August 2016

Cut apart the genbank file, now contains only the products and sequences of
the unnamed proteins (filename: AUP2). Also copied the V5 genbank file and
renamed V6, so all genes named hereafter will be added to this file; the
note field of the genbank file should be used to justify the naming of each
gene.

Running the new file through NCBI batch CD-Search Tool again, and will make
a note of any promising results.
(Still running; Search-ID QM3-qcdsearch-29D17B06C7A6E9DA)
