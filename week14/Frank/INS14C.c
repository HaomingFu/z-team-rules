#include <stdio.h>
#include <string.h>

int T, N, K, i; //1 <= T <= 1000 1 <= N <= 1000 1 <= K <= N
char str[1000], tmp[1000];
int tag;
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
    while (c < 33)
        c = getchar_unlocked();
    while (c >= 48)
    {
        str[i] = c;
        c = getchar_unlocked();
        i = i + 1;
    }
    str[i] = '\0';
}
void removefirstc(int i, int tag, int N, char str[], char tmp[], char c)
{
	while(i < N && str[i] == c)
	{
		tmp[i] = c;
		i++;
	}
	if(i == N){
		tmp[i-1] = '\0';
	}else{
		while(i < N)
		{
			tmp[i] = str[i+1];
			i++;
		}
		tmp[i] = '\0';
	}
}
int main()
{
    // freopen("INS14C.txt", "r", stdin);
	fast_scani(&T);
	while(T--)
	{
		fast_scani(&N);
		fast_scani(&K);
		fast_scanstr(str);
		tag = 0; //先删除第一个1 min
		while(N > K)
		{
			i = 0;
			if(tag){ //先删除第一个0 max
				removefirstc(i, tag, N, str, tmp, '1');
				tag = 0;
			}else{ //先删除最第一个1 min
				removefirstc(i, tag, N, str, tmp, '0');
				tag = 1;
			}
			N--;
			strcpy(str, tmp);
			//printf("%s\n", str);
		}
		printf("%s\n", str);
	}
	// fclose(stdin);
	return 0;
}
