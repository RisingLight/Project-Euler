# Euler 30. Digit fifth powers

result=0
for i in range(2,1000000):
	sum=0
	for j in str(i):
		sum=sum+int(j)**5
	if sum==i:
		result+=i

print(result)