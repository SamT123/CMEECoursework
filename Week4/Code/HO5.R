rm(list=ls())
getwd()
d<-read.table("../Data/SparrowSize.txt", header=TRUE)

boxplot(d$Mass~d$Sex.1, col = c("red", "blue"), ylab="Body mass (g)")

t.test1 <- t.test(d$Mass~d$Sex.1)
t.test1

d1<-as.data.frame(head(d, 50))
length(d1$Mass)
t.test2 <- t.test(d1$Mass~d1$Sex)
t.test2



d01 <- d[d$Year == 2001,]
Wmean <- mean(d$Wing, na.rm = T)

t.test3 <- t.test(d01$Wing, mu = Wmean,na.rm = T)


t.test4 <- t.test(d01$Wing~d01$Sex,na.rm = T)

t.test5 <- t.test(d$Wing~d$Sex, na.rm = T)

t.test6 <- t.test(d$Tarsus~d$Sex, na.rm = T)

#install.packages("pwr")

require("pwr")



myd <- 5 / sqrt(var(d$Wing, na.rm = T))

pwr.t.test( d = myd , sig.level = 0.05, power = 0.80, type = c("two.sample") )