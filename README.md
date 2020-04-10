# Analysis of Network on Hero Journey Movies 🍿

This repository aims to share files about the Networks in Hero Journey Movies.
The movies are:

- Star Wars (1977)
- Lion King (1994)
- Matrix (1999)
- Harry Potter and Philosopher's stone (2001)
- Spiderman (2002)

### Prerequisites

- R version >= 3.5.3

- Python version >= 3.8.2

### Packages 

You may install some packages.

- R
  - iGraph
- Python
  - Enum
  - BeautifulSoup
  - Json
  - Requests
  - PPrint
  - Dataclasses
  
### Structure

The webscrapper access the The Movie Database and collect information about
those movies. Please do not run again because may overwritten the data files already created.


The data directory has all files that constructs the networks of the films. 
In relation and relations types folders, the files are adjacency matrix, in archetypes
are information about gender and archetype of each character.

The plots.md is a R Notebook with examples of usage of igraph and plot the graph of the
movies network
