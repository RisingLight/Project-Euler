'''
Project Euler Challenge 03. Largest prime factor
Problem Statement: What is the largest prime factor of the number 600851475143 ?
'''

def largest_fact():   #Function that returns the largest prime factor
    
    max_prime_fac = 0   #Variable that stores the largest prime factor
    thresh = number     #Variable that stores threshold for optimisation of the code with dealing with such large numbers
    
    for i in range(1,(number+1)):    #Loop to find the factors of the 'number'
        
        if(i>thresh):               #If the value of 'i' exceeds the 'thresh' value
            break                    #We stop because all the alternate factors have already been checked
        
        if is_factor(i) and is_prime(i):    #Checking if the value if 'i' is the factor of 'number' and is prime or not
            max_prime_fac = i               #If yes, assign 'i' value to 'max_prime_fac'
            thresh = number/i               #Change the 'thresh' to the alternate factor of 'number' to that of 'i'
                    
    return max_prime_fac                    #Return the largest prime factor value

def is_factor(i):     #Function that checks if the 'i' is a factor of 'number' or not 
    return number%i == 0      #Returns the value in boolean

def is_prime(i):     #Function that checks if 'i' is prome or not
    
    count = 0        #Counter variable for checking prime
    
    for j in range(1,i+1):   #Loop to check prime
        if(i%j==0):          #If found a multiple
           count+=1          #Increment the counter by 1
           
    return count ==2         #Check and return if the counter == 2 i.e number is prime or not

number=600851475143          #Variable thta contains the number according to the question
print("Calculating...")      #Message showing calculation in process
print(largest_fact())        #Displaying the result
print("END")                 #Disply end message