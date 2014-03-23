#include <iostream>
#include <string>

using namespace std;

string reverseWords(const string &s){
    string temp;
    int i=0;
    int j=0;
    while(i<s.length()){
        if(s[i]==' '){
            temp =' ' +  s.substr(j,i-j) + temp;
            j=i+1;
        }
        ++i;
    }
    return s.substr(j,s.length()-j+1)+temp;
}

int main(){
    string s;
    getline(cin,s);

    cout<<reverseWords(s)<<endl;
}
