
#include<iostream> 
#include<cstring>
using namespace std; 
  
long long int sumprimes(long long int n) 
{ 
    
    bool prime[n + 1]; 
  
    // Create a boolean array "prime[0..n]" 
    // and initialize all entries it as true. 
    // A value in prime[i] will finally be 
    // false if i is Not a prime, else true. 
    memset(prime, true, n + 1); 
  
    for (long long int p = 2; p * p <= n; p++) { 
  
        // If prime[p] is not changed, then 
        // it is a prime 
        if (prime[p] == true) { 
  
            // Update all multiples of p 
            for (long long int i = p * 2; i <= n; i += p) 
                prime[i] = false; 
        } 
    } 
  
    // Return sum of primes generated through 
    // Sieve. 
   long long int sum = 0; 
    for (long long int i = 2; i <= n; i++) 
        if (prime[i]) 
            sum += i; 
    return sum; 
} 
  
// Driver code 
int main() 
{ 
    int n = 2000000; 
    cout << sumprimes(n); 
    return 0; 
} 
