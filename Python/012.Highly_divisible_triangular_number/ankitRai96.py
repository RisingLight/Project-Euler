'''
Author:  ankitRai96
Problem: find the value of the first triangle number to
         have over five hundred divisors
''' 
from math import sqrt

def divisorCount(n):
    count = 0
    for i in range(1,int(sqrt(n))+1):
        if n%i == 0:
            if n/i == i:
                count = count + 1
            else:
                count = count + 2
    return count

if __name__ == '__main__':
    counter = 1
    while True:
        tn = (counter * (counter+1))//2
        res = divisorCount(tn)
        counter = counter + 1
        if res > 500:
            print(tn)
            break