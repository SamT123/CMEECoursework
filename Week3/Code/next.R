
## Script: next.R
## Author: Sam Turner sat19@ic.ac.uk
## About: Demonstrate passing to next iterator term in R

# clear environment
rm(list=ls())

for (i in 1:10) {
  if ((i %% 2) == 0) 
    next # pass to next iteration of loop 
  print(i)
}