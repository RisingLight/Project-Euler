#include<iostream>
#include<math.h>
using namespace std;

int main(){
   long n=100,m,a,s;

            a =(n * (n + 1) * (2*n + 1) )/ 6;  //Sum of Squares of 100 natural numbers
            m = (n * (n + 1)) / 2; //Sum of first 100 Natural Numbers
            s = m*m; //Square of Sum of first 100 natural numbers
            
    cout<<"Difference between the Sum of the Squares of the 1st 100 natural numbers and the square of the sum is : "<<s-a;


return 0;

}
