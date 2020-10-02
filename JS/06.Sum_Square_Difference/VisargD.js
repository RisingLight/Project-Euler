/**
 * Euler 06 in Javascript
 */

function sum_of_squares() {
    var sum = 0;
    for (var i = 1; i <= 100; i++) {
      sum += (i ** 2);
    }
    return sum;
  }
  
  function square_of_sum() {
    var square;
    var sum = 0;
    for (var i = 1; i <= 100; i++) {
      sum += i;
    }
    square = sum ** 2;
    return square;
  }
  
  console.log(square_of_sum() - sum_of_squares());