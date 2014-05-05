#include <stdio.h>
#include <math.h>
inline int scani()
{
	int z=0;
	char c;
	do{ c=getchar_unlocked(); } while(c<'0');  //getchar_unlocked() is the thread unsafe version of getchar()
	for(;c>='0';c=getchar_unlocked()) z = (z<<3) + (z<<1) + (c&15);
	return z;
}
// 1.7 * 10^308
double g(int n)
{
	double p = pow(5, 0.5);
	return ((pow(1+p,n*1.0)-pow(1-p,n*1.0))*1.0/(p*pow(2.0, n*1.0)));
}
int main(){
	int t=scani();
	while(t--){
		printf("%.f\n", g(scani()+2));
	}
	return 0;
}
