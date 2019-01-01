import java.util.*;

public class Multiples{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);

        int numberOfTimes= in.nextInt();

        for(int i=0; i<= numberOfTimes; i++)
        {
            if(i%3==0 && i%5==0)
                System.out.println(i);
        }

    }
}