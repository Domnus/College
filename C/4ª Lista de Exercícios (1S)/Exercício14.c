#include <stdio.h>

int main()
{
    int soma_Impares = 0, i = 1, num;

    printf("Digite um número: ");
    scanf("%d", &num);

    while (soma_Impares < num)
    {
        soma_Impares += i;
        i += 2;
    }

    if (num == soma_Impares)
    {
        printf("Quadrado Perfeito.\n");
    }
    else
    {
        printf("Não é um quadrado perfeito.\n");
    }
}