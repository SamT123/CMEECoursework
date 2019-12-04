# Calculate linear regressions of Prey mass vs Predator mass, faceted by feedig interaction type, location and predator life stage

require(ggplot2)
require(dplyr)

# load data
MyDF <- read.csv("../Data/EcolArchives-E089-51-D1.csv")
# convert prey mass units to grams
MyDF[MyDF$Prey.mass.unit == "mg",]$Prey.mass = MyDF[MyDF$Prey.mass.unit == "mg",]$Prey.mass / 1000
MyDF$Prey.mass.unit = "g"

# get vectors of unique lifestages, interactions, location
lifestages <- as.vector(unique(MyDF$Predator.lifestage))
interactions <- as.vector(unique(MyDF$Type.of.feeding.interaction))
locations <- as.vector(unique(MyDF$Location))

# calculate number of rows in output dataframe
rows = length(lifestages)*length(interactions)*length(locations)

# initialise output dataframe with appropriate column headings
outmat <- data.frame(matrix(ncol = 8, nrow = rows))
x <- c("lifestage", "interaction","location", "regression.slope", "regression.intercept", "R2", "F.statistic.value",  "p-value")
colnames(outmat) <- x


i<-0

# loop over interaction types, lifestages, and locations
for (interaction in interactions){
    for (lifestage in lifestages){
        for (location in locations){
            # take the specified subset of the data
            d = MyDF[MyDF$Predator.lifestage == lifestage, ][MyDF$Type.of.feeding.interaction == interaction, ][MyDF$Location == location, ]
            
            # require at east 3 non-NA predator mass and prey mass values to fit linear model
            if (sum(!is.na(d['Predator.mass'])) > 3 &  sum(!is.na(d['Prey.mass'])) > 3 ){
                
                # fit linear model
                l=lm(Predator.mass~Prey.mass, data = MyDF[MyDF$Predator.lifestage == lifestage, ][MyDF$Type.of.feeding.interaction == interaction, ])
                # get summary of linear model
                s=summary(l)
                # write line of output dataframe
                outmat[i,]<-c(lifestage, interaction,location, s$coefficients['Prey.mass','Estimate'], s$coefficients['(Intercept)','Estimate'], s$r.squared, s$fstatistic['value'], s$coefficients[2,4])
            }
            # if insufficient non-NA values, enter NA values
            else {
                outmat[i,] <- c(lifestage, interaction, location, NA, NA, NA, NA, NA)
            }
            i <- i + 1
        }
    }
}
# write output to csv
write.csv(outmat, '../Results/PP_regress_results_loc.csv')



