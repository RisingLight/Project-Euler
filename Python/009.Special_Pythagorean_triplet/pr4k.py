'''
Project Euler : Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''
# Method Used ~ Brute Force

# time ~ 0.22s user 0.02s system 99% cpu 0.233 total

# Alternate method ~ To be found

for a in range(1,1001):#iterating a for 1-1000
    for b in range(1,1001): # iterating b for 1-1000
        c=1000-a-b  # finding c from condition a+b+c=1000
        if a<b<c and (a**2 + b**2 == c**2):  #checking for pythagorean tripet
            print("Product is ",a*b*c," for triplet {},{},{}".format(a,b,c))
            break