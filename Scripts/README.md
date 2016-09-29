# Sequence_Reverse.py

**Function**  
Cuts a sequence in half and reattaches them in the opposite order, e.g.:
* A------B
* A---||---B
* ---BA---

**Purpose**  
Rearrangement of sequences to check coverage levels and determine whether
a contig is circular, when run through Resequencing on the SMRT Portal.

**Syntax**  
./Sequence_Reverse.py [input] [output]

**Limitations**  
Only accepts a single sequence, with a single-line header starting with '>'.

# Sequence_Reverse_Plus.py

**Additions**
As Sequence_Reverse, but can handle multiple sequences per file thanks to help from BioPython and  
http://stackoverflow.com/questions/7654971/parsing-a-fasta-file-using-a-generator-python
