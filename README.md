# Algorithmic-Redistricting
**Deep Reinforcement Learning project for Redistricting.**

Our Project was to build a Deep Reinforcement Learning Model to perform redistricting in the state of Iowa. 

## Problem Statement

- Redistricting Plans can have the impact of enabling political parties to gain unfair advantages through gerrymandering. GerryMadering is the art of drawing districts in favour of one political party which can often lead to inaccurate representation of the vote distribution. While no Machine Learning Model is free from biases because they are programmed by us at the end of the day, but what we can do is at least bring insights from data to make a more fairer redistricting plan that can potray a more accurate depiction of the actual vote distribution.

## Tools
- Programming Language - Python
  - Librabries - Pandas, Matplotlib, Seaborn 
  - Deep Learning Framework - PyTorch
  - Developement Environment - Google Collab, Jupyter Notebook

# Objective 
- We decided to use the state of Iowa as our dataset on which to perfrom algorithmic redistricting. 

# Data
- We used the mggg-states github to use the Iowa Shapefile that they had: [mggg-states](https://github.com/mggg-states/IA-shapefiles#metadata). We used [mygeodata](https://mygeodata.cloud/converter/shp-to-csv) to convert Iowa Shapefiles to a CSV format 

####  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Metadata
- `STATEFP10`: State FIPS code
- `COUNTYFP`: County FIPS
- `GEOID10`: State and county FIPS
- `NAME10`: County name
- `NAMELSAD`: County legal and statistical name
- `ALAND10`: Area land in square meters
- `AWATER10`: Area water in square meters
- `INTPTLAT10`: Latitude of internal point
- `INTPTLON10`: Longitude of internal point
- `TOTPOP`: Total population
- `NH_WHITE`: White, non-hispanic, population
- `NH_BLACK`: Black, non-hispanic, population
- `NH_AMIN`: American Indian and Alaska Native, non-hispanic, population
- `NH_ASIAN`: Asian, non-hispanic, population
- `NH_NHPI`: Native Hawaiian and Pacific Islander, non-hispanic, population
- `NH_OTHER`: Other race, non-hispanic, population
- `NH_2MORE`: Two or more races, non-hispanic, population
- `HISP`: Hispanic population
- `H_WHITE`: White, hispanic, population
- `H_BLACK`: Black, hispanic, population
- `H_AMIN`: American Indian and Alaska Native, hispanic, population
- `H_ASIAN`: Asian, hispanic, population
- `H_NHPI`: Native Hawaiian and Pacific Islander, hispanic, population
- `H_OTHER`: Other race, hispanic, population
- `H_2MORE`: Two or more races, hispanic, population
- `VAP`: Total voting age population
- `HVAP`: Hispanic voting age population
- `WVAP`: White, non-hispanic, voting age population
- `BVAP`: Black, non-hispanic, voting age population
- `AMINVAP`: American Indian and Alaska Native, non-hispanic, voting age population
- `ASIANVAP`: Asian, non-hispanic, voting age population
- `NHPIVAP`: Native Hawaiian and Pacific Islander, non-hispanic, voting age population
- `OTHERVAP`: Other race, non-hispanic, voting age population
- `2MOREVAP`: Two or more races, non-hispanic, voting age population
- `TOTVOT00`: Number of votes cast in 2000 presidential race
- `PRES00D`: Number of votes for 2000 Democratic presidential candidate
- `PRES00R`: Number of votes for 2000 Republican presidential candidate
- `PRES00G`: Number of votes for 2000 Green Party presidential candidate
- `PRES00OTH`: Number of votes for 2000 other presidential candidates
- `TOTVOT04`: Number of votes cast in 2004 presidential race
- `PRES04D`: Number of votes for 2004 Democratic presidential candidate
- `PRES04R`: Number of votes for 2004 Republican presidential candidate
- `PRES04OTH`: Number of votes for 2004 other presidential candidates
- `TOTVOT08`: Number of votes cast in 2008 presidential race
- `PRES08D`: Number of votes for 2008 Democratic presidential candidate
- `PRES08R`: Number of votes for 2008 Republican presidential candidate
- `PRES08OTH`: Number of votes for 2008 other presidential candidates
- `TOTVOT12`: Number of votes cast in 2012 presidential race
- `PRES12D`: Number of votes for 2012 Democratic presidential candidate
- `PRES12R`: Number of votes for 2012 Republican presidential candidate
- `PRES12OTH`: Number of votes for 2012 other presidential candidates
- `TOTVOT16`: Number of votes cast in 2016 presidential race
- `PRES16D`: Number of votes for 2016 Democratic presidential candidate
- `PRES16R`: Number of votes for 2016 Republican presidential candidate
- `PRES16OTH`: Number of votes for 2016 other presidential candidates
- `CD`: Congressional district ID
