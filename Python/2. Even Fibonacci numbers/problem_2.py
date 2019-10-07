fibs = [0,1]
even_fibs = 0
for i in range(2,20000):
    fib = fibs[i-1]+fibs[i-2]
    if fib<4000000:
        fibs.append(fib)
        if fib %2 ==0:
            even_fibs+=fib
    else:
        break
print(even_fibs)
