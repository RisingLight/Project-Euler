import math  
num = 0  
primeList = []

def isprime(test):
    if test == 2:  
        primeList.append(2)  
        return True  
    elif test < 2:  
        return False  
    else:  
        for i in primeList:  
            if i > math.sqrt(test):
                break
            elif test % i == 0:
                return False
        primeList.append(test)
        return True

def rotations(n):
    answer = []
    rotation = n
    while not rotation in answer:
        answer.append(rotation)
        rotation = int(str(rotation)[1:] + str(rotation)[0])
    return answer

for i in range(2,1000000):
    numList = rotations(i)
    valid = True
    for j in numList:
        if not isprime(j):
            valid = False
    if valid:
        num += 1

    print(num)