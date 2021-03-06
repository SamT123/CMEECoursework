

## Script:  Vectorize1.R
## Author:  Sam Turner sat19@ic.ac.uk
## About:   Runs vectorized and unvectorized stochastic
#           (with gaussian fluctuations) Ricker Eqn. 

rm(list=ls())


# Samraat's original unvectorized function

stochrick<-function(p0=runif(1000,0.5,1.5),r=1.2,K=1,sigma=0.2,numyears=100)
{
  #initialize
  N<-matrix(NA,numyears,length(p0))
  N[1,]<-p0
  
  for (pop in 1:length(p0)) #loop through the populations
  {
    for (yr in 2:numyears) #for each pop, loop through the years
    {
      N[yr,pop]<-N[yr-1,pop]*exp(r*(1-N[yr-1,pop]/K)+rnorm(1,0,sigma))
    }
  }
 return(N)

}

# My new vectorized function, using vector arithmatic

stochrickvect<-function(p0=runif(1000,0.5,1.5),r=1.2,K=1,sigma=0.2,numyears=100)
{
  #initialize
  N<-matrix(NA,numyears,length(p0))
  N[1,]<-p0
  for (yr in 2:numyears) #for each pop, loop through the years
    {
      N[yr,] <- N[yr-1,]*exp(r*(1-N[yr-1,]/K)+rnorm(1,0,sigma))
    }
  return(N)
  }




# Print results to terminal
cat(" R \n---\n")

cat("Unvectorized:\t", system.time(res2<-stochrick())[[3]],"\n")

cat("Vectorized:\t", system.time(res2<-stochrickvect())[[3]],"\n\n")


