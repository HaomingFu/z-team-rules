/* Frome: http://oj.leetcode.com/problems/valid-palindrome/
 * A version 2 answer
 * Sample
 */
#include <iostream>

using namespace std;

class Solution {
    public:
        bool isPalindrome(string s) {
            int ib = 0;
            int ie = s.length() -1;
            if(ie<=0)
                return true;

            while(ib < ie) {
                while(!valid(s[ib]) && ib <ie)
                    ++ib;
                while(!valid(s[ie]) && ib < ie)
                    --ie;

                if(ib < ie && !equal(s[ib], s[ie]))
                    return false;

                ++ib, --ie;
            }

            return true;
            
        }
        bool valid(char c) {
            if((c<='Z' && c>='A') || (c<='z' && c>= 'a') || (c<='9' && c>= '0'))
                return true;
            return false;
        }

        bool equal(char x, char y) {
            if (x==y)
                return true;
            if(x-y == 'a' - 'A' || y - x == 'a' - 'A')
                return true;
            return false;
        }
};

int main(int argc, char * argv[]) {
    Solution mysolution;

    string s1 = "A man, a plan, a canal: Panama";
    string s2 = "race a car";

    cout<<mysolution.isPalindrome(s1)<<endl<<mysolution.isPalindrome(s2)<<endl;
}
