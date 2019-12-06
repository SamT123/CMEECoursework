## Script:  TreeHeight.R
## Author:  Sam Turner sat19@ic.ac.uk

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
  print(paste("Tree height is:", height))

  return (height)
}

# read in data
MyData <- read.csv("../Data/trees.csv", header = TRUE)

# add column containing tree heights calculated using mapply
MyData$Tree.Height.m <- mapply(function (i,j) TreeHeight(i,j), MyData['Angle.degrees'], MyData['Distance.m'])

# write output csv
write.csv(MyData, "../Results/TreeHts.csv")
