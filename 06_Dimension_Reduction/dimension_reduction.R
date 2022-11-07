library(tidyverse)
library(ggplot2)
library(broom)  # for augment(), tidy()

blue_jays <- read_csv("https://wilkelab.org/SDS375/datasets/blue_jays.csv")

# Plot without scaling
blue_jays %>%
  ggplot() +
  aes(skull_size_mm, head_length_mm) + 
  geom_point(aes(color = sex))

# Plot with scaling
blue_jays %>% 
  # scale all numeric columns
  mutate(across(where(is.numeric), scale)) %>%
  ggplot() +
  aes(skull_size_mm, head_length_mm) + 
  geom_point(aes(color = sex))


# We perform a PCA with prcomp()
blue_jays %>% 
  select(where(is.numeric)) %>% # retain only numeric columns
  scale() %>%                   # scale to zero mean and unit variance
  prcomp()                      # do PCA

# First we run the PCA and store results as pca_fit:
pca_fit <- blue_jays %>% 
  select(where(is.numeric)) %>% # retain only numeric columns
  scale() %>%                   # scale to zero mean and unit variance
  prcomp() 



# Then we add PC coordinates into original dataset and plot:
pca_fit %>%
  augment(blue_jays) %>% # adds the fitted coordinates into the original dataset
  ggplot(aes(.fittedPC1, .fittedPC2)) +
  geom_point(aes(color = sex))


# Plot PC 2 against PC 1
pca_fit %>%
  # add PCs to the original dataset
  augment(blue_jays) %>%
  ggplot(aes(.fittedPC1, .fittedPC2)) +
  geom_point(aes(color = sex))

#Plot PC 3 against PC 2
pca_fit %>%
  # add PCs to the original dataset
  augment(blue_jays) %>%
  ggplot(aes(.fittedPC2, .fittedPC3)) +
  geom_point(aes(color = sex))


# Plot the rotation matrix
arrow_style <- arrow(
  angle = 20, length = grid::unit(8, "pt"),
  ends = "first", type = "closed"
)
pca_fit %>%
  # extract rotation matrix
  tidy(matrix = "rotation") %>%
  pivot_wider(
    names_from = "PC", values_from = "value",
    names_prefix = "PC"
  ) %>%
  ggplot(aes(PC1, PC2)) +
  geom_segment(
    xend = 0, yend = 0,
    arrow = arrow_style
  ) +
  geom_text(aes(label = column), hjust = 1) +
  xlim(-1.5, 0.5) + ylim(-1, 1) + 
  coord_fixed()