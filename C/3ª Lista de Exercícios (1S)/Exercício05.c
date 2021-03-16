#include <stdio.h>

int main()
{
    float lab, sem, fin, media;

    printf("Trabalho de Laboratório: ");
    scanf("%f", &lab);

    printf("Avaliação Semestral: ");
    scanf("%f", &sem);

    printf("Exame final: ");
    scanf("%f", &fin);

    media = ((lab * 2.0) + (sem * 5) + (fin * 5)) / 10;
    
    printf("Média do Aluno: %g. ", media);
    if (media > 0 && media < 2.9)
    {
        printf("Aluno Reprovado.\n");
    }
    else if (media > 2.9 && media < 4.9)
    {
        printf("Aluno de Recuperação\n");
    }
    else if (media > 5 && media < 10)
    {
        printf("Aluno Aprovado.\n");
    }
}