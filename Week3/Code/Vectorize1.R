# Comparison of element-wise matrix sum to built in vectorized sum function

M <- matrix(runif(1000000),1000,1000)

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
 

cat(" R\n---\n")

cat("Unvectorized:\t", system.time(SumAllElements(M))[[3]],"\n")

cat("Vectorized:\t", system.time(sum(M))[[3]],"\n\n")
