#include <stdio.h>
#include <string.h>
inline int scani()
{
	int z = 0;
	char c;
	do{
		c = getchar_unlocked();
	}while(c < '0'); 
	for(;c >= '0';c = getchar_unlocked())
		z = (z << 3) + (z << 1) + (c & 15);
	return z;
}
inline void scanchararr(char *arr)
{
	char c;
	int i = 0;
	do{ c=getchar_unlocked(); } while(c<'A');
	for(;c>='A' && c<='Z';c=getchar_unlocked(),i++) arr[i] = c;
	arr[i] = '\0';
}
int main()
{
	char str[50005];
	int t = scani();
	while(t--)
	{
		scani();
		scanchararr(str);
		printf("%c\n", str[strlen(str)-1]);
	}
	return 0;
}
