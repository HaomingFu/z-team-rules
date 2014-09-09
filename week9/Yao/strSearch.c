#include <stdio.h>
#include <string.h>
#define MAXLEN 500

int getLine(char*sptr, int maxlen){
    int i,c;
    for(i=0;i<maxlen-1 && (c=getchar())!=EOF && c!='\n';++i)
        sptr[i] = c;
    if(c=='\n')
        sptr[i++]='\n';
    sptr[i]='\0';

    return i;
}

int main(int argc, char* argv[]){
    int found = 0;
    char line[MAXLEN];

    if(argc != 2)
        printf("Usage: find pattern\n");
    else
        while(getLine(line, MAXLEN)>0){
            if(strstr(line, argv[1])!=NULL){
                printf("%s", line);
                found++;
            }
        }

    return found;
}
