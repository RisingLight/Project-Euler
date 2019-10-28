// Project Euler : Problem Number 02
using System;
namespace _2._Even_Fibonacci_numbers
{
    class EvenFiboNumbers
    {
        static int evenFibSum(int limit)
        {
            if (limit < 2)
                return 0;

            // Initialize first two even 
            // prime numbers and their sum 
            long ef1 = 0, ef2 = 2;
            long sum = ef1 + ef2;

            // calculating sum of even  
            // Fibonacci value 
            while (ef2 <= limit)
            {

                // get next even value of  
                // Fibonacci sequence 
                long ef3 = 4 * ef2 + ef1;

                // If we go beyond limit, 
                // we break loop 
                if (ef3 > limit)
                    break;

                // Move to next even number 
                // and update sum 
                ef1 = ef2;
                ef2 = ef3;
                sum += ef2;
            }

            return (int)sum;
        }

        // Driver code 
        public static void Main()
        {
            int limit = 4000000;
            Console.Write(evenFibSum(limit));

        }
    }
}
