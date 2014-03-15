/* Written by Yao Zhao
 * Running time: 0.18s Memory:2.8M on Sphere online judge
 * Stupid program. I need to improve it
 */
#include <iostream>
#include <string>
#include  <stack>
#include <sstream>

using namespace std;

int main(){
    int num;
    cin>>num;
    for(int i =0;i<num;++i){
        stack<char> stk;
        string expr;
        cin>>expr;
        int len = expr.size();
        string res;
        for(int j = 0; j< len; ++j){
            if(expr[j] >=97 && expr[j]<=122){
                char c = expr[j];
                stringstream ss;
                ss<<c;
                string s;
                ss>>s;
                res.append(s);
            }
            else{
                if(expr[j]=='+'||expr[j]=='-'||expr[j]=='*'||expr[j]=='/'||expr[j]=='^')
                    stk.push(expr[j]);
                else{
                    if(expr[j]==')'){
                        char c = stk.top();
                        stk.pop();
                        stringstream ss;
                        string s;
                        ss<<c;
                        ss>>s;
                        res.append(s);
                    }
                }
            }
                    
        }

        cout<<res<<endl;
    }
    return 0;
}
