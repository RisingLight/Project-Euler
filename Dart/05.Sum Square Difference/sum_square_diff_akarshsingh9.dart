int sumOfSquares(int n)
{
  int twon = 2*n;
  int prod = n*(n+1)*(twon+1);
  int result = (prod/6).floor();
  return result;
}

int sumOfn(int n)
{
  int prod = n*(n+1);
  int result = (prod/2).floor();
  return result;
}

void main() {
  int n = 100;
  int s = sumOfSquares(n);
  int s1 = sumOfn(n);
  int s2 = s1*s1;
  int res = s2 - s;
  print("Sum of Squares of first $n natural numbers: $s");
  print("Square of Sum of first $n natural numbers: $s2");
  print("Result is $res");
}
