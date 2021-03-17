#!/bin/bash

#this script generates a SLURM file for the AHPCC Razor cluster

# define some variables
job = 'Trinity-assembly'
wall = 6
queue = 'mod16core'
nodes = 1 #nodes number
pnn = 1 #pnn num

#this section prints the header/required info for the pbs script

print('#SBATCH -J', job ) #name of the job
print('#SBATCH --partition comp06')
print('#SBATCH -o', job + '.txt')
print('#SBATCH -e', job + '.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=ebahrami@uark.edu')
print('#SBATCH --nodes=1' + str(nodes))
print('#SBATCH --ntasks-per-node=' + str(pnn))
print('#SBATCH --walltime=' + str(wall) + ':00:00')

export OMP_NUM_THREADS=32

# load required modules
print('#module load samtools')
print('#module load salmon/0.8.2')
print('#module load java')

# cd into the directory where you're submitting this script from
print('cd $SLURM_SUBMIT_DIR')

# copy files from storage to scratc

print('rsync -av RNA-R*.fastq.gz /scratch/$SLURM_JOB_ID')

# cd onto the scratch disk to run the job
print('cd /scratch/$SLURM_JOB_ID/')

# run the Trinity assembly
print('/share/apps/bioinformatics/trinity/trinityrnaseq-v2.11.0/Trinity --seqType fq --left RNA-R1.fastq.gz --right RNA-R2.fastq.gz --CPU 48 --max_memory 250G --trimmomatic --no_normalize_reads --full_cleanup --output trinity_Run2')






