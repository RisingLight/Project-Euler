#include <stdio.h>
#define MAX_DIGIT 200

int main()
{
    //Find and Store 100! in array because no datatype can store such a huge value.
    int fact[MAX_DIGIT] = {1};
    
    int number_of_digit = 1,i,j,carry = 0,sum=0;
    for(j=2;j<=100;j++)
    {
        for(i=0; i<number_of_digit; i++)
            {
            int x = fact[i]*j; //product
            fact[i] = (x+carry)%10;
            carry = (x+carry)/10;
        
            //we are at end of the number with some carry remaining.
            //number of digit will increase by 1
            if (i == number_of_digit-1 && carry>0)
            number_of_digit++;
            }
    }
    //to display the calculated factorial.
    printf("100!= ");
    for(i=number_of_digit-1; i>=0; i--)
    {
        printf("%d",fact[i]);
    }
    printf("\n");
    
    //To Display the sum og it's digit.
    printf("Sum of digit of 100! = ");
    for(i=number_of_digit-1; i>=0; i--)
    {
        sum=sum+fact[i];
        
    }
    printf("%d",sum);

    return 0;
}
