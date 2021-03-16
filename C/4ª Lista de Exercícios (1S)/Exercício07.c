#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int num, menor = 50, maior = 0;
    int lower = 1, upper = 50, i;
    srand(time(NULL));

    for (i = 0; i < 20; i++)
    {
        num = (rand() % (upper - lower + 1) + lower);
        printf("%d\n", num);
        if (num > maior)
        {
            maior = num;
        }
        if (num < menor)
        {
            menor = num;
        }
    }
    printf("Maior número gerado: %d\nMenor número gerado: %d.\n", maior, menor);
}