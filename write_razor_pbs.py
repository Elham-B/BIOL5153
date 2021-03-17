#!/usr/bin/env python

#this script generates a pbs file for the AHPCC Razor cluster

# define some variables
queue = 'med16core'
wall = 3 # this is in hours
Jname = 'ebahrami'

#this section prints the header/required info for the pbs script
print('#PBS -N' + ' ' + Jname) # job name
print('#PBS -q' + ' ' + queue) # which queue to use
print('#PBS -j oe') # jointhe STDOUT and STDERR into a single file
print('#PBS -o ' + Jname + '.$PBS') # set the name of the job output file
print('#PBS -l nodes=1:ppn=1') # how many resource to ask foe (nods + num nods, ppn = num processors)
print('#PBS -l walltime=' + str(wall) + ':00:00') # set the walltime (default to 1 hr)
print()
#cd to working directory
print('cd $PBS_O_WORKDIR')
print()

#load the necessary modules
print('#load modul')
print('#module purge')
print('module load gcc/7.2.1')
print()
#commands for this job
print('# insert commands here')

