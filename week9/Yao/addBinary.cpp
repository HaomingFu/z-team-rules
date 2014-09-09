/* From：http://oj.leetcode.com/problems/add-binary/
 * Accepted
 * Date: May 11, 2014
 */
#include <iostream>

using namespace std;

class Solution {
    public:
        string addBinary(string a, string b) {
            int aval = 0, bval = 0,c;
            
            int alen = a.length();
            int blen = b.length();
            int temp=0;
            string res;
            while(alen >0 || blen > 0) {
                if(alen > 0)
                    aval = a[--alen] - '0';
                else
                    aval = 0;
                if(blen >0)
                    bval = b[--blen] - '0';
                else 
                    bval = 0;
                temp += aval + bval;
                c = (temp>=2 ? temp -2: temp);
                temp = (temp >=2 ? 1:0);
                res.insert(0, 1, (char)(c + '0'));
            }
            if(temp==1)
                res.insert(0, 1,'1' );

            return res;
        }
};

int main(int argc, char *argv[]){
    Solution mysolution;
    string s1 = "1100";
    string s2 = "11";
    cout<<mysolution.addBinary(s1,s2)<<endl;
}
