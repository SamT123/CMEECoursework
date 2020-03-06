#!/bin/bash

# Author:  Sam Turner sat19@ic.ac.uk
# Script:  CompileLaTeX.sh
# Desc:    Compiles a pdf from [name].tex and referenced .bib file, which must
#          be in same directory. [name].pdf is saved in specified directory, and opened
# Arguments: 1 -> filename for .tex file without extension eg. FirstExample
#            2 -> directory to save to
# Date: Oct 2019


# Compile LaTeX document


texcount -1 write_up.tex > write_up1.sum
cat write_up1.sum | head -c 4 > write_up.sum

pdflatex "write_up.tex"
pdflatex "write_up.tex"
bibtex "write_up"
pdflatex "write_up.tex"
pdflatex "write_up.tex"


# Move document to specified location
#mv $1.pdf $2$1.pdf 

# Open document
# open $2$1.pdf

# Remove extra files created by pdflatex
rm *~
rm *.aux
rm *.dvi
rm *.log
rm *.nav
rm *.out
rm *.snm
rm *.toc
rm *.bbl
rm *.blg
