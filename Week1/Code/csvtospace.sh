#!/bin/bash
# Author: Sam Turner sat19@ic.ac.uk
# Script: csvtospace.sh
# Desc: substitute commas in files with spaces
# saves the output into a .csv file
# Arguments: 1-> comma delimited file
# Date: Oct 2018

echo "Creating a space delimited version of $1 ..."
cat $1 | tr -s "," " " >> $1.txt
echo "Done!"
exit