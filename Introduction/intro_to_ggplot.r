library(ggplot2)


ggplot(
  data = temperatures,
  mapping = aes(x = day_of_year, y = temperature, color = location)
) + geom_line()




