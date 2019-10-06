'''
Project Euler Challenge 05. Smallest multiple
Problem Statement: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

'''
Note: I optimised the brute force code as much as I could.
If anyone could optimise it further, feel free. I figured an alternate methord by factorization with
lower time complexity. Make sure you have a look at that too (if not available in this repository 
check online.)
''' 

#Methord Used : Brute Force
#Time Complexity : ~61 ms

#Alternate methord: Factorization Algorithm

from datetime import datetime            #Importing datetime for calculating time complexity

def smallest():             #Returns the smallest +ve number that is evenly divisible to all the numbers between 1 to 20
    start_time = datetime.now()
    num = 20
    #check = [20, 19, 18, 17, 16, 14, 13, 11]
    check = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    while True:
        for i in range (0, len(check)):
            if(num%check[i] !=0):
                num+=20
                break
        if i==(len(check)-1):
            print(num)
            print("TOTAL TIME: ", datetime.now()-start_time,)
            break
    
smallest()  #Calling the function to get results