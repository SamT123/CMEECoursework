# Week 3
Coursework for CMEE week 3.
## Topics:
* R

## Requirements
* `R 3.6`
* `Python 3.7`
* `ggplot`
* `dplyr`
* `tidyr`
* `maps`

## Contents
### [Code](https://github.com/SamT123/CMEECoursework/tree/master/Week3/Code)
**apply1.R**
* Demonstrate apply function.

**apply2.R**
* Demosntrate apply function to sum a matrix.

**autocorrelation.tex**
* .tex file to compile to autocorrelation write-up.

**basic_io.R**
* csv input and output.

**boilerplate.R**
* Demonstrate R function.

**break.R**
* Demonstrate loop break.

**browse.R**
* Demostrate browser for debugging.

**CompileLaTeX_no_bib.sh**
* Compile latex document with no bibliography.
* Example usage:
`bash CompileLaTeX_no_bib autocorrelation ../Results`

**control_flow.R**
* Demonstrate looping and control flow.

**DataWrang.R**
* Data wrangling using base R.
* Conversion from wide format to long format.

**DataWrangTidy.R**
* Data wrangling using tidyr.
* Conversion from wide format to long format.

**TreeHeight.R**
* Calculate tree heights of trees in ../Data/trees.csv.

**get_TreeHeight.R**
* Find tree heights from distance to tree and angle to treetop data for specified csv. Default data is used if none provided.
* Produces output with tree height column appended.
* Example usage:
`Rscript get_TreeHeight.R ../Data/trees.csv`

**get_TreeHeight.py**
* Find tree heights from distance to tree and angle to treetop data. Default data is used if none provided.
* Produces output with tree height column appended.
* Example usage:
`python3 get_TreeHeight.py ../Data/trees.csv`

**run_get_treeheight.sh**
* Run .R and .py treeheight programs. Uses command line input file argument, or, if absent, default input file.
* Example usage:
`bash run_get_treeheight.sh ../Data/trees.csv`

**Girko.R**
* Plots eigenvalues of random real matrix, demonstrating Girko's Circular Law.

**GPDD_Data.R**
* Plots positions of samples for species observation data.

**MyBars.R**
* Demonstrate building a plot with ggplot2.

**next.R**
* Demonstrate passing to next iteration in for loop.

**plotLin.R**
* Demonstrate building linear regression plot with ggplot2.

**PP_Lattice**
* Make lattice plots for predator size, prey size, and size ratio faceted by feeding interation type.
* Save means and medians of predator size, prey size, and size ratio, for each interaction type.

**PP_regress.R**
* Plot regressions of predator size against prey size, faceted by interaction type and predator life stage.
* Save summary statistics of each regression.

**PP_regress_loc.R**
* Calculate and save summary statistics for linear regressions of of predator size against prey size, faceted by interaction type, location, and predator life stage.

**preallocate.loc**
* Demonstrate speed advantage of preallocation for R vectors.

**Ricker.R**
* Calculate population size time series from Ricker model.

**sample.R**
* Compare speeds when using: loops vs vectorization; preallocation vs reallocation.

**TAutoCorr.R**
* Calculate p value for autocorrelation in Key West Temperature data.
* Plots figures for inclusion in autocorrelation.pdf write-up.

**try.R**
* Demonstrate try function.

**Vectorize1.R**
* Compare times to sum elements of 1000 * 1000 matrix by: looping; or by built-in sum() function.

**Vectorize1.py**
* Compare times to sum elements of 1000 * 1000 matrix by: looping; or by numpy sum() function.

**Vectorize2.R**
* Compare times to simulate 1000 stochastic Ricker runs by: looping; or vectorization with vector arithmatic.

**Vectorize2.py**
* Compare times to simulate 1000 stochastic Ricker runs by: looping; or vectorization with numpy array arithmatic.

**VectorizeTimes.sh**
* Run Vectorize1.{py, R} and Vectorize2.{py, R} to demonstrate advantage of vectorization.

### [Data](https://github.com/SamT123/CMEECoursework/tree/master/Week3/Data)
**EcolArchives-E089-51-D1.csv**
* Feeding interactions data

**GPDDFiltered.RData**
* Species observation data with locations

**KeyWestAnnualMeantemperature.RData**
* Annual temperatures in Key West for 1901-2000

**PoundHillData.csv**
* Species observation data in wide format

**PoundHillMetaData.csv**
* Metadata for PoundHill.csv dataset

**Results.csv**
* Data for bar plot demonstration

**trees.csv**
* Field data with distance to tree and angle to treetop to convert to tree height

### [Results](https://github.com/SamT123/CMEECoursework/tree/master/Week3/Results)
**autocorrelation.pdf**
* Compiled Key West autocorrelation write-up
