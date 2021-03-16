#include <stdio.h>

int main()
{
    float x, y;

    printf("Valor de x: ");
    scanf("%f", &x);

    printf("Valor de y: ");
    scanf("%f", &y);

    if (x == 0 && y == 0)
    {
        printf("Origem.\n");
    }
    else if (x == 0)
    {
        printf("Eixo X.\n");
    }
    else if (y == 0)
    {
        printf("Eixo Y.\n");
    }
    else if (x > 0 && y > 0)
    {
        printf("Quadrante 1.\n");
    }
    else if (x < 0 && y > 0)
    {
        printf("Quadrante 2.\n");
    }
    else if (x < 0 && y < 0)
    {
        printf("Quadrante 3.\n");
    }
    else if (x > 0 && y < 0)
    {
        printf("Quadrante 4.\n");
    }
}