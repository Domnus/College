#include <stdio.h>

int main()
{
    float list[5];
    int total = 0, i = 0, maior = 0, menor = 10;
    float media, nota;

    while (i < 5)
    {
        printf("Aluno %d\nNota: ", i+1);
        scanf("%f", &list[i]);
        i++;
    }

    for (i = 0; i < 5; i++)
    {
       if (list[i] > maior) 
       {
           maior = list[i];
       }
       if (list[i] < menor)
       {
           menor = list[i];
       }
    }

    printf("Maior nota: %d\nMenor nota: %d\n", maior, menor);
}
