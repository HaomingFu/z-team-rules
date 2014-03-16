/* return a palindrome
 * Running time:0.75s Memory: 2.7
 * Written by Yao Zhao
 * Date: March 15, 2014
 */
#include <iostream>
#include <string>

using namespace std;

int main(){
    int n;
    cin>>n;
    int count = 0;
    while(count<n){
        count++;

        string num;
        cin>>num;
        int size = num.length();
        int r,l;
        l=size/2-1;
        r=size%2==1?size/2+1:size/2;
        if(size==1){
            l=0;
            r=0;
        }

        string rnum(num,r,size-r);
        string lnum;
        
        for(int i=l;i>=0;--i)
            lnum.push_back(num[i]);
        if(lnum.compare(rnum)>0){
            num.replace(r,size-r,lnum);
        }
        else{
            int i;
            if(size%2==1)
               i=size/2; 
            else
                i=size/2-1;
            for(;i>=0;--i){
                if(num[i]!='9'){
                    num[i]++;
                    for(int j=r;j<size;++j)
                        num[j]=num[size-1-j];
                    break;
                }
                else
                    num[i]='0';
            }
            if(num[0]=='0'){
                num.resize(num.length()+1,'0');
                num.assign(num.length(),'0');
                num[0]=num[num.length()-1]='1';
            }
        }
        cout<<num<<endl;
        
    }
}
