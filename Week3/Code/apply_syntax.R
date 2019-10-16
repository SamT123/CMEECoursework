sq <- function(x){
    return(x*x)
}

ad <- function(x,y){
    return(x+y)
}

d = c(1:20)
e = c(21:40)

sqs <- mapply(function(i,j) ad(i,j),d,e)