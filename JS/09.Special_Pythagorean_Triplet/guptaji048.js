/*
Euler 09 done in JavaScript
*/
var c;

for (var a = 1; a < 500; a++) {
  for (var b = a; b < 1000; b++) {
    c = Math.sqrt(a * a + b * b);
    if (c % 1 === 0 && a + b + c == 1000) {
      console.log("The triplets are", a, b, c);
      console.log("Product is", a * b * c);
    }
  }
}
