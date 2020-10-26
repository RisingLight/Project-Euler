# Euler Problem 25

def _fibo():
	a, b, i = 1, 1, 1
	while True:
		yield a, i
		a, b, i = b, a + b, i + 1


def main(n=1000):
	for f, i in _fibo():
		if len(str(f)) == n:
			break
	print(i)


if __name__ == '__main__':
	main()
