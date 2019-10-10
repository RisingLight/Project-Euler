package main

func main() {

	fibs := fibonacci([]int{1, 2}, 1, 2, 2)

	sum := 0
	for _, item := range fibs {
		if item%2 == 0 {
			sum += item
		}
	}

	println(sum)

}

func fibonacci(fib []int, n1, n2, index int) []int {

	if fib[len(fib)-1] > 4000000 {
		return fib[:len(fib)-1]
	}

	fib = append(fib, fib[index-1]+fib[index-2])

	return fibonacci(fib, fib[index-1], fib[index-2], index+1)

}
