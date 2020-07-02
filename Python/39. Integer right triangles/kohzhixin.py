"""
Problem 39
"""

def solution(max_p):
    max_num = 0
    for p in range(0, max_p, 2):
        c = 0
        for a in range(2, int(p/3)):
            if (p**2 - 2*p*a) % (2 * (p-a)) == 0:
                c += 1
        if c > max_num:
            max_num = c
    return max_num

print(solution(1000))