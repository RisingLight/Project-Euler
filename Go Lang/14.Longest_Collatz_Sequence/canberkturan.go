package main

import "fmt"

func get_len_of_chain(start_number int) int {
  length:=1
  n:=start_number
  for n!=1{
    if n % 2 == 0{
      n = n/2
    }else{
      n = 3*n + 1
    }
    length+=1
  }
  return length
}

func main(){
  max:=0
  max_collatz:=0

  for n:=1; n<1000000; n++{
    length := get_len_of_chain(n)
    if length > max{
      max = length
      max_collatz = n
    }
  }
  fmt.Println("Start Number of Longest Collatz Sequence:",max_collatz)
}
