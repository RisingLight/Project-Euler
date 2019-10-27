
#include <bits/stdc++.h> 
using namespace std; 
  
void testSomeNumbers(int limit, int number) 
{ 
   if (number < 3) 
     return; 
  
   for (int a = 1; a <= limit; a++) 
     for (int b = a; b <= limit; b++) 
     { 
         //a^n + b^n = c^n ?
         int pow_sum = pow(a, number) + pow(b, number); 
         double c = pow(pow_sum, 1.0/number); 
         int c_pow = pow((int)c, number); 
         if (c_pow == pow_sum) 
         { 
            cout << "Count example found\n"; 
            return; 
         } 
     } 
  
     cout << "No counter example within given"
            " range and data\n"; 
} 
  
int main() 
{ 
    testSomeNumbers(10, 3); 
    return 0; 
} 
