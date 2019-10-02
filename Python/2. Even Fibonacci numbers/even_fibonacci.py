'''
Project Euler Challenge 02. Even Fibonacci numbers
Problem Statement: Find the sum of even numbers in fibonacci series which is less than 40000000
'''

def fibo_sum():             #The function that returns the sum
    
    temp = 0                #Variable that helps in swapping the current number into the previous number variable
    pre = 1                 #Variable that store the previous value of the fibonacci series
    even_sum = 0            #Variable that store the sum
    i=0                     #Variable that itterates to generate new elements in the series
    
    while i <= 4000000:     #Loop to generate new numbers starts 
        
        if i<=1:            #Handelling cases when the series has the elements 0 and 1
            i+=1            #Incrementing the values of 'i' by 1 and no swapping of 'prev' with 'i'
            
        else:               #If the number is greater that 1
            temp = i        #Storing 'i' to 'temp' for swapping
            i += pre        #creating new fibonacci element
            pre = temp      #Updating the 'pre' with the value stored in 'temp' i.e last value if 'i' before creating of new fibonacci element
            
        if i%2==0:          #Checking if the element is even or not
            even_sum += i   #If yes then add it to the sum
    
    return even_sum         #Return the sum value
        
print(fibo_sum())           #Testing the output