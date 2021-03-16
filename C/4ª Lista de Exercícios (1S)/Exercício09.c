#include <stdio.h>

int main()
{
    int i, n = 0, n2 = 1, x;
    printf("%d ", n2);

    for (i = 1; i < 20; i++)
    {
        x = n + n2;
        printf("%d ", x);
        n = n2;
        n2 = x;
    }
    printf("\n");
}