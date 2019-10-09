# Euler 29. Distinct powers

result=[]
for i in range(2,101):
	for j in range(2,101):
		result.append(i**j)
		
print(len(set(result)))