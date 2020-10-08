power_digit_sum <- function(num, ...) {
  tidy_num <- formatC(num, ...)
  num_char <- as.character(tidy_num)
  num_split <- unlist(strsplit(num_char, split = ""))
  sum(as.numeric(num_split))
}

# show that the example works
power_digit_sum(2^15)

# solution
# 1200
power_digit_sum(2^1000, format = "f", digits = 0)


