import math
import itertools


def is_prime(n: int) -> bool:
    if n % 2 == 0 and n > 2:
        return False
    return all(n % j for j in range(3, int(math.sqrt(n)) + 1, 2))


if __name__ == "__main__":
    result = 0
    for i in list(itertools.permutations('1234567')):
        permutation_number = int("".join(i))
        if is_prime(permutation_number):
            if result < permutation_number:
                result = permutation_number
    print(result)
