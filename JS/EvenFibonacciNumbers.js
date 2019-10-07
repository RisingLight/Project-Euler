/**
 * Each new term in the Fibonacci sequence is generated 
 * by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
 * 
 * 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
 * 
 * By considering the terms in the Fibonacci sequence 
 * whose values do not exceed four million, find the sum of the even-valued terms.
 */

function EvenFibonacciNumber (){
    evenFibs = new Array();
    
    lastFib = 0;
    i = 1;
    sumOfFibs = 0;
    while (true) {
        fibAux = calculateFib(i);
        i++;

        if (fibAux > 4000000) {
            break;
        }
        
        if (isEven(fibAux)) {
            lastFib = fibAux;
            evenFibs.push(fibAux);
            sumOfFibs += fibAux
        }
    }

    alert(sumOfFibs)
}

function calculateFib (n) {
    if (n <= 2) {
        return 1;
    } else {
        return calculateFib(n-1) + calculateFib(n-2)
    }
}

function isEven (number) {
    if (number % 2 == 0) {
        return true;
    } else {
        return false;
    }
}