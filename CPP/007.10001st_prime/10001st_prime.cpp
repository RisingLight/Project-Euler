#include <bits/stdc++.h>
#define MAXS 1000007

using namespace std;

typedef vector<int> vi;
bool visited[MAXS];

/**
 * k is wich prime number you want to get.
 * 
 * This function looks for prime numbers 
 * between 1 and MAXS, passing as a parameter 
 * which prime number you want to get. The 
 * function returns -1 if the kth prime number
 * is not between 1 and MAXS.
 * */
int sieveOfEratosthenes10001st(int k) {
   int result = -1;
   int countOfPrimes = 0;

   bool found = false;
   int j; int i = 2;
   while(i < MAXS && !found) {

      if(!visited[i]){
         countOfPrimes++;

         if(countOfPrimes == k) {
            result = i;
            found = true;
         } else {
            j = 2;

            while(j * i < MAXS) {
               visited[j*i] = true;
               j++;
            }
         }
      }

      i++;
   }

   return result;
}


int main() {

   cout << sieveOfEratosthenes10001st(10001) << endl;

   return 0;
}
