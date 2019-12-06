#!/bin/bash
# Author: Sam Turner sat19@ic.ac.uk
# Script: tabtocsv.sh
# Description: substitute the tabs in the files with commas
# Saves the output into a .csv file in ../Results/
# Arguments: 1 -> tab delimited file
# Date: Oct 2019

if [ -z "$1" ]
then
    echo "Error. Path to tab separated file required."
    exit
fi

echo "Creating a comma delimited version of $1 ..."

# cat reads file -> tr replaces '\t' with ',' -> basename used to generate new file name
cat $1 | tr -s "\t" "," > ../Results/$(basename $1).csv
echo "Done!"
exit
