#include <stdio.h>

int main()
{
    int x, soma = 0, media, i;

    printf("Digite 10 números para calcular a média:\n");

    for (i = 0; i < 10; i++)
    {
        printf("-> ");
        scanf("%d", &x);

        soma += x;
    }
    media = soma / 10;

    printf("A média é %d.\n", media);
}