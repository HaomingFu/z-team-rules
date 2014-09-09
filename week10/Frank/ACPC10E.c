/*
 * 
 pay attention to overflow
TIME: 0s MEM：1.6M 
STATUS: Accepted
DATE：May 14, 2014
From: http://www.spoj.com/problems/ACPC10E/
__author__ = 'frankfu'
*/
#include <stdio.h>
#include <math.h>
#define LL long long

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

int main(){
	int G, A, T, D; // G > 0  (0 < A ≤ T)   four numbers in the input are no larger than 216
	LL X, Y, tmp, expo, tt;
	//~ freopen("ACPC10E.txt", "r", stdin);
	while(1){
		scanf("%d", &G);
		if(G < 0) break;
		fast_scani(&T); 
		fast_scani(&A);
		fast_scani(&D);
		X = 1ll*T*(T-1)/2*G;
		Y = 0;
		tmp = 1ll*A*G + D;
		if(tmp & (tmp-1)){
			expo =  ceil(log2(tmp));
			tt = (LL)(1ll<<expo);
			Y = tt - tmp;
			tmp = tt;
		}
		X += tmp-1;
		printf("%d*%d/%d+%d=%lld+%lld\n", G, A, T, D, X, Y);
	}
	//~ fclose(stdin);
	return 0;
}
