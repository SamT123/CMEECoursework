# Calculate Ne and SFS for North and South killer whale population
# load in data as a matrix (MUCH faster computation than dataframe, important for big genome data)

# YOU NEED TO CHANGE FILE PATH !
# Note: "cat()" esentially means "print" - so whenever this appears, we are printing a progress update to the terminal
cat("Loading data...","\n")
north <- as.matrix(read.csv("../Data/killer_whale_North.csv", header = FALSE, colClasses = "numeric"))
south <- as.matrix(read.csv("../Data/killer_whale_South.csv", header = FALSE, colClasses = "numeric"))

# check data - each row is a genome

####################
### ------------ ###
### Ne ESTIMATES ###
### ------------ ###
####################

# function to calculate tajima's theta estimate from a set on genomes, provided as a parameter called "genomes"
# theta = average num. pairwise differences = sum of pairwise differences / number of pairs 
tajimas <- function(genomes){
  
  # start pairwise_differences counter at 0
  pairwise_differences <- 0
  
  # n = number of genomes = number of rows of genomes matrix
  n <- dim(genomes)[1]
  
  cat("\t","Calculating pairwise differences for Tajima's estimator...","\n")
  
  # i : loop over the n genomes
  for (i in 1:n){
    # j : loop over every genome in the rows below i
    for (j in i:(n))
      # increase pairwise_differences by the number of differences between the i'th genome and j'th genome
      pairwise_differences <- pairwise_differences + sum(genomes[i,] != genomes[j,])
  }
  
  # return the number of pairwise_differences divided by the number of pairs, n(n-1)/2
  return (pairwise_differences / (n*(n-1)/2) )  
}

# function to calculate Watterson's theta estimate from a set on genomes, provided as a parameter called "genomes"
# theta = number of segregating sites / harmonic_series up to n-1
wattersons <- function(genomes){
  # total number of sites = number of columns of genomes matrix
  sites <- dim(genomes)[2]
  
  # n = number of genomes = number of rows of genomes matrix
  n <- dim(genomes)[1]
  
  # start pairwise_differences counter at 0
  segregating = 0
  
  cat("\t","Calculating segregating sites for Watterson's estimator...","\n\n")
  
  # loop over each of the sites ( = each column )
  for (i in 1:sites) {
    # if the length of the vector containing all unique values from the column is not 1, then the site is segregating 
    if(length(unique(genomes[,i])) != 1){
      # so we increase the segregating sites count by 1
      segregating <- segregating + 1
    }
  }
  
  # we also need to work out that denominator - this sum is called the "harmonic series"
  # start our sum at zero
  harmonic <- 0
  # add 1/k to the counter for each value of k up to n-1
  for ( k in 1:(n-1) ){
    harmonic <- harmonic + 1/k
  }
  
  # return the estimate!
  return (segregating / harmonic)
}



# check our functions work by checking the example from the lecture
cat("Running example data","\n")
example_df <- cbind(c(0,0,0,1,1), c(0,1,1,0,0), c(0,1,1,1,1))
example_tajima <- tajimas(example_df)
example_watterson <- wattersons(example_df)
cat("\n\t","Tajima's estimate:\t", example_tajima,"\n\n") # should equal 1.6
cat("\t","Watterson's estimate:\t",example_watterson,"\n\n") # should equal 1.44


# calculate the Tajima and Watterson estimate of theta for each population

cat("Calculating theta estimates for North population:","\n")
north_taj <- tajimas(north)
north_wat <- wattersons(north)

cat("Calculating theta estimates for South population:","\n")
south_taj <- tajimas(south)
south_wat <- wattersons(south)


# a function to convert from a theta estimate, mutation rate, and number of sites to an Ne estimate
theta_to_Ne <- function(theta, mu, sites){
  return (theta / (4*mu*sites))
}

# provided data
mu <- 1e-8
sites <- 50000

# calculate Ne estimates
north_taj_Ne <- theta_to_Ne(north_taj, mu, sites)
north_wat_Ne <- theta_to_Ne(north_wat, mu, sites)
south_taj_Ne <- theta_to_Ne(south_taj, mu, sites)
south_wat_Ne <- theta_to_Ne(south_wat, mu, sites)

# print Ne estimates

cat("North population  Ne by Tajima's estimator:\t", north_taj_Ne,"\n")
cat("North population  Ne by Watterson's estimator:\t", north_wat_Ne,"\n")
cat("South population  Ne by Tajima's estimator:\t", south_taj_Ne,"\n")
cat("South population  Ne by Watterson's estimator: ", south_wat_Ne,"\n\n")


#######################
### --------------- ###
### SFS CALCULATION ###
### --------------- ###
#######################

# function to calculate the Site Frequeny Spectrum of a set of genomes
# we need to count how often each possible allele frequency occurs
# first we will calculate the frequency of the derived allele at each of the 50000 sites
calc_SFS <- function(genomes){
  
  # number of sites = number of columns
  sites <- dim(genomes)[2]
  
  # number of genomes = number of rows
  n <- dim(genomes)[1]
  
  # start the frequencies vector as a vector with only NA values, and length equal to te number of frequencies we will have
  # this is done for computational efficiency
  frequencies <- rep(NA, sites)
  
  # for each site...
  cat("\t","Counting allele frequencies","\n")
  for (i in 1:sites){
    # make the corresponding position in the frequencies vector equal to the derived frequency at the site
    frequencies[i] <- (sum(genomes[,i]))
  }
  
  # now lets turn this into an SFS, = frequency of frequencies 
  
  # start with empty sfs vector
  sfs <- c()
  
  # table(vector) gives the frequency of values in the vector
  tbl <- table(frequencies)
  
  cat("\t","Counting allele frequency frequencies","\n\n")
  
  # for each frequency in the range of possible frequencies (0 = all ancestral, n = all derived)
  for (f in 0:n){
    # make the f +1 'th position in sfs equal to the number of occurances of that frequency
    sfs[f+1] <- sum(tbl[names(tbl)==f]) / n
    
  }
  # return the SFS excluding the count for sites where all alleles are ancestral (the first entry)
  return(sfs[-1])
}

# calculate the sfs for each dataset
cat("Calculating SFS for North population:","\n")
N_sfs <- calc_SFS(north)

cat("Calculating SFS for North population:","\n")
S_sfs <- calc_SFS(south)


# make barplot of the SFSs side by side - stolen from the example_03.R script
barplot(t(cbind(N_sfs, S_sfs)), beside=T, names.arg=seq(1,nrow(south),1), legend=c("North", "South"))
