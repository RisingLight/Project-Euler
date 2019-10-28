// Problem 20 : Factorial digit sum
// n! means n × (n − 1) × ... × 3 × 2 × 1
// Find the sum of the digits in the number 100!

#include<stdio.h>

int main()
{
    int a[200],n,counter,temp;
    a[0]=1;
    counter=0;
    n = 100;
    for(; n>=2; n--)
    {
        temp=0;
        for(int i=0; i<=counter; i++)
        {
            temp=(a[i]*n)+temp;
            a[i]=temp%10;
            temp=temp/10;
        }
        while(temp>0)
        {
            a[++counter]=temp%10;
            temp=temp/10;
        }
    }
    int sum = 0;
    for(int i=0;i<=counter;i++)
        sum+=a[i];

    printf("Sum of digits in 100 factorial : %d",sum);

}