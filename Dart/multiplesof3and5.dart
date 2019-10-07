int sum=0;
void main(){
  for(int i=0;i<1000;i++){
    if(i%3==0 || i%5==0) {
      print(i);
      sum = sum+i;
      
    }
  }
print("Sum of all numbers that are mulitples of 3 or 5 less than 1000:");
print(sum);
}
