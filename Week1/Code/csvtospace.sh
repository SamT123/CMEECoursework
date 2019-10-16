#!/bin/bash
# Author: Sam Turner sat19@ic.ac.uk
# Script: csvtospace.sh
# Desc: substitute commas in specified file with spaces, saved at ../Results/ <filename>.txt
# Arguments: 1-> comma delimited file
# Date: Oct 2018

echo "Creating a space delimited version of $1 ..."
cat $1 | tr -s "," " " >> ../Results/$(basename $1 | cut -f 1 -d '.').txt
echo "Done!"
exit
