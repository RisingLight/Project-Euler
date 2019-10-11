/*
Problem 10 - Summation of Primes
*/

#include <bits/stdc++.h>
using namespace std;

long n = 2000000;

int isPrime(long val) {
    for(auto i = 2;i<=sqrt(val);i++){
        if(val%i==0){
            return 0;
        }
    }
    return 1;
}

int main() {
    long sum=2;
    for(auto i = 3;i<n;i++){
        if(isPrime(i)){
            sum+=i;
        }
    }
    cout<<sum;
}
