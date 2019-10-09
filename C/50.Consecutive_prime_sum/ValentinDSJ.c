//Euler problem 50
//Consecutive prime sum

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#define LIMIT 1000000

static bool is_prime(int x)
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

static void prime_tab(void)
{
    int *prime_tab = calloc(LIMIT / 4, sizeof(int));
    int length = 0;

    for (int x = 2; x < LIMIT; x++)
        if (is_prime(x)) {
            prime_tab[length] = x;
            length++;
        }
    prime_tab[length] = -1;
    
    int *sum_tab = calloc(length + 1, sizeof(int));

    sum_tab[0] = 0;
    length = 0;
    for (int x = 0; sum_tab[x] < LIMIT; x++) {
        sum_tab[x + 1] = sum_tab[x] + prime_tab[x];
        length++;
    }
    
    int res = 0;
    int temp_res = 0;
    int diff = 0;
    int temp_diff = 0;
    for (int x = length; x > 0; x--) {
        for (int y = 0; y < length; y++) {
            temp_res = sum_tab[x] - sum_tab[y];
            temp_diff = x - y;
            if (temp_res > LIMIT)
                break;
            if (is_prime(temp_res) && (temp_diff > diff)) {
                res = temp_res;
                diff = temp_diff;
            }
        }
    }
    printf("The biggest sum of consecutive primes is: %d\nWith: %d consecutive primes.\n", res, diff);
}

int main(void)
{
    prime_tab();
    return 0;
}