#include <stdio.h>

int main()
{
  int sum = 0, num, i = 1;

  printf("Digite um número: ");
  fflush(stdin);
  scanf("%d", &num);

  while (i <= num)
  {
    sum += i;
    i++;
  }

  printf("A soma dos números até %d é %d.\n", num, sum);

  return 0;
}
