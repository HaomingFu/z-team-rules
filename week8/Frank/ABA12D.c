/*
 * A023194		 Numbers n such that sigma(n) (sum of divisors of n) is prime.
TIME: 0s MEM：1.6M 
STATUS: Accepted
DATE：May 1, 2014
From: http://www.spoj.com/problems/ABA12D/
__author__ = 'frankfu'
*/
#include<stdio.h>
#include<math.h>
int main()
{
	//A023194 Numbers n such that sigma(n) (sum of divisors of n) is prime.
	int k_number[] = {2, 4, 9, 16, 25, 64, 289, 729, 1681, 2401, 3481, 4096, 5041, 7921, 10201,
		15625, 17161, 27889, 28561, 29929, 65536, 83521, 85849, 146689, 262144, 279841,
		 458329, 491401, 531441, 552049, 579121, 597529, 683929, 703921, 707281, 734449,
		  829921, 1190281};
	
	int t, count,i, low,high;
	scanf("%d",&t);
	while(t--)
	{
		count=0;i=0;
		scanf("%d %d",&low,&high);
		while(k_number[i] < low)
			i++;
		while(k_number[i] <= high)
		{
			count++;	
			i++;
		}	
		printf("%d\n",count);
	}
	return 0;
}
