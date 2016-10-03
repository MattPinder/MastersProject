#Must be run as sudo

#$ -S /bin/bash

module load PROKKA/vX.XX

prokka --cleandb

prokka --setupdb
