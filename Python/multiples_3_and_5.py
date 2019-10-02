def sum():
    summ=0
    for i in range(1000):
        if i%3 ==0  or i%5==0:
            summ+=i
    return summ

if __name__ == "__main__":
	print(sum())
