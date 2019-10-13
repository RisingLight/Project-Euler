# Euler 49. Prime Permutations
# Not an optimized solution, but it works.
def primes_sieve2(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False

primes=[x for x in primes_sieve2(9999) if len(str(x))==4 and x not in [1487, 4817, 8147]] 

def Euler49():
	for i in range(len(primes)):
		d1=primes[i]
		primeraresta=set([x-d1 for x in primes[i+1::]])
		for j in range(i+1,len(primes)):
			d2=primes[j]
			for k in range(j+1,len(primes)):
				d3=primes[k]
				if d2-d1==d3-d2:
					FirstPrime=set(list(str(d2)))
					SecondPrime=set(list(str(d1)))
					ThirdPrime=set(list(str(d3)))
					if len(ThirdPrime.intersection(FirstPrime).intersection(SecondPrime))==len(FirstPrime) and len(FirstPrime)==len(SecondPrime) and len(SecondPrime)==len(ThirdPrime):
						return(print("%s%s%s"%(d1,d2,d3)))

Euler49()