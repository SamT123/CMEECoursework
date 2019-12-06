# This function calculates heights of trees given distance of each tree 
# from its base and angle to its top, using  the trigonometric formula:
#
# height = distance * tan(radians)
#
# ARGUMENTS
# degrees:   The angle of elevation of tree
# distance:  The distance from base of tree (e.g., meters)
#
# OUTPUT
# The heights of the tree, same units as "distance"

rm(list=ls())

TreeHeight <- function(degrees, distance){
  radians <- degrees * pi / 180
  height <- distance * tan(radians)

  return (height)
}

# get file name from command line arg
if (length( commandArgs(trailing = T) ) == 0 ){
  print("No input file specified: using default trees.csv")
  fname = "../Data/trees.csv"
} else {
  fname = commandArgs(trailing = T)[1]
}

# read in tree distance and angle data
MyData <- read.csv(file = fname, header = TRUE)

# calculate heights
MyData$Tree.Height.m <- mapply(function (i,j) TreeHeight(i,j),MyData['Angle.degrees'], MyData['Distance.m'])

# get file basename
fbase = tools::file_path_sans_ext(basename(fname))
writepath = paste("../Results/", fbase, "_treeheights.csv", sep = "")

# save dataset
print("Saving output csv to ../Results/trees_treeheights.csv...")
write.csv(MyData, writepath)
