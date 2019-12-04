# Week 1
Coursework for CMEE week 1.
## Topics:
* UNIX
* Shell scripting
* LaTex
* Git
## Contents
### [Code](https://github.com/SamT123/CMEECoursework/tree/master/Week2/Code)
**UnixPrac1.txt**

**boilerplate.sh**	
- `I am a boilerplate. I like to boil plates. Give me a plate. - Oenone Scott 2019`
- Boilerplate script demonstrating essential features of a shell script

**tabtocsv.sh**
- Converts tab separated file to comma separated file
- Example usage:
`bash tabtocsv.sh ../SandBox/test.txt`

**variables.sh**
- Demonstate variable assignment

**MyExampleScript.sh**
- Demonstrate environment variables

**CountLines.sh**
- Count the lines in a file passed as an argument
- Example usage:
`bash CountLines.sh testfile.txt`

**ConcatenateTwoFiles.sh**
- Append the content of file 2 to the end of file 1, saving as file 3
- Example usage:
`bash ConcatenateTwoFiles.sh ../Sandbox/file1.txt ../Sandbox/file2.txt ../Results/Concat.txt`

**tiff2png.sh**
- Convert file.tif  to file.jpeg file, saving output at ../Results/file.jpg
- Example usage:
`bash tif2jpg.sh ../Data/GMARBLES.tif`

**csvtospace.sh**
- Convert comma separated file to space separated file
- Example usage:
`bash csvtospace.sh ../Data/Temperatures/1801.csv`

**CompileLaTeX.sh**
- Compile a pdf from name.tex and referenced .bib file, which must be in same directory. Saves compiled pdf to specified directory.
- Example usage:
`bash CompileLaTeX.sh FirstExample ../Results/`

**FirstExample.tex**
- Example LaTeX document

**FirstBiblio.bib**
- Example LaTeX bibliography

## [Data](https://github.com/SamT123/CMEECoursework/tree/master/Week2/Data)

**GMARBLES.tif**

**Temperatures/**
- csv files to convert to space delimited value files

**fasta/**
- fasta files for UnixPrac1.txt

## [Results](https://github.com/SamT123/CMEECoursework/tree/master/Week2/Results)
