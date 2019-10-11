import 'dart:math'; 
bool isPrime(int number)
{
  bool result = true;
  for(int i = 2; i<=sqrt(number).floor(); i++)
  {
    if(number % i == 0)
    {
      result = false;
      break;
    }
  }
return result;
}
largestFactor()
{
  var n = 600851475143;
  var t = sqrt(n).floor();
  var prime = 2;
  while(t>1)
  {
    if(n%t == 0 && isPrime(t))
    {
      prime = t;
      break;
    }
    t--;
  }
  return prime;
}


void main() {
  
  
  print("Largest Factor 0f 600851475143 is ");
  print(largestFactor());
  
}
