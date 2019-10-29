/*
    Project Euler Question 6. Sum square difference
    
	Problem Statement: 
    
    The sum of the squares of the first ten natural numbers is,

        1^2 + 2^2 + ... + 10^2 = 385
    
    The square of the sum of the first ten natural numbers is,

        (1 + 2 + ... + 10)^2 = 552 = 3025
    
    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum.
 */

fun Int.square() = this * this

fun sum(n: Int) = (n * (n + 1)) / 2

fun sumOfSquares(n: Int) = n * (n + 1) * (2 * n + 1) / 6

fun sumSquareDifference(n: Int) = sum(n).square() - sumOfSquares(n)

fun main(args: Array<String>) {
    println("Sum square difference of 100: " + sumSquareDifference(100))
}
