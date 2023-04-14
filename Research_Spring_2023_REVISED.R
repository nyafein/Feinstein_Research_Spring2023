# Nya Feinstein
# Research Project Spring 2023

library(lubridate)
library(tidyverse)
library(dplyr)
library(ggplot2)

# Load in the data

df1 <- read.csv("C:/Users/nsf00/PycharmProjects/Research_Spring_2023/mid6/saved/similarity_results_4.csv")

head(df1)

# Step 1: Create a list of dates between 2011-08-10 and 2023-02-25

# defining start date
start_date <- ymd("2011-08-10")

# defining end date
end_date <- ymd("2023-02-25")

# generating range of dates
date <- seq(start_date, end_date,"days")
print(date)

# Step 2: Create a list of weeks (1 repeated 7 times, 2 repeated 7 times, etc)

# Find length of our dates
len_dates <- length(date)

# Find how many weeks that is (rounded up)
week_count <- round(len_dates/7)

# Create list of week numbers
weeks <-rep(1:week_count,each=7)

# Make sure range and weeks are the same length
len_dates
# 4218
length(weeks)
# 4221
# Delete the last three values of weeks
weeks <- head(weeks,-3)
length(weeks)

# Step 3: Create a data frame with dates and weeks

df2 <- data.frame(date, weeks)

# Step 4: In df1, make sure each date only has one entry
df1 <- df1 %>% group_by(date) %>% summarise(n = n(), scores_war = mean(scores_war), scores_invasion = mean(scores_invasion), scores_aid = mean(scores_aid), 
                                            scores_peace = mean(scores_peace), scores_negotiation = mean(scores_negotiation), scores_conflict = mean(scores_conflict), 
                                            scores_military = mean(scores_military), scores_attack = mean(scores_attack), 
                                            scores_missile = mean(scores_missile), scores_sanction = mean(scores_sanction), scores_cyber = mean(scores_cyber))


# Step 5: Make sure dates in both data frames are in the same format

df1$date <- as.Date(df1$date)
df2$date <- as.Date(df2$date)

# Step 6: Merge df1 and df2 with an outer join on dates

df_main <- merge(x=df1,y=df2, 
                 by.x = "date", by.y = "date", all.x = FALSE, all.y = TRUE)

# Step 7: Make all NA values = 0

df_main <- replace(df_main, is.na(df_main), 0)

# Step 8: Group by week into new data frame

df_grouped <- df_main %>% group_by(weeks) %>% summarise(n = sum(n), scores_war = mean(scores_war), scores_invasion = mean(scores_invasion), 
                                                        scores_aid = mean(scores_aid), scores_peace = mean(scores_peace), scores_negotiation = mean(scores_negotiation),
                                                        scores_conflict = mean(scores_conflict), 
                                                        scores_military = mean(scores_military), scores_attack = mean(scores_attack), 
                                                        scores_missile = mean(scores_missile), scores_sanction = mean(scores_sanction), scores_cyber = mean(scores_cyber))

# Step 9: Visualizations!
# Look at df_main to find what week February 24, 2022 (current war) - Week 551
# and February 20, 2014 (Russia annexed Crimea) - Week 133

# Create breaks and labels for the x axis

lbls = c("2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023")

brks = c(21, 73, 126, 178, 230, 282, 334, 386, 439, 491, 543, 595)

lmts = c(0:603)


plot_war <- ggplot(data = df_grouped, aes(x = weeks, y = scores_war)) 
plot_war + geom_point() + labs(x = "", y = "Similarity Score", title = "Similarity Score of 'War'") + geom_vline(xintercept = 133, color = "red") + geom_vline(xintercept = 551, color = "red") + scale_x_continuous(breaks = brks, labels=lbls) + theme(axis.text.x = element_text(angle = 45, vjust = 0.65)) + stat_smooth(se = FALSE, span = 0.2)


plot_invasion <- ggplot(data = df_grouped, aes(x = weeks, y = scores_invasion))
plot_invasion + geom_point() + labs(x = "", y = "Similarity Score", title = "Similarity Score of 'Invasion'") + geom_vline(xintercept = 133, color = "red") + geom_vline(xintercept = 551, color = "red") +  scale_x_continuous(breaks = brks, labels=lbls) + theme(axis.text.x = element_text(angle = 45, vjust = 0.65)) + stat_smooth(se = FALSE, span = 0.2)



plot_aid <- ggplot(data = df_grouped, aes(x = weeks, y = scores_aid))
plot_aid + geom_point() + labs(x = "", y = "Similarity Score", title = "Similarity Score of 'Aid'") + geom_vline(xintercept = 133, color = "red") + geom_vline(xintercept = 551, color = "red") +  scale_x_continuous(breaks = brks, labels=lbls) + theme(axis.text.x = element_text(angle = 45, vjust = 0.65)) + stat_smooth(se = FALSE, span = 0.2)


plot_peace <- ggplot(data = df_grouped, aes(x = weeks, y = scores_peace))
plot_peace + geom_point() + labs(x = "", y = "Similarity Score", title = "Similarity Score of 'Peace'") + geom_vline(xintercept = 133, color = "red") + geom_vline(xintercept = 551, color = "red") +  scale_x_continuous(breaks = brks, labels=lbls) + theme(axis.text.x = element_text(angle = 45, vjust = 0.65)) + stat_smooth(se = FALSE, span = 0.2)


plot_negotiation <- ggplot(data = df_grouped, aes(x = weeks, y = scores_negotiation))
plot_negotiation + geom_point() + labs(x = "", y = "Similarity Score", title = "Similarity Score of 'Negotiation'") + geom_vline(xintercept = 133, color = "red") + geom_vline(xintercept = 551, color = "red") +  scale_x_continuous(breaks = brks, labels=lbls) + theme(axis.text.x = element_text(angle = 45, vjust = 0.65)) + stat_smooth(se = FALSE, span = 0.2)


plot_conflict <- ggplot(data = df_grouped, aes(x = weeks, y = scores_conflict))
plot_conflict + geom_point() + labs(x = "", y = "Similarity Score", title = "Similarity Score of 'Conflict'") + geom_vline(xintercept = 133, color = "red") + geom_vline(xintercept = 551, color = "red") +  scale_x_continuous(breaks = brks, labels=lbls) + theme(axis.text.x = element_text(angle = 45, vjust = 0.65)) + stat_smooth(se = FALSE, span = 0.2)


plot_military <- ggplot(data = df_grouped, aes(x = weeks, y = scores_military))
plot_military + geom_point() + labs(x = "", y = "Similarity Score", title = "Similarity Score of 'Military'") + geom_vline(xintercept = 133, color = "red") + geom_vline(xintercept = 551, color = "red") +  scale_x_continuous(breaks = brks, labels=lbls) + theme(axis.text.x = element_text(angle = 45, vjust = 0.65)) + stat_smooth(se = FALSE, span = 0.2)


plot_attack <- ggplot(data = df_grouped, aes(x = weeks, y = scores_attack))
plot_attack + geom_point() + labs(x = "", y = "Similarity Score", title = "Similarity Score of 'Attack'") + geom_vline(xintercept = 133, color = "red") + geom_vline(xintercept = 551, color = "red") +  scale_x_continuous(breaks = brks, labels=lbls) + theme(axis.text.x = element_text(angle = 45, vjust = 0.65)) + stat_smooth(se = FALSE, span = 0.2)


plot_missile <- ggplot(data = df_grouped, aes(x = weeks, y = scores_missile))
plot_missile + geom_point() + labs(x = "", y = "Similarity Score", title = "Similarity Score of 'Missile'") + geom_vline(xintercept = 133, color = "red") + geom_vline(xintercept = 551, color = "red") +  scale_x_continuous(breaks = brks, labels=lbls) + theme(axis.text.x = element_text(angle = 45, vjust = 0.65)) + stat_smooth(se = FALSE, span = 0.2)


plot_sanction <- ggplot(data = df_grouped, aes(x = weeks, y = scores_sanction))
plot_sanction + geom_point() + labs(x = "", y = "Similarity Score", title = "Similarity Score of 'Sanction'") + geom_vline(xintercept = 133, color = "red") + geom_vline(xintercept = 551, color = "red") +  scale_x_continuous(breaks = brks, labels=lbls) + theme(axis.text.x = element_text(angle = 45, vjust = 0.65)) + stat_smooth(se = FALSE, span = 0.2)


plot_cyber <- ggplot(data = df_grouped, aes(x = weeks, y = scores_cyber))
plot_cyber + geom_point() + labs(x = "", y = "Similarity Score", title = "Similarity Score of 'Cyber'") + geom_vline(xintercept = 133, color = "red") + geom_vline(xintercept = 551, color = "red") +  scale_x_continuous(breaks = brks, labels=lbls) + theme(axis.text.x = element_text(angle = 45, vjust = 0.65)) + stat_smooth(se = FALSE, span = 0.2)


# Now, create a plot for total articles

plot_total <- ggplot(data = df_grouped, aes(x = weeks, y = n))
plot_total + geom_point() + stat_smooth(se = FALSE, span = 0.2) + labs(x = "", y = "Article Count", title = "Article Count Over Time") + geom_vline(xintercept = 133, color = "red") + geom_vline(xintercept = 551, color = "red") +  scale_x_continuous(breaks = brks, labels=lbls) + theme(axis.text.x = element_text(angle = 45, vjust = 0.65))

