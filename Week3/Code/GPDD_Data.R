## Script: GPDD_Data.R
## Author: Sam Turner sat19@ic.ac.uk
## About: Plot location of species observation data on world map

# clear workspace
rm(list=ls())

# load dependencies
require("maps")

print("Drawing map...")
# load data
load("../Data/GPDDFiltered.RData")

# draw map
map(database = "world", fill=TRUE, col="white", 
    bg = "#94e0ff", ylim = c(-60,90), border = "grey")

# add points to map
points(gpdd$long,gpdd$lat,col=2,pch=4, cex=0.5)

# There is a disproportinate number of measurements in UK and West Coast of USA.
# Results from this dataset are not necessarily representative of patterns in other regions
# (particularly those with highly disctinct climates). Similarly, there
# is a bias towards coastal regions