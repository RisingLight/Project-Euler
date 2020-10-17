library(gtools)

base <- 0:9

# run permutations
perm <- permutations(n = 10,
             r = 10,
             v = base)

# solution
# 2 7 8 3 9 1 5 4 6 0
perm[1000000, ]

