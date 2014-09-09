/* From http://oj.leetcode.com/problems/interleaving-string/
 * Running out of time limit
 * Recursion is not good. I need to convert it to a DP
 */
#include <iostream>
#include <cstring>

using namespace std;

class Solution {
    public:
        bool isInterleave(string s1, string s2, string s3) {
            if(s3.length() != s1.length() + s2.length() )
                return false;
            if((s1.length() == 0 && equal(s2, s3)) || (s2.length() == 0 &&
                    equal(s1,s3)))
                return true;
        
            string tmp1=s3, tmp2=s3;
            return (s3[0]==s1[0] && isInterleave(rm1stletter(s1), s2,rm1stletter(s3) )) ||
                (s3[0] == s2[0] && isInterleave(s1, rm1stletter(s2), rm1stletter(s3) ));

        }
    private:
        bool equal(string &x, string &y) {
            if(x.length()!=y.length())
                return false;
            int i;
            for(i=0;i<x.length(); ++i) {
                if(x[i]!=y[i])
                    return false;
            }
            return true;
        }

        string rm1stletter(const string &s) {
            string tmp(s, 1,s.length()-1);

            return tmp;
        }
};
int main(int argc, char * argv[]) {
    Solution mysolution;

    string test1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa";
    string test2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab";
    string test3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab";

    string s1 = "aabcc", s2="dbbca", s3="aadbbcbcac", s4="aadbbbaccc";

    cout<<mysolution.isInterleave(s1, s2, s3)<<endl;
    cout<<mysolution.isInterleave(s1, s2, s4)<<endl;
    cout<<mysolution.isInterleave(test1, test2, test3)<<endl;
}
