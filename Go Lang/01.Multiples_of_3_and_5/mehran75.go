package main

func main() {

	maxNumber := 1000

	sum := 0
	for i := 0; i < maxNumber; i++ {
		if i%3 == 0 || i%5 == 0 {
			sum += i
		}
	}

	println(sum)

}
