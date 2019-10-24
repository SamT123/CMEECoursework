rm(list = ls())

ls(envir = .GlobalEnv)

d <- read.table("../Data/SparrowSize.txt", header = T)

d1<-subset(d, d$Tarsus!="NA"); seTarsus<-sqrt(var(d1$Tarsus)/length(d1$Tarsus)); seTarsus

d12001<-subset(d1, d1$Year==2001); seTarsus2001<-sqrt(var(d12001$Tarsus)/length(d12001$Tarsus)); seTarsus2001



seT <- sqrt(var( d$Tarsus, na.rm = T) / sum(!is.na(d$Tarsus)))
CIseT <- c(mean(d$Tarsus, na.rm = T) - seT, mean(d$Tarsus, na.rm = T) + seT)

seW <- sqrt(var( d$Wing, na.rm = T) / sum(!is.na(d$Wing)))
CIseW <- c(mean(d$Wing, na.rm = T) - seW, mean(d$Wing, na.rm = T) + seW)

seB <- sqrt(var( d$Bill, na.rm = T) / sum(!is.na(d$Bill)))
CIseB <- c(mean(d$Bill, na.rm = T) - seB, mean(d$Bill, na.rm = T) + seB)


d01 <- d[d$Year == 2001,]
seT01 <- sqrt(var( d01$Tarsus, na.rm = T) / sum(!is.na(d01$Tarsus)))
CIseT01 <- c(mean(d01$Tarsus, na.rm = T) - seT01, mean(d01$Tarsus, na.rm = T) + seT01)

seW01 <- sqrt(var( d01$Wing, na.rm = T) / sum(!is.na(d01$Wing)))
CIseW01 <- c(mean(d01$Wing, na.rm = T) - seB01, mean(d01$Wing, na.rm = T) + seW01)

seB01 <- sqrt(var( d01$Bill, na.rm = T) / sum(!is.na(d01$Bill)))
CIseB01 <- c(mean(d01$Bill, na.rm = T) - seB01, mean(d01$Bill, na.rm = T) + seB01)

