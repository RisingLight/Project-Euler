/*
    Project Euler Question 20. Factorial digit sum
    
	Problem Statement: 
    
	n! means n × (n − 1) × ... × 3 × 2 × 1
	For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
        and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
    
	Find the sum of the digits in the number 100!
 */

import java.math.BigInteger

fun factorial(n: BigInteger): BigInteger {
    return when (n) {
        BigInteger.ONE, BigInteger.ZERO -> BigInteger.ONE
        else -> n.multiply(factorial(n.minus(BigInteger.ONE)))
    }
}

fun main() {
    var sum = 0
    val factorialString = factorial(BigInteger("100")).toString()
    val len = factorialString.length
    for (i in 0..len-1) {
        sum = sum + factorialString.substring(i, i+1).toInt()
    }
    println(sum)
}
