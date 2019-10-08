#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#define LIMIT 1000000

bool is_prime(int x)
{
    int y = 5;

    if (x <= 3)
        return true;
    else if ((x % 2 == 0) || (x % 3 == 0))
        return false;
    while ((y * y) <= x) {
        if ((x % y == 0) || (x % (y + 2) == 0))
            return false;
        y += 6;
    }
    return true;
}

int prime_sum(int start)
{
    int total = 0;
    int temp;
    int count = 0;

    for (int x = start; ; x++) {
        temp = is_prime(x);
        if (temp && (total + x) > LIMIT)
            break;
        else if (temp)
            total += x;
    }
    return total;
}

int main(void)
{
    int total;

    for (int x = 2; !is_prime(total); x++) {
        total = prime_sum(x);
        printf("%d\n", total);
    }
    return 0;
}