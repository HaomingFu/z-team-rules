/*
 * 	ft(n) = ft(n-1) + ft(n-2) + (n-1)  with ft(0) = 0  & ft(1) =1
 *  F(n)=ft(n)+n+2    =>  ft(n)=F(n)-n-2
 * 	| F(n+1)|	| 1 1 |(n-1)  | F(2)   F(1)|
	| F(n) 	| = | 1 0 |   *   | F(1)   F(0)|
	Using delta to take modules 
TIME: 0s MEM：1.6M 
STATUS: Accepted
DATE：April 16, 2014
From: http://www.spoj.com/problems/FIBTWIST/
__author__ = 'frankfu'
*/
#include <stdio.h>
#define ll long long
#define m struct m
#define	gi(a) scanf("%d",&a)
#define	T return
m{ll a1,a2,a3,a4;};
inline int scani()
{
	int z=0;
	char c;
	do{ c=getchar_unlocked(); } while(c<'0');
	for(;c>='0';c=getchar_unlocked()) z = (z<<3) + (z<<1) + (c&15);
	return z;
}
m mu(m t1,m t2, int M){
	m p;
	p.a1=((t1.a1*t2.a1)+(t1.a2*t2.a3))%M;
	p.a2=((t1.a1*t2.a2)+(t1.a2*t2.a4))%M;
	p.a3=((t1.a3*t2.a1)+(t1.a4*t2.a3))%M;
	p.a4=((t1.a3*t2.a2)+(t1.a4*t2.a4))%M;
	T p;
}
m e(m B,ll n, int M){
	if(n==1)T B;
	m C=e(B,n/2, M);
	C=mu(C,C, M);
	if(n%2==1) T mu(B,C,M);
	T C;
}
int main(){
	int t=scani(),n,M;  //10<=t<=100  0<=n<=10^9  100<=M<=10^9
	m A, F, tmp;
	A.a1=1;A.a2=1;A.a3=1;A.a4=0;
	F.a1=6;F.a2=4;F.a3=4;F.a4=2; 
	ll delta;
	while(t--){
		n=scani();M=scani();
		if(n == 0){
			printf("0\n");
			continue;
		}
		if(n == 1)
		{
			printf("1\n");
			continue;
		}
		tmp = e(A, n-1, M);
		tmp = mu(tmp, F, M);
		delta = ((n+2)/M + 1)*M;
		printf("%lld\n", (tmp.a2+delta-n-2)%M);
	}
	T 0;
}
