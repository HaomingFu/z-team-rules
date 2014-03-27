/* Accepted
 * By Yao
 * March 27, 2014
 * From http://oj.leetcode.com/problems/evaluate-reverse-polish-notation/
 */
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
    public:
        int evalRPN(vector<string> &tokens) {
            int array[1000];
            int *parr = array;
            for(vector<string>::iterator it = tokens.begin();it!=tokens.end();++it){
                int val;
                val = (*it)[0] - '0';
                if((val>=0 && val<=9) || (*it).length()>1)
                    *parr++ = string2num(*it);

                if((*it)[0] == '+'){
                    int op1 = *(--parr);
                    int op2 = *(--parr);
                    *parr = op1 + op2;
                    ++parr;
                }
                else if((*it)[0] == '-' && (*it).length()==1){
                    int op1 = *(--parr);
                    int op2 = *(--parr);
                    *parr = op2 - op1;
                    ++parr;
                }
                else if((*it)[0] == '*'){
                    int op1 = *(--parr);
                    int op2 = *(--parr);
                    *parr = op1 * op2;
                    ++parr;
                }
                else if((*it)[0] == '/'){
                    int op1 = *(--parr);
                    int op2 = *(--parr);
                    *parr = op2/op1;
                    ++parr;
                }
            }


            return array[0];
        }

        int string2num(string & str){
            int res =0;
            char buffer[20];
            size_t len;
            int flag =1;
            if(str[0] == '-'){
                len = str.copy(buffer, str.length()-1, 1);
                flag = -1;
            }
            else
                len = str.copy(buffer, str.length(), 0);

            for(int i=0;i<len;++i)
                res = 10*res + (buffer[i]-'0');

            return flag*res;
        }
};

int main(){
    Solution mysolution;

    vector<string> strvec;

    strvec.push_back("-2");
    strvec.push_back("1");
    strvec.push_back("+");
    strvec.push_back("3");
    strvec.push_back("*");

    cout<<mysolution.evalRPN(strvec)<<endl;

}
