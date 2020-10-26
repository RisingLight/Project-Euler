//Euler 20 Factorial digit sum done in Java

import java.math.BigInteger;

public class pragyanmehrotra {

    static BigInteger factorial(BigInteger n){
        if(n.equals(new BigInteger("1")) || n.equals(new BigInteger("0")))
            return new BigInteger("1");
        return n.multiply(factorial(n.subtract(new BigInteger("1"))));
    }

    public static void main(String[] args) {
        BigInteger d = new BigInteger("100");
        BigInteger n = factorial(d);
        String sn = n.toString();
        int ans = 0;
        for(int i = 0;i<sn.length();i++){
            ans += sn.charAt(i) - '0';
        }
        System.out.println(ans);
    }
}