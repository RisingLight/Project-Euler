#Euler 14
#Problem Name - Longest Collatz Sequence

def get_len_of_chain(start_number):
    length = 1
    n = start_number
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n+1
        length+=1
    return length

max, max_collatz = 0,0
for n in range(1,1000000):
    length = get_len_of_chain(n)
    if length > max:
        max = length
        max_collatz = n
print(f"Starting Number of Longest Collatz Sequence: {max_collatz}")
print(f"Length of Longest Collatz Sequence: {max}")
