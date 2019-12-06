# Demonstrate browser() function for debugging

## Script: browse.R
## Author: Sam Turner sat19@ic.ac.uk
## About: Demonstrate browser() function for debugging

# clear environment
rm(list=ls())

# Exponential population growth simulation, returning population size time series
Exponential <- function(N0 = 1, r = 1, generations = 10) {
    #preallocate vector
    N <- rep(NA, generations)
    N[1] <- N0
    # Calculate population size each generation
    for (t in 2:generations){
        N[t] <- N[t-1] * exp(r)
        browser()
    }
    return(N)
}

# plot exponential population growth
plot(Exponential(), type="l", main="Exponential growth", xlab = "Generation", ylab="N")
