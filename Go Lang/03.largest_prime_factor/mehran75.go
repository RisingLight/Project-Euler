package main

import "fmt"

func main() {
	num := 600851475143
	fmt.Println(sieveOfEratosthenes(num))
}

func sieveOfEratosthenes(N int) (prime int) {
	prime = 0
	for i := 2; i < N; i++ {
		if b[i] == true {
			continue
		}
		if i > prime {
			prime = i
		}
		for k := i * i; k < N; k += i {
			b[k] = true
		}
	}
	return
}
