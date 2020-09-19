//Euler problem07
using System;
using System.Collections.Generic;
using System.Linq;

namespace _Prime_10001st
{
    class Prime_10001st
    {
        public static void Main()
        {
            List<long> primeNumbers = new List<long>() { 2 };
            for (long i = 3; i < long.MaxValue; i += 2)
            {
                if (!primeNumbers.Any(p => (i % p) == 0))
                {
                    primeNumbers.Add(i);
                    if (primeNumbers.Count == 10001)
                    {
                        Console.WriteLine(i);
                        break;
                    }
                }
            }
        }
    }
}
