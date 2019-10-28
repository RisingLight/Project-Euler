// Euler 1
using System;

namespace _5_multiples
{
    public class MainClass
    {
        public static void Main()
        {
            int currentNumber = 1000;
            int allSum = 0;

            currentNumber = currentNumber - 1;
            while (currentNumber > 0)
            {
                if ( (currentNumber % 3 == 0) | (currentNumber % 5 == 0))
                {
                    allSum = allSum + currentNumber;
                }
                currentNumber = currentNumber - 1;
            }
            Console.WriteLine(allSum);
        }
    }
}
