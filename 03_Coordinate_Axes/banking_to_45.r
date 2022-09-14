library(tidyverse)

stock_price <- read_csv("google.csv")
bank_slopes(as.numeric(stock_price$date), stock_price$close, method = "as")




