#! /usr/bin/env python3
import csv
from Bio import SeqIO

genome=SeqIO.read('watermelon.fsa','fasta')
exons=''
# creat the name of the output file to hold the features
output_file = 'CDS' + '.fasta'
# print(output_file)
# open our outputfile in 'write' mode
out = open(output_file, 'w')

with open('watermelon.gff','r')  as f:
    reader=csv.reader(f,dialect='excel', delimiter='\t') # deliminates each line based on tabs
  
    for cols in reader: 
#         print(cols)
        if 'exon' in cols[-1]: # checks if the word 'exon' exists in the last column of each line
            
            start=int(cols[3])-1 # reads column 3 (start of exon).
            end=int(cols[4])-1 # reads column 4 (end of exon).
            
#             print(start,end) # prints the first and last base number of each exon.

            ex=str(genome.seq[start:end]) # copies the exon sequence from the fasta file.
    
#             print(gene)

            exons+=ex # splices the exons together.
exons

# close the output file
out.close()
