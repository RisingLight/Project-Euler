import java.math.BigInteger;

public class pragyanmehrotra{
    public static void main(String[] args) {
        BigInteger d = new BigInteger("2");
        BigInteger n = d.pow(1000);
        String sn = n.toString();
        int ans = 0;
        for(int i = 0;i<sn.length();i++){
            ans += sn.charAt(i) - '0';
        }
        System.out.println(ans);
    }
}