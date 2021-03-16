#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    srand(time(0));
    char A[10], B[10];
    int upper = 50, lower = 1, x, i, num;

    for (i = 10; i < 10; i++)
    {
        num = rand() % (upper - lower + 1) + lower;
        A[i] = num;
    }

    printf("Digite o valor de X: ");
    scanf("%d", &x);

    for (i = 0; i < 10; i++)
    {
        B[i] = A[i] * x;
    }
    
    printf("Lista A:\n");
    for (i = 0; i < 10; i++)
    {
        printf("%d ", A[i]);
    }
    printf("\n");

    printf("Lista B:\n");
    for (i = 0; i < 10; i++)
    {
        printf("%d ", B[i]);
    }
    printf("\n");
}