'''
Project Euler Challenge 06. Sum square difference in Python
Problem Statement: Find the sum square difference of first hundred natural numbers
'''

def sum_sq_dif():                     # A function that will return the sum_square_difference of first 100 nautral numbers 
    
    sum_of_sq = 0                     # Initialising this variable to store the sum of squares
    sq_of_sum = 0                     # Initialising this variable to store the square of sums
    
    for i in range(1, 101):           # A loop to get the first 100 natural numbers (numbers gets stored in 'i')
        
        sum_of_sq += i*i              # Adding the square of 'i' to the get the sum of squares
        sq_of_sum += i                # Adding 'i' to the get the sum of the numbers
        
    sq_of_sum *= sq_of_sum            # Squaring the sum of numbers to get the square of sum (after loop ends)
    
    return sq_of_sum - sum_of_sq      # returning the difference between the square of sums and sums of square


print(sum_sq_dif())                   # Calling the function to check output