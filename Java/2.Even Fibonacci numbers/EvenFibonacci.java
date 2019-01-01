import java.util.Scanner;

public class EvenFibonacci {
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int firstNumber= 0;
        int secondNumber=1;
        int i=0;
        int sum;
        System.out.print("Enter number of terms: ");
        int numberOfTimes= in.nextInt();

       while(i!=numberOfTimes){
           sum=firstNumber+secondNumber;
           if(sum%2==0)
           {
              i++;
              System.out.println(sum);
           }
           firstNumber=secondNumber;
           secondNumber=sum;
       }

    }
}

