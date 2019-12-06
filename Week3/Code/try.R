## Script:  try.R
## Author:  Sam Turner sat19@ic.ac.uk
## About:   demonstrate the try function

doit <- function(popn){
	x <- sample(popn, replace = TRUE)
	if(length(unique(x)) > 30) {#only take mean if sample was sufficient
		 print(paste("Mean of this sample was:", as.character(mean(x))))
		} 
	else {
		stop("Couldn't calculate mean: too few unique values!")
		}
	}

popn <- rnorm(50)

result <- lapply(1:15, function(i) try(doit(popn), FALSE))