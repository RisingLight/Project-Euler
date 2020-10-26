// Problem 4
// A palindromic number reads the same both ways.
// The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

// Find the largest palindrome made from the product of two 3-digit numbers.

package main

import (
	"fmt"
	"strconv"
)

func reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func isPalindrome(number int) bool {
	strNumber := strconv.Itoa(number)
	reversedStrNumber := reverse(strNumber)

	return strNumber == reversedStrNumber
}

func main() {

	result := 0
	temp := 0

	for i := 999; i > 0; i-- {
		for j := 999; j > 0; j-- {
			temp = i * j
			// is palindrome and is larger than the previous result
			if isPalindrome(temp) && temp > result {
				result = temp
			}
		}
	}

	fmt.Println(result)
}
