/* Accepted
 * By Yao
 * Date: March 28, 2014
 * From http://oj.leetcode.com/problems/reverse-words-in-a-string/
 */
#include <iostream>
#include <string>

using namespace std;

string reverseWords(const string &s){
    char word[100];
    string res;
    int i=0;
    int j=0;
    int status =0;
    while(s[i]!='\0'){
       if(s[i]!=' ' &&  s[i] !='\t' && s[i]!='\n') {
           status = 1;
           word[j++] = s[i];
       }
       if(status && (s[i] == ' ' || s[i] == '\t'|| s[i]=='\n')){
           status = 0;
           if(!res.length())
               res  = string(word, j) + res;
           else
               res = string(word, j) + ' ' + res;
           j = 0;
       }
       i++;
    }
    if(j && res.length())
        res = string(word, j) + ' ' + res;
    if(j && !res.length())
        res = string(word, j);
    
    return res;
}

int main(){
    string s;
    getline(cin,s);

    cout<<reverseWords(s)<<endl;
}
