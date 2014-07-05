/*

TIME: 0s MEM：2.6M
O(logn)
STATUS: Accepted
DATE：July 05, 2014
From: http://www.spoj.com/problems/ADV04J/
__author__ = 'Francis'
Tags: simple patterns again
*/

#include<iostream>
#include<fstream>

using namespace std;

int t;
long long int a;
int res=0;

int main()
{
    freopen("ADV04J.txt", "r", stdin);	
	cin>>t;
	while(t--)
	{
		cin>>a;
		res = 0;
		while(a>0)
		{
			if(a==2)
			{ 
				res+=2;
				break;
			}
			if(a%2==0)
				a/=2;
			else
				a = (a/2)+1;
			res++;
		}
		cout<<res<<endl;
	}
	fclose(stdin);
	return 0;
}
