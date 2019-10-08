'''
Project Euler Challenger 10. Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

# Fast Exponentiation
# number to find summation of all primes below number
last_prime = 2000000

# create a set excluding even numbers
numbers = set(xrange(3, last_prime + 1, 2)) 

for number in xrange(3, int(last_prime ** 0.5) + 1):
    if number not in numbers:
        #number must have been removed because it has a prime factor
        continue

    num = number
    while num < last_prime:
        num += number
        if num in numbers:
            # Remove multiples of prime found
            numbers.remove(num)

print 2 + sum(numbers)
