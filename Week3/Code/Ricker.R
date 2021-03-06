
## Script: Ricker.R
## Author: Sam Turner sat19@ic.ac.uk
## About: plot Ricker model time series

Ricker <- function(N0=1, r=1, K=10, generations=50)
{
  # Runs a simulation of the Ricker model
  # Returns a vector of length generations

  N <- rep(NA, generations)    # Creates a vector of NA

  N[1] <- N0
  for (t in 2:generations)
  {
    N[t] <- N[t-1] * exp(r*(1.0-(N[t-1]/K)))
  }
  return (N)
}

#plot ricker population time series
plot(Ricker(generations=10), type="l", xlab="Population size", ylab="Generation")

if (file.exists("Rplots.pdf")){
    file.remove("Rplots.pdf")
}