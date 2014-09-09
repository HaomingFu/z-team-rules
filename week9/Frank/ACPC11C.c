/*
 * 
O(n)
consider all possible cases, that means one of N corridors is not 
walked through and there may exists turn round if the corridor that not 
walked through is at index 0 or index N-1. record the smallest value
TIME: 0.08s MEM：1.9M 
STATUS: Accepted
DATE：May 12, 2014
From: http://www.spoj.com/problems/ACPC11C/
__author__ = 'frankfu'
*/
#include <stdio.h>
#define LL long long
#define SIZE 100000

inline void fast_scani(int *a)
{
    register char c=0;
    while (c<33) c=getchar_unlocked();
    *a=0;
    while (c>33)
    {
        *a=*a*10+c-'0';
        c=getchar_unlocked();
    }
}
inline void fast_scani(int *a)
{
    register char c=0;
    while (c<33) c=getchar_unlocked();
    *a=0;
    while (c>33)
    {
        *a=(*a<<3)+(*a<<1)+(c&15);
        // *a=*a*10+c-'0';
        c=getchar_unlocked();
    }
}
int main(){
	int t, N, i, sum, tmp, ret;  //(1 ≤ T ≤ 100)  2 ≤ N ≤ 100, 000
	int L[SIZE];
	//~ freopen("ACPC11C.txt", "r", stdin);
	fast_scani(&t);
	while(t--){
		fast_scani(&N);
		i = 0; sum = 0;		
		while(i < N){
			fast_scani(&L[i]);  //(1 ≤ Li ≤ 1,000,000)
			sum += L[i];
			i++;
		}
		tmp = ret = sum-L[0];
		for(i = 0; i < N-1; i++)
		{
			tmp += (L[i]<<1)-L[i+1];
			if(tmp < ret) ret = tmp;
		}
		tmp = sum-L[N-1];
		if(tmp < ret) ret = tmp;
		for(i = N-1; i >= 1; i--)
		{
			tmp += (L[i]<<1)-L[i-1];
			if(tmp < ret) ret = tmp;
		}
		printf("%d\n", ret);
	}
	//~ fclose(stdin);
	return 0;
}