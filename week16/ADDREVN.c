/*

TIME: 0.05s MEM：1.6M
STATUS: Accepted
DATE：July 05, 2014
From: http://www.spoj.com/problems/ADDREV/
__author__ = 'Francis'
Tags: simple patterns again
*/
#include <stdio.h>
#include <string.h>
#define ll long long int

int T, i, j, carry, tmp, len, ti, tj; // (equal to about 10000)
ll A, B , C;


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
void reverseNum(ll *a)
{
    ll reverse = 0;
    while(*a)
    {
        reverse = (reverse<<3) + (reverse<<1) + *a%10;
        *a = *a/10;
    }
    *a = reverse;
}
int main()
{
    // freopen("ADDREV.txt", "r", stdin);
    fast_scani(&T);

    while(T--)
    {
        fast_scanll(&A);
        fast_scanll(&B);
        reverseNum(&A);
        reverseNum(&B);
        C = A + B;
        reverseNum(&C);
        printf("%lld\n", C);
    }
    // fclose(stdin);
    return 0;
}   