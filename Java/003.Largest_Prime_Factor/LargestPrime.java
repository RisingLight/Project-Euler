
import java.util.Scanner;

public class LargestPrime {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int largestPrime = 0;
        int number = in.nextInt();
            for (int j = 2; j < number; j++) {
                if (number % j == 0 & isPrime(j)) {
                    largestPrime = j;
                }
            }

        System.out.println(largestPrime);
    }

    private static boolean isPrime(int j) {
        for (int i =2; i<j;i++)
        {
            if(j%i==0)
                return false;
        }
        return true;
    }

}
