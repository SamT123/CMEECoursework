# This function calculates heights of trees given distance of each tree 
# from its base and angle to its top, using  the trigonometric formula 
#
# height = distance * tan(radians)
#
# ARGUMENTS
# degrees:   The angle of elevation of tree
# distance:  The distance from base of tree (e.g., meters)
#
# OUTPUT
# The heights of the tree, same units as "distance"



TreeHeight <- function(degrees, distance){
  radians <- degrees * pi / 180
  height <- distance * tan(radians)

  return (height)
}

# get file name from command line arg
if (length( commandArgs(trailing = T) ) == 0 ){
  print("Need input file")
} else {
  fname = commandArgs(trailing = T)

  # read in tree distance and angle data
  MyData <- read.csv(file = fname, header = TRUE)

  # calculate heights
  MyData$Tree.Height.m <- mapply(function (i,j) TreeHeight(i,j),MyData['Angle.degrees'], MyData['Distance.m'])

  # get file basename
  fbase = tools::file_path_sans_ext(basename(fname))
  writepath = paste("../Results/", fbase, "_treeheights.csv", sep = "")

  # save dataset
  write.csv(MyData, writepath)

}