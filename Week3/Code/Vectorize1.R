

## Script:  Vectorize1.R
## Author:  Sam Turner sat19@ic.ac.uk
## About:   Comparison of element-wise matrix sum to built in vectorized sum function

# generate 1000 * 1000 matrix of random numbers
M <- matrix(runif(1000000),1000,1000)

# sum all elements of matrix by looping
SumAllElements <- function(M){
  Dimensions <- dim(M)
  Tot <- 0
  for (i in 1:Dimensions[1]){
    for (j in 1:Dimensions[2]){
      Tot <- Tot + M[i,j]
    }
  }
  return (Tot)
}
 
# Time built-in and loopy methods of matrix summing
cat(" R \n---\n")

cat("Unvectorized:\t", system.time(SumAllElements(M))[[3]],"\n")

cat("Vectorized:\t", system.time(sum(M))[[3]],"\n\n")
