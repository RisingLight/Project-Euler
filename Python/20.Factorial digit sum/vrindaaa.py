#Euler Problem 20 done in python3
n = 100
k = 1
while(n>1):
	k *= n
	n -= 1
s = 0
while(k>0):
	s += k%10
	k = k//10
print(s)