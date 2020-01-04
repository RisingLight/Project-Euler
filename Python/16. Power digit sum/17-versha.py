  
def getSum(n): 
  
    sum = 0

    while(n > 0): 
        sum += int(n%10) 
        n = int(n/10) 
  
    return sum
  

print(getSum(2**1000)) 
