# Euler 50. Consecutive prime sum

def primes_sieve2(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False


n=1000000
primes=list(primes_sieve2(n))
i=0
j=0
while j<n:
    j=j+primes[i]
    i=i+1

nexti=True
while nexti:
    suma=sum(primes[0:i])
    for k in range(1,len(primes)-i):
        if suma>n:
            break

        suma=suma-primes[k-1]+primes[k+i-1]
        if suma in primes:
            nexti=False
            break
    i=i-1

print(suma)