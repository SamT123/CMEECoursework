data <- read.csv("../data/LogisticGrowthData.csv") 
data$ID <- NA
combos <- unique(cbind(as.vector(data$Species), as.vector(data$Temp),as.vector(data$Medium),as.vector(data$Rep)))
ID_list <- list()
for (i in 1:305){
  combo<-combos[i,]
  species <- combo[1]
  temp <- combo[2]
  medium <- combo[3]
  repli <- combo[4]
  
  data[(data$Species == species) & (data$Temp == temp) & (data$Medium == medium) & (data$Rep == repli),]$ID <- i
  
  ID_list$i <- list("Species"=species, "Temp"=temp, "Medium"=medium, "Rep"=repli)
}
  #d<-data[(data$Species == species) & (data$Temp == temp) & (data$Medium == medium) & (data$Rep == repli),]$PopBio
  #mi<- min(d)
  #ma <- max(d)
  #data[(data$Species == species) & (data$Temp == temp) &(data$Medium == medium) & (data$Rep == repli),]$PopBio <- 0.01+0.99*((d-mi)/(ma-mi))

for (myID in 1:305){
  t<-data[data$ID == myID,]$Time
  mi<- min(t)
  ma <- max(t)
  newT <- 1*((t-mi)/(ma-mi))
  data[data$ID == myID,]$Time <- 1*((t-mi)/(ma-mi))
  
  if (sum(data[data$ID == myID,]$PopBio < 0) >0){
    data <- data[data$ID != myID,]
  }
  
}

write.csv(data, "../data/LogisticGrowthDataScaled.csv")
data2 <- read.csv("../data/LogisticGrowthDataScaled.csv")

