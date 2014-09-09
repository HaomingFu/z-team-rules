/* Read lines from input, sort them using quick sort and print lines
 * From the C Programming Languages, Chapter 5.6, Page 90
 * Date: May 8, 2014
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAXLINES 5000
#define MAXLEN 500

char *lineptr[MAXLINES];

int readlines(char* lineptr[], int nlines);
void writelines(char* lineptr[], int nlines);
void quicksort(char* lineptr[], int left, int right);
int getLine(char*, int maxlen);

int main(int argc, char** argv){
    int nlines;
    if((nlines=readlines(lineptr, MAXLINES))>=0){
        quicksort(lineptr, 0, nlines-1);
        writelines(lineptr, nlines);
        return 0;
    }
    else{
        printf("error:input is too big to sort\n");
        return 1;
    }
}

int getLine(char* line, int maxlen){
    int len=0;
    
    while(len < maxlen && (*line=getchar())!='\n'){
        len++;
        line++;
    }
    *line = '\0';
    return len;
}
int readlines(char* lineptr[], int maxlines){
    int len, nlines;
    char *p, line[MAXLEN];

    nlines=0;
    while((len=getLine(line, MAXLEN))>0){
       if(nlines > maxlines || (p = (char*)malloc(MAXLEN * sizeof(char))) == NULL) 
               return -1;
       else{
           strcpy(p, line);
           lineptr[nlines++] = p;
       }
    }
    return nlines;
}

void writelines(char *lineptr[], int nlines){
    int i;
    for(i=0;i<nlines;++i)
        printf("%s\n", lineptr[i]);
}
void quicksort(char *v[], int left, int right){
    int i, last; 
    void swap(char*v[], int i, int j);

    if(left >= right)
        return;
    swap(v, left, (left+right)/2);
    last = left;
    for(i=left+1;i<=right;++i){
        if(strcmp(v[i], v[left])<0)
            swap(v, ++last, i);
    }
    swap(v, last,left);
    quicksort(v, left, last -1);
    quicksort(v, last+1, right);
}
void swap(char *v[], int i, int j){
    char* temp = v[i];
    v[i]=v[j];
    v[j]=temp;
}


