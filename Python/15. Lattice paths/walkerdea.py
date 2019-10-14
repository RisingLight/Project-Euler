#Euler problem_15

def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)

def paths(len):
    res = 1
    for i in range(len):
        res *= (2 * len) - i
        res /= i + 1
    return int(res)

print(paths(20))
