
/*
 * Problem 07: 10001st Prime
 * Using Sieve of Eratosthene to filter out the prime numbers
 * program will keep a counter to count number of primes
 * once the counter reaches the 10001 
 * program will return the prime number at this counter
 */
int sieveOfE(int number)
{
  var visited = new List.filled(10000007,false);
  int res = 0;
  int primecount = 0;
  bool found = false;
  int i = 2, j;
  while(i < 10000007 && !found)
  {
    if(!visited[i])
    {
      primecount++;
      if(primecount == number)
      {
        res = i;
        found = true;
      }
      else{
        j = 2;
        while(j*i < 10000007)
        {
          visited[j*i] = true;
          j++;
        }
      }
      
    }
    i++;
  }
  return res;
}
void main() {
  print(sieveOfE(10001));
  
}
