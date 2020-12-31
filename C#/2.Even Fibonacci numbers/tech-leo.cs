using System;
class Program
{
    static void Main(string[] args)
    {
        int FirstNumber = 0;
        int SecondNumber = 1;
        int i = 0;
        int sum;
        int numberOfTimes = 0;
        Console.WriteLine("Enter Number of Terms: ");
        string input = string.Empty;
        do
        {
            input = Console.ReadLine();
        } while (!Int32.TryParse(input, out numberOfTimes));

        numberOfTimes = int.Parse(input);
        while (i != numberOfTimes)
        {
            sum = FirstNumber + SecondNumber;
            if (sum % 2 == 0)
            {
                i++;
                Console.WriteLine(sum);
            }
            FirstNumber = SecondNumber;
            SecondNumber = sum;
        }

        Console.ReadKey();

    }
}

