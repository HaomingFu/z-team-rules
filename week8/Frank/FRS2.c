/*
do some precomputation,consider two layers of loop, with Fib(n) = Fib(n%MI), Fib(Fib(n)) = Fib(Fib(n%M)).
TIME: 0.49s MEM：1.6M 
STATUS: Accepted
DATE：April 28, 2014
From: http://www.spoj.com/problems/FRS2/
__author__ = 'frankfu'
*/
/*
 * from:http://stackoverflow.com/questions/12073617/fast-input-output-function?lq=1
 * http://stackoverflow.com/questions/1042110/using-scanf-in-c-programs-is-faster-than-using-cin
 * 
 * getchar_unlocked() seems faster is that it doesn't check for any locks on the input stream from where 
 * it is supposed to fetch a character. So if another thread has locked the input stream, this thread is 
 * supposed to wait till lock count has come to zero. But this function doesn't care about it, thereby 
 * destroying synchronisation between threads.
   But if you are sure that lack of synchronisation wont harm you, then this function might help you to be a bit faster.
 * 
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define ll		long long
#define MO		1000000007  //outside layer
#define MI		2000000016  //inside layer   Fib(n) = Fib(n%MI)
#define M		329616      //Fib(Fib(n)) = Fib(Fib(n%M))
#define matrix		struct Matrix
matrix{ll a1,a2,a3,a4;};

inline int scani()
{
	int z=0;
	char c;
	do{ c=getchar_unlocked(); } while(c<'0');  //getchar_unlocked() is the thread unsafe version of getchar()
	for(;c>='0';c=getchar_unlocked()) z = (z<<3) + (z<<1) + (c&15);
	return z;
}
inline void scanchararr(char *arr)
{
	char c;
	int i = 0;
	do{ c=getchar_unlocked(); } while(c<'0');
	for(;c>='0' && i<300;c=getchar_unlocked(),i++) arr[i] = c;
	arr[i] = '\0';
}
matrix multiply(matrix t1,matrix t2, int MOD){
	matrix tmp;
	tmp.a1=((t1.a1*t2.a1)+(t1.a2*t2.a3))%MOD;
	tmp.a2=((t1.a1*t2.a2)+(t1.a2*t2.a4))%MOD;
	tmp.a3=((t1.a3*t2.a1)+(t1.a4*t2.a3))%MOD;
	tmp.a4=((t1.a3*t2.a2)+(t1.a4*t2.a4))%MOD;
	return tmp;
}
matrix expo(matrix B,ll n, int MOD){
	if(n==1){
		return B;
	}
	matrix C=expo(B,n>>1, MOD);
	C=multiply(C,C, MOD);
	if(n%2==1){
		return multiply(B,C, MOD);
	}
	return C;
}
int main(){
	int t=scani();
	int len, val, i, ret;
	matrix A;
	A.a1=1;	A.a2=1;
	A.a3=1; A.a4=0;
	char num[105];
	while(t--){
		scanchararr(num);
		len=strlen(num); //do not include '\0'
		val=1;ret=0;
		if(len<18){
			ret=atoll(num)%M;
			if(ret == 0){
				printf("0\n");
				continue;
			}
		}else{
			for(i=len-1;i>=0;i--)
			{
				ret=(ret+(num[i]-'0')*val)%M;
				val=((val<<3)+(val<<1))%M;
			}
		}
		printf("%lld\n", expo(A, expo(A, ret, MI).a2, MO).a2);
	}
	return 0;
}
