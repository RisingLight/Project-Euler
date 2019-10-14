#include <iostream>
#include <string>

using namespace std;
bool isPalindrome(string x){
    if (x.length() == 1){return true;}
    if (x.length() == 2){if (x[0] == x[1]) {return true;} return false;}
    if (x[0] == x[x.length()-1]){return isPalindrome(x.substr(1,x.length()-2));}
    return false;
}

bool isPalindromeHelper(int x){
    string numString = to_string(x);
    return isPalindrome(numString);
}
int main()
{
    int highestPalindrome = 0;
    int highesti = 0;
    int highestj = 0;
    for (int i = 999; i > 99; i--){
        for (int j = 999; j > 99; j--){
            if (isPalindromeHelper(i*j)){
                if (highestPalindrome < i*j){highestPalindrome=i*j; highesti=i; highestj=j;}
            }
        }
    }
    cout << endl << "The largest palindrome that is the product of two 3-digit numbers is: " << highestPalindrome << " (" << highesti << " x " << highestj << ")." << endl;
    return 0;
}
