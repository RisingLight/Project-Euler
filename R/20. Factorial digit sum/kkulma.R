power_digit_sum <- function(num, ...) {
  tidy_num <- formatC(num, ...)
  num_char <- as.character(tidy_num)
  num_split <- unlist(strsplit(num_char, split = ""))
  sum(as.numeric(num_split))
}

# show that the example works
power_digit_sum(factorial(10), format = "f", digits = 0)

# solution
# 645
power_digit_sum(factorial(100), format = "f", digits = 0)


