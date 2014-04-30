/*
 * sigma(lcm(i,n)) = sigma(d*φ(d)/2)*n   (n|d)
 * use sieve method to get φ(n)  
 * use formula to get sigma(lcm(i,n)), use number theory basics
 * 
TIME: 3.13s MEM：17M 
STATUS: Accepted
Refer to:http://blog.csdn.net/acm_cxlove/article/details/11827227 
* http://www.cppblog.com/AmazingCaddy/archive/2010/08/07/122534.aspx
* http://oibh.info/archives/423
* http://cleverspace.ucoz.net/blog/spoj_lcmsum/2013-11-25-83
DATE：April 30, 2014
From: http://www.spoj.com/problems/LCMSUM/
__author__ = 'frankfu'
*/
#include <stdio.h>
#include <stdlib.h>
#define N  1000005
#define LL long long
int t, n, i, j, k;
LL phi[N] , ans[N];
inline int scani()
{
	int z = 0;
	char c;
	do{
		c = getchar_unlocked();
	}while(c < '0'); 
	for(;c >= '0';c = getchar_unlocked())
		z = (z << 3) + (z << 1) + (c & 15);
	return z;
}
void init () {
    ans[1] = 1LL;
    for (i = 2 ; i < N ; i ++) {
		if (i != 2){
			j = i - 1;
			ans[j] = (1LL * j * j * phi[j] >> 1) + j;// get part of ans[n] when divisor is n and 1
		}
        if (phi[i]) continue;  //get φ(n)
        for (j = i ; j < N ; j += i) {
            if (!phi[j]) phi[j] = j;
            phi[j] = phi[j] * 1LL / i * (i - 1);
        }
    }
    for (i = 2 ; i * i < N ; i ++) {   // get part of  ans[n] when divisor is between 2 and n-1
        ans[i * i] += 1LL * i * i * phi[i] * i >> 1;  // consider n = i*i boundary
        for (j = i * i + i , k = i + 1 ; j < N ; j += i , k ++) {
            ans[j] += (1LL * j * phi[i] * i >> 1) + (1LL * j * k * phi[k] >> 1);
        }
    }
}
int main () {
    init ();
    t = scani();
    while (t --) {
        n = scani();
        printf("%lld\n", ans[n]);
    }
    return 0;
}
