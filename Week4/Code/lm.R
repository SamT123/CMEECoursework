x <- c(1,2,3,4,8)
y <- c(4,3,5,7,9)
model1 <- lm(y~x)

model1

summary(model1)

cov(x,y)


b1 <- cov(x,y) / var(x)
b0 <- mean(y) - b1*mean(x)

anova(model1)