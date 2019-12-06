## Script: DataWrang.R
## Author: Sam Turner sat19@ic.ac.uk
## About: Data wrangling using tidyR


################################################################
################## Wrangling the Pound Hill Dataset ############
################################################################

require(dplyr)
require(tidyr)
require(reshape2)

rm(list=ls())
############# Load the dataset ###############
# header = false because the raw data don't have real headers
MyData <- as.matrix(read.csv("../data/PoundHillData.csv",header = F)) 

# header = true because we do have metadata headers
MyMetaData <- read.csv("../data/PoundHillMetaData.csv",header = T, sep=";", stringsAsFactors = F)

############# Inspect the dataset ###############
dim(MyData)
dplyr::glimpse(MyData)

############# Transpose ###############
# To get those species into columns and treatments into rows 
MyData <- t(MyData)
dim(MyData)

############# Replace species absences with zeros ###############
MyData[MyData == ""] = 0

############# Convert raw matrix to data frame ###############

TempData <- as.data.frame(MyData[-1,],stringsAsFactors = F) #stringsAsFactors = F is important!


colnames(TempData) <- MyData[1,] # assign column names from original data

############# Convert from wide to long format  ###############

?melt #check out the melt function

MyWrangledData <- tidyr::gather(TempData, key = Species, value = Count, -Cultivation,-Block,-Plot,-Quadrat)

MyWrangledData <- MyWrangledData %>%
  mutate(Cultivation = factor(Cultivation),
         Block = factor(Block),
         Plot = factor(Plot),
         Quadrat = factor(Quadrat),
         Count = as.integer(Count))

dplyr::glimpse(MyWrangledData)
dim(MyWrangledData)