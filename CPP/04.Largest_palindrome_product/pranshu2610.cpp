// Project Euler : Problem Number 28

// A palindromic number reads the same both ways.
// The largest palindrome made from the product of two 2-digit numbers
//  is 9009 = 91 × 99.
// Find the largest palindrome made from the product of
// two 3-digit numbers.

#include<iostream>
using namespace std;
int isPal(int n);
int main()
{
    int i,j,big=0;
    for (i=100;i<1000;i++){
        for(j=i;j<1000;j++){
            if (isPal(i*j))
                {
                    if((i*j)>big)
                    {
                        big = i*j;
                    }
                }
        }
    }
    cout<<big<<endl;
}
int isPal(int n)
{
    int temp=n,reverseN=0,remainder;
    while( temp != 0)
       {
          remainder = temp % 10;
          reverseN = reverseN * 10 + remainder;
          temp /= 10;
       }
    if(n==reverseN)
    {
        return 1;
    }
    else
        return 0;
}
