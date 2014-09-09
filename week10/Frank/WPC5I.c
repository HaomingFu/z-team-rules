/*
 * 
 basic of lcm and gcd
TIME: 0s MEM：2.2M 
STATUS: Accepted
DATE：May 15, 2014
From: http://www.spoj.com/problems/WPC5I/
__author__ = 'frankfu'
*/
#include <stdio.h>
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
LL gcd_nonre(LL a, LL b)
{
    LL tmp;
    while(b != 0){
        tmp = a;
        a = b;
        b = tmp%b;
    }
    return a;
}
LL lcm(LL a,LL b){return a/gcd_nonre(a,b)*b;}
int main(){
	int T, m, n, i, gcdv;//1 <= T <= 2000  1 <= m,n < 2^31
	LL lcmv, initial;
	freopen("WPC5I.txt", "r", stdin);
	fast_scani(&T);
	while(T--)
	{
		fast_scani(&m);
		fast_scani(&n);
		gcdv = gcd_nonre(m,n);
		lcmv = 1ll*m/gcdv*n;
		initial = lcmv/gcdv;
		for (i = 1; i <= gcdv; ++i)
		{
			if(lcm(m,initial*i)%n == 0 && lcm(n,initial*i)%m == 0)
				break;
		}
		printf("%lld\n", initial*i);
	}
	fclose(stdin);
	return 0;
}
