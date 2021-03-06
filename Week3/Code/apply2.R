
## Script: apply2.R
## Author: Sam Turner sat19@ic.ac.uk
## About: Demonstrating apply() function on random matrix

# clear environment
rm(list=ls())

SomeOperation <- function(v) {
    if (sum(v) > 0 ) {
        return (v * 100)
    }
    return (v)
}

M <- matrix(rnorm(100), 10, 10)
print (apply(M, 1, SomeOperation))