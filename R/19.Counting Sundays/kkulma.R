library(lubridate)
library(dplyr)

base <- data.frame(
  date = seq(as.Date("1901-01-01"), as.Date("2000-12-31"), by = "day")
)

# solution
# 171
base %>% 
  dplyr::mutate(dname = lubridate::wday(date, label = TRUE)) %>% 
  dplyr::filter(lubridate::day(date) == 1 & dname == "Sun")
