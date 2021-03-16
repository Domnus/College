#include <stdio.h>

int main()
{
  int nota;

  do
  {
    printf("Digite uma nota: ");
    fflush(stdin);
    scanf("%d", &nota);

  } while (nota > 10 || nota < 0);
}
