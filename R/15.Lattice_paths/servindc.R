#  Solution to Euler problem 15
Lattice_paths <- function(n){
  n <- as.integer(n)
  p <- 0
  for (i in 0:n){
    p <- p + (factorial(n)/(factorial(n-i)*factorial(i)))^2
  }
  print(p)
}
cat("Routes through a 20x20 grid: ", Lattice_paths(20))
