"""
Euler discovered the remarkable quadratic formula:
n2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 412 + 41 + 41 is clearly divisible by 41.
The incredible formula  n2 − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:
n² + an + b, where |a| &lt; 1000 and |b| &lt; 1000
where |n| is the modulus/absolute value of ne.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""
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
