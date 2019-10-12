# Euler: 10.Summation of primes
from sys import stdout
n = 50  # Enter Input here
A = [True]*n
for i in range(2, int(n**0.5)):
    if A[i]:
        for j in range(i**2, n, i):
            A[j] = False

stdout.write('{}\n'.format(sum((i for i in range(2, n) if A[i]))))
