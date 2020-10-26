# Euler 02. Even Fibonacci numbers
Fibonacci<-c(0,1)
NewElement<-sum(tail(Fibonacci,2))

while(NewElement<4000000){
    Fibonacci<-c(Fibonacci,NewElement)
    NewElement<-sum(tail(Fibonacci,2))
}

print(sum(Fibonacci[Fibonacci%%2!=0]))