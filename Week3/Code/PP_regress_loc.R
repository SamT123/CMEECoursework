require(ggplot2)
require(dplyr)
MyDF <- read.csv("../data/EcolArchives-E089-51-D1.csv")


lifestages <- unique(MyDF$Predator.lifestage)
interactions <- unique(MyDF$Type.of.feeding.interaction)
locations <- unique(MyDF$Location)

rows = length(lifestages)*length(interactions)*length(locations)


outmat <- data.frame(matrix(ncol = 8, nrow = rows))
x <- c("lifestage", "interaction","location", "regression.slope", "regression.intercept", "R2", "F.statistic.value",  "p-value")
colnames(outmat) <- x

i<-0

for (interaction in interactions){
    for (lifestage in lifestages){
        for (location in locations){


            d = MyDF[MyDF$Predator.lifestage == lifestage, ][MyDF$Type.of.feeding.interaction == interaction, ][MyDF$Location == location, ]

            if ( dim(d['Predator.mass'])[[1]] - sum(is.na(d['Predator.mass'])) > 3 & dim(d['Prey.mass'])[[1]] - sum(is.na(d['Prey.mass'])) > 3 ){

            
                
                l=lm(Predator.mass~Prey.mass, data = MyDF[MyDF$Predator.lifestage == lifestage, ][MyDF$Type.of.feeding.interaction == interaction, ])
                s=summary(l)
                # print(c(lifestage, interaction, s$coefficients['Prey.mass','Estimate'], s$coefficients['(Intercept)','Estimate'], s$r.squared, s$fstatistic['value'], 10))
                outmat[i,]<-c(lifestage, interaction,location, s$coefficients['Prey.mass','Estimate'], s$coefficients['(Intercept)','Estimate'], s$r.squared, s$fstatistic['value'], s$coefficients[2,4])
            }
            
            else {
                outmat[i,] <- c(lifestage, interaction, location, NA, NA, NA, NA, NA)
            }
            i <- i + 1
        }
    }
}
write.csv(outmat, '../Results/PP_regress_results.csv')