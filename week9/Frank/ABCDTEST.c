//dfs TLE

#include <stdio.h>
#include <stdlib.h>
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
void dfs(int in, int *count, char *str, char *ret, int N)
{
	if(in == (N<<1)){
		ret[in] = '\0';
		//~ printf("%s\n", str);
		printf("%s\n", ret);
		//~ int i;
		//~ for(i = 0; i < 4; i++)
			//~ printf("%d ", count[i]);
		//~ printf("\n");
		exit(0);
	}
	char c = 'A';
	while(c <= 'D'){
		if(c == str[in] || (in>=1 && c == ret[in-1]) || (count[c-'A']+1) > N){
			c++;
			continue;
		}
		ret[in] = c;
		count[c-'A']++;
		dfs(in+1, count, str, ret, N);
		count[c-'A']--;
		c++;
	}
}
int main(){
	int N, i; // N ≤ 50000
	char str[SIZE];
	char ret[SIZE];
	//~ char c;
	//~ freopen("ABCD.txt", "r", stdin);
	//~ int t;
	//~ fast_scani(&t);
	//~ while(t--){
		fast_scani(&N);
		fast_scanstr(str);
		int count[4]={0}, len=(N<<1);
		for(i = 0; i < len; i++){
			count[str[i]-'A']++;
		}
		//~ for(i = 0; i < 4; i++)
			//~ printf("%d ", count[i]);
		//~ printf("\n");
		dfs(0, count, str, ret, N);
	//~ }
	//~ fclose(stdin);
	return 0;
}
