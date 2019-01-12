#include<iostream>
using namespace std;

int main()
{
  lpf();
return 0;
}

void lpf()
{int num1,num2,i,oldn=1,newn=0;
  cout<<" Enter the 2 numbers you want to find the largest prime factor ";

  cin>>num;
  num2=sqrt(num);
  for(i=1;i<num2;i++)
    {if(num1%i==0)
      {
        if(i>newn)
          { newn=i}
        }

    }
cout<<"\n The largest prime number is "<<newn;
  }
