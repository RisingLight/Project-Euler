import java.util.Scanner;

public class Oasis99hs {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        long a = 1;
        for (int i = 1; i <= number; i++) {
            a = a * i / gcd(a, i);
        }
        System.out.println(a);
    }

    private static long gcd(long a, long b) {
        if (b != 0) {
            return gcd(b, a % b);
        } else {
            return a;
        }
    }
}