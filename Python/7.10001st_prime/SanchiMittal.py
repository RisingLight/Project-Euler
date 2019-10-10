'''
The 10001st prime number will be printed.

Algorithm used -> Sieve Of Eratosthenes
'''

m = 1000100
'''
This function looks for prime numbers between 1 and m 
and returns the n-th prime number. Here, n = 10001.
-1 is returned if n-th prime number is not found in 
the mentioned range.
'''
def SieveOfEratosthenes(n):
    A = [True for i in range(2,m)]
    A[0] = False
    A[1] = False
    counter = 0
    for i in range(2,len(A)):
        if A[i] == True:
            counter+=1
            for j in range(i*i, len(A), i):
                A[j] = False

        if counter == n:
            return i

    return -1

print(SieveOfEratosthenes(10001))