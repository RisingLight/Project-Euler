'''
	Project Euler Question 20. Factorial digit sum
	Problem Statement: 
	n! means n × (n − 1) × ... × 3 × 2 × 1

	For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
	and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

	Find the sum of the digits in the number 100!	
'''
import math

def factorial_digit_sum(factorial_n):
	result = 0
	for n in str(factorial_n):
		result += int(n)	
	
	return result

if __name__ == "__main__":
	n = 100
	factorial_of_n = math.factorial(n)
	factorial_sum = factorial_digit_sum(factorial_of_n)
	print(factorial_sum)

