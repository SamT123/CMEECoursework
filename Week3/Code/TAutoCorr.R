# Calculate approximate p value for autocorrelation in Key West temperature data

library(ggplot2)

# load data
load("../Data/KeyWestAnnualMeanTemperature.Rdata", .GlobalEnv)

tempdata <- ats$Temp
 
# get lag-1 autocorrelation for a vector
get_auto <- function(data){
    n <- length(data)

    data_minus_first <- data[-1]

    data_minus_last <- data[-n]

    return (cor(data_minus_last, data_minus_first))

}

# correlation coefficient for real temp data
c <- get_auto(tempdata)

# plot temperature time series
plot.new()
plot(ats$Year, ats$Temp, type="n") 
lines(ats, p=)

# plot scatter of tn vs tn+1
plot.new()
plot(tempdata[-1],tempdata[-length(tempdata)])


# preallocate for scrambled correlation coefficeints
scrambled_autos <- rep(NA, 100000)

# fill vector of correlation coefficients for scrambled order temperatures
for (i in 1:100000){
    scrambled <- sample(tempdata,replace = FALSE)
    scrambled_autos[i] <- get_auto(scrambled)
}


# count how often the correlation coefficient of the scrambled data exceeds that of the real value
count <- 0

for (i in 1:10000){
    if (c < scrambled_autos[i]) {
        count <- count + 1
    }
}

# print result
options(scipen=999)
print(sprintf('Approx. p value = %s',count/100000))




# histogram of scrambled data correlation coefficients
df_scram <- data.frame(scrambled_autos)

p<-ggplot(df_scram, aes(x = scrambled_autos)) + geom_histogram(color="black", fill="white", binwidth = 0.01) + xlab( "Scrambled vector autocorrelations")

p <- p + geom_vline(aes(xintercept=c), color="red", linetype="dashed", size=1 ) 

p <- p + geom_text(x=c-0.015, y=1130, angle = 90, label="Real correlation coefficient")

p

# pdf("../Results/AutoC.pdf")
# print(p)
# dev.off()

ggsave("../Results/AutoC.pdf", width = 10, height = 7)

# scatter of x[t] vs x[n+1]

df_temp <- data.frame('x_t1' = tempdata[-1], 'x_t' = tempdata[-length(tempdata)])
q <- ggplot(df_temp, aes(x_t, x_t1)) + geom_point() + xlab( expression( paste( x[t], '/ °C'))) + ylab(expression( paste( x[t+1], '/ °C'))) + xlim(23,27) + ylim(23,27)

q

pdf("../Results/AutoCscatter.pdf")
print(q)
dev.off()

# temperature time series

df_all_temp <- data.frame('temps' = tempdata, idx = 1:length(tempdata))
r <- ggplot(ats, aes(x = Year, y = Temp)) + geom_line() + ylab("Temperature / °C")
r
# pdf("../Results/TempTimeSeries.pdf")
# print(r)
# dev.off()

ggsave("../Results/TempTimeSeries.pdf", width = 10, height = 5)

if (file.exists("Rplots.pdf")){
    file.remove("Rplots.pdf")
}