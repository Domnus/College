#include <stdio.h>

int main()
{
  float IMC, altura, peso;

  printf("Informe sua altura: ");
  scanf("%f", &altura);

  printf("Informe seu peso: ");
  scanf("%f", &peso);

  IMC = peso / (altura*altura);

  printf("Seu IMC é %.2f.\n", IMC);

  if (IMC < 18)
  {
    printf("Você está abaixo do peso.\n");
  }
  else if (IMC > 18 && IMC < 25)
  {
    printf("Você está com o IMC normal.\n");
  }
  else if (IMC > 25 && IMC < 30)
  {
    printf("Você está acima do peso.\n");
  }
  else
  {
    printf("Você está fazendo cosplay de Majin Buu");
  }
}
