/*
 * easy
TIME: 0.06s MEM：1.6M 
STATUS: Accepted
DATE：May 10, 2014
From: http://www.spoj.com/problems/ARMY/
__author__ = 'frankfu'
*/
#include <stdio.h>
#define LL long long

inline int scani()
{
	int z = 0;
	char c;
	do{
		c=getchar_unlocked();
	}while(c < '0'); 
	for(;c >= '0';c = getchar_unlocked())
		z = (z<<3) + (z<<1) + (c&15);
	return z;
}
inline void fast_scani(int *a)
{
    register char c=0;
    while (c<33) c=getchar_unlocked();
    *a=0;
    while (c>33)
    {
        *a=*a*10+c-'0';
        c=getchar_unlocked();
    }
}
//char s[16];
inline void fast_scanstr(char *str)
{
    register char c=0;
    register int i = 0;
    while (c < 33)
        c = getchar_unlocked();
    while (c > 65)
    {
        str[i] = c;
        c = getchar_unlocked();
        i = i + 1;
    }
    str[i] = '\0';
}
int main(){
	int t, NG, NM, maxG, maxM, tmp;
	fast_scani(&t);
	while(t--){
		getchar_unlocked();
		fast_scani(&NG);
		fast_scani(&NM);
		maxM = maxG = 0;
		while(NG--){
			fast_scani(&tmp);
			if(tmp > maxG) maxG = tmp;
		}
		while(NM--){
			fast_scani(&tmp);
			if(tmp > maxM) maxM = tmp;
		}
		if(maxG >= maxM)
			printf("%s\n", "Godzilla");
		else
			printf("%s\n", "MechaGodzilla");			
	}	return 0;
}
