#!/bin/bash
# Author: Sam Turner sat19@ic.ac.uk
# Script: CountLines.sh
# Desc: count the number of lines in the file specified in the argument
# Arguments: 1 -> text file
# Date: Oct 2018

if [ -z "$1" ]
then
    echo "Error. Path to file required."
    exit
fi

NumLines=`wc -l < $1`
echo "The file $1 has $NumLines lines"
echo
