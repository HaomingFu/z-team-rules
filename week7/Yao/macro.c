#include <stdio.h>

#define swap(t, x, y) { t temp; temp = x; x= y; y=temp;}

int main(int argc, char **argv){
    int a = 1;
    int b = 2;
    printf("Before swap: \n");
    printf("a = %d, b = %d \n", a, b);

    swap(int, a, b)

    printf("After swap: \n");
    printf("a = %d, b = %d \n", a, b);

    return 0;
}
