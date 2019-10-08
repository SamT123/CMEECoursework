#!/bin/bash
# Author: Sam Turner sat19@ic.ac.uk
# Script: csvtospace.sh
# Desc: substitute commas in specified file with spaces, saved at ../Results/ <filename.csv>.txt
# Arguments: 1-> comma delimited file
# Date: Oct 2018

echo "Creating a space delimited version of $1 ..."
cat $1 | tr -s "," " " >> ../Results/$(basename $1).txt
echo "Done!"
exit
