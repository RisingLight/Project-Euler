// Problem 10 : Summation of primes
// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
// Find the sum of all the primes below two million.

#include<stdio.h>
#include<math.h>

int prime(long n);
// return 1 if n is prime, else returns 0

int main()
{
    long n = 2000000;
    long sum = 2;
    for(long i = 3; i<n; i++)
    {
        if(prime(i)) sum += i;
    }

    printf("%ld",sum);
}

int prime(long n)
{
    for(long i=2;i<=sqrt(n);i++)
    {
        if(n%i==0) return 0;
    }

    return 1;
}