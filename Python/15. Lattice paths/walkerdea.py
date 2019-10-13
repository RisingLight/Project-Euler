#Euler problem_15

def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)

def paths(len, h):
    com = len + h
    res = fact(com) / (fact(len) + fact(h))
    return res

print(paths(20, 20))
