//Euler 10
import'dart:math';

void main() {
  
  int summ = 0;
  for (int i = 2; i <= 2000001; i++) {
    if(is_Prime(i)){
  
      summ += i;
      
    }
    
  }print(summ);
}

bool is_Prime(int x){
  final lower = sqrt(x).floor();
  var div_f = 0;
  for (var div =1 ;div<=lower;div++){
    if(x % div ==0){
      div_f += 1;
    }
    if(div_f>1){
      return false;
    }
  }
  return true;
  
}
