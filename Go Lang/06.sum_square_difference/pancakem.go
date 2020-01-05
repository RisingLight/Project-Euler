// Problem 6
// The sum of the squares of the first ten natural numbers is,
//
//	12 + 22 + ... + 102 = 385
// The square of the sum of the first ten natural numbers is,

//	(1 + 2 + ... + 10)2 = 552 = 3025
// Hence the difference between the sum of the squares of
// the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

// Find the difference between the sum of the squares of
// the first one hundred natural numbers and the square of the sum.

package main

import "fmt"

func generateXNo(x int) []int {
	numbers := make([]int, 0)
	for i := 1; i < x+1; i++ {
		numbers = append(numbers, i)
	}
	return numbers
}

func sumOfSquareFirstXNo(number int) int {
	numbers := generateXNo(number)
	sum := 0
	for _, element := range numbers {
		sum += element * element
	}
	return sum
}

func squareOfSumOfFirstXNo(number int) int {
	numbers := generateXNo(number)
	sum := 0
	for _, element := range numbers {
		sum += element
	}
	return sum * sum
}

func main() {
	fmt.Println(squareOfSumOfFirstXNo(100) - sumOfSquareFirstXNo(100))
}
