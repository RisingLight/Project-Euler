coins = [1, 2, 5, 10, 20, 50, 100, 200]

def solution(amt):
    ans = [0] * (amt + 1)
    ans[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], amt + 1):
            ans[j] += ans[j - coins[i]]
    return ans[-1]

print(solution(200))