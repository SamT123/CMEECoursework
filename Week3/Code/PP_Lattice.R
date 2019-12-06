
## Script: PP_Lattice.R
## Author: Sam Turner sat19@ic.ac.uk
## About: Feeding interaction and body size plots.

# This script produces density plots and averages of prey size, predator size, and size ratio.
# Plots are faceted by feeding interaction type.
# Also saves to csv the mean and medians of predator size, prey size, and mass ratio for each 
# feeding interaction type, both logged and non-logged. 

# OUTPUTS :     ../Results/Pred_Lattice.pdf         =   density plot of predator size, faceted by feeding interation type
#               ../Results/Prey_Lattice.pdf         =   density plot of prey size, faceted by feeding interation type
#               ../Results/SizeRatio_Lattice.pdf    =   density plot of size ratio, faceted by feeding interation type
#               ../Results/PP_results_non_log.pdf   =   non-logged means and medians
#               ../Results/PP_results_non_log.pdf   =   logged means and medians

# clear environment
rm(list=ls())

# load dependencies
require(dplyr)
require(lattice)

# load data
MyDF <- read.csv("../Data/EcolArchives-E089-51-D1.csv")

# convert prey mass units to grams
MyDF[MyDF$Prey.mass.unit == "mg",]$Prey.mass = MyDF[MyDF$Prey.mass.unit == "mg",]$Prey.mass / 1000
MyDF$Prey.mass.unit = "g"

print("Making plots...")
# PREDATOR MASS #

# make density plot of predator mass faceted by Type.of.feeding.interaction
pdf("../Results/Pred_Lattice.pdf", # Open blank pdf page using a relative path
    11.7, 8.3)

densityplot(~log(Predator.mass) | Type.of.feeding.interaction, data=MyDF)
dev.off();


# PREY MASS #

# make density plot of prey mass faceted by Type.of.feeding.interaction
pdf("../Results/Prey_Lattice.pdf", # Open blank pdf page using a relative path
    11.7, 8.3)
densityplot(~log(Prey.mass) | Type.of.feeding.interaction, data=MyDF)
dev.off();


# MASS RATIO #

# make density plot of mass ratio faceted by Type.of.feeding.interaction
pdf("../Results/SizeRatio_Lattice.pdf", # Open blank pdf page using a relative path
    11.7, 8.3)
densityplot(~log(Prey.mass/Predator.mass) | Type.of.feeding.interaction, data=MyDF)
dev.off();

print("Finding means...")

# AVERAGES #

# find mean and median predator mass, prey mass, and size ratio
meanPred = mean(MyDF$Predator.mass)
medPred = median(MyDF$Predator.mass)

meanPrey = mean(MyDF$Prey.mass)
medPrey = median(MyDF$Prey.mass)

meanRatio = mean(MyDF$Prey.mass/MyDF$Predator.mass)
medRatio = median(MyDF$Prey.mass/MyDF$Predator.mass)

# save averages to output file
d = data.frame(row.names = c('predator', 'prey', 'ratio'),'mean.g'=c(meanPred,meanPrey,meanRatio),'median.g'=c(medPred,medPrey,medRatio))
write.csv(d, '../Results/PP_Results_non_log.csv')


# LOG AVERAGES #

# find means and medians of log mass, faceted by interaction type
outmat <- MyDF %>%
  group_by(Type.of.feeding.interaction) %>%
  summarize(mean_Pred = mean(log(Predator.mass), na.rm = TRUE),
            mean_Prey = mean(log(Prey.mass), na.rm = TRUE),
            mean_Ratio = mean(log(Prey.mass/Predator.mass)),
            med_Pred = median(log(Predator.mass), na.rm = TRUE),
            med_Prey = median(log(Prey.mass), na.rm = TRUE),
            med_Ratio = median(log(Prey.mass/Predator.mass)))


# produce and save matrix with appropriate column headings
outmat <- data.frame(outmat)

colnames(outmat) <- c('Feeding interaction type',
                      'Mean log Pred size (g)',
                      'Mean log Prey size (g)',
                      'Mean log Size Ratio',
                      'Median log Pred size (g)',
                      'Median log Prey size (g)',
                      'Median log Size Ratio')

write.csv(outmat, "../Results/PP_Results.csv")

