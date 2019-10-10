# Euler 28. Number spiral diagonals

n=1001
capas=int((n-1)/2) 

suma=1

start=1
for i in range(1,capas+1):
	for j in range(1,5):
		corner=start+2*i*j
		suma=suma+corner
	start=corner

print(suma)