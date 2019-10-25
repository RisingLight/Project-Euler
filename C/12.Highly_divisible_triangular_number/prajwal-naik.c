//Euler 12

#include<stdio.h>
#include<math.h>
int divisorCount(int );

int main()
{
	int counter=1;
	while(1)
	{
		int tn=((counter*(counter+1))/2);
		int res=divisorCount(tn);
		counter+=1;
		if(res>500)
		{
			printf("%d", tn);
			break;
		}
	}
}

int divisorCount(int n)
{
	int count =0;
	for(int i=1; i<=sqrt(n); i++)
	{
		if(n%i==0)
		{
			if(n/i==i)
				count+=1;
			else
				count+=2;
		}
	}
	return count;
}

