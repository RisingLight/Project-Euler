#Euler Problem_40

def getDigit(n):
    s = 0
    k = 0
    while s < n:
        r = s
        s += 9 * (10 ** k) * (k+1)
        k += 1
    h = n - r - 1
    t = 10 ** (k-1) + (h / k)
    pos = h % k
    return str(t)[pos]

res = 1

for i in range(7):
    res *= int(getDigit(10**i))



print(res)

