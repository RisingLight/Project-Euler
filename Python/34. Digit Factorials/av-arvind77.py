#EULER PROBLEM 34 DIGIT FACTORIALS
from math import factorial
import time

start = time.time()

f = [factorial(0),
factorial(1),
factorial(2),
factorial(3),
factorial(4),
factorial(5),
factorial(6),
factorial(7),
factorial(8),
factorial(9)]


def factorial_digits(n):
	s = 0
	while n:
		s += f[n%10]
		n //= 10
	return s

solution = 0

for i in range(10,1854721):
	if factorial_digits(i) == i:
		solution += i

print(solution)
end = time.time()
print(end - start)