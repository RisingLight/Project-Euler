#EULER PROLEM 12

from functools import reduce
n = 28
while True:
	triangle_number = n*(n+1)/2
	n = n+1
	dic = {}
	i = 2
	while i <= triangle_number:
		if triangle_number % i == 0:
			triangle_number = triangle_number/i
			if i in dic:
				dic[i] += 1
			else:
				dic[i] = 1
			i -= 1
		i += 1
	powers = [(x+1) for x in list(dic.values())]
	divisors = reduce(lambda x,y:x*y, powers)
	if divisors > 500:
		print((n-1)*(n)/2)
		break