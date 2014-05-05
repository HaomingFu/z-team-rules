#include<stdio.h>

int main()
{
	int n;
	int A[30];
	scanf("%d",&n);
	A[0]=1;
	A[1]=3;
	for(int i=2; i<=n; i++)
	{
		A[i]=A[i-1]+A[i-2]+A[i-1];
	}
	printf("%d\n",A[n]);
	return 0;
}
