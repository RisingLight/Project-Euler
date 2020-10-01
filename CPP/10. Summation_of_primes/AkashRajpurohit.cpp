/*
    Problem 10 : Summation of primes
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
*/

#include <bits/stdc++.h> 
using namespace std; 
  
long long checkPrime(int n) { 
    bool prime[n+1]; 
    memset(prime, true, sizeof(prime)); 
  
    for (int p=2; p*p<=n; p++)  { 
        if (prime[p] == true) {
            for (int i=p*p; i<=n; i += p) 
                prime[i] = false; 
        } 
    }

    long long result = 0;
  
    // Print all prime numbers 
    for (int p=2; p<=n; p++) 
       if (prime[p]) result += p; 
    
    return result;
} 

int main() { 
    int n = 2000000;
    long long result = checkPrime(n); 
    cout << "Result: " << result;
    return 0; 
}