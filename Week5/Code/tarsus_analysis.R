

tarsus <- read.table("tarsus.csv", sep = ',', header = T)

b = seq(min(tarsus$Tarsus) - 1, max(tarsus$Tarsus) + 1, 0.5)

hist(tarsus$Tarsus, breaks = b)
head(tarsus)