#include <stdio.h>

int main()
{
  float media, idade, soma = 0, i = 0;

  do
  {

    i++;
    soma += idade;

    printf("Digite a idade (0 para parar o programa): ");
    scanf("%f", &idade);

  } while (idade != 0);

  media = soma / i;
  printf("A média das idades é: %g.\n", media);

}
