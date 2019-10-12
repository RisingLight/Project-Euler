// C program to find smallest number evenly divisible by all numbers 1 to n 
#include<stdio.h> 
#include<stdlib.h>

long long int gcd(long long int n1, long long int n2)
{  long long int result,i;
for(i=1; i <= n1 && i <= n2; ++i)
    {
        // Checks if i is factor of both integers
        if(n1%i==0 && n2%i==0)
            result = i;
    }
    return result;
    }

  
// Function returns the lcm of first n numbers 
long long int lcm(long long n) 
{ 
    long long int ans = 1;     
    for (long long int  i = 1; i <= n; i++) 
        ans = (ans * i)/(gcd(ans, i)); 
    return ans; 
} 
  
// Driver program to test the above function 
int main()  
{ 
    long long n = 20; 
    cout << lcm(n); 
    return 0; 
} 
