/*
 * find a formula(referring other's idea, but improve the speed) to calculate the number of triangles
TIME: 0.28s MEM：2.2M 
STATUS: Accepted
DATE：May 10, 2014
From: http://www.spoj.com/problems/IITWPC4B/
__author__ = 'frankfu'
*/
#include <iostream>
#include <cmath> 
using namespace std;
typedef unsigned long long LL;

int main()
{
    ios::sync_with_stdio(false);
    int t;
    LL ans,n;
    long double N;
    cin>>t;
    while(t--)
    {
        cin>>n;
        N = n;
        if((n&1))
            ans = (LL)roundl((1.0*(N+3)*(N+3))/48.0);
        else
            ans = (LL)roundl((1.0*N*N)/48.0);
        cout<<ans<<endl;    
    }
    return 0;
}

