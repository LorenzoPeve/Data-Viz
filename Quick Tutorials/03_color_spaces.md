Explore HCL colors interactively in R
================

texas_income \<-
readRDS(url(“<https://wilkelab.org/SDS375/datasets/Texas_income.rds>”))

# 1.0 Penguins Data

### 1.1 Default Colors

Scatter plot of the penguin dataset using default colors

``` r
ggplot(penguins, aes(body_mass_g, bill_length_mm, color = species)) +
  geom_point(na.rm = TRUE) +
  theme_bw()
```

![](color_spaces_files/figure-gfm/unnamed-chunk-1-1.png)<!-- -->

### 1.2 Specified Colors

Manually pick three colors for a qualitative color scale. Use
**hue-chroma** plane to use colors with same luminance (i.e., perceived
the same by human eye).

Use `colorspace::hcl_color_picker()` which loads a *Shiny App*

``` r
colors <- c('#8BC875', '#7DBFF5', '#FC9EB1')
```

``` r
ggplot(penguins, aes(body_mass_g, bill_length_mm, color = species)) +
  geom_point(na.rm = TRUE) +
  theme_bw() +
  scale_color_manual(
    values = colors
  )
```

![](color_spaces_files/figure-gfm/unnamed-chunk-3-1.png)<!-- -->

# 2.0 Texas Income

``` r
texas_income <- readRDS(url("https://wilkelab.org/SDS375/datasets/Texas_income.rds"))
```

### 2.1 Default Colors

Choropleth plot of median income in Texas counties

``` r
ggplot(texas_income) +
  geom_sf(aes(fill = median_income))
```

    ## old-style crs object detected; please recreate object with a recent sf::st_crs()
    ## old-style crs object detected; please recreate object with a recent sf::st_crs()
    ## old-style crs object detected; please recreate object with a recent sf::st_crs()

![](color_spaces_files/figure-gfm/unnamed-chunk-5-1.png)<!-- -->

### 2.2 Using `viridis` scale

``` r
colors <- c(viridis(6)) # Sample six colors

ggplot(texas_income) +
  geom_sf(aes(fill = median_income)) +
  scale_fill_gradientn(
    colours = colors
  )
```

    ## old-style crs object detected; please recreate object with a recent sf::st_crs()
    ## old-style crs object detected; please recreate object with a recent sf::st_crs()
    ## old-style crs object detected; please recreate object with a recent sf::st_crs()

![](color_spaces_files/figure-gfm/unnamed-chunk-6-1.png)<!-- -->
