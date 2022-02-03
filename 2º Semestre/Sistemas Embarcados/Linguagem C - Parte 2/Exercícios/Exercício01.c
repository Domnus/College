#include <stdio.h>

int main()
{
    float list[5];
    int total = 0, i = 0;
    float media, nota;

    while (i < 5)
    {
        printf("Aluno %d\nNota: ", i+1);
        scanf("%f", &list[i]);
        i++;
    }

    for (i = 0; i < 5; i++)
    {
        total += list[i];
    }

    media = total / 5;

    printf("Média total da classe: %.1f.\n", media);

}
