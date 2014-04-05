/*
 * By Yao 
 * From  http://oj.leetcode.com/problems/climbing-stairs/ 
 * A stupid problem to calculate Fibonacci series
 * Iterative and recursive solutions are provided. 
 *
 * Accpted.
 *
 * Date: April 5, 2014
 */
#include <iostream>

using namespace std;

class Solution{
    public:
        int climbStairs(int n){
           if(n==1)
               return 1;
           else if(n==2)
               return 2;
           else{
               int a= 1;
               int b = 2;
              for(int i=2;i<n;++i){
                  int temp = b;
                  b +=a;
                  a = temp;
              }
              return b;
           }
        }
        int climbStairs_recursive(int n){
            if(n==1)
                return 1;
            else if(n==2)
                return 2;
            else
                return climbStairs_recursive(n-1) + climbStairs_recursive(n-2);
        }
};


int main(){
    Solution solution;
    cout<<solution.climbStairs(5)<<endl;
    cout<<solution.climbStairs_recursive(5)<<endl;
}
