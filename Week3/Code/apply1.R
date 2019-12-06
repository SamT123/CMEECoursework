
## Script: apply1.R
## Author: Sam Turner sat19@ic.ac.uk
## About: Demonstrating apply() function on random matrix


# clear environment
rm(list=ls())

## Build a random matrix
M <- matrix(rnorm(100), 10, 10)

## Take the mean of each row
RowMeans <- apply(M, 1, mean)
print (RowMeans)

## Now the variance
RowVars <- apply(M, 1, var)
print (RowVars)

## By column
ColMeans <- apply(M, 2, mean)
print (ColMeans)