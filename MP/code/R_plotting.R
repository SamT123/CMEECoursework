############
# PACKAGES #
############
require(dplyr)
require(ggplot2)
rm(list = ls())
graphics.off()
options("scipen"=100, "digits"=4)



#############
# LOAD DATA #
#############

data <- read.csv("../data/LogisticGrowthData.csv")




#################
# PLOT SCATTERS #
#################
n<-0
for (s in unique(data$Species)){
  d <- dplyr::filter(data, Species == s)
  d$Temp <- as.factor(d$Temp)
  p <- ggplot(d, aes(x = Time, PopBio, colour = Temp)) + geom_point()
  p <- p + facet_wrap(vars(Medium),nrow = length(unique(d$Medium)),scales='free') + theme_bw() + xlab(paste("Time / ", d$Time_units)) + ylab(paste("Population Biomass / ", d$PopBio_units)) + labs(color="Temperature / °C") + ggtitle(s) + guides(fill=guide_legend(title="Temperature / °C"))
  ggsave(paste("../results/",n,"_", s, ".pdf"))
  n<-n+1
}



