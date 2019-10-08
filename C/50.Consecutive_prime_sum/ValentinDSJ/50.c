#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#define limit 1000000

bool is_prime(uint16_t x)
{
    uint16_t y = 5;

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

uint16_t prime_sum(uint16_t n, uint16_t total)
{
   
}

int main(void)
{
    uint16_t res;
    res = prime_sum(3, 2);
    printf("%s\n", res);
    return 0;
}