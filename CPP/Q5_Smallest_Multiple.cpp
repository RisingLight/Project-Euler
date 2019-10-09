#include<iostream>

using namespace std;

long long lcm(long long,long long);
long long hcf(long long,long long);

long long lcm(long long x,long long y){

         long lcm;
         lcm=(x*y)/hcf(x,y);

         return lcm;
}


long long hcf(long long x,long long y){

         while(x!=y){
            if(x>y){    x=x-y;      }
            else { y=y-x;}  }
        return x;

        }





int main(){

long a=1;

for(long i=11;i<=20;i++){
        a=lcm(a,i);


}

cout<<"LCM "<<a;

return 0;
}
