# Calculate and plot linear regressions of Prey mass vs Predator mass, faceted by feedig interaction type and predator life stage

# load dependencies
require(ggplot2)
require(dplyr)

# load data
MyDF <- read.csv("../Data/EcolArchives-E089-51-D1.csv")
# convert prey mass units to grams
MyDF[MyDF$Prey.mass.unit == "mg",]$Prey.mass = MyDF[MyDF$Prey.mass.unit == "mg",]$Prey.mass / 1000
MyDF$Prey.mass.unit = "g"


# make plot with colour representing lifestage
p <- ggplot(MyDF, aes(log(Prey.mass),log(Predator.mass), colour = Predator.lifestage))

# specify number of legend rows
p <- p + guides(fill=guide_legend(nrow=1))

# specify point shape
p <- p + geom_point(shape = 3)

# specify facet by feeding interaction type
p <- p + facet_grid(Type.of.feeding.interaction ~ .)

# add linear regression lines
p <- p + geom_smooth(method = "lm",fullrange = TRUE)

# set theme
p <- p + theme_bw()

# specify legend position and axis labels
p <- p + theme(legend.position = "bottom") + xlab("Prey mass in grams") + ylab("Predator mass in grams") 

# specify typeface
p <- p + theme(axis.text = element_text(size = 10), axis.title = element_text(size=10))
p <- p + theme(strip.text = element_text(size = I(6), face = I('bold') ))

# save figure
pdf("../Results/CopyFigure.pdf")
print(p)
graphics.off();




# get vectors of unique lifestages, interactions
lifestages <- as.vector(unique(MyDF$Predator.lifestage))
interactions <- as.vector(unique(MyDF$Type.of.feeding.interaction))

#calculate number of rows in output dataframe
rows = length(lifestages)*length(interactions)

# initialise dataframe with appropriate columns names
outmat <- data.frame(matrix(ncol = 7, nrow = rows))
x <- c("lifestage", "interaction", "regression.slope", "regression.intercept", "R2", "F.statistic.value",  "p-value")
colnames(outmat) <- x


i<-0

# loop over each interaction
for (interaction in interactions){
    # and over each lifestage
    for (lifestage in lifestages){
        # take the specified subset of the data
        d = MyDF[MyDF$Predator.lifestage == lifestage, ][MyDF$Type.of.feeding.interaction == interaction, ]
        
        # require at east 3 non-NA predator mass and prey mass values to fit linear model
        if ( sum(!is.na(d['Predator.mass'])) > 3 & sum(!is.na(d['Prey.mass'])) > 3){
            # fit linear model
            l=lm(Predator.mass~Prey.mass, data = MyDF[MyDF$Predator.lifestage == lifestage, ][MyDF$Type.of.feeding.interaction == interaction, ])
            # get linear model summary
            s=summary(l)
            
            # write line of output dataframe
            outmat[i,]<-c(lifestage, interaction, s$coefficients['Prey.mass','Estimate'], s$coefficients['(Intercept)','Estimate'], s$r.squared, s$fstatistic['value'], s$coefficients[2,4])
        }
        
        # if insufficient number of non-NA values, write NA to output dataframe
        else {
            outmat[i,] <- c(lifestage, interaction, NA, NA, NA, NA, NA)
        }
        i <- i + 1
    }

}

# save dataframe
write.csv(outmat, '../Results/PP_regress_results.csv')


