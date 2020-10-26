from numpy import *

filename = 'euler11.txt'

with open(filename, "r") as ins:
    array = []
    for line in ins:
        array.append(line)
print(array)
newArray = []
for i in array:
    j = i.split(' ')
    k = [int(n) for n in j]
    newArray.append(k)
print(newArray)

problemMatrix = matrix(newArray)
print(problemMatrix)

maxProd = 1

for i in range(16):
    for j in range(16):
        prod1 = problemMatrix[i,j]*problemMatrix[i+1,j]*problemMatrix[i+2,j]*problemMatrix[i+3,j]
        if prod1 > maxProd:
            maxProd = prod1
        prod2 = problemMatrix[i,j]*problemMatrix[i,j+1]*problemMatrix[i,j+2]*problemMatrix[i,j+3]
        if prod2 > maxProd:
            maxProd = prod2
        prod3 = problemMatrix[i,j]*problemMatrix[i+1,j+1]*problemMatrix[i+2,j+2]*problemMatrix[i+3,j+3]
        if prod3 > maxProd:
            maxProd = prod3
        prod4 = problemMatrix[19-i,j]*problemMatrix[18-i,j+1]*problemMatrix[17-i,j+2]*problemMatrix[16-i,j+3]
        if prod4 > maxProd:
            maxProd = prod4
print(maxProd)