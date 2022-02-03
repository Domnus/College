#include <stdio.h>

int main()
{
  float angulo;

  printf("Informe o ângulo: ");
  scanf("%f", &angulo);

  if (angulo > 360)
  {
    angulo -= 360;
  }

  if (angulo <= 90)
  {
    printf("O ângulo está no Quadrante 1.\n");
  }
  else if (angulo > 90 && angulo <=180)
  {
    printf("O ângulo está no Quadrante 2.\n");
  }
  else if (angulo > 180 && angulo <= 270)
  {
    printf("O ângulo está no Quadrante 3.\n");
  }
  else if (angulo > 270 && angulo <=360)
  {
    printf("O ângulo está no Quadrante 4.\n");
  }
}
