#include <stdio.h>

int main()
{
    int i;
    float nota1, nota2, media;

    for (i = 1; i < 11;)
    {
        printf("%dº Aluno | Nota 1:", i);
        scanf("%f", &nota1);
        if (nota1 > 10 || nota1 < 0)
        {
            printf("Nota inválida!\n");
            continue;
        }
        else
        {
            printf("%dº Aluno | Nota 2: ", i);
            scanf("%f", &nota2);
            if (nota2 > 10 || nota2 < 0)
            {
                printf("Nota inválida!\n");
                continue;
            }
            else
            {
                media = (nota1 + nota2) / 2;
                printf("Média: %g\n", media);
                ++i;
            }
            
        }
        
    }
}