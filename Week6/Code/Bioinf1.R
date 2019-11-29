library(stringr)

bears <- read.csv("../Data/bears.csv", header = FALSE, colClasses = "character")
colnames(bears)<-1:10000

SNPs = c()

for (i in 1:10000) {
  if(dim(unique(bears[i]))[1] != 1){
    SNPs <- c(SNPs, i)
  }
}
freq <-c()
for (SNP in SNPs){
  ref <- bears[SNP][1,]
  l <- bears[SNP]
  f<-length(l[l==ref])

  if (f<20){
    f<-40-f
  }
  freq <- c(freq, f/40)
}

barplot(freq,ylim=c(0,1))

g <- data.frame(homref = numeric(),het = numeric(), homnon = numeric())


homref = rep(0,length(SNPs))
het = rep(0,length(SNPs))
homnon = rep(0,length(SNPs))

cnt = 0


for (SNP in SNPs){
  cnt<-cnt+1
  ref <- bears[SNP][1,]
  
  for (i in 1:20){
    i<-2*i-1
    j=i+1
    pair = (bears[i:j, SNP] == ref)
    

    if (sum(pair) == 2){
      homref[cnt] <- homref[cnt]+1
    }
    
    
    if (sum(pair) == 1){
      het[cnt] <- het[cnt]+1
    }
    
    
    if (sum(pair) == 0){
      homnon[cnt] <- homnon[cnt]+1
    }

  }
}

g <- data.frame(homref,het, homnon)
colnames(g)<-c('homref', 'het', 'homnon')

g$ref = (g$homref/20+g$het/40)
g$exphomref = g$ref ^ 2
g$exphet = g$ref * (1-g$ref) * 2
g$exphomnon = (1-g$ref) ^ 2

g$chi <- rowSums(( (g[1:3] - g[5:7]*20)^2) /(g[5:7]*20))
g$sig <- (g$chi>3.84)  


g$inb <- (2 * g$ref * (1-g$ref) - g$het/20) / 2*g$het/20


barplot(g$inb)
