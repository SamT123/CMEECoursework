## Script: preallocate.R
## Author: Sam Turner sat19@ic.ac.uk
## About: Demonstrate speed benefits of vector preallocation

# reallocation for large vector is slow
reallocate <- function() {
    a <- NA

    for (i in 1:10000) {
        a <- c(a, i)
        #print(a)
        #print(object.size(a))
    }
}

# preallocation for large vector is faster
preallocate <- function() {
    a <- rep(NA, 10000)

    for (i in 1:10000) {
        a[i] <- i
        #print(a)
        #print(object.size(a))
    }
}

# compare times
print(system.time(reallocate()))
print(system.time(preallocate()))

