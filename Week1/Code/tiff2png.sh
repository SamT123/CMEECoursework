#!/bin/bash
# Author: Sam Turner sat19@ic.ac.uk
# Script: tiff2png.sh
# Desc: Convert all .tif files in ../Data/ to .png files, which are saved at ../Results/<input_name>.png
# Arguments: none
# Date: Oct 2019

for f in ../Data/*.tif;
    do
        echo "Converting $f";
        convert "$f" "../Results/$(basename "$f" .tif).jpg";
    done
