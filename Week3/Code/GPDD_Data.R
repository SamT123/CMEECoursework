require("maps")
load("../Data/GPDDFiltered.RData")
maps::map("world")
points(gpdd$long,gpdd$lat,col=2,pch=4, cex=0.5)

# disproportinate measurements in UK and West Coast of USA - so clearly not globally representative. Further, might mean there is a bias towards coastal regions