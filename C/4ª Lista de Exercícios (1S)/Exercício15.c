#include <stdio.h>

int main()
{
    int n, i = 1, j;   

    printf("Digite um número: ");
    scanf("%d", &n);

    while (i <= n)
    {
        j = i;
        while (j <= (i*i))
        {
            printf("%d ", j);
            j += i;
        }
        printf("\n");
        i += 1;
    }
}