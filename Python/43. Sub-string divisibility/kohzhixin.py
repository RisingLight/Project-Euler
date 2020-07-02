"""
Problem 43
"""

from itertools import permutations

div = [2, 3, 5, 7, 11, 13, 17]

def solution():
    total = 0
    for i in list(permutations([j for j in range(10)])):
        if check_num(i):
            total += int("".join([str(n) for n in i]))
    return total

def check_num(i):
    for j in range(len(div)):
        num = i[j+1] * 100 + i[j+2] * 10 + i[j+3]
        if num % div[j] != 0:
            return False
    return True       


print(solution())