/*
B[i][j] = A[i][j]+max{B[i+1][j], B[i][j+1], B[i+1][j+1]}+min{B[i+1][j], B[i][j+1], B[i+1][j+1]}
calculate from big index to small index
TIME: 0.06s MEM：5.1M 
STATUS: Accepted
DATE：June 21, 2014
From: http://www.spoj.com/problems/INS14E/
__author__ = 'Francis'
Tags: DP
*/

#include <stdio.h>
#include <string.h>

int T, M, N; //1<= T <=10 2 <= M,N <= 500 0 <= A[i][j] <=10^6
int A[505][505];
double B[505][505], tmp;
int i, j;
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
void Max(double *tmp, double b){if(*tmp < b) *tmp = b;}
void Min(double *tmp, double b){if(*tmp > b) *tmp = b;}
int main()
{
    freopen("INS14E.txt", "r", stdin);
    fast_scani(&T);
    while(T--)
    {
        fast_scani(&M);        
        fast_scani(&N);
        for (i = 0; i < M; ++i)
            for (j = 0; j < N; ++j)
                fast_scani(&A[i][j]);
        for (i = M-1; i >= 0; --i)
        {
            for (j = N-1; j >= 0; --j)
            {
                B[i][j] = 0;
                tmp = 0;
                if(i < M-1 && j < N-1)  Max(&tmp, B[i+1][j+1]); 
                if(i < M-1)  Max(&tmp, B[i+1][j]);
                if(j < N-1) Max(&tmp, B[i][j+1]);
                B[i][j] += tmp*0.5;
                if(i < M-1 && j < N-1)  Min(&tmp, B[i+1][j+1]); 
                if(i < M-1)  Min(&tmp, B[i+1][j]);
                if(j < N-1) Min(&tmp, B[i][j+1]);
                B[i][j] += tmp*0.5;
                B[i][j] += A[i][j];
                // printf("B[%d][%d]:=%.6f\n", i, j, B[i][j]);
            }
        }
        printf("%.6f\n", B[0][0]);
    }
    fclose(stdin);
    return 0;
}
