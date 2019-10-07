'''
1000-digit Fibonacci number
Problem 25

'''

i = 0
first_number = 0
second_number = 1

while True:
    if i % 2 == 0:
        first_number += second_number
    elif i % 2 == 1:
        second_number += first_number
    i += 1
    if len(str(first_number)) == 1000 or len(str(second_number)) == 1000: break
print(i)
