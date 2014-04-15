/*
This probs has something to do with OPC3A.
Using matrix exponentiation to calculate Fib(n) without mod will get
a number bigger than range of long long, and the process of calculate pow(2, Fib(n))
costs too much time. 
Considering that, using eulerv totient function to help reduce Fib(n),  0<=n<=10^15.

finally realize (G[i-2]*G[i-1])%MOD=G[i], it is a trick
MOD=10^9+7
G[n] = (2^(Fib(n)%(MOD-1)))%MOD

Refer to:  discussion in forum
http://zh.wikipedia.org/wiki/%E6%AC%A7%E6%8B%89%E5%87%BD%E6%95%B0
http://zh.wikipedia.org/wiki/%E6%AC%A7%E6%8B%89%E5%AE%9A%E7%90%86_(%E6%95%B0%E8%AE%BA)
 
TIME: 0.14s MEM：9.2M 
STATUS:Accepted
DATE：April 15, 2014
From: http://www.spoj.com/problems/OPC3A/
__author__ = 'frankfu'
*/
#include <stdio.h>
#define ll		long long
#define MOD		1000000007
#define matrix		struct Matrix
matrix{ll a1,a2,a3,a4;};

inline int scani()
{
	int z=0;
	char c;
	do{ c=getchar_unlocked(); } while(c<'0');
	for(;c>='0';c=getchar_unlocked()) z = (z<<3) + (z<<1) + (c&15);
	return z;
}
inline ll scanll(){
	ll i=0;
	int minus=0;
	char c;
	for(c=getchar();(c<'0'||c>'9')&&(c!='-');
		      c=getchar());
	if(c=='-')
		      {minus=1;c='0';}
	for(i=0;c>='0'&&c<='9';c=getchar())
		      i=(i<<3)+(i<<1)+(c-48);
	if(minus)i=(~i)+1;
	return i;
}
matrix multiply(matrix t1,matrix t2){
	matrix tmp;
	tmp.a1=((t1.a1*t2.a1)+(t1.a2*t2.a3))%(MOD-1);
	tmp.a2=((t1.a1*t2.a2)+(t1.a2*t2.a4))%(MOD-1);
	tmp.a3=((t1.a3*t2.a1)+(t1.a4*t2.a3))%(MOD-1);
	tmp.a4=((t1.a3*t2.a2)+(t1.a4*t2.a4))%(MOD-1);
	
	return tmp;
}
matrix expo(matrix B,ll n){
	if(n==1){
		return B;
	}
	matrix C=expo(B,n/2);
	C=multiply(C,C);
	if(n%2==1){
		return multiply(B,C);
	}
	return C;
}
ll powder2N(ll n)
{
	if(n==1) return 2;
	ll tmp=powder2N(n/2);
	tmp=(tmp*tmp)%MOD;
	if(n%2==1) return (2*tmp)%MOD;
	return tmp;
}
int main(){
	int t=scani();
	matrix A;
	A.a1=1;	A.a2=1;
	A.a3=1; A.a4=0;
	while(t--){
		ll n=scanll();
		//scanf("%lld",&n);
		if(n==0){
			printf("0\n");
			continue;
		}
		if(n==1){
			printf("2\n");
			continue;
		}
		matrix tmp=expo(A,n);
		printf("%lld\n",(powder2N(tmp.a2))%MOD);
	}
	return 0;
}
