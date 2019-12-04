require("maps")
load("../Data/GPDDFiltered.RData")
# draw map


map(database = "world", fill=TRUE, col="white", 
    bg = "#94e0ff", ylim = c(-60,90), border = "grey")


# add points to map
points(gpdd$long,gpdd$lat,col=2,pch=4, cex=0.5)

# disproportinate number of measurements in UK and West Coast of USA - so clearly not globally representative. Further, might mean there is a bias towards coastal regions