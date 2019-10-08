#include <stdio.h>

int
main ()
{
	int sum;
	int a;
	int b;
	int tmp;

	a = 1;
	b = 2;
	sum = 0;
	while (b < 4000000) {
		if (b % 2 == 0)
			sum += b;
		tmp = a + b;
		a = b;
		b = tmp;
	}

	printf("%d\n", sum);
}
