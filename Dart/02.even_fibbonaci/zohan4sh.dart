/*
02. Even Fibonacci numbers
Find the sum of even numbers in fibonacci series which is less than 40000000
'''*/

int sum=0;   /*declaring variables*/
int i=0;
int max = 4000000; /*not exceeding 4 million*/
int temp=0;
int pre= 1;
int even_sum=0;
void main() {
while(i <= max){
  if (i<=1){
    i+=1;
  }  
  else{
    temp = i;
    i += pre;
    pre = temp;
  }
  if(i%2==0){
    even_sum +=i; /*if even adding*/
  }
}
  print(even_sum); /*printing sum value*/
}
