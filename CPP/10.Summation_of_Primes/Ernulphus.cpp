//Euler Problem_num 10
#include<iostream>

bool isPrime(int x);

int main()
{
  unsigned long sum = 2;
  int LAST_PRIME = 2000000;

  int p = 3;
  while (p < LAST_PRIME)
  {
    if (isPrime(p))
    {
      sum += p;
      std::cout << p << std::endl;
    }
    p++;
  }
  std::cout << sum << std::endl;
}

bool isPrime(int x)
{
  for (int i = 2; i < x; i++)
  {
    if (x%i == 0) //i is a factor of x
    {
      return false;
    }
  }
  return true;
}
