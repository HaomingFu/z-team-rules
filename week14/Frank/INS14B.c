/*
list all factors of N*N, and remove those who ((N*N)/factor%2 == 1).
TIME: 0.09s MEM：1.9M 
STATUS: Accepted
DATE：June 18, 2014
From: http://www.spoj.com/problems/INS14B/
__author__ = 'frankfu'
*/
#include <stdio.h>

inline void fast_scani(int *a)
{
    register char c=0;
    while (c<33) c=getchar_unlocked();
    *a=0;
    while (c>33)
    {
        *a=(*a<<3)+(*a<<1)+(c&15);
        c=getchar_unlocked();
    }
}
int main()
{
	int T,N, ret, i, n; //1<=T<=1000 1<=N<=1000
	fast_scani(&T);
	while(T--)
	{
		fast_scani(&N);
		n = N*N;
		ret = 0;
		for (i = 1; i <= N; ++i)
		{
			if(n%i == 0)
			{
				if(((n/i)&1) == 0) 
					ret++;
				if(i != N)
				{
					if((i&1) == 0) 
						ret++;
				}
			}
		}
		printf("%d\n", ret);
	}
	return 0;
}
