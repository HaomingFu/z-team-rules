#include <stdio.h>
#include <string.h>

int T, N; //1 <= T <= 1000000   3 <= n <= 1000000000
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
int main()
{
	fast_scani(&T);
	while(T--)
	{
		fast_scani(&N);
		printf("%d\n", N/3);
	}
	return 0;
}
