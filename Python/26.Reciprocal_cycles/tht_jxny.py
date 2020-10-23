# Euler 26
def recurring_cycle(n, d):
    # n is numerator and d is denominator
    for t in range(1, d):
        if 1 == 10**t % d:
            return t
    return 0

if __name__ == "__main__":
    longest = max(recurring_cycle(1, i) for i in range(2,1001))
    print([i for i in range(1,1001) if recurring_cycle(1, i) == longest][0])
