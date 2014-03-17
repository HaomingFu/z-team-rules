/* A stupid solution to the K-th smallest problem
 * By using the provided functions in C++, it exceeds the time limits. 
 * Written by Yao Zhao
 * Date: March 16, 2014
 */
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

unsigned array[5000000];
void randomize(unsigned a, unsigned b, unsigned mod){
    for(int i=0;i<5000000;i++){
        a=31014*(a & 65535) + (a>>16);
        b=17508*(b & 65535)+ (b>>16);
        array[i]=((a<<16) + b) % mod;
    }
}
int main(){

    unsigned a, b, mod;
    int k;
    cin>>a>>b>>mod>>k;

    randomize(a,b,mod);

    vector<unsigned> randomized(array, array+sizeof(array)/sizeof(unsigned));

    sort(randomized.begin(), randomized.end());

    cout<<randomized.at(k-1)<<endl;

   return 0; 
}
