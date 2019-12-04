#!/bin/bash
# Author: Sam Turner sat19@ic.ac.uk
# Script: tiff2png.sh
# Desc: Convert all .tif files in ../Data/ to .png files, which are saved at ../Results/<input_name>.png
# Arguments: none
# Date: Oct 2019


# loop over all *.tif files in ../Data
for f in ../Data/*.tif;
    do
        # Do conversion and save as .jpg
        echo "Converting $f";
        convert "$f" "../Results/$(basename "$f" .tif).jpg";
    done
