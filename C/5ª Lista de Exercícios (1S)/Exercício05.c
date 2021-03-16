#include <stdio.h>

int main()
{
    int i, n;

    printf("Digite um número: ");
    scanf("%d", &n);

    for (i = n; i > 0; i--)
    {
        printf("%d ", i);
    }
    printf("\n");
}