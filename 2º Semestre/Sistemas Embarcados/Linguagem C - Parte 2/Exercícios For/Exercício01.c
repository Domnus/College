#include <stdio.h>

int main()
{
  int sum = 0, num;

  for (int i = 0; i < 10; i++)
  {
    printf("Digite um número: ");
    fflush(stdin);
    scanf("%d", &num);

    sum += num;
  }

  printf("A soma é %d.\n", sum);
}
