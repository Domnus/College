#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    srand(time(0));

    int upper = 50, lower = 1, num;
    int opcao;
    char list[10];

    for (int i = 0; i < 10; i++)
    {
        num = rand() % (upper - lower + 1) + lower;
        list[i] = num;
    }
    printf("Opção 1: Mostrar o vetor na ordem direta.\nOpção 2: Mostra o vetor na ordem inversa.\n");
    scanf("%d", &opcao);

    if (opcao == 1)   
    {
        for (int i = 0; i < 10; i++)
        {
            printf("%d ", list[i]);
        }
    }
    else if (opcao == 2)
    {
        for (int i = 10; i > 0; i--)
        {
            printf("%d ", list[i]);
        }
    }
    else 
    {
        printf("Opção inválida!");
    }
    printf("\n");
}