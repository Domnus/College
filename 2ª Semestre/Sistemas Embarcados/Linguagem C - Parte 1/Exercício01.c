#include <stdio.h>

int main()
{
  int idade;

  printf("Digite a idade do nadador: ");
  scanf("%d", &idade);

  if (idade <= 8)
  {
    printf("Categoria Infantil A\n");
  }
  else if (idade < 13)
  {
    printf("Categoria Infantil B\n");
  }
  else if (idade < 18)
  {
    printf("Categoria Juvenil A\n");
  }
  else if (idade < 21)
  {
    printf("Categoria Infantil B\n");
  }
  else if (idae >= 21)
  {
    printf("Categoria Sênior\n");
  }
}
