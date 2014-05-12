#include <stdio.h>

int main(int argc, char *argv[]){
    printf("argc: %d \n", argc);
    printf("Parameters are: \n");

    while(argc-- > 0)
        printf(argc > 1 ? "%s ":"%s", *++argv);

    printf("\n");

    return 0;
}

