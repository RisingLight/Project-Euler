#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

static int int_size(int nbr)
{
    int i = 0;
    int mod_nbr = 10;
    int count = 0;

    if (nbr < 0)
        count += 1;
    while (i != nbr){
        count += 1;
        i = nbr % mod_nbr;
        mod_nbr *= 10;
    }
    return (count);
}

static char *my_putnbr_string(int nb)
{
    long mod_number = 10;
    int y;
    int i = 0;
    char *string = malloc(int_size(nb) + 1);

    if (nb < 0){
        nb = nb * -1;
    }
    while (nb % mod_number != nb){
        mod_number *= 10;
    }
    for (int x = mod_number; x >= 10; x = x / 10){
        y = (nb % x) / (x / 10) + 48;
        string[i] = y;
        i += 1;
    }
    return (string);
}

bool is_palindrome(int x)
{
    char *str = my_putnbr_string(x);

    for (int x = 0, y = strlen(str) - 1; x <= y; x++, y--) {
        if (str[x] != str[y])
            return false;
    }
    return true;
}

int main(void)
{
    int res = 0;
    int temp = 0;
    
    for (int x = 999; x > 0; x--) {
        for (int y = 999; y > 0; y--) {
            temp = x * y;
            if (is_palindrome(temp) && (temp > res))
                res = temp;
        }
    }
    printf("%d\n", res);
    return 0;
}