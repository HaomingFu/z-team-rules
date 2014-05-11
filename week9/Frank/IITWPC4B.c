/*
 * find a formula(referring other's idea, but improve the speed) to calculate the number of triangles
TIME: 0.02s MEM：2.2M 
STATUS: Accepted
DATE：May 10, 2014
From: http://www.spoj.com/problems/IITWPC4B/
__author__ = 'frankfu'
*/
#include <stdio.h>
#include <math.h>
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
int main(){
	int t, n; //(1 <= T <= 10^5)   (n >= 1 && n <= 10^9)
	fast_scani(&t);
	while(t--){
		fast_scani(&n);
		if((n&1)){
			// faster than 	printf("%.Lf\n", roundl(1.0l*(n+3)*(n+3)/48.0));
			printf("%lld\n", (unsigned long long)roundl(1.0l*(n+3)*(n+3)/48.0));
		}
		else{
			printf("%lld\n", (unsigned long long)roundl(1.0l*n*n/48.0));			
		}
	}
	return 0;
}
