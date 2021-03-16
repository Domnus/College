#include <stdio.h>

int main()
{
  int n, total = 1;

  printf("Digite um número: ");
  fflush(stdin);
  scanf("%d", &n);

  for (int i = n; i > 0; i--)
  {
    total *= i;
  }

  printf("O fatorial de %d é %d.\n", n, total);
}
