//backtrace TLE

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
	char ret[SIZE], c;
	freopen("ABCDB.txt", "r", stdin);
	int t;
	fast_scani(&t);
	while(t--){
		fast_scani(&N);
		fast_scanstr(str);
		int count[4]={0}, len=(N<<1);
		for(i = 0; i < len; i++){
			count[str[i]-'A']++;
		}
		//~ for(i = 0; i < 4; i++)
			//~ printf("%d ", count[i]);
		//~ printf("\n");
		for(i = 0; i < len; i++){
			c = 'A';
			while(c == str[i] || (i>=1 && c == ret[i-1]) || (count[c-'A']+1) > N){
				c++;
				if(c > 'D'){
					count[ret[i-1]-'A']--;
					ret[i-1]++;
					c = ret[i-1];
					i--;
					continue;
				}
			}
			ret[i] = c;
			count[c-'A']++;
		}
		ret[i] = '\0';
		//~ printf("%s\n", str);
		printf("%s\n", ret);
		//~ for(i = 0; i < 4; i++)
			//~ printf("%d ", count[i]);
		//~ printf("\n");
	}
	fclose(stdin);
	return 0;
}
