# Sequence_Reverse.py

**Function**: cuts a sequence in half and reattaches them in the opposite order, e.g.:
* A------B
* A---||---B
* ---BA---

**Purpose**: rearrangement of sequences to check coverage levels and determine whether
a contig is circular, when run through Resequencing on the SMRT Portal.

**Syntax**  
./Sequence_Reverse.py [input] [output]

**Limitations**
* Only accepts a single sequence, with a single-line header starting with '>'.
