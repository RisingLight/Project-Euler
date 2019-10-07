#include <iostream>  
using namespace std;  
int main() {  
  int n1=0,n2=1,n3,i=1;    
while(1)   
 {    
  n3=n1+n2;    
  if(1000-n3<=0)
  {
      break;
  }
  i++;
  n1=n2;    
  n2=n3;    
 }   
 cout << i+1;
   return 0;  
   }  