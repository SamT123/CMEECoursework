#preallocation speed benefits

reallocate <- function() {
    a <- NA

    for (i in 1:10000) {
        a <- c(a, i)
        #print(a)
        #print(object.size(a))
    }
}

preallocate <- function() {
    a <- rep(NA, 10000)

    for (i in 1:10000) {
        a[i] <- i
        #print(a)
        #print(object.size(a))
    }
}

print(system.time(reallocate()))
print(system.time(preallocate()))

