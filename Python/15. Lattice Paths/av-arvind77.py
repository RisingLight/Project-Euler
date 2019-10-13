# Euler Problem 15 

#LATTIC PATHS


from math import factorial

#import time from time to calculate exection time
from time import time

#time at the start of execution
start = time()

#binomial coefficient function
#https://en.wikipedia.org/wiki/Binomial_coefficient
def nck(n,k):
	#function which will return the binomial coefficient
	#of n,k
	return factorial(n)/(factorial(k)*factorial(n-k))

#Number of lattice paths from (0,0) to (a,b) is given by
#binomial coefficient C(a+b,a)
print 'Number of lattice paths is: '+str(nck(20+20,20))

#time at the end of program execution
end = time()

#Printing the total time
print end-start