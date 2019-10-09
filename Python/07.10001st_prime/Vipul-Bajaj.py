# Euler 7
# Problem Name - 10001st_prime 
# Description - Print the 10001st Prime Number

# Maximum number upto which you can query.
MAX = 10000007 
# Function to return nth prime number if between 1 and MAX range, returns the nth prime number if 1 <= n  < MAX otherwise None
def return_nth_prime(n): 
    prime = [True for i in range(MAX+1)] 
    p = 2
    prime_till_now = 0
    found = False
    ans = None
    while (p  < MAX and not found): 
        if (prime[p] == True): 
            prime_till_now+=1
            if prime_till_now == n:
                ans = p
                found = True
            for i in range(p * p, MAX+1, p): 
                prime[i] = False
        p += 1
    return ans

if __name__ == "__main__":
    print(return_nth_prime(10001))  # Will print 10001st prime number
