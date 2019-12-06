#!/bin/bash
# Author: Sam Turner sat19@ic.ac.uk
# Script: ConcatenateTwoFiles.sh
# Desc: Concatentate two files and save to specified path
# Arguments: 1 -> input .txt file to be placed at top of output file
#            2 -> input .txt file to be places at bottom of output file
#            3 -> output file path (recommended ../Results/<filename>.txt
# Date: Oct 2019

if [ -z "$1"] || [ -z "$2"] ||  [-z "$3"] 
then
    echo "Error. 3 arguments required: 2 input files to concatenate, and 1 output file path"
    exit
fi

# copy first input file to output file
cat $1 > $3
# copy second input file to output
cat $2 >> $3

echo "Merged File is"
cat $3
