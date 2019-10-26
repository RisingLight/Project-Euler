# Euler Problem 16 done in Python3
x = pow(2, 1000)
s = 0
while(x>0):
	s+=x%10
	x=x//10
print(s)