/*
 * sort helps a lot
TIME: 6.86s MEM：2.8M 
STATUS: Accepted
DATE：May 2, 2014
From: http://www.spoj.com/problems/ABCDEF/
__author__ = 'frankfu'
*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;
#define MAX  2000000000
inline int scani()
{
	int z=0, negTag = 0;
	char c;
	do{ c=getchar_unlocked(); } while(c<'0' && c!='-');
	for(;c>='0' || c=='-';c=getchar_unlocked()){
		if(c == '-'){
			negTag = 1;
			continue;
		}
		z = (z<<3) + (z<<1) + (c&15);
	}
	if(negTag) z = -z;
	return z;
}
int pivotLoc(int *arr, int bt, int ed)
{
	int stand;

	stand = arr[bt];

	while (bt < ed) {
		while (bt < ed && arr[ed] >= stand)	ed --;
		if (bt < ed)	arr[bt ++] = arr[ed];

		while (bt < ed && arr[bt] <= stand)	bt ++;
		if (bt < ed)	arr[ed --] = arr[bt];
	}
	arr[bt] = stand;
	return bt;
}
void quickSort(int *arr, int bt, int ed)
{
	int pivot;
	if (bt < ed) {
		pivot = pivotLoc(arr, bt, ed);
		quickSort(arr, bt, pivot - 1);
		quickSort(arr, pivot + 1, ed);
	}
}
int main()
{
	int N = scani(), i = 0, j = 0, k = 0, count = 0, size; // 1<=N<=100 // set S of integers between -30000 and 30000 (inclusive)
	int S[100];
	i = 0; j = 0; k = 0; count = 0;
	while(i < N)
	{
		S[i] = scani();
		i++;
	}
	size = N*N*N;
	int *retArr1 = (int *)malloc(size*sizeof(int));
	int *retArr2 = (int *)malloc(size*sizeof(int));
	memset(retArr1,0,size*sizeof(int));
	memset(retArr2,0,size*sizeof(int));
	for(i = 0; i < N; i++)
		for(j = 0; j < N; j++)
			for(k = 0; k < N; k++)
			{
				*(retArr1+i*N*N+j*N+k) = S[i]*S[j]+S[k];
				if(S[i] != 0) *(retArr2+i*N*N+j*N+k) = S[i]*(S[j]+S[k]);
				else  *(retArr2+i*N*N+j*N+k) = MAX;
			}
	sort(retArr1, retArr1+size);
	sort(retArr2, retArr2+size);
	count = 0;
	for(i = 0, j = 0; i < size && j < size; )
	{
		if(retArr2[j] == MAX){
			j++;
			continue;
		}
		if(*(retArr1+i) == *(retArr2+j)){
			int tmp1 = 1,tmp2 = 1;
			while(*(retArr1+i) == *(retArr1+i+tmp1)) tmp1++;
			while(*(retArr2+j) == *(retArr2+j+tmp2)) tmp2++;
			count += tmp1*tmp2;
			i = i+tmp1;
			j = j+tmp2;
		}
		else if(*(retArr1+i) > *(retArr2+j)) j++;
		else i++;
	}
	printf("%d\n", count);
	free(retArr1);
	free(retArr2);
	return 0;
}

