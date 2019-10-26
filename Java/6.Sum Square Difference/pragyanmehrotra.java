//Euler 6 Sum square difference done in Java

import java.math.BigInteger;

public class pragyanmehrotra {
    
    public static void main(String[] args) {
        BigInteger sum = new BigInteger("0");
        BigInteger sumOfSquares = new BigInteger("0");
        for(BigInteger i = new BigInteger("1");!i.equals(new BigInteger("101"));i = i.add(new BigInteger("1"))){
            sum = sum.add(i);
            sumOfSquares = sumOfSquares.add(i.multiply(i));
        }
        BigInteger squareOfSum = sum.multiply(sum);
        BigInteger diff = squareOfSum.subtract(sumOfSquares);
        System.out.println(diff);
    }
}