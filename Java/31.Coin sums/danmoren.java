/*
	Project Euler - 31
*/
public class Exercise31 {

	public static void main (String[] args) {
		
		int sum = 0;

        for (int a = 0; a <= 200; a++) {
            for (int b = 0; b <= 100; b++) {
                for (int c = 0; c <= 40; c++) {
                    for (int d = 0; d <= 20; d++) {
				        for (int e = 0; e <= 10; e++) {
				            for (int f = 0; f <= 4; f++) {
				                for (int g = 0; g <= 2; g++) {
				                    if (a + 2 * b + 5 * c + 10 * d + 20 * e + 50 * f + 100 * g == 200) {
				                    	sum++;                    	
				                    }
				                }
				            }
				        }
                    }
                }
            }
        }
        sum = sum + 1;
        System.out.println(sum);
	}	
}