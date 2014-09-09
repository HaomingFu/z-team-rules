/*
 * Operations on some bits of a number
 * function: getNumberOfNonZero(int num), 
 *
 * From <The C Programming Language>
 *
 * Date: April 10, 2014
 */


#include <stdio.h>

//count the numberof 1s in a given  number 
int getNumberOfNonZero(int num){
    int count = 0;
    while(num){
        count++;
        num = num & (num-1);
    }

    return count;
}
/* getbits: get n bits from position p, position 0 starts from the rightest side*/
int getbits(unsigned x, int n, int p){
    return (x >> (p+1-n)) & ~(~0 << n);
}
 
int main(int argc, char **argv){
    int num = 11;

    printf("In %d, there are %d 1s.\n", num, getNumberOfNonZero(num));
    return 0;
}
