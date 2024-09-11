# Homework 1

This first assignment will just have you practice what we learned in class the first day. If you follow the instructions carefully, you will get full credit and the whole assignment should only take you a few minutes.

1) If you are reading this you have accepted your assignment on GitHub Classroom. The next step is to clone this repository to your local machine so you can make edits and push them back up to GitHub Classroom. Clone this repository using one of the three methods discussed in class. Put the local repo somewhere you will remember to look.

2) Add two directories to your repo:

  - One directory should be called `R`.
  
  - The other directory should be called `Figures`.
  
3) Commit the changes from step 2 and use the following commit message:

> Project organization. Added directories R and Figures.

4) Add a new R script to the `R` directory. Name this script `hw1.R`. Open the script using RStudio.

5) Add the following lines to the script:

```r
set.seed(9876)

x <- rnorm(100)

hist(x)
```

6) Finally, add the following lines to the script, **but be sure to edit the code supplied to the `filename` argument**. Name the file `sample_hist.png` and have it save to the `Figures` directory. Be sure to use the `here()` function from package `here`, using the `::` notation.

```r
png(
  filename = <add-filename-here>,
  width = 4, height = 3,
  units = "in", 
  res = 300
)

  hist(x)
  
dev.off()
```

7) Run your script and double check that there is an image of a histogram saved in the `Figures` directory.

8) Commit the changes from steps 4-7 and add the following commit message:

> Added R script R/hw1.R and ran it, producing an image of a histogram saved to `Figures/sample_hist.png`.

9) Push your changes up to the remote.









