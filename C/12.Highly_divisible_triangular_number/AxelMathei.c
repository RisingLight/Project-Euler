// Euler 12

#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isPrime(int n) {
    if (n == 1)
        return false;
    else if (n < 4)
        return true;
    else if (n % 2 == 0)
        return false;
    else if (n < 9)
        return true;
    else if (n % 3 == 0)
        return false;
    else {
        int r = sqrt(n);
        int f = 5;
        while (f <= r) {
            if ((n % f == 0) || (n % (f + 2) == 0))
                return false;
            f += 6;
        }
        return true;
    }
}


int main() {
    long n = 3; // start with a prime
    int Dn = 2; // number of divisors for any prime
    int cnt = 0; // to insure the while loop is entered
    int n1, Dn1, exponent;
    const int P = 200;
    int primearray[P];
    
    // Initialize primearray
    int idx = 0;
    int candidate = 1;
    do {
        candidate += 1;
        if (isPrime(candidate)) {
            primearray[idx] = candidate;
            idx++;
        }
    } while (idx < P);
    
    while (cnt <= 500) {
        n++;
        n1 = n;
        if (n1 % 2 == 0)
            n1 /= 2;
        Dn1 = 1;
        for (int i = 0; i < P; i++) {
            if (primearray[i] * primearray[i] > n1) {
                Dn1 *= 2;
                break;
                /*
                * When the prime divisor would be greater than the residual n1,
                * that residual n1 is the last prime factor with an exponent=1. 
                * No necessity to identify it.
                */
            }
            exponent = 1;
            while (n1 % primearray[i] == 0) {
                exponent++;
                n1 /= primearray[i];
            }
            if (exponent > 1)
                Dn1 *= exponent;
            if (n1 == 1)
                break;    
        }
        cnt = Dn * Dn1;
        Dn = Dn1;
    }
    printf("%ld\n", n * (n - 1) / 2);
}
