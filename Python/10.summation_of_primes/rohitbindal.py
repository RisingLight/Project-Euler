import math
n = 2000000


def isprime(val):
    i = 2
    while i <= int(math.sqrt(val)):
        if val % i == 0:
            # print("NP", val)
            return 0
        i += 1
    return 1


def main():
    sum_ = 2
    for i in range(3, n):
        if isprime(i):
            sum_ += i
    print(sum_)


if __name__ == "__main__":
    main()
