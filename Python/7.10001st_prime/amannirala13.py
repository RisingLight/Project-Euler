'''
Project Euler Challenge 07. 10001st prime
Problem Statement: What is the 10 001st prime number?
'''
from datetime import datetime

#Check if the number is prime or not
def is_prime(number):
    c=0
    for i in range (1,number+1):
       if number%i==0:
           c+=1
    return c == 2

start_time = datetime.now()
count = 0
num = 0
while count != 10001:
    num+=1
    if is_prime(num):
        count +=1
print(num)
print("Time taken: ", datetime.now()-start_time) #Time taken to complete (~5min)