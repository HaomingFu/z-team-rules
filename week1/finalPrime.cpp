/* SPOJ: Prime Generator ID:2 / 
 * Running time: 3.01s Memory:3.4M
 * written by Yao Zhao
 * Thanks to Haoming, giving me a lot of help on this. 
 */
#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;
const int  MAXP=100003; //size of prime table
const int MAXPA=40000; //size of the arrayo of prime numbersf
const int MAXN = 100002; //size of testing number table


void primeTable(int parr[]){
    bool * ptbl = (bool*)malloc(MAXP*sizeof(bool));
    memset(ptbl,true,MAXP);
    memset(ptbl,2,false);

    for(int ix=2;ix<MAXP;++ix)
        if(ptbl[ix])
            for(int k=2;k*ix<MAXP;++k)
                ptbl[k*ix]=false;
    int j=0;
    for(int ix=2;ix<MAXP;++ix){
        if(ptbl[ix]){
            parr[j]=ix;
            j++;
        }
    }
}

int factor(int val,int *parr){
    int *a= parr;
    while((*a)*(*a)<=val){
        if(val%(*a)==0)
            return *a;
        else
            a++;
    }
    return val;
}

int main(){
    int * parr=(int *)malloc(sizeof(int)*MAXPA);
    memset(parr,0, MAXPA);
    primeTable(parr);

    int *nums=(int*)malloc(sizeof(int)*MAXN);

    int total;
    cin>>total;
    int t=0;
    while(t<total){
        t++;
        int m,n;
        cin>>m>>n;
        m=(m==1?2:m);

        int len=n-m+1;
        int *index = nums;
        for(int i=0;i<len;++i)
            *(index++)=m+i;

        int i=0;
        while(i<len){
            if(nums[i]){
                int step = factor(nums[i],parr);
                if(step==nums[i])
                    cout<<step<<endl;
                for(int k=0;i+k*step<len;++k)
                    nums[i+k*step]=0;
            }
            i++;
        }
    }

}
