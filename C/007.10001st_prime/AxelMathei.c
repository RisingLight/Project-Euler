// Euler 07

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
    const int LIMIT = 10001;
    int count = 1;
    int candidate = 1;
    do {
        candidate += 2;
        if (isPrime(candidate))
            count += 1;
    } while (count < LIMIT);
    printf("%d", candidate);
}
