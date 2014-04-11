/* function(s1, s2): return the first location in a string s1 where any char from s2 occurs, or -1
 * if s1 contains on chars from s2;
 *
 * From <The C programming language> Exercise 2-5
 *
 * Date: April 10, 2014
 * 
 */
 
#include <stdio.h>

int find_first_occur(char s1[], char s2[], int lenofs2){
    int i,j, min;
    int indexes[lenofs2];
    for(j=0;s2[j]!='\0';++j){
        for(i=0;s1[i]!='\0' && s1[i]!=s2[j];++i){
        }
        if(s1[i]!='\0')
            indexes[j]=i;
        else
            indexes[j]=-1;
    }

   min = lenofs2;
   for(i=0;i<lenofs2;++i)
       if(min > indexes[i] && indexes[i]!=-1)
           min = indexes[i];
    if(min==lenofs2)
        min=-1;

   return min;
}

int main(int argc, char** argv){
    char s1[]="Hello world";
    char s2[]="it";

    printf("First occurance is at: %d\n", find_first_occur(s1,s2, 2));
    return 0;
}
