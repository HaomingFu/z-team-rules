// Written by Yao Zhao
// Date: March 23, 2014
// Not accepted, but I didn't find what's wrong;
#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

void add(string op1, string op2);
void substract(string op1, string  op2);
void multiply(string op1, string op2);
int string2num(string op);
string val2string(int val);

int main(){
    int n;
    cin>>n;
    int count = 0;
    while(count<n){
        string expr;
        cin>>expr;

        int i = 0;
        while(expr[i]>=48 && expr[i]<=57)
            ++i;

        string op1, op2;
        op1 =  expr.substr(0,i);
        op2 = expr.substr(i+1, expr.length() - i -1);
        switch(expr[i]){
            case '+':
                add(op1, op2);
                break;
            case '-':
                substract(op1, op2);
                break;
            case '*':
                multiply(op1, op2);
                break;
        }

        count++;
    }
}

void add(string op1, string op2){
    int val1=0;
    int val2=0;
    int res;

    val1 = string2num(op1);
    val2 = string2num(op2);
    res = val1 + val2;
    string r (val2string(res));
    op2 = '+' + op2;
    int len = op1.length()>op2.length()?op1.length():op2.length();
    len = len>r.length() ? len:r.length();

    cout<<setw(len)<<op1<<endl<<setw(len)<<op2<<endl;
    for(int i=0;i<len;++i)
        cout<<'-';
    cout<<endl;
    cout<<setw(len)<<r<<endl<<endl;

}
int string2num(string op){
    int val=0;
    for(int i=0;i<op.length();++i)
        val = val*10 + int(op[i]) - 48;

    return val;
}

string val2string(int val){
    if(val ==0)
        return "0";
    string res;
    while(val>0){
        res = char(val%10 + 48) + res;
        val /= 10;
    }
    return res;
}

void substract(string op1, string op2){
    int val1=0;
    int val2=0;
    int res;
    
    val1 = string2num(op1);
    val2 = string2num(op2);
    res = val1 - val2;
    string r (val2string(res));
    op2 = '-' + op2;
    int len = op1.length() > op2.length() ? op1.length():op2.length();
    cout<<setw(len)<<op1<<endl<<setw(len)<<op2<<endl;
    int dashNum = r.length() > op2.length() ? r.length(): op2.length();
    string dash;
    for(int i=0;i<dashNum;++i)
        dash += '-';
    cout<<setw(len)<<dash<<endl;
    cout<<setw(len)<<r<<endl<<endl;
}
void multiply(string op1, string op2){
    int val1, val2, res;

    val1 = string2num(op1);
    val2 = string2num(op2);
    res = val2*val1;
    int len = op2.length();
    int tem[len];
    for(int i = len -1; i>-1;--i){
        tem[len-1-i] = (int(op2[i]) - 48)*val1;
    }
    op2 = '*'+op2;
    string r (val2string(res));
    int maxLen = op1.length() > op2.length() ? op1.length(): op2.length();
    int maxLen1 = maxLen;
    maxLen = maxLen > r.length() ? maxLen: r.length();
    cout<<setw(maxLen)<<op1<<endl<<setw(maxLen)<<op2<<endl;
    string symbol;
    if(len==1)
        maxLen1 = maxLen;
    for(int i=0;i<maxLen1;++i)
        symbol += '-';
    cout<<setw(maxLen)<<symbol<<endl;
    if(len!=1){
        for(int i=0;i<len;++i){
            cout<<setw(maxLen-i)<<tem[i]<<endl;
        }
        string s;
        string last = val2string(tem[len-1]);
        int dashNum = r.length() > last.length()+len-1 ? r.length() : last.length() + len-1; 
        for(int i=0;i<dashNum;++i)
           s +='-'; 
        cout<<setw(maxLen)<<s<<endl;
    }
    cout<<setw(maxLen)<<res<<endl<<endl;
}
