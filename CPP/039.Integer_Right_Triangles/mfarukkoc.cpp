/*
Euler Problem 39
Integer Right Triangles:
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?
*/
#include <iostream>
#include <string>
using namespace std;
int countSolutions(int p) 
{
    int count = 0;
    for (int a = 1; a <= p; a++) {
      for (int b = a; b <= p; b++) {
        int c = p - a - b;
        if (b <= c && a * a + b * b == c * c)    //Condition to check if the triangle satisifies the pythagoras formula
          count++;
      }
    }
      return count;
} 
string run() 
{
    int maxPerimeter = 0;                     //Initial default values
    int maxTriangles = 0;                     // Set to 0 so that it get overwritten by any value grt 0
    
    for (int p = 1; p <= 1000; p++) {         //Bruteforce from 1 to 1000
      int triangles = countSolutions(p);
      if (triangles > maxTriangles) {          //If the number of solutions found are more than the current max than replacement occurs
        maxTriangles = triangles;
        maxPerimeter = p;
      }
    }
    return to_string(maxPerimeter);
  }   
    
int main()
{
   cout<<run();
   return 0;
}
