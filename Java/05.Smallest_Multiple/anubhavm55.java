//Euler Problem_5
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class anubhavm55 {
    static int hcf(int a,int b)
        {
            while(a!=b)
            {
                if(a>b)
                    a=a-b;
                else
                    b=b-a;
            }
            return a;
        }

    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        int i;
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            int dp[]=new int[n+1];
            for(i=1;i<=n;i++)
            {
                if(i==1)
                    dp[i]=1;
                else
                    dp[i]=(i*dp[i-1])/hcf(i,dp[i-1]);
            }
            System.out.println(dp[n]);
        }
    }
}