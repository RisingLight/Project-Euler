function summationOfPrimes() {
  let num = 2000000;
  let result = 0;

  for (let i = 2; i <= num; i++) {
    if (isPrime(i)) result += i;
  }

  alert(result);
}

function isPrime(number) {
  let result = true;

  for (let i = 2; i <= Math.floor(Math.sqrt(number)); i++) {
    if (number % i == 0) {
      result = false;
      break;
    }
  }
  return result;
}

summationOfPrimes();
