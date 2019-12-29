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
