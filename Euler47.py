#!/usr/bin/env python
# coding: utf-8

# In[27]:


def prime_no_collector(prime, n):
    if n == 1:                       #checking whether n == 1, not appending if it is equal as 1 is not a prime number 
        return prime
    for i in range(2, int(n**0.5)+1): #Running loop from 2 to sq_root(n) to check whether the number is prime or not
        if n%i == 0:                 #checking whether the numbe ris divisble or not (if divisible then it isn't a prime)
            return prime             #if not prime then returning the array without appending
    return prime.append(n)
        


# In[33]:


'''

#Testing the prime_no_collector function
prime = []
for i in range(1,20):
    prime_no_collector(prime,i)
print(prime)
#Excpected Output: 2, 3, 5, 7, 11, 13, 17, 19
#Function Output: [2, 3, 5, 7, 11, 13, 17, 19]

'''


# In[34]:


def prime_factors(prime, n):
    factors = []
    for i in prime:
        if n%i == 0:
            factors.append(i)
    return factors


# In[38]:


'''

#Testing function prime_factors:
print(prime_factors(prime, 15))
print(prime_factors(prime, 17))
print(prime_factors(prime, 14))

#Expected Output: [3, 5]    [17]    [2, 7]
#Function Output: [3, 5]
#                 [17]
#                 [2, 7]

'''


# In[45]:


def main():
    prime = []
    answer = 0
    for i in range(1,1000000):              #looping till 1,000,000
        prime_no_collector(prime,i)         #collecting all prime numbers as we iterate
        if len(prime_factors(prime, i)) == 4 and len(prime_factors(prime, i+1)) == 4 and len(prime_factors(prime, i+2)) == 4 and len(prime_factors(prime, i+3)) == 4:
            return i
print(main())


# In[ ]:




