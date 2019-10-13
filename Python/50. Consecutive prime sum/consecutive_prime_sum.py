from datetime import datetime

start_time = datetime.now()

def is_prime(num):
    for j in range (2,int(num/2)+1):
        if(num%j==0):
            return False
    return True

def call():
    sum1=0
    max1=0
    count=0
    c=0
    for i in range(2,1000000):
        for j in range(i,1000000):
            if is_prime(j):
                  sum1+=j
                  c+=1
                  if is_prime(sum1) and sum1<1000000:
                    if c>count:
                        max1=sum1
                        count=c
                        #print(j," ")
                  if sum1>1000000:
                      break      
        sum1=0
        c=0                       
    print(max1)
    print(count)
    print("TOTAL TIME: ", datetime.now()-start_time)
    
call()