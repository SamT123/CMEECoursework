
## Script: break.R
## Author: Sam Turner sat19@ic.ac.uk
## About: Demonstrate breaking out of loop in R

# clear environment
rm(list=ls())

i <- 0 #Initialize i
    while(i < Inf) {
        if (i == 20) {
            break 
             } # Break out of the while loop! 
        else { 
            cat("i equals " , i , " \n")
            i <- i + 1 # Update i
    }
}