/*  A simple question from <The C programming Language>
 *  1st. Delete all the specified characters from a string
 *  2nd. Delete all the charcters appearing in a string from the src
 */
#include <stdio.h>

void squeeze(char src[], char c){
    int i, j;
    for(i=j=0;src[i]!='\0';++i){
        if(src[i]!=c)
            src[j++]=src[i];
    }
    src[j]='\0';
}
//delete each characters appearing in line from src
void squeezeStr(char src[], char line[]){
    int i,j,k;
    for(i=0;line[i]!='\0';++i)
        for(j=k=0;src[j]!='\0';++j){
            if(src[j]!=line[i])
                src[k++]=src[j];
        }
        src[k]='\0';
}
int main(int argc, char ** argv){
    char src[] = "Hello World";
    char src2[] = "Hello World";
    squeeze(src, 'o');
    squeezeStr(src2, "World");

    printf("%s\n%s\n", src, src2);

    return 0;
}
