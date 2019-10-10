# The number 197, is called a circular prime because all rotations of the
# digits:
# 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
# 73, 79, and 97.
#
# How many circular primes are there below one million?


def prime_sieve(n):
    """
    Return a list of prime numbers from 2 to a prime < n.
    Very fast (n<10,000,000) in 0.4 sec.
    Example:
    >>>prime_sieve(25)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    Algorithm & Python source: Robert William Hanks
    http://stackoverflow.com/questions/17773352/python-sieve-prime-numbers
    """
    sieve = [True] * (n/2)
    for i in xrange(3, int(n**0.5)+1, 2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1, n/2) if sieve[i]]


def is_prime(number):

    if number == 2 or number == 3:
        return True
    if number < 2 or number % 2 == 0:
        return False
    if number < 9:
        return True
    if number % 3 == 0:
        return False

    limit = int(number**0.5)
    check = 5

    while check <= limit:
        if number % check == 0:
            return False
        if number % (check+2) == 0:
            return False
        check += 6

    return True


def is_circular(number):
    number_str = str(number)
    iterations = len(number_str) - 1

    for _ in range(iterations):
        number_str = number_str[-1]+number_str[:-1]
        if not is_prime(int(number_str)):
            return False
    return True

primes = prime_sieve(1000000)
result = sum([1 for prime in primes if is_circular(prime)])

print result