#include <stdio.h>
#include <curses.h>

int main(void)
{
  int reprovado = 0, aprovado = 0, i = 0;
  float n1, n2, media;

  while (i < 5)
  {
    printf("%dº Aluno: \n", i+1);
    printf("Nota 1: ");
    scanf("%f'", &n1);

    if (n1 > 10 || n1 < 0)
    {
      printf("Nota inválida!\n");
      continue;
    }
    else
    {
      printf("Nota 2: ");
      scanf("%f", &n2);

      if (n2 > 10 || n2 < 0)
      {
        printf("Nota inválida!\n");
        continue;
      }
      else
      {
        media = (n1 + n2) / 2;

        if (media >= 7)
        {
          printf("Média do aluno = %.1f.\nAluno aprovado!\n", media);
          aprovado++;
        }
        else
        {
          printf("Média do aluno = %.1f.\nAluno reprovado!\n", media);
          reprovado++;
        }
      }
    }
      i++;
  }

  printf("Alunos aprovados = %d.\nAlunos reprovados= %d.\n", aprovado, reprovado);

}
