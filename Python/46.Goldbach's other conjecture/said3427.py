# Euler 46.Goldbach's other conjecture
import math
def primes_sieve2(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False

def isComposite(x):
	for i in range(2,x):
		if x%i==0 and i!=x:
			return True
	return False
	
i=9
while True:
	if isComposite(i):
		n=0
		for j in primes_sieve2(i):
			probe=math.sqrt((i-j)/2)
			if probe.is_integer():
				n+=1
		if n==0:
			break
	i+=2

print(i)