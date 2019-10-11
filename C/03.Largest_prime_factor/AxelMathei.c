// Euler 03

#include <stdio.h>
#include <math.h>

int main() {
    long long n = 600851475143;
    long long lastFactor = 0;
    if (n % 2 == 0) {
        lastFactor = 2;
        n /= 2;
        while (n % 2 == 0)
            n /= 2;
    }
    else
        lastFactor = 1;
    long long factor = 3;
    long long maxFactor = sqrtl(n);
    while (n > 1 && factor <= maxFactor) {
        if (n % factor == 0) {
            n /= factor;
            lastFactor = factor;
            while (n % factor == 0)
                n /= factor;
            maxFactor = sqrtl(n);
        }
        factor += 2;
    }
    if (n == 1)
        printf("%lld", lastFactor);
    else
        printf("%lld", n);
}
