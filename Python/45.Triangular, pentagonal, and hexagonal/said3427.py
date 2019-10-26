# Euler 45. Triangular, pentagonal, and hexagonal
import math

def isPentagonal(x):
	result=(1+math.sqrt(24*x+1))/6
	return result.is_integer()

def isTriangle(x):
	result=(-1+math.sqrt(8*x+1))/2
	return result.is_integer()

def isHexagonal(x):
	result=(1+math.sqrt(8*x+1))/4
	return result.is_integer()

def Hexagonal(x):
	return x*(2*x-1)
	
i=0
n=1
while i<3:
	num=Hexagonal(n)
	if isTriangle(num) and isPentagonal(num):
		i+=1 
	n+=1

print(num)