#include <stdio.h>

// Project Euler : Problem Number 05

// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

int main()
{
    for (int i = 1; i <= 1000000000; i++)
    {
        int track = 0;
        for (int j = 1; j <= 20; j++)
        {
            if ((i % j) == 0)
            {
                track += 1;
                if (track == 20)
                {
                    if (i % 2 == 0)
                    {
                        printf("%d\n", i);
                        return 0;
                    }
                }
            }
        }
    }
}
