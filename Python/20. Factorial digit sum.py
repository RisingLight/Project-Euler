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

