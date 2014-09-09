/* From: http://oj.leetcode.com/problems/valid-palindrome/
 * Accepted
 * Date: May 11, 2014
 */
#include <iostream>
#include <cctype>

using namespace std;

class Solution {
    public:
        bool isPalindrome(string s) {
            int len, i;
            len = s.length();
            string::iterator ib = s.begin();
            string::iterator ie = s.end();
            ie--;
            while(ib < ie){
                while( !isalnum(*(ib)) && ib < ie ) //pay attentionto special cases
                    ib++;
                while(!isalnum(*(ie)) && ib < ie )
                    ie--;
                if(tolower(*ib) != tolower(*ie))
                    return false;
                else{
                    ib++;
                    ie--;
                }
            }

            return true;
        }
};

int main(int argc, char *argv[]){
    Solution mysolution;
    string s = "A man, a plan, a canal: Panama";
    string s2 = "race a car";

    cout<<mysolution.isPalindrome(s)<<endl;
    cout<<mysolution.isPalindrome(s2)<<endl;
}

