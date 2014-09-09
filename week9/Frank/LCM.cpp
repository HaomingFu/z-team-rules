#include <cstdio>
#include <map>
using namespace std; 
typedef long long  LL;

LL gcd_nonre(LL a, LL b)
{
    LL tmp;
    while(b != 0){
        tmp = a;
        a = b;
        b = tmp%b;
    }
    return a;
}
LL lcm(LL a,LL b){return a/gcd_nonre(a,b)*b;}
inline LL scan()
{
	LL z = 0;
	char c;
	do{ c=getchar_unlocked(); } while(c<'0');
	for(;c>='0';c=getchar_unlocked()) z = (z<<3) + (z<<1) + (c&15);
	return z;
}
int main()
{
	map<LL,LL>dp[45];
	map<LL,LL>sum[45];
	int saved[45]={0}, i, nc, h;
    map<LL,LL>::iterator it, ir;
    pair<map<LL,LL>::iterator,map<LL,LL>::iterator> ret;
    LL n, m;
    dp[1][1]=1;
    for(i=2;i<=40;i++)
    {
        dp[i]=dp[i-1];
        dp[i][i]++;
        for(it=dp[i-1].begin();it!=dp[i-1].end();it++){
			if(i%it->first == 0)  dp[i][i]+=it->second;
			else if(it->first%i == 0) dp[i][it->first]+=it->second;
            else  dp[i][lcm(it->first,i)]+=it->second;
		}
    }
    nc = scan();
    for(h=1;h<=nc;h++)
    {
        n = scan(); m = scan();
        printf("Case #%d: ", h);
        if(m==1)
        {
			printf("%lld\n", (1LL<<n)-1);
        }
        else
        {
			if(saved[n]){
				it = sum[n].end();
				it--;
				if(m <= it->first){
					ret = sum[n].equal_range(m);
					printf("%lld\n", ret.first->second);
				}else{
					printf("0\n");
				}
			}else{
				it = dp[n].end(); 
				it--;
				sum[n][it->first] = it->second;
				for(ir=it, it--;it!=dp[n].begin();ir=it, it--){
					sum[n][it->first] = sum[n][ir->first] + it->second;
				}
				if(it != dp[n].begin()){
					sum[n][it->first] = sum[n][ir->first] + it->second;
				}
				it = sum[n].end();
				it--;
				if(m <= it->first){
					ret = sum[n].equal_range(m);
					printf("%lld\n", ret.first->second);
				}else{
					printf("0\n");
				}
				saved[n] = 1;
			}
        }
    }
}

