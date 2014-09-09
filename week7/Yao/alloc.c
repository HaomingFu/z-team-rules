/*  a simple version of MALLOC
 */

#include <stdio.h>

#define MAXSIZE  10000

static int allocbuf[MAXSIZE];
static int *allocp = allocbuf;

static int * alloc(int size){
    if(allocbuf + MAXSIZE - allocp >= size){
        allocp += size;
        return allocp - size;
    }
    else
        return 0;
}

void afree(int * p){
    if(p>= allocbuf && p<=allocp)
        allocp = p;
}
