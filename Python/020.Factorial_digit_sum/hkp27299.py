def factorial(n):

    return 1 if (n==1 or n==0) else n * factorial(n - 1);

n = int(input("Enter number = "))

answer = factorial(n)
answer1 = list(map(int, str(answer)))
ans = 0
for i in answer1:
    ans += i
print(ans)
