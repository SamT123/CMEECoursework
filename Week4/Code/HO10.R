d<-read.table("../Data/SparrowSize.txt", header=TRUE)
plot(d$Mass~d$Tarsus, ylab="Mass (g)", xlab="Tarsus (mm)", pch=19, cex=0.4)

d1<-subset(d, d$Mass!="NA")
d2<-subset(d1, d1$Tarsus!="NA")
length(d2$Tarsus)

model1<-lm(Mass~Tarsus, data=d2)
summary(model1)
model1

hist(model1$residuals)

head(model1$residuals)


x<-c(1:100)
b<-0.5
m<-1.5
y<-m*x+b
plot(x,y, xlim=c(0,100), ylim=c(0,100), pch=19, cex=0.5)

model2<-lm(y~x)
summary(model2)

d2$z.Tarsus<-scale(d2$Tarsus)
model3<-lm(Mass~z.Tarsus, data=d2)
summary(model3)


d4<-subset(d, d$Wing!="NA")
m4<-lm(Wing~Sex, data=d4)
t4<-t.test(d4$Wing~d4$Sex, var.equal=TRUE)
summary(m4)


d5 <- subset(d, d$Bill != "NA")
d6 <- subset(d5, d$Mass != "NA")
m5 <- lm(Mass~Bill, data=d6)