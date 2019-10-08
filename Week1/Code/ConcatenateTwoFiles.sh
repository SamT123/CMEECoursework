#!/bin/bash
# Author: Sam Turner sat19@ic.ac.uk
# Script: ConcatenateTwoFiles.sh
# Desc: Concatentate two files and save to specified path
# Arguments: 1 -> input .txt file to be placed at top of output file
             2 -> input .txt file to be places at bottom of output file
             3 -> output file path (recommended ../Results/<filename>.txt
# Date: Oct 2019

cat $1 > $3
cat $2 >> $3

echo "Merged File is"
cat $3
