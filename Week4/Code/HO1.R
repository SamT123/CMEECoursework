getwd()
#setwd("Week4/Code")
myNumericVector <- c(1.3,2.5,1.9,3.4,5.6,1.4,3.1,2.9)
myCharacterVector <- c("low","low","low","low","high","high","high","high")
myLogicalVector <- c(TRUE,TRUE,FALSE,FALSE,TRUE,TRUE,FALSE,FALSE)

str(myNumericVector)
str(myCharacterVector)

myMixedVector <-c(1, TRUE, FALSE, 3, "help", 1.2, TRUE, "notwhatIplanned")
str(myMixedVector)

library(lme4)
require(lme4)

rm(list = ls())

ls(envir = .GlobalEnv)

d <- read.table("../Data/SparrowSize.txt", header = T)
str(d)

#require("somebullshit")
#library("somebullshit")

head(d)

mode(c(0,0,0,0,1,2,2))

hist(d$Tarsus, breaks = 100, col="grey")

require(ggplot2)
require(gridExtra)
#install.packages('gridExtra')


p1 <- qplot(Bill, data = d, geom =  "histogram")
p2 <- qplot(Mass, data = d, geom =  "histogram")
p3 <- qplot(Wing, data = d, geom =  "histogram")
p4 <- qplot(Tarsus, data = d, geom =  "histogram")


grid.arrange(p1, p2, p3, p4, nrow = 2)



mean(d$Bill, na.rm = T)
var(d$Bill, na.rm = T)
sqrt(var(d$Bill, na.rm = T))

mean(d$Mass, na.rm = T)
var(d$Mass, na.rm = T)
sqrt(var(d$Mass, na.rm = T))