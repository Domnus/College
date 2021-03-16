#include <stdio.h>

int main()
{
    float list[5];
    int total = 0, i = 0, maior = 0, menor = 10;
    int notasAzuis;

    while (i < 5)
    {
        printf("Aluno %d\nNota: ", i+1);
        scanf("%f", &list[i]);
        i++;
    }

    for (i = 0; i < 5; i++)
    {
       if (list[i] >= 7) 
       {
           notasAzuis++;
       }
    }

    printf("Notas azuis: %d\n", notasAzuis);
}