'''
Project Euler Challenger 4. Largest palindrome product
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_pallindrome(n):

    s = str(n)
    for n in range(1, int(len(s)/2) + 1):

        if s[n-1] != s[-n]:
            return False

    return True


largest = 0

for j in range(100, 1000):
    for k in range(j, 1000):

        if is_pallindrome(j*k):

            if (j*k) > largest: largest = j*k

print (largest)