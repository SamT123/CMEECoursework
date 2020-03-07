#!/bin/bash

# Author:  Sam Turner sat19@ic.ac.uk
# Script:  clean_up.sh
# Desc:    removes files created by running run_MiniProject, including write up - restoring MiniProject directory to original state.
# Arguments: none
# Date: March 2020


rm ../results/*.pdf
rm ../report/write_up.pdf
rm ../data/LogisticGrowthDataLogClean.csv
rm ../data/inits.csv
rm ../data/*.rds