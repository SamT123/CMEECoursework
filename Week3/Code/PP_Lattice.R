# Density plots and averages of prey size, predator size, and size ratio:; faceted by feeding interaction type

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


# make density plot of predator mass faceted by Type.of.feeding.interaction
pdf("../Results/Pred_Lattice.pdf", # Open blank pdf page using a relative path
    11.7, 8.3)

densityplot(~log(Predator.mass) | Type.of.feeding.interaction, data=MyDF)

dev.off();

# make density plot of prey mass faceted by Type.of.feeding.interaction
pdf("../Results/Prey_Lattice.pdf", # Open blank pdf page using a relative path
    11.7, 8.3)
densityplot(~log(Prey.mass) | Type.of.feeding.interaction, data=MyDF)
dev.off();

# make density plot of mass ratio faceted by Type.of.feeding.interaction
pdf("../Results/SizeRatio_Lattice.pdf", # Open blank pdf page using a relative path
    11.7, 8.3)
densityplot(~log(Prey.mass/Predator.mass) | Type.of.feeding.interaction, data=MyDF)
dev.off();


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


#ddply(MyDF,~,summarise,mean=mean(age),sd=sd(age))


# find means and medians, faceted by interaction type
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

