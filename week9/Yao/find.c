#include <stdio.h>
#include <string.h>

#define MAXLEN 500

int getLine(char* sptr, int maxlen){
    int c, i;
    for(i=0; i < maxlen-1 && (c=getchar())!=EOF && c!= '\n';++i)
        sptr[i]=c;

    if(c=='\n')
        sptr[i++] = '\n';
    sptr[i]='\0';
    
    return i;
}
int main(int argc, char* argv[]){
    int except=0, number=0, found=0;
    char c;
    long lineno =0;
    char line[MAXLEN];

    while(--argc > 0 && (*++argv)[0] == '-'){
        while( c = *++argv[0]){
            switch(c){
            case 'x':
                except = 1;
                break;
            case 'n':
                number = 1;
                break;
            default:
                printf("find: illegal options %c\n",c);
                argc = 0;
                found = -1;
                break;
            }
        }
    }

    if(argc != 1)
        printf("Usage: find -x -n pattern\n");
    else
        while (getLine(line, MAXLEN) >0 ) {
            lineno++;
            if (( strstr(line, *argv) != NULL) != except) {
                if (number)
                    printf("%ld:", lineno);
                printf("%s", line);
                found++;
            }
        }

    return found;
}
