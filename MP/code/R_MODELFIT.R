############
# PACKAGES #
############

library(repr)
require("minpack.lm")
require("ggplot2")
require("lazyeval")
require("reshape2")
###################
# MODEL FUNCTIONS #
###################


Quadratic <- function(t, a, b,c){
  return(c*t**2 + b*t + a)
}


Cubic <- function(t, a, b, c, d){
  return(d*t**3 + c*t**2 + b*t + a)
}


Logistic <- function(t, N0, Nmax, r){
  
  return( ( N0 * Nmax * exp(r*t) ) /  ( Nmax + N0 * (exp(r*t) - 1) )  )
}

Gompertz <- function(t, A, rmax, tlag){
  #A <- log(Nmax / N0)
  exponent <- (( rmax * exp(1) * (tlag - t)  / A) + 1)
  
  return( (A * exp( -exp( exponent  ))))
}  

Baranyi <- function(t, N0, Nmax, rmax, h0){
  logn0=log(N0)
  lognmax=log(Nmax)
  At <- rmax * t + (1/rmax) * log( exp( - rmax * t ) + exp( -h0 ) - exp( - rmax * t - h0 ))
  lognt <- logn0 + At - log( 1 + (exp( At ) - 1)/exp(lognmax - logn0) )
  return( exp(lognt) )
  
  #At <- t + ( 1 / rmax ) * log( ( exp( -rmax * t ) + h0 ) / ( 1 + h0 ) )
  #return( N0 + rmax * At - log( 1 + (exp(  rmax * At ) - 1) / (exp( N0 - Nmax ))))
} 



##################
# OBSERVE MODELS #
##################

time_range <- seq(0,1,len=200)

test_plot <- function(fun,Time,...){
  Nt <- fun(Time, ...)
  df <- data.frame(Time, Nt)
  p <- ggplot(df, aes(x = Time, y = Nt)) + geom_line() + ggtitle(as.character(substitute(fun)))
  p
}

test_plot(Cubic,time_range, 1/3,-45,1400,0)

test_plot(Logistic,time_range, 700,20000,6)

test_plot(Gompertz,time_range, 500,8000,0.3)

test_plot(Baranyi,time_range, 0.001,0.15,20,0.05)

########
# GOMPERTZ
########

test_plot(Gompertz,time_range, 500,8000,0.3)

#################
# MODEL FITTING #
#################

# LOAD DATA
data <- read.csv("../data/LogisticGrowthDataScaled.csv")
data$Temp <- as.factor(data$Temp)
IDs = unique(data$ID)
combos <- unique(cbind(as.vector(data$Species), as.vector(data$Temp),as.vector(data$Medium),as.vector(data$Rep)))
ID_list <- list()
for (i in 1:dim(combos)[1]){
  species <- combos[i,1]
  temp <- combos[i,2]
  medium <- combos[i,3]
  repli <- combos[i,4]
}


# for a given species, temp, medium, fit and overlay all listed models

success_df <- data.frame("Quadratic"=rep(0,305),"Cubic"=rep(0,305),"Logictic"=rep(0,305),"Gompertz"=rep(0,305),"Baranyi"=rep(0,305))
success_df[i,model_name]<-1




multifit <- function(myID, model_fits, linear_names, inits, plot_fits){
  
  
  
  run_info <- data[data$ID == myID,]
  species <- as.character(run_info$Species[1])
  temp <- as.character(run_info$Temp[1])
  medium <- as.character(run_info$Medium[1])
  repli <- as.character(run_info$Rep[1])

  # filter to get desired time series
  d <- dplyr::filter(data, ID == myID)
  t_range <- seq(min(d$Time),max(d$Time),len=200)
  fit_df <- data.frame(t_range)
  ModelFits <- list()
  success <- list()
  for (model_name in names(model_fits)){
    print(model_name)
    model_fit <- model_fits[[model_name]]
    if (model_name %in% linear_names){
      print("lm fit  attempted")
      pwr <- model_fit
      result <- try(PowFit <- lm(PopBio ~ poly(Time,degree = pwr, raw=T), data=d), silent = F)
    }
    
    else{
      print("nlm fit  attempted")
      params <- paste0("x", 1:length(inits[[model_name]]))
      ls<-c(c(0,0),rep(-Inf,-2+length(inits[[model_name]])))
      fml <- as.formula(paste("PopBio ~ model_fit(Time, ", paste(params, collapse= ","), ")"))
      result <- try(PowFit <- nlsLM(fml, data = d, start = inits[[model_name]] ,  control = list(maxiter = 500),lower = ls), silent = T)
    }
    
    
    
    model_fun <- model_functions[[model_name]]
    
    if ( class(result) == "try-error" ){
      print("Error")
      cat(geterrmessage())
      success[[model_name]] <- 0
      ModelFits[[model_name]] <- NA
      cat("\n")
      estimates <- do.call(model_fun, c(list(t_range), unname(inits[[model_name]])))
      fit_df[[paste0(model_name)]] <- estimates

    }
    else{
      print("Success")
      print(summary(PowFit))
      success[[model_name]] <- 1
      ModelFits[[model_name]] <- PowFit
      cat("\n")
      estimates <- do.call(model_fun, c(list(t_range), unname(coef(PowFit))))
      fit_df[[paste0(model_name)]] <- estimates
      
    }

  }

  if (plot_fits){
    print("ue")
    p <- ggplot() + geom_point(data = d, aes(x = Time, PopBio) )
    
    y_m <- melt(fit_df, id.vars=c("t_range"))
    
    p <- p + geom_line(data = y_m, aes(x = t_range, y = value, group = variable, colour = variable))
    p <- p + ggtitle(paste(c(species, temp, medium), collapse =", " )) + labs(color="Model") + ylab(paste("Population Biomass / ", d$PopBio_units)) + xlab("Time / Hours")
    
    print(p)
  }
  
  
  return(success)
}

gen_inits <- function(n_param){
  return( setNames( as.list(rep(.1, n_param)) , paste0("x", 1:n_param) ))
}





inits_df <- read.csv("../data/inits.csv")


get_inits <- function(myID){
  
  d<-dplyr::filter(inits_df, ID == myID)
  initvals=list()
  for (m in non_linears){
    i_s <- dplyr::filter(d, Model == m)$Value
    
    sublist <- setNames(as.list(i_s) , paste0("x", 1:length(i_s)))
    initvals[[m]]<-setNames( as.list(i_s) , paste0("x", 1:length(i_s)) )
  }
  
  return(initvals)
}







inits <- list("Logistic" = gen_inits(3), "Gompertz" = gen_inits(3),"Baranyi" = gen_inits(4), "Quadratic"=gen_inits(3),"Cubic"=gen_inits(4) )



model_functions <- list("Logistic"=Logistic, "Gompertz"=Gompertz, "Baranyi"=Baranyi, "Quadratic"=Quadratic, "Cubic"=Cubic)
model_fits <- list("Quadratic"=2, "Cubic"=3, "Logistic"=Logistic,"Gompertz"=Gompertz,"Baranyi"=Baranyi)
linears <- c("Quadratic", "Cubic")
non_linears=c("Logistic","Gompertz","Baranyi")



r<-function(myID){
  inits <- get_inits(myID)
  multifit(myID, model_fits, linears, inits,TRUE)
}
ModelFits_df<- data.frame("id"=rep(0,305),"Quadratic"=rep(0,305),"Cubic"=rep(0,305),"Logistic"=rep(0,305),"Gompertz"=rep(0,305),"Baranyi"=rep(0,305))
for (n in IDs){
  print(n)
  inits <- get_inits(n)
  a<-multifit(n, model_fits, linears, inits,F)
  ModelFits_df[n,]<-c(list("id"=n),a)
}

long<-melt(ModelFits_df,id.vars = c("id"))

ggplot(long, aes(x = variable, y = id, fill = value)) +
  geom_tile()


