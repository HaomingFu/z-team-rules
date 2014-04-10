#include <stdio.h>
#include <stdlib.h>
/*
Using sliding window alg 
Helped by .::Lakshman::. mainly by changing scanf into an inline scan function
TIME: 0.22s MEM：6.6M 
STATUS:Accepted
DATE：April 11, 2014
From: http://www.spoj.com/submit/ALIEN/
__author__ = 'frankfu'
*/
//fast I/O
inline int scan()
{
	int z=0;
	char c;
	do{ c=getchar_unlocked(); } while(c<'0');
	for(;c>='0';c=getchar_unlocked()) z = (z<<3) + (z<<1) + (c&15);
	return z;
}
int main()
{
	int t = 0,At = 0,Bt = 0,i = 0;
	int nstations = 0,npeople = 0,front = 0,back = -1,nptmp = 0;
	int finished = 0;
	int *A;
	t = scan();
	while(t)
	{
		At=scan();Bt=scan();
		i = 0;
		A = (int *)malloc(At*sizeof(int));
		while(i < At)
		{
			A[i++]=scan();
		}
		nstations = 0;npeople = 0;front = 0;back = -1;nptmp = A[0];finished = 0;
		while(finished == 0)
		{
			if(nptmp <= Bt && (front-back > nstations || (front-back == nstations && nptmp <= npeople)))
			{
				nstations = front-back;
				npeople = nptmp;
			}
			if(finished) break;
			if(nptmp <= Bt)
			{
				front += 1;
				if(front <= At-1)
					nptmp += A[front];
				else
				{
					front -= 1;
					finished = 1;
				}
			}
			else
			{
				back += 1;
				nptmp -= A[back];
			}
		}
		printf("%d %d\n", npeople, nstations);
		t--;
	}
	return 0;
}
