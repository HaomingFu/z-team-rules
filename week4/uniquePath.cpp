/* 
 * Recursive Expression: f(m,n) = f(m-1, n) + f(m, n-1)
 * From http://oj.leetcode.com/problems/unique-paths/
 * 
 * Accepted
 * 
 * Too simple
 * Date: April 5, 2014
 */
#include<iostream>

using namespace std;

int uniquePaths(int m, int n){
    int a[m][n];
    for(int i = 0;i<n;++i)
        a[0][i] = 1;
    for( int i = 0; i<m;++i)
        a[i][0] = 1;

    int i,j;
    for( i = 1;i<n; ++i)
        for(j = 1;j<m;++j)
            a[j][i] = a[j-1][i] + a[j][i-1];

    return a[m-1][n-1];
}


int main(){
    cout<<"a[3][3] = "<<uniquePaths(3,3)<<endl;

    return 0;
}
