#Euler 24
from itertools import permutations

def lexicographical_permutation(str):
    permutation = sorted(''.join(chars) for chars in permutations(str))
    for x in permutation:
        print(x)

str = 'abc'
lexicographical_permutation(str)