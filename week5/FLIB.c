/*
Using 2*2 matrix exponentiation, consider G(n)=f(2n)*f(2n+1)
Refer to: 
https://bitbucket.org/sudharsan123/spoj/src/11bdb99c99e4f56cc751e76b78a8055ef78158af/FLIB.cpp?at=master
http://hi.baidu.com/dut200901102/item/5bd5dfdcd9135115d68ed026
TIME: 1.74s MEM：1.6M 
STATUS:Accepted
DATE：April 14, 2014
From: http://www.spoj.com/submit/FLIB/
__author__ = 'frankfu'
*/
#include <stdio.h>
#define	glli(a)		scanf("%lld",&a)
#define ll		long long
#define INF		2147483647
#define MOD		1000000007
#define clear(a,b)	memset(a,b,sizeof(a))
#define matrix		struct Matrix
matrix{ll a1,a2,a3,a4;};

inline int scan()
{
	int z=0;
	char c;
	do{ c=getchar_unlocked(); } while(c<'0');
	for(;c>='0';c=getchar_unlocked()) z = (z<<3) + (z<<1) + (c&15);
	return z;
}
matrix multiply(matrix t1,matrix t2){
	matrix tmp;
	tmp.a1=((t1.a1*t2.a1)+(t1.a2*t2.a3))%MOD;
	tmp.a2=((t1.a1*t2.a2)+(t1.a2*t2.a4))%MOD;
	tmp.a3=((t1.a3*t2.a1)+(t1.a4*t2.a3))%MOD;
	tmp.a4=((t1.a3*t2.a2)+(t1.a4*t2.a4))%MOD;
	
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
int main(){
	int t=scan();
	matrix A;
	A.a1=1;	A.a2=1;
	A.a3=1; A.a4=0;
	while(t--){
		ll n=0;
		glli(n);
		if(n==0){
			printf("0\n");
			continue;
		}
		if(n==1){
			printf("2\n");
			continue;
		}
		
		matrix tmp1=expo(A,2*n);
		matrix tmp2=multiply(A,tmp1);
		
		printf("%lld\n",((tmp1.a2)*(tmp2.a2))%MOD);
	}
	return 0;
}
