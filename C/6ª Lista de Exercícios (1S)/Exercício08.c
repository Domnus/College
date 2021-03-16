#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    srand(time(0));

    int A[20], B[20], C[20];
    int upper = 50, lower = 1, n, b = 0, c = 0;

    for (int i = 0; i < 20; i++)
    {
        A[i] = rand() % (upper - lower + 1) + lower;
    }

    for (int i = 0; i < 10; i++)
    {
        if (A[i] % 2 == 0)
        {
            B[b] = A[i];
            b++;
        }
        else
        {
            C[c] = A[i];
            c++;
        }
        
    }

    for (int i = 0; i < 10; i++)
    {
        printf("%d ", A[i]);
    }
    printf("\n");

    for (int i = 0; i < 10; i++)
    {
        printf("%d ", B[i]);
    }
    printf("\n");

    for (int i = 0; i < 10; i++)
    {
        printf("%d ", C[i]);
    }
    printf("\n");
}