#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 5005
/*
Using simple DP
Referred to:http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=dynProg
TIME: 0s MEM：1.6M 
STATUS:Accepted
DATE：April 12, 2014
From: http://www.spoj.com/submit/ACODE/
__author__ = 'frankfu'
*/

char acode[MAXN];
int main()
{
	while(1==1)
	{
		memset(acode, 0, sizeof(acode));
		fgets(acode, MAXN, stdin);
		if(acode[0] == '0') break;
		else{
			long long dp0 = 1, dp1 = 1, dp2=0;
			int temp = 0, begin = 1, len = strlen(acode)-1;
			if(len == 1) dp2 = 1;
			while(begin < len)
			{
				dp2 = 0;
				if(acode[begin]-'0')
					dp2 = dp1;
				temp = (acode[begin-1]-'0')*10+(acode[begin]-'0');
				if(9 < temp && temp <= 26)
					dp2 += dp0;
				dp0 = dp1;
				dp1 = dp2;				
				begin++;
			}			
			printf("%lld\n", dp2);
		}
	}
	return 0;
}
