# Project Euler : Problem Number 28

# Starting with the number 1 and moving to the right in a
# clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001
# spiral formed in the same way?

lim=1002001
i=1
j=1
c=1
leftInc=0
Lsum=0
Rsum=0
while(i<lim):
    i=i+leftInc
    leftInc=2*c
    if(i<lim):
        Lsum=Lsum+i
    c=c+1
c=2
while(j<=lim):
    rigInc=2*c
    j=j+rigInc
    if(j<=lim):
        Rsum=Rsum+j
    j=j+rigInc
    if(j<=lim):
        Rsum=Rsum+j
    c=c+2
Tsum=Lsum+Rsum
print(Tsum)
