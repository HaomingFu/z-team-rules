/*
http://en.wikipedia.org/wiki/Wilson's_theorem
According to wilson's theorm (n-1)! mod n =(n-1) if n is prime. 
given n and p. n and p is very large but abs(n-p) is around 1000. 
2 cases 
case 1. n>=p so p will be somewhere in the expansion of n!.
so n!%p=0. 
case 2. (n<p) (p-1)!=(p-1)(p-2) ... (n+1)n!=p-1 calculate
 (p-1)(p-2)..*(n+1) mod p and take modular inverse to find the ans.

 refer to:http://discuss.codechef.com/questions/40916/tux-coder-2014-editorials

TIME: 0.04s MEM：2.2M 
STATUS: Accepted
DATE：June 16, 2014
From: http://www.spoj.com/problems/DCEPC11B/
__author__ = 'frankfu'
*/

#include <stdio.h>
#include <string.h>

typedef long long ll;

ll expo_recur(ll a,ll b,ll mod){
    ll res;
    if(b==0)
        return 1;
    if(b==1)
        return a;
    res = expo_recur(a,b>>1,mod)%mod;
    if(!(b&1))
        return (res*res)%mod;
    else
        return (((res*res)%mod)*a)%mod;
}
ll expo(ll a,ll b,ll mod){
    ll res = 1;
    while(b){
		if(b&1) res=(res*a)%mod;
		a = (a*a)%mod;
		b = b >> 1;
	}
	return res;
}

inline void fast_scanll(ll *a)
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
    ll t,n,p,res,i;

    fast_scanll(&t);
    while(t--){
        fast_scanll(&n);
        fast_scanll(&p);

        if(n == 1){
            printf("1\n");
            continue;
        }
        if(n > p-1){
            printf("0\n");
            continue;
        }
        if(n == p-1){
            printf("%lld\n", p-1);
            continue;
        }
        res = 1;
        for(i = n+1;i <= p-2 ;i++)
            res = (res*i)%p;
        res = expo(res,p-2,p);
        printf("%lld\n", res);
    }
    return 0;
}