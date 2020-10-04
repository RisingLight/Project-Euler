import java.math.BigInteger;

public class Kimi450 {
    public static void main(String[] args) {
        BigInteger prev = new BigInteger("0");
        BigInteger current = new BigInteger("1");
        BigInteger temp = new BigInteger("0");
        int index = 1;
        while (current.toString().length() < 1000){ 
            temp = current;
            current = prev.add(current);
            prev = temp;
            index ++;
        }    
        System.out.println(index);
    }
}