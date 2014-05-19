/* From
 * http://stackoverflow.com/questions/5414854/remove-duplicates-from-array-in-linear-time-and-without-extra-arrays
 * The algorithm seems incorrect
 */
#include<stdio.h>
int main() {
    int a[8] = {3, 6, 3, 4, 5, 1, 7, 7};
    int n = 8, j, k;
    for (int i=0; i<n; i++)
    {
        if (a[i] != i)
        {
             j = a[i];
             k = a[j];
             a[j] = j;  // Swap a[j] and a[i]
             a[i] = k;
         }
     }

     for (int i=0; i<n; i++)
     {
         if (a[i] == i)
         {
            printf("%d\n", i);
         }
     }
}
