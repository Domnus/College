#include <stdio.h>

int main()
{
    int i;
    char nome[20];

    printf("Digite um nome: ");
    scanf("%s", &nome);

    for (i = 1; i < 11; ++i)
    {
        printf("%s\n", nome);
    }
}