//Euler 50.Consecutive_prime_sum in Go
package  main

import "fmt"

const limit int = 1000000

func is_prime(x int) (res bool) {
	y := 5

	if x <= 3 {
		return true
	} else if (x % 2) == 0 || (x % 3) == 0 {
		return false
	}
	for (y * y) <= x {
		if (x % y) == 0 || (x % (y + 2)) == 0 {
			return false
		}
		y += 6;
	}
	return true
}

func solver() (res int, diff int) {
	prime_tab := []int{}

	for x := 2; x < limit; x++ {
		if (is_prime(x)) {
			prime_tab = append(prime_tab, x)
		}
	}
	
	sum_tab := []int{0}

	for x := 0; sum_tab[x] < limit; x++ {
		sum_tab = append(sum_tab, sum_tab[x] + prime_tab[x])
	}
	
	res = 0
	diff = 0
	temp_res := 0
	temp_diff := 0
	for x := len(sum_tab) - 1; x > 0; x-- {
		for y := 0; y < len(sum_tab); y++ {
			temp_res = sum_tab[x] - sum_tab[y]
			temp_diff = x - y
			if temp_res > limit {
				break;
			}
			if is_prime(temp_res) && temp_diff > diff {
				res = temp_res
				diff = temp_diff
			}
		}
	} 

	return
}

func main() {
	x, y := solver()
	fmt.Printf("The biggest sum of consecutive primes is %d\nWith %d consecutive primes.", x, y)
}
