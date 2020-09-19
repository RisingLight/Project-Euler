//Euler problem03
using System;
namespace largest_prime_fac
{
    class largest_prime_fac
    {
        public static void Main()
        {
            long num = 600851475143;
            int count = 3;
            while (num > 1)
            {
                if (num % count == 0)
                {
                    num /= count;
                }
                else
                {
                    count += 2;
                }
            }
            Console.WriteLine("The largest prime factor of the number {0} is {1} ", 600851475143, count);
            Console.ReadKey();
        }
    }
}
