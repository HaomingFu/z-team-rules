/*
 * 
use the simple idea of brute force.
2*2N can be divided into N*(2*2)
for 2*2:
AB->CD AC->BD AD->BC BC->AD BD->AC CD->AB , vice versa
and consider the left 2*2 pair will influence the current pair 
TIME: 0.02s MEM：1.8M 
STATUS: Accepted
DATE：May 14, 2014
From: http://www.spoj.com/problems/ABCD/
__author__ = 'frankfu'
*/
#include <stdio.h>
#include <string.h>
#define LL long long
#define SIZE 100005

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
inline void fast_scanstr(char *str)
{
	register char c=0;
	register int i = 0;
	while (c < 65)
		c = getchar_unlocked();
	while (c >= 65 && c <= 68)
	{
		str[i] = c;
		c = getchar_unlocked();
		i = i + 1;
	}
	str[i] = '\0';
}
int main(){
	int N, i; // N ≤ 50000
	char str[SIZE];
	char ret[SIZE], c=' ';
	//~ freopen("ABCDB.txt", "r", stdin);
	//~ int t;
	//~ fast_scani(&t);
	//~ while(t--){
		fast_scani(&N);
		fast_scanstr(str);
		int len=(N<<1);
		for(i = 0; i < len; i += 2){
			if((str[i] == 'A' && str[i+1] == 'B') || (str[i] == 'B' && str[i+1] == 'A')){
				if(c == 'C'){
					ret[i] = 'D';
					ret[i+1] = 'C';
				}else{
					ret[i] = 'C';
					ret[i+1] = 'D';
				}
			}
 			if((str[i] == 'A' && str[i+1] == 'C') || (str[i] == 'C' && str[i+1] == 'A')){
				if(c == 'B'){
					ret[i] = 'D';
					ret[i+1] = 'B';
				}else{
					ret[i] = 'B';
					ret[i+1] = 'D';
				}
			}
			if((str[i] == 'A' && str[i+1] == 'D') || (str[i] == 'D' && str[i+1] == 'A')){
				if(c == 'B'){
					ret[i] = 'C';
					ret[i+1] = 'B';
				}else{
					ret[i] = 'B';
					ret[i+1] = 'C';
				}
			}
			if((str[i] == 'B' && str[i+1] == 'C') || (str[i] == 'C' && str[i+1] == 'B')){
				if(c == 'A'){
					ret[i] = 'D';
					ret[i+1] = 'A';
				}else{
					ret[i] = 'A';
					ret[i+1] = 'D';
				}
			}
			if((str[i] == 'B' && str[i+1] == 'D') || (str[i] == 'D' && str[i+1] == 'B')){
				if(c == 'A'){
					ret[i] = 'C';
					ret[i+1] = 'A';
				}else{
					ret[i] = 'A';
					ret[i+1] = 'C';
				}
			}
			if((str[i] == 'C' && str[i+1] == 'D') || (str[i] == 'D' && str[i+1] == 'C')){
				if(c == 'A'){
					ret[i] = 'B';
					ret[i+1] = 'A';
				}else{
					ret[i] = 'A';
					ret[i+1] = 'B';
				}
			}
			c = ret[i+1];
		}
		ret[i] = '\0';
		//~ printf("%s\n", str);		
		printf("%s\n", ret);
	//~ }
	//~ fclose(stdin);
	return 0;
}
