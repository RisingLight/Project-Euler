#  Solution to Euler problem 03
# Finds the largest prime factor of a given number N.

checkPrime <- function(p, n){
  while (!n%%p){
  n <- n%/%p
  }
  return(n)
}

maxPrime <- function(N){
  n <- N
  n <- checkPrime(2, n)
  if (n==1){
    return(2)
  }
  top = as.integer(sqrt(n))
  for (i in seq(3,top+2,2)){
    n <- checkPrime(i, n)    # Remove prime 'i' as factor of n
    if (n==1){
      return(i)
    }
  }
  return(n)
}

print(maxPrime(600851475143))
