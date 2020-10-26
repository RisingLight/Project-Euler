#include<iostream>

using namespace std;

void mul35();

int main(void)
{
  mul35();
  return 0;
}


void mul35()
{
  cout<<" 100 numbers will be displayed :-\n";
  int i;
  for(i=1;i<=100;i++)
  {
    cout<<" "<<i<<": "<<3*i<<" - "<<5*i<<" \n";
  }
}
