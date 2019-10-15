'''
Author:  ankitRai96
Problem: find the value of the first triangle number to
         have over five hundred divisors
''' 
def divisorCount(n):
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            count = count + 1
    return count

def triangularNumber(n):
    tn = 0
    for i in range(1,n+1):
        tn = tn + i
    return tn

if __name__ == '__main__':
    counter = 1
    while True:
        tn = triangularNumber(counter)
        res = divisorCount(tn)
        counter = counter + 1
        if res > 500:
            print(tn)