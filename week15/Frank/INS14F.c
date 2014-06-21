/*
2*K-1 >= N, N*(N-1)*...*(N-K+1) = N!/(N-K)!
2*K-1 < N, K*(N-1)*...*(N-K+1) = K*(N-1)!/(K-1)!

use the idea of n!*X % MOD = 1 to get Factorial_inv to get rid of TLE
Factorial_inv(n!) = X = (n!)^(MOD-2)
MOD = 10^9+7
Factorial_inv((n-1)!) = n*(n!)^(MOD-2), because (n-1)!*n*X % MOD = 1

TIME: 0.19s MEM：17M 
STATUS: Accepted
DATE：June 21, 2014
From: http://www.spoj.com/problems/INS14F/
__author__ = 'Francis'
Tags: Factorial, Factorial_inv, Power
*/
#include <stdio.h>
#include <string.h>

#define MOD 1000000007
#define SIZE 1000005
#define ll long long

int T, N, K; //1 <= T <= 100000  1 <= K <= N <= 1000000
int i, j;
ll ret, fac[SIZE], fac_inv[SIZE];

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
ll Power(ll a, ll b)
{
    ll ans = 1;
    while(b)
    {
        if(b&1) ans = ans*a%MOD;
        a = a*a%MOD;
        b = b >> 1;
    }
    return ans;
}
void verify()
{
    for (i = 990; i <= 1000; ++i)
    {
        printf("%lld ", Power(fac[i], MOD-1)%MOD);
    }
    printf("\n");
    for (i = 1; i < 10; ++i)
    {
        printf("%lld ", fac[i]);
    }
    printf("\n");
    for (i = 1; i < 10; ++i)
    {
        printf("%lld ", fac_inv[i]);
    }
    printf("\n");
}
void precompute()
{
    fac[0] = 1;
    for (i = 1; i <= 1000000; ++i)
    {
        fac[i] = fac[i-1]*i%MOD;
    }
    fac_inv[1000000] = Power(fac[1000000], MOD-2);
    for (i = 1000000-1; i >= 0; --i)
    {
        fac_inv[i] = fac_inv[i+1]*(i+1)%MOD;
    }
}
int main()
{
    // freopen("INS14F.txt", "r", stdin);
    fast_scani(&T);
    precompute();
    while(T--)
    {
        fast_scani(&N);
        fast_scani(&K);
        ret = 1l;
        if(((K<<1)-1) >= N){
            ret = fac[N]*fac_inv[N-K]%MOD;
        }else{
            ret = (K*fac[N-1]%MOD)*fac_inv[N-K]%MOD;
        }
        printf("%lld\n", ret);
    }
    // verify();
    // fclose(stdin);
    return 0;
}