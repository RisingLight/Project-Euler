# Euler 47.Distinct primes factors
import math

def factor(n):
	if n <= 1: return []
	prime = next((x for x in range(2, math.ceil(math.sqrt(n))+1) if n%x == 0), n)
	return [prime] + factor(n//prime)

n=4
i=0
end=0
while True:
	i+=1
	l=len(set(factor(i)))
	if l != n:
		end=0
	else:
		end+=1
	if end==n:
		result=i-n+1
		break

print(result)