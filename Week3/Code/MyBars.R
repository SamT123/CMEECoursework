## Script: MyBars.R
## Author: Sam Turner sat19@ic.ac.uk
## About: Demonstrate building up a bar plot with ggplot2.

# clear environment
rm(list=ls())


# load dependencies
require(ggplot2)

# load data
a <- read.table("../Data/Results.txt", header = TRUE)

a$ymin <- rep(0, dim(a)[1])
p <- ggplot(a)

# Plot first set of bars
p <- p + geom_linerange(data = a, aes(
                          x = x,
                          ymin = ymin,
                          ymax = y1,
                          size = (0.5)
                          ),
                        colour = "#E69F00",
                        alpha = 1/2, show.legend = FALSE)

# Plot second set of bars
p <- p + geom_linerange(data = a, aes(
                          x = x,
                          ymin = ymin,
                          ymax = y2,
                          size = (0.5)
                          ),
                        colour = "#56B4E9",
                        alpha = 1/2, show.legend = FALSE)

# Plot third set of bars
p <- p + geom_linerange(data = a, aes(
                          x = x,
                          ymin = ymin,
                          ymax = y3,
                          size = (0.5)
                          ),
                        colour = "#D55E00",
                        alpha = 1/2, show.legend = FALSE)

# add annotation
p <- p + geom_text(data = a, aes(x = x, y = -500, label = Label))

# now set the axis labels, remove the legend, and prepare for bw printing
p <- p + scale_x_continuous("My x axis",
                            breaks = seq(3, 5, by = 0.05)) + 
                            scale_y_continuous("My y axis") + 
                            theme_bw() + 
                            theme(legend.position = "none") 

# save to pdf
pdf("../Results/MyBars.pdf")
print(p)
dev.off()
