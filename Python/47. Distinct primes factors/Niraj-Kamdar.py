# Euler: 47. Distinct primes factors
from itertools import count

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
          71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157]
s = 0
for i in count(1):
    c = 0
    for j in primes:
        if i % j == 0:
            c += 1
        elif c == 4:
            s += 1
            break
    if j == primes[-1]:
        s = 0
    if s == 4:
        print(i-3, i-2, i-1, i)
        break
