public class QuadraticPrimes {

	public static void main(String[] args) {

		System.out.println(maxQuadPrime());

	}

	public static int maxQuadPrime() {

		int maxN = 0;
		int maxA = 0;
		int maxB = 0;

		int currentMax = 0;

		for (int a = -999; a < 1000; a += 2) {
			for (int b = 3; b < 1000; b += 2) {
				currentMax = findMaxN(a,b);
				if (currentMax > maxN) {
					maxN = currentMax;
					maxA = a;
					maxB = b;
				}
			}
		}

		return maxA * maxB;
	}

	public static int findMaxN(int a, int b) {

		int max = 0;
		int n = 2;

		while (isPrime(n*n + a*n + b)) {
			if (n > max)
				max = n++;
		}

		return max;
	}

	public static boolean isPrime(int input) {

		if (input == 2) 
			return true;
		if (input <= 1) 
			return false;
		if (input % 2 == 0) 
			return false;

		/** 
		 * Only up to the square root. 
		 *  If there exists a factor between input and sqrt(input)
		 *  then that value will have a corresponding factor between 3 and sqrt(input)
		 */
		for (int i = input - 2; i >= Math.sqrt(input); i -= 2) {
			if (input % i == 0) 
				return false;
		}

		return true;
	}
}
