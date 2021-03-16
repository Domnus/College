#include <stdio.h>

int main()
{
  int n, div;

  printf("Digite um número: ");
  fflush(stdin);
  scanf("%d", &n);

  printf("Divisores de %d:", n);

  for (int i = 1; i <= n; i++)
  {
    if (n % i == 0)
    {
      printf(" %d", i);
    }
  }
  printf("\n");
}
