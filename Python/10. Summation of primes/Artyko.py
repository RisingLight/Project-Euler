import math


def is_prime(n: int) -> bool:
    if n % 2 == 0 and n > 2:
        return False
    return all(n % j for j in range(3, int(math.sqrt(n)) + 1, 2))


if __name__ == "__main__":
    results = 0
    for i in range(2000000):
        if is_prime(i):
            results += i
    print(results)
