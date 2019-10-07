d1 = 0
d2 = 0
d3 = 0
d4 = 0
d5 = 0
numbers = []

while True:
    num = (d1**5) + (d2**5) + (d3**5) + (d4**5) + (d5**5)
    if str(num) == str(d1) + str(d2) + str(d3) + str(d4) + str(d5):
        number.append(num)
    d5 += 1
    if d5 >= 9:
        d5 = 0
        d4 += 1
        if d4 >= 9:
            d4 = 0
            d3 += 1
            if d3 >= 9:
                d3 = 0
                d2 += 1
                if d2 >= 9:
                    d2 = 0
                    d1 += 1
                    if d1 >= 9: break

