# Project Euler : Problem Number 28
# The Fibonacci sequence is defined by the recurrence relation:
#    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

#Hence the first 12 terms will be:
#    F1 = 1
#    F2 = 1
#    F3 = 2
#    F4 = 3
#    F5 = 5
#    F6 = 8
#    F7 = 13
#    F8 = 21
#    F9 = 34
#    F10 = 55
#    F11 = 89
#    F12 = 144

#The 12th term, F12, is the first term to contain three digits.
#What is the index of the first term in the Fibonacci
#sequence to contain 1000 digits?

def digit(n):
    count=0
    while(n>0):
        count=count+1
        n=n//10
    return count

t1 = 1
t2 = 1
nextTerm = 0
i = 2;
while(digit(nextTerm)<1000):
    nextTerm = t1 + t2
    t1 = t2
    t2 = nextTerm
    i=i+1
    
print(i)


