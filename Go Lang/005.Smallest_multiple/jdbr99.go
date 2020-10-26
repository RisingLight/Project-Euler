// Euler 05. Smallest Multiple
// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

package main

import (
	"fmt"
)

func main() {
	// We set the number to find the multiples of
	num := 20
	// We set a flag to indicate when the number is found
	flag := true
	// We create an array of the numbers which we want to check if the number is multiple of
	check := [20]int{20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
	// We iterate until the flag is changed to `false`
	for flag {
		// We iterate checking if each number in the `check` array is multiple of `num`
		for i, n := range check {
			// If any number is not a multiple, then we change `num` to be the next multiple of the biggest number
			if num%n != 0 {
				num += check[0]
				break
			}
			// If every number was a multiple, then we raise the flag, since we've now found the number
			if i == len(check)-1 {
				flag = false
				break
			}
		}
	}
	// We print the found number
	fmt.Println(num)
}
