"""
Problem 24 - Lexicographic permutations
"""

from itertools import permutations


def get_xth_permutation(digits:list, x:int) -> int:
    sorted_perms = sorted(permutations(digits))
    str_number = ''.join(str(i) for i in sorted_perms[x-1])
    return int(str_number)


digits = [i for i in range(10)]
result = get_xth_permutation(digits, 1000000)
print(result)
