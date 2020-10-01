 ## Project Euler 5: Smallest Multiple

  answer <- 2520
  while (sum(answer %% (1:20)) != 0) {
      answer <- answer + 2520                   # Increase by smallest number divisible by 1:10
  }
  print(answer)
