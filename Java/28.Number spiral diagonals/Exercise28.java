public class Exercise28 {
		
	public static void main (String[] args) {

		long startTime = System.currentTimeMillis();	
		
		final int limit = 1001;
		int sum;
		int size; 
		int corner, diff;
		sum=1;

		for (size=3; size<=limit; size+=2) {
			corner = size*size;
			diff = size - 1;
			sum += 4 * corner - 6 * diff;	
		}
		System.out.println(sum);

        long endTime = System.currentTimeMillis();
        System.out.println("Program finished in " + (endTime - startTime) + " milliseconds");
	}
}