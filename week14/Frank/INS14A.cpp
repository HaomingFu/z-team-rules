//get enough test cases for INS14A
#include <iostream>
#include <fstream>
using namespace std;

string dec2bin(int x) {
   string s = "";
   while(x) {
      s = char((x&1)+'0') + s;
      x >>= 1;
   }
   return s;
}

int main()
{
   ofstream out("INS14Acom.txt");

   int tc = 0;
   for(int i = 1; i < 1024; i++)
      tc +=  __builtin_popcount(i);
   out << tc << endl;

   for(int i = 1; i < 1024; i++) {
      int n = __builtin_popcount(i);
      string s = dec2bin(i);
      for(int j = 1; j <= n; j++)
         out << j << endl << s << endl;
   }
   out.close();
}
