import numpy as np
nums = list(range(1,21))
#Pure brute-force method
for numerator in range(20,10000000000):
    remainders = []
    for denominator in nums:
        if numerator%denominator == 0:
            remainders.append(numerator%denominator)
        else:
            remainders.append(numerator%denominator)
            break;
    if np.sum(remainders) == 0:
        print("{} is the smallest divider".format(numerator))
        break;
