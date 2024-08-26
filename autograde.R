
if(!require(testthat)){
  install.packages("testthat")
}

library(testthat)

test_that(
  "Directory structure is correct",
  {expect_true(
    dir.exists("R")
  )
  expect_true(dir.exists("Figures"))
  expect_true(file.exists("Figures/sample_hist.png"))
  expect_true(file.exists("R/hw1.R"))}
)


