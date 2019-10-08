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
    if (x % 2 == 0 || x % 3 == 0)
        return false;
    while ((y * y) <= x) {
        if (x % y == 0 || x % (y + 2) == 0)
            return false;
        y += 6;
    }
    return true;
}

int main(void)
{
    int total = 0;
    
    for (int x = 2; ; x++) {
        if (is_prime(x) && (total + x) > LIMIT)
            break;
        else if (is_prime(x)) {
            printf("%d\n", total);
            total += x;
        }
    }
    printf("%d\n", total);
    return 0;
}