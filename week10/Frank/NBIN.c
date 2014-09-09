/*
 * 
brute force  and simple dp
TIME: 0s MEM：2.2M 
STATUS: Accepted
DATE：May 15, 2014
From: http://www.spoj.com/problems/NBIN/
__author__ = 'frankfu'
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LL long long
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
inline void fast_scanll(LL *a)
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
int binarySearch(const LL A[], LL X, int N)
{
    int low, mid, high;
    low = 0; high = N - 1;
    while(low <= high)
    {
        mid = (low + high) / 2;
        if(A[mid] < X)
            low = mid + 1;
        else if(A[mid] > X)
            high = mid - 1;
        else
            return mid; /*Found: Return mid,A[mid] = X*/
    }
    return high;/*Not Found: Return low,A[low] < X*/
}
int main(){
	LL start[] = {1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
	 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 
	 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 
	 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 
	 1134903170, 1836311903, 2971215073u, 4807526976, 7778742049, 12586269025, 20365011074,
	  32951280099, 53316291173, 86267571272, 139583862445, 225851433717, 365435296162, 
	  591286729879, 956722026041, 1548008755920, 2504730781961, 4052739537881, 
	  6557470319842, 10610209857723, 17167680177565, 27777890035288, 44945570212853, 
	  72723460248141, 117669030460994, 190392490709135, 308061521170129, 498454011879264,
	  806515533049393, 1304969544928657}, N, tmp;

	int T, index, id, ib;  //T(<=1000)   N(<=10^15)
	char ret[75] = {0};
	// freopen("NBIN.txt", "r", stdin);
	fast_scani(&T);
	while(T--)
	{
		fast_scanll(&N);
		index = binarySearch(start, N, (sizeof(start)/sizeof(start[0])));
		if(N == start[index]){
			printf("1");
			while(index--) printf("0");
			printf("\n");
		}
		else if(N == start[index+1]-1){
			int t = 0;
			while(t <= index){
				if(t&1) printf("0");
				else printf("1");
				t++;
			}
			printf("\n");
		}
		else{
			ib = index + 1;
			tmp = N;
			id = 0;
			while(tmp >= 2){
				tmp -= start[index];
				ret[id] = '1';
				ret[id+1] = '0';
				id += 2;
				index = binarySearch(start, tmp, (sizeof(start)/sizeof(start[0])));
				while(id < ib-index-1)  ret[id++] = '0';
			}
			if(tmp == 1){
				ret[id] = '1';
				id++;
			}
			ret[id] = '\0';
			printf("%s\n", ret);
		}
	}
	// fclose(stdin);
	return 0;
}
