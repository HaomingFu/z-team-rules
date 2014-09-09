/* By Yao
 * Exceed time limit, bad running time
 * From http://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/
 * Date: March 25, 2014
 */
#include <iostream>

using namespace std;

class Solution{
    public:
        int removeDuplicates(int A[], int n){
            if(n<2)
                return n;
            int i = 1;
            while(i<n){
                int current = A[i-1];
                if(current == A[i]){
                    for(int j = i;j<n;++j)
                        A[j-1]=A[j];
                    n--;
                }
                else
                    i++;
            }

            return n;
        }
};

int main(){
    int array=3;
    Solution mysolution;
    cout<<mysolution.removeDuplicates(array, 1)<<endl;

    return 0;
}
