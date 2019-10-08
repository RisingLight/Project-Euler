#include<iostream>

using namespace std;
int main(){
    int c;
    for (int a=1;a<=1000;a++){
        for(int b=1;b<=1000;b++){
            c=1000-a-b;
            if (a<b && b<c && (a*a + b*b == c*c)){
                cout<<"Product of triplets "<<a<<","<<b<<","<<c<<" is "<<a*b*c<<endl;
                break;
            }
        }
    }
    return 0;
}