import java.util.Scanner;

public class SumSquareDifference {

    public static void sumsquarediff() {
        Scanner input = new Scanner(System.in);
        System.out.print("Please enter a number: ");
        int sum_of_squares = 0;
        int squares_of_sums = 0;

        int num = input.nextInt();

        for (int i = 1; i < num+1; i++) {
            sum_of_squares += i * i;
            squares_of_sums += i;
        }

        squares_of_sums *= squares_of_sums;

        System.out.println(squares_of_sums - sum_of_squares);

    }
}


