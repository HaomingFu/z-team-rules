#include <stdio.h>

void swap(int *A, int ix, int iy){
    int temp = A[ix];
    A[ix] = A[iy];
    A[iy] = temp;
}

int partition(int *A, int p, int r){
    int value = A[r];
    int i = p-1;
    int j, tmp;

    for(j = p ; j<= r; j++){
        if(A[j] <= value){
            i++;
            tmp = A[i];
            A[i] = A[j];
            A[j] = tmp;
        }
    }
   /* 
    tmp = A[++i];
    A[i] = A[r];
    A[r] = tmp;*/

    return i;
}

void QuickSort(int *array, int first, int last){
    int q;
    if(first < last){
        q = partition(array, first, last);
        QuickSort(array, first, q-1);
        QuickSort(array, q+1, last);
    }
}


int main() {
    int numArray[8] = {30,15,11,40,75,80,70,60};
    int i;

    printf("Before sorting: \n");
    for (i=0; i<8; ++i)
        printf("numArray[%d] = %d\n", i, numArray[i]);

    int first = 0;
    int last = sizeof(numArray)/sizeof(numArray[0]);
    QuickSort(numArray, first, last - 1);

    printf("After sorting: \n");
    for(i=0; i<8; ++i)
        printf("numArray[%d]  = %d\n", i, numArray[i]);

    return 0;
}
