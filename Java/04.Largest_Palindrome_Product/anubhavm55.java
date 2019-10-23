//Euler Problem_04

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        int i,j,len,a0,n,f;
        int x,y;
        String s;
        z:for(a0 = 0; a0 < t; a0++){
            n = in.nextInt();
            for(i=n-1;i>=101101;i--)
            {
                f=0;
                s=Integer.toString(i);
                len=s.length();
                for(j=0;j<len;j++)
                {
                    if(s.charAt(j)!=s.charAt(len-j-1))
                    {
                        f=1;
                    }
                }
                if(f==0)
                {
                    for(x=100;x<=999;x++)
                    {
                        if(i%x==0)
                        {
                            if(((i/x)>=100)&&((i/x)<=999))
                            {
                                System.out.println(i);
                                continue z;
                            }
                        }
                    }
                }
            }
        }
    }
}