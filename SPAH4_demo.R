
#This is a R script to calculate 'SPAtial Hybrid 4' efficiency (SPAH4) which can be used to compare spatial patterns in two raster maps 
#Note that the "no values (here -9999)" in 2D maps are cleared first. Observed and Simulated two arrays (2D) are provided to the function.

#Detailed explanation goes here

#The newly proposed SPAtial Hybrid 4 efficiency (SPAH4) metric  is proven to be robust 
#and easy to interpret due to its three distinct and complementary components of correlation, variance, histogram matching and kurtosis ratio.

#Created on Thu July 18 12:00:00 2024
#@ authors:                 Eymen Berkay Yorulmaz, Elif Kartal, Mehmet Cüneyd Demirel
#@ author's organization:   Department of Civil Engineering, Istanbul Technical University, Demirel's Hydrology and Remote Sensing LAB
#@ author's webpage:        https://www.linkedin.com/in/eymen-berkay-yorulmaz-7203051b6/
#@ author's email id:       yorulmaz21@itu.edu.tr
#
#A libray with R functions for calculation of 'SPAtial Hybrid 4' efficiency (SPAH4) metric.


#clean Global Environment
rm(list=ls()) 

# WD: working directory
setwd(dirname(rstudioapi::getActiveDocumentContext()$path)) #For Rstudio users

###############automated setwd for all R users
script.dir <- getSrcDirectory(function(x) {x})
print(script.dir)
setwd(script.dir)
##############

#install.packages("pracma") #histc is in pracma, uncomment and install first
#install.packages("moments") #kurtosis is in pracma, uncomment and install first
library(pracma)
library(moments)

# read ascii
mask <- read.delim('./map_files/mask_1km.asc', header = FALSE, sep = ",", dec = ".")
dimens=dim(mask)
mask=array(as.numeric(unlist(mask)), dim=c(dimens[1], dimens[2]))

map1 <- read.delim('./map_files/obs.asc', header = FALSE, sep = "\t", dec = ".")  #observed data comes here
map1=array(as.numeric(unlist(map1)), dim=c(dimens[1], dimens[2]))
map1=map1[as.logical(mask)]

map2 <- read.delim('./map_files/sim_1.asc', header = FALSE, sep = "\t", dec = ".") #You can test other asc files here
map2=array(as.numeric(unlist(map2)), dim=c(dimens[1], dimens[2]))
map2=map2[as.logical(mask)]

obs <- map1[ map1 != -9999 ]
sim <- map2[ map2 != -9999 ]


#CORR
alpha=cor(obs,sim)

#coefficient of variation
cv_obs=sd(obs)/mean(obs);
cv_sim=sd(sim)/mean(sim);

beta=cv_sim/cv_obs;

#HISTOmatch
obs=(obs-mean(obs))/sd(obs)
sim=(sim-mean(sim))/sd(sim)

bins=floor(sqrt(length(obs)))

h1 <- hist(obs, breaks=bins, freq=TRUE, plot=TRUE)
h2 <- hist(sim, breaks=bins, freq=TRUE, plot=TRUE) #False makes Density instead of frequency, try it

a=histc(obs, h1$breaks)
b=histc(sim, h1$breaks)
c=cbind(a$cnt, b$cnt)
d <- pmin(c[,1],c[,2])
overlap=sum(d)
histogram_match=overlap/sum(a$cnt)
gamma=histogram_match

#coefficient of kurtosis ratio
kappa= kurtosis(sim)/kurtosis(obs)

spah4 = 1- sqrt( (alpha-1)^2 + (beta-1)^2 + (gamma-1)^2 + (kappa-1)^2 )

#print(paste0("SPAEF: ", round(spaef, digits = 6)))
cat("SPAH4: ", spah4)

