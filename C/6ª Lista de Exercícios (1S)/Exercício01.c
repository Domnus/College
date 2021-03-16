#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main()
{
  srand(time(0));

  int par = 0, impar = 0, num, i;
  int upper = 50, lower = 0;

  for (i = 0; i < 50; i++)
  {
    num = rand() % (upper - lower + 1) + lower;

    if (num % 2 == 0)
    {
      par++;
      printf("%d é par.\n", num);
    }
    else
    {
      impar++;
      printf("%d é impar.\n", num);
    }
  }
  
  printf("Foram gerados %d números pares e %d números impares.\n", par, impar);
}