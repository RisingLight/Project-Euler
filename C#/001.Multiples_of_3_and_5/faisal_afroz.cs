// Euler Problem_001 by faisal_afroz with O(1) complexity.
using System;

namespace MultiplesOf3and5
{
    public class Program
    {
        public static void Main()
        {
            int maxNumber=1000;
            int x = (maxNumber-1)/3;
            int y = (maxNumber-1)/5;
            int z = (maxNumber-1)/15;
            int sum3 = (3*x*(x+1))/2;
            int sum5 = (5*y*(y+1))/2;
            int sum15 = (15*z*(z+1))/2;
            int sum = sum3 + sum5 - sum15;
            Console.WriteLine(sum);
        }
    }
}
