'''
Project Euler Challenger 16. Power digit sum
What is the sum of the digits of the number 2^1000?
'''

# Fast Exponentiation
def binPow(a, b):
    power = 1

    while b > 0:

        if b & 1:
            power = power * a

        a = a * a
        b >>= 1

    return power


power_digit = str(binPow(2, 1000))

sum = 0
for digit in power_digit:
    sum += int(digit)

print(sum)
