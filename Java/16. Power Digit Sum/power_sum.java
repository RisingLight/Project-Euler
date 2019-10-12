import java.math.BigInteger;

public class Problem16 {

	public static void main(String[] args) {

		int a = 2;
		int b = 1000;
		// Converting Integer to BigInteger.
		BigInteger number = new BigInteger(String.valueOf(a));
		// Getting 2^1000.
		BigInteger power = number.pow(b);
		// Converting BigInteger to String.
		String powerInString = String.valueOf(power);
		int length = powerInString.length();
		int sum = 0;
		int temp = 0;
		for (int i = 0; i < length; i++) {
			// Converting char to int.
			temp = powerInString.charAt(i) - 48;
			sum += temp;
		}
		System.out.println("The sum of the digits of the number 2^1000 is : " + sum);
	}

}