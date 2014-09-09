#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 100
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

int main () {
    int t = scani();
    char equation[100];
    char *ep,*i1,*i2, *i3, *i, *end, *tmp;
    int num1, num2, num3;
    while (t --) {
        getchar();
        gets(equation);
        ep = equation;
        tmp = equation;
        num1 = num2 = num3 = 0;
        i1 = strstr(ep, " + ");
        i2 = strstr(ep, " = ");
        i3 = strstr(ep, "machula");
        end = ep+strlen(ep);
        if(i3 < i1){
			//~ num3 = atoi(strncpy(tmp, i2+3, end-i2-3));
			//~ num2 = atoi(strncpy(tmp, i1+3, i2-i1-3));
			for(i = i1+3; i < i2; i ++)
				num2 = (num2<<3) + (num2<<1) + *i-'0';
			for(i = i2+3; i < end; i ++)
				num3 = (num3<<3) + (num3<<1) + *i-'0';
			printf("%d + %d = %d\n", (num3-num2), num2, num3);	
		}
		if(i1 < i3  && i3 < i2){
			//~ num1 = atoi(strncpy(tmp, ep, i1-ep));
			//~ num3 = atoi(strncpy(tmp, i2+3, end-i2-3));
			for(i = ep; i < i1; i ++)
				num1 = (num1<<3) + (num1<<1) + *i-'0';
			for(i = i2+3; i < end; i ++)
				num3 = (num3<<3) + (num3<<1) + *i-'0';
			printf("%d + %d = %d\n", num1, (num3-num1), num3);	
		}
		if(i3 > i2){
			//~ num1 = atoi(strncpy(tmp, ep, i1-ep));
			//~ num2 = atoi(strncpy(tmp, i1+3, i2-i1-3));
			for(i = ep; i < i1; i ++)
				num1 = (num1<<3) + (num1<<1) + *i-'0';
			for(i = i1+3; i < i2; i ++)
				num2 = (num2<<3) + (num2<<1) + *i-'0';
			printf("%d + %d = %d\n", num1, num2, num1+num2);	
		}
    }
    return 0;
}
