/*

TIME: 0.01s MEM：2.2M
O(n)
STATUS: Accepted
DATE：July 04, 2014
From: http://www.spoj.com/problems/ABSP1/
__author__ = 'Francis'
Tags: simple patterns
*/
#include <stdio.h>
#include <string.h>
#define ll long long int

int T, N, i; //(T<=1000)(N<=10000)
int A[10005];  //1<=A[i]<=1000000000 & A[i] <= A[i+1]
ll sum;

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

int main()
{
    freopen("AMSCO1.txt", "r", stdin);
    fast_scani(&T);

    while(T--)
    {
        fast_scani(&N);
        sum = 0;
        for (i = 0; i < N; ++i)
        {
            fast_scani(A+i);
            sum += A[i]*((i<<1)-N+1);
        }
        printf("%lld\n", sum);
    }
    fclose(stdin);
    return 0;
}