#include <stdio.h>


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