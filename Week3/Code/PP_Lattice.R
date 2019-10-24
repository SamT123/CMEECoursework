
require(dplyr)
MyDF <- read.csv("../Data/EcolArchives-E089-51-D1.csv")

library(lattice)
pdf("../Results/Pred_Lattice.pdf", # Open blank pdf page using a relative path
    11.7, 8.3)
densityplot(~log(Predator.mass) | Type.of.feeding.interaction, data=MyDF)
graphics.off();

pdf("../Results/Prey_Lattice.pdf", # Open blank pdf page using a relative path
    11.7, 8.3)
densityplot(~log(Prey.mass) | Type.of.feeding.interaction, data=MyDF)
graphics.off();

pdf("../Results/SizeRatio_Lattice.pdf", # Open blank pdf page using a relative path
    11.7, 8.3)
densityplot(~log(Prey.mass/Predator.mass) | Type.of.feeding.interaction, data=MyDF)
graphics.off();


meanPred = mean(MyDF$Predator.mass)
medPred = median(MyDF$Predator.mass)

meanPrey = mean(MyDF$Prey.mass)
medPrey = median(MyDF$Prey.mass)

meanRatio = mean(MyDF$Prey.mass/MyDF$Predator.mass)
medRatio = median(MyDF$Prey.mass/MyDF$Predator.mass)

d = data.frame(row.names = c('predator', 'prey', 'ratio'),'mean.g'=c(meanPred,meanPrey,meanRatio),'median.g'=c(medPred,medPrey,medRatio))
write.csv(d, '../Results/PP_Results_non_log.csv')


#ddply(MyDF,~,summarise,mean=mean(age),sd=sd(age))

dplyr::glimpse(MyDF)


outmat <- MyDF %>%
  group_by(Type.of.feeding.interaction) %>%
  summarize(mean_Pred = mean(log(Predator.mass), na.rm = TRUE), mean_Prey = mean(log(Prey.mass), na.rm = TRUE), mean_Ratio = mean(log(Prey.mass/Predator.mass)),
    med_Pred = median(log(Predator.mass), na.rm = TRUE), med_Prey = median(log(Prey.mass), na.rm = TRUE), med_Ratio = median(log(Prey.mass/Predator.mass)))


outmat <- data.frame(outmat)

colnames(outmat) <- c('Feeding interaction type', 'Mean log Pred size (g)' , 'Mean log Prey size (g)', "Mean log Size Ratio", 'Median log Pred size (g)' , 'Median log Prey size (g)', "Median log Size Ratio")

write.csv(outmat, "../Results/PP_Results.csv")