
# I first do Q1 by the FST method.
# Then Q2, genetic distance vs physical distance - he doesn't show how to do this in the example code...
# Then I've copy & pasted the example code for PCA and tree annotation methods as these are simpler.

# BTW if you dont get PCA, I found this video super helpful: https://www.youtube.com/watch?v=FgakZw6K1QQ
# Or if youre lazy: https://www.youtube.com/watch?v=HMOI_lkzW08

#######################
### FST calculation ###
### --------------- ###
#######################

# we will calculate FST for each pair of populations (A vs B, A vs C etc etc)

# load in data as a matrix (MUCH faster computation than dataframe, important for big genome data)

# YOU NEED TO CHANGE FILE PATH !
alleles <- as.matrix(read.csv("../Data/turtle.csv", header = FALSE, colClasses = "numeric"))



# function to calculate average FST across whole genome of two populations, a1 and a2
# we will keep track of the sum of FSTs from all sites with
#   a) derived allele frequency > 3% (we will get a list of these sites later)
#   b) non-infinite FST = biallelic in at least one population
get_ave_FST <- function(alleles1, alleles2, high_freq){
  # start total FST counter at 0
  total <- 0
  
  # start counter of eligable, segregating sites at 0
  seg <- 0
  
  # number of sites to loop over = number of columns
  sites = dim(alleles1)[2]
  
  # get allele frequencies
  f1 <- colSums(alleles1)/20
  f2 <- colSums(alleles2)/20
  
  
  # for each site in the genome...
  for (i in 1:sites){
    
    # only consider the site if:
    # high_freq == TRUE     AND    ( biallelic in a1     OR     biallelic in a2 )
    if(high_freq[i] == TRUE & ( length(unique(alleles1[,i])) != 1 | length(unique(alleles2[,i])) != 1)) {
      # if this condition is met:
      # calculate Hs using formula from lecture
      Hs <- f1[i] * (1-f1[i]) + f2[i] * (1-f2[i])
      
      # calculate Ht using formula from lecture
      Ht <- f1[i] * (1-f1[i]) + f2[i] * (1-f2[i]) + (abs(f1[i]-f2[i])**2) / 2

      # calculate FST using formula from lecture
      fst <- ( (Ht - Hs) / Ht )

      # add the FST for this site to the total
      total <- total + fst
      # and increase the count of eligable sites by 1
      seg <- seg + 1 
    }
  }
  
  # return the mean FST = total FST / number of eligable sites included
  return (total / seg)
}



# split up the 80 genome x 2000 sites matrix into matrices containing only the genomes for a specific location
A_alleles = alleles[1:20,]
B_alleles = alleles[21:40,]
C_alleles = alleles[41:60,]
D_alleles = alleles[61:80,]

# we need to determine which sites have a derived allele frequency > 3%, to put into our FST average function
# start with a vector with FALSE for all 2000 sites
high_freq = rep(FALSE,2000)

# look at each of the 2000 sites in the full 80 genome data set
for (i in 1:2000){
  
  # if the (sum of the column / 80) > 0.03, then we can accept the site
  if (sum(alleles[,i]) / 80 > 0.03){
    # so we should set the corresponding position in the vector to TRUE 
    high_freq[i] <- 1
  }
}

# finally, print out the results, calling the function with the 2 datasets of interest and the vector of frequency acceptance
cat("Mean FSTs:","\n",
    "\nA vs B:", get_ave_FST(A_alleles, B_alleles, high_freq),
    "\nA vs C:", get_ave_FST(A_alleles, C_alleles, high_freq),
    "\nA vs D:", get_ave_FST(A_alleles, D_alleles, high_freq),
    "\nB vs C:", get_ave_FST(B_alleles, C_alleles, high_freq),
    "\nB vs D:", get_ave_FST(B_alleles, D_alleles, high_freq),
    "\nC vs D:", get_ave_FST(C_alleles, D_alleles, high_freq),"\n")


### Q2 ###

#######################
### IBD calculation ###
### --------------- ###
#######################


# load genotype data as 80 sample x 2000 site matrix
genotypes <- as.matrix(read.csv("../Data/turtle.genotypes.csv", header = FALSE,stringsAsFactors=F, colClasses = "numeric"))

# calculate pairwise euclidean distance between sample genotypes, in 80 sample x 80 sample distance matrix
# this is essentially the distance between the genomes in the 2000 diomension space where each dimension represents the genotype at one site
genetic_distance <- as.matrix(dist(genotypes))

# put one-dimensional physical distances from origin in matrix
locations <- matrix(rep(rep(c(5,10,12,50), each=10),40),ncol=40)
# subtract the transpose to get pairwise distances between populations
physical_distances = abs(locations - t(locations))

# unwrap these distance matrices into vectors and plot scatter
plot(x=c(physical_distances), y=c(genetic_distance), xlab = "Physical distance / km", ylab = "Genetic distance")




### Q1 other methods ###
### COPIED FROM example_04.R  ###

### annotate location/group on tree inferred from distance matrix

distance <- dist(genotypes)

tree <- hclust(distance)

locations_vec <- rep(c("A","B","C","D"), each=10)
plot(tree, labels=locations_vec)

### or we can do a PCA
### we can filter our low-frequency variants first
colors <- rep(c("blue","red","yellow","green"), each=5)

index <- which(apply(FUN=sum, X=genotypes, MAR=2)/(nrow(genotypes)*2)>0.03)

pca <- prcomp(genotypes[,index], center=T, scale=T)

summary(pca)

plot(pca$x[,1], pca$x[,2], col=colors, pch=1)
legend("right", legend=sort(unique(locations_vec)), col=unique(colors), pch=1)
