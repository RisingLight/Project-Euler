using System;
using System.Numerics;
using System.Linq;

namespace FactorialDigitSum
{
    public class MainClass
    {
        public static void Main()
        {
            BigInteger number = factorial(new BigInteger(100));

            int ans = 0;
            foreach (char c in number.ToString())
            {
                ans += c - '0';
            }
            Console.WriteLine(ans);
        }

        private static BigInteger factorial(BigInteger n)
        {
            BigInteger res = new BigInteger(1);
            while (n > 1)
            {
                res *= n;
                n -= 1;
            }
            return res;
        }
    }
}