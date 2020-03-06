library(ape)

leopard <- read.csv("../Data/leopard_gecko.csv", header = FALSE, colClasses = "character")
bent <- read.csv("../Data/bent-toed_gecko.csv", header = FALSE, colClasses = "character")
western <- read.csv("../Data/western_banded_gecko.csv", header = FALSE, colClasses = "character")

colnames(leopard)<-1:20000
colnames(bent)<-1:20000
colnames(western)<-1:20000


# want fixed differences only
fixed_sites <- function(genomes){
  fixed = c()
  for (i in 1:dim(genomes)[2]) {
    if(dim(unique(genomes[i]))[1] == 1){
      fixed <- c(fixed, i)
    }
  }
  return (unlist(fixed))
}

cat("Finding fixed sites for leopard...","\n")
leopard_fixed <- fixed_sites(leopard)

cat("Finding fixed sites for bent-toe...","\n")
bent_fixed <- fixed_sites(bent)

cat("Finding fixed sites for western...","\n")
western_fixed <- fixed_sites(western)



get_div <- function(genome1,genome2, fixed1, fixed2){

  cat("\t","Finding shares fixed sites...","\n")
  both_fixed <- intersect(fixed1, fixed2)
  
  tot <- 0
  div <- 0
  
  g1 = genome1[1,]
  g2 = genome2[1,]
  
  cat("\t","Finding fixed diverged sites...","\n")
  
  for (i in both_fixed) {
    tot <- tot + 1
    if (g1[i] != g2[i]) {
      div <- div + 1
    }
  }
  return(c(div, tot, div/tot))
}



cat("Finding leopard / bent-toe divergence","\n")
div_leo_ben  <- get_div(leopard, bent, leopard_fixed, bent_fixed)

cat("Finding leopard / western divergence","\n")
div_leo_west <- get_div(leopard, western, leopard_fixed, western_fixed)

cat("Finding bent-toe / western divergence","\n")
div_ben_west  <- get_div(bent, western, bent_fixed, western_fixed)


# rate in MY / site !!! in div / MY = rate along a single lineage

rate <- div_leo_ben[3] / (30*2)

div_time_leo_ben <-  div_leo_ben[3] / (2*rate)
div_time_leo_west <- div_leo_west[3] / (2*rate)
div_time_ben_west <- div_ben_west[3] / (2*rate)

cat("\nDivergence time leopard - bent:\t", div_time_leo_ben, " MY\n")
cat("Divergence time leopard - west:\t", div_time_leo_west, " MY\n")
cat("Divergence time bent - west:\t", div_time_ben_west, " MY\n")


text.string<-
  "((Bent_toed_gecko, Western_banded_gecko), Leopard_gecko);"
vert.tree<-read.tree(text=text.string)

plot(vert.tree,no.margin=TRUE,edge.width=2)


# without PM
get_div_new <- function(genome1,genome2){
  div <- 0
  
  cat("\t","Finding fixed diverged sites...","\n")
  
  for (i in 1:dim(genome1)[2]) {
    if (length( intersect(genome1[,i], genome2[,i]) ) == 0 ) {
      div <- div + 1
    }
  }
  
  return(div)
}

