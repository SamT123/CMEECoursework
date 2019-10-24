# regressions by lifestage and interaction

require(ggplot2)
require(dplyr)
MyDF <- read.csv("../data/EcolArchives-E089-51-D1.csv")


p <- ggplot(MyDF, aes(log(Prey.mass),log(Predator.mass), colour = Predator.lifestage))
p <- p + guides(fill=guide_legend(nrow=1))

p <- p + geom_point(shape = 3)

p <- p + facet_grid(Type.of.feeding.interaction ~ .) + theme(strip.text.x = element_text(size = 80, colour = "orange", angle = 90))

p <- p + geom_smooth(method = "lm",fullrange = TRUE)


p <- p + theme_bw()

p <- p + theme(legend.position = "bottom") + xlab("Prey mass in grams") + ylab("Predator mass in grams") 


p <- p + theme(axis.text = element_text(size = 10), axis.title = element_text(size=10))
p <- p + theme(strip.text = element_text(size = I(6), face = I('bold') ))


pdf("../Results/CopyFigure.pdf")
p
graphics.off();


lifestages <- unique(MyDF$Predator.lifestage)
interactions <- unique(MyDF$Type.of.feeding.interaction)
rows = length(lifestages)*length(interactions)

outmat <- data.frame(matrix(ncol = 7, nrow = rows))
x <- c("lifestage", "interaction", "regression.slope", "regression.intercept", "R2", "F.statistic.value",  "p-value")
colnames(outmat) <- x

i<-0

for (interaction in interactions){
    for (lifestage in lifestages){

        d = MyDF[MyDF$Predator.lifestage == lifestage, ][MyDF$Type.of.feeding.interaction == interaction, ]
        print(dim(d))
        if ( dim(d['Predator.mass'])[[1]] - sum(is.na(d['Predator.mass'])) > 3 & dim(d['Prey.mass'])[[1]] - sum(is.na(d['Prey.mass'])) > 3){

        
            
            l=lm(Predator.mass~Prey.mass, data = MyDF[MyDF$Predator.lifestage == lifestage, ][MyDF$Type.of.feeding.interaction == interaction, ])
            s=summary(l)
            # print(c(lifestage, interaction, s$coefficients['Prey.mass','Estimate'], s$coefficients['(Intercept)','Estimate'], s$r.squared, s$fstatistic['value'], 10))
            outmat[i,]<-c(lifestage, interaction, s$coefficients['Prey.mass','Estimate'], s$coefficients['(Intercept)','Estimate'], s$r.squared, s$fstatistic['value'], s$coefficients[2,4])
        }
        
        else {
            outmat[i,] <- c(lifestage, interaction, NA, NA, NA, NA, NA)
        }
        i <- i + 1
    }

}
write.csv(outmat, '../Results/PP_regress_results.csv')


# MyDF[MyDF$Predator.lifestage = '',][MyDF$Type.of.feeding.interaction = '',]

# outmat <- MyDF %>%
#   group_by(Type.of.feeding.interaction) %>% 
#   do(lm(Predator.mass~Prey.mass, data=.) %>% coef %>% as_data_frame)

# outmat <- MyDF %>%
#   group_by(Type.of.feeding.interaction + Predator.lifestage) %>%
#   summarize(mean_Pred = mean(log(Predator.mass), na.rm = TRUE), mean_Prey = mean(log(Prey.mass), na.rm = TRUE), mean_Ratio = mean(log(Prey.mass/Predator.mass)),
#     med_Pred = median(log(Predator.mass), na.rm = TRUE), med_Prey = median(log(Prey.mass), na.rm = TRUE), med_Ratio = median(log(Prey.mass/Predator.mass)))



# dplyr::glimpse(MyDF)
