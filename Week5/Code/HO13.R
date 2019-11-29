rm(list = ls())
d<-read.table("../Data/SparrowSize.txt", header=TRUE)


d1<-subset(d, d$Wing!="NA")
summary(d1$Wing)
hist(d1$Wing)

model1<-lm(Wing~Sex.1,data=d1)
summary(model1)

anova(model1)

t.test(d1$Wing~d1$Sex.1, var.equal=TRUE)

require(dplyr)
tbl_df(d1)

glimpse(d1)
d$Mass %>% cor.test(d$Tarsus, na.rm=TRUE)

d1 %>%
group_by(BirdID) %>%
summarise (count=length(BirdID))

d1 %>%
group_by(BirdID) %>%
summarise (count=length(BirdID)) %>%
count(count)

LMM no p values - that's ok, look at parameter estimate and compoare to stadnatd error -does 1.96 go past zero for estimate?