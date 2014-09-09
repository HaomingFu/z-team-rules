/*
Using matrix exponentiation to calculate Fib(n) without mod will get
a number bigger than range of long long, and the process of calculate pow(2, Fib(n))
costs too much time. 0<=n<=1000000, but Fib(1000000) return overflow(bigger than long long)

finally realize (G[i-2]*G[i-1])%MOD=G[i], it is a trick

Refer to:  discussion in forum 
TIME: 0.14s MEM：9.2M 
STATUS:Accepted
DATE：April 15, 2014
From: http://www.spoj.com/problems/OPC3A/
__author__ = 'frankfu'
*/
#include <stdio.h>
#define MOD		1000000007
#define ll		long long
inline int scan()
{
	int z=0;
	char c;
	do{ c=getchar_unlocked(); } while(c<'0');
	for(;c>='0';c=getchar_unlocked()) z = (z<<3) + (z<<1) + (c&15);
	return z;
}
int main(){
	int t=scan(),i;
	ll G[1000001];
	G[0] = 1;
	G[1] = 2;
	for(i=2; i<1000001; i++)
		G[i] = (G[i-1]*G[i-2])%MOD;
	while(t--){
		i=scan();
		printf("%lld\n", G[i]);
	}
	return 0;
}
