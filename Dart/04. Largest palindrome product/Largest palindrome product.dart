//Euler 04


bool isPalindrome(String str) {
  String s = str.toLowerCase().replaceAll(RegExp(r'[\W_]'), '');
  return s == s.split('').reversed.join('');
}

void main() {
  int large = 0;
  var x;
  for (var i = 100; i < 1000; i++) {
    for (var j = i; j< 1000; j++){
      x = (i*j).toString();
              if (isPalindrome(x)){
                if(i*j > large){
                  large = i*j;
                }
                
              }

    }
    
  }
  print(large);
}