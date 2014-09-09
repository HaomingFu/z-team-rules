#include <stdio.h>
#define MOD 1000000007
#define LL long long 
/*
Using matrix exponentiation, implement it with while loop rather than recursive function call
Refer to: http://fulmicoton.com/posts/fibonacci/   http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html#exact 
http://nayuki.eigenstate.org/page/fast-fibonacci-algorithms
TIME: 0.05s MEM：1.6M 
STATUS:Accepted
DATE：April 8, 2014
From: http://www.spoj.com/submit/FIBOSUM/
__author__ = 'frankfu'
*/
LL fib_matrix(int n)
{
	int i=0,j=0,k=0;
	LL fib[2][2]={{1,1},{1,0}}, ans[2][2]={{1,0},{0,1}}, temp[2][2]={{0,0},{0,0}};
	while(n)
	{
		if(n&1)
		{
			for(i=0;i<2;i++)
				for(j=0;j<2;j++)
					temp[i][j]=0;
			for(i=0;i<2;i++) 
				for(j=0;j<2;j++)
					for(k=0;k<2;k++)
						temp[i][j]=(temp[i][j]+ans[i][k]*fib[k][j])%MOD;
			for(i=0;i<2;i++) 
				for(j=0;j<2;j++) 
					ans[i][j]=temp[i][j];
		}
		n = n >> 1;
		if(!n) 
			break;
		for(i=0;i<2;i++)
			for(j=0;j<2;j++)
				temp[i][j]=0;
		for(i=0;i<2;i++) 
			for(j=0;j<2;j++) 
				for(k=0;k<2;k++)
					temp[i][j]=(temp[i][j]+fib[i][k]*fib[k][j])%MOD;
		for(i=0;i<2;i++)
			for(j=0;j<2;j++) 
				fib[i][j]=temp[i][j];
	}
	return (ans[0][1])%MOD;
}

int main()
{
	int t=0,M=0,N=0;
	scanf("%d", &t);
	while(t)
	{
		scanf("%d %d", &N, &M);
		printf("%lld\n", (fib_matrix(M+2)-fib_matrix(N+1)+MOD)%MOD);
		t--;
	}
	return 0;
}

