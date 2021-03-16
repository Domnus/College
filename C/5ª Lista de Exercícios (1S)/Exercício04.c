#include <stdio.h>

int main()
{
    int n, i;

    printf("Digite um número: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++)
    {
        printf("%d ", i);
    }
    printf("\n");
}