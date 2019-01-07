
#include<iostream>
using namespace std;

void fibo()
{ long input=0,num1=0,num2=1,i=0,count; // giving default values

  cout<<" Enter the limit for the number of output from the series:- ";
  cin>>input;
  for(i=0,count=0;i<input;i++)
  {
    if((num1+num2)%2==0)
    {cout<<" num"<<count+1<<": "<<num1+num2<<" "; // Printing next number
    count++;
}
    num1=num1+num2;       //   moving to the next number by swap
    num2=num1-num2;
    num1=num1-num2;

    num2= num1+num2;     //  next value updated
  }
}

int main(void)
{
  fibo();       // Fibo Fucntion call
  return 0;
}
