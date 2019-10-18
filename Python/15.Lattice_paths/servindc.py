#  Solution to Euler problem 15
from math import factorial as f

def Lattice_paths(n):
    pascal_row = []
    for i in range(n+1):
        pascal_row.append( f(n)//(f(n-i)*f(i)) )
    return sum([i**2 for i in pascal_row])

k = Lattice_paths(20)

print(f"There are {k} routes through a 20×20 grid.")
