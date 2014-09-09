/* Accepted
 * By Yao March 25
 * http://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/
 */

#include <iostream>

using namespace std;

class Solution{
    public:
        int removeDuplicate(int A[], int n){
            if(n<2)
                return n;
            int current = A[0];
            for(int i=1;i<n;++i){
                if(A[i]==current){
                    A[i]=999999;
                }
                else
                    current = A[i];
            }

            //find the first node that is duplicated
            int i=1;
            int j;
             while(i<n && A[i]!=999999)
                    ++i;
            j = i;
            while(i<n && j<n){
                while(j<n && A[j]==999999)
                    ++j;

                if(j==n)
                    return i;

                A[i]=A[j];
                A[j]=999999;
                i++;
                j++;

                while(i<n && A[i]!=999999)
                    ++i;
            }

            return i;

    } 
};

int main(){
    int array[] = {1,1,2};

    Solution mysolution;
    cout<<mysolution.removeDuplicate(array,3)<<endl;
}
