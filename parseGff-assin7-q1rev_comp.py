#! /usr/bin/env python3
import csv
import argparse
from Bio import SeqIO

# inputs: 1) GFF file, 2) corresponding genome sequence(FASTA format)

# GFF filename
gff_input = 'watermelon.gff'

# fasta_filename
fasta_input = 'watermelon.fsa'
# create an argument parser object
parser = argparse.ArgumentParser(description='This script will parse a GFF file and extract each feachere from the genome')

# add positional argument
parser.add_argument("gff", help='name of the GFF file')
parser.add_argument("fasta", help='name of FASTA file')

# pars the arguments
args = parser.parse_args()


# read in FASTA
genome = SeqIO.read(args.fasta, 'fasta')
print(genome.id)
print(genome.seq)

# open and read in GFF file
with open(args.gff, 'r') as gff_in:

    def reverse_complement(fasta):
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        return ''.join([complement[base] for base in fasta[::-1]])








